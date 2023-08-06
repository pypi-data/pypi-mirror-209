import gfort2py as gf
import os
from pathlib import Path

from metalattice.abaqus.fortran import lib

fortran_src = ["lattice.f"]

current = Path(os.path.dirname(__file__))
code_dir = current.joinpath("code")
bin_dir = current.joinpath("bin")
if not bin_dir.exists():
    os.mkdir(bin_dir)
idx = 0
bin_dir_tmp = bin_dir.joinpath(f"{idx}")


def compile_fortran():  # compile fortran code and use gfort2py
    cwd = os.getcwd()
    if not bin_dir_tmp.exists():
        os.mkdir(bin_dir_tmp)
    os.chdir(bin_dir_tmp)
    if code_dir.exists():
        for f in code_dir.iterdir():
            if f.name in fortran_src:
                os.system(
                    f"gfortran -fPIC -shared -c {f.absolute()}")
                os.system(
                    f"gfortran -fPIC -shared -o {f.stem}.so {f.absolute()}")
        for f in code_dir.iterdir():
            if f.name in fortran_src:
                libname = str(bin_dir_tmp.joinpath(f.with_suffix(".so").name))
                mod_file = str(bin_dir_tmp.joinpath(f.with_suffix(".mod").name))
                module = gf.fFort(libname=libname, mod_file=mod_file)
                setattr(lib, str(f.stem), module)
    os.chdir(cwd)


compile_fortran()
