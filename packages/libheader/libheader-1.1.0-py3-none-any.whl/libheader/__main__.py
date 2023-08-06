import sys

if len(sys.argv) > 1:
    if sys.argv[1] == "gcc":
        sys.argv = sys.argv[1:]
        from . import gcclh
    elif sys.argv[1] == "lib" or sys.argv[1] == "make":
        sys.argv = sys.argv[1:]
        from . import makelh
