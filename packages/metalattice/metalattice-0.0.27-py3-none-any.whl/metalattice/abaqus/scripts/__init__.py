import os
from pathlib import Path

from metalattice.abaqus import abaqus_cmd

current = Path(os.path.dirname(__file__))


def run_abaqus_script(
    script_file: str
):
    suffix = ".py"
    script = Path(script_file)
    if script.suffix != suffix:
        script = script.with_suffix(suffix)
    if not script.is_file():
        script = current.joinpath(script.name)
    assert script.is_file()
    cmd = abaqus_cmd + f" python {script.absolute()}"
    os.system(cmd)
