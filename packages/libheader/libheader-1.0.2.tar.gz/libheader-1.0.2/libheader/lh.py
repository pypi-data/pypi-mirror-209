import os
import sys

def hexStrOf(i: int):
    return "{:2X}".format(i)

def createLH(header: str, lib: bytes) -> str:
    h = f"// {os.name}_{sys.platform}\n"
    h += header
    # then add lib file to end of file
    h += "\n/*"

    # add byte data to lib
    for byte in lib:
        h += hexStrOf(byte)

    h += "*/"

    return h

def extractLH(lh: str) -> bytes: # returns the lib file
    # dont need to return the header, because it can be included directly
    lstr = lh.split('\n')[-1]
    if not lstr.startswith("/*") or not lstr.endswith("*/"):
        print("Invalid LH")
        return None
    
    if len(lstr) % 2 != 0:
        print("Invalid LH")
        return None
    lstr = lstr[2:-2]
    lib: list[int] = []
    for i in range(0, len(lstr), 2):
        byt = lstr[i]+lstr[i+1]
        byt = int(byt, 16)
        lib.append(byt)
    return bytes(lib)
