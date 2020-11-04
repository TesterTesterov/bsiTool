import cx_Freeze
import sys

base = None 

if sys.platform=='win32':
    base = "Win32GUI"


executables = [cx_Freeze.Executable("bsitool.py")]    

cx_Freeze.setup(
        name = "Name",
        options = {"build_exe":{"packages":["sys"]}},
        version="1",
        executables=executables) 