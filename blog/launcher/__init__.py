# import os
import time
# from ..blog.backend import launch
# import pathlib
import subprocess
from .logger import logger
from inspect import cleandoc

# path = pathlib.Path(os.path.abspath(__file__))

# process_frontend = subprocess.Popen(['', ''], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# process_backend = subprocess.Popen('pdm run uvicorn __init__:app --reload', stdout=subprocess.PIPE, stderr=subprocess.PIPE,cwd=path.parent.parent/'backend',shell=True)
# print(process_backend.stderr.readline().decode()) # type: ignore
# print("后端已启动！")

# process_backend = launch()
process_backend = subprocess.Popen(
    'uvicorn backend:app --reload', stdout=subprocess.PIPE, 
    stderr=subprocess.PIPE,cwd="./blog/backend",shell=True)
process_frontend = subprocess.Popen(
    'npm run dev', stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,cwd="./blog/frontend",shell=True
)
breakpoint()
while backend_info := cleandoc(process_backend.stderr.readline().decode(encoding="GBK")): # type: ignore
    if not backend_info:
        break
    logger.info(backend_info)
logger.info("后端服务已启动")
while frontend_info := cleandoc(process_backend.stderr.readline().decode(encoding="GBK")): # type: ignore
    if not frontend_info:
        break
    logger.info(frontend_info)
logger.info("前端服务已启动")
while True:
    try:
        time.sleep(0.2)
        if output1:= process_backend.stdout.readline().decode(): # type: ignore
            logger.info('BackEnd:'+output1.strip())
        if output2 := process_frontend.stdout.readline().decode():# type: ignore
            logger.info('FrontEnd:'+output2.strip())
        if output1 == '' and output2 == '' and process_backend.poll() is not None and process_frontend.poll() is not None:
            break
    except KeyboardInterrupt:
        logger.warning("用户主动结束了进程")
        break
