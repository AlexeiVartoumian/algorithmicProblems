

import re 
import json
import boto3
import logging 
import os 
import time 

logger = logging.getLogger()
logger.setLevel(logging.INFO)

QUEUE_URL = "https://sqs.eu-west-2.amazonaws.com/390746273208/verification-code-queue"


def extract_number(text):
    pattern = r'; padding-top: 0;">(\d{4})</td>'

    matches = re.findall(pattern, text)

    if matches:
        logger.info(f"Found numbers: {matches}")
        return matches
    else:
        logger.info("No numenrs found in content" )
        return []


def push_to_sqs(verification_code):

    try:
        sqs = boto3.client('sqs')
        #queue_url = QUEUE_URL

        message_body = {
            'verification_code': verification_code
        }
        response = sqs.send_message(
            QueueUrl= QUEUE_URL,
            MessageBody= json.dumps(message_body)
        )
        logger.info(f"Successfully pushed code {verification_code}")
        return True
    except Exception as e:
        logger.error(f"Failed to push to SQS: {str(e)}")
        return False
    
def lambda_handler(event , context):
    
    #todo link lambda to sns topic. 
    try:
        
        logger.info("recieved event from SNs")
        message = event['Records'][0]['Sns']['Message']
        logger.info(f"Processing image: {message}")

        
        logger.info(f"Processing message: {message}")

        extracted_numbers = push_to_sqs(extract_number(message))

        if extracted_numbers:
            
            return {
                'statusCode': 200,
                'body' : json.dumps({
                'message' : 'Successfully pushed code to sqs' ,
                'extracted_numbers' : extracted_numbers
                })
            }
        else:
            logger.warning("No verification code found in message")
            return {
                'statusCode' : 404,
                'body' : json.dumps({
                    'message':'No numbers found in message'
                })
            }

    except Exception as e :
        return {
            'statusCode' : 500,
            'body': json.dumps({'error': str(e)})
        }
    




