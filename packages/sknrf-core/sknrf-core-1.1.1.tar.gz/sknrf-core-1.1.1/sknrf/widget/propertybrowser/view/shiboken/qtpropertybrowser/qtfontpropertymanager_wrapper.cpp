
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
#include "qtfontpropertymanager_wrapper.h"

#include <cctype>
#include <cstring>
#include <iterator>
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

void QtFontPropertyManagerWrapper::pysideInitQtMetaTypes()
{
}

void QtFontPropertyManagerWrapper::resetPyMethodCache()
{
    std::fill_n(m_PyMethodCache, sizeof(m_PyMethodCache) / sizeof(m_PyMethodCache[0]), false);
}

QtFontPropertyManagerWrapper::QtFontPropertyManagerWrapper(QObject * parent) : QtFontPropertyManager(parent)
{
    resetPyMethodCache();
    // ... middle
}

bool QtFontPropertyManagerWrapper::check(const QtProperty * property) const
{
    if (m_PyMethodCache[0])
        return this->::QtFontPropertyManager::check(property);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return false;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "check";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[0] = true;
        gil.release();
        return this->::QtFontPropertyManager::check(property);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], property)
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
        Shiboken::Warnings::warnInvalidReturnValue("QtFontPropertyManager", "check", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QIcon QtFontPropertyManagerWrapper::checkIcon(const QtProperty * property) const
{
    if (m_PyMethodCache[1])
        return this->::QtAbstractPropertyManager::checkIcon(property);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return {};
    static PyObject *nameCache[2] = {};
    static const char *funcName = "checkIcon";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[1] = true;
        gil.release();
        return this->::QtAbstractPropertyManager::checkIcon(property);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], property)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return {};
    }
    // Check return type
    Shiboken::Conversions::PythonToCppConversion pythonToCpp =
        Shiboken::Conversions::pythonToCppValueConversion(SbkPySide6_QtGuiTypes[SBK_QICON_IDX], pyResult);
    if (!pythonToCpp) {
        Shiboken::Warnings::warnInvalidReturnValue("QtFontPropertyManager", "checkIcon", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QIcon >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return {};
    }
    ::QIcon cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtFontPropertyManagerWrapper::childEvent(QChildEvent * event)
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

void QtFontPropertyManagerWrapper::connectNotify(const QMetaMethod & signal)
{
    if (m_PyMethodCache[3]) {
        return this->::QObject::connectNotify(signal);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "connectNotify";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[3] = true;
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

QtProperty * QtFontPropertyManagerWrapper::createProperty()
{
    if (m_PyMethodCache[4])
        return this->::QtAbstractPropertyManager::createProperty();
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return nullptr;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "createProperty";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[4] = true;
        gil.release();
        return this->::QtAbstractPropertyManager::createProperty();
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
        Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], pyResult);
    if (!pythonToCpp) {
        Shiboken::Warnings::warnInvalidReturnValue("QtFontPropertyManager", "createProperty", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QtProperty >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return nullptr;
    }
    ::QtProperty *cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtFontPropertyManagerWrapper::customEvent(QEvent * event)
{
    if (m_PyMethodCache[5]) {
        return this->::QObject::customEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "customEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[5] = true;
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

void QtFontPropertyManagerWrapper::disconnectNotify(const QMetaMethod & signal)
{
    if (m_PyMethodCache[6]) {
        return this->::QObject::disconnectNotify(signal);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "disconnectNotify";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[6] = true;
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

QString QtFontPropertyManagerWrapper::displayText(const QtProperty * property) const
{
    if (m_PyMethodCache[7])
        return this->::QtAbstractPropertyManager::displayText(property);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return ::QString();
    static PyObject *nameCache[2] = {};
    static const char *funcName = "displayText";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[7] = true;
        gil.release();
        return this->::QtAbstractPropertyManager::displayText(property);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], property)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return ::QString();
    }
    // Check return type
    Shiboken::Conversions::PythonToCppConversion pythonToCpp =
        Shiboken::Conversions::pythonToCppConversion(SbkPySide6_QtCoreTypeConverters[SBK_QSTRING_IDX], pyResult);
    if (!pythonToCpp) {
        Shiboken::Warnings::warnInvalidReturnValue("QtFontPropertyManager", "displayText", "QString", Py_TYPE(pyResult)->tp_name);
        return ::QString();
    }
    ::QString cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

bool QtFontPropertyManagerWrapper::event(QEvent * event)
{
    if (m_PyMethodCache[8])
        return this->::QObject::event(event);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return false;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "event";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[8] = true;
        gil.release();
        return this->::QObject::event(event);
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
        Shiboken::Warnings::warnInvalidReturnValue("QtFontPropertyManager", "event", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

bool QtFontPropertyManagerWrapper::eventFilter(QObject * watched, QEvent * event)
{
    if (m_PyMethodCache[9])
        return this->::QObject::eventFilter(watched, event);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return false;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "eventFilter";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[9] = true;
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
        Shiboken::Warnings::warnInvalidReturnValue("QtFontPropertyManager", "eventFilter", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QBrush QtFontPropertyManagerWrapper::foreground(const QtProperty * property) const
{
    if (m_PyMethodCache[10])
        return this->::QtAbstractPropertyManager::foreground(property);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return {};
    static PyObject *nameCache[2] = {};
    static const char *funcName = "foreground";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[10] = true;
        gil.release();
        return this->::QtAbstractPropertyManager::foreground(property);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], property)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return {};
    }
    // Check return type
    Shiboken::Conversions::PythonToCppConversion pythonToCpp =
        Shiboken::Conversions::pythonToCppValueConversion(SbkPySide6_QtGuiTypes[SBK_QBRUSH_IDX], pyResult);
    if (!pythonToCpp) {
        Shiboken::Warnings::warnInvalidReturnValue("QtFontPropertyManager", "foreground", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QBrush >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return {};
    }
    ::QBrush cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QString QtFontPropertyManagerWrapper::formatText(const QtProperty * property) const
{
    if (m_PyMethodCache[11])
        return this->::QtAbstractPropertyManager::formatText(property);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return ::QString();
    static PyObject *nameCache[2] = {};
    static const char *funcName = "formatText";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[11] = true;
        gil.release();
        return this->::QtAbstractPropertyManager::formatText(property);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], property)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return ::QString();
    }
    // Check return type
    Shiboken::Conversions::PythonToCppConversion pythonToCpp =
        Shiboken::Conversions::pythonToCppConversion(SbkPySide6_QtCoreTypeConverters[SBK_QSTRING_IDX], pyResult);
    if (!pythonToCpp) {
        Shiboken::Warnings::warnInvalidReturnValue("QtFontPropertyManager", "formatText", "QString", Py_TYPE(pyResult)->tp_name);
        return ::QString();
    }
    ::QString cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

bool QtFontPropertyManagerWrapper::hasValue(const QtProperty * property) const
{
    if (m_PyMethodCache[12])
        return this->::QtAbstractPropertyManager::hasValue(property);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return false;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "hasValue";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[12] = true;
        gil.release();
        return this->::QtAbstractPropertyManager::hasValue(property);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], property)
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
        Shiboken::Warnings::warnInvalidReturnValue("QtFontPropertyManager", "hasValue", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtFontPropertyManagerWrapper::initializeProperty(QtProperty * property)
{
    if (m_PyMethodCache[13]) {
        return this->::QtFontPropertyManager::initializeProperty(property);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "initializeProperty";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[13] = true;
        gil.release();
        return this->::QtFontPropertyManager::initializeProperty(property);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], property)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

bool QtFontPropertyManagerWrapper::isReadOnly(const QtProperty * arg__1) const
{
    if (m_PyMethodCache[14])
        return this->::QtAbstractPropertyManager::isReadOnly(arg__1);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return false;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "isReadOnly";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[14] = true;
        gil.release();
        return this->::QtAbstractPropertyManager::isReadOnly(arg__1);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], arg__1)
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
        Shiboken::Warnings::warnInvalidReturnValue("QtFontPropertyManager", "isReadOnly", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QString QtFontPropertyManagerWrapper::maximumText(const QtProperty * property) const
{
    if (m_PyMethodCache[15])
        return this->::QtAbstractPropertyManager::maximumText(property);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return ::QString();
    static PyObject *nameCache[2] = {};
    static const char *funcName = "maximumText";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[15] = true;
        gil.release();
        return this->::QtAbstractPropertyManager::maximumText(property);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], property)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return ::QString();
    }
    // Check return type
    Shiboken::Conversions::PythonToCppConversion pythonToCpp =
        Shiboken::Conversions::pythonToCppConversion(SbkPySide6_QtCoreTypeConverters[SBK_QSTRING_IDX], pyResult);
    if (!pythonToCpp) {
        Shiboken::Warnings::warnInvalidReturnValue("QtFontPropertyManager", "maximumText", "QString", Py_TYPE(pyResult)->tp_name);
        return ::QString();
    }
    ::QString cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QString QtFontPropertyManagerWrapper::minimumText(const QtProperty * property) const
{
    if (m_PyMethodCache[16])
        return this->::QtAbstractPropertyManager::minimumText(property);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return ::QString();
    static PyObject *nameCache[2] = {};
    static const char *funcName = "minimumText";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[16] = true;
        gil.release();
        return this->::QtAbstractPropertyManager::minimumText(property);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], property)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return ::QString();
    }
    // Check return type
    Shiboken::Conversions::PythonToCppConversion pythonToCpp =
        Shiboken::Conversions::pythonToCppConversion(SbkPySide6_QtCoreTypeConverters[SBK_QSTRING_IDX], pyResult);
    if (!pythonToCpp) {
        Shiboken::Warnings::warnInvalidReturnValue("QtFontPropertyManager", "minimumText", "QString", Py_TYPE(pyResult)->tp_name);
        return ::QString();
    }
    ::QString cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QString QtFontPropertyManagerWrapper::pkAvgText(const QtProperty * property) const
{
    if (m_PyMethodCache[17])
        return this->::QtAbstractPropertyManager::pkAvgText(property);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return ::QString();
    static PyObject *nameCache[2] = {};
    static const char *funcName = "pkAvgText";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[17] = true;
        gil.release();
        return this->::QtAbstractPropertyManager::pkAvgText(property);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], property)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return ::QString();
    }
    // Check return type
    Shiboken::Conversions::PythonToCppConversion pythonToCpp =
        Shiboken::Conversions::pythonToCppConversion(SbkPySide6_QtCoreTypeConverters[SBK_QSTRING_IDX], pyResult);
    if (!pythonToCpp) {
        Shiboken::Warnings::warnInvalidReturnValue("QtFontPropertyManager", "pkAvgText", "QString", Py_TYPE(pyResult)->tp_name);
        return ::QString();
    }
    ::QString cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtFontPropertyManagerWrapper::setCheck(QtProperty * property, bool check)
{
    if (m_PyMethodCache[18]) {
        return this->::QtFontPropertyManager::setCheck(property, check);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "setCheck";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[18] = true;
        gil.release();
        return this->::QtFontPropertyManager::setCheck(property, check);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(NN)",
        Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], property),
        Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), &check)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

