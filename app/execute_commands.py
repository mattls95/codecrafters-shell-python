import os.path
import subprocess
from .get_executable import get_executable


def execute_cd_cmd(path:str) -> None:
  if os.path.exists(path):
      os.chdir(path)
      return
  print(f"{path}: No such file or directory")

def execute_pwd_cmd() -> None:
    print(os.path.abspath("."))

def execute_type_cmd(user_cmd_arg, type_arg):
    executable = get_executable(type_arg)
    if type_arg in ('echo', 'exit', 'type', 'pwd'):
        print(f"{type_arg} is a shell builtin")
    elif executable:
        print(f"{user_cmd_arg[1]} is {executable}")
    else:
        print(f"{user_cmd_arg[1]} not found")

def execute_echo_cmd(user_cmd_arg):
    print(" ".join(user_cmd_arg[1:]))

def execute_default(user_cmd_arg, user_cmd):
    file_path = get_executable(user_cmd)
    if file_path:
        print(subprocess.run(user_cmd_arg, capture_output=True, text=True).stdout,end="")
    else:
        print(f"{user_cmd}: command not found")