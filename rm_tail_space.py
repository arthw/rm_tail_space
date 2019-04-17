#!/usr/bin/python3
import sys
import os
import random
import shutil

def help():

    print("\nHelp:")
    print("    rm_tail_space will remove the tailling space of text file")
    print("\nUsage:\n    %s filename" % sys.argv[0])
    print("\nCopyright:\n    Free software, developed by Jianyu Zhang, zhang.jianyu@outlook.com")

def rm_tail_space(filename):
    tmp = "/tmp/rm_tail_space_%06d" % random.randint(1, 1000)
    with open(tmp, "w") as out:
        with open(filename, "r") as f:
            while True:
                line = f.readline()
                if line=="":
                    break
                line = line.rstrip()
                out.write(line+"\n")

    shutil.copyfile(tmp, filename)
    os.remove(tmp)
    print("Done!")


if __name__ == "__main__":
    if len(sys.argv)<2:
        help()
        sys.exit(1)

    p1 = sys.argv[1]
    p_help = p1..lower()
    if p_help == 'h' or p_help =="help":
        help()
        sys.exit(0)

    if not os.path.exists(p1):
        print("No exists file %s" % p1)
        help()
        sys.exit(1)

    sys.exit(rm_tail_space(p1))