void QtFontPropertyManagerWrapper::timerEvent(QTimerEvent * event)
{
    if (m_PyMethodCache[19]) {
        return this->::QObject::timerEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "timerEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[19] = true;
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

void QtFontPropertyManagerWrapper::uninitializeProperty(QtProperty * property)
{
    if (m_PyMethodCache[20]) {
        return this->::QtFontPropertyManager::uninitializeProperty(property);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "uninitializeProperty";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[20] = true;
        gil.release();
        return this->::QtFontPropertyManager::uninitializeProperty(property);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], property)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

QString QtFontPropertyManagerWrapper::unitText(const QtProperty * property) const
{
    if (m_PyMethodCache[21])
        return this->::QtAbstractPropertyManager::unitText(property);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return ::QString();
    static PyObject *nameCache[2] = {};
    static const char *funcName = "unitText";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[21] = true;
        gil.release();
        return this->::QtAbstractPropertyManager::unitText(property);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], property)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return ::QString();
    }
    // Check return type
    Shiboken::Conversions::PythonToCppConversion pythonToCpp =
        Shiboken::Conversions::pythonToCppConversion(SbkPySide6_QtCoreTypeConverters[SBK_QSTRING_IDX], pyResult);
    if (!pythonToCpp) {
        Shiboken::Warnings::warnInvalidReturnValue("QtFontPropertyManager", "unitText", "QString", Py_TYPE(pyResult)->tp_name);
        return ::QString();
    }
    ::QString cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QIcon QtFontPropertyManagerWrapper::valueIcon(const QtProperty * property) const
{
    if (m_PyMethodCache[22])
        return this->::QtFontPropertyManager::valueIcon(property);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return {};
    static PyObject *nameCache[2] = {};
    static const char *funcName = "valueIcon";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[22] = true;
        gil.release();
        return this->::QtFontPropertyManager::valueIcon(property);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], property)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return {};
    }
    // Check return type
    Shiboken::Conversions::PythonToCppConversion pythonToCpp =
        Shiboken::Conversions::pythonToCppValueConversion(SbkPySide6_QtGuiTypes[SBK_QICON_IDX], pyResult);
    if (!pythonToCpp) {
        Shiboken::Warnings::warnInvalidReturnValue("QtFontPropertyManager", "valueIcon", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QIcon >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return {};
    }
    ::QIcon cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QString QtFontPropertyManagerWrapper::valueText(const QtProperty * property) const
{
    if (m_PyMethodCache[23])
        return this->::QtFontPropertyManager::valueText(property);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return ::QString();
    static PyObject *nameCache[2] = {};
    static const char *funcName = "valueText";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[23] = true;
        gil.release();
        return this->::QtFontPropertyManager::valueText(property);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], property)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return ::QString();
    }
    // Check return type
    Shiboken::Conversions::PythonToCppConversion pythonToCpp =
        Shiboken::Conversions::pythonToCppConversion(SbkPySide6_QtCoreTypeConverters[SBK_QSTRING_IDX], pyResult);
    if (!pythonToCpp) {
        Shiboken::Warnings::warnInvalidReturnValue("QtFontPropertyManager", "valueText", "QString", Py_TYPE(pyResult)->tp_name);
        return ::QString();
    }
    ::QString cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

