#!/usr/bin/env python3
import pathlib, sys, shutil, tempfile
from distlib.wheel import Wheel

assert len(sys.argv) > 3, f"usage: {sys.argv[0]} MESA_TAG VERSION FILES..."
version = f"{sys.argv[1].split('-')[1]}.{sys.argv[2]}"
files = [pathlib.Path(f) for f in sys.argv[3:]]

init = "\n".join(["import pathlib", "root = pathlib.Path(__file__).parent"] +
                 [f"{f.stem} = root / {f.name!r}" for f in files] + ["__all__ = [" + ", ".join([repr(f.stem) for f in files]) + "]"])
meta = f"""Metadata-Version: 2.1
Name: tinymesa
Version: {version}
Summary: mesa, but tiny
Requires-Python: >=3.8
"""

with tempfile.TemporaryDirectory() as td:
  prefix = pathlib.Path(td)
  platlib = prefix / "platlib"
  (platlib / "tinymesa").mkdir(parents=True, exist_ok=True)
  (platlib / "tinymesa/__init__.py").write_text(init)
  for f in files: shutil.copy(f, platlib / "tinymesa" / f.name)
  (platlib / f"tinymesa.dist-info").mkdir()
  (platlib / f"tinymesa.dist-info/METADATA").write_text(meta)

  wheel = Wheel()
  pathlib.Path("dist").mkdir(exist_ok=True)
  wheel.name, wheel.version, wheel.dirname = "tinymesa", version, "dist"
  outfile = wheel.build({"prefix": str(prefix), "platlib": str(platlib)}, tags={"pyver": ["py3"], "abi": ["none"]})
  print(f"successfully build {outfile}")
