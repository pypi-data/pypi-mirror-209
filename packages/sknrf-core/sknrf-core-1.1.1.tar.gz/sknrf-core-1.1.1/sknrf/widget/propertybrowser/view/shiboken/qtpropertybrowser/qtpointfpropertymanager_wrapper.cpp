
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
#include "qtpointfpropertymanager_wrapper.h"

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

void QtPointFPropertyManagerWrapper::pysideInitQtMetaTypes()
{
}

void QtPointFPropertyManagerWrapper::resetPyMethodCache()
{
    std::fill_n(m_PyMethodCache, sizeof(m_PyMethodCache) / sizeof(m_PyMethodCache[0]), false);
}

QtPointFPropertyManagerWrapper::QtPointFPropertyManagerWrapper(QObject * parent) : QtPointFPropertyManager(parent)
{
    resetPyMethodCache();
    // ... middle
}

bool QtPointFPropertyManagerWrapper::check(const QtProperty * property) const
{
    if (m_PyMethodCache[0])
        return this->::QtPointFPropertyManager::check(property);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return false;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "check";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[0] = true;
        gil.release();
        return this->::QtPointFPropertyManager::check(property);
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
        Shiboken::Warnings::warnInvalidReturnValue("QtPointFPropertyManager", "check", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QIcon QtPointFPropertyManagerWrapper::checkIcon(const QtProperty * property) const
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
        Shiboken::Warnings::warnInvalidReturnValue("QtPointFPropertyManager", "checkIcon", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QIcon >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return {};
    }
    ::QIcon cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtPointFPropertyManagerWrapper::childEvent(QChildEvent * event)
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

void QtPointFPropertyManagerWrapper::connectNotify(const QMetaMethod & signal)
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

QtProperty * QtPointFPropertyManagerWrapper::createProperty()
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
        Shiboken::Warnings::warnInvalidReturnValue("QtPointFPropertyManager", "createProperty", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QtProperty >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return nullptr;
    }
    ::QtProperty *cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtPointFPropertyManagerWrapper::customEvent(QEvent * event)
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

void QtPointFPropertyManagerWrapper::disconnectNotify(const QMetaMethod & signal)
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

QString QtPointFPropertyManagerWrapper::displayText(const QtProperty * property) const
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
        Shiboken::Warnings::warnInvalidReturnValue("QtPointFPropertyManager", "displayText", "QString", Py_TYPE(pyResult)->tp_name);
        return ::QString();
    }
    ::QString cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

bool QtPointFPropertyManagerWrapper::event(QEvent * event)
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
        Shiboken::Warnings::warnInvalidReturnValue("QtPointFPropertyManager", "event", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

bool QtPointFPropertyManagerWrapper::eventFilter(QObject * watched, QEvent * event)
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
        Shiboken::Warnings::warnInvalidReturnValue("QtPointFPropertyManager", "eventFilter", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QBrush QtPointFPropertyManagerWrapper::foreground(const QtProperty * property) const
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
        Shiboken::Warnings::warnInvalidReturnValue("QtPointFPropertyManager", "foreground", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QBrush >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return {};
    }
    ::QBrush cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QString QtPointFPropertyManagerWrapper::formatText(const QtProperty * property) const
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
        Shiboken::Warnings::warnInvalidReturnValue("QtPointFPropertyManager", "formatText", "QString", Py_TYPE(pyResult)->tp_name);
        return ::QString();
    }
    ::QString cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

bool QtPointFPropertyManagerWrapper::hasValue(const QtProperty * property) const
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
        Shiboken::Warnings::warnInvalidReturnValue("QtPointFPropertyManager", "hasValue", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtPointFPropertyManagerWrapper::initializeProperty(QtProperty * property)
{
    if (m_PyMethodCache[13]) {
        return this->::QtPointFPropertyManager::initializeProperty(property);
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
        return this->::QtPointFPropertyManager::initializeProperty(property);
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

bool QtPointFPropertyManagerWrapper::isReadOnly(const QtProperty * arg__1) const
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
        Shiboken::Warnings::warnInvalidReturnValue("QtPointFPropertyManager", "isReadOnly", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QString QtPointFPropertyManagerWrapper::maximumText(const QtProperty * property) const
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
        Shiboken::Warnings::warnInvalidReturnValue("QtPointFPropertyManager", "maximumText", "QString", Py_TYPE(pyResult)->tp_name);
        return ::QString();
    }
    ::QString cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QString QtPointFPropertyManagerWrapper::minimumText(const QtProperty * property) const
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
        Shiboken::Warnings::warnInvalidReturnValue("QtPointFPropertyManager", "minimumText", "QString", Py_TYPE(pyResult)->tp_name);
        return ::QString();
    }
    ::QString cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QString QtPointFPropertyManagerWrapper::pkAvgText(const QtProperty * property) const
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
        Shiboken::Warnings::warnInvalidReturnValue("QtPointFPropertyManager", "pkAvgText", "QString", Py_TYPE(pyResult)->tp_name);
        return ::QString();
    }
    ::QString cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtPointFPropertyManagerWrapper::setCheck(QtProperty * property, bool check)
{
    if (m_PyMethodCache[18]) {
        return this->::QtPointFPropertyManager::setCheck(property, check);
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
        return this->::QtPointFPropertyManager::setCheck(property, check);
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

void QtPointFPropertyManagerWrapper::timerEvent(QTimerEvent * event)
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

void QtPointFPropertyManagerWrapper::uninitializeProperty(QtProperty * property)
{
    if (m_PyMethodCache[20]) {
        return this->::QtPointFPropertyManager::uninitializeProperty(property);
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
        return this->::QtPointFPropertyManager::uninitializeProperty(property);
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

QString QtPointFPropertyManagerWrapper::unitText(const QtProperty * property) const
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
        Shiboken::Warnings::warnInvalidReturnValue("QtPointFPropertyManager", "unitText", "QString", Py_TYPE(pyResult)->tp_name);
        return ::QString();
    }
    ::QString cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QIcon QtPointFPropertyManagerWrapper::valueIcon(const QtProperty * property) const
{
    if (m_PyMethodCache[22])
        return this->::QtAbstractPropertyManager::valueIcon(property);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return {};
    static PyObject *nameCache[2] = {};
    static const char *funcName = "valueIcon";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[22] = true;
        gil.release();
        return this->::QtAbstractPropertyManager::valueIcon(property);
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
        Shiboken::Warnings::warnInvalidReturnValue("QtPointFPropertyManager", "valueIcon", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QIcon >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return {};
    }
    ::QIcon cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QString QtPointFPropertyManagerWrapper::valueText(const QtProperty * property) const
{
    if (m_PyMethodCache[23])
        return this->::QtPointFPropertyManager::valueText(property);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return ::QString();
    static PyObject *nameCache[2] = {};
    static const char *funcName = "valueText";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[23] = true;
        gil.release();
        return this->::QtPointFPropertyManager::valueText(property);
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
        Shiboken::Warnings::warnInvalidReturnValue("QtPointFPropertyManager", "valueText", "QString", Py_TYPE(pyResult)->tp_name);
        return ::QString();
    }
    ::QString cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

const QMetaObject *QtPointFPropertyManagerWrapper::metaObject() const
{
    if (QObject::d_ptr->metaObject)
        return QObject::d_ptr->dynamicMetaObject();
    SbkObject *pySelf = Shiboken::BindingManager::instance().retrieveWrapper(this);
    if (pySelf == nullptr)
        return QtPointFPropertyManager::metaObject();
    return PySide::SignalManager::retrieveMetaObject(reinterpret_cast<PyObject *>(pySelf));
}

int QtPointFPropertyManagerWrapper::qt_metacall(QMetaObject::Call call, int id, void **args)
{
    int result = QtPointFPropertyManager::qt_metacall(call, id, args);
    return result < 0 ? result : PySide::SignalManager::qt_metacall(this, call, id, args);
}

void *QtPointFPropertyManagerWrapper::qt_metacast(const char *_clname)
{
    if (!_clname)
        return {};
    SbkObject *pySelf = Shiboken::BindingManager::instance().retrieveWrapper(this);
    if (pySelf && PySide::inherits(Py_TYPE(pySelf), _clname))
        return static_cast<void *>(const_cast< QtPointFPropertyManagerWrapper *>(this));
    return QtPointFPropertyManager::qt_metacast(_clname);
}

QtPointFPropertyManagerWrapper::~QtPointFPropertyManagerWrapper()
{
    SbkObject *wrapper = Shiboken::BindingManager::instance().retrieveWrapper(this);
    Shiboken::Object::destroy(wrapper, this);
}

// Target ---------------------------------------------------------

extern "C" {
static int
Sbk_QtPointFPropertyManager_Init(PyObject *self, PyObject *args, PyObject *kwds)
{
    SBK_UNUSED(kwds)
    const QMetaObject *metaObject;
    SbkObject *sbkSelf = reinterpret_cast<SbkObject *>(self);
    PySide::Feature::Select(self);
    if (Shiboken::Object::isUserType(self) && !Shiboken::ObjectType::canCallConstructor(self->ob_type, Shiboken::SbkType< ::QtPointFPropertyManager >()))
        return -1;

    ::QtPointFPropertyManagerWrapper *cptr{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtPointFPropertyManager.__init__";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp[1];
    SBK_UNUSED(pythonToCpp)
    const Py_ssize_t numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {nullptr};

    // invalid argument lengths

    if (!PyArg_ParseTuple(args, "|O:QtPointFPropertyManager", &(pyArgs[0])))
        return -1;


    // Overloaded function decisor
    // 0: QtPointFPropertyManager::QtPointFPropertyManager(QObject*)
    if (numArgs == 0) {
        overloadId = 0; // QtPointFPropertyManager(QObject*)
    } else if (numArgs >= 1
        && (pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkPySide6_QtCoreTypes[SBK_QOBJECT_IDX], (pyArgs[0])))) {
        overloadId = 0; // QtPointFPropertyManager(QObject*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtPointFPropertyManager_Init_TypeError;

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
                    goto Sbk_QtPointFPropertyManager_Init_TypeError;
                }
                if (value) {
                    pyArgs[0] = value;
                    if (!(pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkPySide6_QtCoreTypes[SBK_QOBJECT_IDX], (pyArgs[0]))))
                        goto Sbk_QtPointFPropertyManager_Init_TypeError;
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
            // QtPointFPropertyManager(QObject*)
            void *addr = PySide::nextQObjectMemoryAddr();
            if (addr) {
                cptr = new (addr) ::QtPointFPropertyManagerWrapper(cppArg0);
                PySide::setNextQObjectMemoryAddr(nullptr);
            } else {
                cptr = new ::QtPointFPropertyManagerWrapper(cppArg0);
            }

            // Ownership transferences (constructor heuristics).
            Shiboken::Object::setParent(pyArgs[0], self);
        }
    }

    if (PyErr_Occurred() || !Shiboken::Object::setCppPointer(sbkSelf, Shiboken::SbkType< ::QtPointFPropertyManager >(), cptr)) {
        delete cptr;
        return -1;
    }
    if (!cptr) goto Sbk_QtPointFPropertyManager_Init_TypeError;

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
            goto Sbk_QtPointFPropertyManager_Init_TypeError;
    };


    return 1;

    Sbk_QtPointFPropertyManager_Init_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return -1;
}

static PyObject *Sbk_QtPointFPropertyManagerFunc_check(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtPointFPropertyManagerWrapper *>(reinterpret_cast< ::QtPointFPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPOINTFPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtPointFPropertyManager.check";
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
    if (overloadId == -1) goto Sbk_QtPointFPropertyManagerFunc_check_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // check(const QtProperty*)const
            bool cppResult = Shiboken::Object::hasCppWrapper(reinterpret_cast<SbkObject *>(self))
                ? const_cast<const ::QtPointFPropertyManagerWrapper *>(cppSelf)->::QtPointFPropertyManager::check(cppArg0)
                : const_cast<const ::QtPointFPropertyManagerWrapper *>(cppSelf)->check(cppArg0);
            pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtPointFPropertyManagerFunc_check_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtPointFPropertyManagerFunc_decimals(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtPointFPropertyManagerWrapper *>(reinterpret_cast< ::QtPointFPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPOINTFPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtPointFPropertyManager.decimals";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtPointFPropertyManager::decimals(const QtProperty*)const->int
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArg)))) {
        overloadId = 0; // decimals(const QtProperty*)const
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtPointFPropertyManagerFunc_decimals_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // decimals(const QtProperty*)const
            int cppResult = const_cast<const ::QtPointFPropertyManagerWrapper *>(cppSelf)->decimals(cppArg0);
            pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<int>(), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtPointFPropertyManagerFunc_decimals_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtPointFPropertyManagerFunc_initializeProperty(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtPointFPropertyManagerWrapper *>(reinterpret_cast< ::QtPointFPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPOINTFPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtPointFPropertyManager.initializeProperty";
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
    if (overloadId == -1) goto Sbk_QtPointFPropertyManagerFunc_initializeProperty_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // initializeProperty(QtProperty*)
            static_cast<::QtPointFPropertyManagerWrapper *>(cppSelf)->QtPointFPropertyManagerWrapper::initializeProperty_protected(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtPointFPropertyManagerFunc_initializeProperty_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtPointFPropertyManagerFunc_maximum(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtPointFPropertyManagerWrapper *>(reinterpret_cast< ::QtPointFPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPOINTFPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtPointFPropertyManager.maximum";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtPointFPropertyManager::maximum(const QtProperty*)const->QPointF
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArg)))) {
        overloadId = 0; // maximum(const QtProperty*)const
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtPointFPropertyManagerFunc_maximum_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // maximum(const QtProperty*)const
            QPointF cppResult = const_cast<const ::QtPointFPropertyManagerWrapper *>(cppSelf)->maximum(cppArg0);
            pyResult = Shiboken::Conversions::copyToPython(SbkPySide6_QtCoreTypes[SBK_QPOINTF_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtPointFPropertyManagerFunc_maximum_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtPointFPropertyManagerFunc_minimum(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtPointFPropertyManagerWrapper *>(reinterpret_cast< ::QtPointFPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPOINTFPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtPointFPropertyManager.minimum";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtPointFPropertyManager::minimum(const QtProperty*)const->QPointF
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArg)))) {
        overloadId = 0; // minimum(const QtProperty*)const
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtPointFPropertyManagerFunc_minimum_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // minimum(const QtProperty*)const
            QPointF cppResult = const_cast<const ::QtPointFPropertyManagerWrapper *>(cppSelf)->minimum(cppArg0);
            pyResult = Shiboken::Conversions::copyToPython(SbkPySide6_QtCoreTypes[SBK_QPOINTF_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtPointFPropertyManagerFunc_minimum_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtPointFPropertyManagerFunc_precision(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtPointFPropertyManagerWrapper *>(reinterpret_cast< ::QtPointFPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPOINTFPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtPointFPropertyManager.precision";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtPointFPropertyManager::precision(const QtProperty*)const->int
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArg)))) {
        overloadId = 0; // precision(const QtProperty*)const
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtPointFPropertyManagerFunc_precision_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // precision(const QtProperty*)const
            int cppResult = const_cast<const ::QtPointFPropertyManagerWrapper *>(cppSelf)->precision(cppArg0);
            pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<int>(), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtPointFPropertyManagerFunc_precision_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtPointFPropertyManagerFunc_setCheck(PyObject *self, PyObject *args)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtPointFPropertyManagerWrapper *>(reinterpret_cast< ::QtPointFPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPOINTFPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtPointFPropertyManager.setCheck";
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
    if (overloadId == -1) goto Sbk_QtPointFPropertyManagerFunc_setCheck_TypeError;

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
                ? cppSelf->::QtPointFPropertyManager::setCheck(cppArg0, cppArg1)
                : cppSelf->setCheck(cppArg0, cppArg1);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtPointFPropertyManagerFunc_setCheck_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtPointFPropertyManagerFunc_setMaximum(PyObject *self, PyObject *args)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtPointFPropertyManagerWrapper *>(reinterpret_cast< ::QtPointFPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPOINTFPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtPointFPropertyManager.setMaximum";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp[2];
    SBK_UNUSED(pythonToCpp)
    const Py_ssize_t numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {nullptr, nullptr};

    // invalid argument lengths

    if (!PyArg_UnpackTuple(args, "setMaximum", 2, 2, &(pyArgs[0]), &(pyArgs[1])))
        return {};


    // Overloaded function decisor
    // 0: QtPointFPropertyManager::setMaximum(QtProperty*,QPointF)
    if (numArgs == 2
        && (pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::pythonToCppReferenceConversion(SbkPySide6_QtCoreTypes[SBK_QPOINTF_IDX], (pyArgs[1])))) {
        overloadId = 0; // setMaximum(QtProperty*,QPointF)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtPointFPropertyManagerFunc_setMaximum_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp[0](pyArgs[0], &cppArg0);
        if (!Shiboken::Object::isValid(pyArgs[1]))
            return {};
        ::QPointF cppArg1_local;
        ::QPointF *cppArg1 = &cppArg1_local;
        if (pythonToCpp[1].isValue())
            pythonToCpp[1](pyArgs[1], &cppArg1_local);
        else
            pythonToCpp[1](pyArgs[1], &cppArg1);


        if (!PyErr_Occurred()) {
            // setMaximum(QtProperty*,QPointF)
            cppSelf->setMaximum(cppArg0, *cppArg1);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtPointFPropertyManagerFunc_setMaximum_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtPointFPropertyManagerFunc_setMinimum(PyObject *self, PyObject *args)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtPointFPropertyManagerWrapper *>(reinterpret_cast< ::QtPointFPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPOINTFPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtPointFPropertyManager.setMinimum";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp[2];
    SBK_UNUSED(pythonToCpp)
    const Py_ssize_t numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {nullptr, nullptr};

    // invalid argument lengths

    if (!PyArg_UnpackTuple(args, "setMinimum", 2, 2, &(pyArgs[0]), &(pyArgs[1])))
        return {};


    // Overloaded function decisor
    // 0: QtPointFPropertyManager::setMinimum(QtProperty*,QPointF)
    if (numArgs == 2
        && (pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::pythonToCppReferenceConversion(SbkPySide6_QtCoreTypes[SBK_QPOINTF_IDX], (pyArgs[1])))) {
        overloadId = 0; // setMinimum(QtProperty*,QPointF)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtPointFPropertyManagerFunc_setMinimum_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp[0](pyArgs[0], &cppArg0);
        if (!Shiboken::Object::isValid(pyArgs[1]))
            return {};
        ::QPointF cppArg1_local;
        ::QPointF *cppArg1 = &cppArg1_local;
        if (pythonToCpp[1].isValue())
            pythonToCpp[1](pyArgs[1], &cppArg1_local);
        else
            pythonToCpp[1](pyArgs[1], &cppArg1);


        if (!PyErr_Occurred()) {
            // setMinimum(QtProperty*,QPointF)
            cppSelf->setMinimum(cppArg0, *cppArg1);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtPointFPropertyManagerFunc_setMinimum_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtPointFPropertyManagerFunc_setPrecision(PyObject *self, PyObject *args)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtPointFPropertyManagerWrapper *>(reinterpret_cast< ::QtPointFPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPOINTFPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtPointFPropertyManager.setPrecision";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp[2];
    SBK_UNUSED(pythonToCpp)
    const Py_ssize_t numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {nullptr, nullptr};

    // invalid argument lengths

    if (!PyArg_UnpackTuple(args, "setPrecision", 2, 2, &(pyArgs[0]), &(pyArgs[1])))
        return {};


    // Overloaded function decisor
    // 0: QtPointFPropertyManager::setPrecision(QtProperty*,int)
    if (numArgs == 2
        && (pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::pythonToCppConversion(Shiboken::Conversions::PrimitiveTypeConverter<int>(), (pyArgs[1])))) {
        overloadId = 0; // setPrecision(QtProperty*,int)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtPointFPropertyManagerFunc_setPrecision_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp[0](pyArgs[0], &cppArg0);
        int cppArg1;
        pythonToCpp[1](pyArgs[1], &cppArg1);

        if (!PyErr_Occurred()) {
            // setPrecision(QtProperty*,int)
            cppSelf->setPrecision(cppArg0, cppArg1);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtPointFPropertyManagerFunc_setPrecision_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtPointFPropertyManagerFunc_setRange(PyObject *self, PyObject *args)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtPointFPropertyManagerWrapper *>(reinterpret_cast< ::QtPointFPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPOINTFPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtPointFPropertyManager.setRange";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp[3];
    SBK_UNUSED(pythonToCpp)
    const Py_ssize_t numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {nullptr, nullptr, nullptr};

    // invalid argument lengths

    if (!PyArg_UnpackTuple(args, "setRange", 3, 3, &(pyArgs[0]), &(pyArgs[1]), &(pyArgs[2])))
        return {};


    // Overloaded function decisor
    // 0: QtPointFPropertyManager::setRange(QtProperty*,QPointF,QPointF)
    if (numArgs == 3
        && (pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::pythonToCppReferenceConversion(SbkPySide6_QtCoreTypes[SBK_QPOINTF_IDX], (pyArgs[1])))
        && (pythonToCpp[2] = Shiboken::Conversions::pythonToCppReferenceConversion(SbkPySide6_QtCoreTypes[SBK_QPOINTF_IDX], (pyArgs[2])))) {
        overloadId = 0; // setRange(QtProperty*,QPointF,QPointF)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtPointFPropertyManagerFunc_setRange_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp[0](pyArgs[0], &cppArg0);
        if (!Shiboken::Object::isValid(pyArgs[1]))
            return {};
        ::QPointF cppArg1_local;
        ::QPointF *cppArg1 = &cppArg1_local;
        if (pythonToCpp[1].isValue())
            pythonToCpp[1](pyArgs[1], &cppArg1_local);
        else
            pythonToCpp[1](pyArgs[1], &cppArg1);

        if (!Shiboken::Object::isValid(pyArgs[2]))
            return {};
        ::QPointF cppArg2_local;
        ::QPointF *cppArg2 = &cppArg2_local;
        if (pythonToCpp[2].isValue())
            pythonToCpp[2](pyArgs[2], &cppArg2_local);
        else
            pythonToCpp[2](pyArgs[2], &cppArg2);


        if (!PyErr_Occurred()) {
            // setRange(QtProperty*,QPointF,QPointF)
            cppSelf->setRange(cppArg0, *cppArg1, *cppArg2);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtPointFPropertyManagerFunc_setRange_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtPointFPropertyManagerFunc_setValue(PyObject *self, PyObject *args)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtPointFPropertyManagerWrapper *>(reinterpret_cast< ::QtPointFPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPOINTFPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtPointFPropertyManager.setValue";
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
    // 0: QtPointFPropertyManager::setValue(QtProperty*,QPointF)
    if (numArgs == 2
        && (pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::pythonToCppReferenceConversion(SbkPySide6_QtCoreTypes[SBK_QPOINTF_IDX], (pyArgs[1])))) {
        overloadId = 0; // setValue(QtProperty*,QPointF)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtPointFPropertyManagerFunc_setValue_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp[0](pyArgs[0], &cppArg0);
        if (!Shiboken::Object::isValid(pyArgs[1]))
            return {};
        ::QPointF cppArg1_local;
        ::QPointF *cppArg1 = &cppArg1_local;
        if (pythonToCpp[1].isValue())
            pythonToCpp[1](pyArgs[1], &cppArg1_local);
        else
            pythonToCpp[1](pyArgs[1], &cppArg1);


        if (!PyErr_Occurred()) {
            // setValue(QtProperty*,QPointF)
            cppSelf->setValue(cppArg0, *cppArg1);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtPointFPropertyManagerFunc_setValue_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtPointFPropertyManagerFunc_subDoublePropertyManager(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtPointFPropertyManagerWrapper *>(reinterpret_cast< ::QtPointFPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPOINTFPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // subDoublePropertyManager()const
            QtDoublePropertyManager * cppResult = const_cast<const ::QtPointFPropertyManagerWrapper *>(cppSelf)->subDoublePropertyManager();
            pyResult = Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTDOUBLEPROPERTYMANAGER_IDX], cppResult);
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

static PyObject *Sbk_QtPointFPropertyManagerFunc_uninitializeProperty(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtPointFPropertyManagerWrapper *>(reinterpret_cast< ::QtPointFPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPOINTFPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtPointFPropertyManager.uninitializeProperty";
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
    if (overloadId == -1) goto Sbk_QtPointFPropertyManagerFunc_uninitializeProperty_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // uninitializeProperty(QtProperty*)
            static_cast<::QtPointFPropertyManagerWrapper *>(cppSelf)->QtPointFPropertyManagerWrapper::uninitializeProperty_protected(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtPointFPropertyManagerFunc_uninitializeProperty_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtPointFPropertyManagerFunc_value(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtPointFPropertyManagerWrapper *>(reinterpret_cast< ::QtPointFPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPOINTFPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtPointFPropertyManager.value";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtPointFPropertyManager::value(const QtProperty*)const->QPointF
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArg)))) {
        overloadId = 0; // value(const QtProperty*)const
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtPointFPropertyManagerFunc_value_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // value(const QtProperty*)const
            QPointF cppResult = const_cast<const ::QtPointFPropertyManagerWrapper *>(cppSelf)->value(cppArg0);
            pyResult = Shiboken::Conversions::copyToPython(SbkPySide6_QtCoreTypes[SBK_QPOINTF_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtPointFPropertyManagerFunc_value_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtPointFPropertyManagerFunc_valueText(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtPointFPropertyManagerWrapper *>(reinterpret_cast< ::QtPointFPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPOINTFPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtPointFPropertyManager.valueText";
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
    if (overloadId == -1) goto Sbk_QtPointFPropertyManagerFunc_valueText_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // valueText(const QtProperty*)const
            QString cppResult = static_cast<::QtPointFPropertyManagerWrapper *>(cppSelf)->QtPointFPropertyManagerWrapper::valueText_protected(cppArg0);
            pyResult = Shiboken::Conversions::copyToPython(SbkPySide6_QtCoreTypeConverters[SBK_QSTRING_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtPointFPropertyManagerFunc_valueText_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}


static const char *Sbk_QtPointFPropertyManager_PropertyStrings[] = {
    nullptr // Sentinel
};

static PyMethodDef Sbk_QtPointFPropertyManager_methods[] = {
    {"check", reinterpret_cast<PyCFunction>(Sbk_QtPointFPropertyManagerFunc_check), METH_O, nullptr},
    {"decimals", reinterpret_cast<PyCFunction>(Sbk_QtPointFPropertyManagerFunc_decimals), METH_O, nullptr},
    {"initializeProperty", reinterpret_cast<PyCFunction>(Sbk_QtPointFPropertyManagerFunc_initializeProperty), METH_O, nullptr},
    {"maximum", reinterpret_cast<PyCFunction>(Sbk_QtPointFPropertyManagerFunc_maximum), METH_O, nullptr},
    {"minimum", reinterpret_cast<PyCFunction>(Sbk_QtPointFPropertyManagerFunc_minimum), METH_O, nullptr},
    {"precision", reinterpret_cast<PyCFunction>(Sbk_QtPointFPropertyManagerFunc_precision), METH_O, nullptr},
    {"setCheck", reinterpret_cast<PyCFunction>(Sbk_QtPointFPropertyManagerFunc_setCheck), METH_VARARGS, nullptr},
    {"setMaximum", reinterpret_cast<PyCFunction>(Sbk_QtPointFPropertyManagerFunc_setMaximum), METH_VARARGS, nullptr},
    {"setMinimum", reinterpret_cast<PyCFunction>(Sbk_QtPointFPropertyManagerFunc_setMinimum), METH_VARARGS, nullptr},
    {"setPrecision", reinterpret_cast<PyCFunction>(Sbk_QtPointFPropertyManagerFunc_setPrecision), METH_VARARGS, nullptr},
    {"setRange", reinterpret_cast<PyCFunction>(Sbk_QtPointFPropertyManagerFunc_setRange), METH_VARARGS, nullptr},
    {"setValue", reinterpret_cast<PyCFunction>(Sbk_QtPointFPropertyManagerFunc_setValue), METH_VARARGS, nullptr},
    {"subDoublePropertyManager", reinterpret_cast<PyCFunction>(Sbk_QtPointFPropertyManagerFunc_subDoublePropertyManager), METH_NOARGS, nullptr},
    {"uninitializeProperty", reinterpret_cast<PyCFunction>(Sbk_QtPointFPropertyManagerFunc_uninitializeProperty), METH_O, nullptr},
    {"value", reinterpret_cast<PyCFunction>(Sbk_QtPointFPropertyManagerFunc_value), METH_O, nullptr},
    {"valueText", reinterpret_cast<PyCFunction>(Sbk_QtPointFPropertyManagerFunc_valueText), METH_O, nullptr},

    {nullptr, nullptr, 0, nullptr} // Sentinel
};

static int Sbk_QtPointFPropertyManager_setattro(PyObject *self, PyObject *name, PyObject *value)
{
    PySide::Feature::Select(self);
    if (value && PyCallable_Check(value)) {
        auto plain_inst = reinterpret_cast< ::QtPointFPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPOINTFPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self)));
        auto inst = dynamic_cast<QtPointFPropertyManagerWrapper *>(plain_inst);
        if (inst)
            inst->resetPyMethodCache();
    }
    Shiboken::AutoDecRef pp(reinterpret_cast<PyObject *>(PySide::Property::getObject(self, name)));
    if (!pp.isNull())
        return PySide::Property::setValue(reinterpret_cast<PySideProperty *>(pp.object()), self, value);
    return PyObject_GenericSetAttr(self, name, value);
}

} // extern "C"

static int Sbk_QtPointFPropertyManager_traverse(PyObject *self, visitproc visit, void *arg)
{
    return SbkObject_TypeF()->tp_traverse(self, visit, arg);
}
static int Sbk_QtPointFPropertyManager_clear(PyObject *self)
{
    return reinterpret_cast<PyTypeObject *>(SbkObject_TypeF())->tp_clear(self);
}
// Class Definition -----------------------------------------------
extern "C" {
static PyTypeObject *_Sbk_QtPointFPropertyManager_Type = nullptr;
static PyTypeObject *Sbk_QtPointFPropertyManager_TypeF(void)
{
    return _Sbk_QtPointFPropertyManager_Type;
}

static PyType_Slot Sbk_QtPointFPropertyManager_slots[] = {
    {Py_tp_base,        nullptr}, // inserted by introduceWrapperType
    {Py_tp_dealloc,     reinterpret_cast<void *>(&SbkDeallocWrapper)},
    {Py_tp_repr,        nullptr},
    {Py_tp_hash,        nullptr},
    {Py_tp_call,        nullptr},
    {Py_tp_str,         nullptr},
    {Py_tp_getattro,    nullptr},
    {Py_tp_setattro,    reinterpret_cast<void *>(Sbk_QtPointFPropertyManager_setattro)},
    {Py_tp_traverse,    reinterpret_cast<void *>(Sbk_QtPointFPropertyManager_traverse)},
    {Py_tp_clear,       reinterpret_cast<void *>(Sbk_QtPointFPropertyManager_clear)},
    {Py_tp_richcompare, nullptr},
    {Py_tp_iter,        nullptr},
    {Py_tp_iternext,    nullptr},
    {Py_tp_methods,     reinterpret_cast<void *>(Sbk_QtPointFPropertyManager_methods)},
    {Py_tp_getset,      nullptr},
    {Py_tp_init,        reinterpret_cast<void *>(Sbk_QtPointFPropertyManager_Init)},
    {Py_tp_new,         reinterpret_cast<void *>(SbkObject_tp_new)},
    {0, nullptr}
};
static PyType_Spec Sbk_QtPointFPropertyManager_spec = {
    "1:qtpropertybrowser.QtPointFPropertyManager",
    sizeof(SbkObject),
    0,
    Py_TPFLAGS_DEFAULT|Py_TPFLAGS_BASETYPE|Py_TPFLAGS_HAVE_GC,
    Sbk_QtPointFPropertyManager_slots
};

} //extern "C"

static void *Sbk_QtPointFPropertyManager_typeDiscovery(void *cptr, PyTypeObject *instanceType)
{
    SBK_UNUSED(cptr)
    SBK_UNUSED(instanceType)
    if (instanceType == Shiboken::SbkType< ::QObject >())
        return dynamic_cast< ::QtPointFPropertyManager *>(reinterpret_cast< ::QObject *>(cptr));
    return {};
}


// Type conversion functions.

// Python to C++ pointer conversion - returns the C++ object of the Python wrapper (keeps object identity).
static void QtPointFPropertyManager_PythonToCpp_QtPointFPropertyManager_PTR(PyObject *pyIn, void *cppOut)
{
    Shiboken::Conversions::pythonToCppPointer(Sbk_QtPointFPropertyManager_TypeF(), pyIn, cppOut);
}
static PythonToCppFunc is_QtPointFPropertyManager_PythonToCpp_QtPointFPropertyManager_PTR_Convertible(PyObject *pyIn)
{
    if (pyIn == Py_None)
        return Shiboken::Conversions::nonePythonToCppNullPtr;
    if (PyObject_TypeCheck(pyIn, Sbk_QtPointFPropertyManager_TypeF()))
        return QtPointFPropertyManager_PythonToCpp_QtPointFPropertyManager_PTR;
    return {};
}

// C++ to Python pointer conversion - tries to find the Python wrapper for the C++ object (keeps object identity).
static PyObject *QtPointFPropertyManager_PTR_CppToPython_QtPointFPropertyManager(const void *cppIn)
{
    return PySide::getWrapperForQObject(reinterpret_cast<::QtPointFPropertyManager *>(const_cast<void *>(cppIn)), Sbk_QtPointFPropertyManager_TypeF());

}

// The signatures string for the functions.
// Multiple signatures have their index "n:" in front.
static const char *QtPointFPropertyManager_SignatureStrings[] = {
    "qtpropertybrowser.QtPointFPropertyManager(self,parent:PySide6.QtCore.QObject=0)",
    "qtpropertybrowser.QtPointFPropertyManager.check(self,property:qtpropertybrowser.QtProperty)->bool",
    "qtpropertybrowser.QtPointFPropertyManager.decimals(self,property:qtpropertybrowser.QtProperty)->int",
    "qtpropertybrowser.QtPointFPropertyManager.initializeProperty(self,property:qtpropertybrowser.QtProperty)",
    "qtpropertybrowser.QtPointFPropertyManager.maximum(self,property:qtpropertybrowser.QtProperty)->PySide6.QtCore.QPointF",
    "qtpropertybrowser.QtPointFPropertyManager.minimum(self,property:qtpropertybrowser.QtProperty)->PySide6.QtCore.QPointF",
    "qtpropertybrowser.QtPointFPropertyManager.precision(self,property:qtpropertybrowser.QtProperty)->int",
    "qtpropertybrowser.QtPointFPropertyManager.setCheck(self,property:qtpropertybrowser.QtProperty,check:bool)",
    "qtpropertybrowser.QtPointFPropertyManager.setMaximum(self,property:qtpropertybrowser.QtProperty,maxVal:typing.Union[PySide6.QtCore.QPointF, PySide6.QtCore.QPoint])",
    "qtpropertybrowser.QtPointFPropertyManager.setMinimum(self,property:qtpropertybrowser.QtProperty,minVal:typing.Union[PySide6.QtCore.QPointF, PySide6.QtCore.QPoint])",
    "qtpropertybrowser.QtPointFPropertyManager.setPrecision(self,property:qtpropertybrowser.QtProperty,prec:int)",
    "qtpropertybrowser.QtPointFPropertyManager.setRange(self,property:qtpropertybrowser.QtProperty,minVal:typing.Union[PySide6.QtCore.QPointF, PySide6.QtCore.QPoint],maxVal:typing.Union[PySide6.QtCore.QPointF, PySide6.QtCore.QPoint])",
    "qtpropertybrowser.QtPointFPropertyManager.setValue(self,property:qtpropertybrowser.QtProperty,val:typing.Union[PySide6.QtCore.QPointF, PySide6.QtCore.QPoint])",
    "qtpropertybrowser.QtPointFPropertyManager.subDoublePropertyManager(self)->qtpropertybrowser.QtDoublePropertyManager",
    "qtpropertybrowser.QtPointFPropertyManager.uninitializeProperty(self,property:qtpropertybrowser.QtProperty)",
    "qtpropertybrowser.QtPointFPropertyManager.value(self,property:qtpropertybrowser.QtProperty)->PySide6.QtCore.QPointF",
    "qtpropertybrowser.QtPointFPropertyManager.valueText(self,property:qtpropertybrowser.QtProperty)->QString",
    nullptr}; // Sentinel

void init_QtPointFPropertyManager(PyObject *module)
{
    _Sbk_QtPointFPropertyManager_Type = Shiboken::ObjectType::introduceWrapperType(
        module,
        "QtPointFPropertyManager",
        "QtPointFPropertyManager*",
        &Sbk_QtPointFPropertyManager_spec,
        &Shiboken::callCppDestructor< ::QtPointFPropertyManager >,
        SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYMANAGER_IDX],
        0,
        0);
    auto *pyType = Sbk_QtPointFPropertyManager_TypeF(); // references _Sbk_QtPointFPropertyManager_Type
    InitSignatureStrings(pyType, QtPointFPropertyManager_SignatureStrings);
    SbkObjectType_SetPropertyStrings(pyType, Sbk_QtPointFPropertyManager_PropertyStrings);
    SbkqtpropertybrowserTypes[SBK_QTPOINTFPROPERTYMANAGER_IDX] = pyType;

    // Register Converter
    SbkConverter *converter = Shiboken::Conversions::createConverter(pyType,
        QtPointFPropertyManager_PythonToCpp_QtPointFPropertyManager_PTR,
        is_QtPointFPropertyManager_PythonToCpp_QtPointFPropertyManager_PTR_Convertible,
        QtPointFPropertyManager_PTR_CppToPython_QtPointFPropertyManager);

    Shiboken::Conversions::registerConverterName(converter, "QtPointFPropertyManager");
    Shiboken::Conversions::registerConverterName(converter, "QtPointFPropertyManager*");
    Shiboken::Conversions::registerConverterName(converter, "QtPointFPropertyManager&");
    Shiboken::Conversions::registerConverterName(converter, typeid(::QtPointFPropertyManager).name());
    Shiboken::Conversions::registerConverterName(converter, typeid(::QtPointFPropertyManagerWrapper).name());


    Shiboken::ObjectType::setTypeDiscoveryFunctionV2(Sbk_QtPointFPropertyManager_TypeF(), &Sbk_QtPointFPropertyManager_typeDiscovery);

    PySide::Signal::registerSignals(pyType, &::QtPointFPropertyManager::staticMetaObject);
    QtPointFPropertyManagerWrapper::pysideInitQtMetaTypes();
    Shiboken::ObjectType::setSubTypeInitHook(pyType, &PySide::initQObjectSubType);
    PySide::initDynamicMetaObject(pyType, &::QtPointFPropertyManager::staticMetaObject, sizeof(QtPointFPropertyManagerWrapper));
}
