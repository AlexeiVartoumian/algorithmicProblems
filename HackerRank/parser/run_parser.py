import sys
import subprocess
import os
from datetime import datetime


def run_script(script_name, folder_path):

    script_path = os.path.join(os.path.dirname(__file__), script_name)
    # change to python depend if path executes like this
    
    result = subprocess.run(['py', script_path, folder_path], capture_output=True, text=True)


    print(f"output of {script_name}")
    print(result.stdout)


    if result.stderr:
        print(f"Errors in {script_name}")
        print(result.stderr)

def run_git_commands(folder_path):
    try:

        os.chdir(folder_path)

        #git add .
        subprocess.run(['git', 'add', '.'], check=True)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        commit_message = f"Auto-commit: {timestamp}"

        #git commit
        subprocess.run(['git', 'commit', '-m', commit_message], check=True)

        subprocess.run(['git', 'push'], check=True)

        print("git operations completed")
    except subprocess.CalledProcessError as e:
        print(f"An error occured during Git operations: {e}")
    finally:
        os.chdir(os.path.dirname(__file__))
def main():
    if len(sys.argv) != 2:
        print("usecase : python run_parser.py < some path in same directory -challenge-folder")
        sys.exit(1)
    
    folder_path = sys.argv[1]

    scripts = ['gethtml.py','render.py','postprocess.py']

    for script in scripts:
        run_script(script , folder_path)

    run_git_commands(folder_path)
if __name__ == "__main__" :
    main()