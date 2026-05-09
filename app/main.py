import sys


def main():
    
    while True:
        sys.stdout.write("$ ")
        user_cmd_arg = input().split(" ")
        user_cmd = user_cmd_arg[0]

        match user_cmd:
            case 'type':
                if user_cmd_arg[1] in ('echo', 'exit', 'type'):
                    print(f"{user_cmd} is a shell builtin")
            case 'echo':
                print(" ".join(user_cmd_arg[1:]))
            case 'exit':
                break
            case _:
                print(f"{user_cmd}: command not found")


if __name__ == "__main__":
    main()
