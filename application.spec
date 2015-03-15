# -*- mode: python -*-
a = Analysis(['application.py'],
             pathex=['C:\\work\\qt-psymot'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=['hook/rthook_pyqt5.py'])
plugins = [("qt5_plugins/platforms/qwindows.dll",
             "C:\\Qt\\Qt5.4.1\\5.4\\msvc2013_64\\plugins\\platforms\\qwindows.dll", "BINARY")]
"""
data = [
  ("qt.conf", "qt.conf", "DATA")
]
"""

pyz = PYZ(a.pure)

exe = EXE(pyz,
          a.scripts,
          a.binaries + plugins,
          a.zipfiles,
          #a.datas + data,
          a.datas,
          name='application.exe',
          debug=True,
          strip=None,
          upx=True,
          console=True )

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='application')
