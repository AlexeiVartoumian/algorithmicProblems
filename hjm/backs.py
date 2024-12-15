import boto3
import os
import json
from botocore.exceptions import ClientError

def assume_control_tower_role(account_id):
    """
    Assume the AWSControlTowerExecution role in AFT account
    """
    sts = boto3.client('sts')
    role_arn = f'arn:aws:iam::{account_id}:role/AWSControlTowerExecution'
    
    assumed_role = sts.assume_role(
        RoleArn=role_arn,
        RoleSessionName='BackupVaultSync'
    )
    
    return assumed_role['Credentials']

def get_aft_backup_client():
    """
    Get a backup client for the AFT account
    """
    aft_account_id = os.environ['AFT_ACCOUNT_ID']
    credentials = assume_control_tower_role(aft_account_id)
    
    return boto3.client(
        'backup',
        aws_access_key_id=credentials['AccessKeyId'],
        aws_secret_access_key=credentials['SecretAccessKey'],
        aws_session_token=credentials['SessionToken']
    )

def create_backup_vault_if_not_exists(backup_client, vault_name):
    """
    Create backup vault if it doesn't exist
    """
    try:
        backup_client.describe_backup_vault(
            BackupVaultName=vault_name
        )
        print(f"Backup vault {vault_name} already exists")
    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceNotFoundException':
            try:
                backup_client.create_backup_vault(
                    BackupVaultName=vault_name,
                    Tags={
                        'CreatedBy': 'ControlTowerBackupSync',
                        'SourceAccount': os.environ['AFT_ACCOUNT_ID']
                    }
                )
                print(f"Created backup vault: {vault_name}")
            except Exception as create_error:
                print(f"Error creating backup vault: {str(create_error)}")
                raise
        else:
            raise

def lambda_handler(event, context):
    """
    Lambda handler that processes backup events and ensures vault exists
    """
    # Get clients
    mgmt_backup = boto3.client('backup')
    aft_backup = get_aft_backup_client()
    
    # Get vault names from environment
    source_vault_name = os.environ['AFT_VAULT_NAME']
    mgmt_vault_name = os.environ['MGMT_VAULT_NAME']
    
    # Ensure vault exists in management account
    create_backup_vault_if_not_exists(mgmt_backup, mgmt_vault_name)
    
    # If this is a backup completion event, copy the recovery point
    if 'detail' in event and event['detail'].get('state') == 'COMPLETED':
        recovery_point_arn = event['detail']['recoveryPointArn']
        aft_account_id = os.environ['AFT_ACCOUNT_ID']
        
        try:
            mgmt_backup.copy_recovery_point(
                SourceBackupVaultName=source_vault_name,
                SourceRecoveryPointArn=recovery_point_arn,
                DestinationBackupVaultName=mgmt_vault_name,
                IamRoleArn=f'arn:aws:iam::{aft_account_id}:role/AWSControlTowerExecution'
            )
            print(f"Initiated copy of recovery point: {recovery_point_arn}")
        except Exception as e:
            print(f"Error copying recovery point: {str(e)}")
            raise
    
    return {
        'statusCode': 200,
        'body': json.dumps('Backup sync operation completed')
    }