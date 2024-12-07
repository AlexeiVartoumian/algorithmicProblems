#!/bin/bash

aws cloudtrail create-trail \
  --name org-cloudtrail \
  --s3-bucket-name aws-custom-cloud-trail-logs-654654622351 \
  --is-organization-trail \
  --is-multi-region-trail \
  --cloud-watch-logs-log-group-arn GET THIS FROM CLOUDFORMATION TEMPLATE CLOUDWATCH.YML \
  --cloud-watch-logs-role-arn GET THIS FROM CLOUDFORMATION TEMPLATE CLOUDWATCH.YML
aws cloudtrail start-logging --name org-cloudtrail
aws cloudtrail stop-logging --name org-cloudtrail

//https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-delegated-administrator.html
