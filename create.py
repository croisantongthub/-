# imports
import subprocess
from pathlib import Path
# tools
def nasm(filename):
  binname = Path("~/bin") / Path(filename).stem 
  subprocess.run(["nasm", filename, "-o", binname])
# code
