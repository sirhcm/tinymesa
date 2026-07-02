#!/usr/bin/env python3
import argparse, pathlib, shutil, tempfile
from distlib.wheel import Wheel

parser = argparse.ArgumentParser()
parser.add_argument("--tag")
parser.add_argument("--sha")
parser.add_argument("--platform", required=True)
parser.add_argument("mesa_tag")

args, files = parser.parse_known_args()
if args.tag: assert args.tag.startswith('v') and args.tag[1:].isdigit(), "expected tag of form 'vN'"
else: assert args.sha, "expected one of --tag or --sha to be set"

version = args.mesa_tag.split('-')[1] + (f".{args.tag[1:]}" if args.tag else f"+{args.sha}")
files = [pathlib.Path(f) for f in files]

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
  outfile = wheel.build({"prefix": str(prefix), "platlib": str(platlib)}, tags={"pyver": ["py3"], "abi": ["none"], "arch": [args.platform]})
  print(f"successfully build {outfile}")
