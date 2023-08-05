#!python3
from libheader import lh
import os
import sys

if len(sys.argv) != 3:
    print("USAGE: ")
    print("makelh [file.h] [file.c]")
    exit()

with open(sys.argv[1], "r") as f:
    header = f.read()

name = '.'.join(sys.argv[2].split('.')[:-1])

os.system(f"gcc -c {sys.argv[2]} -o temp.o")
os.system(f"ar rcs {name}.lib temp.o")
os.remove("temp.o")

with open(f"{name}.lib", "rb") as f:
    lib = f.read()

os.remove(f"{name}.lib")

a = lh.createLH(header, lib)
with open(name+".lh", "w+") as f:
    f.write(a)