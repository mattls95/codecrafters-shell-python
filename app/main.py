import sys


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
                    print(f"{type_arg}: not found")
            case 'echo':
                print(" ".join(user_cmd_arg[1:]))
            case 'exit':
                break
            case _:
                print(f"{user_cmd}: command not found")


if __name__ == "__main__":
    main()
