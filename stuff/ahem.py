#!/usr/bin/env python3

import os
import re
import sys
import shutil

def cleanup_test_profile():
    """profile from AWS credentials file,
    leaving all other profiles intact.
    """
    # Path to AWS credentials file
    creds_path = os.path.expanduser('~/.aws/credentials')
    
    # Check if file exists
    if not os.path.exists(creds_path):
        print(f"AWS credentials file not found at {creds_path}")
        return False
    
    # Create a backup
    backup_path = creds_path + '.bak'
    shutil.copy2(creds_path, backup_path)
    print(f"Backup created at {backup_path}")
    
    # Read the current contents
    with open(creds_path, 'r') as f:
        content = f.read()
    
    pattern = r'\[-test\](.*?)(?=\[\w+\]|$)'
    
  
    if not re.search(pattern, content, re.DOTALL):
        print("No [-test] profile found in credentials file.")
        return False
  
    new_content = re.sub(pattern, '', content, flags=re.DOTALL)
    
    new_content = re.sub(r'\n{3,}', '\n\n', new_content)
    
  
    with open(creds_path, 'w') as f:
        f.write(new_content)
    
    print("Successfully removed [saml-test] profile from credentials file.")
    return True