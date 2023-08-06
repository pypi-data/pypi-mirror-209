
// default includes
#include <shiboken.h>
#ifndef QT_NO_VERSION_TAGGING
#  define QT_NO_VERSION_TAGGING
#endif
#include <QtCore/QDebug>
#include <pysideqobject.h>
#include <pysidesignal.h>
#include <pysideproperty.h>
#include <signalmanager.h>
#include <pysidemetafunction.h>
#include <pysideqenum.h>
#include <pysideqflags.h>
#include <pysideqmetatype.h>
#include <pysideutils.h>
#include <feature_select.h>
QT_WARNING_DISABLE_DEPRECATED


// module include
#include "qprogressindicator_python.h"

// main header
#include "qprogressindicator_wrapper.h"

#include <algorithm>
#include <cctype>
#include <cstring>
#include <iterator>
#include <set>
#include <typeinfo>

template <class T>
static const char *typeNameOf(const T &t)
{
    const char *typeName =  typeid(t).name();
    auto size = std::strlen(typeName);
#if defined(Q_CC_MSVC) // MSVC: "class QPaintDevice * __ptr64"
    if (auto lastStar = strchr(typeName, '*')) {
        // MSVC: "class QPaintDevice * __ptr64"
        while (*--lastStar == ' ') {
        }
        size = lastStar - typeName + 1;
    }
#else // g++, Clang: "QPaintDevice *" -> "P12QPaintDevice"
    if (size > 2 && typeName[0] == 'P' && std::isdigit(typeName[1])) {
        ++typeName;
        --size;
    }
#endif
    char *result = new char[size + 1];
    result[size] = '\0';
    memcpy(result, typeName, size);
    return result;
}

// Native ---------------------------------------------------------

void QProgressIndicatorWrapper::pysideInitQtMetaTypes()
{
}

void QProgressIndicatorWrapper::resetPyMethodCache()
{
    std::fill_n(m_PyMethodCache, sizeof(m_PyMethodCache) / sizeof(m_PyMethodCache[0]), false);
}

QProgressIndicatorWrapper::QProgressIndicatorWrapper(QWidget * parent) : QProgressIndicator(parent)
{
    resetPyMethodCache();
    // ... middle
}

