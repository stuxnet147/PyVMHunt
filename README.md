# PyVMHunt
Experimental implementation of vmhunt
# Trace
I traced the binary with triton
``` asm
Test1 proc
  db      0ebh, 10h
  dd      20204c57h
  dd      107
  dd      0
  dd      20204c57h
  xor rax, rax
  add rax, 0DEADC0DEh
  add rax, 0DEADC0DEh
  add rax, 0DEADC0DEh
  sub rax, 0DEADC0DEh
  sub rax, 0DEADC0DEh
  sub rax, 0DEADC0DEh
  add rax, 0DEADC0DEh
  db      0ebh, 10h
  dd      20204c57h
  dd      507
  dd      0
  dd      20204c57h
  ret
Test1 endp
```
- https://github.com/stuxnet147/PyVMHunt/releases/download/main/instrace.txt (Themida Fish64 White)
# Reference
- https://dl.acm.org/doi/pdf/10.1145/3243734.3243827
- https://www.youtube.com/watch?v=ovfv3Ph2ajs
- https://github.com/s3team/VMHunt/blob/master/main.cpp
