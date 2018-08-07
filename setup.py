from cx_Freeze import setup, Executable

base = None    

executables = [Executable("ADI.py", base=base)]

packages = ["idna", "os", "sys", "zipfile", "configparser", "pickle"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Alternate Daz Installer",
    options = options,
    version = "1",
    description = 'A Commandline interface for installing and uninstall DAZ Studio Assets.',
    executables = executables
)