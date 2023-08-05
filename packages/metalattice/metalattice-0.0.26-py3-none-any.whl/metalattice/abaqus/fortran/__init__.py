import gfort2py as gf
import os
from pathlib import Path

from metalattice.abaqus.fortran import lib

# compile fortran code and use gfort2py
cwd = os.getcwd()
current = Path(os.path.dirname(__file__))
code_dir = current.joinpath("code")
bin_dir = current.joinpath("bin")
if not bin_dir.exists():
    os.mkdir(bin_dir)
os.chdir(bin_dir)
if code_dir.exists():
    for f in code_dir.iterdir():
        if f.suffix in [".f", ".for", ".f90"]:
            os.system(f"gfortran -fPIC -shared -c {f.absolute()}")
            os.system(f"gfortran -fPIC -shared -o {f.stem}.so {f.absolute()}")
            libname = str(bin_dir.joinpath(f.with_suffix(".so").name))
            mod_file = str(bin_dir.joinpath(f.with_suffix(".mod").name))
            module = gf.fFort(libname=libname, mod_file=mod_file)
            setattr(lib, str(f.stem), module)
os.chdir(cwd)
