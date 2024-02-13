# Plotting Tool Project with PySide6


## Running with Python
**Py Version:**<br>
Runs with Python3.12 but for build use: `py -3.10 -m venv .venv`

**Custom C library builds with:**<br>
[x86_64-13.2.0-release-posix-seh-ucrt-rt_v11-rev0.7z](https://github.com/niXman/mingw-builds-binaries/releases)

**Build/Install custom library:**<br>
inside c_libraries\ use: 'python.exe .\setup.py install'

**Move generated file to lib**<br>
`c_._libraries\build\lib...\custom....pyd` **>** `.venv\Lib\site-packages\custom_math\custom_math.pyd`

**custom_math c library**:<br>
```python
import custom_math
custom_math.simpsons_rule(x:List[float], y:List[float]) -> float
```

## Building executable:
1. `pip install -r dev_requirements.txt`
2. `nuitka.bat --standalone --disable-console --plugin-enable=pyside6 --include-data-dir=resources=resources --include-data-dir=csv_data=csv_data .\main.py`
3. `main.dist/main.exe`

## Build setup file:
1. Install and run [Inno Setup](https://jrsoftware.org/isinfo.php)
2. Create script file using Script Wizard
3. Add path to main.exe, files and folders (include files [yes])
4. Deselect "Associate a file type to the main executable"
5. Do not compile script now!
6. Go to [FILES] section and change folders' DestDir to: {app}/folder_name
7. Save and compile the InnoSetupScript.iss



## Future work:
1. Fix issue with .csv not having headers
2. Fix plot buttons size/font
3. Add better status bar to handle user errors
4. Check Pyside QSS hex color issue 
5. Add .exe icon

