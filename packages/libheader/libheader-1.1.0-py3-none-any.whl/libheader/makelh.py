#!python3
from . import lh
import os
import sys

if len(sys.argv) < 3:
    print("USAGE: ")
    print("makelh [file.h] [*.c]")
    exit()

with open(sys.argv[1], "r") as f:
    header = f.read()

name = '.'.join(sys.argv[1].split('.')[:-1])

for i in sys.argv[2:]:
    os.system(f"gcc -c {i} -o {i}.o")
os.system(f"ar rcs {name}.lib {' '.join([i+'.o' for i in sys.argv[2:]])}")
for i in sys.argv[2:]:
    os.remove(f"{i}.o")

with open(f"{name}.lib", "rb") as f:
    lib = f.read()

os.remove(f"{name}.lib")

a = lh.createLH(header, lib)
with open(name+".lh", "w+") as f:
    f.write(a)