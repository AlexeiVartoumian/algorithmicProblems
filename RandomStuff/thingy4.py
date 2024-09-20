import os
import sys

def print_directory_tree(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print(f"{indent}{os.path.basename(root)}/")
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print(f"{subindent}{f}")

def lambda_handler(event, context):
    print(f"Python version: {sys.version}")
    
    print("\nsys.path:")
    for path in sys.path:
        print(path)
    
    ansible_paths = [
        '/opt/python',
        '/opt/python/lib/python3.9/site-packages',
        '/var/task'
    ]
    
    for path in ansible_paths:
        print(f"\nDirectory tree for {path}:")
        if os.path.exists(path):
            print_directory_tree(path)
        else:
            print(f"Path does not exist: {path}")
    
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
        'body': 'Directory tree printed to CloudWatch logs'
    }