const QMetaObject *QtFontPropertyManagerWrapper::metaObject() const
{
    if (QObject::d_ptr->metaObject)
        return QObject::d_ptr->dynamicMetaObject();
    SbkObject *pySelf = Shiboken::BindingManager::instance().retrieveWrapper(this);
    if (pySelf == nullptr)
        return QtFontPropertyManager::metaObject();
    return PySide::SignalManager::retrieveMetaObject(reinterpret_cast<PyObject *>(pySelf));
}

int QtFontPropertyManagerWrapper::qt_metacall(QMetaObject::Call call, int id, void **args)
{
    int result = QtFontPropertyManager::qt_metacall(call, id, args);
    return result < 0 ? result : PySide::SignalManager::qt_metacall(this, call, id, args);
}

void *QtFontPropertyManagerWrapper::qt_metacast(const char *_clname)
{
    if (!_clname)
        return {};
    SbkObject *pySelf = Shiboken::BindingManager::instance().retrieveWrapper(this);
    if (pySelf && PySide::inherits(Py_TYPE(pySelf), _clname))
        return static_cast<void *>(const_cast< QtFontPropertyManagerWrapper *>(this));
    return QtFontPropertyManager::qt_metacast(_clname);
}

QtFontPropertyManagerWrapper::~QtFontPropertyManagerWrapper()
{
    SbkObject *wrapper = Shiboken::BindingManager::instance().retrieveWrapper(this);
    Shiboken::Object::destroy(wrapper, this);
}

