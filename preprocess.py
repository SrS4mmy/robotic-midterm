import subprocess
import os
import sys

# grab requirements for rvc3 uts robotik (linux)
def main(file_path='requirements.txt'):
    if not os.path.exists(file_path):
        print(f"file {file_path}not found")
        return
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'freeze','>',file_path ])
        subprocess.check_call([sys.executable, '-m', 'pip', 'install','-r',file_path ])
        print("requirements fulfilled")
    except subprocess.CalledProcessError as e:
        print("requirements not fulfilled")

if __name__ == "__main__":
    main()