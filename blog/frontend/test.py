import subprocess

# 定义要运行的命令
command = ["npm", "run", "dev"]

# 使用 subprocess.Popen 运行命令
process = subprocess.Popen(
    "npm run dev", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
)

# 实时读取输出
while True:
    output = process.stdout.readline()
    if output == "" and process.poll() is not None:
        break
    if output:
        print(output.strip())

# 捕获标准错误
stderr = process.stderr.read()
if stderr:
    print("标准错误:")
    print(stderr)

# 打印你好世界
print("hello,world")
