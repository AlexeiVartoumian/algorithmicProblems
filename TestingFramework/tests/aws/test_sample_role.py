from src.aws.role_validator import AWSRoleValidator
import json

def test_flowlogs_role_permissions(accounts_config):
    """
    Test to validate flowlogs role permissions across all vended accounts
    """
    managed_accounts = accounts_config.get_managed_accounts()
    region = accounts_config.region

    for account in managed_accounts:
        account_id, account_name = account['account_id'], account['account_name']
        
        print(f"Testing flowlogs role in {account_id}:{account_name}")
        
        validator = AWSRoleValidator(account_id)
        
        # Test flowlogs role specifically
        result = validator.compare_role_permissions(
            f"{region}.{account_name}.role.flowlogsRole",
            "other/roles/flowlogsRole.json",
            f"{region}.{account_name}.policy.flowlogsRole_policy"
        )
        assert result is True, f"Flowlogs role validation failed for account {account_name}"