TEMPLATE = app

win32 {
    ASM = $$find(SOURCES, ^.*\.asm$)
    SOURCES -= $$ASM

    masm.input = ASM
    masm.output = ${QMAKE_FILE_BASE}.obj

    contains(QMAKE_TARGET.arch, x86_64) {
        CONFIG += win32_x64
        masm.name = MASM64 compiler
        masm.commands = ml64 /Fo ${QMAKE_FILE_OUT} /c ${QMAKE_FILE_IN}
    } else {
        CONFIG += win32_x86
        masm.name = MASM compiler
        masm.commands = ml /Fo ${QMAKE_FILE_OUT} /c ${QMAKE_FILE_IN}
    }

    QMAKE_EXTRA_COMPILERS += masm
}

CONFIG += warn_off release

RESOURCES = \
    resources/pyqtdeploy.qrc

SOURCES = pyqtdeploy_main.cpp pyqtdeploy_start.cpp pdytools_module.cpp
DEFINES += PYQTDEPLOY_FROZEN_MAIN
DEFINES += PYQTDEPLOY_OPTIMIZED
HEADERS = pyqtdeploy_version.h frozen_bootstrap.h frozen_main.h

INCLUDEPATH += C:/Python34/src/Python-3.4.3/Include
LIBS += -LC:/Python34/Lib/site-packages -lsip
LIBS += -lsqlite3
LIBS += -LC:/Python34/Lib/site-packages/PyQt5 -lQtWidgets -lQtGui -lQtCore
LIBS += -LC:/Python34/DLLs -lpython3

!win32 {
    DEFINES += MODULE_NAME=\\\"sqlite3\\\"
    DEFINES += SQLITE_OMIT_LOAD_EXTENSION
    INCLUDEPATH += C:/Python34/src/Python-3.4.3/Modules
    INCLUDEPATH += C:/Python34/src/Python-3.4.3/Modules/_sqlite
    SOURCES += C:/Python34/src/Python-3.4.3/Modules/_heapqmodule.c
    SOURCES += C:/Python34/src/Python-3.4.3/Modules/_sqlite/cache.c
    SOURCES += C:/Python34/src/Python-3.4.3/Modules/_sqlite/connection.c
    SOURCES += C:/Python34/src/Python-3.4.3/Modules/_math.c
    SOURCES += C:/Python34/src/Python-3.4.3/Modules/selectmodule.c
    SOURCES += C:/Python34/src/Python-3.4.3/Modules/_sqlite/microprotocols.c
    SOURCES += C:/Python34/src/Python-3.4.3/Modules/_sqlite/prepare_protocol.c
    SOURCES += C:/Python34/src/Python-3.4.3/Modules/_sqlite/statement.c
    SOURCES += C:/Python34/src/Python-3.4.3/Modules/_datetimemodule.c
    SOURCES += C:/Python34/src/Python-3.4.3/Modules/timemodule.c
    SOURCES += C:/Python34/src/Python-3.4.3/Modules/_sqlite/row.c
    SOURCES += C:/Python34/src/Python-3.4.3/Modules/mathmodule.c
    SOURCES += C:/Python34/src/Python-3.4.3/Modules/_posixsubprocess.c
    SOURCES += C:/Python34/src/Python-3.4.3/Modules/_sqlite/util.c
    SOURCES += C:/Python34/src/Python-3.4.3/Modules/_sqlite/module.c
    SOURCES += C:/Python34/src/Python-3.4.3/Modules/_sqlite/cursor.c
}

linux-* {
    LIBS += -lutil -ldl
}

win32 {
    LIBS += -ladvapi32 -lshell32 -luser32 -lws2_32 -lole32 -loleaut32
    DEFINES += MS_WINDOWS _WIN32_WINNT=Py_WINVER NTDDI_VERSION=Py_NTDDI WINVER=Py_WINVER

    # This is added from the qmake spec files but clashes with _pickle.c.
    DEFINES -= UNICODE
}

macx {
    LIBS += -framework SystemConfiguration -framework CoreFoundation
}
