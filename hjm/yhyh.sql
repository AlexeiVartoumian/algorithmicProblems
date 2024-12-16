-- Basic query to examine usernames for common PII patterns
SELECT DISTINCT useridentity.username,
       eventtime,
       eventname,
       sourceipaddress
FROM cloudtrail_logs
WHERE useridentity.username REGEXP '(?i)(^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$)' -- Email addresses
   OR useridentity.username REGEXP '\d{3}[-.]?\d{2}[-.]?\d{4}' -- SSN-like patterns
   OR useridentity.username REGEXP '\b\d{10,16}\b' -- Possible phone numbers or account numbers
   OR useridentity.username REGEXP '(?i)(password|secret|key|token|pwd|credential)'
ORDER BY eventtime DESC;

-- Query to find usernames containing name-like patterns
SELECT DISTINCT useridentity.username,
       COUNT(*) as occurrence_count
FROM cloudtrail_logs
WHERE useridentity.username REGEXP '[A-Z][a-z]+\s+[A-Z][a-z]+' -- First Last name pattern
GROUP BY useridentity.username
HAVING COUNT(*) > 1
ORDER BY occurrence_count DESC;

-- Query to analyze username patterns across regions
SELECT aws_region,
       useridentity.username,
       COUNT(*) as action_count
FROM cloudtrail_logs
WHERE useridentity.username REGEXP '(?i)(^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$)'
   OR useridentity.username REGEXP '\d{3}[-.]?\d{2}[-.]?\d{4}'
GROUP BY aws_region, useridentity.username
ORDER BY action_count DESC;

-- Query to identify potentially sensitive actions by users with PII in username
SELECT useridentity.username,
       eventname,
       COUNT(*) as action_count
FROM cloudtrail_logs
WHERE (useridentity.username REGEXP '(?i)(^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$)'
   OR useridentity.username REGEXP '\d{3}[-.]?\d{2}[-.]?\d{4}')
AND eventname LIKE '%Secret%'
   OR eventname LIKE '%Password%'
   OR eventname LIKE '%Credential%'
   OR eventname LIKE '%Key%'
GROUP BY useridentity.username, eventname
ORDER BY action_count DESC;