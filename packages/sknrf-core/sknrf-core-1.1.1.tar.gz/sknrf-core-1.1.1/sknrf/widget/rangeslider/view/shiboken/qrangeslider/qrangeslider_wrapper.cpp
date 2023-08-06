
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
#include "qrangeslider_python.h"

// main header
#include "qrangeslider_wrapper.h"

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

void QRangeSliderWrapper::pysideInitQtMetaTypes()
{
    qRegisterMetaType< ::QRangeSlider::HandleMovementMode >("QRangeSlider::HandleMovementMode");
    qRegisterMetaType< ::QRangeSlider::SpanHandle >("QRangeSlider::SpanHandle");
}

void QRangeSliderWrapper::resetPyMethodCache()
{
    std::fill_n(m_PyMethodCache, sizeof(m_PyMethodCache) / sizeof(m_PyMethodCache[0]), false);
}

QRangeSliderWrapper::QRangeSliderWrapper(QWidget * parent) : QRangeSlider(parent)
{
    resetPyMethodCache();
    // ... middle
}

QRangeSliderWrapper::QRangeSliderWrapper(Qt::Orientation orientation, QWidget * parent) : QRangeSlider(orientation, parent)
{
    resetPyMethodCache();
    // ... middle
}

void QRangeSliderWrapper::actionEvent(QActionEvent * event)
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

void QRangeSliderWrapper::changeEvent(QEvent * e)
{
    if (m_PyMethodCache[1]) {
        return this->::QAbstractSlider::changeEvent(e);
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
        return this->::QAbstractSlider::changeEvent(e);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtCoreTypes[SBK_QEVENT_IDX], e)
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

void QRangeSliderWrapper::childEvent(QChildEvent * event)
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

void QRangeSliderWrapper::closeEvent(QCloseEvent * event)
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

void QRangeSliderWrapper::connectNotify(const QMetaMethod & signal)
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

void QRangeSliderWrapper::contextMenuEvent(QContextMenuEvent * event)
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

void QRangeSliderWrapper::customEvent(QEvent * event)
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

int QRangeSliderWrapper::devType() const
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
        Shiboken::Warnings::warnInvalidReturnValue("QRangeSlider", "devType", "int", Py_TYPE(pyResult)->tp_name);
        return 0;
    }
    int cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QRangeSliderWrapper::disconnectNotify(const QMetaMethod & signal)
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

void QRangeSliderWrapper::dragEnterEvent(QDragEnterEvent * event)
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

void QRangeSliderWrapper::dragLeaveEvent(QDragLeaveEvent * event)
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

void QRangeSliderWrapper::dragMoveEvent(QDragMoveEvent * event)
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

void QRangeSliderWrapper::dropEvent(QDropEvent * event)
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

void QRangeSliderWrapper::enterEvent(QEnterEvent * event)
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

