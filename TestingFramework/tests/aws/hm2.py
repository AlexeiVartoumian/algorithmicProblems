from pathlib import Path
from src.aws.role_validator import AWSRoleValidator
import json

def test_additional_role_permissions(accounts_config):
    managed_accounts = accounts_config.get_managed_accounts()
    region = accounts_config.region

    # Load the roles we want to test
    with open("other/roles/flowlogsRole.json", 'r') as f:
        roles_to_test = json.load(f)  # Now loads an array of roles

    for account in managed_accounts:
        account_id, account_name = account['account_id'], account['account_name']
        validator = AWSRoleValidator(account_id)

        # Test each role in our list
        for role_entry in roles_to_test:
            role_name = role_entry if isinstance(role_entry, str) else role_entry["role_name"]
            aws_role_name = f"{region}.{account_name}.role.{role_name}"
            
            print(f"\nTesting {role_name} in {account_id}:{account_name}")
            
            # Verify role exists
            try:
                validator.iam.get_role(RoleName=aws_role_name)
                print(f"Found role: {aws_role_name}")
                
                # Now do the policy comparison
                result = validator.compare_role_permissions(
                    aws_role_name,
                    f"other/policies/{role_name}_policy.json",
                    f"{region}.{account_name}.policy.{role_name}_policy"
                )
                assert result is True, f"Policy validation failed for {role_name} in account {account_name}"
                
            except validator.iam.exceptions.NoSuchEntityException:
                print(f"Role {aws_role_name} does not exist in account {account_name}")
                assert False, f"Role {role_name} not found in account {account_name}"