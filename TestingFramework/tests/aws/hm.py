from pathlib import Path
from src.aws.role_validator import AWSRoleValidator
import json

def test_flowlogs_role_permissions(accounts_config):
    managed_accounts = accounts_config.get_managed_accounts()
    region = accounts_config.region

    for account in managed_accounts:
        account_id, account_name = account['account_id'], account['account_name']
        
        print(f"\nTesting flowlogs role in {account_id}:{account_name}")
        
        validator = AWSRoleValidator(account_id)
        role_name = f"{region}.{account_name}.role.flowlogsRole"

        # Let's list all roles and look for something similar to flowlogs
        print("\nListing roles:")
        roles = validator.iam.list_roles()
        for role in roles['Roles']:
            if 'flow' in role['RoleName'].lower():  # Look for any role with 'flow' in the name
                print(f"Found potential flowlogs role: {role['RoleName']}")
                print(f"Role ARN: {role['Arn']}")
                
                # Check policies for this role
                attached = validator.iam.list_attached_role_policies(RoleName=role['RoleName'])
                print(f"Attached policies for {role['RoleName']}:")
                for policy in attached['AttachedPolicies']:
                    print(f"- {policy['PolicyName']}")



def test_flowlogs_role_permissions(accounts_config):
    managed_accounts = accounts_config.get_managed_accounts()
    region = accounts_config.region

    for account in managed_accounts:
        account_id, account_name = account['account_id'], account['account_name']
        
        validator = AWSRoleValidator(account_id)
        role_name = f"{region}.{account_name}.role.flowlogsRole"

        print(f"\nChecking flowlogs role in {account_id}:{account_name}")
        print(f"Looking for role: {role_name}")
        
        # Get and print ALL policies attached to this role
        attached_policies = validator.iam.list_attached_role_policies(RoleName=role_name)
        print("\nAll attached policies for this role:")
        for policy in attached_policies['AttachedPolicies']:
            print(f"Found policy:")
            print(f"  Name: {policy['PolicyName']}")
            print(f"  ARN: {policy['PolicyArn']}")
        
        # Print what policy name we're searching for
        expected_policy = f"{region}.{account_name}.policy.flowlogsRole_policy"
        print(f"\nExpecting to find policy named: {expected_policy}")

        # Now try the comparison
        result = validator.compare_role_permissions(
            role_name,
            "other/roles/flowlogsRole.json",
            expected_policy
        )
        assert result is True, "Policy validation failed"