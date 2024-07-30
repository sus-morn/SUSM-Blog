import os
import time
import pathlib
import subprocess

path = pathlib.Path(os.path.abspath(__file__))

# process_frontend = subprocess.Popen(['', ''], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
process_backend = subprocess.Popen('pdm run uvicorn __init__:app --reload', stdout=subprocess.PIPE, stderr=subprocess.PIPE,cwd=path.parent.parent/'backend',shell=True)
print("后端已启动！")

while True:
    time.sleep(0.2)
    output = process_backend.stdout.readline().decode()
    if output == '' and process_backend.poll() is not None:
        break
    if output:
        print(output.strip())