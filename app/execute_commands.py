import os
import subprocess
from shlex import split, join, quote
from .get_executable import get_executable


def execute_cd_cmd(path:str) -> None:
    if path.strip() == "~":
        os.chdir(os.environ["HOME"])
        return
    elif os.path.exists(path):
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

def execute_echo_cmd(user_input:str):
    tokens = split(user_input)

    for token in tokens:
        if token.startswith("'") and token.endswith("'"):
            token.replace("'", "")

    print("".join(tokens))
        

def execute_default(user_cmd_arg, user_cmd):
    file_path = get_executable(user_cmd)
    if file_path:
        print(subprocess.run(user_cmd_arg, capture_output=True, text=True).stdout,end="")
    else:
        print(f"{user_cmd}: command not found")