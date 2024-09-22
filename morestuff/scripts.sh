#!/bin/bash
which python3
python3 --version

Now, let's try the commands again with python3:
Copycp -r $(python3 -c "import ansible; print(ansible.__path__[0])") .
cp -r $(python3 -c "import ansible_runner; print(ansible_runner.__path__[0])") .
cp $(which ansible-playbook) .

If any of these commands fail, let's try to locate the files manually:
Copyfind /usr/local/lib/python3* -name "ansible" -type d
find /usr/local/lib/python3* -name "ansible_runner" -type d
which ansible-playbook

Once you've located the correct paths, copy them manually:
Copycp -r /path/to/ansible .
cp -r /path/to/ansible_runner .
cp /path/to/ansible-playbook .

After copying the files, create the zip file:
Copyzip -r ../ansible_layer.zip .

Check the contents and size:
Copyunzip -l ../ansible_layer.zip
du -sh ../ansible_layer.zip


sudo yum install python3-pip -y
pip install ansible ansible-runner