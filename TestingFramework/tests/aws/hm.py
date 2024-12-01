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
                
                policy_name = None  # Initialize before the loop
                for policy in attached['AttachedPolicies']:
                    print(f"- {policy['PolicyName']}")
                    policy_name = policy['PolicyName']  # Capture the policy name
                
                if policy_name:  # Only try comparison if we found a policy
                    result = validator.compare_role_permissions(
                        role['RoleName'],
                        "other/policies/flowlogsRole_policy.json",
                        policy_name
                    )
                    assert result is True, f"Policy validation failed for {role['RoleName']}"
                else:
                    print("No policies found attached to this role")
                break