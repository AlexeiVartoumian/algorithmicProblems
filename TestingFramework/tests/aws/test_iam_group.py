import pytest
from src.aws.role_manager import AWSRoleManager


import json

def test_iam_group(accounts_config):

    region = accounts_config.region
    managed_accounts = accounts_config.get_managed_accounts()

    for account in managed_accounts:
        account_id , account_name = account['account_id'] , account['account_name']

        print(f"{account_id}: {account_name}")

        role_manager = AWSRoleManager(account_id)
        session = role_manager.assume_role()

        iam = session.client('iam')

        group_name = f"{region}.{account_name}.group.aws.admin"
        response = iam.get_group(GroupName = group_name)
        print(response)

        assert group_name in response ["Group"]["GroupName"]