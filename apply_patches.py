#!/usr/bin/env python3
import sys, os, pathlib, email.parser
from packaging.version import Version
from packaging.specifiers import SpecifierSet

assert len(sys.argv) == 2, f"usage: {sys.argv[0]} MESA_VER"
mesa_ver = Version(sys.argv[1])
parser = email.parser.HeaderParser()

for p in (pathlib.Path(__file__).parent / 'patches').iterdir():
  if mesa_ver in SpecifierSet(parser.parse(p.open()).get('Mesa-Version', '')):
    os.system(f"patch -p1 --fuzz=3 -i {p}")
