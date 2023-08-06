
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
#include "qtstringpropertymanager_wrapper.h"

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

void QtStringPropertyManagerWrapper::pysideInitQtMetaTypes()
{
}

void QtStringPropertyManagerWrapper::resetPyMethodCache()
{
    std::fill_n(m_PyMethodCache, sizeof(m_PyMethodCache) / sizeof(m_PyMethodCache[0]), false);
}

QtStringPropertyManagerWrapper::QtStringPropertyManagerWrapper(QObject * parent) : QtStringPropertyManager(parent)
{
    resetPyMethodCache();
    // ... middle
}

bool QtStringPropertyManagerWrapper::check(const QtProperty * property) const
{
    if (m_PyMethodCache[0])
        return this->::QtStringPropertyManager::check(property);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return false;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "check";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[0] = true;
        gil.release();
        return this->::QtStringPropertyManager::check(property);
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
        Shiboken::Warnings::warnInvalidReturnValue("QtStringPropertyManager", "check", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QIcon QtStringPropertyManagerWrapper::checkIcon(const QtProperty * property) const
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
        Shiboken::Warnings::warnInvalidReturnValue("QtStringPropertyManager", "checkIcon", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QIcon >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return {};
    }
    ::QIcon cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtStringPropertyManagerWrapper::childEvent(QChildEvent * event)
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

void QtStringPropertyManagerWrapper::connectNotify(const QMetaMethod & signal)
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

QtProperty * QtStringPropertyManagerWrapper::createProperty()
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
        Shiboken::Warnings::warnInvalidReturnValue("QtStringPropertyManager", "createProperty", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QtProperty >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return nullptr;
    }
    ::QtProperty *cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtStringPropertyManagerWrapper::customEvent(QEvent * event)
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

void QtStringPropertyManagerWrapper::disconnectNotify(const QMetaMethod & signal)
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

QString QtStringPropertyManagerWrapper::displayText(const QtProperty * property) const
{
    if (m_PyMethodCache[7])
        return this->::QtStringPropertyManager::displayText(property);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return ::QString();
    static PyObject *nameCache[2] = {};
    static const char *funcName = "displayText";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[7] = true;
        gil.release();
        return this->::QtStringPropertyManager::displayText(property);
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
        Shiboken::Warnings::warnInvalidReturnValue("QtStringPropertyManager", "displayText", "QString", Py_TYPE(pyResult)->tp_name);
        return ::QString();
    }
    ::QString cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

bool QtStringPropertyManagerWrapper::event(QEvent * event)
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
        Shiboken::Warnings::warnInvalidReturnValue("QtStringPropertyManager", "event", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

bool QtStringPropertyManagerWrapper::eventFilter(QObject * watched, QEvent * event)
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
        Shiboken::Warnings::warnInvalidReturnValue("QtStringPropertyManager", "eventFilter", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QBrush QtStringPropertyManagerWrapper::foreground(const QtProperty * property) const
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
        Shiboken::Warnings::warnInvalidReturnValue("QtStringPropertyManager", "foreground", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QBrush >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return {};
    }
    ::QBrush cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QString QtStringPropertyManagerWrapper::formatText(const QtProperty * property) const
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
        Shiboken::Warnings::warnInvalidReturnValue("QtStringPropertyManager", "formatText", "QString", Py_TYPE(pyResult)->tp_name);
        return ::QString();
    }
    ::QString cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

bool QtStringPropertyManagerWrapper::hasValue(const QtProperty * property) const
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
        Shiboken::Warnings::warnInvalidReturnValue("QtStringPropertyManager", "hasValue", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtStringPropertyManagerWrapper::initializeProperty(QtProperty * property)
{
    if (m_PyMethodCache[13]) {
        return this->::QtStringPropertyManager::initializeProperty(property);
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
        return this->::QtStringPropertyManager::initializeProperty(property);
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

bool QtStringPropertyManagerWrapper::isReadOnly(const QtProperty * property) const
{
    if (m_PyMethodCache[14])
        return this->::QtStringPropertyManager::isReadOnly(property);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return false;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "isReadOnly";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[14] = true;
        gil.release();
        return this->::QtStringPropertyManager::isReadOnly(property);
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
        Shiboken::Warnings::warnInvalidReturnValue("QtStringPropertyManager", "isReadOnly", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QString QtStringPropertyManagerWrapper::maximumText(const QtProperty * property) const
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
        Shiboken::Warnings::warnInvalidReturnValue("QtStringPropertyManager", "maximumText", "QString", Py_TYPE(pyResult)->tp_name);
        return ::QString();
    }
    ::QString cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QString QtStringPropertyManagerWrapper::minimumText(const QtProperty * property) const
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
        Shiboken::Warnings::warnInvalidReturnValue("QtStringPropertyManager", "minimumText", "QString", Py_TYPE(pyResult)->tp_name);
        return ::QString();
    }
    ::QString cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QString QtStringPropertyManagerWrapper::pkAvgText(const QtProperty * property) const
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
        Shiboken::Warnings::warnInvalidReturnValue("QtStringPropertyManager", "pkAvgText", "QString", Py_TYPE(pyResult)->tp_name);
        return ::QString();
    }
    ::QString cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtStringPropertyManagerWrapper::setCheck(QtProperty * property, bool check)
{
    if (m_PyMethodCache[18]) {
        return this->::QtStringPropertyManager::setCheck(property, check);
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
        return this->::QtStringPropertyManager::setCheck(property, check);
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

void QtStringPropertyManagerWrapper::timerEvent(QTimerEvent * event)
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

void QtStringPropertyManagerWrapper::uninitializeProperty(QtProperty * property)
{
    if (m_PyMethodCache[20]) {
        return this->::QtStringPropertyManager::uninitializeProperty(property);
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
        return this->::QtStringPropertyManager::uninitializeProperty(property);
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

QString QtStringPropertyManagerWrapper::unitText(const QtProperty * property) const
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
        Shiboken::Warnings::warnInvalidReturnValue("QtStringPropertyManager", "unitText", "QString", Py_TYPE(pyResult)->tp_name);
        return ::QString();
    }
    ::QString cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QIcon QtStringPropertyManagerWrapper::valueIcon(const QtProperty * property) const
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
        Shiboken::Warnings::warnInvalidReturnValue("QtStringPropertyManager", "valueIcon", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QIcon >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return {};
    }
    ::QIcon cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QString QtStringPropertyManagerWrapper::valueText(const QtProperty * property) const
{
    if (m_PyMethodCache[23])
        return this->::QtStringPropertyManager::valueText(property);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return ::QString();
    static PyObject *nameCache[2] = {};
    static const char *funcName = "valueText";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[23] = true;
        gil.release();
        return this->::QtStringPropertyManager::valueText(property);
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
        Shiboken::Warnings::warnInvalidReturnValue("QtStringPropertyManager", "valueText", "QString", Py_TYPE(pyResult)->tp_name);
        return ::QString();
    }
    ::QString cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

const QMetaObject *QtStringPropertyManagerWrapper::metaObject() const
{
    if (QObject::d_ptr->metaObject)
        return QObject::d_ptr->dynamicMetaObject();
    SbkObject *pySelf = Shiboken::BindingManager::instance().retrieveWrapper(this);
    if (pySelf == nullptr)
        return QtStringPropertyManager::metaObject();
    return PySide::SignalManager::retrieveMetaObject(reinterpret_cast<PyObject *>(pySelf));
}

int QtStringPropertyManagerWrapper::qt_metacall(QMetaObject::Call call, int id, void **args)
{
    int result = QtStringPropertyManager::qt_metacall(call, id, args);
    return result < 0 ? result : PySide::SignalManager::qt_metacall(this, call, id, args);
}

void *QtStringPropertyManagerWrapper::qt_metacast(const char *_clname)
{
    if (!_clname)
        return {};
    SbkObject *pySelf = Shiboken::BindingManager::instance().retrieveWrapper(this);
    if (pySelf && PySide::inherits(Py_TYPE(pySelf), _clname))
        return static_cast<void *>(const_cast< QtStringPropertyManagerWrapper *>(this));
    return QtStringPropertyManager::qt_metacast(_clname);
}

QtStringPropertyManagerWrapper::~QtStringPropertyManagerWrapper()
{
    SbkObject *wrapper = Shiboken::BindingManager::instance().retrieveWrapper(this);
    Shiboken::Object::destroy(wrapper, this);
}

// Target ---------------------------------------------------------

extern "C" {
static int
Sbk_QtStringPropertyManager_Init(PyObject *self, PyObject *args, PyObject *kwds)
{
    SBK_UNUSED(kwds)
    const QMetaObject *metaObject;
    SbkObject *sbkSelf = reinterpret_cast<SbkObject *>(self);
    PySide::Feature::Select(self);
    if (Shiboken::Object::isUserType(self) && !Shiboken::ObjectType::canCallConstructor(self->ob_type, Shiboken::SbkType< ::QtStringPropertyManager >()))
        return -1;

    ::QtStringPropertyManagerWrapper *cptr{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtStringPropertyManager.__init__";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp[1];
    SBK_UNUSED(pythonToCpp)
    const Py_ssize_t numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {nullptr};

    // invalid argument lengths

    if (!PyArg_ParseTuple(args, "|O:QtStringPropertyManager", &(pyArgs[0])))
        return -1;


    // Overloaded function decisor
    // 0: QtStringPropertyManager::QtStringPropertyManager(QObject*)
    if (numArgs == 0) {
        overloadId = 0; // QtStringPropertyManager(QObject*)
    } else if (numArgs >= 1
        && (pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkPySide6_QtCoreTypes[SBK_QOBJECT_IDX], (pyArgs[0])))) {
        overloadId = 0; // QtStringPropertyManager(QObject*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtStringPropertyManager_Init_TypeError;

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
                    goto Sbk_QtStringPropertyManager_Init_TypeError;
                }
                if (value) {
                    pyArgs[0] = value;
                    if (!(pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkPySide6_QtCoreTypes[SBK_QOBJECT_IDX], (pyArgs[0]))))
                        goto Sbk_QtStringPropertyManager_Init_TypeError;
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
            // QtStringPropertyManager(QObject*)
            void *addr = PySide::nextQObjectMemoryAddr();
            if (addr) {
                cptr = new (addr) ::QtStringPropertyManagerWrapper(cppArg0);
                PySide::setNextQObjectMemoryAddr(nullptr);
            } else {
                cptr = new ::QtStringPropertyManagerWrapper(cppArg0);
            }

            // Ownership transferences (constructor heuristics).
            Shiboken::Object::setParent(pyArgs[0], self);
        }
    }

    if (PyErr_Occurred() || !Shiboken::Object::setCppPointer(sbkSelf, Shiboken::SbkType< ::QtStringPropertyManager >(), cptr)) {
        delete cptr;
        return -1;
    }
    if (!cptr) goto Sbk_QtStringPropertyManager_Init_TypeError;

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
            goto Sbk_QtStringPropertyManager_Init_TypeError;
    };


    return 1;

    Sbk_QtStringPropertyManager_Init_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return -1;
}

static PyObject *Sbk_QtStringPropertyManagerFunc_check(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtStringPropertyManagerWrapper *>(reinterpret_cast< ::QtStringPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTSTRINGPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtStringPropertyManager.check";
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
    if (overloadId == -1) goto Sbk_QtStringPropertyManagerFunc_check_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // check(const QtProperty*)const
            bool cppResult = Shiboken::Object::hasCppWrapper(reinterpret_cast<SbkObject *>(self))
                ? const_cast<const ::QtStringPropertyManagerWrapper *>(cppSelf)->::QtStringPropertyManager::check(cppArg0)
                : const_cast<const ::QtStringPropertyManagerWrapper *>(cppSelf)->check(cppArg0);
            pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtStringPropertyManagerFunc_check_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtStringPropertyManagerFunc_displayText(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtStringPropertyManagerWrapper *>(reinterpret_cast< ::QtStringPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTSTRINGPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtStringPropertyManager.displayText";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtAbstractPropertyManager::displayText(const QtProperty*)const->QString
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArg)))) {
        overloadId = 0; // displayText(const QtProperty*)const
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtStringPropertyManagerFunc_displayText_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // displayText(const QtProperty*)const
            QString cppResult = static_cast<::QtStringPropertyManagerWrapper *>(cppSelf)->QtStringPropertyManagerWrapper::displayText_protected(cppArg0);
            pyResult = Shiboken::Conversions::copyToPython(SbkPySide6_QtCoreTypeConverters[SBK_QSTRING_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtStringPropertyManagerFunc_displayText_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtStringPropertyManagerFunc_initializeProperty(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtStringPropertyManagerWrapper *>(reinterpret_cast< ::QtStringPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTSTRINGPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtStringPropertyManager.initializeProperty";
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
    if (overloadId == -1) goto Sbk_QtStringPropertyManagerFunc_initializeProperty_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // initializeProperty(QtProperty*)
            static_cast<::QtStringPropertyManagerWrapper *>(cppSelf)->QtStringPropertyManagerWrapper::initializeProperty_protected(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtStringPropertyManagerFunc_initializeProperty_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtStringPropertyManagerFunc_isReadOnly(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtStringPropertyManagerWrapper *>(reinterpret_cast< ::QtStringPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTSTRINGPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtStringPropertyManager.isReadOnly";
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
    if (overloadId == -1) goto Sbk_QtStringPropertyManagerFunc_isReadOnly_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // isReadOnly(const QtProperty*)const
            bool cppResult = Shiboken::Object::hasCppWrapper(reinterpret_cast<SbkObject *>(self))
                ? const_cast<const ::QtStringPropertyManagerWrapper *>(cppSelf)->::QtStringPropertyManager::isReadOnly(cppArg0)
                : const_cast<const ::QtStringPropertyManagerWrapper *>(cppSelf)->isReadOnly(cppArg0);
            pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtStringPropertyManagerFunc_isReadOnly_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtStringPropertyManagerFunc_regExp(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtStringPropertyManagerWrapper *>(reinterpret_cast< ::QtStringPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTSTRINGPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtStringPropertyManager.regExp";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtStringPropertyManager::regExp(const QtProperty*)const->QRegularExpression
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArg)))) {
        overloadId = 0; // regExp(const QtProperty*)const
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtStringPropertyManagerFunc_regExp_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // regExp(const QtProperty*)const
            QRegularExpression cppResult = const_cast<const ::QtStringPropertyManagerWrapper *>(cppSelf)->regExp(cppArg0);
            pyResult = Shiboken::Conversions::copyToPython(SbkPySide6_QtCoreTypes[SBK_QREGULAREXPRESSION_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtStringPropertyManagerFunc_regExp_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtStringPropertyManagerFunc_setCheck(PyObject *self, PyObject *args)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtStringPropertyManagerWrapper *>(reinterpret_cast< ::QtStringPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTSTRINGPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtStringPropertyManager.setCheck";
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
    if (overloadId == -1) goto Sbk_QtStringPropertyManagerFunc_setCheck_TypeError;

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
                ? cppSelf->::QtStringPropertyManager::setCheck(cppArg0, cppArg1)
                : cppSelf->setCheck(cppArg0, cppArg1);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtStringPropertyManagerFunc_setCheck_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtStringPropertyManagerFunc_setReadOnly(PyObject *self, PyObject *args)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtStringPropertyManagerWrapper *>(reinterpret_cast< ::QtStringPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTSTRINGPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtStringPropertyManager.setReadOnly";
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
    // 0: QtStringPropertyManager::setReadOnly(QtProperty*,bool)
    if (numArgs == 2
        && (pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::pythonToCppConversion(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), (pyArgs[1])))) {
        overloadId = 0; // setReadOnly(QtProperty*,bool)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtStringPropertyManagerFunc_setReadOnly_TypeError;

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

    Sbk_QtStringPropertyManagerFunc_setReadOnly_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtStringPropertyManagerFunc_setRegExp(PyObject *self, PyObject *args)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtStringPropertyManagerWrapper *>(reinterpret_cast< ::QtStringPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTSTRINGPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtStringPropertyManager.setRegExp";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp[2];
    SBK_UNUSED(pythonToCpp)
    const Py_ssize_t numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {nullptr, nullptr};

    // invalid argument lengths

    if (!PyArg_UnpackTuple(args, "setRegExp", 2, 2, &(pyArgs[0]), &(pyArgs[1])))
        return {};


    // Overloaded function decisor
    // 0: QtStringPropertyManager::setRegExp(QtProperty*,QRegularExpression)
    if (numArgs == 2
        && (pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::pythonToCppReferenceConversion(SbkPySide6_QtCoreTypes[SBK_QREGULAREXPRESSION_IDX], (pyArgs[1])))) {
        overloadId = 0; // setRegExp(QtProperty*,QRegularExpression)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtStringPropertyManagerFunc_setRegExp_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp[0](pyArgs[0], &cppArg0);
        if (!Shiboken::Object::isValid(pyArgs[1]))
            return {};
        ::QRegularExpression cppArg1_local;
        ::QRegularExpression *cppArg1 = &cppArg1_local;
        if (pythonToCpp[1].isValue())
            pythonToCpp[1](pyArgs[1], &cppArg1_local);
        else
            pythonToCpp[1](pyArgs[1], &cppArg1);


        if (!PyErr_Occurred()) {
            // setRegExp(QtProperty*,QRegularExpression)
            cppSelf->setRegExp(cppArg0, *cppArg1);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtStringPropertyManagerFunc_setRegExp_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtStringPropertyManagerFunc_setValue(PyObject *self, PyObject *args)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtStringPropertyManagerWrapper *>(reinterpret_cast< ::QtStringPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTSTRINGPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtStringPropertyManager.setValue";
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
    // 0: QtStringPropertyManager::setValue(QtProperty*,QString)
    if (numArgs == 2
        && (pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::pythonToCppConversion(SbkPySide6_QtCoreTypeConverters[SBK_QSTRING_IDX], (pyArgs[1])))) {
        overloadId = 0; // setValue(QtProperty*,QString)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtStringPropertyManagerFunc_setValue_TypeError;

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

    Sbk_QtStringPropertyManagerFunc_setValue_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtStringPropertyManagerFunc_uninitializeProperty(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtStringPropertyManagerWrapper *>(reinterpret_cast< ::QtStringPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTSTRINGPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtStringPropertyManager.uninitializeProperty";
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
    if (overloadId == -1) goto Sbk_QtStringPropertyManagerFunc_uninitializeProperty_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // uninitializeProperty(QtProperty*)
            static_cast<::QtStringPropertyManagerWrapper *>(cppSelf)->QtStringPropertyManagerWrapper::uninitializeProperty_protected(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtStringPropertyManagerFunc_uninitializeProperty_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtStringPropertyManagerFunc_value(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtStringPropertyManagerWrapper *>(reinterpret_cast< ::QtStringPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTSTRINGPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtStringPropertyManager.value";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtStringPropertyManager::value(const QtProperty*)const->QString
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArg)))) {
        overloadId = 0; // value(const QtProperty*)const
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtStringPropertyManagerFunc_value_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // value(const QtProperty*)const
            QString cppResult = const_cast<const ::QtStringPropertyManagerWrapper *>(cppSelf)->value(cppArg0);
            pyResult = Shiboken::Conversions::copyToPython(SbkPySide6_QtCoreTypeConverters[SBK_QSTRING_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtStringPropertyManagerFunc_value_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtStringPropertyManagerFunc_valueText(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtStringPropertyManagerWrapper *>(reinterpret_cast< ::QtStringPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTSTRINGPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtStringPropertyManager.valueText";
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
    if (overloadId == -1) goto Sbk_QtStringPropertyManagerFunc_valueText_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // valueText(const QtProperty*)const
            QString cppResult = static_cast<::QtStringPropertyManagerWrapper *>(cppSelf)->QtStringPropertyManagerWrapper::valueText_protected(cppArg0);
            pyResult = Shiboken::Conversions::copyToPython(SbkPySide6_QtCoreTypeConverters[SBK_QSTRING_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtStringPropertyManagerFunc_valueText_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}


static const char *Sbk_QtStringPropertyManager_PropertyStrings[] = {
    nullptr // Sentinel
};

static PyMethodDef Sbk_QtStringPropertyManager_methods[] = {
    {"check", reinterpret_cast<PyCFunction>(Sbk_QtStringPropertyManagerFunc_check), METH_O, nullptr},
    {"displayText", reinterpret_cast<PyCFunction>(Sbk_QtStringPropertyManagerFunc_displayText), METH_O, nullptr},
    {"initializeProperty", reinterpret_cast<PyCFunction>(Sbk_QtStringPropertyManagerFunc_initializeProperty), METH_O, nullptr},
    {"isReadOnly", reinterpret_cast<PyCFunction>(Sbk_QtStringPropertyManagerFunc_isReadOnly), METH_O, nullptr},
    {"regExp", reinterpret_cast<PyCFunction>(Sbk_QtStringPropertyManagerFunc_regExp), METH_O, nullptr},
    {"setCheck", reinterpret_cast<PyCFunction>(Sbk_QtStringPropertyManagerFunc_setCheck), METH_VARARGS, nullptr},
    {"setReadOnly", reinterpret_cast<PyCFunction>(Sbk_QtStringPropertyManagerFunc_setReadOnly), METH_VARARGS, nullptr},
    {"setRegExp", reinterpret_cast<PyCFunction>(Sbk_QtStringPropertyManagerFunc_setRegExp), METH_VARARGS, nullptr},
    {"setValue", reinterpret_cast<PyCFunction>(Sbk_QtStringPropertyManagerFunc_setValue), METH_VARARGS, nullptr},
    {"uninitializeProperty", reinterpret_cast<PyCFunction>(Sbk_QtStringPropertyManagerFunc_uninitializeProperty), METH_O, nullptr},
    {"value", reinterpret_cast<PyCFunction>(Sbk_QtStringPropertyManagerFunc_value), METH_O, nullptr},
    {"valueText", reinterpret_cast<PyCFunction>(Sbk_QtStringPropertyManagerFunc_valueText), METH_O, nullptr},

    {nullptr, nullptr, 0, nullptr} // Sentinel
};

static int Sbk_QtStringPropertyManager_setattro(PyObject *self, PyObject *name, PyObject *value)
{
    PySide::Feature::Select(self);
    if (value && PyCallable_Check(value)) {
        auto plain_inst = reinterpret_cast< ::QtStringPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTSTRINGPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self)));
        auto inst = dynamic_cast<QtStringPropertyManagerWrapper *>(plain_inst);
        if (inst)
            inst->resetPyMethodCache();
    }
    Shiboken::AutoDecRef pp(reinterpret_cast<PyObject *>(PySide::Property::getObject(self, name)));
    if (!pp.isNull())
        return PySide::Property::setValue(reinterpret_cast<PySideProperty *>(pp.object()), self, value);
    return PyObject_GenericSetAttr(self, name, value);
}

} // extern "C"

static int Sbk_QtStringPropertyManager_traverse(PyObject *self, visitproc visit, void *arg)
{
    return SbkObject_TypeF()->tp_traverse(self, visit, arg);
}
static int Sbk_QtStringPropertyManager_clear(PyObject *self)
{
    return reinterpret_cast<PyTypeObject *>(SbkObject_TypeF())->tp_clear(self);
}
// Class Definition -----------------------------------------------
extern "C" {
static PyTypeObject *_Sbk_QtStringPropertyManager_Type = nullptr;
static PyTypeObject *Sbk_QtStringPropertyManager_TypeF(void)
{
    return _Sbk_QtStringPropertyManager_Type;
}

static PyType_Slot Sbk_QtStringPropertyManager_slots[] = {
    {Py_tp_base,        nullptr}, // inserted by introduceWrapperType
    {Py_tp_dealloc,     reinterpret_cast<void *>(&SbkDeallocWrapper)},
    {Py_tp_repr,        nullptr},
    {Py_tp_hash,        nullptr},
    {Py_tp_call,        nullptr},
    {Py_tp_str,         nullptr},
    {Py_tp_getattro,    nullptr},
    {Py_tp_setattro,    reinterpret_cast<void *>(Sbk_QtStringPropertyManager_setattro)},
    {Py_tp_traverse,    reinterpret_cast<void *>(Sbk_QtStringPropertyManager_traverse)},
    {Py_tp_clear,       reinterpret_cast<void *>(Sbk_QtStringPropertyManager_clear)},
    {Py_tp_richcompare, nullptr},
    {Py_tp_iter,        nullptr},
    {Py_tp_iternext,    nullptr},
    {Py_tp_methods,     reinterpret_cast<void *>(Sbk_QtStringPropertyManager_methods)},
    {Py_tp_getset,      nullptr},
    {Py_tp_init,        reinterpret_cast<void *>(Sbk_QtStringPropertyManager_Init)},
    {Py_tp_new,         reinterpret_cast<void *>(SbkObject_tp_new)},
    {0, nullptr}
};
static PyType_Spec Sbk_QtStringPropertyManager_spec = {
    "1:qtpropertybrowser.QtStringPropertyManager",
    sizeof(SbkObject),
    0,
    Py_TPFLAGS_DEFAULT|Py_TPFLAGS_BASETYPE|Py_TPFLAGS_HAVE_GC,
    Sbk_QtStringPropertyManager_slots
};

} //extern "C"

static void *Sbk_QtStringPropertyManager_typeDiscovery(void *cptr, PyTypeObject *instanceType)
{
    SBK_UNUSED(cptr)
    SBK_UNUSED(instanceType)
    if (instanceType == Shiboken::SbkType< ::QObject >())
        return dynamic_cast< ::QtStringPropertyManager *>(reinterpret_cast< ::QObject *>(cptr));
    return {};
}


// Type conversion functions.

// Python to C++ pointer conversion - returns the C++ object of the Python wrapper (keeps object identity).
static void QtStringPropertyManager_PythonToCpp_QtStringPropertyManager_PTR(PyObject *pyIn, void *cppOut)
{
    Shiboken::Conversions::pythonToCppPointer(Sbk_QtStringPropertyManager_TypeF(), pyIn, cppOut);
}
static PythonToCppFunc is_QtStringPropertyManager_PythonToCpp_QtStringPropertyManager_PTR_Convertible(PyObject *pyIn)
{
    if (pyIn == Py_None)
        return Shiboken::Conversions::nonePythonToCppNullPtr;
    if (PyObject_TypeCheck(pyIn, Sbk_QtStringPropertyManager_TypeF()))
        return QtStringPropertyManager_PythonToCpp_QtStringPropertyManager_PTR;
    return {};
}

// C++ to Python pointer conversion - tries to find the Python wrapper for the C++ object (keeps object identity).
static PyObject *QtStringPropertyManager_PTR_CppToPython_QtStringPropertyManager(const void *cppIn)
{
    return PySide::getWrapperForQObject(reinterpret_cast<::QtStringPropertyManager *>(const_cast<void *>(cppIn)), Sbk_QtStringPropertyManager_TypeF());

}

// The signatures string for the functions.
// Multiple signatures have their index "n:" in front.
static const char *QtStringPropertyManager_SignatureStrings[] = {
    "qtpropertybrowser.QtStringPropertyManager(self,parent:PySide6.QtCore.QObject=0)",
    "qtpropertybrowser.QtStringPropertyManager.check(self,property:qtpropertybrowser.QtProperty)->bool",
    "qtpropertybrowser.QtStringPropertyManager.displayText(self,property:qtpropertybrowser.QtProperty)->QString",
    "qtpropertybrowser.QtStringPropertyManager.initializeProperty(self,property:qtpropertybrowser.QtProperty)",
    "qtpropertybrowser.QtStringPropertyManager.isReadOnly(self,property:qtpropertybrowser.QtProperty)->bool",
    "qtpropertybrowser.QtStringPropertyManager.regExp(self,property:qtpropertybrowser.QtProperty)->PySide6.QtCore.QRegularExpression",
    "qtpropertybrowser.QtStringPropertyManager.setCheck(self,property:qtpropertybrowser.QtProperty,check:bool)",
    "qtpropertybrowser.QtStringPropertyManager.setReadOnly(self,property:qtpropertybrowser.QtProperty,readOnly:bool)",
    "qtpropertybrowser.QtStringPropertyManager.setRegExp(self,property:qtpropertybrowser.QtProperty,regExp:typing.Union[PySide6.QtCore.QRegularExpression, QString])",
    "qtpropertybrowser.QtStringPropertyManager.setValue(self,property:qtpropertybrowser.QtProperty,val:QString)",
    "qtpropertybrowser.QtStringPropertyManager.uninitializeProperty(self,property:qtpropertybrowser.QtProperty)",
    "qtpropertybrowser.QtStringPropertyManager.value(self,property:qtpropertybrowser.QtProperty)->QString",
    "qtpropertybrowser.QtStringPropertyManager.valueText(self,property:qtpropertybrowser.QtProperty)->QString",
    nullptr}; // Sentinel

void init_QtStringPropertyManager(PyObject *module)
{
    _Sbk_QtStringPropertyManager_Type = Shiboken::ObjectType::introduceWrapperType(
        module,
        "QtStringPropertyManager",
        "QtStringPropertyManager*",
        &Sbk_QtStringPropertyManager_spec,
        &Shiboken::callCppDestructor< ::QtStringPropertyManager >,
        SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYMANAGER_IDX],
        0,
        0);
    auto *pyType = Sbk_QtStringPropertyManager_TypeF(); // references _Sbk_QtStringPropertyManager_Type
    InitSignatureStrings(pyType, QtStringPropertyManager_SignatureStrings);
    SbkObjectType_SetPropertyStrings(pyType, Sbk_QtStringPropertyManager_PropertyStrings);
    SbkqtpropertybrowserTypes[SBK_QTSTRINGPROPERTYMANAGER_IDX] = pyType;

    // Register Converter
    SbkConverter *converter = Shiboken::Conversions::createConverter(pyType,
        QtStringPropertyManager_PythonToCpp_QtStringPropertyManager_PTR,
        is_QtStringPropertyManager_PythonToCpp_QtStringPropertyManager_PTR_Convertible,
        QtStringPropertyManager_PTR_CppToPython_QtStringPropertyManager);

    Shiboken::Conversions::registerConverterName(converter, "QtStringPropertyManager");
    Shiboken::Conversions::registerConverterName(converter, "QtStringPropertyManager*");
    Shiboken::Conversions::registerConverterName(converter, "QtStringPropertyManager&");
    Shiboken::Conversions::registerConverterName(converter, typeid(::QtStringPropertyManager).name());
    Shiboken::Conversions::registerConverterName(converter, typeid(::QtStringPropertyManagerWrapper).name());


    Shiboken::ObjectType::setTypeDiscoveryFunctionV2(Sbk_QtStringPropertyManager_TypeF(), &Sbk_QtStringPropertyManager_typeDiscovery);

    PySide::Signal::registerSignals(pyType, &::QtStringPropertyManager::staticMetaObject);
    QtStringPropertyManagerWrapper::pysideInitQtMetaTypes();
    Shiboken::ObjectType::setSubTypeInitHook(pyType, &PySide::initQObjectSubType);
    PySide::initDynamicMetaObject(pyType, &::QtStringPropertyManager::staticMetaObject, sizeof(QtStringPropertyManagerWrapper));
}
