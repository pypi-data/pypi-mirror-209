
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
#include "qtpropertybrowser_python.h"

// main header
#include "qttreepropertybrowser_wrapper.h"

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

void QtTreePropertyBrowserWrapper::pysideInitQtMetaTypes()
{
    qRegisterMetaType< ::QtTreePropertyBrowser::ResizeMode >("QtTreePropertyBrowser::ResizeMode");
}

void QtTreePropertyBrowserWrapper::resetPyMethodCache()
{
    std::fill_n(m_PyMethodCache, sizeof(m_PyMethodCache) / sizeof(m_PyMethodCache[0]), false);
}

QtTreePropertyBrowserWrapper::QtTreePropertyBrowserWrapper(QWidget * parent) : QtTreePropertyBrowser(parent)
{
    resetPyMethodCache();
    // ... middle
}

void QtTreePropertyBrowserWrapper::actionEvent(QActionEvent * event)
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

void QtTreePropertyBrowserWrapper::changeEvent(QEvent * event)
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

void QtTreePropertyBrowserWrapper::childEvent(QChildEvent * event)
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

void QtTreePropertyBrowserWrapper::closeEvent(QCloseEvent * event)
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

void QtTreePropertyBrowserWrapper::connectNotify(const QMetaMethod & signal)
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

void QtTreePropertyBrowserWrapper::contextMenuEvent(QContextMenuEvent * event)
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

