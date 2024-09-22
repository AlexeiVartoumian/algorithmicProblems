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


Creating a Minimal Ansible Lambda Layer
Follow these steps to create a minimal Ansible layer for AWS Lambda:

Set up a clean virtual environment:
bashCopypython3 -m venv ansible-layer-env
source ansible-layer-env/bin/activate

Install Ansible and minimum required dependencies:
bashCopypip install ansible-core PyYAML jinja2 cryptography

Create the layer structure:
bashCopymkdir -p ansible-layer/python/lib/python3.9/site-packages

Copy Ansible and its dependencies:
bashCopycp -r ansible-layer-env/lib/python3.9/site-packages/ansible ansible-layer/python/lib/python3.9/site-packages/
cp -r ansible-layer-env/lib/python3.9/site-packages/yaml ansible-layer/python/lib/python3.9/site-packages/
cp -r ansible-layer-env/lib/python3.9/site-packages/jinja2 ansible-layer/python/lib/python3.9/site-packages/
cp -r ansible-layer-env/lib/python3.9/site-packages/cryptography ansible-layer/python/lib/python3.9/site-packages/

Remove unnecessary files to reduce size:
bashCopyfind ansible-layer -name '*.pyc' -delete
find ansible-layer -name '__pycache__' -exec rm -rf {} +
rm -rf ansible-layer/python/lib/python3.9/site-packages/ansible/test

Create the zip file:
bashCopycd ansible-layer
zip -r ../ansible-minimal-layer.zip python

Check the size of the zip file:
bashCopyls -lh ansible-minimal-layer.zip


This process should create a significantly smaller zip file containing only the essential Ansible components needed for Lambda.