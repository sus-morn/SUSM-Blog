"""启动后端"""
import subprocess

def launch():
    """启动后端"""
    with subprocess.Popen(
        'pdm run uvicorn __init__:app --reload', stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE,cwd=".",shell=True) as process_backend:
        print(process_backend.stderr.readline().decode()) # type: ignore
        print("后端服务已启动")
        return process_backend
