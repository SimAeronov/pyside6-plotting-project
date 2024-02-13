#Project with pyside6

## Running with Python
**Version**
Runs with Python3.12 but for build use: 'py -3.10 -m venv .venv'

**Custom C library builds with:**
x86_64-13.2.0-release-posix-seh-ucrt-rt_v11-rev0.7z

**Build/Install custom library**
inside c_libraries\ use: 'python.exe .\setup.py install'

**Move generated file to lib**
c_._libraries\build\lib...\custom....pyd **->** .venv\Lib\site-packages\custom_math\custom_math.pyd

**custom_math c library**
custom_math.simpsons_rule(x:List\[float\], y:List\[float\]) -> float

