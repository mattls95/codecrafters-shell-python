import sys
import subprocess
from get_executable import get_executable
from execute_commands import execute_pwd_cmd, execute_type_cmd, execute_echo_cmd, execute_default, execute_cd_cmd


def main():
    
    while True:
        sys.stdout.write("$ ")
        user_cmd_arg = input().split(" ")
        user_cmd = user_cmd_arg[0]

        match user_cmd:
            case 'pwd':
                execute_pwd_cmd()
            case 'type':
                type_arg = user_cmd_arg[1]
                execute_type_cmd(user_cmd_arg, type_arg)
            case 'echo':
                execute_echo_cmd(user_cmd_arg)
            case 'cd':
                execute_cd_cmd(path=user_cmd_arg[1])
            case 'exit':
                break
            case _:
                execute_default(user_cmd, user_cmd_arg)


if __name__ == "__main__":
    main()