QWidget * QtTreePropertyBrowserWrapper::createAttributeEditor(QtProperty * property, QWidget * parent, BrowserCol attribute)
{
    if (m_PyMethodCache[6])
        return this->::QtAbstractPropertyBrowser::createAttributeEditor(property, parent, attribute);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return nullptr;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "createAttributeEditor";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[6] = true;
        gil.release();
        return this->::QtAbstractPropertyBrowser::createAttributeEditor(property, parent, attribute);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(NNN)",
        Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], property),
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtWidgetsTypes[SBK_QWIDGET_IDX], parent),
        Shiboken::Conversions::copyToPython(PepType_SETP(reinterpret_cast<SbkEnumType *>(SbkqtpropertybrowserTypes[SBK_BROWSERCOL_IDX]))->converter, &attribute)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return nullptr;
    }
    // Check return type
    Shiboken::Conversions::PythonToCppConversion pythonToCpp =
        Shiboken::Conversions::pythonToCppPointerConversion(SbkPySide6_QtWidgetsTypes[SBK_QWIDGET_IDX], pyResult);
    if (!pythonToCpp) {
        Shiboken::Warnings::warnInvalidReturnValue("QtTreePropertyBrowser", "createAttributeEditor", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QWidget >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return nullptr;
    }
    ::QWidget *cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QWidget * QtTreePropertyBrowserWrapper::createEditor(QtProperty * property, QWidget * parent)
{
    if (m_PyMethodCache[7])
        return this->::QtAbstractPropertyBrowser::createEditor(property, parent);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return nullptr;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "createEditor";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[7] = true;
        gil.release();
        return this->::QtAbstractPropertyBrowser::createEditor(property, parent);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(NN)",
        Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], property),
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtWidgetsTypes[SBK_QWIDGET_IDX], parent)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return nullptr;
    }
    // Check return type
    Shiboken::Conversions::PythonToCppConversion pythonToCpp =
        Shiboken::Conversions::pythonToCppPointerConversion(SbkPySide6_QtWidgetsTypes[SBK_QWIDGET_IDX], pyResult);
    if (!pythonToCpp) {
        Shiboken::Warnings::warnInvalidReturnValue("QtTreePropertyBrowser", "createEditor", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QWidget >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return nullptr;
    }
    ::QWidget *cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtTreePropertyBrowserWrapper::customEvent(QEvent * event)
{
    if (m_PyMethodCache[8]) {
        return this->::QObject::customEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "customEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[8] = true;
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

int QtTreePropertyBrowserWrapper::devType() const
{
    if (m_PyMethodCache[9])
        return this->::QWidget::devType();
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return 0;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "devType";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[9] = true;
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
        Shiboken::Warnings::warnInvalidReturnValue("QtTreePropertyBrowser", "devType", "int", Py_TYPE(pyResult)->tp_name);
        return 0;
    }
    int cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtTreePropertyBrowserWrapper::disconnectNotify(const QMetaMethod & signal)
{
    if (m_PyMethodCache[10]) {
        return this->::QObject::disconnectNotify(signal);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "disconnectNotify";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[10] = true;
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

void QtTreePropertyBrowserWrapper::dragEnterEvent(QDragEnterEvent * event)
{
    if (m_PyMethodCache[11]) {
        return this->::QWidget::dragEnterEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "dragEnterEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[11] = true;
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

void QtTreePropertyBrowserWrapper::dragLeaveEvent(QDragLeaveEvent * event)
{
    if (m_PyMethodCache[12]) {
        return this->::QWidget::dragLeaveEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "dragLeaveEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[12] = true;
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

void QtTreePropertyBrowserWrapper::dragMoveEvent(QDragMoveEvent * event)
{
    if (m_PyMethodCache[13]) {
        return this->::QWidget::dragMoveEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "dragMoveEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[13] = true;
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

void QtTreePropertyBrowserWrapper::dropEvent(QDropEvent * event)
{
    if (m_PyMethodCache[14]) {
        return this->::QWidget::dropEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "dropEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[14] = true;
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

void QtTreePropertyBrowserWrapper::enterEvent(QEnterEvent * event)
{
    if (m_PyMethodCache[15]) {
        return this->::QWidget::enterEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "enterEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[15] = true;
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

bool QtTreePropertyBrowserWrapper::event(QEvent * event)
{
    if (m_PyMethodCache[16])
        return this->::QWidget::event(event);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return false;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "event";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[16] = true;
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
        Shiboken::Warnings::warnInvalidReturnValue("QtTreePropertyBrowser", "event", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

bool QtTreePropertyBrowserWrapper::eventFilter(QObject * watched, QEvent * event)
{
    if (m_PyMethodCache[17])
        return this->::QObject::eventFilter(watched, event);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return false;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "eventFilter";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[17] = true;
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
        Shiboken::Warnings::warnInvalidReturnValue("QtTreePropertyBrowser", "eventFilter", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtTreePropertyBrowserWrapper::focusInEvent(QFocusEvent * event)
{
    if (m_PyMethodCache[18]) {
        return this->::QWidget::focusInEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "focusInEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[18] = true;
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

bool QtTreePropertyBrowserWrapper::focusNextPrevChild(bool next)
{
    if (m_PyMethodCache[19])
        return this->::QWidget::focusNextPrevChild(next);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return false;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "focusNextPrevChild";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[19] = true;
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
        Shiboken::Warnings::warnInvalidReturnValue("QtTreePropertyBrowser", "focusNextPrevChild", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtTreePropertyBrowserWrapper::focusOutEvent(QFocusEvent * event)
{
    if (m_PyMethodCache[20]) {
        return this->::QWidget::focusOutEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "focusOutEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[20] = true;
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

bool QtTreePropertyBrowserWrapper::hasHeightForWidth() const
{
    if (m_PyMethodCache[21])
        return this->::QWidget::hasHeightForWidth();
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return false;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "hasHeightForWidth";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[21] = true;
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
        Shiboken::Warnings::warnInvalidReturnValue("QtTreePropertyBrowser", "hasHeightForWidth", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

int QtTreePropertyBrowserWrapper::heightForWidth(int arg__1) const
{
    if (m_PyMethodCache[22])
        return this->::QWidget::heightForWidth(arg__1);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return 0;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "heightForWidth";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[22] = true;
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
        Shiboken::Warnings::warnInvalidReturnValue("QtTreePropertyBrowser", "heightForWidth", "int", Py_TYPE(pyResult)->tp_name);
        return 0;
    }
    int cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtTreePropertyBrowserWrapper::hideEvent(QHideEvent * event)
{
    if (m_PyMethodCache[23]) {
        return this->::QWidget::hideEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "hideEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[23] = true;
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

void QtTreePropertyBrowserWrapper::initPainter(QPainter * painter) const
{
    if (m_PyMethodCache[24]) {
        return this->::QWidget::initPainter(painter);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "initPainter";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[24] = true;
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

void QtTreePropertyBrowserWrapper::inputMethodEvent(QInputMethodEvent * event)
{
    if (m_PyMethodCache[25]) {
        return this->::QWidget::inputMethodEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "inputMethodEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[25] = true;
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

QVariant QtTreePropertyBrowserWrapper::inputMethodQuery(Qt::InputMethodQuery arg__1) const
{
    if (m_PyMethodCache[26])
        return this->::QWidget::inputMethodQuery(arg__1);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return ::QVariant();
    static PyObject *nameCache[2] = {};
    static const char *funcName = "inputMethodQuery";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[26] = true;
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
        Shiboken::Warnings::warnInvalidReturnValue("QtTreePropertyBrowser", "inputMethodQuery", "QVariant", Py_TYPE(pyResult)->tp_name);
        return ::QVariant();
    }
    ::QVariant cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtTreePropertyBrowserWrapper::itemChanged(QtBrowserItem * item)
{
    if (m_PyMethodCache[27]) {
        return this->::QtTreePropertyBrowser::itemChanged(item);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "itemChanged";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[27] = true;
        gil.release();
        return this->::QtTreePropertyBrowser::itemChanged(item);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX], item)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

void QtTreePropertyBrowserWrapper::itemInserted(QtBrowserItem * item, QtBrowserItem * afterItem)
{
    if (m_PyMethodCache[28]) {
        return this->::QtTreePropertyBrowser::itemInserted(item, afterItem);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "itemInserted";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[28] = true;
        gil.release();
        return this->::QtTreePropertyBrowser::itemInserted(item, afterItem);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(NN)",
        Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX], item),
        Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX], afterItem)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

void QtTreePropertyBrowserWrapper::itemRemoved(QtBrowserItem * item)
{
    if (m_PyMethodCache[29]) {
        return this->::QtTreePropertyBrowser::itemRemoved(item);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "itemRemoved";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[29] = true;
        gil.release();
        return this->::QtTreePropertyBrowser::itemRemoved(item);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX], item)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

void QtTreePropertyBrowserWrapper::keyPressEvent(QKeyEvent * event)
{
    if (m_PyMethodCache[30]) {
        return this->::QWidget::keyPressEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "keyPressEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[30] = true;
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

void QtTreePropertyBrowserWrapper::keyReleaseEvent(QKeyEvent * event)
{
    if (m_PyMethodCache[31]) {
        return this->::QWidget::keyReleaseEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "keyReleaseEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[31] = true;
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

void QtTreePropertyBrowserWrapper::leaveEvent(QEvent * event)
{
    if (m_PyMethodCache[32]) {
        return this->::QWidget::leaveEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "leaveEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[32] = true;
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

int QtTreePropertyBrowserWrapper::metric(QPaintDevice::PaintDeviceMetric arg__1) const
{
    if (m_PyMethodCache[33])
        return this->::QWidget::metric(arg__1);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return 0;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "metric";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[33] = true;
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
        Shiboken::Warnings::warnInvalidReturnValue("QtTreePropertyBrowser", "metric", "int", Py_TYPE(pyResult)->tp_name);
        return 0;
    }
    int cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QSize QtTreePropertyBrowserWrapper::minimumSizeHint() const
{
    if (m_PyMethodCache[34])
        return this->::QWidget::minimumSizeHint();
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return {};
    static PyObject *nameCache[2] = {};
    // This method belongs to a property.
    static const char *funcName = "1:minimumSizeHint";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[34] = true;
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
        Shiboken::Warnings::warnInvalidReturnValue("QtTreePropertyBrowser", "minimumSizeHint", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QSize >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return {};
    }
    ::QSize cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtTreePropertyBrowserWrapper::mouseDoubleClickEvent(QMouseEvent * event)
{
    if (m_PyMethodCache[35]) {
        return this->::QWidget::mouseDoubleClickEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "mouseDoubleClickEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[35] = true;
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

void QtTreePropertyBrowserWrapper::mouseMoveEvent(QMouseEvent * event)
{
    if (m_PyMethodCache[36]) {
        return this->::QWidget::mouseMoveEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "mouseMoveEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[36] = true;
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

void QtTreePropertyBrowserWrapper::mousePressEvent(QMouseEvent * event)
{
    if (m_PyMethodCache[37]) {
        return this->::QWidget::mousePressEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "mousePressEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[37] = true;
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

void QtTreePropertyBrowserWrapper::mouseReleaseEvent(QMouseEvent * event)
{
    if (m_PyMethodCache[38]) {
        return this->::QWidget::mouseReleaseEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "mouseReleaseEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[38] = true;
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

void QtTreePropertyBrowserWrapper::moveEvent(QMoveEvent * event)
{
    if (m_PyMethodCache[39]) {
        return this->::QWidget::moveEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "moveEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[39] = true;
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

bool QtTreePropertyBrowserWrapper::nativeEvent(const QByteArray & eventType, void * message, qintptr * result)
{
    if (m_PyMethodCache[40]) {
        return this->::QWidget::nativeEvent(eventType, message, result);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return false;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "nativeEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[40] = true;
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

QPaintEngine * QtTreePropertyBrowserWrapper::paintEngine() const
{
    if (m_PyMethodCache[41])
        return this->::QWidget::paintEngine();
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return nullptr;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "paintEngine";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[41] = true;
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
        Shiboken::Warnings::warnInvalidReturnValue("QtTreePropertyBrowser", "paintEngine", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QPaintEngine >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return nullptr;
    }
    ::QPaintEngine *cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtTreePropertyBrowserWrapper::paintEvent(QPaintEvent * event)
{
    if (m_PyMethodCache[42]) {
        return this->::QWidget::paintEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "paintEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[42] = true;
        gil.release();
        return this->::QWidget::paintEvent(event);
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

QPaintDevice * QtTreePropertyBrowserWrapper::redirected(QPoint * offset) const
{
    if (m_PyMethodCache[43])
        return this->::QWidget::redirected(offset);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return nullptr;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "redirected";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[43] = true;
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
        Shiboken::Warnings::warnInvalidReturnValue("QtTreePropertyBrowser", "redirected", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QPaintDevice >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return nullptr;
    }
    ::QPaintDevice *cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtTreePropertyBrowserWrapper::resizeEvent(QResizeEvent * event)
{
    if (m_PyMethodCache[44]) {
        return this->::QWidget::resizeEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "resizeEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[44] = true;
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

void QtTreePropertyBrowserWrapper::setVisible(bool visible)
{
    if (m_PyMethodCache[45]) {
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
        m_PyMethodCache[45] = true;
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

QPainter * QtTreePropertyBrowserWrapper::sharedPainter() const
{
    if (m_PyMethodCache[46])
        return this->::QWidget::sharedPainter();
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return nullptr;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "sharedPainter";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[46] = true;
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
        Shiboken::Warnings::warnInvalidReturnValue("QtTreePropertyBrowser", "sharedPainter", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QPainter >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return nullptr;
    }
    ::QPainter *cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtTreePropertyBrowserWrapper::showEvent(QShowEvent * event)
{
    if (m_PyMethodCache[47]) {
        return this->::QWidget::showEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "showEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[47] = true;
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

QSize QtTreePropertyBrowserWrapper::sizeHint() const
{
    if (m_PyMethodCache[48])
        return this->::QWidget::sizeHint();
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return {};
    static PyObject *nameCache[2] = {};
    // This method belongs to a property.
    static const char *funcName = "1:sizeHint";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[48] = true;
        gil.release();
        return this->::QWidget::sizeHint();
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
        Shiboken::Warnings::warnInvalidReturnValue("QtTreePropertyBrowser", "sizeHint", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QSize >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return {};
    }
    ::QSize cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtTreePropertyBrowserWrapper::tabletEvent(QTabletEvent * event)
{
    if (m_PyMethodCache[49]) {
        return this->::QWidget::tabletEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "tabletEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[49] = true;
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

void QtTreePropertyBrowserWrapper::timerEvent(QTimerEvent * event)
{
    if (m_PyMethodCache[50]) {
        return this->::QObject::timerEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "timerEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[50] = true;
        gil.release();
        return this->::QObject::timerEvent(event);
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

void QtTreePropertyBrowserWrapper::wheelEvent(QWheelEvent * event)
{
    if (m_PyMethodCache[51]) {
        return this->::QWidget::wheelEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "wheelEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[51] = true;
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

const QMetaObject *QtTreePropertyBrowserWrapper::metaObject() const
{
    if (QObject::d_ptr->metaObject)
        return QObject::d_ptr->dynamicMetaObject();
    SbkObject *pySelf = Shiboken::BindingManager::instance().retrieveWrapper(this);
    if (pySelf == nullptr)
        return QtTreePropertyBrowser::metaObject();
    return PySide::SignalManager::retrieveMetaObject(reinterpret_cast<PyObject *>(pySelf));
}

int QtTreePropertyBrowserWrapper::qt_metacall(QMetaObject::Call call, int id, void **args)
{
    int result = QtTreePropertyBrowser::qt_metacall(call, id, args);
    return result < 0 ? result : PySide::SignalManager::qt_metacall(this, call, id, args);
}

void *QtTreePropertyBrowserWrapper::qt_metacast(const char *_clname)
{
    if (!_clname)
        return {};
    SbkObject *pySelf = Shiboken::BindingManager::instance().retrieveWrapper(this);
    if (pySelf && PySide::inherits(Py_TYPE(pySelf), _clname))
        return static_cast<void *>(const_cast< QtTreePropertyBrowserWrapper *>(this));
    return QtTreePropertyBrowser::qt_metacast(_clname);
}

QtTreePropertyBrowserWrapper::~QtTreePropertyBrowserWrapper()
{
    SbkObject *wrapper = Shiboken::BindingManager::instance().retrieveWrapper(this);
    Shiboken::Object::destroy(wrapper, this);
}

// Target ---------------------------------------------------------

extern "C" {
static int
Sbk_QtTreePropertyBrowser_Init(PyObject *self, PyObject *args, PyObject *kwds)
{
    SBK_UNUSED(kwds)
    const QMetaObject *metaObject;
    SbkObject *sbkSelf = reinterpret_cast<SbkObject *>(self);
    PySide::Feature::Select(self);
    if (Shiboken::Object::isUserType(self) && !Shiboken::ObjectType::canCallConstructor(self->ob_type, Shiboken::SbkType< ::QtTreePropertyBrowser >()))
        return -1;

    ::QtTreePropertyBrowserWrapper *cptr{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtTreePropertyBrowser.__init__";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp[1];
    SBK_UNUSED(pythonToCpp)
    const Py_ssize_t numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {nullptr};

    // invalid argument lengths

    if (!PyArg_ParseTuple(args, "|O:QtTreePropertyBrowser", &(pyArgs[0])))
        return -1;


    // Overloaded function decisor
    // 0: QtTreePropertyBrowser::QtTreePropertyBrowser(QWidget*)
    if (numArgs == 0) {
        overloadId = 0; // QtTreePropertyBrowser(QWidget*)
    } else if (numArgs >= 1
        && (pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkPySide6_QtWidgetsTypes[SBK_QWIDGET_IDX], (pyArgs[0])))) {
        overloadId = 0; // QtTreePropertyBrowser(QWidget*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtTreePropertyBrowser_Init_TypeError;

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
                    goto Sbk_QtTreePropertyBrowser_Init_TypeError;
                }
                if (value) {
                    pyArgs[0] = value;
                    if (!(pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkPySide6_QtWidgetsTypes[SBK_QWIDGET_IDX], (pyArgs[0]))))
                        goto Sbk_QtTreePropertyBrowser_Init_TypeError;
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
        ::QWidget *cppArg0 = 0;
        if (pythonToCpp[0])
            pythonToCpp[0](pyArgs[0], &cppArg0);

        if (!PyErr_Occurred()) {
            // QtTreePropertyBrowser(QWidget*)
            void *addr = PySide::nextQObjectMemoryAddr();
            if (addr) {
                cptr = new (addr) ::QtTreePropertyBrowserWrapper(cppArg0);
                PySide::setNextQObjectMemoryAddr(nullptr);
            } else {
                cptr = new ::QtTreePropertyBrowserWrapper(cppArg0);
            }

            // Ownership transferences (constructor heuristics).
            Shiboken::Object::setParent(pyArgs[0], self);
        }
    }

    if (PyErr_Occurred() || !Shiboken::Object::setCppPointer(sbkSelf, Shiboken::SbkType< ::QtTreePropertyBrowser >(), cptr)) {
        delete cptr;
        return -1;
    }
    if (!cptr) goto Sbk_QtTreePropertyBrowser_Init_TypeError;

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
            goto Sbk_QtTreePropertyBrowser_Init_TypeError;
    };


    return 1;

    Sbk_QtTreePropertyBrowser_Init_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return -1;
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_alternatingRowColors(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // alternatingRowColors()const
            bool cppResult = const_cast<const ::QtTreePropertyBrowserWrapper *>(cppSelf)->alternatingRowColors();
            pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_attributes(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // attributes()const
            BrowserCol cppResult = BrowserCol(const_cast<const ::QtTreePropertyBrowserWrapper *>(cppSelf)->attributes());
            pyResult = Shiboken::Conversions::copyToPython(PepType_SETP(reinterpret_cast<SbkEnumType *>(SbkqtpropertybrowserTypes[SBK_BROWSERCOL_IDX]))->converter, &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_backgroundColor(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtTreePropertyBrowser.backgroundColor";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtTreePropertyBrowser::backgroundColor(QtBrowserItem*)const->QColor
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX], (pyArg)))) {
        overloadId = 0; // backgroundColor(QtBrowserItem*)const
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtTreePropertyBrowserFunc_backgroundColor_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtBrowserItem *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // backgroundColor(QtBrowserItem*)const
            QColor cppResult = const_cast<const ::QtTreePropertyBrowserWrapper *>(cppSelf)->backgroundColor(cppArg0);
            pyResult = Shiboken::Conversions::copyToPython(SbkPySide6_QtGuiTypes[SBK_QCOLOR_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtTreePropertyBrowserFunc_backgroundColor_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_calculatedBackgroundColor(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtTreePropertyBrowser.calculatedBackgroundColor";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtTreePropertyBrowser::calculatedBackgroundColor(QtBrowserItem*)const->QColor
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX], (pyArg)))) {
        overloadId = 0; // calculatedBackgroundColor(QtBrowserItem*)const
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtTreePropertyBrowserFunc_calculatedBackgroundColor_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtBrowserItem *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // calculatedBackgroundColor(QtBrowserItem*)const
            QColor cppResult = const_cast<const ::QtTreePropertyBrowserWrapper *>(cppSelf)->calculatedBackgroundColor(cppArg0);
            pyResult = Shiboken::Conversions::copyToPython(SbkPySide6_QtGuiTypes[SBK_QCOLOR_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtTreePropertyBrowserFunc_calculatedBackgroundColor_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_editItem(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtTreePropertyBrowser.editItem";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtTreePropertyBrowser::editItem(QtBrowserItem*)
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX], (pyArg)))) {
        overloadId = 0; // editItem(QtBrowserItem*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtTreePropertyBrowserFunc_editItem_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtBrowserItem *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // editItem(QtBrowserItem*)
            cppSelf->editItem(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtTreePropertyBrowserFunc_editItem_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_indentation(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // indentation()const
            int cppResult = const_cast<const ::QtTreePropertyBrowserWrapper *>(cppSelf)->indentation();
            pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<int>(), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_isExpanded(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtTreePropertyBrowser.isExpanded";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtTreePropertyBrowser::isExpanded(QtBrowserItem*)const->bool
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX], (pyArg)))) {
        overloadId = 0; // isExpanded(QtBrowserItem*)const
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtTreePropertyBrowserFunc_isExpanded_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtBrowserItem *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // isExpanded(QtBrowserItem*)const
            bool cppResult = const_cast<const ::QtTreePropertyBrowserWrapper *>(cppSelf)->isExpanded(cppArg0);
            pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtTreePropertyBrowserFunc_isExpanded_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_isHeaderVisible(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // isHeaderVisible()const
            bool cppResult = const_cast<const ::QtTreePropertyBrowserWrapper *>(cppSelf)->isHeaderVisible();
            pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_isItemVisible(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtTreePropertyBrowser.isItemVisible";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtTreePropertyBrowser::isItemVisible(QtBrowserItem*)const->bool
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX], (pyArg)))) {
        overloadId = 0; // isItemVisible(QtBrowserItem*)const
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtTreePropertyBrowserFunc_isItemVisible_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtBrowserItem *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // isItemVisible(QtBrowserItem*)const
            bool cppResult = const_cast<const ::QtTreePropertyBrowserWrapper *>(cppSelf)->isItemVisible(cppArg0);
            pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtTreePropertyBrowserFunc_isItemVisible_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_itemChanged(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtTreePropertyBrowser.itemChanged";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtAbstractPropertyBrowser::itemChanged(QtBrowserItem*)
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX], (pyArg)))) {
        overloadId = 0; // itemChanged(QtBrowserItem*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtTreePropertyBrowserFunc_itemChanged_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtBrowserItem *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // itemChanged(QtBrowserItem*)
            static_cast<::QtTreePropertyBrowserWrapper *>(cppSelf)->QtTreePropertyBrowserWrapper::itemChanged_protected(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtTreePropertyBrowserFunc_itemChanged_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_itemInserted(PyObject *self, PyObject *args)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtTreePropertyBrowser.itemInserted";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp[2];
    SBK_UNUSED(pythonToCpp)
    const Py_ssize_t numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {nullptr, nullptr};

    // invalid argument lengths

    if (!PyArg_UnpackTuple(args, "itemInserted", 2, 2, &(pyArgs[0]), &(pyArgs[1])))
        return {};


    // Overloaded function decisor
    // 0: QtAbstractPropertyBrowser::itemInserted(QtBrowserItem*,QtBrowserItem*)
    if (numArgs == 2
        && (pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX], (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX], (pyArgs[1])))) {
        overloadId = 0; // itemInserted(QtBrowserItem*,QtBrowserItem*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtTreePropertyBrowserFunc_itemInserted_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return {};
        ::QtBrowserItem *cppArg0;
        pythonToCpp[0](pyArgs[0], &cppArg0);
        if (!Shiboken::Object::isValid(pyArgs[1]))
            return {};
        ::QtBrowserItem *cppArg1;
        pythonToCpp[1](pyArgs[1], &cppArg1);

        if (!PyErr_Occurred()) {
            // itemInserted(QtBrowserItem*,QtBrowserItem*)
            static_cast<::QtTreePropertyBrowserWrapper *>(cppSelf)->QtTreePropertyBrowserWrapper::itemInserted_protected(cppArg0, cppArg1);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtTreePropertyBrowserFunc_itemInserted_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_itemRemoved(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtTreePropertyBrowser.itemRemoved";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtAbstractPropertyBrowser::itemRemoved(QtBrowserItem*)
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX], (pyArg)))) {
        overloadId = 0; // itemRemoved(QtBrowserItem*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtTreePropertyBrowserFunc_itemRemoved_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtBrowserItem *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // itemRemoved(QtBrowserItem*)
            static_cast<::QtTreePropertyBrowserWrapper *>(cppSelf)->QtTreePropertyBrowserWrapper::itemRemoved_protected(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtTreePropertyBrowserFunc_itemRemoved_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_propertiesWithoutValueMarked(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // propertiesWithoutValueMarked()const
            bool cppResult = const_cast<const ::QtTreePropertyBrowserWrapper *>(cppSelf)->propertiesWithoutValueMarked();
            pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_resizeMode(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // resizeMode()const
            QtTreePropertyBrowser::ResizeMode cppResult = QtTreePropertyBrowser::ResizeMode(const_cast<const ::QtTreePropertyBrowserWrapper *>(cppSelf)->resizeMode());
            pyResult = Shiboken::Conversions::copyToPython(PepType_SETP(reinterpret_cast<SbkEnumType *>(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_RESIZEMODE_IDX]))->converter, &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_resizeSection(PyObject *self, PyObject *args)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtTreePropertyBrowser.resizeSection";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp[2];
    SBK_UNUSED(pythonToCpp)
    const Py_ssize_t numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {nullptr, nullptr};

    // invalid argument lengths

    if (!PyArg_UnpackTuple(args, "resizeSection", 2, 2, &(pyArgs[0]), &(pyArgs[1])))
        return {};


    // Overloaded function decisor
    // 0: QtTreePropertyBrowser::resizeSection(int,int)
    if (numArgs == 2
        && (pythonToCpp[0] = Shiboken::Conversions::pythonToCppConversion(Shiboken::Conversions::PrimitiveTypeConverter<int>(), (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::pythonToCppConversion(Shiboken::Conversions::PrimitiveTypeConverter<int>(), (pyArgs[1])))) {
        overloadId = 0; // resizeSection(int,int)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtTreePropertyBrowserFunc_resizeSection_TypeError;

    // Call function/method
    {
        int cppArg0;
        pythonToCpp[0](pyArgs[0], &cppArg0);
        int cppArg1;
        pythonToCpp[1](pyArgs[1], &cppArg1);

        if (!PyErr_Occurred()) {
            // resizeSection(int,int)
            cppSelf->resizeSection(cppArg0, cppArg1);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtTreePropertyBrowserFunc_resizeSection_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_rootIsDecorated(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // rootIsDecorated()const
            bool cppResult = const_cast<const ::QtTreePropertyBrowserWrapper *>(cppSelf)->rootIsDecorated();
            pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_sectionSize(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtTreePropertyBrowser.sectionSize";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtTreePropertyBrowser::sectionSize(int)const->int
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppConversion(Shiboken::Conversions::PrimitiveTypeConverter<int>(), (pyArg)))) {
        overloadId = 0; // sectionSize(int)const
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtTreePropertyBrowserFunc_sectionSize_TypeError;

    // Call function/method
    {
        int cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // sectionSize(int)const
            int cppResult = const_cast<const ::QtTreePropertyBrowserWrapper *>(cppSelf)->sectionSize(cppArg0);
            pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<int>(), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtTreePropertyBrowserFunc_sectionSize_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_setAlternatingRowColors(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtTreePropertyBrowser.setAlternatingRowColors";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtTreePropertyBrowser::setAlternatingRowColors(bool)
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppConversion(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), (pyArg)))) {
        overloadId = 0; // setAlternatingRowColors(bool)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtTreePropertyBrowserFunc_setAlternatingRowColors_TypeError;

    // Call function/method
    {
        bool cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // setAlternatingRowColors(bool)
            cppSelf->setAlternatingRowColors(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtTreePropertyBrowserFunc_setAlternatingRowColors_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_setAttributes(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtTreePropertyBrowser.setAttributes";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtTreePropertyBrowser::setAttributes(BrowserCol)
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppConversion(PepType_SETP(reinterpret_cast<SbkEnumType *>(SbkqtpropertybrowserTypes[SBK_BROWSERCOL_IDX]))->converter, (pyArg)))) {
        overloadId = 0; // setAttributes(BrowserCol)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtTreePropertyBrowserFunc_setAttributes_TypeError;

    // Call function/method
    {
        ::BrowserCol cppArg0{NONE};
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // setAttributes(BrowserCol)
            cppSelf->setAttributes(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtTreePropertyBrowserFunc_setAttributes_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_setBackgroundColor(PyObject *self, PyObject *args)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtTreePropertyBrowser.setBackgroundColor";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp[2];
    SBK_UNUSED(pythonToCpp)
    const Py_ssize_t numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {nullptr, nullptr};

    // invalid argument lengths

    if (!PyArg_UnpackTuple(args, "setBackgroundColor", 2, 2, &(pyArgs[0]), &(pyArgs[1])))
        return {};


    // Overloaded function decisor
    // 0: QtTreePropertyBrowser::setBackgroundColor(QtBrowserItem*,QColor)
    if (numArgs == 2
        && (pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX], (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::pythonToCppReferenceConversion(SbkPySide6_QtGuiTypes[SBK_QCOLOR_IDX], (pyArgs[1])))) {
        overloadId = 0; // setBackgroundColor(QtBrowserItem*,QColor)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtTreePropertyBrowserFunc_setBackgroundColor_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return {};
        ::QtBrowserItem *cppArg0;
        pythonToCpp[0](pyArgs[0], &cppArg0);
        if (!Shiboken::Object::isValid(pyArgs[1]))
            return {};
        ::QColor cppArg1_local;
        ::QColor *cppArg1 = &cppArg1_local;
        if (pythonToCpp[1].isValue())
            pythonToCpp[1](pyArgs[1], &cppArg1_local);
        else
            pythonToCpp[1](pyArgs[1], &cppArg1);


        if (!PyErr_Occurred()) {
            // setBackgroundColor(QtBrowserItem*,QColor)
            cppSelf->setBackgroundColor(cppArg0, *cppArg1);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtTreePropertyBrowserFunc_setBackgroundColor_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_setExpanded(PyObject *self, PyObject *args)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtTreePropertyBrowser.setExpanded";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp[2];
    SBK_UNUSED(pythonToCpp)
    const Py_ssize_t numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {nullptr, nullptr};

    // invalid argument lengths

    if (!PyArg_UnpackTuple(args, "setExpanded", 2, 2, &(pyArgs[0]), &(pyArgs[1])))
        return {};


    // Overloaded function decisor
    // 0: QtTreePropertyBrowser::setExpanded(QtBrowserItem*,bool)
    if (numArgs == 2
        && (pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX], (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::pythonToCppConversion(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), (pyArgs[1])))) {
        overloadId = 0; // setExpanded(QtBrowserItem*,bool)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtTreePropertyBrowserFunc_setExpanded_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return {};
        ::QtBrowserItem *cppArg0;
        pythonToCpp[0](pyArgs[0], &cppArg0);
        bool cppArg1;
        pythonToCpp[1](pyArgs[1], &cppArg1);

        if (!PyErr_Occurred()) {
            // setExpanded(QtBrowserItem*,bool)
            cppSelf->setExpanded(cppArg0, cppArg1);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtTreePropertyBrowserFunc_setExpanded_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_setHeaderLabels(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtTreePropertyBrowser.setHeaderLabels";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtTreePropertyBrowser::setHeaderLabels(QStringList&)
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppConversion(SbkPySide6_QtCoreTypeConverters[SBK_QSTRINGLIST_IDX], (pyArg)))) {
        overloadId = 0; // setHeaderLabels(QStringList&)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtTreePropertyBrowserFunc_setHeaderLabels_TypeError;

    // Call function/method
    {
        ::QStringList cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // setHeaderLabels(QStringList&)
            cppSelf->setHeaderLabels(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtTreePropertyBrowserFunc_setHeaderLabels_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_setHeaderVisible(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtTreePropertyBrowser.setHeaderVisible";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtTreePropertyBrowser::setHeaderVisible(bool)
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppConversion(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), (pyArg)))) {
        overloadId = 0; // setHeaderVisible(bool)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtTreePropertyBrowserFunc_setHeaderVisible_TypeError;

    // Call function/method
    {
        bool cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // setHeaderVisible(bool)
            cppSelf->setHeaderVisible(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtTreePropertyBrowserFunc_setHeaderVisible_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_setIndentation(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtTreePropertyBrowser.setIndentation";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtTreePropertyBrowser::setIndentation(int)
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppConversion(Shiboken::Conversions::PrimitiveTypeConverter<int>(), (pyArg)))) {
        overloadId = 0; // setIndentation(int)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtTreePropertyBrowserFunc_setIndentation_TypeError;

    // Call function/method
    {
        int cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // setIndentation(int)
            cppSelf->setIndentation(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtTreePropertyBrowserFunc_setIndentation_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_setItemVisible(PyObject *self, PyObject *args)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtTreePropertyBrowser.setItemVisible";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp[2];
    SBK_UNUSED(pythonToCpp)
    const Py_ssize_t numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {nullptr, nullptr};

    // invalid argument lengths

    if (!PyArg_UnpackTuple(args, "setItemVisible", 2, 2, &(pyArgs[0]), &(pyArgs[1])))
        return {};


    // Overloaded function decisor
    // 0: QtTreePropertyBrowser::setItemVisible(QtBrowserItem*,bool)
    if (numArgs == 2
        && (pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX], (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::pythonToCppConversion(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), (pyArgs[1])))) {
        overloadId = 0; // setItemVisible(QtBrowserItem*,bool)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtTreePropertyBrowserFunc_setItemVisible_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return {};
        ::QtBrowserItem *cppArg0;
        pythonToCpp[0](pyArgs[0], &cppArg0);
        bool cppArg1;
        pythonToCpp[1](pyArgs[1], &cppArg1);

        if (!PyErr_Occurred()) {
            // setItemVisible(QtBrowserItem*,bool)
            cppSelf->setItemVisible(cppArg0, cppArg1);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtTreePropertyBrowserFunc_setItemVisible_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_setPropertiesWithoutValueMarked(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtTreePropertyBrowser.setPropertiesWithoutValueMarked";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtTreePropertyBrowser::setPropertiesWithoutValueMarked(bool)
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppConversion(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), (pyArg)))) {
        overloadId = 0; // setPropertiesWithoutValueMarked(bool)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtTreePropertyBrowserFunc_setPropertiesWithoutValueMarked_TypeError;

    // Call function/method
    {
        bool cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // setPropertiesWithoutValueMarked(bool)
            cppSelf->setPropertiesWithoutValueMarked(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtTreePropertyBrowserFunc_setPropertiesWithoutValueMarked_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_setResizeMode(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtTreePropertyBrowser.setResizeMode";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtTreePropertyBrowser::setResizeMode(QtTreePropertyBrowser::ResizeMode)
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppConversion(PepType_SETP(reinterpret_cast<SbkEnumType *>(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_RESIZEMODE_IDX]))->converter, (pyArg)))) {
        overloadId = 0; // setResizeMode(QtTreePropertyBrowser::ResizeMode)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtTreePropertyBrowserFunc_setResizeMode_TypeError;

    // Call function/method
    {
        ::QtTreePropertyBrowser::ResizeMode cppArg0{QtTreePropertyBrowser::Interactive};
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // setResizeMode(QtTreePropertyBrowser::ResizeMode)
            cppSelf->setResizeMode(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtTreePropertyBrowserFunc_setResizeMode_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_setRootIsDecorated(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtTreePropertyBrowser.setRootIsDecorated";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtTreePropertyBrowser::setRootIsDecorated(bool)
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppConversion(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), (pyArg)))) {
        overloadId = 0; // setRootIsDecorated(bool)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtTreePropertyBrowserFunc_setRootIsDecorated_TypeError;

    // Call function/method
    {
        bool cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // setRootIsDecorated(bool)
            cppSelf->setRootIsDecorated(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtTreePropertyBrowserFunc_setRootIsDecorated_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_setSplitterPosition(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtTreePropertyBrowser.setSplitterPosition";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtTreePropertyBrowser::setSplitterPosition(int)
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppConversion(Shiboken::Conversions::PrimitiveTypeConverter<int>(), (pyArg)))) {
        overloadId = 0; // setSplitterPosition(int)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtTreePropertyBrowserFunc_setSplitterPosition_TypeError;

    // Call function/method
    {
        int cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // setSplitterPosition(int)
            cppSelf->setSplitterPosition(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtTreePropertyBrowserFunc_setSplitterPosition_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_splitterPosition(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // splitterPosition()const
            int cppResult = const_cast<const ::QtTreePropertyBrowserWrapper *>(cppSelf)->splitterPosition();
            pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<int>(), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}


static const char *Sbk_QtTreePropertyBrowser_PropertyStrings[] = {
    "alternatingRowColors::",
    "attributes::",
    "headerVisible:isHeaderVisible:",
    "indentation::",
    "propertiesWithoutValueMarked::",
    "resizeMode::",
    "rootIsDecorated::",
    "splitterPosition::",
    nullptr // Sentinel
};

static const char *Sbk_QtTreePropertyBrowser_EnumFlagInfo[] = {
    "ResizeMode:IntEnum",
    nullptr // Sentinel
};

static PyMethodDef Sbk_QtTreePropertyBrowser_methods[] = {
    {"alternatingRowColors", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_alternatingRowColors), METH_NOARGS, nullptr},
    {"attributes", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_attributes), METH_NOARGS, nullptr},
    {"backgroundColor", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_backgroundColor), METH_O, nullptr},
    {"calculatedBackgroundColor", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_calculatedBackgroundColor), METH_O, nullptr},
    {"editItem", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_editItem), METH_O, nullptr},
    {"indentation", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_indentation), METH_NOARGS, nullptr},
    {"isExpanded", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_isExpanded), METH_O, nullptr},
    {"isHeaderVisible", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_isHeaderVisible), METH_NOARGS, nullptr},
    {"isItemVisible", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_isItemVisible), METH_O, nullptr},
    {"itemChanged", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_itemChanged), METH_O, nullptr},
    {"itemInserted", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_itemInserted), METH_VARARGS, nullptr},
    {"itemRemoved", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_itemRemoved), METH_O, nullptr},
    {"propertiesWithoutValueMarked", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_propertiesWithoutValueMarked), METH_NOARGS, nullptr},
    {"resizeMode", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_resizeMode), METH_NOARGS, nullptr},
    {"resizeSection", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_resizeSection), METH_VARARGS, nullptr},
    {"rootIsDecorated", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_rootIsDecorated), METH_NOARGS, nullptr},
    {"sectionSize", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_sectionSize), METH_O, nullptr},
    {"setAlternatingRowColors", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_setAlternatingRowColors), METH_O, nullptr},
    {"setAttributes", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_setAttributes), METH_O, nullptr},
    {"setBackgroundColor", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_setBackgroundColor), METH_VARARGS, nullptr},
    {"setExpanded", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_setExpanded), METH_VARARGS, nullptr},
    {"setHeaderLabels", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_setHeaderLabels), METH_O, nullptr},
    {"setHeaderVisible", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_setHeaderVisible), METH_O, nullptr},
    {"setIndentation", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_setIndentation), METH_O, nullptr},
    {"setItemVisible", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_setItemVisible), METH_VARARGS, nullptr},
    {"setPropertiesWithoutValueMarked", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_setPropertiesWithoutValueMarked), METH_O, nullptr},
    {"setResizeMode", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_setResizeMode), METH_O, nullptr},
    {"setRootIsDecorated", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_setRootIsDecorated), METH_O, nullptr},
    {"setSplitterPosition", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_setSplitterPosition), METH_O, nullptr},
    {"splitterPosition", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_splitterPosition), METH_NOARGS, nullptr},

    {nullptr, nullptr, 0, nullptr} // Sentinel
};

static int Sbk_QtTreePropertyBrowser_setattro(PyObject *self, PyObject *name, PyObject *value)
{
    PySide::Feature::Select(self);
    if (value && PyCallable_Check(value)) {
        auto plain_inst = reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self)));
        auto inst = dynamic_cast<QtTreePropertyBrowserWrapper *>(plain_inst);
        if (inst)
            inst->resetPyMethodCache();
    }
    Shiboken::AutoDecRef pp(reinterpret_cast<PyObject *>(PySide::Property::getObject(self, name)));
    if (!pp.isNull())
        return PySide::Property::setValue(reinterpret_cast<PySideProperty *>(pp.object()), self, value);
    return PyObject_GenericSetAttr(self, name, value);
}

} // extern "C"

static int Sbk_QtTreePropertyBrowser_traverse(PyObject *self, visitproc visit, void *arg)
{
    return SbkObject_TypeF()->tp_traverse(self, visit, arg);
}
static int Sbk_QtTreePropertyBrowser_clear(PyObject *self)
{
    return reinterpret_cast<PyTypeObject *>(SbkObject_TypeF())->tp_clear(self);
}
static void * Sbk_QtTreePropertyBrowserSpecialCastFunction(void *obj, PyTypeObject *desiredType)
{
    auto me = reinterpret_cast< ::QtTreePropertyBrowser *>(obj);
    if (desiredType == SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYBROWSER_IDX])
        return static_cast< ::QtAbstractPropertyBrowser *>(me);
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
static PyTypeObject *_Sbk_QtTreePropertyBrowser_Type = nullptr;
static PyTypeObject *Sbk_QtTreePropertyBrowser_TypeF(void)
{
    return _Sbk_QtTreePropertyBrowser_Type;
}

static PyType_Slot Sbk_QtTreePropertyBrowser_slots[] = {
    {Py_tp_base,        nullptr}, // inserted by introduceWrapperType
    {Py_tp_dealloc,     reinterpret_cast<void *>(&SbkDeallocWrapper)},
    {Py_tp_repr,        nullptr},
    {Py_tp_hash,        nullptr},
    {Py_tp_call,        nullptr},
    {Py_tp_str,         nullptr},
    {Py_tp_getattro,    nullptr},
    {Py_tp_setattro,    reinterpret_cast<void *>(Sbk_QtTreePropertyBrowser_setattro)},
    {Py_tp_traverse,    reinterpret_cast<void *>(Sbk_QtTreePropertyBrowser_traverse)},
    {Py_tp_clear,       reinterpret_cast<void *>(Sbk_QtTreePropertyBrowser_clear)},
    {Py_tp_richcompare, nullptr},
    {Py_tp_iter,        nullptr},
    {Py_tp_iternext,    nullptr},
    {Py_tp_methods,     reinterpret_cast<void *>(Sbk_QtTreePropertyBrowser_methods)},
    {Py_tp_getset,      nullptr},
    {Py_tp_init,        reinterpret_cast<void *>(Sbk_QtTreePropertyBrowser_Init)},
    {Py_tp_new,         reinterpret_cast<void *>(SbkObject_tp_new)},
    {0, nullptr}
};
static PyType_Spec Sbk_QtTreePropertyBrowser_spec = {
    "1:qtpropertybrowser.QtTreePropertyBrowser",
    sizeof(SbkObject),
    0,
    Py_TPFLAGS_DEFAULT|Py_TPFLAGS_BASETYPE|Py_TPFLAGS_HAVE_GC,
    Sbk_QtTreePropertyBrowser_slots
};

} //extern "C"

static void *Sbk_QtTreePropertyBrowser_typeDiscovery(void *cptr, PyTypeObject *instanceType)
{
    SBK_UNUSED(cptr)
    SBK_UNUSED(instanceType)
    if (instanceType == Shiboken::SbkType< ::QObject >())
        return dynamic_cast< ::QtTreePropertyBrowser *>(reinterpret_cast< ::QObject *>(cptr));
    if (instanceType == Shiboken::SbkType< ::QPaintDevice >())
        return dynamic_cast< ::QtTreePropertyBrowser *>(reinterpret_cast< ::QPaintDevice *>(cptr));
    return {};
}


// Type conversion functions.

// Python to C++ enum conversion.
static void QtTreePropertyBrowser_ResizeMode_PythonToCpp_QtTreePropertyBrowser_ResizeMode(PyObject *pyIn, void *cppOut)
{
    const auto value = static_cast<::QtTreePropertyBrowser::ResizeMode>(Shiboken::Enum::getValue(pyIn));
    *reinterpret_cast<::QtTreePropertyBrowser::ResizeMode *>(cppOut) = value;

}
static PythonToCppFunc is_QtTreePropertyBrowser_ResizeMode_PythonToCpp_QtTreePropertyBrowser_ResizeMode_Convertible(PyObject *pyIn)
{
    if (PyObject_TypeCheck(pyIn, SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_RESIZEMODE_IDX]))
        return QtTreePropertyBrowser_ResizeMode_PythonToCpp_QtTreePropertyBrowser_ResizeMode;
    return {};
}
static PyObject *QtTreePropertyBrowser_ResizeMode_CppToPython_QtTreePropertyBrowser_ResizeMode(const void *cppIn)
{
    const int castCppIn = int(*reinterpret_cast<const ::QtTreePropertyBrowser::ResizeMode *>(cppIn));
    return Shiboken::Enum::newItem(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_RESIZEMODE_IDX], castCppIn);

}

// Python to C++ pointer conversion - returns the C++ object of the Python wrapper (keeps object identity).
static void QtTreePropertyBrowser_PythonToCpp_QtTreePropertyBrowser_PTR(PyObject *pyIn, void *cppOut)
{
    Shiboken::Conversions::pythonToCppPointer(Sbk_QtTreePropertyBrowser_TypeF(), pyIn, cppOut);
}
static PythonToCppFunc is_QtTreePropertyBrowser_PythonToCpp_QtTreePropertyBrowser_PTR_Convertible(PyObject *pyIn)
{
    if (pyIn == Py_None)
        return Shiboken::Conversions::nonePythonToCppNullPtr;
    if (PyObject_TypeCheck(pyIn, Sbk_QtTreePropertyBrowser_TypeF()))
        return QtTreePropertyBrowser_PythonToCpp_QtTreePropertyBrowser_PTR;
    return {};
}

// C++ to Python pointer conversion - tries to find the Python wrapper for the C++ object (keeps object identity).
static PyObject *QtTreePropertyBrowser_PTR_CppToPython_QtTreePropertyBrowser(const void *cppIn)
{
    return PySide::getWrapperForQObject(reinterpret_cast<::QtTreePropertyBrowser *>(const_cast<void *>(cppIn)), Sbk_QtTreePropertyBrowser_TypeF());

}

// The signatures string for the functions.
// Multiple signatures have their index "n:" in front.
static const char *QtTreePropertyBrowser_SignatureStrings[] = {
    "qtpropertybrowser.QtTreePropertyBrowser(self,parent:PySide6.QtWidgets.QWidget=0)",
    "qtpropertybrowser.QtTreePropertyBrowser.alternatingRowColors(self)->bool",
    "qtpropertybrowser.QtTreePropertyBrowser.attributes(self)->qtpropertybrowser.BrowserCol",
    "qtpropertybrowser.QtTreePropertyBrowser.backgroundColor(self,item:qtpropertybrowser.QtBrowserItem)->PySide6.QtGui.QColor",
    "qtpropertybrowser.QtTreePropertyBrowser.calculatedBackgroundColor(self,item:qtpropertybrowser.QtBrowserItem)->PySide6.QtGui.QColor",
    "qtpropertybrowser.QtTreePropertyBrowser.editItem(self,item:qtpropertybrowser.QtBrowserItem)",
    "qtpropertybrowser.QtTreePropertyBrowser.indentation(self)->int",
    "qtpropertybrowser.QtTreePropertyBrowser.isExpanded(self,item:qtpropertybrowser.QtBrowserItem)->bool",
    "qtpropertybrowser.QtTreePropertyBrowser.isHeaderVisible(self)->bool",
    "qtpropertybrowser.QtTreePropertyBrowser.isItemVisible(self,item:qtpropertybrowser.QtBrowserItem)->bool",
    "qtpropertybrowser.QtTreePropertyBrowser.itemChanged(self,item:qtpropertybrowser.QtBrowserItem)",
    "qtpropertybrowser.QtTreePropertyBrowser.itemInserted(self,item:qtpropertybrowser.QtBrowserItem,afterItem:qtpropertybrowser.QtBrowserItem)",
    "qtpropertybrowser.QtTreePropertyBrowser.itemRemoved(self,item:qtpropertybrowser.QtBrowserItem)",
    "qtpropertybrowser.QtTreePropertyBrowser.propertiesWithoutValueMarked(self)->bool",
    "qtpropertybrowser.QtTreePropertyBrowser.resizeMode(self)->qtpropertybrowser.QtTreePropertyBrowser.ResizeMode",
    "qtpropertybrowser.QtTreePropertyBrowser.resizeSection(self,logicalIndex:int,size:int)",
    "qtpropertybrowser.QtTreePropertyBrowser.rootIsDecorated(self)->bool",
    "qtpropertybrowser.QtTreePropertyBrowser.sectionSize(self,logicalIndex:int)->int",
    "qtpropertybrowser.QtTreePropertyBrowser.setAlternatingRowColors(self,enable:bool)",
    "qtpropertybrowser.QtTreePropertyBrowser.setAttributes(self,attributes:qtpropertybrowser.BrowserCol)",
    "qtpropertybrowser.QtTreePropertyBrowser.setBackgroundColor(self,item:qtpropertybrowser.QtBrowserItem,color:typing.Union[PySide6.QtGui.QColor, PySide6.QtGui.QRgba64, QVariant, PySide6.QtCore.Qt.GlobalColor, QString, unsigned int])",
    "qtpropertybrowser.QtTreePropertyBrowser.setExpanded(self,item:qtpropertybrowser.QtBrowserItem,expanded:bool)",
    "qtpropertybrowser.QtTreePropertyBrowser.setHeaderLabels(self,labels:QStringList)",
    "qtpropertybrowser.QtTreePropertyBrowser.setHeaderVisible(self,visible:bool)",
    "qtpropertybrowser.QtTreePropertyBrowser.setIndentation(self,i:int)",
    "qtpropertybrowser.QtTreePropertyBrowser.setItemVisible(self,item:qtpropertybrowser.QtBrowserItem,visible:bool)",
    "qtpropertybrowser.QtTreePropertyBrowser.setPropertiesWithoutValueMarked(self,mark:bool)",
    "qtpropertybrowser.QtTreePropertyBrowser.setResizeMode(self,mode:qtpropertybrowser.QtTreePropertyBrowser.ResizeMode)",
    "qtpropertybrowser.QtTreePropertyBrowser.setRootIsDecorated(self,show:bool)",
    "qtpropertybrowser.QtTreePropertyBrowser.setSplitterPosition(self,position:int)",
    "qtpropertybrowser.QtTreePropertyBrowser.splitterPosition(self)->int",
    nullptr}; // Sentinel

void init_QtTreePropertyBrowser(PyObject *module)
{
    _Sbk_QtTreePropertyBrowser_Type = Shiboken::ObjectType::introduceWrapperType(
        module,
        "QtTreePropertyBrowser",
        "QtTreePropertyBrowser*",
        &Sbk_QtTreePropertyBrowser_spec,
        &Shiboken::callCppDestructor< ::QtTreePropertyBrowser >,
        SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYBROWSER_IDX],
        0,
        Shiboken::ObjectType::WrapperFlags::DeleteInMainThread);
    auto *pyType = Sbk_QtTreePropertyBrowser_TypeF(); // references _Sbk_QtTreePropertyBrowser_Type
    InitSignatureStrings(pyType, QtTreePropertyBrowser_SignatureStrings);
    SbkObjectType_SetPropertyStrings(pyType, Sbk_QtTreePropertyBrowser_PropertyStrings);
    SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX] = pyType;

    // Register Converter
    SbkConverter *converter = Shiboken::Conversions::createConverter(pyType,
        QtTreePropertyBrowser_PythonToCpp_QtTreePropertyBrowser_PTR,
        is_QtTreePropertyBrowser_PythonToCpp_QtTreePropertyBrowser_PTR_Convertible,
        QtTreePropertyBrowser_PTR_CppToPython_QtTreePropertyBrowser);

    Shiboken::Conversions::registerConverterName(converter, "QtTreePropertyBrowser");
    Shiboken::Conversions::registerConverterName(converter, "QtTreePropertyBrowser*");
    Shiboken::Conversions::registerConverterName(converter, "QtTreePropertyBrowser&");
    Shiboken::Conversions::registerConverterName(converter, typeid(::QtTreePropertyBrowser).name());
    Shiboken::Conversions::registerConverterName(converter, typeid(::QtTreePropertyBrowserWrapper).name());


    MultipleInheritanceInitFunction func = Shiboken::ObjectType::getMultipleInheritanceFunction(SbkPySide6_QtWidgetsTypes[SBK_QWIDGET_IDX]);
    Shiboken::ObjectType::setMultipleInheritanceFunction(Sbk_QtTreePropertyBrowser_TypeF(), func);
    Shiboken::ObjectType::setCastFunction(Sbk_QtTreePropertyBrowser_TypeF(), &Sbk_QtTreePropertyBrowserSpecialCastFunction);
    Shiboken::ObjectType::setTypeDiscoveryFunctionV2(Sbk_QtTreePropertyBrowser_TypeF(), &Sbk_QtTreePropertyBrowser_typeDiscovery);

    // Pass the ..._EnumFlagInfo to the class.
    SbkObjectType_SetEnumFlagInfo(pyType, Sbk_QtTreePropertyBrowser_EnumFlagInfo);

    // Initialization of enums.
    PyTypeObject *EType{};

    // Initialization of enum 'ResizeMode'.
    EType = Shiboken::Enum::createScopedEnum(Sbk_QtTreePropertyBrowser_TypeF(),
        "ResizeMode",
        "1:qtpropertybrowser.QtTreePropertyBrowser.ResizeMode",
        "QtTreePropertyBrowser::ResizeMode");
    if (!EType)
        return;

    if (!Shiboken::Enum::createScopedEnumItem(EType,
        Sbk_QtTreePropertyBrowser_TypeF(), "Interactive", Shiboken::Enum::EnumValueType(QtTreePropertyBrowser::ResizeMode::Interactive)))
        return;
    if (!Shiboken::Enum::createScopedEnumItem(EType,
        Sbk_QtTreePropertyBrowser_TypeF(), "Stretch", Shiboken::Enum::EnumValueType(QtTreePropertyBrowser::ResizeMode::Stretch)))
        return;
    if (!Shiboken::Enum::createScopedEnumItem(EType,
        Sbk_QtTreePropertyBrowser_TypeF(), "Fixed", Shiboken::Enum::EnumValueType(QtTreePropertyBrowser::ResizeMode::Fixed)))
        return;
    if (!Shiboken::Enum::createScopedEnumItem(EType,
        Sbk_QtTreePropertyBrowser_TypeF(), "ResizeToContents", Shiboken::Enum::EnumValueType(QtTreePropertyBrowser::ResizeMode::ResizeToContents)))
        return;
    // PYSIDE-1735: Resolving the whole enum class at the end for API compatibility.
    EType = morphLastEnumToPython();
    SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_RESIZEMODE_IDX] = EType;
    // Register converter for enum 'QtTreePropertyBrowser::ResizeMode'.
    {
        SbkConverter *converter = Shiboken::Conversions::createConverter(EType,
            QtTreePropertyBrowser_ResizeMode_CppToPython_QtTreePropertyBrowser_ResizeMode);
        Shiboken::Conversions::addPythonToCppValueConversion(converter,
            QtTreePropertyBrowser_ResizeMode_PythonToCpp_QtTreePropertyBrowser_ResizeMode,
            is_QtTreePropertyBrowser_ResizeMode_PythonToCpp_QtTreePropertyBrowser_ResizeMode_Convertible);
        Shiboken::Enum::setTypeConverter(EType, converter, false);
        Shiboken::Conversions::registerConverterName(converter, "QtTreePropertyBrowser::ResizeMode");
        Shiboken::Conversions::registerConverterName(converter, "ResizeMode");
    }
    // End of 'ResizeMode' enum.

    PySide::Signal::registerSignals(pyType, &::QtTreePropertyBrowser::staticMetaObject);
    QtTreePropertyBrowserWrapper::pysideInitQtMetaTypes();
    Shiboken::ObjectType::setSubTypeInitHook(pyType, &PySide::initQObjectSubType);
    PySide::initDynamicMetaObject(pyType, &::QtTreePropertyBrowser::staticMetaObject, sizeof(QtTreePropertyBrowserWrapper));
}
