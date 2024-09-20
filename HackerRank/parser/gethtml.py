
import sys
import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager



# def get_challenge_html(challenge_name):
#     base_url = "https://www.hackerrank.com/challenges"
#     url = f"{base_url}{challenge_name}"

#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
#         'Accept-Language': 'en-US,en;q=0.9',
#         'Referer': 'https://www.google.com',
#         'Connection': 'keep-alive',
#     }

#     response = requests.get(url, headers=headers)

#     if response.status_code != 200:

#         print(f"Failed to retrieve page . status code {response.status_code}")
#         return None

#     soup = BeautifulSoup(response.text , 'html.parser')

#     #challenge_div = soup.find('div', class_=["content-text", "challenge-text"])

#     print(soup)
#     challenge_div = soup.select_one('div.content-text.challenge-text')
#     if not challenge_div: 
#         print("Failed to find div with the required classes")
#         return None

#     return str(challenge_div)
def get_challenge_html(challenge_name):
    base_url = "https://www.hackerrank.com/challenges/"
    url = f"{base_url}{challenge_name}"

    # Configure Selenium to use Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run headless Chrome (no GUI)
    
    # Set custom headers
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")
    chrome_options.add_argument("accept-language=en-US,en;q=0.9")

    # Initialize WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    
    # Make the request to the URL
    driver.get(url)
    
    # Give the page some time to load JavaScript content
    driver.implicitly_wait(30)  # Wait up to 10 seconds for the content to load
    
    # Get page source after JavaScript execution
    page_source = driver.page_source
    
    # Parse the HTML content using BeautifulSoup
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')
    print(soup)
    # Find the div with the required classes, allowing for additional classes
    #challenge_div = soup.find('div', class_=['content-text', 'challenge-text'])
    
    challenge_div = soup.find('div', class_=['challenge-body-html'])
    if not challenge_div:
        print("Failed to find the div with the required classes.")
        driver.quit()
        return None
    
    driver.quit()
    return str(challenge_div)

def save_html_to_file(html_content , folder_path):

    os.makedirs(folder_path, exist_ok=True)

    file_path = os.path.join(folder_path, 'input.html')

    with open( file_path, "w" , encoding= 'utf-8') as file:
        file.write(html_content)

    print( f"Html content saved to {file_path}" ) 

def main():
    if len(sys.argv) != 2:
        print("Usage py gethtml.py <folder name>")
        sys.exit(1)
    
    folder_path = sys.argv[1]

    #get challenge anme from folder path
    challenge_name = os.path.basename(folder_path)
    html_content = get_challenge_html(challenge_name)
    
    if html_content:
        save_html_to_file(html_content, folder_path)


if __name__== "__main__":
    main()