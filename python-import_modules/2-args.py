#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv[1:])
    argv = sys.argv[1:]
    i = 1
    if len(sys.argv[1:]) == 0:
        print(f"{argc} arguments.")
    elif len(sys.argv[1:]) == 1:
        print(f"{argc} argument:")
        while i <= argc:
            print("{:d}: {:s}".format(i, sys.argv[i]))
            i += 1
    elif len(sys.argv[1:]) > 1:
        print(f"{argc} arguments:")
        while i <= argc:
            print("{:d}: {:s}".format(i, sys.argv[i]))
            i += 1
