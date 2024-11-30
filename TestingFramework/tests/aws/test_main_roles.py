from src.aws.role_validator import AWSRoleValidator
import json

def test_compare_role_permissions(accounts_config):

    managed_accounts = accounts_config.get_maanged_accounts()
    region = accounts_config.region

    for account in managed_accounts:
        account_id , account_name = account['account_id'], account['account_name']
        account_roles = accounts_config.get_account_roles(account_name)

        print(f"{account_id}:{account_name}")

        validator = AWSRoleValidator(account_id)
        for role_name in account_roles:
            
            role_config = accounts_config.get_roles_config_entry(role_name)

            for policy_entry in role_config['policy_files']:
                print(f"\t{role_name}:{policy_entry['policy_name']}")
                result = validator.compare_role_permissions(
                    f"{region}.{account_name}.role.{role_name}"
                    f"{accounts_config.base_config_path}/json/{policy_entry['policy_file']}",
                    f"{region}.{account_name}.policy.{policy_entry['policy_name']}"
                )
                assert result is True
    