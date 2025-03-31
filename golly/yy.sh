#!/bin/bash

# Set variables
LOG_GROUP_NAME="/ec2/commands-output"
INSTANCE_ID=$(curl -s http://169.254.169.254/latest/meta-data/instance-id)
LOG_STREAM_NAME="command-output-${INSTANCE_ID}"
REGION=$(curl -s http://169.254.169.254/latest/meta-data/placement/region)

# Install CloudWatch agent
yum update -y
yum install -y amazon-cloudwatch-agent

# Create CloudWatch agent configuration
cat > /opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json << 'EOF'
{
  "agent": {
    "run_as_user": "root"
  },
  "logs": {
    "logs_collected": {
      "files": {
        "collect_list": [
          {
            "file_path": "/var/log/command-output.log",
            "log_group_name": "${LOG_GROUP_NAME}",
            "log_stream_name": "${LOG_STREAM_NAME}",
            "timezone": "UTC"
          }
        ]
      }
    },
    "force_flush_interval": 5
  }
}
EOF

# Replace variables in the config file
sed -i "s|\${LOG_GROUP_NAME}|${LOG_GROUP_NAME}|g" /opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json
sed -i "s|\${LOG_STREAM_NAME}|${LOG_STREAM_NAME}|g" /opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json

# Start CloudWatch agent
/opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -s -c file:/opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json

# Make sure log file exists
touch /var/log/command-output.log
chmod 644 /var/log/command-output.log

# Create a function to run commands and log their output
run_and_log() {
  command="$1"
  echo "Running command: $command" >> /var/log/command-output.log
  echo "==================== OUTPUT START ====================" >> /var/log/command-output.log
  
  # Execute the command directly instead of using eval
  # This is safer as it avoids potential shell injection issues
  bash -c "$command" >> /var/log/command-output.log 2>&1
  exit_code=$?
  
  echo "==================== OUTPUT END ====================" >> /var/log/command-output.log
  echo "Exit code: $exit_code" >> /var/log/command-output.log
  echo "" >> /var/log/command-output.log
}

# Verify the CloudWatch agent is running
run_and_log "systemctl status amazon-cloudwatch-agent"

# Install and configure Python and other packages
run_and_log "echo 'Starting package installations and configurations'"
run_and_log "yum update -y"

# Python installation and setup
run_and_log "echo 'Installing Python and dependencies'"
run_and_log "yum install -y python3 python3-pip python3-devel gcc"
run_and_log "alternatives --set python /usr/bin/python3"
run_and_log "python --version"
run_and_log "pip3 --version"

# Install common Python packages
run_and_log "echo 'Installing Python packages'"
run_and_log "pip3 install boto3 requests pymysql"

# System configuration checks
run_and_log "echo 'Running system checks'"
run_and_log "hostnamectl"
run_and_log "free -m"
run_and_log "df -h"
run_and_log "systemctl status amazon-cloudwatch-agent"

# Network configuration and checks
run_and_log "echo 'Running network checks'"
run_and_log "ip addr show"
run_and_log "netstat -tulpn"

# Install and configure additional tools as needed
run_and_log "echo 'Installing additional tools'"
run_and_log "yum install -y wget git jq"

# Deploy application or run tests (customize as needed)
run_and_log "echo 'Setting up application environment'"
run_and_log "mkdir -p /app"
run_and_log "cd /app && echo 'Application directory created' > app_setup.log"

# Execute Python code and capture output
run_and_log "echo 'Running Python code snippets'"

# Method 1: Run Python directly with the -c flag
run_and_log "python3 -c 'print(\"Hello World from Python one-liner!\")'"

# Method 2: Create and execute a Python script
cat > /tmp/test_script.py << 'EOF'
#!/usr/bin/env python3

import sys
import platform
import datetime

print("Hello World from Python script!")
print(f"Python version: {sys.version}")
print(f"Platform: {platform.platform()}")
print(f"Current time: {datetime.datetime.now()}")

# Sample calculation
total = 0
for i in range(1, 11):
    total += i
    print(f"Adding {i}, new total: {total}")

print("Script completed successfully!")
EOF

# Make the script executable and run it
run_and_log "chmod +x /tmp/test_script.py"
run_and_log "python3 /tmp/test_script.py"

# Method 3: Execute Python code that interacts with AWS
cat > /tmp/aws_test.py << 'EOF'
#!/usr/bin/env python3

import boto3
import json

try:
    # Get instance metadata
    session = boto3.Session()
    ec2 = session.client('ec2')
    
    # Get instance ID from metadata service
    import requests
    instance_id = requests.get('http://169.254.169.254/latest/meta-data/instance-id', timeout=2).text
    
    # Get instance details
    response = ec2.describe_instances(InstanceIds=[instance_id])
    
    print(f"Instance ID: {instance_id}")
    print(f"Instance Type: {response['Reservations'][0]['Instances'][0]['InstanceType']}")
    print(f"Launch Time: {response['Reservations'][0]['Instances'][0]['LaunchTime']}")
    
    # List all available regions
    regions = [region['RegionName'] for region in ec2.describe_regions()['Regions']]
    print(f"Available AWS regions: {', '.join(regions)}")
    
except Exception as e:
    print(f"Error occurred: {e}")
EOF

run_and_log "python3 /tmp/aws_test.py"

# Verify that logs are being sent to CloudWatch
run_and_log "echo 'Checking CloudWatch agent logs'"
run_and_log "cat /opt/aws/amazon-cloudwatch-agent/logs/amazon-cloudwatch-agent.log"

# Final verification
run_and_log "echo 'Log file contents:'"
run_and_log "ls -la /var/log/command-output.log"
run_and_log "echo 'User data script execution completed'"