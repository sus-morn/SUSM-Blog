"""启动后端"""
import subprocess

def launch():
    """启动后端"""
    process_backend = subprocess.Popen(
        'pdm run uvicorn __init__:app --reload', stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE,cwd=".",shell=True)
    print(process_backend.stderr.readline().decode()) # type: ignore
    return process_backend
