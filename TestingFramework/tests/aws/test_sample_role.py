from pathlib import Path
from src.aws.role_validator import AWSRoleValidator
import json

def test_service_role_permissions(accounts_config):
    """
    Test to validate service role permissions across all vended accounts
    """
    # Load all service roles configuration
    with open("other/roles/service_roles.json", 'r') as f:
        roles_config = json.load(f)

    managed_accounts = accounts_config.get_managed_accounts()
    region = accounts_config.region

    for account in managed_accounts:
        account_id, account_name = account['account_id'], account['account_name']
        validator = AWSRoleValidator(account_id)

        for role in roles_config:
            role_name = role['role_name']
            # This path pattern is what the validator checks for
            policy_file = f"other/policies/{role_name}_policy.json"
            aws_role_name = f"{region}.{account_name}.role.{role_name}"
            
            print(f"\nTesting {role_name} in account {account_id}:{account_name}")

            result = validator.compare_role_permissions(
                aws_role_name,
                policy_file,  # Validator checks for other/policies
                aws_role_name
            )
            assert result is True, f"Policy validation failed for {role_name} in account {account_name}"
# from pathlib import Path
# from src.aws.role_validator import AWSRoleValidator
# import json

# def test_flowlogs_role_permissions(accounts_config):
#     """
#     Test to validate flowlogs role permissions across all vended accounts
#     """
#     # Load the roles configuration
#     roles_file = "other/roles/flowlogsRole.json"
#     with open(roles_file, 'r') as f:
#         roles_config = json.load(f)

#     # For now, just get the flowlogs role
#     flowlogs_role = next(role for role in roles_config if role['role_name'] == 'flowlogsRole')
    
#     # Construct path to the corresponding policy
#     policy_file = f"other/policies/{flowlogs_role['role_name']}_policy.json"
    
#     print(f"\nTesting role: {flowlogs_role['role_name']}")
#     print(f"Using policy file: {policy_file}")

#     managed_accounts = accounts_config.get_managed_accounts()
#     region = accounts_config.region

#     for account in managed_accounts:
#         account_id, account_name = account['account_id'], account['account_name']
        
#         print(f"\nTesting in account {account_id}:{account_name}")
        
#         validator = AWSRoleValidator(account_id)
#         role_name = f"{region}.{account_name}.role.{flowlogs_role['role_name']}"

#         # The validator will handle the inline policy checking
#         result = validator.compare_role_permissions(
#             role_name,
#             policy_file,
#             role_name  # For inline policies, we don't need a specific policy name
#         )
#         assert result is True, f"Policy validation failed for {flowlogs_role['role_name']} in account {account_name}"
