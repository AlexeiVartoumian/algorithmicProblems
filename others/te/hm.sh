#!/bin/bash

# Configuration
ROLE_NAME="AWSControlTowerExecution"
OUTPUT_DIR="account_vpc_results"
PYTHON_SCRIPT="find_default_vpcs.py" 
SUMMARY_FILE="all_accounts_summary.csv"


mkdir -p $OUTPUT_DIR


echo "AccountID,AccountName,ScriptExecutionStatus" > $SUMMARY_FILE


if [ ! -f "$PYTHON_SCRIPT" ]; then
    echo "Error: Python script $PYTHON_SCRIPT not found!"
    exit 1
fi

# Get list of all accounts in organization
echo "Listing all accounts in the organization..."
ACCOUNTS=$(aws organizations list-accounts --query 'Accounts[?Status==`ACTIVE`].[Id,Name]' --output json)


TOTAL_ACCOUNTS=$(echo $ACCOUNTS | jq length)
echo "Found $TOTAL_ACCOUNTS accounts"

# Process each account
ACCOUNT_COUNT=0
echo $ACCOUNTS | jq -c '.[]' | while read -r account; do
    ACCOUNT_COUNT=$((ACCOUNT_COUNT+1))
    
    account_id=$(echo $account | jq -r '.[0]')
    account_name=$(echo $account | jq -r '.[1]' | sed 's/ /_/g')
    
    echo "[$ACCOUNT_COUNT/$TOTAL_ACCOUNTS] Processing account: $account_name ($account_id)"
    
    echo "  Assuming role in account..."
    CREDENTIALS=$(aws sts assume-role \
        --role-arn "arn:aws:iam::${account_id}:role/${ROLE_NAME}" \
        --role-session-name "VpcFinder" \
        --query 'Credentials.[AccessKeyId,SecretAccessKey,SessionToken]' \
        --output text)
    
    if [ $? -ne 0 ]; then
        echo "  Failed to assume role in account $account_id. Skipping."
        echo "$account_id,$account_name,ROLE_ASSUMPTION_FAILED" >> $SUMMARY_FILE
        continue
    fi
    
    # Set temporary credentials as environment variables
    export AWS_ACCESS_KEY_ID=$(echo $CREDENTIALS | awk '{print $1}')
    export AWS_SECRET_ACCESS_KEY=$(echo $CREDENTIALS | awk '{print $2}')
    export AWS_SESSION_TOKEN=$(echo $CREDENTIALS | awk '{print $3}')
    
    # Create an account-specific output file
    OUTPUT_FILE="${OUTPUT_DIR}/${account_id}_${account_name}_vpcs.txt"
    
    # Execute the Python script with the temporary credentials
    echo "  Executing Python script..."
    python $PYTHON_SCRIPT > $OUTPUT_FILE 2>&1
    
    if [ $? -eq 0 ]; then
        echo "  Script executed successfully for account $account_id"
        echo "$account_id,$account_name,SUCCESS" >> $SUMMARY_FILE
    else
        echo "  Script execution failed for account $account_id"
        echo "$account_id,$account_name,SCRIPT_EXECUTION_FAILED" >> $SUMMARY_FILE
    fi
    
    
    unset AWS_ACCESS_KEY_ID
    unset AWS_SECRET_ACCESS_KEY
    unset AWS_SESSION_TOKEN
    
    
    sleep 1
done

echo "Complete! Results for each account are in the $OUTPUT_DIR directory"
echo "Summary of execution is available in $SUMMARY_FILE"