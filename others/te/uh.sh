#!/bin/bash
# Script to delete existing user (if present) and create a new AWS IAM admin user

# Set variables
USERNAME=""
PASSWORD=""
POLICY_ARN="arn:aws:iam::aws:policy/AdministratorAccess"
ACCOUNT_ID=$(aws sts get-caller-identity --query "Account" --output text)
CONSOLE_URL="https://${ACCOUNT_ID}.signin.aws.amazon.com/console"

# Delete the user if it exists
echo "Checking if user ${USERNAME} already exists..."
if aws iam get-user --user-name ${USERNAME} >/dev/null 2>&1; then
  echo "User ${USERNAME} exists. Deleting..."
  
  # Check if login profile exists and delete it
  if aws iam get-login-profile --user-name ${USERNAME} >/dev/null 2>&1; then
    echo "Deleting login profile..."
    aws iam delete-login-profile --user-name ${USERNAME}
  fi
  
  # List and detach all policies
  echo "Detaching policies..."
  for policy in $(aws iam list-attached-user-policies --user-name ${USERNAME} --query "AttachedPolicies[].PolicyArn" --output text); do
    echo "Detaching policy: ${policy}"
    aws iam detach-user-policy --user-name ${USERNAME} --policy-arn ${policy}
  done
  
  # Delete the user
  echo "Deleting user..."
  aws iam delete-user --user-name ${USERNAME}
  echo "User ${USERNAME} has been deleted."
else
  echo "User ${USERNAME} does not exist. Proceeding with creation."
fi

# Create the user
echo "Creating IAM user: ${USERNAME}..."
aws iam create-user --user-name ${USERNAME}

# Attach the AdministratorAccess policy
echo "Attaching AdministratorAccess policy..."
aws iam attach-user-policy --user-name ${USERNAME} --policy-arn ${POLICY_ARN}

# Create login profile with password that doesn't require reset
echo "Setting up login profile with initial password..."
aws iam create-login-profile --user-name ${USERNAME} --password "${PASSWORD}" --password-reset-required false

# Verify console access is enabled
echo "Verifying console access..."
if aws iam get-login-profile --user-name ${USERNAME} >/dev/null 2>&1; then
  echo "Console access successfully enabled."
else
  echo "ERROR: Failed to enable console access. Please check for errors above."
  exit 1
fi

# Output the credentials
echo ""
echo "===================================================="
echo "            AWS ADMIN USER CREDENTIALS              "
echo "===================================================="
echo "Username: ${USERNAME}"
echo "Password: ${PASSWORD}"
echo "Console URL: ${CONSOLE_URL}"
echo "===================================================="
echo ""
echo "IMPORTANT: Store these credentials securely!"