void QProgressIndicatorWrapper::actionEvent(QActionEvent * event)
{
    if (m_PyMethodCache[0]) {
        return this->::QWidget::actionEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "actionEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[0] = true;
        gil.release();
        return this->::QWidget::actionEvent(event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtGuiTypes[SBK_QACTIONEVENT_IDX], event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

void QProgressIndicatorWrapper::changeEvent(QEvent * event)
{
    if (m_PyMethodCache[1]) {
        return this->::QWidget::changeEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "changeEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[1] = true;
        gil.release();
        return this->::QWidget::changeEvent(event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtCoreTypes[SBK_QEVENT_IDX], event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

void QProgressIndicatorWrapper::childEvent(QChildEvent * event)
{
    if (m_PyMethodCache[2]) {
        return this->::QObject::childEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "childEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[2] = true;
        gil.release();
        return this->::QObject::childEvent(event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtCoreTypes[SBK_QCHILDEVENT_IDX], event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

void QProgressIndicatorWrapper::closeEvent(QCloseEvent * event)
{
    if (m_PyMethodCache[3]) {
        return this->::QWidget::closeEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "closeEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[3] = true;
        gil.release();
        return this->::QWidget::closeEvent(event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtGuiTypes[SBK_QCLOSEEVENT_IDX], event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

void QProgressIndicatorWrapper::connectNotify(const QMetaMethod & signal)
{
    if (m_PyMethodCache[4]) {
        return this->::QObject::connectNotify(signal);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "connectNotify";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[4] = true;
        gil.release();
        return this->::QObject::connectNotify(signal);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::copyToPython(SbkPySide6_QtCoreTypes[SBK_QMETAMETHOD_IDX], &signal)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

void QProgressIndicatorWrapper::contextMenuEvent(QContextMenuEvent * event)
{
    if (m_PyMethodCache[5]) {
        return this->::QWidget::contextMenuEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "contextMenuEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[5] = true;
        gil.release();
        return this->::QWidget::contextMenuEvent(event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtGuiTypes[SBK_QCONTEXTMENUEVENT_IDX], event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

void QProgressIndicatorWrapper::customEvent(QEvent * event)
{
    if (m_PyMethodCache[6]) {
        return this->::QObject::customEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "customEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[6] = true;
        gil.release();
        return this->::QObject::customEvent(event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtCoreTypes[SBK_QEVENT_IDX], event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

int QProgressIndicatorWrapper::devType() const
{
    if (m_PyMethodCache[7])
        return this->::QWidget::devType();
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return 0;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "devType";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[7] = true;
        gil.release();
        return this->::QWidget::devType();
    }

    Shiboken::AutoDecRef pyArgs(PyTuple_New(0));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return 0;
    }
    // Check return type
    Shiboken::Conversions::PythonToCppConversion pythonToCpp =
        Shiboken::Conversions::pythonToCppConversion(Shiboken::Conversions::PrimitiveTypeConverter<int>(), pyResult);
    if (!pythonToCpp) {
        Shiboken::Warnings::warnInvalidReturnValue("QProgressIndicator", "devType", "int", Py_TYPE(pyResult)->tp_name);
        return 0;
    }
    int cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QProgressIndicatorWrapper::disconnectNotify(const QMetaMethod & signal)
{
    if (m_PyMethodCache[8]) {
        return this->::QObject::disconnectNotify(signal);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "disconnectNotify";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[8] = true;
        gil.release();
        return this->::QObject::disconnectNotify(signal);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::copyToPython(SbkPySide6_QtCoreTypes[SBK_QMETAMETHOD_IDX], &signal)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

void QProgressIndicatorWrapper::dragEnterEvent(QDragEnterEvent * event)
{
    if (m_PyMethodCache[9]) {
        return this->::QWidget::dragEnterEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "dragEnterEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[9] = true;
        gil.release();
        return this->::QWidget::dragEnterEvent(event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtGuiTypes[SBK_QDRAGENTEREVENT_IDX], event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

void QProgressIndicatorWrapper::dragLeaveEvent(QDragLeaveEvent * event)
{
    if (m_PyMethodCache[10]) {
        return this->::QWidget::dragLeaveEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "dragLeaveEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[10] = true;
        gil.release();
        return this->::QWidget::dragLeaveEvent(event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtGuiTypes[SBK_QDRAGLEAVEEVENT_IDX], event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

void QProgressIndicatorWrapper::dragMoveEvent(QDragMoveEvent * event)
{
    if (m_PyMethodCache[11]) {
        return this->::QWidget::dragMoveEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "dragMoveEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[11] = true;
        gil.release();
        return this->::QWidget::dragMoveEvent(event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtGuiTypes[SBK_QDRAGMOVEEVENT_IDX], event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

void QProgressIndicatorWrapper::dropEvent(QDropEvent * event)
{
    if (m_PyMethodCache[12]) {
        return this->::QWidget::dropEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "dropEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[12] = true;
        gil.release();
        return this->::QWidget::dropEvent(event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtGuiTypes[SBK_QDROPEVENT_IDX], event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

void QProgressIndicatorWrapper::enterEvent(QEnterEvent * event)
{
    if (m_PyMethodCache[13]) {
        return this->::QWidget::enterEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "enterEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[13] = true;
        gil.release();
        return this->::QWidget::enterEvent(event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtGuiTypes[SBK_QENTEREVENT_IDX], event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

bool QProgressIndicatorWrapper::event(QEvent * event)
{
    if (m_PyMethodCache[14])
        return this->::QWidget::event(event);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return false;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "event";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[14] = true;
        gil.release();
        return this->::QWidget::event(event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtCoreTypes[SBK_QEVENT_IDX], event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return false;
    }
    // Check return type
    Shiboken::Conversions::PythonToCppConversion pythonToCpp =
        Shiboken::Conversions::pythonToCppConversion(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), pyResult);
    if (!pythonToCpp) {
        Shiboken::Warnings::warnInvalidReturnValue("QProgressIndicator", "event", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

bool QProgressIndicatorWrapper::eventFilter(QObject * watched, QEvent * event)
{
    if (m_PyMethodCache[15])
        return this->::QObject::eventFilter(watched, event);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return false;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "eventFilter";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[15] = true;
        gil.release();
        return this->::QObject::eventFilter(watched, event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(NN)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtCoreTypes[SBK_QOBJECT_IDX], watched),
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtCoreTypes[SBK_QEVENT_IDX], event)
    ));
    bool invalidateArg2 = PyTuple_GET_ITEM(pyArgs, 1)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (invalidateArg2)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 1));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return false;
    }
    // Check return type
    Shiboken::Conversions::PythonToCppConversion pythonToCpp =
        Shiboken::Conversions::pythonToCppConversion(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), pyResult);
    if (!pythonToCpp) {
        Shiboken::Warnings::warnInvalidReturnValue("QProgressIndicator", "eventFilter", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QProgressIndicatorWrapper::focusInEvent(QFocusEvent * event)
{
    if (m_PyMethodCache[16]) {
        return this->::QWidget::focusInEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "focusInEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[16] = true;
        gil.release();
        return this->::QWidget::focusInEvent(event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtGuiTypes[SBK_QFOCUSEVENT_IDX], event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

bool QProgressIndicatorWrapper::focusNextPrevChild(bool next)
{
    if (m_PyMethodCache[17])
        return this->::QWidget::focusNextPrevChild(next);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return false;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "focusNextPrevChild";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[17] = true;
        gil.release();
        return this->::QWidget::focusNextPrevChild(next);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), &next)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return false;
    }
    // Check return type
    Shiboken::Conversions::PythonToCppConversion pythonToCpp =
        Shiboken::Conversions::pythonToCppConversion(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), pyResult);
    if (!pythonToCpp) {
        Shiboken::Warnings::warnInvalidReturnValue("QProgressIndicator", "focusNextPrevChild", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QProgressIndicatorWrapper::focusOutEvent(QFocusEvent * event)
{
    if (m_PyMethodCache[18]) {
        return this->::QWidget::focusOutEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "focusOutEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[18] = true;
        gil.release();
        return this->::QWidget::focusOutEvent(event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtGuiTypes[SBK_QFOCUSEVENT_IDX], event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

bool QProgressIndicatorWrapper::hasHeightForWidth() const
{
    if (m_PyMethodCache[19])
        return this->::QWidget::hasHeightForWidth();
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return false;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "hasHeightForWidth";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[19] = true;
        gil.release();
        return this->::QWidget::hasHeightForWidth();
    }

    Shiboken::AutoDecRef pyArgs(PyTuple_New(0));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return false;
    }
    // Check return type
    Shiboken::Conversions::PythonToCppConversion pythonToCpp =
        Shiboken::Conversions::pythonToCppConversion(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), pyResult);
    if (!pythonToCpp) {
        Shiboken::Warnings::warnInvalidReturnValue("QProgressIndicator", "hasHeightForWidth", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

int QProgressIndicatorWrapper::heightForWidth(int w) const
{
    if (m_PyMethodCache[20])
        return this->::QProgressIndicator::heightForWidth(w);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return 0;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "heightForWidth";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[20] = true;
        gil.release();
        return this->::QProgressIndicator::heightForWidth(w);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(i)",
        w
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return 0;
    }
    // Check return type
    Shiboken::Conversions::PythonToCppConversion pythonToCpp =
        Shiboken::Conversions::pythonToCppConversion(Shiboken::Conversions::PrimitiveTypeConverter<int>(), pyResult);
    if (!pythonToCpp) {
        Shiboken::Warnings::warnInvalidReturnValue("QProgressIndicator", "heightForWidth", "int", Py_TYPE(pyResult)->tp_name);
        return 0;
    }
    int cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QProgressIndicatorWrapper::hideEvent(QHideEvent * event)
{
    if (m_PyMethodCache[21]) {
        return this->::QWidget::hideEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "hideEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[21] = true;
        gil.release();
        return this->::QWidget::hideEvent(event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtGuiTypes[SBK_QHIDEEVENT_IDX], event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

void QProgressIndicatorWrapper::initPainter(QPainter * painter) const
{
    if (m_PyMethodCache[22]) {
        return this->::QWidget::initPainter(painter);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "initPainter";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[22] = true;
        gil.release();
        return this->::QWidget::initPainter(painter);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtGuiTypes[SBK_QPAINTER_IDX], painter)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

void QProgressIndicatorWrapper::inputMethodEvent(QInputMethodEvent * event)
{
    if (m_PyMethodCache[23]) {
        return this->::QWidget::inputMethodEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "inputMethodEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[23] = true;
        gil.release();
        return this->::QWidget::inputMethodEvent(event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtGuiTypes[SBK_QINPUTMETHODEVENT_IDX], event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

QVariant QProgressIndicatorWrapper::inputMethodQuery(Qt::InputMethodQuery arg__1) const
{
    if (m_PyMethodCache[24])
        return this->::QWidget::inputMethodQuery(arg__1);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return ::QVariant();
    static PyObject *nameCache[2] = {};
    static const char *funcName = "inputMethodQuery";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[24] = true;
        gil.release();
        return this->::QWidget::inputMethodQuery(arg__1);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::copyToPython(PepType_SETP(reinterpret_cast<SbkEnumType *>(SbkPySide6_QtCoreTypes[SBK_QT_INPUTMETHODQUERY_IDX]))->converter, &arg__1)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return ::QVariant();
    }
    // Check return type
    Shiboken::Conversions::PythonToCppConversion pythonToCpp =
        Shiboken::Conversions::pythonToCppConversion(SbkPySide6_QtCoreTypeConverters[SBK_QVARIANT_IDX], pyResult);
    if (!pythonToCpp) {
        Shiboken::Warnings::warnInvalidReturnValue("QProgressIndicator", "inputMethodQuery", "QVariant", Py_TYPE(pyResult)->tp_name);
        return ::QVariant();
    }
    ::QVariant cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QProgressIndicatorWrapper::keyPressEvent(QKeyEvent * event)
{
    if (m_PyMethodCache[25]) {
        return this->::QWidget::keyPressEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "keyPressEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[25] = true;
        gil.release();
        return this->::QWidget::keyPressEvent(event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtGuiTypes[SBK_QKEYEVENT_IDX], event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

void QProgressIndicatorWrapper::keyReleaseEvent(QKeyEvent * event)
{
    if (m_PyMethodCache[26]) {
        return this->::QWidget::keyReleaseEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "keyReleaseEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[26] = true;
        gil.release();
        return this->::QWidget::keyReleaseEvent(event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtGuiTypes[SBK_QKEYEVENT_IDX], event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

void QProgressIndicatorWrapper::leaveEvent(QEvent * event)
{
    if (m_PyMethodCache[27]) {
        return this->::QWidget::leaveEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "leaveEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[27] = true;
        gil.release();
        return this->::QWidget::leaveEvent(event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtCoreTypes[SBK_QEVENT_IDX], event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

int QProgressIndicatorWrapper::metric(QPaintDevice::PaintDeviceMetric arg__1) const
{
    if (m_PyMethodCache[28])
        return this->::QWidget::metric(arg__1);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return 0;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "metric";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[28] = true;
        gil.release();
        return this->::QWidget::metric(arg__1);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::copyToPython(PepType_SETP(reinterpret_cast<SbkEnumType *>(SbkPySide6_QtGuiTypes[SBK_QPAINTDEVICE_PAINTDEVICEMETRIC_IDX]))->converter, &arg__1)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return 0;
    }
    // Check return type
    Shiboken::Conversions::PythonToCppConversion pythonToCpp =
        Shiboken::Conversions::pythonToCppConversion(Shiboken::Conversions::PrimitiveTypeConverter<int>(), pyResult);
    if (!pythonToCpp) {
        Shiboken::Warnings::warnInvalidReturnValue("QProgressIndicator", "metric", "int", Py_TYPE(pyResult)->tp_name);
        return 0;
    }
    int cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QSize QProgressIndicatorWrapper::minimumSizeHint() const
{
    if (m_PyMethodCache[29])
        return this->::QWidget::minimumSizeHint();
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return {};
    static PyObject *nameCache[2] = {};
    // This method belongs to a property.
    static const char *funcName = "1:minimumSizeHint";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[29] = true;
        gil.release();
        return this->::QWidget::minimumSizeHint();
    }

    Shiboken::AutoDecRef pyArgs(PyTuple_New(0));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return {};
    }
    // Check return type
    Shiboken::Conversions::PythonToCppConversion pythonToCpp =
        Shiboken::Conversions::pythonToCppValueConversion(SbkPySide6_QtCoreTypes[SBK_QSIZE_IDX], pyResult);
    if (!pythonToCpp) {
        Shiboken::Warnings::warnInvalidReturnValue("QProgressIndicator", "minimumSizeHint", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QSize >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return {};
    }
    ::QSize cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QProgressIndicatorWrapper::mouseDoubleClickEvent(QMouseEvent * event)
{
    if (m_PyMethodCache[30]) {
        return this->::QWidget::mouseDoubleClickEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "mouseDoubleClickEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[30] = true;
        gil.release();
        return this->::QWidget::mouseDoubleClickEvent(event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtGuiTypes[SBK_QMOUSEEVENT_IDX], event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

void QProgressIndicatorWrapper::mouseMoveEvent(QMouseEvent * event)
{
    if (m_PyMethodCache[31]) {
        return this->::QWidget::mouseMoveEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "mouseMoveEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[31] = true;
        gil.release();
        return this->::QWidget::mouseMoveEvent(event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtGuiTypes[SBK_QMOUSEEVENT_IDX], event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

void QProgressIndicatorWrapper::mousePressEvent(QMouseEvent * event)
{
    if (m_PyMethodCache[32]) {
        return this->::QWidget::mousePressEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "mousePressEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[32] = true;
        gil.release();
        return this->::QWidget::mousePressEvent(event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtGuiTypes[SBK_QMOUSEEVENT_IDX], event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

void QProgressIndicatorWrapper::mouseReleaseEvent(QMouseEvent * event)
{
    if (m_PyMethodCache[33]) {
        return this->::QWidget::mouseReleaseEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "mouseReleaseEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[33] = true;
        gil.release();
        return this->::QWidget::mouseReleaseEvent(event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtGuiTypes[SBK_QMOUSEEVENT_IDX], event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

void QProgressIndicatorWrapper::moveEvent(QMoveEvent * event)
{
    if (m_PyMethodCache[34]) {
        return this->::QWidget::moveEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "moveEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[34] = true;
        gil.release();
        return this->::QWidget::moveEvent(event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtGuiTypes[SBK_QMOVEEVENT_IDX], event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

bool QProgressIndicatorWrapper::nativeEvent(const QByteArray & eventType, void * message, qintptr * result)
{
    if (m_PyMethodCache[35]) {
        return this->::QWidget::nativeEvent(eventType, message, result);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return false;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "nativeEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[35] = true;
        gil.release();
        return this->::QWidget::nativeEvent(eventType, message, result);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(NN)",
        Shiboken::Conversions::copyToPython(SbkPySide6_QtCoreTypes[SBK_QBYTEARRAY_IDX], &eventType),
        Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<void *>(), message)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return false;
    }
    // Begin code injection
    // TEMPLATE - return_native_eventfilter_conversion - START
    bool cppResult = false;
    if (PySequence_Check(pyResult.object()) && (PySequence_Size(pyResult.object()) == 2)) {
        Shiboken::AutoDecRef pyItem(PySequence_GetItem(pyResult.object(), 0));
        Shiboken::Conversions::pythonToCppCopy(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), pyItem, &(cppResult));
        if (result) {
            Shiboken::AutoDecRef pyResultItem(PySequence_GetItem(pyResult, 1));
            Shiboken::Conversions::pythonToCppCopy(Shiboken::Conversions::PrimitiveTypeConverter<long>(), pyResultItem, (result));
        }
    }
    // TEMPLATE - return_native_eventfilter_conversion - END
    // End of code injection


    return cppResult;
}

QPaintEngine * QProgressIndicatorWrapper::paintEngine() const
{
    if (m_PyMethodCache[36])
        return this->::QWidget::paintEngine();
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return nullptr;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "paintEngine";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[36] = true;
        gil.release();
        return this->::QWidget::paintEngine();
    }

    Shiboken::AutoDecRef pyArgs(PyTuple_New(0));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return nullptr;
    }
    // Check return type
    Shiboken::Conversions::PythonToCppConversion pythonToCpp =
        Shiboken::Conversions::pythonToCppPointerConversion(SbkPySide6_QtGuiTypes[SBK_QPAINTENGINE_IDX], pyResult);
    if (!pythonToCpp) {
        Shiboken::Warnings::warnInvalidReturnValue("QProgressIndicator", "paintEngine", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QPaintEngine >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return nullptr;
    }
    ::QPaintEngine *cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QProgressIndicatorWrapper::paintEvent(QPaintEvent * event)
{
    if (m_PyMethodCache[37]) {
        return this->::QProgressIndicator::paintEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "paintEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[37] = true;
        gil.release();
        return this->::QProgressIndicator::paintEvent(event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtGuiTypes[SBK_QPAINTEVENT_IDX], event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

QPaintDevice * QProgressIndicatorWrapper::redirected(QPoint * offset) const
{
    if (m_PyMethodCache[38])
        return this->::QWidget::redirected(offset);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return nullptr;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "redirected";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[38] = true;
        gil.release();
        return this->::QWidget::redirected(offset);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtCoreTypes[SBK_QPOINT_IDX], offset)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return nullptr;
    }
    // Check return type
    Shiboken::Conversions::PythonToCppConversion pythonToCpp =
        Shiboken::Conversions::pythonToCppPointerConversion(SbkPySide6_QtGuiTypes[SBK_QPAINTDEVICE_IDX], pyResult);
    if (!pythonToCpp) {
        Shiboken::Warnings::warnInvalidReturnValue("QProgressIndicator", "redirected", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QPaintDevice >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return nullptr;
    }
    ::QPaintDevice *cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QProgressIndicatorWrapper::resizeEvent(QResizeEvent * event)
{
    if (m_PyMethodCache[39]) {
        return this->::QWidget::resizeEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "resizeEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[39] = true;
        gil.release();
        return this->::QWidget::resizeEvent(event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtGuiTypes[SBK_QRESIZEEVENT_IDX], event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

void QProgressIndicatorWrapper::setVisible(bool visible)
{
    if (m_PyMethodCache[40]) {
        return this->::QWidget::setVisible(visible);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    // This method belongs to a property.
    static const char *funcName = "2:setVisible";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[40] = true;
        gil.release();
        return this->::QWidget::setVisible(visible);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), &visible)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

QPainter * QProgressIndicatorWrapper::sharedPainter() const
{
    if (m_PyMethodCache[41])
        return this->::QWidget::sharedPainter();
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return nullptr;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "sharedPainter";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[41] = true;
        gil.release();
        return this->::QWidget::sharedPainter();
    }

    Shiboken::AutoDecRef pyArgs(PyTuple_New(0));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return nullptr;
    }
    // Check return type
    Shiboken::Conversions::PythonToCppConversion pythonToCpp =
        Shiboken::Conversions::pythonToCppPointerConversion(SbkPySide6_QtGuiTypes[SBK_QPAINTER_IDX], pyResult);
    if (!pythonToCpp) {
        Shiboken::Warnings::warnInvalidReturnValue("QProgressIndicator", "sharedPainter", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QPainter >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return nullptr;
    }
    ::QPainter *cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QProgressIndicatorWrapper::showEvent(QShowEvent * event)
{
    if (m_PyMethodCache[42]) {
        return this->::QWidget::showEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "showEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[42] = true;
        gil.release();
        return this->::QWidget::showEvent(event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtGuiTypes[SBK_QSHOWEVENT_IDX], event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

QSize QProgressIndicatorWrapper::sizeHint() const
{
    if (m_PyMethodCache[43])
        return this->::QProgressIndicator::sizeHint();
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return {};
    static PyObject *nameCache[2] = {};
    static const char *funcName = "sizeHint";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[43] = true;
        gil.release();
        return this->::QProgressIndicator::sizeHint();
    }

    Shiboken::AutoDecRef pyArgs(PyTuple_New(0));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return {};
    }
    // Check return type
    Shiboken::Conversions::PythonToCppConversion pythonToCpp =
        Shiboken::Conversions::pythonToCppValueConversion(SbkPySide6_QtCoreTypes[SBK_QSIZE_IDX], pyResult);
    if (!pythonToCpp) {
        Shiboken::Warnings::warnInvalidReturnValue("QProgressIndicator", "sizeHint", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QSize >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return {};
    }
    ::QSize cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QProgressIndicatorWrapper::tabletEvent(QTabletEvent * event)
{
    if (m_PyMethodCache[44]) {
        return this->::QWidget::tabletEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "tabletEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[44] = true;
        gil.release();
        return this->::QWidget::tabletEvent(event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtGuiTypes[SBK_QTABLETEVENT_IDX], event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

void QProgressIndicatorWrapper::timerEvent(QTimerEvent * event)
{
    if (m_PyMethodCache[45]) {
        return this->::QProgressIndicator::timerEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "timerEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[45] = true;
        gil.release();
        return this->::QProgressIndicator::timerEvent(event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtCoreTypes[SBK_QTIMEREVENT_IDX], event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

void QProgressIndicatorWrapper::wheelEvent(QWheelEvent * event)
{
    if (m_PyMethodCache[46]) {
        return this->::QWidget::wheelEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "wheelEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[46] = true;
        gil.release();
        return this->::QWidget::wheelEvent(event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtGuiTypes[SBK_QWHEELEVENT_IDX], event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

const QMetaObject *QProgressIndicatorWrapper::metaObject() const
{
    if (QObject::d_ptr->metaObject)
        return QObject::d_ptr->dynamicMetaObject();
    SbkObject *pySelf = Shiboken::BindingManager::instance().retrieveWrapper(this);
    if (pySelf == nullptr)
        return QProgressIndicator::metaObject();
    return PySide::SignalManager::retrieveMetaObject(reinterpret_cast<PyObject *>(pySelf));
}

int QProgressIndicatorWrapper::qt_metacall(QMetaObject::Call call, int id, void **args)
{
    int result = QProgressIndicator::qt_metacall(call, id, args);
    return result < 0 ? result : PySide::SignalManager::qt_metacall(this, call, id, args);
}

void *QProgressIndicatorWrapper::qt_metacast(const char *_clname)
{
    if (!_clname)
        return {};
    SbkObject *pySelf = Shiboken::BindingManager::instance().retrieveWrapper(this);
    if (pySelf && PySide::inherits(Py_TYPE(pySelf), _clname))
        return static_cast<void *>(const_cast< QProgressIndicatorWrapper *>(this));
    return QProgressIndicator::qt_metacast(_clname);
}

QProgressIndicatorWrapper::~QProgressIndicatorWrapper()
{
    SbkObject *wrapper = Shiboken::BindingManager::instance().retrieveWrapper(this);
    Shiboken::Object::destroy(wrapper, this);
}

// Target ---------------------------------------------------------

extern "C" {
static int
Sbk_QProgressIndicator_Init(PyObject *self, PyObject *args, PyObject *kwds)
{
    SBK_UNUSED(kwds)
    const QMetaObject *metaObject;
    SbkObject *sbkSelf = reinterpret_cast<SbkObject *>(self);
    PySide::Feature::Select(self);
    if (Shiboken::Object::isUserType(self) && !Shiboken::ObjectType::canCallConstructor(self->ob_type, Shiboken::SbkType< ::QProgressIndicator >()))
        return -1;

    ::QProgressIndicatorWrapper *cptr{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qprogressindicator.QProgressIndicator.__init__";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp[1];
    SBK_UNUSED(pythonToCpp)
    const Py_ssize_t numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {nullptr};

    // invalid argument lengths

    if (!PyArg_ParseTuple(args, "|O:QProgressIndicator", &(pyArgs[0])))
        return -1;


    // Overloaded function decisor
    // 0: QProgressIndicator::QProgressIndicator(QWidget*)
    if (numArgs == 0) {
        overloadId = 0; // QProgressIndicator(QWidget*)
    } else if (numArgs >= 1
        && (pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkPySide6_QtWidgetsTypes[SBK_QWIDGET_IDX], (pyArgs[0])))) {
        overloadId = 0; // QProgressIndicator(QWidget*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QProgressIndicator_Init_TypeError;

    // Call function/method
    {
        if (kwds && PyDict_Size(kwds) > 0) {
            PyObject *value{};
            Shiboken::AutoDecRef kwds_dup(PyDict_Copy(kwds));
            static PyObject *const key_parent = Shiboken::String::createStaticString("parent");
            if (PyDict_Contains(kwds, key_parent)) {
                value = PyDict_GetItem(kwds, key_parent);
                if (value && pyArgs[0]) {
                    errInfo.reset(key_parent);
                    Py_INCREF(errInfo.object());
                    goto Sbk_QProgressIndicator_Init_TypeError;
                }
                if (value) {
                    pyArgs[0] = value;
                    if (!(pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkPySide6_QtWidgetsTypes[SBK_QWIDGET_IDX], (pyArgs[0]))))
                        goto Sbk_QProgressIndicator_Init_TypeError;
                }
                PyDict_DelItem(kwds_dup, key_parent);
            }
            if (PyDict_Size(kwds_dup) > 0) {
                errInfo.reset(kwds_dup.release());
                // fall through to handle extra keyword signals and properties
            }
        }
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return -1;
        ::QWidget *cppArg0 = nullptr;
        if (pythonToCpp[0])
            pythonToCpp[0](pyArgs[0], &cppArg0);

        if (!PyErr_Occurred()) {
            // QProgressIndicator(QWidget*)
            void *addr = PySide::nextQObjectMemoryAddr();
            if (addr) {
                cptr = new (addr) ::QProgressIndicatorWrapper(cppArg0);
                PySide::setNextQObjectMemoryAddr(nullptr);
            } else {
                cptr = new ::QProgressIndicatorWrapper(cppArg0);
            }

            // Ownership transferences (constructor heuristics).
            Shiboken::Object::setParent(pyArgs[0], self);
        }
    }

    if (PyErr_Occurred() || !Shiboken::Object::setCppPointer(sbkSelf, Shiboken::SbkType< ::QProgressIndicator >(), cptr)) {
        delete cptr;
        return -1;
    }
    if (!cptr) goto Sbk_QProgressIndicator_Init_TypeError;

    Shiboken::Object::setValidCpp(sbkSelf, true);
    Shiboken::Object::setHasCppWrapper(sbkSelf, true);
    if (Shiboken::BindingManager::instance().hasWrapper(cptr)) {
        Shiboken::BindingManager::instance().releaseWrapper(Shiboken::BindingManager::instance().retrieveWrapper(cptr));
    }
    Shiboken::BindingManager::instance().registerWrapper(sbkSelf, cptr);

    // QObject setup
    PySide::Signal::updateSourceObject(self);
    metaObject = cptr->metaObject(); // <- init python qt properties
    if (!errInfo.isNull() && PyDict_Check(errInfo.object())) {
        if (!PySide::fillQtProperties(self, metaObject, errInfo))
            goto Sbk_QProgressIndicator_Init_TypeError;
    };


    return 1;

    Sbk_QProgressIndicator_Init_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return -1;
}

static PyObject *Sbk_QProgressIndicatorFunc_animationDelay(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QProgressIndicatorWrapper *>(reinterpret_cast< ::QProgressIndicator *>(Shiboken::Conversions::cppPointer(SbkqprogressindicatorTypes[SBK_QPROGRESSINDICATOR_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // animationDelay()const
            int cppResult = const_cast<const ::QProgressIndicatorWrapper *>(cppSelf)->animationDelay();
            pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<int>(), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QProgressIndicatorFunc_color(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QProgressIndicatorWrapper *>(reinterpret_cast< ::QProgressIndicator *>(Shiboken::Conversions::cppPointer(SbkqprogressindicatorTypes[SBK_QPROGRESSINDICATOR_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // color()const
            const QColor & cppResult = const_cast<const ::QProgressIndicatorWrapper *>(cppSelf)->color();
            pyResult = Shiboken::Conversions::copyToPython(SbkPySide6_QtGuiTypes[SBK_QCOLOR_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QProgressIndicatorFunc_heightForWidth(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QProgressIndicatorWrapper *>(reinterpret_cast< ::QProgressIndicator *>(Shiboken::Conversions::cppPointer(SbkqprogressindicatorTypes[SBK_QPROGRESSINDICATOR_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qprogressindicator.QProgressIndicator.heightForWidth";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QWidget::heightForWidth(int)const->int
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppConversion(Shiboken::Conversions::PrimitiveTypeConverter<int>(), (pyArg)))) {
        overloadId = 0; // heightForWidth(int)const
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QProgressIndicatorFunc_heightForWidth_TypeError;

    // Call function/method
    {
        int cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // heightForWidth(int)const
            int cppResult = Shiboken::Object::hasCppWrapper(reinterpret_cast<SbkObject *>(self))
                ? const_cast<const ::QProgressIndicatorWrapper *>(cppSelf)->::QProgressIndicator::heightForWidth(cppArg0)
                : const_cast<const ::QProgressIndicatorWrapper *>(cppSelf)->heightForWidth(cppArg0);
            pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<int>(), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QProgressIndicatorFunc_heightForWidth_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QProgressIndicatorFunc_isAnimated(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QProgressIndicatorWrapper *>(reinterpret_cast< ::QProgressIndicator *>(Shiboken::Conversions::cppPointer(SbkqprogressindicatorTypes[SBK_QPROGRESSINDICATOR_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // isAnimated()const
            bool cppResult = const_cast<const ::QProgressIndicatorWrapper *>(cppSelf)->isAnimated();
            pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QProgressIndicatorFunc_isDisplayedWhenStopped(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QProgressIndicatorWrapper *>(reinterpret_cast< ::QProgressIndicator *>(Shiboken::Conversions::cppPointer(SbkqprogressindicatorTypes[SBK_QPROGRESSINDICATOR_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // isDisplayedWhenStopped()const
            bool cppResult = const_cast<const ::QProgressIndicatorWrapper *>(cppSelf)->isDisplayedWhenStopped();
            pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QProgressIndicatorFunc_paintEvent(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QProgressIndicatorWrapper *>(reinterpret_cast< ::QProgressIndicator *>(Shiboken::Conversions::cppPointer(SbkqprogressindicatorTypes[SBK_QPROGRESSINDICATOR_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qprogressindicator.QProgressIndicator.paintEvent";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QWidget::paintEvent(QPaintEvent*)
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppPointerConversion(SbkPySide6_QtGuiTypes[SBK_QPAINTEVENT_IDX], (pyArg)))) {
        overloadId = 0; // paintEvent(QPaintEvent*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QProgressIndicatorFunc_paintEvent_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QPaintEvent *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // paintEvent(QPaintEvent*)
            static_cast<::QProgressIndicatorWrapper *>(cppSelf)->QProgressIndicatorWrapper::paintEvent_protected(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QProgressIndicatorFunc_paintEvent_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QProgressIndicatorFunc_setAnimationDelay(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QProgressIndicatorWrapper *>(reinterpret_cast< ::QProgressIndicator *>(Shiboken::Conversions::cppPointer(SbkqprogressindicatorTypes[SBK_QPROGRESSINDICATOR_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qprogressindicator.QProgressIndicator.setAnimationDelay";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QProgressIndicator::setAnimationDelay(int)
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppConversion(Shiboken::Conversions::PrimitiveTypeConverter<int>(), (pyArg)))) {
        overloadId = 0; // setAnimationDelay(int)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QProgressIndicatorFunc_setAnimationDelay_TypeError;

    // Call function/method
    {
        int cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // setAnimationDelay(int)
            cppSelf->setAnimationDelay(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QProgressIndicatorFunc_setAnimationDelay_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QProgressIndicatorFunc_setColor(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QProgressIndicatorWrapper *>(reinterpret_cast< ::QProgressIndicator *>(Shiboken::Conversions::cppPointer(SbkqprogressindicatorTypes[SBK_QPROGRESSINDICATOR_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qprogressindicator.QProgressIndicator.setColor";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QProgressIndicator::setColor(QColor)
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppReferenceConversion(SbkPySide6_QtGuiTypes[SBK_QCOLOR_IDX], (pyArg)))) {
        overloadId = 0; // setColor(QColor)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QProgressIndicatorFunc_setColor_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QColor cppArg0_local;
        ::QColor *cppArg0 = &cppArg0_local;
        if (pythonToCpp.isValue())
            pythonToCpp(pyArg, &cppArg0_local);
        else
            pythonToCpp(pyArg, &cppArg0);


        if (!PyErr_Occurred()) {
            // setColor(QColor)
            cppSelf->setColor(*cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QProgressIndicatorFunc_setColor_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QProgressIndicatorFunc_setDisplayedWhenStopped(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QProgressIndicatorWrapper *>(reinterpret_cast< ::QProgressIndicator *>(Shiboken::Conversions::cppPointer(SbkqprogressindicatorTypes[SBK_QPROGRESSINDICATOR_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qprogressindicator.QProgressIndicator.setDisplayedWhenStopped";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QProgressIndicator::setDisplayedWhenStopped(bool)
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppConversion(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), (pyArg)))) {
        overloadId = 0; // setDisplayedWhenStopped(bool)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QProgressIndicatorFunc_setDisplayedWhenStopped_TypeError;

    // Call function/method
    {
        bool cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // setDisplayedWhenStopped(bool)
            cppSelf->setDisplayedWhenStopped(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QProgressIndicatorFunc_setDisplayedWhenStopped_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QProgressIndicatorFunc_sizeHint(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QProgressIndicatorWrapper *>(reinterpret_cast< ::QProgressIndicator *>(Shiboken::Conversions::cppPointer(SbkqprogressindicatorTypes[SBK_QPROGRESSINDICATOR_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // sizeHint()const
            QSize cppResult = Shiboken::Object::hasCppWrapper(reinterpret_cast<SbkObject *>(self))
                ? const_cast<const ::QProgressIndicatorWrapper *>(cppSelf)->::QProgressIndicator::sizeHint()
                : const_cast<const ::QProgressIndicatorWrapper *>(cppSelf)->sizeHint();
            pyResult = Shiboken::Conversions::copyToPython(SbkPySide6_QtCoreTypes[SBK_QSIZE_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QProgressIndicatorFunc_startAnimation(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QProgressIndicatorWrapper *>(reinterpret_cast< ::QProgressIndicator *>(Shiboken::Conversions::cppPointer(SbkqprogressindicatorTypes[SBK_QPROGRESSINDICATOR_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // startAnimation()
            cppSelf->startAnimation();
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;
}

static PyObject *Sbk_QProgressIndicatorFunc_stopAnimation(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QProgressIndicatorWrapper *>(reinterpret_cast< ::QProgressIndicator *>(Shiboken::Conversions::cppPointer(SbkqprogressindicatorTypes[SBK_QPROGRESSINDICATOR_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // stopAnimation()
            cppSelf->stopAnimation();
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;
}

static PyObject *Sbk_QProgressIndicatorFunc_timerEvent(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QProgressIndicatorWrapper *>(reinterpret_cast< ::QProgressIndicator *>(Shiboken::Conversions::cppPointer(SbkqprogressindicatorTypes[SBK_QPROGRESSINDICATOR_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qprogressindicator.QProgressIndicator.timerEvent";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QObject::timerEvent(QTimerEvent*)
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppPointerConversion(SbkPySide6_QtCoreTypes[SBK_QTIMEREVENT_IDX], (pyArg)))) {
        overloadId = 0; // timerEvent(QTimerEvent*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QProgressIndicatorFunc_timerEvent_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QTimerEvent *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // timerEvent(QTimerEvent*)
            static_cast<::QProgressIndicatorWrapper *>(cppSelf)->QProgressIndicatorWrapper::timerEvent_protected(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QProgressIndicatorFunc_timerEvent_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}


static const char *Sbk_QProgressIndicator_PropertyStrings[] = {
    "color::",
    "delay:animationDelay:setAnimationDelay",
    "displayedWhenStopped:isDisplayedWhenStopped:",
    nullptr // Sentinel
};

static PyMethodDef Sbk_QProgressIndicator_methods[] = {
    {"animationDelay", reinterpret_cast<PyCFunction>(Sbk_QProgressIndicatorFunc_animationDelay), METH_NOARGS, nullptr},
    {"color", reinterpret_cast<PyCFunction>(Sbk_QProgressIndicatorFunc_color), METH_NOARGS, nullptr},
    {"heightForWidth", reinterpret_cast<PyCFunction>(Sbk_QProgressIndicatorFunc_heightForWidth), METH_O, nullptr},
    {"isAnimated", reinterpret_cast<PyCFunction>(Sbk_QProgressIndicatorFunc_isAnimated), METH_NOARGS, nullptr},
    {"isDisplayedWhenStopped", reinterpret_cast<PyCFunction>(Sbk_QProgressIndicatorFunc_isDisplayedWhenStopped), METH_NOARGS, nullptr},
    {"paintEvent", reinterpret_cast<PyCFunction>(Sbk_QProgressIndicatorFunc_paintEvent), METH_O, nullptr},
    {"setAnimationDelay", reinterpret_cast<PyCFunction>(Sbk_QProgressIndicatorFunc_setAnimationDelay), METH_O, nullptr},
    {"setColor", reinterpret_cast<PyCFunction>(Sbk_QProgressIndicatorFunc_setColor), METH_O, nullptr},
    {"setDisplayedWhenStopped", reinterpret_cast<PyCFunction>(Sbk_QProgressIndicatorFunc_setDisplayedWhenStopped), METH_O, nullptr},
    {"sizeHint", reinterpret_cast<PyCFunction>(Sbk_QProgressIndicatorFunc_sizeHint), METH_NOARGS, nullptr},
    {"startAnimation", reinterpret_cast<PyCFunction>(Sbk_QProgressIndicatorFunc_startAnimation), METH_NOARGS, nullptr},
    {"stopAnimation", reinterpret_cast<PyCFunction>(Sbk_QProgressIndicatorFunc_stopAnimation), METH_NOARGS, nullptr},
    {"timerEvent", reinterpret_cast<PyCFunction>(Sbk_QProgressIndicatorFunc_timerEvent), METH_O, nullptr},

    {nullptr, nullptr, 0, nullptr} // Sentinel
};

static int Sbk_QProgressIndicator_setattro(PyObject *self, PyObject *name, PyObject *value)
{
    PySide::Feature::Select(self);
    if (value && PyCallable_Check(value)) {
        auto plain_inst = reinterpret_cast< ::QProgressIndicator *>(Shiboken::Conversions::cppPointer(SbkqprogressindicatorTypes[SBK_QPROGRESSINDICATOR_IDX], reinterpret_cast<SbkObject *>(self)));
        auto inst = dynamic_cast<QProgressIndicatorWrapper *>(plain_inst);
        if (inst)
            inst->resetPyMethodCache();
    }
    Shiboken::AutoDecRef pp(reinterpret_cast<PyObject *>(PySide::Property::getObject(self, name)));
    if (!pp.isNull())
        return PySide::Property::setValue(reinterpret_cast<PySideProperty *>(pp.object()), self, value);
    return PyObject_GenericSetAttr(self, name, value);
}

} // extern "C"

static int Sbk_QProgressIndicator_traverse(PyObject *self, visitproc visit, void *arg)
{
    return SbkObject_TypeF()->tp_traverse(self, visit, arg);
}
static int Sbk_QProgressIndicator_clear(PyObject *self)
{
    return reinterpret_cast<PyTypeObject *>(SbkObject_TypeF())->tp_clear(self);
}
static void * Sbk_QProgressIndicatorSpecialCastFunction(void *obj, PyTypeObject *desiredType)
{
    auto me = reinterpret_cast< ::QProgressIndicator *>(obj);
    if (desiredType == SbkPySide6_QtWidgetsTypes[SBK_QWIDGET_IDX])
        return static_cast< ::QWidget *>(me);
    else if (desiredType == SbkPySide6_QtCoreTypes[SBK_QOBJECT_IDX])
        return static_cast< ::QObject *>(me);
    else if (desiredType == SbkPySide6_QtGuiTypes[SBK_QPAINTDEVICE_IDX])
        return static_cast< ::QPaintDevice *>(me);
    return me;
}


// Class Definition -----------------------------------------------
extern "C" {
static PyTypeObject *_Sbk_QProgressIndicator_Type = nullptr;
static PyTypeObject *Sbk_QProgressIndicator_TypeF(void)
{
    return _Sbk_QProgressIndicator_Type;
}

static PyType_Slot Sbk_QProgressIndicator_slots[] = {
    {Py_tp_base,        nullptr}, // inserted by introduceWrapperType
    {Py_tp_dealloc,     reinterpret_cast<void *>(&SbkDeallocWrapper)},
    {Py_tp_repr,        nullptr},
    {Py_tp_hash,        nullptr},
    {Py_tp_call,        nullptr},
    {Py_tp_str,         nullptr},
    {Py_tp_getattro,    nullptr},
    {Py_tp_setattro,    reinterpret_cast<void *>(Sbk_QProgressIndicator_setattro)},
    {Py_tp_traverse,    reinterpret_cast<void *>(Sbk_QProgressIndicator_traverse)},
    {Py_tp_clear,       reinterpret_cast<void *>(Sbk_QProgressIndicator_clear)},
    {Py_tp_richcompare, nullptr},
    {Py_tp_iter,        nullptr},
    {Py_tp_iternext,    nullptr},
    {Py_tp_methods,     reinterpret_cast<void *>(Sbk_QProgressIndicator_methods)},
    {Py_tp_getset,      nullptr},
    {Py_tp_init,        reinterpret_cast<void *>(Sbk_QProgressIndicator_Init)},
    {Py_tp_new,         reinterpret_cast<void *>(SbkObject_tp_new)},
    {0, nullptr}
};
static PyType_Spec Sbk_QProgressIndicator_spec = {
    "1:qprogressindicator.QProgressIndicator",
    sizeof(SbkObject),
    0,
    Py_TPFLAGS_DEFAULT|Py_TPFLAGS_BASETYPE|Py_TPFLAGS_HAVE_GC,
    Sbk_QProgressIndicator_slots
};

} //extern "C"

static void *Sbk_QProgressIndicator_typeDiscovery(void *cptr, PyTypeObject *instanceType)
{
    SBK_UNUSED(cptr)
    SBK_UNUSED(instanceType)
    if (instanceType == Shiboken::SbkType< ::QObject >())
        return dynamic_cast< ::QProgressIndicator *>(reinterpret_cast< ::QObject *>(cptr));
    if (instanceType == Shiboken::SbkType< ::QPaintDevice >())
        return dynamic_cast< ::QProgressIndicator *>(reinterpret_cast< ::QPaintDevice *>(cptr));
    return {};
}


// Type conversion functions.

// Python to C++ pointer conversion - returns the C++ object of the Python wrapper (keeps object identity).
static void QProgressIndicator_PythonToCpp_QProgressIndicator_PTR(PyObject *pyIn, void *cppOut)
{
    Shiboken::Conversions::pythonToCppPointer(Sbk_QProgressIndicator_TypeF(), pyIn, cppOut);
}
static PythonToCppFunc is_QProgressIndicator_PythonToCpp_QProgressIndicator_PTR_Convertible(PyObject *pyIn)
{
    if (pyIn == Py_None)
        return Shiboken::Conversions::nonePythonToCppNullPtr;
    if (PyObject_TypeCheck(pyIn, Sbk_QProgressIndicator_TypeF()))
        return QProgressIndicator_PythonToCpp_QProgressIndicator_PTR;
    return {};
}

// C++ to Python pointer conversion - tries to find the Python wrapper for the C++ object (keeps object identity).
static PyObject *QProgressIndicator_PTR_CppToPython_QProgressIndicator(const void *cppIn)
{
    return PySide::getWrapperForQObject(reinterpret_cast<::QProgressIndicator *>(const_cast<void *>(cppIn)), Sbk_QProgressIndicator_TypeF());

}

// The signatures string for the functions.
// Multiple signatures have their index "n:" in front.
static const char *QProgressIndicator_SignatureStrings[] = {
    "qprogressindicator.QProgressIndicator(self,parent:PySide6.QtWidgets.QWidget=nullptr)",
    "qprogressindicator.QProgressIndicator.animationDelay(self)->int",
    "qprogressindicator.QProgressIndicator.color(self)->PySide6.QtGui.QColor",
    "qprogressindicator.QProgressIndicator.heightForWidth(self,w:int)->int",
    "qprogressindicator.QProgressIndicator.isAnimated(self)->bool",
    "qprogressindicator.QProgressIndicator.isDisplayedWhenStopped(self)->bool",
    "qprogressindicator.QProgressIndicator.paintEvent(self,event:PySide6.QtGui.QPaintEvent)",
    "qprogressindicator.QProgressIndicator.setAnimationDelay(self,delay:int)",
    "qprogressindicator.QProgressIndicator.setColor(self,color:typing.Union[PySide6.QtGui.QColor, PySide6.QtGui.QRgba64, QVariant, PySide6.QtCore.Qt.GlobalColor, QString, unsigned int])",
    "qprogressindicator.QProgressIndicator.setDisplayedWhenStopped(self,state:bool)",
    "qprogressindicator.QProgressIndicator.sizeHint(self)->PySide6.QtCore.QSize",
    "qprogressindicator.QProgressIndicator.startAnimation(self)",
    "qprogressindicator.QProgressIndicator.stopAnimation(self)",
    "qprogressindicator.QProgressIndicator.timerEvent(self,event:PySide6.QtCore.QTimerEvent)",
    nullptr}; // Sentinel

void init_QProgressIndicator(PyObject *module)
{
    _Sbk_QProgressIndicator_Type = Shiboken::ObjectType::introduceWrapperType(
        module,
        "QProgressIndicator",
        "QProgressIndicator*",
        &Sbk_QProgressIndicator_spec,
        &Shiboken::callCppDestructor< ::QProgressIndicator >,
        SbkPySide6_QtWidgetsTypes[SBK_QWIDGET_IDX],
        0,
        Shiboken::ObjectType::WrapperFlags::DeleteInMainThread);
    auto *pyType = Sbk_QProgressIndicator_TypeF(); // references _Sbk_QProgressIndicator_Type
    InitSignatureStrings(pyType, QProgressIndicator_SignatureStrings);
    SbkObjectType_SetPropertyStrings(pyType, Sbk_QProgressIndicator_PropertyStrings);
    SbkqprogressindicatorTypes[SBK_QPROGRESSINDICATOR_IDX] = pyType;

    // Register Converter
    SbkConverter *converter = Shiboken::Conversions::createConverter(pyType,
        QProgressIndicator_PythonToCpp_QProgressIndicator_PTR,
        is_QProgressIndicator_PythonToCpp_QProgressIndicator_PTR_Convertible,
        QProgressIndicator_PTR_CppToPython_QProgressIndicator);

    Shiboken::Conversions::registerConverterName(converter, "QProgressIndicator");
    Shiboken::Conversions::registerConverterName(converter, "QProgressIndicator*");
    Shiboken::Conversions::registerConverterName(converter, "QProgressIndicator&");
    Shiboken::Conversions::registerConverterName(converter, typeid(::QProgressIndicator).name());
    Shiboken::Conversions::registerConverterName(converter, typeid(::QProgressIndicatorWrapper).name());


    MultipleInheritanceInitFunction func = Shiboken::ObjectType::getMultipleInheritanceFunction(SbkPySide6_QtWidgetsTypes[SBK_QWIDGET_IDX]);
    Shiboken::ObjectType::setMultipleInheritanceFunction(Sbk_QProgressIndicator_TypeF(), func);
    Shiboken::ObjectType::setCastFunction(Sbk_QProgressIndicator_TypeF(), &Sbk_QProgressIndicatorSpecialCastFunction);
    Shiboken::ObjectType::setTypeDiscoveryFunctionV2(Sbk_QProgressIndicator_TypeF(), &Sbk_QProgressIndicator_typeDiscovery);

    PySide::Signal::registerSignals(pyType, &::QProgressIndicator::staticMetaObject);
    QProgressIndicatorWrapper::pysideInitQtMetaTypes();
    Shiboken::ObjectType::setSubTypeInitHook(pyType, &PySide::initQObjectSubType);
    PySide::initDynamicMetaObject(pyType, &::QProgressIndicator::staticMetaObject, sizeof(QProgressIndicatorWrapper));
}
