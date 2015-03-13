#include <Python.h>
#include <QtGlobal>

#if PY_MAJOR_VERSION >= 3
extern "C" PyObject *PyInit_QtWidgets(void);
extern "C" PyObject *PyInit_sip(void);
extern "C" PyObject *PyInit_QtGui(void);
extern "C" PyObject *PyInit_QtCore(void);
#if !defined(Q_OS_WIN)
extern "C" PyObject *PyInit__heapq(void);
extern "C" PyObject *PyInit_select(void);
extern "C" PyObject *PyInit__datetime(void);
extern "C" PyObject *PyInit__posixsubprocess(void);
extern "C" PyObject *PyInit__sqlite3(void);
extern "C" PyObject *PyInit_math(void);
extern "C" PyObject *PyInit_time(void);
#endif

static struct _inittab extension_modules[] = {
    {"PyQt5.QtWidgets", PyInit_QtWidgets},
    {"sip", PyInit_sip},
    {"PyQt5.QtGui", PyInit_QtGui},
    {"PyQt5.QtCore", PyInit_QtCore},
#if !defined(Q_OS_WIN)
    {"_heapq", PyInit__heapq},
    {"select", PyInit_select},
    {"_datetime", PyInit__datetime},
    {"_posixsubprocess", PyInit__posixsubprocess},
    {"_sqlite3", PyInit__sqlite3},
    {"math", PyInit_math},
    {"time", PyInit_time},
#endif
    {NULL, NULL}
};
#else
extern "C" void initQtWidgets(void);
extern "C" void initsip(void);
extern "C" void initQtGui(void);
extern "C" void initQtCore(void);
#if !defined(Q_OS_WIN)
extern "C" void init_heapq(void);
extern "C" void initselect(void);
extern "C" void init_datetime(void);
extern "C" void init_posixsubprocess(void);
extern "C" void init_sqlite3(void);
extern "C" void initmath(void);
extern "C" void inittime(void);
#endif

static struct _inittab extension_modules[] = {
    {"PyQt5.QtWidgets", initQtWidgets},
    {"sip", initsip},
    {"PyQt5.QtGui", initQtGui},
    {"PyQt5.QtCore", initQtCore},
#if !defined(Q_OS_WIN)
    {"_heapq", init_heapq},
    {"select", initselect},
    {"_datetime", init_datetime},
    {"_posixsubprocess", init_posixsubprocess},
    {"_sqlite3", init_sqlite3},
    {"math", initmath},
    {"time", inittime},
#endif
    {NULL, NULL}
};
#endif

extern int pyqtdeploy_start(int argc, char **argv,
        struct _inittab *extension_modules, const char *main_module,
        const char *entry_point, const char **path_dirs);

int main(int argc, char **argv)
{
    return pyqtdeploy_start(argc, argv, extension_modules, "__main__", NULL, NULL);
}
