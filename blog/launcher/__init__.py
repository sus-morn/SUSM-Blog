import subprocess
import threading
from .logger import logger
from inspect import cleandoc


def launcher(cmd: str, cwd: str):
    return subprocess.Popen(
        cmd,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        cwd=cwd,
        shell=True,
    )


def _logger_wrapper(func):
    def wrapper(launcher,name: str):
        while True:
            info = func(launcher)
            try:
                logger.info(cleandoc(name+": "+info.decode(encoding="GBK")))
            except UnicodeDecodeError:
                logger.info(cleandoc(name+": "+info.decode(encoding="utf-8")))
    return wrapper

@_logger_wrapper
def _get_output_err(launcher):
    return launcher.stderr.readline()


@_logger_wrapper
def _get_output_out(launcher):
    return launcher.stdout.readline()


def get_output(launcher, name: str):

    threads = [
        threading.Thread(target=_get_output_err, args=(launcher, name)),
        threading.Thread(target=_get_output_out, args=(launcher, name)),
    ]
    for i in threads:
        i.start()
        # i.join()

try:

    threads = []
    cmds = {
        "./blog/backend": ["uvicorn backend:app --reload", "Backend"],
        "./blog/frontend": ["npm run dev", "Frontend"],
    }
    for i in cmds:
        t = threading.Thread(
            target=get_output, args=(launcher(cmds[i][0], i), cmds[i][1])
        )
        logger.info(f"启动{cmds[i][1]}服务")
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()
except KeyboardInterrupt:
    raise KeyboardInterrupt


"""
遗存方案1
完全不能用👇
"""

# process_backend = subprocess.Popen(
#     'uvicorn backend:app --reload', stdout=subprocess.PIPE,
#     stderr=subprocess.PIPE,cwd="./blog/backend",shell=True)
# process_frontend = subprocess.Popen(
#     'npm run dev', stdout=subprocess.PIPE,
#     stderr=subprocess.PIPE,cwd="./blog/frontend",shell=True
# )
# while backend_info := cleandoc(process_backend.stderr.readline().decode(encoding="GBK")): # type: ignore
#     if not backend_info:
#         break
#     logger.info(backend_info)
# logger.info("后端服务已启动")
# while frontend_info := cleandoc(process_backend.stderr.readline().decode(encoding="GBK")): # type: ignore
#     if not frontend_info:
#         break
#     logger.info(frontend_info)
# logger.info("前端服务已启动")
# while True:
#     try:
#         time.sleep(0.2)
#         if output1:= process_backend.stdout.readline().decode(): # type: ignore
#             logger.info('BackEnd:'+output1.strip())
#         if output2 := process_frontend.stdout.readline().decode():# type: ignore
#             logger.info('FrontEnd:'+output2.strip())
#         if output1 == '' and output2 == '' and process_backend.poll() is not None and process_frontend.poll() is not None:
#             break
#     except KeyboardInterrupt:
#         logger.warning("用户主动结束了进程")
#         break
