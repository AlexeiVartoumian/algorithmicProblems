-- Basic query to examine usernames for common PII patterns
SELECT DISTINCT useridentity.username,
       eventtime,
       eventname,
       sourceipaddress
FROM cloudtrail_logs
WHERE 
    -- Email-like patterns
    useridentity.username LIKE '%@%.%'
    -- Looking for numeric patterns that might be SSN-like
    OR (
        LENGTH(REGEXP_REPLACE(useridentity.username, '[^0-9]', '')) >= 9 
        AND LENGTH(REGEXP_REPLACE(useridentity.username, '[^0-9]', '')) <= 11
    )
    -- Looking for sensitive keywords
    OR LOWER(useridentity.username) LIKE '%password%'
    OR LOWER(useridentity.username) LIKE '%secret%'
    OR LOWER(useridentity.username) LIKE '%key%'
    OR LOWER(useridentity.username) LIKE '%token%'
    OR LOWER(useridentity.username) LIKE '%pwd%'
    OR LOWER(useridentity.username) LIKE '%credential%'
ORDER BY eventtime DESC;

-- Query to analyze username patterns across regions
SELECT aws_region,
       useridentity.username,
       COUNT(*) as action_count
FROM cloudtrail_logs
WHERE 
    useridentity.username LIKE '%@%.%'
    OR (
        LENGTH(REGEXP_REPLACE(useridentity.username, '[^0-9]', '')) >= 9
        AND LENGTH(REGEXP_REPLACE(useridentity.username, '[^0-9]', '')) <= 11
    )
GROUP BY aws_region, useridentity.username
ORDER BY action_count DESC;

-- Query to identify potentially sensitive actions
SELECT useridentity.username,
       eventname,
       COUNT(*) as action_count
FROM cloudtrail_logs
WHERE (
    useridentity.username LIKE '%@%.%'
    OR LENGTH(REGEXP_REPLACE(useridentity.username, '[^0-9]', '')) >= 9
)
AND (
    eventname LIKE '%Secret%'
    OR eventname LIKE '%Password%'
    OR eventname LIKE '%Credential%'
    OR eventname LIKE '%Key%'
)
GROUP BY useridentity.username, eventname
ORDER BY action_count DESC;


-- Basic query to get all Service Catalog related events
SELECT 
    eventtime,
    eventname,
    useridentity.username,
    sourceipaddress,
    awsregion,
    requestparameters,
    responseelements
FROM cloudtrail_logs
WHERE 
    eventsource = 'servicecatalog.amazonaws.com'
ORDER BY eventtime DESC
LIMIT 1000;

-- Query to focus on specific Service Catalog actions that might contain sensitive info
SELECT 
    eventtime,
    eventname,
    useridentity.username,
    requestparameters
FROM cloudtrail_logs
WHERE 
    eventsource = 'servicecatalog.amazonaws.com'
    AND eventname IN (
        'CreatePortfolio',
        'CreateProduct',
        'CreateProvisioningArtifact',
        'UpdateProduct',
        'UpdateProvisioningArtifact',
        'UpdatePortfolio',
        'ProvisionProduct',
        'UpdateProvisionedProduct'
    )
ORDER BY eventtime DESC
LIMIT 1000;



ALTER TABLE cloudtrail_logs_partitioned ADD
PARTITION (year='2024', month='01', day='01') 
LOCATION 's3://your-bucket/AWSLogs/your-account-id/CloudTrail/region/year=2024/month=01/day=01/'
PARTITION (year='2024', month='01', day='02') 
LOCATION 's3://your-bucket/AWSLogs/your-account-id/CloudTrail/region/year=2024/month=01/day=02/'
PARTITION (year='2024', month='01', day='03') 
LOCATION 's3://your-bucket/AWSLogs/your-account-id/CloudTrail/region/year=2024/month=01/day=03/';