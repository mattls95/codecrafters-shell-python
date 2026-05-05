import sys


def main():
    
    sys.stdout.write("$ ")
    user_cmd = input()
    print(f"{user_cmd}: command not found")


if __name__ == "__main__":
    main()
