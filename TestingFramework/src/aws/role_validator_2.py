import boto3
import json
from pathlib import Path
from typing import Dict , List , Any
import logging

from src.aws.role_manager import AWSRoleManager
from botocore.exceptions import ClientError


class AWSRoleValidator:
    
    def __init__(self , account_id):
        
        self.account_id = account_id
        self.role_manager=AWSRoleManager(account_id)
        self.session = self.role_manager.assume_role()
        self.iam = self.session.client('iam')
    
    def assume_role_or_service_role(self, role_file: str) -> bool:
    
        return 'other/roles' in role_file

    def compare_role_permissions(self, role_name: str, role_file: str, policy_name: str) -> bool:
        
        with open(role_file, 'r') as f:
            expected_policy = json.load(f)
    
    
        if self.assume_role_or_service_role(role_file):
            # Handle inline policies for service roles
            inline_policies = self.iam.list_role_policies(RoleName=role_name)
            for policy_name in inline_policies['PolicyNames']:
                policy_doc = self.iam.get_role_policy(
                    RoleName=role_name,
                    PolicyName=policy_name
                )
                actual_policy = {
                    "Version": policy_doc['PolicyDocument'].get("Version", "2012-10-17"),
                    "Statement": policy_doc['PolicyDocument'].get("Statement", [])
                }
                return self.compare_policies(expected_policy, actual_policy, role_name)
        
            logging.error(f"No inline policies found for service role {role_name}")
            return False
        else:
            
            attached_policies = self.iam.list_attached_role_policies(RoleName=role_name)
            policy_arn = None

            for policy in attached_policies['AttachedPolicies']:
                logging.info(policy)
                if policy['PolicyName'] == policy_name:
                    policy_arn = policy['PolicyArn']
                    break
        
            if not policy_arn:
                logging.error(f"Policy {policy_name} not found attached to role {role_name}")
                return False

            policy_metadata = self.iam.get_policy(PolicyArn=policy_arn)
            default_version_id = policy_metadata['Policy']['DefaultVersionId']

            policy_version = self.iam.get_policy_version(
                PolicyArn=policy_arn,
                VersionId=default_version_id
            )

            actual_policy = {
                "Version": policy_version['PolicyVersion']['Document'].get("Version", "2012-10-17"),
                "Statement": policy_version['PolicyVersion']['Document'].get("Statement", [])
            }
            return self.compare_policies(expected_policy, actual_policy, role_name)
    



    def compare_policies(self , expected: Dict[str, Any] , actual: Dict[str, Any], role_name: str):

        if expected.get("Version") != actual.get("Version"):
            logging.info("Version mismatch")
            return False
        expected_statements = expected.get("Statement", [])
        actual_statements = actual.get("Statement", [])

        if isinstance(expected_statements,dict):
            expected_statements = [expected_statements]
        
        if isinstance(actual_statements, dict):
            actual_statements = [actual_statements]
        

        expected_statements_match = False
        actual_statements_match = False

        logging.ingo('\n\nLocal json to role check')
        for exp_stmt in expected_statements:
            logging.info(exp_stmt)
            matching_statement = False
            for act_stmt in actual_statements:
                logging.info(act_stmt)
                if self.compare_statements(exp_stmt , act_stmt):
                    logging.info(f"SUCCESS - found matching statement. Expected{exp_stmt}, Actual:{act_stmt}")
                    expected_statements_match = True
                    break
            
            if not expected_statements_match:
                logging.info(f"Role {role_name}: No matching statement found for: {exp_stmt}")
                return False
        
        logging.info(f"Deployed role to local json check")

        for act_stmt in actual_statements:
            for exp_stmt in expected_statements:
                if self.compare_statements(exp_stmt , act_stmt):
                    actual_statements_match = True
                    logging.info(f"SUCCESS - found matching statement expected{exp_stmt}, Actuall: {act_stmt}")
                    break
            
            if not actual_statements_match:
                logging.info(f"Additional permissions found in actual policy: {act_stmt}")
                return False
        
        return expected_statements_match and actual_statements_match
    
    def compare_statements(self , expected: Dict[str, Any] , actual: Dict[str,Any]):
        if expected.get("Effect") != actual.get("Effect"):
            logging.info("Effect mismatch")
            return False
        
        expected_actions = expected.get("Action", [])
        actual_actions = actual.get("Action", [])

        if isinstance(expected_actions, str ):
            expected_actions = [expected_actions]
        if isinstance(actual_actions , str): 
            actual_actions = [actual_actions]
        
        if set(expected_actions) != set(actual_actions):
            logging.info(f"Actions mismatch. Expected: {expected_actions} , Actual: actual_actions")
            return False

        expected_resources = expected.get("Resource" , [])
        actual_resources = actual.get("Resource" , [])

        if isinstance(expected_resources, str):
            expected_resources = [expected_resources]
        
        if isinstance(actual_resources, str):
            actual_resources = [actual_resources]
        
        if set(expected_resources) != set(actual_resources):
            logging.info(f"Resources mismatch . Expected: {expected_resources}, Actual: {actual_resources}")
            return False
        
        return True 