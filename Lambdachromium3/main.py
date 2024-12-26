from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tempfile import mkdtemp
import json
import time
import logging
import boto3
import random 

logger = logging.getLogger()
logger.setLevel(logging.INFO)

QUEUE_URL = "https://sqs.eu-west-2.amazonaws.com/390746273208/verification-code-queue"

def initialise_driver():
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-dev-tools")
    chrome_options.add_argument("--no-zygote")
    chrome_options.add_argument("--single-process")
    chrome_options.add_argument(f"--user-data-dir={mkdtemp()}")
    chrome_options.add_argument(f"--data-path={mkdtemp()}")
    chrome_options.add_argument(f"--disk-cache-dir={mkdtemp()}")
    chrome_options.add_argument("--remote-debugging-pipe")
    chrome_options.add_argument("--verbose")
    chrome_options.add_argument("--log-path=/tmp")
    chrome_options.binary_location = "/opt/chrome/chrome-linux64/chrome"

    service = Service(
        executable_path="/opt/chrome-driver/chromedriver-linux64/chromedriver",
        service_log_path="/tmp/chromedriver.log"
    )

    driver = webdriver.Chrome(
        service=service,
        options=chrome_options
    )

    return driver

def save_screen_shot_to_s3(driver,screenshot_name):

    s3_client = boto3.client('s3')
    bucket_name = 'emailbuckethaha'

    screenshot_path =  f"/tmp/{screenshot_name}.png"
    driver.save_screenshot(screenshot_path)
    
    try:
        s3_client.upload_file(
            screenshot_path,
            bucket_name,
            f"screenshots/{screenshot_name}.png"
        )
        logger.info(f"Screenshot uploaded to s3://{bucket_name}/screenshots/{screenshot_name}.png")
    except Exception as e: 
        logger.error(f"Failed to upload screenshot: {str(e)}")
def perform_sign_up(driver , username):
    try:
        wait = WebDriverWait(driver , 20)
        logger.info("looking for sign up buttin")

        time.sleep(2)
        save_screen_shot_to_s3(driver, f"before_login_find_{random.randint(1000,9999)}")
        logger.info("Attempting to find login button with exact XPath")

        # login_button = wait.until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, '[data-test="header-sign-in"]'))
        # )
        # wait.until(EC.element_to_be_clickable(login_button))
        login_button = driver.find_element(By.CSS_SELECTOR, '[data-test="header-sign-in"]')
        login_url = login_button.get_attribute('href')
        driver.get(login_url)
        logger.info("FOund sign-up button clicking")
        #login_button.click()
        logger.info(f"Current URL after clicking sign up: {driver.current_url}")

        email_field = wait.until (
            EC.presence_of_element_located((By.ID , "PHONE_NUMBER_or_EMAIL_ADDRESS"))
        )
        email_field.send_keys("avarto01@student.bbk.ac.uk")
        save_screen_shot_to_s3(driver, f"email_entered_{random.randint(1000,9999)}")

        click_continue = wait.until(
        EC.presence_of_element_located((By.ID, "forward-button"))
        )
        click_continue.click()
        time.sleep(2)
        logger.info(f"Current url after sign up: {driver.current_url}")
        save_screen_shot_to_s3(driver, f"inputcodes_{random.randint(1000,9999)}")
        return True , "Successfully clicked signup and entered email"
    except Exception as e: 
        logger.error(f"Error in perform_signup: {str(e)}")
        save_screen_shot_to_s3(driver, f"signup_error_{random.randint(1000,9999)}")
        logger.error("Page source at error: " + driver.page_source)

        return False , f"Failed to perform signup: {str(e)}"

def wait_for_sqs_message(queue_url , max_wait_time=60):
    
    sqs = boto3.client('sqs')
    start_time = time.time()

    while(time.time() -start_time < max_wait_time):
        try:
            response = sqs.receive_message(
                QueueUrl=QUEUE_URL,
                MaxNumberOfMessages=1,
                WaitTimeSeconds=5
            )
        
            if 'Messages' in response:

                message = response.get('Mesages')[0]
                logger.info(f"Recieved message: {message['Body']}")

                sqs.delete_message(
                    Queue_url = QUEUE_URL,
                    ReceiptHandle=message['ReceiptHandle']
                )
                return json.loads(message['Body'])

            logger.info("no messsage recieved , continuing to poll")

        except Exception as e : 
            logger.error(f"Error receiving message: {str(e)}")
            return None

def process_verification_code(driver , verification_code):
    """
    enter verification code into 4 diff boxes
    """
    try:
        wait = WebDriverWait(driver , 10 )
        logger.info(f"Attempting to enter verification code :{verification_code}")

        if not verification_code or len(verification_code) !=4 :
            raise ValueError("Verification code must be exactly 4 digits")
        
        for i in range(4):
            input_field = wait.until(
                EC.presence_of_element_located((By.ID , f"EMAIL_OTP_CODE-{i}"))
            )
            logger.info(f"Entering digt {verification_code[i]} into field {i}")
            input_field.send_keys(verification_code[i])

            #save_screen_shot_to_s3(driver , f"otp_digit_{i}")
    
        time.sleep(1)

    except Exception as e:
        logger.error(f"Failed to click succeed: {str(e)}")
        # The code might auto-submit, so this error might be ignorable
        pass
    
    time.sleep(2)
    save_screen_shot_to_s3(driver , f"verifcation_complete_{random.randint(1000,9999)}")
    return True, "Successfully entered verification code"
def lambda_handler(event, context):
    driver = None
    try:
        driver = initialise_driver()
        driver.get("https://www.ubereats.com")

        success, message = perform_sign_up(driver , "avarto01@student.bbk.ac.uk")
        if not success: 
            raise Exception(f"Signup failed: {message}")
        
        logger.info("Watiting for verifcation code from Sqs..")
        verification_code = wait_for_sqs_message(QUEUE_URL)
        
        if verification_code:
            success , message  = process_verification_code(driver ,verification_code)
            if not success:
                raise Exception(f"Verifcation failed: {message}")
       
        
            return {
                'statusCode': 200,
                'body': json.dumps({
                    'message': 'Success',
                    'details': message
                })
            }
        else:
            return {
                'statusCode' : 400,
                'body': json.dumps({
                    'message': 'No verification code recieved within timeout period'
                })
            }
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e)
            })
        }
    finally:
        if driver is not None:
            try: 
                driver.quit()
                logger.info("Browser closed successfully")
            except Exception as e:
                logger.error(f"Error closing browser: {str(e)}")







