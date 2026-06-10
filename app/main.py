import sys
import shlex
from .execute_commands import execute_pwd_cmd, execute_type_cmd, execute_echo_cmd, execute_default, execute_cd_cmd, execute_cat_cmd


def main():
    
    while True:
        sys.stdout.write("$ ")
        try:
            user_input = input()
        except KeyboardInterrupt:
            sys.exit(0)

        user_cmd_arg = shlex.split(user_input)
        user_cmd = user_cmd_arg[0]
  
        match user_cmd:
            case 'pwd':
                execute_pwd_cmd()
            case 'type':
                type_arg = user_cmd_arg[1]
                execute_type_cmd(user_cmd_arg=user_cmd_arg, type_arg=type_arg)
            case 'echo':
                execute_echo_cmd(user_input=user_input)
            case 'cd':
                execute_cd_cmd(path=user_cmd_arg[1])
            case 'cat':
                execute_cat_cmd(user_input=user_input)
            case 'exit':
                break
            case _:
                execute_default(user_cmd_arg=user_cmd_arg, user_cmd=user_cmd)


if __name__ == "__main__":
    main()
