import os
import sys

def find_files(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
    return result

def lambda_handler(event, context):
    print(f"Python version: {sys.version}")
    
    print("\nsys.path:")
    for path in sys.path:
        print(path)
    
    search_paths = ['/opt', '/var/task']
    key_files = ['__init__.py', 'constants.py', 'config.py']
    
    for file in key_files:
        print(f"\nSearching for {file}:")
        for path in search_paths:
            found_files = find_files(file, path)
            if found_files:
                for found in found_files:
                    print(f"Found at: {found}")
            else:
                print(f"Not found in {path}")
    
    print("\nContents of /opt/python:")
    for root, dirs, files in os.walk('/opt/python'):
        level = root.replace('/opt/python', '').count(os.sep)
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
    
    return {
        'statusCode': 200,
        'body': 'File search results printed to CloudWatch logs'
    }