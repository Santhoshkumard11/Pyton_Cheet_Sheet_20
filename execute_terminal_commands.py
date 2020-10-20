#Execute terminal commands in Python

import subprocess
result = subprocess.getoutput(cmd="mkdir new_folder") # replace the string with your command
print(result) # will print the terminal output
