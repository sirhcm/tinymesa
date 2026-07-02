#!/usr/bin/env python3
import shutil, sys, subprocess, pathlib, platform, email.parser
from packaging.version import Version
from packaging.specifiers import SpecifierSet

assert len(sys.argv) == 3, f"usage: {sys.argv[0]} MESA_DIR MESA_TAG"
mesa_dir = pathlib.Path(sys.argv[1])
mesa_ver = Version(sys.argv[2].split('-')[1])
parser = email.parser.HeaderParser()

def system(cmd): subprocess.run(cmd.split(), check=True, cwd=mesa_dir)

for p in (pathlib.Path(__file__).parent / 'patches').iterdir():
  if mesa_ver in SpecifierSet(parser.parse(p.open()).get('Mesa-Version', '')):
    system(f"patch -p1 --fuzz=3 -i {p}")

if platform.system() == "Darwin": (mesa_dir / "include/xf86drm.h").touch()

for p in [mesa_dir / "src" / s / "meson.build" for s in ["compiler", "compiler/nir", "gallium/auxiliary", "nouveau/compiler", "util", "freedreno/ir3", "freedreno/common"]]:
  p.write_text("\n".join(filter(lambda l: "gnu_symbol_visibility" not in l, p.read_text().splitlines())))

with (mesa_dir / "src/meson.build").open("a") as f: f.write("subdir('tinymesa')\n")

(mesa_dir / "src/tinymesa").mkdir(exist_ok=True)
shutil.copy(repo / "meson.build", mesa_dir / "src/tinymesa/meson.build")
