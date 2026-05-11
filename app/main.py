import sys
import os
import shutil
import subprocess


def main():
    
    while True:
        sys.stdout.write("$ ")
        user_cmd_arg = input().split(" ")
        user_cmd = user_cmd_arg[0]

        match user_cmd:
            case 'pwd':
                print(os.path.abspath("."))
            case 'type':
                type_arg = user_cmd_arg[1]
                executable = get_executable(type_arg)
                if type_arg in ('echo', 'exit', 'type'):
                    print(f"{type_arg} is a shell builtin")
                elif executable:
                    print(f"{user_cmd_arg[1]} is {executable}")
                else:
                    print(f"{user_cmd_arg[1]} not found")
            case 'echo':
                print(" ".join(user_cmd_arg[1:]))
            case 'exit':
                break
            case _:
                file_path = get_executable(user_cmd)
                if file_path:
                    print(subprocess.run(user_cmd_arg, capture_output=True, text=True).stdout,end="")
                else:
                    print(f"{user_cmd}: command not found")


def get_executable(cmd:str) -> str:
   paths = os.environ["PATH"].split(":")
   for path in paths:
      file_path = os.path.abspath(path) + f"/{cmd}"
      if os.path.isfile(file_path):
        if is_executable(file_path):
          return file_path
        else:
            continue
   return None

def is_executable(file_path:str):
    return shutil.which(file_path)


if __name__ == "__main__":
    main()
