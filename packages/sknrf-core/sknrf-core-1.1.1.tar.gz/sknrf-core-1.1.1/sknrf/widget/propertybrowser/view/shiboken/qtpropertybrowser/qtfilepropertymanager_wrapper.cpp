
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
#include "qtfilepropertymanager_wrapper.h"

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

void QtFilePropertyManagerWrapper::pysideInitQtMetaTypes()
{
}

void QtFilePropertyManagerWrapper::resetPyMethodCache()
{
    std::fill_n(m_PyMethodCache, sizeof(m_PyMethodCache) / sizeof(m_PyMethodCache[0]), false);
}

QtFilePropertyManagerWrapper::QtFilePropertyManagerWrapper(QObject * parent) : QtFilePropertyManager(parent)
{
    resetPyMethodCache();
    // ... middle
}

bool QtFilePropertyManagerWrapper::check(const QtProperty * property) const
{
    if (m_PyMethodCache[0])
        return this->::QtFilePropertyManager::check(property);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return false;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "check";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[0] = true;
        gil.release();
        return this->::QtFilePropertyManager::check(property);
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
        Shiboken::Warnings::warnInvalidReturnValue("QtFilePropertyManager", "check", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QIcon QtFilePropertyManagerWrapper::checkIcon(const QtProperty * property) const
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
        Shiboken::Warnings::warnInvalidReturnValue("QtFilePropertyManager", "checkIcon", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QIcon >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return {};
    }
    ::QIcon cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtFilePropertyManagerWrapper::childEvent(QChildEvent * event)
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

void QtFilePropertyManagerWrapper::connectNotify(const QMetaMethod & signal)
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

QtProperty * QtFilePropertyManagerWrapper::createProperty()
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
        Shiboken::Warnings::warnInvalidReturnValue("QtFilePropertyManager", "createProperty", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QtProperty >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return nullptr;
    }
    ::QtProperty *cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtFilePropertyManagerWrapper::customEvent(QEvent * event)
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

void QtFilePropertyManagerWrapper::disconnectNotify(const QMetaMethod & signal)
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

QString QtFilePropertyManagerWrapper::displayText(const QtProperty * property) const
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
        Shiboken::Warnings::warnInvalidReturnValue("QtFilePropertyManager", "displayText", "QString", Py_TYPE(pyResult)->tp_name);
        return ::QString();
    }
    ::QString cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

bool QtFilePropertyManagerWrapper::event(QEvent * event)
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
        Shiboken::Warnings::warnInvalidReturnValue("QtFilePropertyManager", "event", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

bool QtFilePropertyManagerWrapper::eventFilter(QObject * watched, QEvent * event)
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
        Shiboken::Warnings::warnInvalidReturnValue("QtFilePropertyManager", "eventFilter", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QBrush QtFilePropertyManagerWrapper::foreground(const QtProperty * property) const
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
        Shiboken::Warnings::warnInvalidReturnValue("QtFilePropertyManager", "foreground", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QBrush >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return {};
    }
    ::QBrush cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QString QtFilePropertyManagerWrapper::formatText(const QtProperty * property) const
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
        Shiboken::Warnings::warnInvalidReturnValue("QtFilePropertyManager", "formatText", "QString", Py_TYPE(pyResult)->tp_name);
        return ::QString();
    }
    ::QString cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

bool QtFilePropertyManagerWrapper::hasValue(const QtProperty * property) const
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
        Shiboken::Warnings::warnInvalidReturnValue("QtFilePropertyManager", "hasValue", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtFilePropertyManagerWrapper::initializeProperty(QtProperty * property)
{
    if (m_PyMethodCache[13]) {
        return this->::QtFilePropertyManager::initializeProperty(property);
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
        return this->::QtFilePropertyManager::initializeProperty(property);
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

bool QtFilePropertyManagerWrapper::isReadOnly(const QtProperty * property) const
{
    if (m_PyMethodCache[14])
        return this->::QtFilePropertyManager::isReadOnly(property);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return false;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "isReadOnly";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[14] = true;
        gil.release();
        return this->::QtFilePropertyManager::isReadOnly(property);
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
        Shiboken::Warnings::warnInvalidReturnValue("QtFilePropertyManager", "isReadOnly", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QString QtFilePropertyManagerWrapper::maximumText(const QtProperty * property) const
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
        Shiboken::Warnings::warnInvalidReturnValue("QtFilePropertyManager", "maximumText", "QString", Py_TYPE(pyResult)->tp_name);
        return ::QString();
    }
    ::QString cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QString QtFilePropertyManagerWrapper::minimumText(const QtProperty * property) const
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
        Shiboken::Warnings::warnInvalidReturnValue("QtFilePropertyManager", "minimumText", "QString", Py_TYPE(pyResult)->tp_name);
        return ::QString();
    }
    ::QString cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QString QtFilePropertyManagerWrapper::pkAvgText(const QtProperty * property) const
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
        Shiboken::Warnings::warnInvalidReturnValue("QtFilePropertyManager", "pkAvgText", "QString", Py_TYPE(pyResult)->tp_name);
        return ::QString();
    }
    ::QString cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtFilePropertyManagerWrapper::setCheck(QtProperty * property, bool check)
{
    if (m_PyMethodCache[18]) {
        return this->::QtFilePropertyManager::setCheck(property, check);
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
        return this->::QtFilePropertyManager::setCheck(property, check);
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

void QtFilePropertyManagerWrapper::timerEvent(QTimerEvent * event)
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

void QtFilePropertyManagerWrapper::uninitializeProperty(QtProperty * property)
{
    if (m_PyMethodCache[20]) {
        return this->::QtFilePropertyManager::uninitializeProperty(property);
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
        return this->::QtFilePropertyManager::uninitializeProperty(property);
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

QString QtFilePropertyManagerWrapper::unitText(const QtProperty * property) const
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
        Shiboken::Warnings::warnInvalidReturnValue("QtFilePropertyManager", "unitText", "QString", Py_TYPE(pyResult)->tp_name);
        return ::QString();
    }
    ::QString cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QIcon QtFilePropertyManagerWrapper::valueIcon(const QtProperty * property) const
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
        Shiboken::Warnings::warnInvalidReturnValue("QtFilePropertyManager", "valueIcon", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QIcon >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return {};
    }
    ::QIcon cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QString QtFilePropertyManagerWrapper::valueText(const QtProperty * property) const
{
    if (m_PyMethodCache[23])
        return this->::QtFilePropertyManager::valueText(property);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return ::QString();
    static PyObject *nameCache[2] = {};
    static const char *funcName = "valueText";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[23] = true;
        gil.release();
        return this->::QtFilePropertyManager::valueText(property);
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
        Shiboken::Warnings::warnInvalidReturnValue("QtFilePropertyManager", "valueText", "QString", Py_TYPE(pyResult)->tp_name);
        return ::QString();
    }
    ::QString cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

const QMetaObject *QtFilePropertyManagerWrapper::metaObject() const
{
    if (QObject::d_ptr->metaObject)
        return QObject::d_ptr->dynamicMetaObject();
    SbkObject *pySelf = Shiboken::BindingManager::instance().retrieveWrapper(this);
    if (pySelf == nullptr)
        return QtFilePropertyManager::metaObject();
    return PySide::SignalManager::retrieveMetaObject(reinterpret_cast<PyObject *>(pySelf));
}

int QtFilePropertyManagerWrapper::qt_metacall(QMetaObject::Call call, int id, void **args)
{
    int result = QtFilePropertyManager::qt_metacall(call, id, args);
    return result < 0 ? result : PySide::SignalManager::qt_metacall(this, call, id, args);
}

void *QtFilePropertyManagerWrapper::qt_metacast(const char *_clname)
{
    if (!_clname)
        return {};
    SbkObject *pySelf = Shiboken::BindingManager::instance().retrieveWrapper(this);
    if (pySelf && PySide::inherits(Py_TYPE(pySelf), _clname))
        return static_cast<void *>(const_cast< QtFilePropertyManagerWrapper *>(this));
    return QtFilePropertyManager::qt_metacast(_clname);
}

QtFilePropertyManagerWrapper::~QtFilePropertyManagerWrapper()
{
    SbkObject *wrapper = Shiboken::BindingManager::instance().retrieveWrapper(this);
    Shiboken::Object::destroy(wrapper, this);
}

// Target ---------------------------------------------------------

extern "C" {
static int
Sbk_QtFilePropertyManager_Init(PyObject *self, PyObject *args, PyObject *kwds)
{
    SBK_UNUSED(kwds)
    const QMetaObject *metaObject;
    SbkObject *sbkSelf = reinterpret_cast<SbkObject *>(self);
    PySide::Feature::Select(self);
    if (Shiboken::Object::isUserType(self) && !Shiboken::ObjectType::canCallConstructor(self->ob_type, Shiboken::SbkType< ::QtFilePropertyManager >()))
        return -1;

    ::QtFilePropertyManagerWrapper *cptr{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtFilePropertyManager.__init__";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp[1];
    SBK_UNUSED(pythonToCpp)
    const Py_ssize_t numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {nullptr};

    // invalid argument lengths

    if (!PyArg_ParseTuple(args, "|O:QtFilePropertyManager", &(pyArgs[0])))
        return -1;


    // Overloaded function decisor
    // 0: QtFilePropertyManager::QtFilePropertyManager(QObject*)
    if (numArgs == 0) {
        overloadId = 0; // QtFilePropertyManager(QObject*)
    } else if (numArgs >= 1
        && (pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkPySide6_QtCoreTypes[SBK_QOBJECT_IDX], (pyArgs[0])))) {
        overloadId = 0; // QtFilePropertyManager(QObject*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtFilePropertyManager_Init_TypeError;

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
                    goto Sbk_QtFilePropertyManager_Init_TypeError;
                }
                if (value) {
                    pyArgs[0] = value;
                    if (!(pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkPySide6_QtCoreTypes[SBK_QOBJECT_IDX], (pyArgs[0]))))
                        goto Sbk_QtFilePropertyManager_Init_TypeError;
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
            // QtFilePropertyManager(QObject*)
            void *addr = PySide::nextQObjectMemoryAddr();
            if (addr) {
                cptr = new (addr) ::QtFilePropertyManagerWrapper(cppArg0);
                PySide::setNextQObjectMemoryAddr(nullptr);
            } else {
                cptr = new ::QtFilePropertyManagerWrapper(cppArg0);
            }

            // Ownership transferences (constructor heuristics).
            Shiboken::Object::setParent(pyArgs[0], self);
        }
    }

    if (PyErr_Occurred() || !Shiboken::Object::setCppPointer(sbkSelf, Shiboken::SbkType< ::QtFilePropertyManager >(), cptr)) {
        delete cptr;
        return -1;
    }
    if (!cptr) goto Sbk_QtFilePropertyManager_Init_TypeError;

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
            goto Sbk_QtFilePropertyManager_Init_TypeError;
    };


    return 1;

    Sbk_QtFilePropertyManager_Init_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return -1;
}

static PyObject *Sbk_QtFilePropertyManagerFunc_check(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtFilePropertyManagerWrapper *>(reinterpret_cast< ::QtFilePropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTFILEPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtFilePropertyManager.check";
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
    if (overloadId == -1) goto Sbk_QtFilePropertyManagerFunc_check_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // check(const QtProperty*)const
            bool cppResult = Shiboken::Object::hasCppWrapper(reinterpret_cast<SbkObject *>(self))
                ? const_cast<const ::QtFilePropertyManagerWrapper *>(cppSelf)->::QtFilePropertyManager::check(cppArg0)
                : const_cast<const ::QtFilePropertyManagerWrapper *>(cppSelf)->check(cppArg0);
            pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtFilePropertyManagerFunc_check_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtFilePropertyManagerFunc_fileMode(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtFilePropertyManagerWrapper *>(reinterpret_cast< ::QtFilePropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTFILEPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtFilePropertyManager.fileMode";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtFilePropertyManager::fileMode(const QtProperty*)const->QFileDialog::FileMode
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArg)))) {
        overloadId = 0; // fileMode(const QtProperty*)const
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtFilePropertyManagerFunc_fileMode_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // fileMode(const QtProperty*)const
            QFileDialog::FileMode cppResult = QFileDialog::FileMode(const_cast<const ::QtFilePropertyManagerWrapper *>(cppSelf)->fileMode(cppArg0));
            pyResult = Shiboken::Conversions::copyToPython(PepType_SETP(reinterpret_cast<SbkEnumType *>(SbkPySide6_QtWidgetsTypes[SBK_QFILEDIALOG_FILEMODE_IDX]))->converter, &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtFilePropertyManagerFunc_fileMode_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtFilePropertyManagerFunc_filter(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtFilePropertyManagerWrapper *>(reinterpret_cast< ::QtFilePropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTFILEPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtFilePropertyManager.filter";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtFilePropertyManager::filter(const QtProperty*)const->QString
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArg)))) {
        overloadId = 0; // filter(const QtProperty*)const
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtFilePropertyManagerFunc_filter_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // filter(const QtProperty*)const
            QString cppResult = const_cast<const ::QtFilePropertyManagerWrapper *>(cppSelf)->filter(cppArg0);
            pyResult = Shiboken::Conversions::copyToPython(SbkPySide6_QtCoreTypeConverters[SBK_QSTRING_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtFilePropertyManagerFunc_filter_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtFilePropertyManagerFunc_initializeProperty(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtFilePropertyManagerWrapper *>(reinterpret_cast< ::QtFilePropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTFILEPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtFilePropertyManager.initializeProperty";
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
    if (overloadId == -1) goto Sbk_QtFilePropertyManagerFunc_initializeProperty_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // initializeProperty(QtProperty*)
            static_cast<::QtFilePropertyManagerWrapper *>(cppSelf)->QtFilePropertyManagerWrapper::initializeProperty_protected(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtFilePropertyManagerFunc_initializeProperty_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtFilePropertyManagerFunc_isReadOnly(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtFilePropertyManagerWrapper *>(reinterpret_cast< ::QtFilePropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTFILEPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtFilePropertyManager.isReadOnly";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtAbstractPropertyManager::isReadOnly(const QtProperty*)const->bool
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArg)))) {
        overloadId = 0; // isReadOnly(const QtProperty*)const
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtFilePropertyManagerFunc_isReadOnly_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // isReadOnly(const QtProperty*)const
            bool cppResult = Shiboken::Object::hasCppWrapper(reinterpret_cast<SbkObject *>(self))
                ? const_cast<const ::QtFilePropertyManagerWrapper *>(cppSelf)->::QtFilePropertyManager::isReadOnly(cppArg0)
                : const_cast<const ::QtFilePropertyManagerWrapper *>(cppSelf)->isReadOnly(cppArg0);
            pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtFilePropertyManagerFunc_isReadOnly_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtFilePropertyManagerFunc_setCheck(PyObject *self, PyObject *args)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtFilePropertyManagerWrapper *>(reinterpret_cast< ::QtFilePropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTFILEPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtFilePropertyManager.setCheck";
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
    if (overloadId == -1) goto Sbk_QtFilePropertyManagerFunc_setCheck_TypeError;

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
                ? cppSelf->::QtFilePropertyManager::setCheck(cppArg0, cppArg1)
                : cppSelf->setCheck(cppArg0, cppArg1);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtFilePropertyManagerFunc_setCheck_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtFilePropertyManagerFunc_setFileMode(PyObject *self, PyObject *args)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtFilePropertyManagerWrapper *>(reinterpret_cast< ::QtFilePropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTFILEPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtFilePropertyManager.setFileMode";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp[2];
    SBK_UNUSED(pythonToCpp)
    const Py_ssize_t numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {nullptr, nullptr};

    // invalid argument lengths

    if (!PyArg_UnpackTuple(args, "setFileMode", 2, 2, &(pyArgs[0]), &(pyArgs[1])))
        return {};


    // Overloaded function decisor
    // 0: QtFilePropertyManager::setFileMode(QtProperty*,QFileDialog::FileMode)
    if (numArgs == 2
        && (pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::pythonToCppConversion(PepType_SETP(reinterpret_cast<SbkEnumType *>(SbkPySide6_QtWidgetsTypes[SBK_QFILEDIALOG_FILEMODE_IDX]))->converter, (pyArgs[1])))) {
        overloadId = 0; // setFileMode(QtProperty*,QFileDialog::FileMode)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtFilePropertyManagerFunc_setFileMode_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp[0](pyArgs[0], &cppArg0);
        ::QFileDialog::FileMode cppArg1{QFileDialog::AnyFile};
        pythonToCpp[1](pyArgs[1], &cppArg1);

        if (!PyErr_Occurred()) {
            // setFileMode(QtProperty*,QFileDialog::FileMode)
            cppSelf->setFileMode(cppArg0, cppArg1);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtFilePropertyManagerFunc_setFileMode_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtFilePropertyManagerFunc_setFilter(PyObject *self, PyObject *args)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtFilePropertyManagerWrapper *>(reinterpret_cast< ::QtFilePropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTFILEPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtFilePropertyManager.setFilter";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp[2];
    SBK_UNUSED(pythonToCpp)
    const Py_ssize_t numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {nullptr, nullptr};

    // invalid argument lengths

    if (!PyArg_UnpackTuple(args, "setFilter", 2, 2, &(pyArgs[0]), &(pyArgs[1])))
        return {};


    // Overloaded function decisor
    // 0: QtFilePropertyManager::setFilter(QtProperty*,QString)
    if (numArgs == 2
        && (pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::pythonToCppConversion(SbkPySide6_QtCoreTypeConverters[SBK_QSTRING_IDX], (pyArgs[1])))) {
        overloadId = 0; // setFilter(QtProperty*,QString)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtFilePropertyManagerFunc_setFilter_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp[0](pyArgs[0], &cppArg0);
        ::QString cppArg1;
        pythonToCpp[1](pyArgs[1], &cppArg1);

        if (!PyErr_Occurred()) {
            // setFilter(QtProperty*,QString)
            cppSelf->setFilter(cppArg0, cppArg1);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtFilePropertyManagerFunc_setFilter_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtFilePropertyManagerFunc_setReadOnly(PyObject *self, PyObject *args)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtFilePropertyManagerWrapper *>(reinterpret_cast< ::QtFilePropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTFILEPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtFilePropertyManager.setReadOnly";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp[2];
    SBK_UNUSED(pythonToCpp)
    const Py_ssize_t numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {nullptr, nullptr};

    // invalid argument lengths

    if (!PyArg_UnpackTuple(args, "setReadOnly", 2, 2, &(pyArgs[0]), &(pyArgs[1])))
        return {};


    // Overloaded function decisor
    // 0: QtFilePropertyManager::setReadOnly(QtProperty*,bool)
    if (numArgs == 2
        && (pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::pythonToCppConversion(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), (pyArgs[1])))) {
        overloadId = 0; // setReadOnly(QtProperty*,bool)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtFilePropertyManagerFunc_setReadOnly_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp[0](pyArgs[0], &cppArg0);
        bool cppArg1;
        pythonToCpp[1](pyArgs[1], &cppArg1);

        if (!PyErr_Occurred()) {
            // setReadOnly(QtProperty*,bool)
            cppSelf->setReadOnly(cppArg0, cppArg1);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtFilePropertyManagerFunc_setReadOnly_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtFilePropertyManagerFunc_setValue(PyObject *self, PyObject *args)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtFilePropertyManagerWrapper *>(reinterpret_cast< ::QtFilePropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTFILEPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtFilePropertyManager.setValue";
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
    // 0: QtFilePropertyManager::setValue(QtProperty*,QString)
    if (numArgs == 2
        && (pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::pythonToCppConversion(SbkPySide6_QtCoreTypeConverters[SBK_QSTRING_IDX], (pyArgs[1])))) {
        overloadId = 0; // setValue(QtProperty*,QString)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtFilePropertyManagerFunc_setValue_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp[0](pyArgs[0], &cppArg0);
        ::QString cppArg1;
        pythonToCpp[1](pyArgs[1], &cppArg1);

        if (!PyErr_Occurred()) {
            // setValue(QtProperty*,QString)
            cppSelf->setValue(cppArg0, cppArg1);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtFilePropertyManagerFunc_setValue_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtFilePropertyManagerFunc_uninitializeProperty(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtFilePropertyManagerWrapper *>(reinterpret_cast< ::QtFilePropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTFILEPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtFilePropertyManager.uninitializeProperty";
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
    if (overloadId == -1) goto Sbk_QtFilePropertyManagerFunc_uninitializeProperty_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // uninitializeProperty(QtProperty*)
            static_cast<::QtFilePropertyManagerWrapper *>(cppSelf)->QtFilePropertyManagerWrapper::uninitializeProperty_protected(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtFilePropertyManagerFunc_uninitializeProperty_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtFilePropertyManagerFunc_value(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtFilePropertyManagerWrapper *>(reinterpret_cast< ::QtFilePropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTFILEPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtFilePropertyManager.value";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtFilePropertyManager::value(const QtProperty*)const->QString
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArg)))) {
        overloadId = 0; // value(const QtProperty*)const
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtFilePropertyManagerFunc_value_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // value(const QtProperty*)const
            QString cppResult = const_cast<const ::QtFilePropertyManagerWrapper *>(cppSelf)->value(cppArg0);
            pyResult = Shiboken::Conversions::copyToPython(SbkPySide6_QtCoreTypeConverters[SBK_QSTRING_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtFilePropertyManagerFunc_value_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtFilePropertyManagerFunc_valueText(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtFilePropertyManagerWrapper *>(reinterpret_cast< ::QtFilePropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTFILEPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtFilePropertyManager.valueText";
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
    if (overloadId == -1) goto Sbk_QtFilePropertyManagerFunc_valueText_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // valueText(const QtProperty*)const
            QString cppResult = static_cast<::QtFilePropertyManagerWrapper *>(cppSelf)->QtFilePropertyManagerWrapper::valueText_protected(cppArg0);
            pyResult = Shiboken::Conversions::copyToPython(SbkPySide6_QtCoreTypeConverters[SBK_QSTRING_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtFilePropertyManagerFunc_valueText_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}


static const char *Sbk_QtFilePropertyManager_PropertyStrings[] = {
    nullptr // Sentinel
};

static PyMethodDef Sbk_QtFilePropertyManager_methods[] = {
    {"check", reinterpret_cast<PyCFunction>(Sbk_QtFilePropertyManagerFunc_check), METH_O, nullptr},
    {"fileMode", reinterpret_cast<PyCFunction>(Sbk_QtFilePropertyManagerFunc_fileMode), METH_O, nullptr},
    {"filter", reinterpret_cast<PyCFunction>(Sbk_QtFilePropertyManagerFunc_filter), METH_O, nullptr},
    {"initializeProperty", reinterpret_cast<PyCFunction>(Sbk_QtFilePropertyManagerFunc_initializeProperty), METH_O, nullptr},
    {"isReadOnly", reinterpret_cast<PyCFunction>(Sbk_QtFilePropertyManagerFunc_isReadOnly), METH_O, nullptr},
    {"setCheck", reinterpret_cast<PyCFunction>(Sbk_QtFilePropertyManagerFunc_setCheck), METH_VARARGS, nullptr},
    {"setFileMode", reinterpret_cast<PyCFunction>(Sbk_QtFilePropertyManagerFunc_setFileMode), METH_VARARGS, nullptr},
    {"setFilter", reinterpret_cast<PyCFunction>(Sbk_QtFilePropertyManagerFunc_setFilter), METH_VARARGS, nullptr},
    {"setReadOnly", reinterpret_cast<PyCFunction>(Sbk_QtFilePropertyManagerFunc_setReadOnly), METH_VARARGS, nullptr},
    {"setValue", reinterpret_cast<PyCFunction>(Sbk_QtFilePropertyManagerFunc_setValue), METH_VARARGS, nullptr},
    {"uninitializeProperty", reinterpret_cast<PyCFunction>(Sbk_QtFilePropertyManagerFunc_uninitializeProperty), METH_O, nullptr},
    {"value", reinterpret_cast<PyCFunction>(Sbk_QtFilePropertyManagerFunc_value), METH_O, nullptr},
    {"valueText", reinterpret_cast<PyCFunction>(Sbk_QtFilePropertyManagerFunc_valueText), METH_O, nullptr},

    {nullptr, nullptr, 0, nullptr} // Sentinel
};

static int Sbk_QtFilePropertyManager_setattro(PyObject *self, PyObject *name, PyObject *value)
{
    PySide::Feature::Select(self);
    if (value && PyCallable_Check(value)) {
        auto plain_inst = reinterpret_cast< ::QtFilePropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTFILEPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self)));
        auto inst = dynamic_cast<QtFilePropertyManagerWrapper *>(plain_inst);
        if (inst)
            inst->resetPyMethodCache();
    }
    Shiboken::AutoDecRef pp(reinterpret_cast<PyObject *>(PySide::Property::getObject(self, name)));
    if (!pp.isNull())
        return PySide::Property::setValue(reinterpret_cast<PySideProperty *>(pp.object()), self, value);
    return PyObject_GenericSetAttr(self, name, value);
}

} // extern "C"

static int Sbk_QtFilePropertyManager_traverse(PyObject *self, visitproc visit, void *arg)
{
    return SbkObject_TypeF()->tp_traverse(self, visit, arg);
}
static int Sbk_QtFilePropertyManager_clear(PyObject *self)
{
    return reinterpret_cast<PyTypeObject *>(SbkObject_TypeF())->tp_clear(self);
}
// Class Definition -----------------------------------------------
extern "C" {
static PyTypeObject *_Sbk_QtFilePropertyManager_Type = nullptr;
static PyTypeObject *Sbk_QtFilePropertyManager_TypeF(void)
{
    return _Sbk_QtFilePropertyManager_Type;
}

static PyType_Slot Sbk_QtFilePropertyManager_slots[] = {
    {Py_tp_base,        nullptr}, // inserted by introduceWrapperType
    {Py_tp_dealloc,     reinterpret_cast<void *>(&SbkDeallocWrapper)},
    {Py_tp_repr,        nullptr},
    {Py_tp_hash,        nullptr},
    {Py_tp_call,        nullptr},
    {Py_tp_str,         nullptr},
    {Py_tp_getattro,    nullptr},
    {Py_tp_setattro,    reinterpret_cast<void *>(Sbk_QtFilePropertyManager_setattro)},
    {Py_tp_traverse,    reinterpret_cast<void *>(Sbk_QtFilePropertyManager_traverse)},
    {Py_tp_clear,       reinterpret_cast<void *>(Sbk_QtFilePropertyManager_clear)},
    {Py_tp_richcompare, nullptr},
    {Py_tp_iter,        nullptr},
    {Py_tp_iternext,    nullptr},
    {Py_tp_methods,     reinterpret_cast<void *>(Sbk_QtFilePropertyManager_methods)},
    {Py_tp_getset,      nullptr},
    {Py_tp_init,        reinterpret_cast<void *>(Sbk_QtFilePropertyManager_Init)},
    {Py_tp_new,         reinterpret_cast<void *>(SbkObject_tp_new)},
    {0, nullptr}
};
static PyType_Spec Sbk_QtFilePropertyManager_spec = {
    "1:qtpropertybrowser.QtFilePropertyManager",
    sizeof(SbkObject),
    0,
    Py_TPFLAGS_DEFAULT|Py_TPFLAGS_BASETYPE|Py_TPFLAGS_HAVE_GC,
    Sbk_QtFilePropertyManager_slots
};

} //extern "C"

static void *Sbk_QtFilePropertyManager_typeDiscovery(void *cptr, PyTypeObject *instanceType)
{
    SBK_UNUSED(cptr)
    SBK_UNUSED(instanceType)
    if (instanceType == Shiboken::SbkType< ::QObject >())
        return dynamic_cast< ::QtFilePropertyManager *>(reinterpret_cast< ::QObject *>(cptr));
    return {};
}


// Type conversion functions.

// Python to C++ pointer conversion - returns the C++ object of the Python wrapper (keeps object identity).
static void QtFilePropertyManager_PythonToCpp_QtFilePropertyManager_PTR(PyObject *pyIn, void *cppOut)
{
    Shiboken::Conversions::pythonToCppPointer(Sbk_QtFilePropertyManager_TypeF(), pyIn, cppOut);
}
static PythonToCppFunc is_QtFilePropertyManager_PythonToCpp_QtFilePropertyManager_PTR_Convertible(PyObject *pyIn)
{
    if (pyIn == Py_None)
        return Shiboken::Conversions::nonePythonToCppNullPtr;
    if (PyObject_TypeCheck(pyIn, Sbk_QtFilePropertyManager_TypeF()))
        return QtFilePropertyManager_PythonToCpp_QtFilePropertyManager_PTR;
    return {};
}

// C++ to Python pointer conversion - tries to find the Python wrapper for the C++ object (keeps object identity).
static PyObject *QtFilePropertyManager_PTR_CppToPython_QtFilePropertyManager(const void *cppIn)
{
    return PySide::getWrapperForQObject(reinterpret_cast<::QtFilePropertyManager *>(const_cast<void *>(cppIn)), Sbk_QtFilePropertyManager_TypeF());

}

// The signatures string for the functions.
// Multiple signatures have their index "n:" in front.
static const char *QtFilePropertyManager_SignatureStrings[] = {
    "qtpropertybrowser.QtFilePropertyManager(self,parent:PySide6.QtCore.QObject=0)",
    "qtpropertybrowser.QtFilePropertyManager.check(self,property:qtpropertybrowser.QtProperty)->bool",
    "qtpropertybrowser.QtFilePropertyManager.fileMode(self,property:qtpropertybrowser.QtProperty)->PySide6.QtWidgets.QFileDialog.FileMode",
    "qtpropertybrowser.QtFilePropertyManager.filter(self,property:qtpropertybrowser.QtProperty)->QString",
    "qtpropertybrowser.QtFilePropertyManager.initializeProperty(self,property:qtpropertybrowser.QtProperty)",
    "qtpropertybrowser.QtFilePropertyManager.isReadOnly(self,property:qtpropertybrowser.QtProperty)->bool",
    "qtpropertybrowser.QtFilePropertyManager.setCheck(self,property:qtpropertybrowser.QtProperty,check:bool)",
    "qtpropertybrowser.QtFilePropertyManager.setFileMode(self,arg__1:qtpropertybrowser.QtProperty,mode:PySide6.QtWidgets.QFileDialog.FileMode)",
    "qtpropertybrowser.QtFilePropertyManager.setFilter(self,arg__1:qtpropertybrowser.QtProperty,arg__2:QString)",
    "qtpropertybrowser.QtFilePropertyManager.setReadOnly(self,property:qtpropertybrowser.QtProperty,readOnly:bool)",
    "qtpropertybrowser.QtFilePropertyManager.setValue(self,arg__1:qtpropertybrowser.QtProperty,arg__2:QString)",
    "qtpropertybrowser.QtFilePropertyManager.uninitializeProperty(self,property:qtpropertybrowser.QtProperty)",
    "qtpropertybrowser.QtFilePropertyManager.value(self,property:qtpropertybrowser.QtProperty)->QString",
    "qtpropertybrowser.QtFilePropertyManager.valueText(self,property:qtpropertybrowser.QtProperty)->QString",
    nullptr}; // Sentinel

void init_QtFilePropertyManager(PyObject *module)
{
    _Sbk_QtFilePropertyManager_Type = Shiboken::ObjectType::introduceWrapperType(
        module,
        "QtFilePropertyManager",
        "QtFilePropertyManager*",
        &Sbk_QtFilePropertyManager_spec,
        &Shiboken::callCppDestructor< ::QtFilePropertyManager >,
        SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYMANAGER_IDX],
        0,
        0);
    auto *pyType = Sbk_QtFilePropertyManager_TypeF(); // references _Sbk_QtFilePropertyManager_Type
    InitSignatureStrings(pyType, QtFilePropertyManager_SignatureStrings);
    SbkObjectType_SetPropertyStrings(pyType, Sbk_QtFilePropertyManager_PropertyStrings);
    SbkqtpropertybrowserTypes[SBK_QTFILEPROPERTYMANAGER_IDX] = pyType;

    // Register Converter
    SbkConverter *converter = Shiboken::Conversions::createConverter(pyType,
        QtFilePropertyManager_PythonToCpp_QtFilePropertyManager_PTR,
        is_QtFilePropertyManager_PythonToCpp_QtFilePropertyManager_PTR_Convertible,
        QtFilePropertyManager_PTR_CppToPython_QtFilePropertyManager);

    Shiboken::Conversions::registerConverterName(converter, "QtFilePropertyManager");
    Shiboken::Conversions::registerConverterName(converter, "QtFilePropertyManager*");
    Shiboken::Conversions::registerConverterName(converter, "QtFilePropertyManager&");
    Shiboken::Conversions::registerConverterName(converter, typeid(::QtFilePropertyManager).name());
    Shiboken::Conversions::registerConverterName(converter, typeid(::QtFilePropertyManagerWrapper).name());


    Shiboken::ObjectType::setTypeDiscoveryFunctionV2(Sbk_QtFilePropertyManager_TypeF(), &Sbk_QtFilePropertyManager_typeDiscovery);

    PySide::Signal::registerSignals(pyType, &::QtFilePropertyManager::staticMetaObject);
    QtFilePropertyManagerWrapper::pysideInitQtMetaTypes();
    Shiboken::ObjectType::setSubTypeInitHook(pyType, &PySide::initQObjectSubType);
    PySide::initDynamicMetaObject(pyType, &::QtFilePropertyManager::staticMetaObject, sizeof(QtFilePropertyManagerWrapper));
}
