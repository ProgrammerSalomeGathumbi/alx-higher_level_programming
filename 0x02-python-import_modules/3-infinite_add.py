#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argv = sys.argv[1:]
    result = 0
    for arg in argv:
        result += int(arg)
        print(result)
