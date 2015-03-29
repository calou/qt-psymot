import sys
from cx_Freeze import setup, Executable

included_files = [("assets", "assets"), ("db/schema.sql", "db/schema.sql"), ("matplotlibrc", "matplotlibrc"),
                  ("../qt.conf", "qt.conf")]
included_packages = ["os", 'time', "sys", "datetime", 'matplotlib.backends.backend_tkagg', 'tkinter',
                     "tkinter.filedialog"]
excluded = ["tcl", "tcl.tzdata", "PyQt4.QtSql", "PyQt4.QtNetwork", "PyQt4.QtTest", "PyQt4.QtXml", "PyQt4.QtScript",
            "PyQt5", "tk", "tk.demos", "tornado", "tk86", "tk8.6", 'pyzmq', 'QScintilla']

build_exe_options = {"packages": included_packages,
                     "excludes": excluded,
                     'include_files': included_files,
                     "optimize": 2}


base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name='Psychomotriciel',
    version='0.1',
    packages=['', 'db', 'gui', 'gui.design', 'gui.window', 'gui.window.stimuli', 'gui.window.patients', 'model',
              'utils'],
    url='',
    license='',
    author='Sébastien Gruchet',
    author_email='gruchet@gmail.com',
    description='',
    options={"build_exe": build_exe_options},

    requires=['pyqt4 (>=4.11)', 'numpy (>=1.9.1)',
              'matplotlib (>=1.4.3)','appdirs (>=1.4.0)'],
    executables=[Executable("application.py", base=base, icon="assets/images/application-icon.ico", compress=True)]
)
