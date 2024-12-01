from pathlib import Path
from src.aws.role_validator import AWSRoleValidator
import json


from pathlib import Path
from src.aws.role_validator import AWSRoleValidator
import json

def test_flowlogs_role_permissions(accounts_config):
    """
    Test to validate flowlogs role permissions across all vended accounts
    """
    # Verify our test policy file exists and is valid
    file_path = "other/policies/flowlogsRole_policy.json"
    json_path = Path(file_path)
    
    print(f"\nChecking if policy file exists at: {json_path.absolute()}")
    if not json_path.exists():
        print(f"Could not find policy file at {json_path.absolute()}")
        return

    managed_accounts = accounts_config.get_managed_accounts()
    region = accounts_config.region

    for account in managed_accounts:
        account_id, account_name = account['account_id'], account['account_name']
        
        print(f"\nTesting flowlogs role in {account_id}:{account_name}")
        
        validator = AWSRoleValidator(account_id)
        role_name = f"{region}.{account_name}.role.flowlogsRole"

        # The validator will automatically handle inline policy checking
        result = validator.compare_role_permissions(
            role_name,
            file_path,  # Point to the policy file, not the role file
            role_name   # For inline policies, the role name is sufficient
        )
        assert result is True, f"Policy validation failed for flowlogs role in account {account_name}"