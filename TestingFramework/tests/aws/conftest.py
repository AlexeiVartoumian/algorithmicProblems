import pytest
import boto3
import json
from pathlib import Path
from typing import Dict , List , Any
import logging


class AccountsConfig:

    def __init__(self , environment=''):
    
        #this might have to be exteneded for future customizations outside of Iam-roles
        self.base_config_path= 'aft-global-customization/terraform/iam-user-roles-interface'

        #all vended account metadata is stored in dynamodb tables in the aft management account
        self.account_data = self.retrieve_managed_accounts_from_dynamo()
        self.region = "eu-west-1"

        #way to go would be to add additional reads 
        with open(f'{self.base_config_path}/config{environment}/json' ,'r') as f:
            self.config = json.load(f)
        
        with open(f'{self.base_config_path}/json/roles.json' , 'r') as r:
            self.roles_config = json.load(r)
        

    def get_account_roles(self, account_name):
        return self.config['AccountGroups'].get(account_name, [])

    def get_roles_config_entry(self,role_name):
        
        for roles_entry in self.roles_config:
            if roles_entry['role_name'] == role_name:
                return roles_entry
    
    def retrieve_manage_accounts_from_dynamo(self):

        dynamodb = boto3.resource('dyanomodb')

        metadata_table = dynamodb.Table('aft-request-metadata')
        request_table = dynamodb.Table('aft-request')

        metadata_response = metadata_table.scan(ProjectionExpression = 'id , email')
        metadata_items = metadata_response.get('Items', [])

        request_response = metadata_table.scan(ProjectionExpression = 'id , custom_fields')
        request_items = request_response.response.get('Items', [])

        custom_fields_by_email = { item['id'] : item.get('custom_fields', '{}') for item in request_items}

        account_data = []

        for metadata_item in metadata_items :
            account_id = metadata_items['id']
            email = metadata_item['email']

            custom_fields = custom_fields_by_email.get(email , '{}')

            if isinstance(custom_fields , str) :
                custom_fields_dict = json.loads(custom_fields)
            else:
                custom_fields_dict = custom_fields
            
            account_name = custom_fields_dict['Acccount_name']
            account_data.append({
                'account_id': account_id,
                'account_name' : account_name
            })
        
        return account_data if account_data else None
        
    def get_managed_accounts(self):
        return self.account_data


@pytest.fixture(scope = "session")
def accounts_config():
    try:
        return AccountsConfig('-RnD')
    except Exception as e:
        print(f"Error creation AccountManager: {str(e)}")
        return AccountsConfig(None)
    



    """
        this will read from the repository global repsoitory for now it is configured to compare Iam roles
        conincdently the first modification will need to happen here since because we are pulling from this repo
        if we modify this to say add more iam roles for the purpose of testing then AFT will actually create those roles as well.

        AS such the task at hand is to make this class extendable . we want to find a way to add an additional iam roles to test
        where we tweak the current code without actually creating the roles in the vended account . once this is confirmed then the codebuild tests will verify 
        """