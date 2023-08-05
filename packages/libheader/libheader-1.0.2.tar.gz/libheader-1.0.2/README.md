# Libheader

### lh

A file type that encapsualtes a header (.h), and a static library (.lib/.a)

should be able to be `#include` by normal C, but requires a special linker that can recognize a .lh file

## Example
main.c
```c
#include "sample/test.lh"

int main() {
    testfunc();
    return 0;
}
```

test.h
```h
#include <stdio.h>
void testfunc();
```

test.c
```c
#include "test.h"
void testfunc() { printf("Hello, World!\n"); }
```

 - `makelh test.h test.c` creates a test.lh
 - `gcclh main.c --lh=test.lh -o test.exe` compiles using the test.lh file
