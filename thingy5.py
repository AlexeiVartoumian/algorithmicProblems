import json
import yaml
import os
import sys
import subprocess

def lambda_handler(event, context):
    # Debugging information
    debug_info = {
        "PATH": os.environ.get("PATH", ""),
        "LAMBDA_TASK_ROOT": os.environ.get("LAMBDA_TASK_ROOT", ""),
        "Python Version": sys.version,
        "Executable": sys.executable,
        "Current Working Directory": os.getcwd(),
        "Directory Contents": os.listdir(os.getcwd()),
        "Temp Directory Contents": os.listdir('/tmp'),
        "Environment Variables": dict(os.environ)
    }
    
    # Try to find ansible-playbook in PATH
    ansible_playbook_path = None
    for path in os.environ.get("PATH", "").split(os.pathsep):
        full_path = os.path.join(path, "ansible-playbook")
        if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
            ansible_playbook_path = full_path
            break
    
    debug_info["ansible-playbook location"] = ansible_playbook_path or "Not found in PATH"

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
    command = [ansible_playbook_path or 'ansible-playbook', playbook_path]

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
    

import sys
import os

# Add the Ansible modules to the Python path
sys.path.append("/opt/python/lib/python3.9/site-packages")

from ansible.module_utils.common.collections import ImmutableDict
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.plugins.callback import CallbackBase
from ansible import context

class ResultCallback(CallbackBase):
    def __init__(self):
        super().__init__()
        self.host_ok = {}
        self.host_unreachable = {}
        self.host_failed = {}

    def v2_runner_on_ok(self, result, **kwargs):
        self.host_ok[result._host.get_name()] = result

    def v2_runner_on_unreachable(self, result):
        self.host_unreachable[result._host.get_name()] = result

    def v2_runner_on_failed(self, result, **kwargs):
        self.host_failed[result._host.get_name()] = result

def run_ansible_task(host, module, args):
    context.CLIARGS = ImmutableDict(connection='local', module_path=['/to/mymodules'], forks=10, become=None,
                                    become_method=None, become_user=None, check=False, diff=False)

    sources = f"{host},"
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=sources)
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    play_source = dict(
        name="Ansible Play",
        hosts=host,
        gather_facts='no',
        tasks=[dict(action=dict(module=module, args=args))]
    )

    play = Play().load(play_source, variable_manager=variable_manager, loader=loader)

    callback = ResultCallback()
    tqm = None

    try:
        tqm = TaskQueueManager(
            inventory=inventory,
            variable_manager=variable_manager,
            loader=loader,
            passwords=dict(),
            stdout_callback=callback
        )
        result = tqm.run(play)
    finally:
        if tqm is not None:
            tqm.cleanup()

    return callback.host_ok, callback.host_failed, callback.host_unreachable

def lambda_handler(event, context):
    print(f"Python version: {sys.version}")
    print(f"sys.path: {sys.path}")
    
    try:
        import ansible
        print(f"Ansible version: {ansible.__version__}")
        
        # Example: Run an Ansible task
        host_ok, host_failed, host_unreachable = run_ansible_task('localhost', 'ping', {})
        
        if host_ok:
            result = host_ok['localhost']._result
            return {
                'statusCode': 200,
                'body': f'Ansible task executed successfully. Result: {result}'
            }
        elif host_failed:
            result = host_failed['localhost']._result
            return {
                'statusCode': 500,
                'body': f'Ansible task failed. Error: {result}'
            }
        elif host_unreachable:
            result = host_unreachable['localhost']._result
            return {
                'statusCode': 500,
                'body': f'Host unreachable. Error: {result}'
            }
    except ImportError as e:
        print(f"Error importing Ansible: {e}")
        return {
            'statusCode': 500,
            'body': f'Failed to import Ansible: {str(e)}'
        }
    except Exception as e:
        print(f"Error executing Ansible task: {e}")
        return {
            'statusCode': 500,
            'body': f'Error executing Ansible task: {str(e)}'
        }