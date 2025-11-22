# tinymesa

Provides a subset of mesa's compiler infrastructure with vastly fewer dependencies.

Supports the following targets:
  - Kepler and later NVIDIA GPUs (via NAK)
  - Adreno a3xx and newer (via IR3)
  - LLVM (via LLVMpipe)

### mesa:
```
$ lddtree libvulkan_lvp.so
libvulkan_lvp.so (interpreter => None)
    libLLVM.so.20.1 => /lib/x86_64-linux-gnu/libLLVM.so.20.1
        libffi.so.8 => /lib/x86_64-linux-gnu/libffi.so.8
        libedit.so.2 => /lib/x86_64-linux-gnu/libedit.so.2
            libtinfo.so.6 => /lib/x86_64-linux-gnu/libtinfo.so.6
            libbsd.so.0 => /lib/x86_64-linux-gnu/libbsd.so.0
                libmd.so.0 => /lib/x86_64-linux-gnu/libmd.so.0
        libxml2.so.2 => /lib/x86_64-linux-gnu/libxml2.so.2
            libicuuc.so.74 => /lib/x86_64-linux-gnu/libicuuc.so.74
                libicudata.so.74 => /lib/x86_64-linux-gnu/libicudata.so.74
            liblzma.so.5 => /lib/x86_64-linux-gnu/liblzma.so.5
        ld-linux-x86-64.so.2 => /lib/x86_64-linux-gnu/ld-linux-x86-64.so.2
    libz.so.1 => /lib/x86_64-linux-gnu/libz.so.1
    libzstd.so.1 => /lib/x86_64-linux-gnu/libzstd.so.1
    libdrm.so.2 => /lib/x86_64-linux-gnu/libdrm.so.2
    libexpat.so.1 => /lib/x86_64-linux-gnu/libexpat.so.1
    libxcb.so.1 => /lib/x86_64-linux-gnu/libxcb.so.1
        libXau.so.6 => /lib/x86_64-linux-gnu/libXau.so.6
        libXdmcp.so.6 => /lib/x86_64-linux-gnu/libXdmcp.so.6
    libxcb-randr.so.0 => /lib/x86_64-linux-gnu/libxcb-randr.so.0
    libX11-xcb.so.1 => /lib/x86_64-linux-gnu/libX11-xcb.so.1
    libxcb-dri3.so.0 => /lib/x86_64-linux-gnu/libxcb-dri3.so.0
    libxcb-present.so.0 => /lib/x86_64-linux-gnu/libxcb-present.so.0
    libxcb-xfixes.so.0 => /lib/x86_64-linux-gnu/libxcb-xfixes.so.0
    libxcb-sync.so.1 => /lib/x86_64-linux-gnu/libxcb-sync.so.1
    libxcb-shm.so.0 => /lib/x86_64-linux-gnu/libxcb-shm.so.0
    libxshmfence.so.1 => /lib/x86_64-linux-gnu/libxshmfence.so.1
    libwayland-client.so.0 => /lib/x86_64-linux-gnu/libwayland-client.so.0
    libstdc++.so.6 => /lib/x86_64-linux-gnu/libstdc++.so.6
    libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6
    libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1
    libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6
```
### tinymesa:
```
$ lddtree libtinymesa.so
libtinymesa-mesa-25.2.7-linux-amd64.so (interpreter => None)
    libz.so.1 => /lib/x86_64-linux-gnu/libz.so.1
    libzstd.so.1 => /lib/x86_64-linux-gnu/libzstd.so.1
    libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6
    libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1
    libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6
    ld-linux-x86-64.so.2 => /lib/x86_64-linux-gnu/ld-linux-x86-64.so.2
```
### tinymesa (with LLVMpipe support):
```
libtinymesa_cpu.so (interpreter => None)
    libz.so.1 => /lib/x86_64-linux-gnu/libz.so.1
    libzstd.so.1 => /lib/x86_64-linux-gnu/libzstd.so.1
    libLLVM.so.20.1 => /lib/x86_64-linux-gnu/libLLVM.so.20.1
        libffi.so.8 => /lib/x86_64-linux-gnu/libffi.so.8
        libedit.so.2 => /lib/x86_64-linux-gnu/libedit.so.2
            libtinfo.so.6 => /lib/x86_64-linux-gnu/libtinfo.so.6
            libbsd.so.0 => /lib/x86_64-linux-gnu/libbsd.so.0
                libmd.so.0 => /lib/x86_64-linux-gnu/libmd.so.0
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

`libtinymesa.so` contains all symbols from `nir`, and a subset of symbols
from `nak` and `freedreno` (see release notes for a list). `libtinymesa_cpu.so` contains
all these symbols, but in addition, a subset of symbols from `gallium`
(see release notes), and as a result depends on LLVM-20.

Builds are automatically generated upon new releases of mesa (checked daily).
