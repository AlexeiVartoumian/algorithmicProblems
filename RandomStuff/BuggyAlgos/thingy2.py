import os
import sys

def print_directory_contents(path, prefix=''):
    try:
        for item in os.listdir(path):
            full_path = os.path.join(path, item)
            if os.path.isdir(full_path):
                print(f"{prefix}{item}/")
                print_directory_contents(full_path, prefix + '  ')
            else:
                print(f"{prefix}{item}")
    except Exception as e:
        print(f"Error listing {path}: {e}")

def lambda_handler(event, context):
    print(f"Python version: {sys.version}")
    
    print("\nsys.path:")
    for path in sys.path:
        print(path)
    
    ansible_locations = [
        '/opt/python/lib/python3.9/site-packages/ansible',
        '/var/task/ansible',
        '/opt/ansible'
    ]
    
    for location in ansible_locations:
        print(f"\nContents of {location}:")
        print_directory_contents(location)
    
    print("\nChecking for key Ansible files:")
    key_files = ['__init__.py', 'constants.py', 'config.py', 'module_utils/__init__.py']
    for location in ansible_locations:
        for file in key_files:
            full_path = os.path.join(location, file)
            if os.path.exists(full_path):
                print(f"Found: {full_path}")
            else:
                print(f"Missing: {full_path}")
    
    try:
        import ansible
        print(f"\nAnsible successfully imported. Version: {ansible.__version__}")
    except ImportError as e:
        print(f"\nFailed to import Ansible: {e}")
        print("Detailed import error:")
        import traceback
        print(traceback.format_exc())
    
    return {
        'statusCode': 200,
        'body': 'Diagnostic information printed to CloudWatch logs'
    }