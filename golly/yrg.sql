


config from cloud.resource where cloud.type = 'aws' AND api.name='aws-s3api-get-bucket-acl' and resource.status = Active and (json.rule='bucketName does not contain "cf-templates" and ) as X; 
config from cloud.resource where cloud.type = 'aws' AND api.name='aws-organizations-account' and (json.rule = name contains "grp-rnd") as Y; 
filter '$.X.accountId == $.Y.accountId'; 
show X;