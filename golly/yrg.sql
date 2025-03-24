
config from cloud.resource where cloud.type = 'aws' AND api.name='aws-s3api-get-bucket-acl' as X; 
config from cloud.resource where cloud.type = 'aws' AND api.name='aws-organizations-account' as Y; 
filter 'X.resource.status = "Active" and 
        not (X.bucketName contains "cf-templates") and 
        not () and 
        Y.name contains "grp-rnd"'; 
show X;