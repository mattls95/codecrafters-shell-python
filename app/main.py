import sys


def main():
    
    while True:
        sys.stdout.write("$ ")
        user_cmd = input()

        match user_cmd:
            case 'exit':
                break

        print(f"{user_cmd}: command not found")


if __name__ == "__main__":
    main()
