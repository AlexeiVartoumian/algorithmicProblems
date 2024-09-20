import os
import sys

def check_path(path):
    print(f"Checking path: {path}")
    print(f"  os.path.exists: {os.path.exists(path)}")
    print(f"  os.path.isfile: {os.path.isfile(path)}")
    print(f"  os.path.isdir: {os.path.isdir(path)}")
    try:
        print(f"  os.listdir: {os.listdir(os.path.dirname(path))}")
    except Exception as e:
        print(f"  Error listing directory: {e}")

def lambda_handler(event, context):
    print(f"Python version: {sys.version}")
    
    print("\nsys.path:")
    for path in sys.path:
        print(path)
    
    ansible_files = ['__init__.py', 'constants.py', 'config.py']
    base_paths = [
        '/opt/python/lib/python3.9/site-packages/ansible',
        '/var/task/ansible',
        '/opt/ansible'
    ]
    
    for base_path in base_paths:
        print(f"\nChecking base path: {base_path}")
        check_path(base_path)
        for file in ansible_files:
            file_path = os.path.join(base_path, file)
            print(f"\nChecking file: {file_path}")
            check_path(file_path)
    
    print("\nContents of /opt:")
    for root, dirs, files in os.walk('/opt'):
        level = root.replace('/opt', '').count(os.sep)
        indent = ' ' * 4 * level
        print(f"{indent}{os.path.basename(root)}/")
        sub_indent = ' ' * 4 * (level + 1)
        for f in files:
            print(f"{sub_indent}{f}")
    
    try:
        import ansible
        print(f"\nAnsible successfully imported. Version: {ansible.__version__}")
    except ImportError as e:
        print(f"\nFailed to import Ansible: {e}")
        print(f"  sys.modules keys: {list(sys.modules.keys())}")
    
    return {
        'statusCode': 200,
        'body': 'Diagnostic information printed to CloudWatch logs'
    }