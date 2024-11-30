import boto3
import json
from pathlib import Path
from typing import Dict , List , Any
import logging
import os

from botocore.exceptions import ClientError 

class AWSRoleManager:

    def __init__(self, account_id):
        self.first_role_arn  = os.getenv('AFT_ADMIN_ARN')
        self.assumed_role_session_name = os.getenv('ROLE_SESSION_NAME')

        self.account_id = account_id
        self.session = self.assume_role()
        self.iam = self.session.client('iam')

    def assume_role(self):
        sts_client = boto3.client('sts')

        first_role_response = sts_client.assume_role(
            RoleArn=self.first_role_arn,
            RoleSessionName=self.assumed_role_session_name
        )

        sts_client_2 = boto3.client(
            'sts' ,
            aws_access_key = first_role_response['Credentials']['AccessKeyId'],
            aws_secret_key =first_role_response['Credentials']['SecretAccessKey'],
            aws_session_token =first_role_response['Credentials']['SecretAccessKey']
        )

        spoke_role_response = sts_client_2.assume_role(
            RoleArn=f'arn:aws:iam::{self.account_id}:role/AWSAFTExecution',
            RoleSessionName ="SpokeAccount"
        )

        return boto3.Session(
            aws_access_key_id=spoke_role_response['Credentials']['AccessKeyId'],
            aws_secret_access_key=spoke_role_response['Credentials']['SecretAccessKey'],
            aws_session_token=spoke_role_response['Credentials']['SessionToken']
        )
    
