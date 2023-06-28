import os
import subprocess

# files = os.system('cmd /c "ls -la"')
str = subprocess.run("ls -la --color=always", capture_output=True, text=True).stdout

print(str)