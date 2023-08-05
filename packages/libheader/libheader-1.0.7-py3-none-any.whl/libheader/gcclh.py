#!python3
from . import lh
import os
import sys

# forward all arguments to gcc, other than custom libs: '--lh=[filename]' if there are spaces in the filename, they must be in quotes
gccargs = sys.argv[1:]
customlibs = []

for arg in gccargs:
    if arg.startswith("--lh="):
        customlibs.append(arg[5:])
        gccargs.remove(arg)
    
i = 0

if os.name == 'nt':
    libname = ".lib"
    libpref = ""
else:
    libname = ".a"
    libpref = "lib"

for l in customlibs:
    with open(l, "r") as f:
        lhsrc = f.read()
    lib = lh.extractLH(lhsrc)
    with open(f"{libpref}temp{i}{libname}", "wb") as f:
        f.write(lib)
    gccargs.append(f"-ltemp{i}")
    i += 1

gccargs.append("-L.")

os.system("gcc "+" ".join(gccargs))

for i in range(len(customlibs)):
    os.remove(f"{libpref}temp{i}{libname}")