// Target ---------------------------------------------------------

extern "C" {
static int
Sbk_QtFontPropertyManager_Init(PyObject *self, PyObject *args, PyObject *kwds)
{
    SBK_UNUSED(kwds)
    const QMetaObject *metaObject;
    SbkObject *sbkSelf = reinterpret_cast<SbkObject *>(self);
    PySide::Feature::Select(self);
    if (Shiboken::Object::isUserType(self) && !Shiboken::ObjectType::canCallConstructor(self->ob_type, Shiboken::SbkType< ::QtFontPropertyManager >()))
        return -1;

    ::QtFontPropertyManagerWrapper *cptr{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtFontPropertyManager.__init__";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp[1];
    SBK_UNUSED(pythonToCpp)
    const Py_ssize_t numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {nullptr};

    // invalid argument lengths

    if (!PyArg_ParseTuple(args, "|O:QtFontPropertyManager", &(pyArgs[0])))
        return -1;


    // Overloaded function decisor
    // 0: QtFontPropertyManager::QtFontPropertyManager(QObject*)
    if (numArgs == 0) {
        overloadId = 0; // QtFontPropertyManager(QObject*)
    } else if (numArgs >= 1
        && (pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkPySide6_QtCoreTypes[SBK_QOBJECT_IDX], (pyArgs[0])))) {
        overloadId = 0; // QtFontPropertyManager(QObject*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtFontPropertyManager_Init_TypeError;

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
                    goto Sbk_QtFontPropertyManager_Init_TypeError;
                }
                if (value) {
                    pyArgs[0] = value;
                    if (!(pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkPySide6_QtCoreTypes[SBK_QOBJECT_IDX], (pyArgs[0]))))
                        goto Sbk_QtFontPropertyManager_Init_TypeError;
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
        ::QObject *cppArg0 = 0;
        if (pythonToCpp[0])
            pythonToCpp[0](pyArgs[0], &cppArg0);

        if (!PyErr_Occurred()) {
            // QtFontPropertyManager(QObject*)
            void *addr = PySide::nextQObjectMemoryAddr();
            if (addr) {
                cptr = new (addr) ::QtFontPropertyManagerWrapper(cppArg0);
                PySide::setNextQObjectMemoryAddr(nullptr);
            } else {
                cptr = new ::QtFontPropertyManagerWrapper(cppArg0);
            }

            // Ownership transferences (constructor heuristics).
            Shiboken::Object::setParent(pyArgs[0], self);
        }
    }

    if (PyErr_Occurred() || !Shiboken::Object::setCppPointer(sbkSelf, Shiboken::SbkType< ::QtFontPropertyManager >(), cptr)) {
        delete cptr;
        return -1;
    }
    if (!cptr) goto Sbk_QtFontPropertyManager_Init_TypeError;

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
            goto Sbk_QtFontPropertyManager_Init_TypeError;
    };


    return 1;

    Sbk_QtFontPropertyManager_Init_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return -1;
}

