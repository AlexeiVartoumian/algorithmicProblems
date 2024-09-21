import subprocess
import json
import yaml
import os
import sys

def lambda_handler(event, context):
    # Debugging information
    debug_info = {
        "PATH": os.environ.get("PATH", ""),
        "LAMBDA_TASK_ROOT": os.environ.get("LAMBDA_TASK_ROOT", ""),
        "Python Version": sys.version,
        "Executable": sys.executable,
        "Current Working Directory": os.getcwd(),
        "Directory Contents": os.listdir(os.getcwd())
    }
    
    # Try to locate ansible-playbook
    try:
        ansible_playbook_path = subprocess.check_output(["which", "ansible-playbook"], text=True).strip()
        debug_info["ansible-playbook location"] = ansible_playbook_path
    except subprocess.CalledProcessError:
        debug_info["ansible-playbook location"] = "Not found in PATH"

    # Define the playbook content in YAML format
    playbook = [
        {
            'name': 'Sample Ansible Playbook',
            'hosts': 'localhost',
            'gather_facts': False,
            'tasks': [
                {
                    'name': 'Echo a message',
                    'debug': {
                        'msg': 'Hello from Ansible in Lambda!'
                    }
                }
            ]
        }
    ]

    # Write the playbook to a temporary file in YAML format
    playbook_path = '/tmp/playbook.yml'
    with open(playbook_path, 'w') as f:
        yaml.dump(playbook, f)

    # Command to run the ansible-playbook with the playbook file
    command = ['ansible-playbook', playbook_path]

    try:
        # Run the ansible-playbook command using subprocess
        result = subprocess.run(command, capture_output=True, text=True)

        # Capture the stdout and stderr output
        output = result.stdout
        error_output = result.stderr

        if result.returncode == 0:
            # Playbook executed successfully
            return {
                'statusCode': 200,
                'body': json.dumps({
                    'message': 'Ansible Playbook Output',
                    'output': output,
                    'debug_info': debug_info
                })
            }
        else:
            # Playbook failed
            return {
                'statusCode': 500,
                'body': json.dumps({
                    'message': 'Ansible Playbook Error',
                    'error': error_output,
                    'debug_info': debug_info
                })
            }
    except Exception as e:
        # Handle errors in case the subprocess call fails
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': f'Error running Ansible Playbook: {str(e)}',
                'debug_info': debug_info
            })
        }