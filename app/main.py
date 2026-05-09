import sys
import os
import shutil


def main():
    
    while True:
        sys.stdout.write("$ ")
        user_cmd_arg = input().split(" ")
        user_cmd = user_cmd_arg[0]

        match user_cmd:
            case 'type':
                type_arg = user_cmd_arg[1]
                if type_arg in ('echo', 'exit', 'type'):
                    print(f"{type_arg} is a shell builtin")
                else:
                    search_for_executable(type_arg)
            case 'echo':
                print(" ".join(user_cmd_arg[1:]))
            case 'exit':
                break
            case _:
                print(f"{user_cmd}: command not found")


def search_for_executable(cmd:str) -> None:
   paths = os.environ["PATH"].split(":")
   for path in paths:
      file_path = os.path.abspath(path) + f"/{cmd}"
      if os.path.isfile(file_path):
        if shutil.which(file_path):
          print(f"{cmd} is {file_path}")
          return
        else:
            continue
   print(f"{cmd} not found")


if __name__ == "__main__":
    main()
