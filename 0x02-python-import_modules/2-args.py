#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]
    if len(argv) == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(len(argv)))
    for i, arg in enumerate(argv):
        print("{}: {}".format(i + 1, arg))
