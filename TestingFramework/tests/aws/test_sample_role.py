from pathlib import Path
from src.aws.role_validator import AWSRoleValidator
import json


def test_flowlogs_role_permissions(accounts_config):
    """
    Test to validate flowlogs role permissions across all vended accounts
    """
    # Check if file exists and print its contents
    file_path = "other/roles/flowlogsRole.json"
    json_path = Path(file_path)
    
    print(f"\nChecking if file exists at: {json_path.absolute()}")
    print(f"File exists: {json_path.exists()}")
    
    if json_path.exists():
        with open(file_path, 'r') as f:
            content = f.read()
            print(f"File content length: {len(content)}")
            print("File content:")
            print(content)
            if len(content) == 0:
                print("File is empty!")
    else:
        print(f"Could not find file at {json_path.absolute()}")
        return

    """
    Test to validate flowlogs role permissions across all vended accounts
    """
    managed_accounts = accounts_config.get_managed_accounts()
    region = accounts_config.region

    for account in managed_accounts:
        account_id, account_name = account['account_id'], account['account_name']
        
        print(f"Testing flowlogs role in {account_id}:{account_name}")
        
        validator = AWSRoleValidator(account_id)
        role_name = f"{region}.{account_name}.role.flowlogsRole"

        # Let's see what policies are actually attached
        attached_policies = validator.iam.list_attached_role_policies(RoleName=role_name)
        print("\nAttached policies:")
        for policy in attached_policies['AttachedPolicies']:
            print(f"Policy Name: {policy['PolicyName']}")
            print(f"Policy ARN: {policy['PolicyArn']}")
        
        result = validator.compare_role_permissions(
            role_name,
            "other/roles/flowlogsRole.json",
            f"{region}.{account_name}.policy.flowlogsRole_policy"  # This might need to change
        )
        assert result is True