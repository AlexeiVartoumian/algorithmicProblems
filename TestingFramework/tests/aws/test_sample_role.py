from pathlib import Path
from src.aws.role_validator import AWSRoleValidator
import json

def test_flowlogs_role_permissions(accounts_config):
    """
    Test to validate flowlogs role permissions across all vended accounts
    """
    # Load and print the roles configuration for debugging
    roles_file = "other/roles/flowlogsRole.json"
    with open(roles_file, 'r') as f:
        roles_config = json.load(f)
        print("\nRoles config content:")
        print(roles_config)

    policy_file = "other/policies/flowlogsRole_policy.json"
    print(f"\nUsing policy file: {policy_file}")

    managed_accounts = accounts_config.get_managed_accounts()
    region = accounts_config.region

    for account in managed_accounts:
        account_id, account_name = account['account_id'], account['account_name']
        
        print(f"\nTesting in account {account_id}:{account_name}")
        
        validator = AWSRoleValidator(account_id)
        role_name = f"{region}.{account_name}.role.flowlogsRole"

        # Check what inline policies exist
        print(f"\nChecking inline policies for role: {role_name}")
        try:
            inline_policies = validator.iam.list_role_policies(RoleName=role_name)
            print("Inline policies found:")
            for policy_name in inline_policies['PolicyNames']:
                print(f"- {policy_name}")
                # Get and print the policy document
                policy_doc = validator.iam.get_role_policy(
                    RoleName=role_name,
                    PolicyName=policy_name
                )
                print(f"Policy document: {json.dumps(policy_doc['PolicyDocument'], indent=2)}")
        except Exception as e:
            print(f"Error checking inline policies: {str(e)}")

        # Now try the validation
        result = validator.compare_role_permissions(
            role_name,
            policy_file,
            role_name
        )
        assert result is True, f"Policy validation failed for flowlogsRole in account {account_name}"
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
