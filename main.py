# import os
import time
from backend import launcher
# import pathlib
# import subprocess

# path = pathlib.Path(os.path.abspath(__file__))

# # process_frontend = subprocess.Popen(['', ''], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# process_backend = subprocess.Popen('pdm run uvicorn __init__:app --reload', stdout=subprocess.PIPE, stderr=subprocess.PIPE,cwd=path.parent.parent/'backend',shell=True)
# print(process_backend.stderr.readline().decode()) # type: ignore
# print("后端已启动！")

process_backend = launcher.launch()
print("后端服务已启动")
while True:
    try:
        time.sleep(0.2)
        output = process_backend.stdout.readline().decode() # type: ignore
        if output == '' and process_backend.poll() is not None:
            break
        if output:
            print(output.strip())
    except KeyboardInterrupt:
        print("用户主动结束了进程")
        break
