#!/bin/bash
# Script to create an AWS IAM admin user

# Set variables
USERNAME=""
PASSWORD=""
POLICY_ARN="arn:aws:iam::aws:policy/AdministratorAccess"
ACCOUNT_ID=$(aws sts get-caller-identity --query "Account" --output text)
CONSOLE_URL="https://${ACCOUNT_ID}.signin.aws.amazon.com/console"

# Create the user
echo "Creating IAM user: ${USERNAME}..."
aws iam create-user --user-name ${USERNAME}

# Attach the AdministratorAccess policy
echo "Attaching AdministratorAccess policy..."
aws iam attach-user-policy --user-name ${USERNAME} --policy-arn ${POLICY_ARN}

# Create login profile with password that doesn't require reset
echo "Setting up login profile with initial password..."
aws iam create-login-profile --user-name ${USERNAME} --password ${PASSWORD} --password-reset-required false

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