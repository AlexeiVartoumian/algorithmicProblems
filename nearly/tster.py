    
import os
import sys
import tempfile
import importlib

# Set Ansible configurations before importing any Ansible modules
os.environ['ANSIBLE_LOCAL_TEMP'] = '/tmp'
os.environ['ANSIBLE_REMOTE_TEMP'] = '/tmp'
os.environ['HOME'] = '/tmp'
os.environ['ANSIBLE_FORKS'] = '1'
from ansible import context
from ansible.module_utils.common.collections import ImmutableDict
from ansible.parsing.dataloader import DataLoader
from ansible.inventory.manager import InventoryManager
from ansible.vars.manager import VariableManager
from ansible.playbook import Playbook
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.plugins.callback import CallbackBase

class ResultCallback(CallbackBase):
    def __init__(self, *args, **kwargs):
        super(ResultCallback, self).__init__(*args, **kwargs)
        self.host_ok = {}
        self.host_unreachable = {}
        self.host_failed = {}

    def v2_runner_on_ok(self, result, *args, **kwargs):
        self.host_ok[result._host.get_name()] = result

    def v2_runner_on_failed(self, result, *args, **kwargs):
        self.host_failed[result._host.get_name()] = result

    def v2_runner_on_unreachable(self, result):
        self.host_unreachable[result._host.get_name()] = result

def run_ansible_playbook():
    playbook_path = '/tmp/test_playbook.yml'
    with open(playbook_path, 'w') as f:
        f.write('''
- name: Test Playbook
  hosts: localhost
  connection: local
  tasks:
    - name: Print message
      debug:
        msg: "Hello from Ansible in Lambda!"
''')

    loader = DataLoader()
    context.CLIARGS = ImmutableDict(connection='local', module_path=None, forks=1, become=None,
                                    become_method=None, become_user=None, check=False, diff=False,
                                    verbosity=0)

    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    results_callback = ResultCallback()

    tqm = None
    try:
        tqm = TaskQueueManager(
            inventory=inventory,
            variable_manager=variable_manager,
            loader=loader,
            passwords={},
            stdout_callback=results_callback
        )

        playbook = Playbook.load(playbook_path, variable_manager=variable_manager, loader=loader)
        
        for play in playbook.get_plays():
            result = tqm.run(play)

        return {
            "ok": results_callback.host_ok,
            "failed": results_callback.host_failed,
            "unreachable": results_callback.host_unreachable
        }
    finally:
        if tqm is not None:
            tqm.cleanup()

def lambda_handler(event, context):
    print(f"Python version: {sys.version}")
    
    try:
        print("Attempting to run Ansible playbook...")
        results = run_ansible_playbook()
        print(f"Playbook execution results: {results}")
    except Exception as e:
        print(f"Error running Ansible playbook: {e}")
        print("Detailed error:")
        import traceback
        print(traceback.format_exc())
    
    return {
        'statusCode': 200,
        'body': 'Ansible playbook execution completed. See CloudWatch logs for details.'
    }


"""
Detailed error:
Traceback (most recent call last):
File "/opt/python/lib/python3.9/site-packages/ansible/executor/task_queue_manager.py", line 167, in init
self._final_q = FinalQueue()
File "/opt/python/lib/python3.9/site-packages/ansible/executor/task_queue_manager.py", line 82, in init
super(FinalQueue, self).init(*args, kwargs)
File "/var/lang/lib/python3.9/multiprocessing/queues.py", line 43, in init
self._rlock = ctx.Lock()
File "/var/lang/lib/python3.9/multiprocessing/context.py", line 68, in Lock
return Lock(ctx=self.get_context())
File "/var/lang/lib/python3.9/multiprocessing/synchronize.py", line 162, in init
SemLock.init(self, SEMAPHORE, 1, 1, ctx=ctx)
File "/var/lang/lib/python3.9/multiprocessing/synchronize.py", line 57, in init
sl = self._semlock = _multiprocessing.SemLock(
OSError: [Errno 38] Function not implemented
During handling of the above exception, another exception occurred:
Traceback (most recent call last):
File "/var/task/lambda_function.py", line 108, in lambda_handler
results = run_ansible_playbook()
File "/var/task/lambda_function.py", line 64, in run_ansible_playbook
pbex = PlaybookExecutor(
File "/opt/python/lib/python3.9/site-packages/ansible/executor/playbook_executor.py", line 62, in init
self._tqm = TaskQueueManager(
File "/opt/python/lib/python3.9/site-packages/ansible/executor/task_queue_manager.py", line 169, in init**
raise AnsibleError("Unable to use multiprocessing, this is normally caused by lack of access to /dev/shm: %s" % to_native(e))
raise AnsibleError("Unable to use multiprocessing, this is normally caused by lack of access to /dev/shm: %s" % to_native(e))
ansible.errors.AnsibleError: Unable to use multiprocessing, this is normally caused by lack of access to /dev/shm: [Errno 38] Function not implemented
END RequestId: b3b93439-6605-4cbf-a63f-0a86b8b0c7eb
REPORT RequestId: b3b93439-6605-4cbf-a63f-0a86b8b0c7eb    Duration: 1236.21 ms    Billed Duration: 1237 ms    Memory Size: 128 MB    Max Memory Used: 60 MB    Init Duration: 750.10 ms
"""