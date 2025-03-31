#!/bin/bash

# Define variables
LOG_GROUP_NAME="/ec2/userdata-logs"
INSTANCE_ID=$(curl -s http://169.254.169.254/latest/meta-data/instance-id)
LOG_STREAM_NAME="userdata-${INSTANCE_ID}"
REGION=$(curl -s http://169.254.169.254/latest/meta-data/placement/region)


log_to_cloudwatch() {
  local command="$1"
  local output
  local timestamp
  
  echo "Executing: $command"
  timestamp=$(date +%s000)
  output=$(bash -c "$command" 2>&1)
  echo "$output"
  
 
  aws logs put-log-events \
    --log-group-name "$LOG_GROUP_NAME" \
    --log-stream-name "$LOG_STREAM_NAME" \
    --log-events timestamp=$timestamp,message="Command: $command
Output: $output" \
    --region "$REGION"
}


if ! command -v aws &> /dev/null; then
  echo "Installing AWS CLI..."
  apt-get update -y || yum update -y
  apt-get install -y unzip || yum install -y unzip
  curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
  unzip awscliv2.zip
  ./aws/install
fi


aws logs create-log-group --log-group-name "$LOG_GROUP_NAME" --region "$REGION" || true


aws logs create-log-stream --log-group-name "$LOG_GROUP_NAME" --log-stream-name "$LOG_STREAM_NAME" --region "$REGION" || true

log_to_cloudwatch "apt-get update -y || yum update -y"
log_to_cloudwatch "apt-get install -y amazon-cloudwatch-agent || yum install -y amazon-cloudwatch-agent"


cat > /opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json << 'EOF'
{
  "agent": {
    "metrics_collection_interval": 60,
    "run_as_user": "root"
  },
  "logs": {
    "logs_collected": {
      "files": {
        "collect_list": [
          {
            "file_path": "/var/log/cloud-init-output.log",
            "log_group_name": "/ec2/userdata-logs",
            "log_stream_name": "cloud-init-{instance_id}",
            "timezone": "UTC"
          }
        ]
      }
    }
  }
}
EOF

log_to_cloudwatch "systemctl start amazon-cloudwatch-agent || service amazon-cloudwatch-agent start"
log_to_cloudwatch "systemctl enable amazon-cloudwatch-agent || chkconfig amazon-cloudwatch-agent on"


log_to_cloudwatch "df -h"
log_to_cloudwatch "free -m"
log_to_cloudwatch "w"



echo "UserData script completed"