static PyObject *Sbk_QtFontPropertyManagerFunc_check(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtFontPropertyManagerWrapper *>(reinterpret_cast< ::QtFontPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTFONTPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtFontPropertyManager.check";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtAbstractPropertyManager::check(const QtProperty*)const->bool
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArg)))) {
        overloadId = 0; // check(const QtProperty*)const
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtFontPropertyManagerFunc_check_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // check(const QtProperty*)const
            bool cppResult = Shiboken::Object::hasCppWrapper(reinterpret_cast<SbkObject *>(self))
                ? const_cast<const ::QtFontPropertyManagerWrapper *>(cppSelf)->::QtFontPropertyManager::check(cppArg0)
                : const_cast<const ::QtFontPropertyManagerWrapper *>(cppSelf)->check(cppArg0);
            pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtFontPropertyManagerFunc_check_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtFontPropertyManagerFunc_initializeProperty(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtFontPropertyManagerWrapper *>(reinterpret_cast< ::QtFontPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTFONTPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtFontPropertyManager.initializeProperty";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtAbstractPropertyManager::initializeProperty(QtProperty*)
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArg)))) {
        overloadId = 0; // initializeProperty(QtProperty*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtFontPropertyManagerFunc_initializeProperty_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // initializeProperty(QtProperty*)
            static_cast<::QtFontPropertyManagerWrapper *>(cppSelf)->QtFontPropertyManagerWrapper::initializeProperty_protected(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtFontPropertyManagerFunc_initializeProperty_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtFontPropertyManagerFunc_setCheck(PyObject *self, PyObject *args)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtFontPropertyManagerWrapper *>(reinterpret_cast< ::QtFontPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTFONTPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtFontPropertyManager.setCheck";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp[2];
    SBK_UNUSED(pythonToCpp)
    const Py_ssize_t numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {nullptr, nullptr};

    // invalid argument lengths

    if (!PyArg_UnpackTuple(args, "setCheck", 2, 2, &(pyArgs[0]), &(pyArgs[1])))
        return {};


    // Overloaded function decisor
    // 0: QtAbstractPropertyManager::setCheck(QtProperty*,bool)
    if (numArgs == 2
        && (pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::pythonToCppConversion(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), (pyArgs[1])))) {
        overloadId = 0; // setCheck(QtProperty*,bool)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtFontPropertyManagerFunc_setCheck_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp[0](pyArgs[0], &cppArg0);
        bool cppArg1;
        pythonToCpp[1](pyArgs[1], &cppArg1);

        if (!PyErr_Occurred()) {
            // setCheck(QtProperty*,bool)
            Shiboken::Object::hasCppWrapper(reinterpret_cast<SbkObject *>(self))
                ? cppSelf->::QtFontPropertyManager::setCheck(cppArg0, cppArg1)
                : cppSelf->setCheck(cppArg0, cppArg1);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtFontPropertyManagerFunc_setCheck_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtFontPropertyManagerFunc_setValue(PyObject *self, PyObject *args)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtFontPropertyManagerWrapper *>(reinterpret_cast< ::QtFontPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTFONTPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtFontPropertyManager.setValue";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp[2];
    SBK_UNUSED(pythonToCpp)
    const Py_ssize_t numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {nullptr, nullptr};

    // invalid argument lengths

    if (!PyArg_UnpackTuple(args, "setValue", 2, 2, &(pyArgs[0]), &(pyArgs[1])))
        return {};


    // Overloaded function decisor
    // 0: QtFontPropertyManager::setValue(QtProperty*,QFont)
    if (numArgs == 2
        && (pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::pythonToCppReferenceConversion(SbkPySide6_QtGuiTypes[SBK_QFONT_IDX], (pyArgs[1])))) {
        overloadId = 0; // setValue(QtProperty*,QFont)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtFontPropertyManagerFunc_setValue_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp[0](pyArgs[0], &cppArg0);
        if (!Shiboken::Object::isValid(pyArgs[1]))
            return {};
        ::QFont cppArg1_local;
        ::QFont *cppArg1 = &cppArg1_local;
        if (pythonToCpp[1].isValue())
            pythonToCpp[1](pyArgs[1], &cppArg1_local);
        else
            pythonToCpp[1](pyArgs[1], &cppArg1);


        if (!PyErr_Occurred()) {
            // setValue(QtProperty*,QFont)
            cppSelf->setValue(cppArg0, *cppArg1);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtFontPropertyManagerFunc_setValue_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtFontPropertyManagerFunc_subBoolPropertyManager(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtFontPropertyManagerWrapper *>(reinterpret_cast< ::QtFontPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTFONTPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // subBoolPropertyManager()const
            QtBoolPropertyManager * cppResult = const_cast<const ::QtFontPropertyManagerWrapper *>(cppSelf)->subBoolPropertyManager();
            pyResult = Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTBOOLPROPERTYMANAGER_IDX], cppResult);
            // Ownership transferences (return value heuristics).
            Shiboken::Object::setParent(self, pyResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtFontPropertyManagerFunc_subEnumPropertyManager(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtFontPropertyManagerWrapper *>(reinterpret_cast< ::QtFontPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTFONTPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // subEnumPropertyManager()const
            QtEnumPropertyManager * cppResult = const_cast<const ::QtFontPropertyManagerWrapper *>(cppSelf)->subEnumPropertyManager();
            pyResult = Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTENUMPROPERTYMANAGER_IDX], cppResult);
            // Ownership transferences (return value heuristics).
            Shiboken::Object::setParent(self, pyResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtFontPropertyManagerFunc_subIntPropertyManager(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtFontPropertyManagerWrapper *>(reinterpret_cast< ::QtFontPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTFONTPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // subIntPropertyManager()const
            QtIntPropertyManager * cppResult = const_cast<const ::QtFontPropertyManagerWrapper *>(cppSelf)->subIntPropertyManager();
            pyResult = Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTINTPROPERTYMANAGER_IDX], cppResult);
            // Ownership transferences (return value heuristics).
            Shiboken::Object::setParent(self, pyResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtFontPropertyManagerFunc_uninitializeProperty(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtFontPropertyManagerWrapper *>(reinterpret_cast< ::QtFontPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTFONTPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtFontPropertyManager.uninitializeProperty";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtAbstractPropertyManager::uninitializeProperty(QtProperty*)
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArg)))) {
        overloadId = 0; // uninitializeProperty(QtProperty*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtFontPropertyManagerFunc_uninitializeProperty_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // uninitializeProperty(QtProperty*)
            static_cast<::QtFontPropertyManagerWrapper *>(cppSelf)->QtFontPropertyManagerWrapper::uninitializeProperty_protected(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtFontPropertyManagerFunc_uninitializeProperty_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtFontPropertyManagerFunc_value(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtFontPropertyManagerWrapper *>(reinterpret_cast< ::QtFontPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTFONTPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtFontPropertyManager.value";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtFontPropertyManager::value(const QtProperty*)const->QFont
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArg)))) {
        overloadId = 0; // value(const QtProperty*)const
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtFontPropertyManagerFunc_value_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // value(const QtProperty*)const
            QFont cppResult = const_cast<const ::QtFontPropertyManagerWrapper *>(cppSelf)->value(cppArg0);
            pyResult = Shiboken::Conversions::copyToPython(SbkPySide6_QtGuiTypes[SBK_QFONT_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtFontPropertyManagerFunc_value_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtFontPropertyManagerFunc_valueIcon(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtFontPropertyManagerWrapper *>(reinterpret_cast< ::QtFontPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTFONTPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtFontPropertyManager.valueIcon";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtAbstractPropertyManager::valueIcon(const QtProperty*)const->QIcon
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArg)))) {
        overloadId = 0; // valueIcon(const QtProperty*)const
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtFontPropertyManagerFunc_valueIcon_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // valueIcon(const QtProperty*)const
            QIcon cppResult = static_cast<::QtFontPropertyManagerWrapper *>(cppSelf)->QtFontPropertyManagerWrapper::valueIcon_protected(cppArg0);
            pyResult = Shiboken::Conversions::copyToPython(SbkPySide6_QtGuiTypes[SBK_QICON_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtFontPropertyManagerFunc_valueIcon_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtFontPropertyManagerFunc_valueText(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtFontPropertyManagerWrapper *>(reinterpret_cast< ::QtFontPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTFONTPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtFontPropertyManager.valueText";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtAbstractPropertyManager::valueText(const QtProperty*)const->QString
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArg)))) {
        overloadId = 0; // valueText(const QtProperty*)const
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtFontPropertyManagerFunc_valueText_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // valueText(const QtProperty*)const
            QString cppResult = static_cast<::QtFontPropertyManagerWrapper *>(cppSelf)->QtFontPropertyManagerWrapper::valueText_protected(cppArg0);
            pyResult = Shiboken::Conversions::copyToPython(SbkPySide6_QtCoreTypeConverters[SBK_QSTRING_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtFontPropertyManagerFunc_valueText_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}


static const char *Sbk_QtFontPropertyManager_PropertyStrings[] = {
    nullptr // Sentinel
};

static PyMethodDef Sbk_QtFontPropertyManager_methods[] = {
    {"check", reinterpret_cast<PyCFunction>(Sbk_QtFontPropertyManagerFunc_check), METH_O, nullptr},
    {"initializeProperty", reinterpret_cast<PyCFunction>(Sbk_QtFontPropertyManagerFunc_initializeProperty), METH_O, nullptr},
    {"setCheck", reinterpret_cast<PyCFunction>(Sbk_QtFontPropertyManagerFunc_setCheck), METH_VARARGS, nullptr},
    {"setValue", reinterpret_cast<PyCFunction>(Sbk_QtFontPropertyManagerFunc_setValue), METH_VARARGS, nullptr},
    {"subBoolPropertyManager", reinterpret_cast<PyCFunction>(Sbk_QtFontPropertyManagerFunc_subBoolPropertyManager), METH_NOARGS, nullptr},
    {"subEnumPropertyManager", reinterpret_cast<PyCFunction>(Sbk_QtFontPropertyManagerFunc_subEnumPropertyManager), METH_NOARGS, nullptr},
    {"subIntPropertyManager", reinterpret_cast<PyCFunction>(Sbk_QtFontPropertyManagerFunc_subIntPropertyManager), METH_NOARGS, nullptr},
    {"uninitializeProperty", reinterpret_cast<PyCFunction>(Sbk_QtFontPropertyManagerFunc_uninitializeProperty), METH_O, nullptr},
    {"value", reinterpret_cast<PyCFunction>(Sbk_QtFontPropertyManagerFunc_value), METH_O, nullptr},
    {"valueIcon", reinterpret_cast<PyCFunction>(Sbk_QtFontPropertyManagerFunc_valueIcon), METH_O, nullptr},
    {"valueText", reinterpret_cast<PyCFunction>(Sbk_QtFontPropertyManagerFunc_valueText), METH_O, nullptr},

    {nullptr, nullptr, 0, nullptr} // Sentinel
};

static int Sbk_QtFontPropertyManager_setattro(PyObject *self, PyObject *name, PyObject *value)
{
    PySide::Feature::Select(self);
    if (value && PyCallable_Check(value)) {
        auto plain_inst = reinterpret_cast< ::QtFontPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTFONTPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self)));
        auto inst = dynamic_cast<QtFontPropertyManagerWrapper *>(plain_inst);
        if (inst)
            inst->resetPyMethodCache();
    }
    Shiboken::AutoDecRef pp(reinterpret_cast<PyObject *>(PySide::Property::getObject(self, name)));
    if (!pp.isNull())
        return PySide::Property::setValue(reinterpret_cast<PySideProperty *>(pp.object()), self, value);
    return PyObject_GenericSetAttr(self, name, value);
}

} // extern "C"

static int Sbk_QtFontPropertyManager_traverse(PyObject *self, visitproc visit, void *arg)
{
    return SbkObject_TypeF()->tp_traverse(self, visit, arg);
}
static int Sbk_QtFontPropertyManager_clear(PyObject *self)
{
    return reinterpret_cast<PyTypeObject *>(SbkObject_TypeF())->tp_clear(self);
}
// Class Definition -----------------------------------------------
extern "C" {
static PyTypeObject *_Sbk_QtFontPropertyManager_Type = nullptr;
static PyTypeObject *Sbk_QtFontPropertyManager_TypeF(void)
{
    return _Sbk_QtFontPropertyManager_Type;
}

static PyType_Slot Sbk_QtFontPropertyManager_slots[] = {
    {Py_tp_base,        nullptr}, // inserted by introduceWrapperType
    {Py_tp_dealloc,     reinterpret_cast<void *>(&SbkDeallocWrapper)},
    {Py_tp_repr,        nullptr},
    {Py_tp_hash,        nullptr},
    {Py_tp_call,        nullptr},
    {Py_tp_str,         nullptr},
    {Py_tp_getattro,    nullptr},
    {Py_tp_setattro,    reinterpret_cast<void *>(Sbk_QtFontPropertyManager_setattro)},
    {Py_tp_traverse,    reinterpret_cast<void *>(Sbk_QtFontPropertyManager_traverse)},
    {Py_tp_clear,       reinterpret_cast<void *>(Sbk_QtFontPropertyManager_clear)},
    {Py_tp_richcompare, nullptr},
    {Py_tp_iter,        nullptr},
    {Py_tp_iternext,    nullptr},
    {Py_tp_methods,     reinterpret_cast<void *>(Sbk_QtFontPropertyManager_methods)},
    {Py_tp_getset,      nullptr},
    {Py_tp_init,        reinterpret_cast<void *>(Sbk_QtFontPropertyManager_Init)},
    {Py_tp_new,         reinterpret_cast<void *>(SbkObject_tp_new)},
    {0, nullptr}
};
static PyType_Spec Sbk_QtFontPropertyManager_spec = {
    "1:qtpropertybrowser.QtFontPropertyManager",
    sizeof(SbkObject),
    0,
    Py_TPFLAGS_DEFAULT|Py_TPFLAGS_BASETYPE|Py_TPFLAGS_HAVE_GC,
    Sbk_QtFontPropertyManager_slots
};

} //extern "C"

static void *Sbk_QtFontPropertyManager_typeDiscovery(void *cptr, PyTypeObject *instanceType)
{
    SBK_UNUSED(cptr)
    SBK_UNUSED(instanceType)
    if (instanceType == Shiboken::SbkType< ::QObject >())
        return dynamic_cast< ::QtFontPropertyManager *>(reinterpret_cast< ::QObject *>(cptr));
    return {};
}


// Type conversion functions.

// Python to C++ pointer conversion - returns the C++ object of the Python wrapper (keeps object identity).
static void QtFontPropertyManager_PythonToCpp_QtFontPropertyManager_PTR(PyObject *pyIn, void *cppOut)
{
    Shiboken::Conversions::pythonToCppPointer(Sbk_QtFontPropertyManager_TypeF(), pyIn, cppOut);
}
static PythonToCppFunc is_QtFontPropertyManager_PythonToCpp_QtFontPropertyManager_PTR_Convertible(PyObject *pyIn)
{
    if (pyIn == Py_None)
        return Shiboken::Conversions::nonePythonToCppNullPtr;
    if (PyObject_TypeCheck(pyIn, Sbk_QtFontPropertyManager_TypeF()))
        return QtFontPropertyManager_PythonToCpp_QtFontPropertyManager_PTR;
    return {};
}

// C++ to Python pointer conversion - tries to find the Python wrapper for the C++ object (keeps object identity).
static PyObject *QtFontPropertyManager_PTR_CppToPython_QtFontPropertyManager(const void *cppIn)
{
    return PySide::getWrapperForQObject(reinterpret_cast<::QtFontPropertyManager *>(const_cast<void *>(cppIn)), Sbk_QtFontPropertyManager_TypeF());

}

// The signatures string for the functions.
// Multiple signatures have their index "n:" in front.
static const char *QtFontPropertyManager_SignatureStrings[] = {
    "qtpropertybrowser.QtFontPropertyManager(self,parent:PySide6.QtCore.QObject=0)",
    "qtpropertybrowser.QtFontPropertyManager.check(self,property:qtpropertybrowser.QtProperty)->bool",
    "qtpropertybrowser.QtFontPropertyManager.initializeProperty(self,property:qtpropertybrowser.QtProperty)",
    "qtpropertybrowser.QtFontPropertyManager.setCheck(self,property:qtpropertybrowser.QtProperty,check:bool)",
    "qtpropertybrowser.QtFontPropertyManager.setValue(self,property:qtpropertybrowser.QtProperty,val:typing.Union[PySide6.QtGui.QFont, QString, QStringList])",
    "qtpropertybrowser.QtFontPropertyManager.subBoolPropertyManager(self)->qtpropertybrowser.QtBoolPropertyManager",
    "qtpropertybrowser.QtFontPropertyManager.subEnumPropertyManager(self)->qtpropertybrowser.QtEnumPropertyManager",
    "qtpropertybrowser.QtFontPropertyManager.subIntPropertyManager(self)->qtpropertybrowser.QtIntPropertyManager",
    "qtpropertybrowser.QtFontPropertyManager.uninitializeProperty(self,property:qtpropertybrowser.QtProperty)",
    "qtpropertybrowser.QtFontPropertyManager.value(self,property:qtpropertybrowser.QtProperty)->PySide6.QtGui.QFont",
    "qtpropertybrowser.QtFontPropertyManager.valueIcon(self,property:qtpropertybrowser.QtProperty)->PySide6.QtGui.QIcon",
    "qtpropertybrowser.QtFontPropertyManager.valueText(self,property:qtpropertybrowser.QtProperty)->QString",
    nullptr}; // Sentinel

void init_QtFontPropertyManager(PyObject *module)
{
    _Sbk_QtFontPropertyManager_Type = Shiboken::ObjectType::introduceWrapperType(
        module,
        "QtFontPropertyManager",
        "QtFontPropertyManager*",
        &Sbk_QtFontPropertyManager_spec,
        &Shiboken::callCppDestructor< ::QtFontPropertyManager >,
        SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYMANAGER_IDX],
        0,
        0);
    auto *pyType = Sbk_QtFontPropertyManager_TypeF(); // references _Sbk_QtFontPropertyManager_Type
    InitSignatureStrings(pyType, QtFontPropertyManager_SignatureStrings);
    SbkObjectType_SetPropertyStrings(pyType, Sbk_QtFontPropertyManager_PropertyStrings);
    SbkqtpropertybrowserTypes[SBK_QTFONTPROPERTYMANAGER_IDX] = pyType;

    // Register Converter
    SbkConverter *converter = Shiboken::Conversions::createConverter(pyType,
        QtFontPropertyManager_PythonToCpp_QtFontPropertyManager_PTR,
        is_QtFontPropertyManager_PythonToCpp_QtFontPropertyManager_PTR_Convertible,
        QtFontPropertyManager_PTR_CppToPython_QtFontPropertyManager);

    Shiboken::Conversions::registerConverterName(converter, "QtFontPropertyManager");
    Shiboken::Conversions::registerConverterName(converter, "QtFontPropertyManager*");
    Shiboken::Conversions::registerConverterName(converter, "QtFontPropertyManager&");
    Shiboken::Conversions::registerConverterName(converter, typeid(::QtFontPropertyManager).name());
    Shiboken::Conversions::registerConverterName(converter, typeid(::QtFontPropertyManagerWrapper).name());


    Shiboken::ObjectType::setTypeDiscoveryFunctionV2(Sbk_QtFontPropertyManager_TypeF(), &Sbk_QtFontPropertyManager_typeDiscovery);

    PySide::Signal::registerSignals(pyType, &::QtFontPropertyManager::staticMetaObject);
    QtFontPropertyManagerWrapper::pysideInitQtMetaTypes();
    Shiboken::ObjectType::setSubTypeInitHook(pyType, &PySide::initQObjectSubType);
    PySide::initDynamicMetaObject(pyType, &::QtFontPropertyManager::staticMetaObject, sizeof(QtFontPropertyManagerWrapper));
}
