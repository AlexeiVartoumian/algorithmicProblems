#!/bin/bash
set -e

# Clean up previous files
rm -rf python ansible_layer.zip

# Create the directory structure
mkdir -p python/lib/python3.9/site-packages
mkdir -p python/bin

# Install Ansible and dependencies
pip3 install --target ./python/lib/python3.9/site-packages ansible-core==2.15.12 jinja2 PyYAML cryptography

# Find and copy ansible executables
find python/lib/python3.9/site-packages -name "ansible-*" -type f -executable -exec cp {} python/bin/ \;

# If ansible-playbook wasn't found, try to locate it and copy manually
if [ ! -f python/bin/ansible-playbook ]; then
    ANSIBLE_PLAYBOOK=$(find python -name ansible-playbook -type f)
    if [ -n "$ANSIBLE_PLAYBOOK" ]; then
        cp "$ANSIBLE_PLAYBOOK" python/bin/
        echo "Manually copied ansible-playbook from $ANSIBLE_PLAYBOOK"
    else
        echo "ERROR: ansible-playbook not found!"
    fi
fi

# Ensure ansible executables are executable
chmod +x python/bin/ansible*

# Remove unnecessary files to reduce size
cd python/lib/python3.9/site-packages

# Remove clearly non-AWS related collections
find ansible_collections -mindepth 1 -maxdepth 1 -type d ! -name "amazon" -exec rm -rf {} +

# Remove __pycache__ directories and .pyc files
find . -type d -name "__pycache__" -exec rm -rf {} +
find . -name "*.pyc" -delete

# Remove test directories
find . -type d -name "tests" -exec rm -rf {} +

# Go back to the root directory
cd ../../../..

# Create the zip file
zip -r ansible_layer.zip python

# Check the size and contents
du -sh ansible_layer.zip
echo "Checking for ansible-playbook in the zip file:"
unzip -l ansible_layer.zip | grep ansible-playbook

echo "Ansible Lambda layer created: ansible_layer.zip"