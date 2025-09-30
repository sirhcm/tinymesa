# tinymesa

provides a subset of mesa's `libvulkan` with vastly fewer dependencies.

```
$ lddtree libtinymesa.so
libtinymesa.so (interpreter => None)
    libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6
    libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1
    libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6
    ld-linux-x86-64.so.2 => /lib/x86_64-linux-gnu/ld-linux-x86-64.so.2
$ lddtree libtinymesa_cpu.so
libtinymesa_cpu.so (interpreter => None)
    libLLVM.so.20.1 => /lib/x86_64-linux-gnu/libLLVM.so.20.1
        libffi.so.8 => /lib/x86_64-linux-gnu/libffi.so.8
        libedit.so.2 => /lib/x86_64-linux-gnu/libedit.so.2
            libtinfo.so.6 => /lib/x86_64-linux-gnu/libtinfo.so.6
            libbsd.so.0 => /lib/x86_64-linux-gnu/libbsd.so.0
                libmd.so.0 => /lib/x86_64-linux-gnu/libmd.so.0
        libz.so.1 => /lib/x86_64-linux-gnu/libz.so.1
        libzstd.so.1 => /lib/x86_64-linux-gnu/libzstd.so.1
        libxml2.so.2 => /lib/x86_64-linux-gnu/libxml2.so.2
            libicuuc.so.74 => /lib/x86_64-linux-gnu/libicuuc.so.74
                libicudata.so.74 => /lib/x86_64-linux-gnu/libicudata.so.74
            liblzma.so.5 => /lib/x86_64-linux-gnu/liblzma.so.5
    libstdc++.so.6 => /lib/x86_64-linux-gnu/libstdc++.so.6
    libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6
    libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1
    libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6
    ld-linux-x86-64.so.2 => /lib/x86_64-linux-gnu/ld-linux-x86-64.so.2
```

`libtinymesa.so` contains all symbols from `libnir`, and a subset of symbols
from `libnak` (see release notes for a list). `libtinymesa_cpu.so` contains
all these symbols, but in addition, a subset of symbols from `libgallium`
(see release notes), and as a result depends on LLVM-20.

Builds are automatically generated upon new releases of mesa (checked daily).

