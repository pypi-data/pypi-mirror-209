# Libheader

### lh

A file type that encapsualtes a header (.h), and a static library (.lib/.a)

should be able to be `#include` by normal C, but requires a special linker that can recognize a .lh file

for now a python script will convert the .lh to a .lib/.a, but later, I will make a gcc plugin.