bool QRangeSliderWrapper::event(QEvent * event)
{
    if (m_PyMethodCache[14])
        return this->::QSlider::event(event);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return false;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "event";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[14] = true;
        gil.release();
        return this->::QSlider::event(event);
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
        Shiboken::Warnings::warnInvalidReturnValue("QRangeSlider", "event", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

bool QRangeSliderWrapper::eventFilter(QObject * watched, QEvent * event)
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
        Shiboken::Warnings::warnInvalidReturnValue("QRangeSlider", "eventFilter", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QRangeSliderWrapper::focusInEvent(QFocusEvent * event)
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

bool QRangeSliderWrapper::focusNextPrevChild(bool next)
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
        Shiboken::Warnings::warnInvalidReturnValue("QRangeSlider", "focusNextPrevChild", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QRangeSliderWrapper::focusOutEvent(QFocusEvent * event)
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

bool QRangeSliderWrapper::hasHeightForWidth() const
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
        Shiboken::Warnings::warnInvalidReturnValue("QRangeSlider", "hasHeightForWidth", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

int QRangeSliderWrapper::heightForWidth(int arg__1) const
{
    if (m_PyMethodCache[20])
        return this->::QWidget::heightForWidth(arg__1);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return 0;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "heightForWidth";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[20] = true;
        gil.release();
        return this->::QWidget::heightForWidth(arg__1);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(i)",
        arg__1
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
        Shiboken::Warnings::warnInvalidReturnValue("QRangeSlider", "heightForWidth", "int", Py_TYPE(pyResult)->tp_name);
        return 0;
    }
    int cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QRangeSliderWrapper::hideEvent(QHideEvent * event)
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

void QRangeSliderWrapper::initPainter(QPainter * painter) const
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

void QRangeSliderWrapper::initStyleOption(QStyleOptionSlider * option) const
{
    if (m_PyMethodCache[23]) {
        return this->::QSlider::initStyleOption(option);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "initStyleOption";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[23] = true;
        gil.release();
        return this->::QSlider::initStyleOption(option);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtWidgetsTypes[SBK_QSTYLEOPTIONSLIDER_IDX], option)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

void QRangeSliderWrapper::inputMethodEvent(QInputMethodEvent * event)
{
    if (m_PyMethodCache[24]) {
        return this->::QWidget::inputMethodEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "inputMethodEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[24] = true;
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

QVariant QRangeSliderWrapper::inputMethodQuery(Qt::InputMethodQuery arg__1) const
{
    if (m_PyMethodCache[25])
        return this->::QWidget::inputMethodQuery(arg__1);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return ::QVariant();
    static PyObject *nameCache[2] = {};
    static const char *funcName = "inputMethodQuery";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[25] = true;
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
        Shiboken::Warnings::warnInvalidReturnValue("QRangeSlider", "inputMethodQuery", "QVariant", Py_TYPE(pyResult)->tp_name);
        return ::QVariant();
    }
    ::QVariant cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QRangeSliderWrapper::keyPressEvent(QKeyEvent * event)
{
    if (m_PyMethodCache[26]) {
        return this->::QRangeSlider::keyPressEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "keyPressEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[26] = true;
        gil.release();
        return this->::QRangeSlider::keyPressEvent(event);
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

void QRangeSliderWrapper::keyReleaseEvent(QKeyEvent * event)
{
    if (m_PyMethodCache[27]) {
        return this->::QWidget::keyReleaseEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "keyReleaseEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[27] = true;
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

void QRangeSliderWrapper::leaveEvent(QEvent * event)
{
    if (m_PyMethodCache[28]) {
        return this->::QWidget::leaveEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "leaveEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[28] = true;
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

int QRangeSliderWrapper::metric(QPaintDevice::PaintDeviceMetric arg__1) const
{
    if (m_PyMethodCache[29])
        return this->::QWidget::metric(arg__1);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return 0;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "metric";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[29] = true;
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
        Shiboken::Warnings::warnInvalidReturnValue("QRangeSlider", "metric", "int", Py_TYPE(pyResult)->tp_name);
        return 0;
    }
    int cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QSize QRangeSliderWrapper::minimumSizeHint() const
{
    if (m_PyMethodCache[30])
        return this->::QSlider::minimumSizeHint();
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return {};
    static PyObject *nameCache[2] = {};
    static const char *funcName = "minimumSizeHint";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[30] = true;
        gil.release();
        return this->::QSlider::minimumSizeHint();
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
        Shiboken::Warnings::warnInvalidReturnValue("QRangeSlider", "minimumSizeHint", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QSize >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return {};
    }
    ::QSize cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QRangeSliderWrapper::mouseDoubleClickEvent(QMouseEvent * event)
{
    if (m_PyMethodCache[31]) {
        return this->::QWidget::mouseDoubleClickEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "mouseDoubleClickEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[31] = true;
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

void QRangeSliderWrapper::mouseMoveEvent(QMouseEvent * event)
{
    if (m_PyMethodCache[32]) {
        return this->::QRangeSlider::mouseMoveEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "mouseMoveEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[32] = true;
        gil.release();
        return this->::QRangeSlider::mouseMoveEvent(event);
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

void QRangeSliderWrapper::mousePressEvent(QMouseEvent * event)
{
    if (m_PyMethodCache[33]) {
        return this->::QRangeSlider::mousePressEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "mousePressEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[33] = true;
        gil.release();
        return this->::QRangeSlider::mousePressEvent(event);
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

void QRangeSliderWrapper::mouseReleaseEvent(QMouseEvent * event)
{
    if (m_PyMethodCache[34]) {
        return this->::QRangeSlider::mouseReleaseEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "mouseReleaseEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[34] = true;
        gil.release();
        return this->::QRangeSlider::mouseReleaseEvent(event);
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

void QRangeSliderWrapper::moveEvent(QMoveEvent * event)
{
    if (m_PyMethodCache[35]) {
        return this->::QWidget::moveEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "moveEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[35] = true;
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

bool QRangeSliderWrapper::nativeEvent(const QByteArray & eventType, void * message, qintptr * result)
{
    if (m_PyMethodCache[36]) {
        return this->::QWidget::nativeEvent(eventType, message, result);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return false;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "nativeEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[36] = true;
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

QPaintEngine * QRangeSliderWrapper::paintEngine() const
{
    if (m_PyMethodCache[37])
        return this->::QWidget::paintEngine();
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return nullptr;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "paintEngine";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[37] = true;
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
        Shiboken::Warnings::warnInvalidReturnValue("QRangeSlider", "paintEngine", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QPaintEngine >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return nullptr;
    }
    ::QPaintEngine *cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QRangeSliderWrapper::paintEvent(QPaintEvent * event)
{
    if (m_PyMethodCache[38]) {
        return this->::QRangeSlider::paintEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "paintEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[38] = true;
        gil.release();
        return this->::QRangeSlider::paintEvent(event);
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

QPaintDevice * QRangeSliderWrapper::redirected(QPoint * offset) const
{
    if (m_PyMethodCache[39])
        return this->::QWidget::redirected(offset);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return nullptr;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "redirected";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[39] = true;
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
        Shiboken::Warnings::warnInvalidReturnValue("QRangeSlider", "redirected", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QPaintDevice >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return nullptr;
    }
    ::QPaintDevice *cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QRangeSliderWrapper::resizeEvent(QResizeEvent * event)
{
    if (m_PyMethodCache[40]) {
        return this->::QWidget::resizeEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "resizeEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[40] = true;
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

void QRangeSliderWrapper::setVisible(bool visible)
{
    if (m_PyMethodCache[41]) {
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
        m_PyMethodCache[41] = true;
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

QPainter * QRangeSliderWrapper::sharedPainter() const
{
    if (m_PyMethodCache[42])
        return this->::QWidget::sharedPainter();
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return nullptr;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "sharedPainter";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[42] = true;
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
        Shiboken::Warnings::warnInvalidReturnValue("QRangeSlider", "sharedPainter", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QPainter >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return nullptr;
    }
    ::QPainter *cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QRangeSliderWrapper::showEvent(QShowEvent * event)
{
    if (m_PyMethodCache[43]) {
        return this->::QWidget::showEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "showEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[43] = true;
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

QSize QRangeSliderWrapper::sizeHint() const
{
    if (m_PyMethodCache[44])
        return this->::QSlider::sizeHint();
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return {};
    static PyObject *nameCache[2] = {};
    static const char *funcName = "sizeHint";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[44] = true;
        gil.release();
        return this->::QSlider::sizeHint();
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
        Shiboken::Warnings::warnInvalidReturnValue("QRangeSlider", "sizeHint", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QSize >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return {};
    }
    ::QSize cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QRangeSliderWrapper::sliderChange(QAbstractSlider::SliderChange change)
{
    if (m_PyMethodCache[45]) {
        return this->::QAbstractSlider::sliderChange(change);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "sliderChange";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[45] = true;
        gil.release();
        return this->::QAbstractSlider::sliderChange(change);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::copyToPython(PepType_SETP(reinterpret_cast<SbkEnumType *>(SbkPySide6_QtWidgetsTypes[SBK_QABSTRACTSLIDER_SLIDERCHANGE_IDX]))->converter, &change)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

void QRangeSliderWrapper::tabletEvent(QTabletEvent * event)
{
    if (m_PyMethodCache[46]) {
        return this->::QWidget::tabletEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "tabletEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[46] = true;
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

void QRangeSliderWrapper::timerEvent(QTimerEvent * arg__1)
{
    if (m_PyMethodCache[47]) {
        return this->::QAbstractSlider::timerEvent(arg__1);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "timerEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[47] = true;
        gil.release();
        return this->::QAbstractSlider::timerEvent(arg__1);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtCoreTypes[SBK_QTIMEREVENT_IDX], arg__1)
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

void QRangeSliderWrapper::wheelEvent(QWheelEvent * e)
{
    if (m_PyMethodCache[48]) {
        return this->::QAbstractSlider::wheelEvent(e);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "wheelEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[48] = true;
        gil.release();
        return this->::QAbstractSlider::wheelEvent(e);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtGuiTypes[SBK_QWHEELEVENT_IDX], e)
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

const QMetaObject *QRangeSliderWrapper::metaObject() const
{
    if (QObject::d_ptr->metaObject)
        return QObject::d_ptr->dynamicMetaObject();
    SbkObject *pySelf = Shiboken::BindingManager::instance().retrieveWrapper(this);
    if (pySelf == nullptr)
        return QRangeSlider::metaObject();
    return PySide::SignalManager::retrieveMetaObject(reinterpret_cast<PyObject *>(pySelf));
}

int QRangeSliderWrapper::qt_metacall(QMetaObject::Call call, int id, void **args)
{
    int result = QRangeSlider::qt_metacall(call, id, args);
    return result < 0 ? result : PySide::SignalManager::qt_metacall(this, call, id, args);
}

void *QRangeSliderWrapper::qt_metacast(const char *_clname)
{
    if (!_clname)
        return {};
    SbkObject *pySelf = Shiboken::BindingManager::instance().retrieveWrapper(this);
    if (pySelf && PySide::inherits(Py_TYPE(pySelf), _clname))
        return static_cast<void *>(const_cast< QRangeSliderWrapper *>(this));
    return QRangeSlider::qt_metacast(_clname);
}

QRangeSliderWrapper::~QRangeSliderWrapper()
{
    SbkObject *wrapper = Shiboken::BindingManager::instance().retrieveWrapper(this);
    Shiboken::Object::destroy(wrapper, this);
}

// Target ---------------------------------------------------------

extern "C" {
static int
Sbk_QRangeSlider_Init(PyObject *self, PyObject *args, PyObject *kwds)
{
    SBK_UNUSED(kwds)
    const QMetaObject *metaObject;
    SbkObject *sbkSelf = reinterpret_cast<SbkObject *>(self);
    PySide::Feature::Select(self);
    if (Shiboken::Object::isUserType(self) && !Shiboken::ObjectType::canCallConstructor(self->ob_type, Shiboken::SbkType< ::QRangeSlider >()))
        return -1;

    ::QRangeSliderWrapper *cptr{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qrangeslider.QRangeSlider.__init__";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp[2];
    SBK_UNUSED(pythonToCpp)
    const Py_ssize_t numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {nullptr, nullptr};

    // invalid argument lengths

    if (!PyArg_ParseTuple(args, "|OO:QRangeSlider", &(pyArgs[0]), &(pyArgs[1])))
        return -1;


    // Overloaded function decisor
    // 0: QRangeSlider::QRangeSlider(QWidget*)
    // 1: QRangeSlider::QRangeSlider(Qt::Orientation,QWidget*)
    if (numArgs == 0) {
        overloadId = 0; // QRangeSlider(QWidget*)
    } else if (numArgs >= 1
        && (pythonToCpp[0] = Shiboken::Conversions::pythonToCppConversion(PepType_SETP(reinterpret_cast<SbkEnumType *>(SbkPySide6_QtCoreTypes[SBK_QT_ORIENTATION_IDX]))->converter, (pyArgs[0])))) {
        if (numArgs == 1) {
            overloadId = 1; // QRangeSlider(Qt::Orientation,QWidget*)
        } else if (numArgs >= 2
            && (pythonToCpp[1] = Shiboken::Conversions::pythonToCppPointerConversion(SbkPySide6_QtWidgetsTypes[SBK_QWIDGET_IDX], (pyArgs[1])))) {
            overloadId = 1; // QRangeSlider(Qt::Orientation,QWidget*)
        }
    } else if (numArgs >= 1
        && (pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkPySide6_QtWidgetsTypes[SBK_QWIDGET_IDX], (pyArgs[0])))) {
        overloadId = 0; // QRangeSlider(QWidget*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QRangeSlider_Init_TypeError;

    // Call function/method
    switch (overloadId) {
        case 0: // QRangeSlider(QWidget * parent)
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
                        goto Sbk_QRangeSlider_Init_TypeError;
                    }
                    if (value) {
                        pyArgs[0] = value;
                        if (!(pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkPySide6_QtWidgetsTypes[SBK_QWIDGET_IDX], (pyArgs[0]))))
                            goto Sbk_QRangeSlider_Init_TypeError;
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
                // QRangeSlider(QWidget*)
                void *addr = PySide::nextQObjectMemoryAddr();
                if (addr) {
                    cptr = new (addr) ::QRangeSliderWrapper(cppArg0);
                    PySide::setNextQObjectMemoryAddr(nullptr);
                } else {
                    cptr = new ::QRangeSliderWrapper(cppArg0);
                }

                // Ownership transferences (constructor heuristics).
                Shiboken::Object::setParent(pyArgs[0], self);
            }
            break;
        }
        case 1: // QRangeSlider(Qt::Orientation orientation, QWidget * parent)
        {
            if (kwds && PyDict_Size(kwds) > 0) {
                PyObject *value{};
                Shiboken::AutoDecRef kwds_dup(PyDict_Copy(kwds));
                static PyObject *const key_parent = Shiboken::String::createStaticString("parent");
                if (PyDict_Contains(kwds, key_parent)) {
                    value = PyDict_GetItem(kwds, key_parent);
                    if (value && pyArgs[1]) {
                        errInfo.reset(key_parent);
                        Py_INCREF(errInfo.object());
                        goto Sbk_QRangeSlider_Init_TypeError;
                    }
                    if (value) {
                        pyArgs[1] = value;
                        if (!(pythonToCpp[1] = Shiboken::Conversions::pythonToCppPointerConversion(SbkPySide6_QtWidgetsTypes[SBK_QWIDGET_IDX], (pyArgs[1]))))
                            goto Sbk_QRangeSlider_Init_TypeError;
                    }
                    PyDict_DelItem(kwds_dup, key_parent);
                }
                if (PyDict_Size(kwds_dup) > 0) {
                    errInfo.reset(kwds_dup.release());
                    // fall through to handle extra keyword signals and properties
                }
            }
            ::Qt::Orientation cppArg0 = static_cast< ::Qt::Orientation>(0);
            pythonToCpp[0](pyArgs[0], &cppArg0);
            if (!Shiboken::Object::isValid(pyArgs[1]))
                return -1;
            ::QWidget *cppArg1 = nullptr;
            if (pythonToCpp[1])
                pythonToCpp[1](pyArgs[1], &cppArg1);

            if (!PyErr_Occurred()) {
                // QRangeSlider(Qt::Orientation,QWidget*)
                void *addr = PySide::nextQObjectMemoryAddr();
                if (addr) {
                    cptr = new (addr) ::QRangeSliderWrapper(cppArg0, cppArg1);
                    PySide::setNextQObjectMemoryAddr(nullptr);
                } else {
                    cptr = new ::QRangeSliderWrapper(cppArg0, cppArg1);
                }

                // Ownership transferences (constructor heuristics).
                Shiboken::Object::setParent(pyArgs[1], self);
            }
            break;
        }
    }

    if (PyErr_Occurred() || !Shiboken::Object::setCppPointer(sbkSelf, Shiboken::SbkType< ::QRangeSlider >(), cptr)) {
        delete cptr;
        return -1;
    }
    if (!cptr) goto Sbk_QRangeSlider_Init_TypeError;

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
            goto Sbk_QRangeSlider_Init_TypeError;
    };


    return 1;

    Sbk_QRangeSlider_Init_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return -1;
}

static PyObject *Sbk_QRangeSliderFunc_handleMovementMode(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QRangeSliderWrapper *>(reinterpret_cast< ::QRangeSlider *>(Shiboken::Conversions::cppPointer(SbkqrangesliderTypes[SBK_QRANGESLIDER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // handleMovementMode()const
            QRangeSlider::HandleMovementMode cppResult = QRangeSlider::HandleMovementMode(const_cast<const ::QRangeSliderWrapper *>(cppSelf)->handleMovementMode());
            pyResult = Shiboken::Conversions::copyToPython(PepType_SETP(reinterpret_cast<SbkEnumType *>(SbkqrangesliderTypes[SBK_QRANGESLIDER_HANDLEMOVEMENTMODE_IDX]))->converter, &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QRangeSliderFunc_keyPressEvent(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QRangeSliderWrapper *>(reinterpret_cast< ::QRangeSlider *>(Shiboken::Conversions::cppPointer(SbkqrangesliderTypes[SBK_QRANGESLIDER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qrangeslider.QRangeSlider.keyPressEvent";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QWidget::keyPressEvent(QKeyEvent*)
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppPointerConversion(SbkPySide6_QtGuiTypes[SBK_QKEYEVENT_IDX], (pyArg)))) {
        overloadId = 0; // keyPressEvent(QKeyEvent*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QRangeSliderFunc_keyPressEvent_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QKeyEvent *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // keyPressEvent(QKeyEvent*)
            static_cast<::QRangeSliderWrapper *>(cppSelf)->QRangeSliderWrapper::keyPressEvent_protected(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QRangeSliderFunc_keyPressEvent_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QRangeSliderFunc_lowerPosition(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QRangeSliderWrapper *>(reinterpret_cast< ::QRangeSlider *>(Shiboken::Conversions::cppPointer(SbkqrangesliderTypes[SBK_QRANGESLIDER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // lowerPosition()const
            int cppResult = const_cast<const ::QRangeSliderWrapper *>(cppSelf)->lowerPosition();
            pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<int>(), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QRangeSliderFunc_lowerValue(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QRangeSliderWrapper *>(reinterpret_cast< ::QRangeSlider *>(Shiboken::Conversions::cppPointer(SbkqrangesliderTypes[SBK_QRANGESLIDER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // lowerValue()const
            int cppResult = const_cast<const ::QRangeSliderWrapper *>(cppSelf)->lowerValue();
            pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<int>(), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QRangeSliderFunc_mouseMoveEvent(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QRangeSliderWrapper *>(reinterpret_cast< ::QRangeSlider *>(Shiboken::Conversions::cppPointer(SbkqrangesliderTypes[SBK_QRANGESLIDER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qrangeslider.QRangeSlider.mouseMoveEvent";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QWidget::mouseMoveEvent(QMouseEvent*)
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppPointerConversion(SbkPySide6_QtGuiTypes[SBK_QMOUSEEVENT_IDX], (pyArg)))) {
        overloadId = 0; // mouseMoveEvent(QMouseEvent*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QRangeSliderFunc_mouseMoveEvent_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QMouseEvent *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // mouseMoveEvent(QMouseEvent*)
            static_cast<::QRangeSliderWrapper *>(cppSelf)->QRangeSliderWrapper::mouseMoveEvent_protected(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QRangeSliderFunc_mouseMoveEvent_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QRangeSliderFunc_mousePressEvent(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QRangeSliderWrapper *>(reinterpret_cast< ::QRangeSlider *>(Shiboken::Conversions::cppPointer(SbkqrangesliderTypes[SBK_QRANGESLIDER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qrangeslider.QRangeSlider.mousePressEvent";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QWidget::mousePressEvent(QMouseEvent*)
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppPointerConversion(SbkPySide6_QtGuiTypes[SBK_QMOUSEEVENT_IDX], (pyArg)))) {
        overloadId = 0; // mousePressEvent(QMouseEvent*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QRangeSliderFunc_mousePressEvent_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QMouseEvent *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // mousePressEvent(QMouseEvent*)
            static_cast<::QRangeSliderWrapper *>(cppSelf)->QRangeSliderWrapper::mousePressEvent_protected(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QRangeSliderFunc_mousePressEvent_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QRangeSliderFunc_mouseReleaseEvent(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QRangeSliderWrapper *>(reinterpret_cast< ::QRangeSlider *>(Shiboken::Conversions::cppPointer(SbkqrangesliderTypes[SBK_QRANGESLIDER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qrangeslider.QRangeSlider.mouseReleaseEvent";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QWidget::mouseReleaseEvent(QMouseEvent*)
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppPointerConversion(SbkPySide6_QtGuiTypes[SBK_QMOUSEEVENT_IDX], (pyArg)))) {
        overloadId = 0; // mouseReleaseEvent(QMouseEvent*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QRangeSliderFunc_mouseReleaseEvent_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QMouseEvent *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // mouseReleaseEvent(QMouseEvent*)
            static_cast<::QRangeSliderWrapper *>(cppSelf)->QRangeSliderWrapper::mouseReleaseEvent_protected(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QRangeSliderFunc_mouseReleaseEvent_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QRangeSliderFunc_paintEvent(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QRangeSliderWrapper *>(reinterpret_cast< ::QRangeSlider *>(Shiboken::Conversions::cppPointer(SbkqrangesliderTypes[SBK_QRANGESLIDER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qrangeslider.QRangeSlider.paintEvent";
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
    if (overloadId == -1) goto Sbk_QRangeSliderFunc_paintEvent_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QPaintEvent *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // paintEvent(QPaintEvent*)
            static_cast<::QRangeSliderWrapper *>(cppSelf)->QRangeSliderWrapper::paintEvent_protected(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QRangeSliderFunc_paintEvent_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QRangeSliderFunc_setHandleMovementMode(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QRangeSliderWrapper *>(reinterpret_cast< ::QRangeSlider *>(Shiboken::Conversions::cppPointer(SbkqrangesliderTypes[SBK_QRANGESLIDER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qrangeslider.QRangeSlider.setHandleMovementMode";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QRangeSlider::setHandleMovementMode(QRangeSlider::HandleMovementMode)
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppConversion(PepType_SETP(reinterpret_cast<SbkEnumType *>(SbkqrangesliderTypes[SBK_QRANGESLIDER_HANDLEMOVEMENTMODE_IDX]))->converter, (pyArg)))) {
        overloadId = 0; // setHandleMovementMode(QRangeSlider::HandleMovementMode)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QRangeSliderFunc_setHandleMovementMode_TypeError;

    // Call function/method
    {
        ::QRangeSlider::HandleMovementMode cppArg0{QRangeSlider::FreeMovement};
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // setHandleMovementMode(QRangeSlider::HandleMovementMode)
            cppSelf->setHandleMovementMode(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QRangeSliderFunc_setHandleMovementMode_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QRangeSliderFunc_setLowerPosition(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QRangeSliderWrapper *>(reinterpret_cast< ::QRangeSlider *>(Shiboken::Conversions::cppPointer(SbkqrangesliderTypes[SBK_QRANGESLIDER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qrangeslider.QRangeSlider.setLowerPosition";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QRangeSlider::setLowerPosition(int)
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppConversion(Shiboken::Conversions::PrimitiveTypeConverter<int>(), (pyArg)))) {
        overloadId = 0; // setLowerPosition(int)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QRangeSliderFunc_setLowerPosition_TypeError;

    // Call function/method
    {
        int cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // setLowerPosition(int)
            cppSelf->setLowerPosition(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QRangeSliderFunc_setLowerPosition_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QRangeSliderFunc_setLowerValue(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QRangeSliderWrapper *>(reinterpret_cast< ::QRangeSlider *>(Shiboken::Conversions::cppPointer(SbkqrangesliderTypes[SBK_QRANGESLIDER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qrangeslider.QRangeSlider.setLowerValue";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QRangeSlider::setLowerValue(int)
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppConversion(Shiboken::Conversions::PrimitiveTypeConverter<int>(), (pyArg)))) {
        overloadId = 0; // setLowerValue(int)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QRangeSliderFunc_setLowerValue_TypeError;

    // Call function/method
    {
        int cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // setLowerValue(int)
            cppSelf->setLowerValue(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QRangeSliderFunc_setLowerValue_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QRangeSliderFunc_setSpan(PyObject *self, PyObject *args)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QRangeSliderWrapper *>(reinterpret_cast< ::QRangeSlider *>(Shiboken::Conversions::cppPointer(SbkqrangesliderTypes[SBK_QRANGESLIDER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qrangeslider.QRangeSlider.setSpan";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp[2];
    SBK_UNUSED(pythonToCpp)
    const Py_ssize_t numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {nullptr, nullptr};

    // invalid argument lengths

    if (!PyArg_UnpackTuple(args, "setSpan", 2, 2, &(pyArgs[0]), &(pyArgs[1])))
        return {};


    // Overloaded function decisor
    // 0: QRangeSlider::setSpan(int,int)
    if (numArgs == 2
        && (pythonToCpp[0] = Shiboken::Conversions::pythonToCppConversion(Shiboken::Conversions::PrimitiveTypeConverter<int>(), (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::pythonToCppConversion(Shiboken::Conversions::PrimitiveTypeConverter<int>(), (pyArgs[1])))) {
        overloadId = 0; // setSpan(int,int)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QRangeSliderFunc_setSpan_TypeError;

    // Call function/method
    {
        int cppArg0;
        pythonToCpp[0](pyArgs[0], &cppArg0);
        int cppArg1;
        pythonToCpp[1](pyArgs[1], &cppArg1);

        if (!PyErr_Occurred()) {
            // setSpan(int,int)
            cppSelf->setSpan(cppArg0, cppArg1);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QRangeSliderFunc_setSpan_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QRangeSliderFunc_setUpperPosition(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QRangeSliderWrapper *>(reinterpret_cast< ::QRangeSlider *>(Shiboken::Conversions::cppPointer(SbkqrangesliderTypes[SBK_QRANGESLIDER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qrangeslider.QRangeSlider.setUpperPosition";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QRangeSlider::setUpperPosition(int)
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppConversion(Shiboken::Conversions::PrimitiveTypeConverter<int>(), (pyArg)))) {
        overloadId = 0; // setUpperPosition(int)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QRangeSliderFunc_setUpperPosition_TypeError;

    // Call function/method
    {
        int cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // setUpperPosition(int)
            cppSelf->setUpperPosition(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QRangeSliderFunc_setUpperPosition_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QRangeSliderFunc_setUpperValue(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QRangeSliderWrapper *>(reinterpret_cast< ::QRangeSlider *>(Shiboken::Conversions::cppPointer(SbkqrangesliderTypes[SBK_QRANGESLIDER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qrangeslider.QRangeSlider.setUpperValue";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QRangeSlider::setUpperValue(int)
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppConversion(Shiboken::Conversions::PrimitiveTypeConverter<int>(), (pyArg)))) {
        overloadId = 0; // setUpperValue(int)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QRangeSliderFunc_setUpperValue_TypeError;

    // Call function/method
    {
        int cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // setUpperValue(int)
            cppSelf->setUpperValue(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QRangeSliderFunc_setUpperValue_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QRangeSliderFunc_upperPosition(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QRangeSliderWrapper *>(reinterpret_cast< ::QRangeSlider *>(Shiboken::Conversions::cppPointer(SbkqrangesliderTypes[SBK_QRANGESLIDER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // upperPosition()const
            int cppResult = const_cast<const ::QRangeSliderWrapper *>(cppSelf)->upperPosition();
            pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<int>(), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QRangeSliderFunc_upperValue(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QRangeSliderWrapper *>(reinterpret_cast< ::QRangeSlider *>(Shiboken::Conversions::cppPointer(SbkqrangesliderTypes[SBK_QRANGESLIDER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // upperValue()const
            int cppResult = const_cast<const ::QRangeSliderWrapper *>(cppSelf)->upperValue();
            pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<int>(), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}


static const char *Sbk_QRangeSlider_PropertyStrings[] = {
    "handleMovementMode::",
    "lowerPosition::",
    "lowerValue::",
    "upperPosition::",
    "upperValue::",
    nullptr // Sentinel
};

static const char *Sbk_QRangeSlider_EnumFlagInfo[] = {
    "HandleMovementMode:IntEnum",
    "SpanHandle:IntEnum",
    nullptr // Sentinel
};

static PyMethodDef Sbk_QRangeSlider_methods[] = {
    {"handleMovementMode", reinterpret_cast<PyCFunction>(Sbk_QRangeSliderFunc_handleMovementMode), METH_NOARGS, nullptr},
    {"keyPressEvent", reinterpret_cast<PyCFunction>(Sbk_QRangeSliderFunc_keyPressEvent), METH_O, nullptr},
    {"lowerPosition", reinterpret_cast<PyCFunction>(Sbk_QRangeSliderFunc_lowerPosition), METH_NOARGS, nullptr},
    {"lowerValue", reinterpret_cast<PyCFunction>(Sbk_QRangeSliderFunc_lowerValue), METH_NOARGS, nullptr},
    {"mouseMoveEvent", reinterpret_cast<PyCFunction>(Sbk_QRangeSliderFunc_mouseMoveEvent), METH_O, nullptr},
    {"mousePressEvent", reinterpret_cast<PyCFunction>(Sbk_QRangeSliderFunc_mousePressEvent), METH_O, nullptr},
    {"mouseReleaseEvent", reinterpret_cast<PyCFunction>(Sbk_QRangeSliderFunc_mouseReleaseEvent), METH_O, nullptr},
    {"paintEvent", reinterpret_cast<PyCFunction>(Sbk_QRangeSliderFunc_paintEvent), METH_O, nullptr},
    {"setHandleMovementMode", reinterpret_cast<PyCFunction>(Sbk_QRangeSliderFunc_setHandleMovementMode), METH_O, nullptr},
    {"setLowerPosition", reinterpret_cast<PyCFunction>(Sbk_QRangeSliderFunc_setLowerPosition), METH_O, nullptr},
    {"setLowerValue", reinterpret_cast<PyCFunction>(Sbk_QRangeSliderFunc_setLowerValue), METH_O, nullptr},
    {"setSpan", reinterpret_cast<PyCFunction>(Sbk_QRangeSliderFunc_setSpan), METH_VARARGS, nullptr},
    {"setUpperPosition", reinterpret_cast<PyCFunction>(Sbk_QRangeSliderFunc_setUpperPosition), METH_O, nullptr},
    {"setUpperValue", reinterpret_cast<PyCFunction>(Sbk_QRangeSliderFunc_setUpperValue), METH_O, nullptr},
    {"upperPosition", reinterpret_cast<PyCFunction>(Sbk_QRangeSliderFunc_upperPosition), METH_NOARGS, nullptr},
    {"upperValue", reinterpret_cast<PyCFunction>(Sbk_QRangeSliderFunc_upperValue), METH_NOARGS, nullptr},

    {nullptr, nullptr, 0, nullptr} // Sentinel
};

static int Sbk_QRangeSlider_setattro(PyObject *self, PyObject *name, PyObject *value)
{
    PySide::Feature::Select(self);
    if (value && PyCallable_Check(value)) {
        auto plain_inst = reinterpret_cast< ::QRangeSlider *>(Shiboken::Conversions::cppPointer(SbkqrangesliderTypes[SBK_QRANGESLIDER_IDX], reinterpret_cast<SbkObject *>(self)));
        auto inst = dynamic_cast<QRangeSliderWrapper *>(plain_inst);
        if (inst)
            inst->resetPyMethodCache();
    }
    Shiboken::AutoDecRef pp(reinterpret_cast<PyObject *>(PySide::Property::getObject(self, name)));
    if (!pp.isNull())
        return PySide::Property::setValue(reinterpret_cast<PySideProperty *>(pp.object()), self, value);
    return PyObject_GenericSetAttr(self, name, value);
}

} // extern "C"

static int Sbk_QRangeSlider_traverse(PyObject *self, visitproc visit, void *arg)
{
    return SbkObject_TypeF()->tp_traverse(self, visit, arg);
}
static int Sbk_QRangeSlider_clear(PyObject *self)
{
    return reinterpret_cast<PyTypeObject *>(SbkObject_TypeF())->tp_clear(self);
}
static void * Sbk_QRangeSliderSpecialCastFunction(void *obj, PyTypeObject *desiredType)
{
    auto me = reinterpret_cast< ::QRangeSlider *>(obj);
    if (desiredType == SbkPySide6_QtWidgetsTypes[SBK_QSLIDER_IDX])
        return static_cast< ::QSlider *>(me);
    else if (desiredType == SbkPySide6_QtWidgetsTypes[SBK_QABSTRACTSLIDER_IDX])
        return static_cast< ::QAbstractSlider *>(me);
    else if (desiredType == SbkPySide6_QtWidgetsTypes[SBK_QWIDGET_IDX])
        return static_cast< ::QWidget *>(me);
    else if (desiredType == SbkPySide6_QtCoreTypes[SBK_QOBJECT_IDX])
        return static_cast< ::QObject *>(me);
    else if (desiredType == SbkPySide6_QtGuiTypes[SBK_QPAINTDEVICE_IDX])
        return static_cast< ::QPaintDevice *>(me);
    return me;
}


// Class Definition -----------------------------------------------
extern "C" {
static PyTypeObject *_Sbk_QRangeSlider_Type = nullptr;
static PyTypeObject *Sbk_QRangeSlider_TypeF(void)
{
    return _Sbk_QRangeSlider_Type;
}

static PyType_Slot Sbk_QRangeSlider_slots[] = {
    {Py_tp_base,        nullptr}, // inserted by introduceWrapperType
    {Py_tp_dealloc,     reinterpret_cast<void *>(&SbkDeallocWrapper)},
    {Py_tp_repr,        nullptr},
    {Py_tp_hash,        nullptr},
    {Py_tp_call,        nullptr},
    {Py_tp_str,         nullptr},
    {Py_tp_getattro,    nullptr},
    {Py_tp_setattro,    reinterpret_cast<void *>(Sbk_QRangeSlider_setattro)},
    {Py_tp_traverse,    reinterpret_cast<void *>(Sbk_QRangeSlider_traverse)},
    {Py_tp_clear,       reinterpret_cast<void *>(Sbk_QRangeSlider_clear)},
    {Py_tp_richcompare, nullptr},
    {Py_tp_iter,        nullptr},
    {Py_tp_iternext,    nullptr},
    {Py_tp_methods,     reinterpret_cast<void *>(Sbk_QRangeSlider_methods)},
    {Py_tp_getset,      nullptr},
    {Py_tp_init,        reinterpret_cast<void *>(Sbk_QRangeSlider_Init)},
    {Py_tp_new,         reinterpret_cast<void *>(SbkObject_tp_new)},
    {0, nullptr}
};
static PyType_Spec Sbk_QRangeSlider_spec = {
    "1:qrangeslider.QRangeSlider",
    sizeof(SbkObject),
    0,
    Py_TPFLAGS_DEFAULT|Py_TPFLAGS_BASETYPE|Py_TPFLAGS_HAVE_GC,
    Sbk_QRangeSlider_slots
};

} //extern "C"

static void *Sbk_QRangeSlider_typeDiscovery(void *cptr, PyTypeObject *instanceType)
{
    SBK_UNUSED(cptr)
    SBK_UNUSED(instanceType)
    if (instanceType == Shiboken::SbkType< ::QObject >())
        return dynamic_cast< ::QRangeSlider *>(reinterpret_cast< ::QObject *>(cptr));
    if (instanceType == Shiboken::SbkType< ::QPaintDevice >())
        return dynamic_cast< ::QRangeSlider *>(reinterpret_cast< ::QPaintDevice *>(cptr));
    return {};
}


// Type conversion functions.

// Python to C++ enum conversion.
static void QRangeSlider_HandleMovementMode_PythonToCpp_QRangeSlider_HandleMovementMode(PyObject *pyIn, void *cppOut)
{
    const auto value = static_cast<::QRangeSlider::HandleMovementMode>(Shiboken::Enum::getValue(pyIn));
    *reinterpret_cast<::QRangeSlider::HandleMovementMode *>(cppOut) = value;

}
static PythonToCppFunc is_QRangeSlider_HandleMovementMode_PythonToCpp_QRangeSlider_HandleMovementMode_Convertible(PyObject *pyIn)
{
    if (PyObject_TypeCheck(pyIn, SbkqrangesliderTypes[SBK_QRANGESLIDER_HANDLEMOVEMENTMODE_IDX]))
        return QRangeSlider_HandleMovementMode_PythonToCpp_QRangeSlider_HandleMovementMode;
    return {};
}
static PyObject *QRangeSlider_HandleMovementMode_CppToPython_QRangeSlider_HandleMovementMode(const void *cppIn)
{
    const int castCppIn = int(*reinterpret_cast<const ::QRangeSlider::HandleMovementMode *>(cppIn));
    return Shiboken::Enum::newItem(SbkqrangesliderTypes[SBK_QRANGESLIDER_HANDLEMOVEMENTMODE_IDX], castCppIn);

}

static void QRangeSlider_SpanHandle_PythonToCpp_QRangeSlider_SpanHandle(PyObject *pyIn, void *cppOut)
{
    const auto value = static_cast<::QRangeSlider::SpanHandle>(Shiboken::Enum::getValue(pyIn));
    *reinterpret_cast<::QRangeSlider::SpanHandle *>(cppOut) = value;

}
static PythonToCppFunc is_QRangeSlider_SpanHandle_PythonToCpp_QRangeSlider_SpanHandle_Convertible(PyObject *pyIn)
{
    if (PyObject_TypeCheck(pyIn, SbkqrangesliderTypes[SBK_QRANGESLIDER_SPANHANDLE_IDX]))
        return QRangeSlider_SpanHandle_PythonToCpp_QRangeSlider_SpanHandle;
    return {};
}
static PyObject *QRangeSlider_SpanHandle_CppToPython_QRangeSlider_SpanHandle(const void *cppIn)
{
    const int castCppIn = int(*reinterpret_cast<const ::QRangeSlider::SpanHandle *>(cppIn));
    return Shiboken::Enum::newItem(SbkqrangesliderTypes[SBK_QRANGESLIDER_SPANHANDLE_IDX], castCppIn);

}

// Python to C++ pointer conversion - returns the C++ object of the Python wrapper (keeps object identity).
static void QRangeSlider_PythonToCpp_QRangeSlider_PTR(PyObject *pyIn, void *cppOut)
{
    Shiboken::Conversions::pythonToCppPointer(Sbk_QRangeSlider_TypeF(), pyIn, cppOut);
}
static PythonToCppFunc is_QRangeSlider_PythonToCpp_QRangeSlider_PTR_Convertible(PyObject *pyIn)
{
    if (pyIn == Py_None)
        return Shiboken::Conversions::nonePythonToCppNullPtr;
    if (PyObject_TypeCheck(pyIn, Sbk_QRangeSlider_TypeF()))
        return QRangeSlider_PythonToCpp_QRangeSlider_PTR;
    return {};
}

// C++ to Python pointer conversion - tries to find the Python wrapper for the C++ object (keeps object identity).
static PyObject *QRangeSlider_PTR_CppToPython_QRangeSlider(const void *cppIn)
{
    return PySide::getWrapperForQObject(reinterpret_cast<::QRangeSlider *>(const_cast<void *>(cppIn)), Sbk_QRangeSlider_TypeF());

}

// The signatures string for the functions.
// Multiple signatures have their index "n:" in front.
static const char *QRangeSlider_SignatureStrings[] = {
    "1:qrangeslider.QRangeSlider(self,parent:PySide6.QtWidgets.QWidget=nullptr)",
    "0:qrangeslider.QRangeSlider(self,orientation:PySide6.QtCore.Qt.Orientation,parent:PySide6.QtWidgets.QWidget=nullptr)",
    "qrangeslider.QRangeSlider.handleMovementMode(self)->qrangeslider.QRangeSlider.HandleMovementMode",
    "qrangeslider.QRangeSlider.keyPressEvent(self,event:PySide6.QtGui.QKeyEvent)",
    "qrangeslider.QRangeSlider.lowerPosition(self)->int",
    "qrangeslider.QRangeSlider.lowerValue(self)->int",
    "qrangeslider.QRangeSlider.mouseMoveEvent(self,event:PySide6.QtGui.QMouseEvent)",
    "qrangeslider.QRangeSlider.mousePressEvent(self,event:PySide6.QtGui.QMouseEvent)",
    "qrangeslider.QRangeSlider.mouseReleaseEvent(self,event:PySide6.QtGui.QMouseEvent)",
    "qrangeslider.QRangeSlider.paintEvent(self,event:PySide6.QtGui.QPaintEvent)",
    "qrangeslider.QRangeSlider.setHandleMovementMode(self,mode:qrangeslider.QRangeSlider.HandleMovementMode)",
    "qrangeslider.QRangeSlider.setLowerPosition(self,lower:int)",
    "qrangeslider.QRangeSlider.setLowerValue(self,lower:int)",
    "qrangeslider.QRangeSlider.setSpan(self,lower:int,upper:int)",
    "qrangeslider.QRangeSlider.setUpperPosition(self,upper:int)",
    "qrangeslider.QRangeSlider.setUpperValue(self,upper:int)",
    "qrangeslider.QRangeSlider.upperPosition(self)->int",
    "qrangeslider.QRangeSlider.upperValue(self)->int",
    nullptr}; // Sentinel

void init_QRangeSlider(PyObject *module)
{
    _Sbk_QRangeSlider_Type = Shiboken::ObjectType::introduceWrapperType(
        module,
        "QRangeSlider",
        "QRangeSlider*",
        &Sbk_QRangeSlider_spec,
        &Shiboken::callCppDestructor< ::QRangeSlider >,
        SbkPySide6_QtWidgetsTypes[SBK_QSLIDER_IDX],
        0,
        Shiboken::ObjectType::WrapperFlags::DeleteInMainThread);
    auto *pyType = Sbk_QRangeSlider_TypeF(); // references _Sbk_QRangeSlider_Type
    InitSignatureStrings(pyType, QRangeSlider_SignatureStrings);
    SbkObjectType_SetPropertyStrings(pyType, Sbk_QRangeSlider_PropertyStrings);
    SbkqrangesliderTypes[SBK_QRANGESLIDER_IDX] = pyType;

    // Register Converter
    SbkConverter *converter = Shiboken::Conversions::createConverter(pyType,
        QRangeSlider_PythonToCpp_QRangeSlider_PTR,
        is_QRangeSlider_PythonToCpp_QRangeSlider_PTR_Convertible,
        QRangeSlider_PTR_CppToPython_QRangeSlider);

    Shiboken::Conversions::registerConverterName(converter, "QRangeSlider");
    Shiboken::Conversions::registerConverterName(converter, "QRangeSlider*");
    Shiboken::Conversions::registerConverterName(converter, "QRangeSlider&");
    Shiboken::Conversions::registerConverterName(converter, typeid(::QRangeSlider).name());
    Shiboken::Conversions::registerConverterName(converter, typeid(::QRangeSliderWrapper).name());


    MultipleInheritanceInitFunction func = Shiboken::ObjectType::getMultipleInheritanceFunction(SbkPySide6_QtWidgetsTypes[SBK_QWIDGET_IDX]);
    Shiboken::ObjectType::setMultipleInheritanceFunction(Sbk_QRangeSlider_TypeF(), func);
    Shiboken::ObjectType::setCastFunction(Sbk_QRangeSlider_TypeF(), &Sbk_QRangeSliderSpecialCastFunction);
    Shiboken::ObjectType::setTypeDiscoveryFunctionV2(Sbk_QRangeSlider_TypeF(), &Sbk_QRangeSlider_typeDiscovery);

    // Pass the ..._EnumFlagInfo to the class.
    SbkObjectType_SetEnumFlagInfo(pyType, Sbk_QRangeSlider_EnumFlagInfo);

    // Initialization of enums.
    PyTypeObject *EType{};

    // Initialization of enum 'HandleMovementMode'.
    EType = Shiboken::Enum::createScopedEnum(Sbk_QRangeSlider_TypeF(),
        "HandleMovementMode",
        "1:qrangeslider.QRangeSlider.HandleMovementMode",
        "QRangeSlider::HandleMovementMode");
    if (!EType)
        return;

    if (!Shiboken::Enum::createScopedEnumItem(EType,
        Sbk_QRangeSlider_TypeF(), "FreeMovement", Shiboken::Enum::EnumValueType(QRangeSlider::HandleMovementMode::FreeMovement)))
        return;
    if (!Shiboken::Enum::createScopedEnumItem(EType,
        Sbk_QRangeSlider_TypeF(), "NoCrossing", Shiboken::Enum::EnumValueType(QRangeSlider::HandleMovementMode::NoCrossing)))
        return;
    if (!Shiboken::Enum::createScopedEnumItem(EType,
        Sbk_QRangeSlider_TypeF(), "NoOverlapping", Shiboken::Enum::EnumValueType(QRangeSlider::HandleMovementMode::NoOverlapping)))
        return;
    // PYSIDE-1735: Resolving the whole enum class at the end for API compatibility.
    EType = morphLastEnumToPython();
    SbkqrangesliderTypes[SBK_QRANGESLIDER_HANDLEMOVEMENTMODE_IDX] = EType;
    // Register converter for enum 'QRangeSlider::HandleMovementMode'.
    {
        SbkConverter *converter = Shiboken::Conversions::createConverter(EType,
            QRangeSlider_HandleMovementMode_CppToPython_QRangeSlider_HandleMovementMode);
        Shiboken::Conversions::addPythonToCppValueConversion(converter,
            QRangeSlider_HandleMovementMode_PythonToCpp_QRangeSlider_HandleMovementMode,
            is_QRangeSlider_HandleMovementMode_PythonToCpp_QRangeSlider_HandleMovementMode_Convertible);
        Shiboken::Enum::setTypeConverter(EType, converter, false);
        Shiboken::Conversions::registerConverterName(converter, "QRangeSlider::HandleMovementMode");
        Shiboken::Conversions::registerConverterName(converter, "HandleMovementMode");
    }
    // End of 'HandleMovementMode' enum.

    // Initialization of enum 'SpanHandle'.
    EType = Shiboken::Enum::createScopedEnum(Sbk_QRangeSlider_TypeF(),
        "SpanHandle",
        "1:qrangeslider.QRangeSlider.SpanHandle",
        "QRangeSlider::SpanHandle");
    if (!EType)
        return;

    if (!Shiboken::Enum::createScopedEnumItem(EType,
        Sbk_QRangeSlider_TypeF(), "NoHandle", Shiboken::Enum::EnumValueType(QRangeSlider::SpanHandle::NoHandle)))
        return;
    if (!Shiboken::Enum::createScopedEnumItem(EType,
        Sbk_QRangeSlider_TypeF(), "LowerHandle", Shiboken::Enum::EnumValueType(QRangeSlider::SpanHandle::LowerHandle)))
        return;
    if (!Shiboken::Enum::createScopedEnumItem(EType,
        Sbk_QRangeSlider_TypeF(), "UpperHandle", Shiboken::Enum::EnumValueType(QRangeSlider::SpanHandle::UpperHandle)))
        return;
    // PYSIDE-1735: Resolving the whole enum class at the end for API compatibility.
    EType = morphLastEnumToPython();
    SbkqrangesliderTypes[SBK_QRANGESLIDER_SPANHANDLE_IDX] = EType;
    // Register converter for enum 'QRangeSlider::SpanHandle'.
    {
        SbkConverter *converter = Shiboken::Conversions::createConverter(EType,
            QRangeSlider_SpanHandle_CppToPython_QRangeSlider_SpanHandle);
        Shiboken::Conversions::addPythonToCppValueConversion(converter,
            QRangeSlider_SpanHandle_PythonToCpp_QRangeSlider_SpanHandle,
            is_QRangeSlider_SpanHandle_PythonToCpp_QRangeSlider_SpanHandle_Convertible);
        Shiboken::Enum::setTypeConverter(EType, converter, false);
        Shiboken::Conversions::registerConverterName(converter, "QRangeSlider::SpanHandle");
        Shiboken::Conversions::registerConverterName(converter, "SpanHandle");
    }
    // End of 'SpanHandle' enum.

    PySide::Signal::registerSignals(pyType, &::QRangeSlider::staticMetaObject);
    QRangeSliderWrapper::pysideInitQtMetaTypes();
    Shiboken::ObjectType::setSubTypeInitHook(pyType, &PySide::initQObjectSubType);
    PySide::initDynamicMetaObject(pyType, &::QRangeSlider::staticMetaObject, sizeof(QRangeSliderWrapper));
}
