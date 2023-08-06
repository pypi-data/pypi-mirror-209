
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
#include "qtvariantpropertymanager_wrapper.h"

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

void QtVariantPropertyManagerWrapper::pysideInitQtMetaTypes()
{
}

void QtVariantPropertyManagerWrapper::resetPyMethodCache()
{
    std::fill_n(m_PyMethodCache, sizeof(m_PyMethodCache) / sizeof(m_PyMethodCache[0]), false);
}

QtVariantPropertyManagerWrapper::QtVariantPropertyManagerWrapper(QObject * parent) : QtVariantPropertyManager(parent)
{
    resetPyMethodCache();
    // ... middle
}

QtVariantProperty * QtVariantPropertyManagerWrapper::addProperty(int propertyType, const QString & name)
{
    if (m_PyMethodCache[0])
        return this->::QtVariantPropertyManager::addProperty(propertyType, name);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return nullptr;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "addProperty";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[0] = true;
        gil.release();
        return this->::QtVariantPropertyManager::addProperty(propertyType, name);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(iN)",
        propertyType,
        Shiboken::Conversions::copyToPython(SbkPySide6_QtCoreTypeConverters[SBK_QSTRING_IDX], &name)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return nullptr;
    }
    // Check return type
    Shiboken::Conversions::PythonToCppConversion pythonToCpp =
        Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTVARIANTPROPERTY_IDX], pyResult);
    if (!pythonToCpp) {
        Shiboken::Warnings::warnInvalidReturnValue("QtVariantPropertyManager", "addProperty", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QtVariantProperty >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return nullptr;
    }
    ::QtVariantProperty *cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

int QtVariantPropertyManagerWrapper::attributeType(int propertyType, const QString & attribute) const
{
    if (m_PyMethodCache[1])
        return this->::QtVariantPropertyManager::attributeType(propertyType, attribute);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return 0;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "attributeType";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[1] = true;
        gil.release();
        return this->::QtVariantPropertyManager::attributeType(propertyType, attribute);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(iN)",
        propertyType,
        Shiboken::Conversions::copyToPython(SbkPySide6_QtCoreTypeConverters[SBK_QSTRING_IDX], &attribute)
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
        Shiboken::Warnings::warnInvalidReturnValue("QtVariantPropertyManager", "attributeType", "int", Py_TYPE(pyResult)->tp_name);
        return 0;
    }
    int cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QVariant QtVariantPropertyManagerWrapper::attributeValue(const QtProperty * property, const QString & attribute) const
{
    if (m_PyMethodCache[2])
        return this->::QtVariantPropertyManager::attributeValue(property, attribute);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return ::QVariant();
    static PyObject *nameCache[2] = {};
    static const char *funcName = "attributeValue";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[2] = true;
        gil.release();
        return this->::QtVariantPropertyManager::attributeValue(property, attribute);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(NN)",
        Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], property),
        Shiboken::Conversions::copyToPython(SbkPySide6_QtCoreTypeConverters[SBK_QSTRING_IDX], &attribute)
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
        Shiboken::Warnings::warnInvalidReturnValue("QtVariantPropertyManager", "attributeValue", "QVariant", Py_TYPE(pyResult)->tp_name);
        return ::QVariant();
    }
    ::QVariant cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QStringList QtVariantPropertyManagerWrapper::attributes(int propertyType) const
{
    if (m_PyMethodCache[3])
        return this->::QtVariantPropertyManager::attributes(propertyType);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return ::QStringList();
    static PyObject *nameCache[2] = {};
    static const char *funcName = "attributes";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[3] = true;
        gil.release();
        return this->::QtVariantPropertyManager::attributes(propertyType);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(i)",
        propertyType
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return ::QStringList();
    }
    // Check return type
    Shiboken::Conversions::PythonToCppConversion pythonToCpp =
        Shiboken::Conversions::pythonToCppConversion(SbkPySide6_QtCoreTypeConverters[SBK_QSTRINGLIST_IDX], pyResult);
    if (!pythonToCpp) {
        Shiboken::Warnings::warnInvalidReturnValue("QtVariantPropertyManager", "attributes", "QStringList", Py_TYPE(pyResult)->tp_name);
        return ::QStringList();
    }
    ::QStringList cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

bool QtVariantPropertyManagerWrapper::check(const QtProperty * property) const
{
    if (m_PyMethodCache[4])
        return this->::QtAbstractPropertyManager::check(property);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return false;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "check";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[4] = true;
        gil.release();
        return this->::QtAbstractPropertyManager::check(property);
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
        Shiboken::Warnings::warnInvalidReturnValue("QtVariantPropertyManager", "check", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QIcon QtVariantPropertyManagerWrapper::checkIcon(const QtProperty * property) const
{
    if (m_PyMethodCache[5])
        return this->::QtAbstractPropertyManager::checkIcon(property);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return {};
    static PyObject *nameCache[2] = {};
    static const char *funcName = "checkIcon";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[5] = true;
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
        Shiboken::Warnings::warnInvalidReturnValue("QtVariantPropertyManager", "checkIcon", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QIcon >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return {};
    }
    ::QIcon cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtVariantPropertyManagerWrapper::childEvent(QChildEvent * event)
{
    if (m_PyMethodCache[6]) {
        return this->::QObject::childEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "childEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[6] = true;
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

void QtVariantPropertyManagerWrapper::connectNotify(const QMetaMethod & signal)
{
    if (m_PyMethodCache[7]) {
        return this->::QObject::connectNotify(signal);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "connectNotify";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[7] = true;
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

QtProperty * QtVariantPropertyManagerWrapper::createProperty()
{
    if (m_PyMethodCache[8])
        return this->::QtVariantPropertyManager::createProperty();
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return nullptr;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "createProperty";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[8] = true;
        gil.release();
        return this->::QtVariantPropertyManager::createProperty();
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
        Shiboken::Warnings::warnInvalidReturnValue("QtVariantPropertyManager", "createProperty", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QtProperty >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return nullptr;
    }
    ::QtProperty *cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtVariantPropertyManagerWrapper::customEvent(QEvent * event)
{
    if (m_PyMethodCache[9]) {
        return this->::QObject::customEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "customEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[9] = true;
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

void QtVariantPropertyManagerWrapper::disconnectNotify(const QMetaMethod & signal)
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

QString QtVariantPropertyManagerWrapper::displayText(const QtProperty * property) const
{
    if (m_PyMethodCache[11])
        return this->::QtAbstractPropertyManager::displayText(property);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return ::QString();
    static PyObject *nameCache[2] = {};
    static const char *funcName = "displayText";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[11] = true;
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
        Shiboken::Warnings::warnInvalidReturnValue("QtVariantPropertyManager", "displayText", "QString", Py_TYPE(pyResult)->tp_name);
        return ::QString();
    }
    ::QString cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

bool QtVariantPropertyManagerWrapper::event(QEvent * event)
{
    if (m_PyMethodCache[12])
        return this->::QObject::event(event);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return false;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "event";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[12] = true;
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
        Shiboken::Warnings::warnInvalidReturnValue("QtVariantPropertyManager", "event", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

bool QtVariantPropertyManagerWrapper::eventFilter(QObject * watched, QEvent * event)
{
    if (m_PyMethodCache[13])
        return this->::QObject::eventFilter(watched, event);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return false;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "eventFilter";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[13] = true;
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
        Shiboken::Warnings::warnInvalidReturnValue("QtVariantPropertyManager", "eventFilter", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QBrush QtVariantPropertyManagerWrapper::foreground(const QtProperty * property) const
{
    if (m_PyMethodCache[14])
        return this->::QtAbstractPropertyManager::foreground(property);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return {};
    static PyObject *nameCache[2] = {};
    static const char *funcName = "foreground";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[14] = true;
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
        Shiboken::Warnings::warnInvalidReturnValue("QtVariantPropertyManager", "foreground", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QBrush >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return {};
    }
    ::QBrush cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QString QtVariantPropertyManagerWrapper::formatText(const QtProperty * property) const
{
    if (m_PyMethodCache[15])
        return this->::QtAbstractPropertyManager::formatText(property);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return ::QString();
    static PyObject *nameCache[2] = {};
    static const char *funcName = "formatText";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[15] = true;
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
        Shiboken::Warnings::warnInvalidReturnValue("QtVariantPropertyManager", "formatText", "QString", Py_TYPE(pyResult)->tp_name);
        return ::QString();
    }
    ::QString cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

bool QtVariantPropertyManagerWrapper::hasValue(const QtProperty * property) const
{
    if (m_PyMethodCache[16])
        return this->::QtVariantPropertyManager::hasValue(property);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return false;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "hasValue";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[16] = true;
        gil.release();
        return this->::QtVariantPropertyManager::hasValue(property);
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
        Shiboken::Warnings::warnInvalidReturnValue("QtVariantPropertyManager", "hasValue", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtVariantPropertyManagerWrapper::initializeProperty(QtProperty * property)
{
    if (m_PyMethodCache[17]) {
        return this->::QtVariantPropertyManager::initializeProperty(property);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "initializeProperty";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[17] = true;
        gil.release();
        return this->::QtVariantPropertyManager::initializeProperty(property);
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

bool QtVariantPropertyManagerWrapper::isPropertyTypeSupported(int propertyType) const
{
    if (m_PyMethodCache[18])
        return this->::QtVariantPropertyManager::isPropertyTypeSupported(propertyType);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return false;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "isPropertyTypeSupported";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[18] = true;
        gil.release();
        return this->::QtVariantPropertyManager::isPropertyTypeSupported(propertyType);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(i)",
        propertyType
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
        Shiboken::Warnings::warnInvalidReturnValue("QtVariantPropertyManager", "isPropertyTypeSupported", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

bool QtVariantPropertyManagerWrapper::isReadOnly(const QtProperty * arg__1) const
{
    if (m_PyMethodCache[19])
        return this->::QtAbstractPropertyManager::isReadOnly(arg__1);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return false;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "isReadOnly";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[19] = true;
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
        Shiboken::Warnings::warnInvalidReturnValue("QtVariantPropertyManager", "isReadOnly", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QString QtVariantPropertyManagerWrapper::maximumText(const QtProperty * property) const
{
    if (m_PyMethodCache[20])
        return this->::QtAbstractPropertyManager::maximumText(property);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return ::QString();
    static PyObject *nameCache[2] = {};
    static const char *funcName = "maximumText";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[20] = true;
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
        Shiboken::Warnings::warnInvalidReturnValue("QtVariantPropertyManager", "maximumText", "QString", Py_TYPE(pyResult)->tp_name);
        return ::QString();
    }
    ::QString cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QString QtVariantPropertyManagerWrapper::minimumText(const QtProperty * property) const
{
    if (m_PyMethodCache[21])
        return this->::QtAbstractPropertyManager::minimumText(property);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return ::QString();
    static PyObject *nameCache[2] = {};
    static const char *funcName = "minimumText";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[21] = true;
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
        Shiboken::Warnings::warnInvalidReturnValue("QtVariantPropertyManager", "minimumText", "QString", Py_TYPE(pyResult)->tp_name);
        return ::QString();
    }
    ::QString cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QString QtVariantPropertyManagerWrapper::pkAvgText(const QtProperty * property) const
{
    if (m_PyMethodCache[22])
        return this->::QtAbstractPropertyManager::pkAvgText(property);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return ::QString();
    static PyObject *nameCache[2] = {};
    static const char *funcName = "pkAvgText";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[22] = true;
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
        Shiboken::Warnings::warnInvalidReturnValue("QtVariantPropertyManager", "pkAvgText", "QString", Py_TYPE(pyResult)->tp_name);
        return ::QString();
    }
    ::QString cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtVariantPropertyManagerWrapper::setAttribute(QtProperty * property, const QString & attribute, const QVariant & value)
{
    if (m_PyMethodCache[23]) {
        return this->::QtVariantPropertyManager::setAttribute(property, attribute, value);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "setAttribute";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[23] = true;
        gil.release();
        return this->::QtVariantPropertyManager::setAttribute(property, attribute, value);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(NNN)",
        Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], property),
        Shiboken::Conversions::copyToPython(SbkPySide6_QtCoreTypeConverters[SBK_QSTRING_IDX], &attribute),
        Shiboken::Conversions::copyToPython(SbkPySide6_QtCoreTypeConverters[SBK_QVARIANT_IDX], &value)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

void QtVariantPropertyManagerWrapper::setCheck(QtProperty * property, bool check)
{
    if (m_PyMethodCache[24]) {
        return this->::QtAbstractPropertyManager::setCheck(property, check);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "setCheck";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[24] = true;
        gil.release();
        return this->::QtAbstractPropertyManager::setCheck(property, check);
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

void QtVariantPropertyManagerWrapper::setValue(QtProperty * property, const QVariant & val)
{
    if (m_PyMethodCache[25]) {
        return this->::QtVariantPropertyManager::setValue(property, val);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "setValue";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[25] = true;
        gil.release();
        return this->::QtVariantPropertyManager::setValue(property, val);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(NN)",
        Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], property),
        Shiboken::Conversions::copyToPython(SbkPySide6_QtCoreTypeConverters[SBK_QVARIANT_IDX], &val)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

void QtVariantPropertyManagerWrapper::timerEvent(QTimerEvent * event)
{
    if (m_PyMethodCache[26]) {
        return this->::QObject::timerEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "timerEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[26] = true;
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

void QtVariantPropertyManagerWrapper::uninitializeProperty(QtProperty * property)
{
    if (m_PyMethodCache[27]) {
        return this->::QtVariantPropertyManager::uninitializeProperty(property);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "uninitializeProperty";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[27] = true;
        gil.release();
        return this->::QtVariantPropertyManager::uninitializeProperty(property);
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

QString QtVariantPropertyManagerWrapper::unitText(const QtProperty * property) const
{
    if (m_PyMethodCache[28])
        return this->::QtAbstractPropertyManager::unitText(property);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return ::QString();
    static PyObject *nameCache[2] = {};
    static const char *funcName = "unitText";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[28] = true;
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
        Shiboken::Warnings::warnInvalidReturnValue("QtVariantPropertyManager", "unitText", "QString", Py_TYPE(pyResult)->tp_name);
        return ::QString();
    }
    ::QString cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QVariant QtVariantPropertyManagerWrapper::value(const QtProperty * property) const
{
    if (m_PyMethodCache[29])
        return this->::QtVariantPropertyManager::value(property);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return ::QVariant();
    static PyObject *nameCache[2] = {};
    static const char *funcName = "value";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[29] = true;
        gil.release();
        return this->::QtVariantPropertyManager::value(property);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], property)
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
        Shiboken::Warnings::warnInvalidReturnValue("QtVariantPropertyManager", "value", "QVariant", Py_TYPE(pyResult)->tp_name);
        return ::QVariant();
    }
    ::QVariant cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QIcon QtVariantPropertyManagerWrapper::valueIcon(const QtProperty * property) const
{
    if (m_PyMethodCache[30])
        return this->::QtVariantPropertyManager::valueIcon(property);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return {};
    static PyObject *nameCache[2] = {};
    static const char *funcName = "valueIcon";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[30] = true;
        gil.release();
        return this->::QtVariantPropertyManager::valueIcon(property);
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
        Shiboken::Warnings::warnInvalidReturnValue("QtVariantPropertyManager", "valueIcon", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QIcon >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return {};
    }
    ::QIcon cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QString QtVariantPropertyManagerWrapper::valueText(const QtProperty * property) const
{
    if (m_PyMethodCache[31])
        return this->::QtVariantPropertyManager::valueText(property);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return ::QString();
    static PyObject *nameCache[2] = {};
    static const char *funcName = "valueText";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[31] = true;
        gil.release();
        return this->::QtVariantPropertyManager::valueText(property);
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
        Shiboken::Warnings::warnInvalidReturnValue("QtVariantPropertyManager", "valueText", "QString", Py_TYPE(pyResult)->tp_name);
        return ::QString();
    }
    ::QString cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

int QtVariantPropertyManagerWrapper::valueType(int propertyType) const
{
    if (m_PyMethodCache[32])
        return this->::QtVariantPropertyManager::valueType(propertyType);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return 0;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "valueType";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[32] = true;
        gil.release();
        return this->::QtVariantPropertyManager::valueType(propertyType);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(i)",
        propertyType
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
        Shiboken::Warnings::warnInvalidReturnValue("QtVariantPropertyManager", "valueType", "int", Py_TYPE(pyResult)->tp_name);
        return 0;
    }
    int cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

const QMetaObject *QtVariantPropertyManagerWrapper::metaObject() const
{
    if (QObject::d_ptr->metaObject)
        return QObject::d_ptr->dynamicMetaObject();
    SbkObject *pySelf = Shiboken::BindingManager::instance().retrieveWrapper(this);
    if (pySelf == nullptr)
        return QtVariantPropertyManager::metaObject();
    return PySide::SignalManager::retrieveMetaObject(reinterpret_cast<PyObject *>(pySelf));
}

int QtVariantPropertyManagerWrapper::qt_metacall(QMetaObject::Call call, int id, void **args)
{
    int result = QtVariantPropertyManager::qt_metacall(call, id, args);
    return result < 0 ? result : PySide::SignalManager::qt_metacall(this, call, id, args);
}

void *QtVariantPropertyManagerWrapper::qt_metacast(const char *_clname)
{
    if (!_clname)
        return {};
    SbkObject *pySelf = Shiboken::BindingManager::instance().retrieveWrapper(this);
    if (pySelf && PySide::inherits(Py_TYPE(pySelf), _clname))
        return static_cast<void *>(const_cast< QtVariantPropertyManagerWrapper *>(this));
    return QtVariantPropertyManager::qt_metacast(_clname);
}

QtVariantPropertyManagerWrapper::~QtVariantPropertyManagerWrapper()
{
    SbkObject *wrapper = Shiboken::BindingManager::instance().retrieveWrapper(this);
    Shiboken::Object::destroy(wrapper, this);
}

// Target ---------------------------------------------------------

extern "C" {
static int
Sbk_QtVariantPropertyManager_Init(PyObject *self, PyObject *args, PyObject *kwds)
{
    SBK_UNUSED(kwds)
    const QMetaObject *metaObject;
    SbkObject *sbkSelf = reinterpret_cast<SbkObject *>(self);
    PySide::Feature::Select(self);
    if (Shiboken::Object::isUserType(self) && !Shiboken::ObjectType::canCallConstructor(self->ob_type, Shiboken::SbkType< ::QtVariantPropertyManager >()))
        return -1;

    ::QtVariantPropertyManagerWrapper *cptr{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtVariantPropertyManager.__init__";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp[1];
    SBK_UNUSED(pythonToCpp)
    const Py_ssize_t numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {nullptr};

    // invalid argument lengths

    if (!PyArg_ParseTuple(args, "|O:QtVariantPropertyManager", &(pyArgs[0])))
        return -1;


    // Overloaded function decisor
    // 0: QtVariantPropertyManager::QtVariantPropertyManager(QObject*)
    if (numArgs == 0) {
        overloadId = 0; // QtVariantPropertyManager(QObject*)
    } else if (numArgs >= 1
        && (pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkPySide6_QtCoreTypes[SBK_QOBJECT_IDX], (pyArgs[0])))) {
        overloadId = 0; // QtVariantPropertyManager(QObject*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtVariantPropertyManager_Init_TypeError;

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
                    goto Sbk_QtVariantPropertyManager_Init_TypeError;
                }
                if (value) {
                    pyArgs[0] = value;
                    if (!(pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkPySide6_QtCoreTypes[SBK_QOBJECT_IDX], (pyArgs[0]))))
                        goto Sbk_QtVariantPropertyManager_Init_TypeError;
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
        ::QObject *cppArg0 = nullptr;
        if (pythonToCpp[0])
            pythonToCpp[0](pyArgs[0], &cppArg0);

        if (!PyErr_Occurred()) {
            // QtVariantPropertyManager(QObject*)
            void *addr = PySide::nextQObjectMemoryAddr();
            if (addr) {
                cptr = new (addr) ::QtVariantPropertyManagerWrapper(cppArg0);
                PySide::setNextQObjectMemoryAddr(nullptr);
            } else {
                cptr = new ::QtVariantPropertyManagerWrapper(cppArg0);
            }

            // Ownership transferences (constructor heuristics).
            Shiboken::Object::setParent(pyArgs[0], self);
        }
    }

    if (PyErr_Occurred() || !Shiboken::Object::setCppPointer(sbkSelf, Shiboken::SbkType< ::QtVariantPropertyManager >(), cptr)) {
        delete cptr;
        return -1;
    }
    if (!cptr) goto Sbk_QtVariantPropertyManager_Init_TypeError;

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
            goto Sbk_QtVariantPropertyManager_Init_TypeError;
    };


    return 1;

    Sbk_QtVariantPropertyManager_Init_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return -1;
}

static PyObject *Sbk_QtVariantPropertyManagerFunc_addProperty(PyObject *self, PyObject *args, PyObject *kwds)
{
    SBK_UNUSED(kwds)
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtVariantPropertyManagerWrapper *>(reinterpret_cast< ::QtVariantPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTVARIANTPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtVariantPropertyManager.addProperty";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp[2];
    SBK_UNUSED(pythonToCpp)
    const Py_ssize_t numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {nullptr, nullptr};

    // invalid argument lengths
    errInfo.reset(Shiboken::checkInvalidArgumentCount(numArgs, 1, 2));
    if (!errInfo.isNull())
        goto Sbk_QtVariantPropertyManagerFunc_addProperty_TypeError;

    if (!PyArg_ParseTuple(args, "|OO:addProperty", &(pyArgs[0]), &(pyArgs[1])))
        return {};


    // Overloaded function decisor
    // 0: QtVariantPropertyManager::addProperty(int,QString)->QtVariantProperty*
    if (numArgs >= 1
        && (pythonToCpp[0] = Shiboken::Conversions::pythonToCppConversion(Shiboken::Conversions::PrimitiveTypeConverter<int>(), (pyArgs[0])))) {
        if (numArgs == 1) {
            overloadId = 0; // addProperty(int,QString)
        } else if (numArgs >= 2
            && (pythonToCpp[1] = Shiboken::Conversions::pythonToCppConversion(SbkPySide6_QtCoreTypeConverters[SBK_QSTRING_IDX], (pyArgs[1])))) {
            overloadId = 0; // addProperty(int,QString)
        }
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtVariantPropertyManagerFunc_addProperty_TypeError;

    // Call function/method
    {
        if (kwds && PyDict_Size(kwds) > 0) {
            PyObject *value{};
            Shiboken::AutoDecRef kwds_dup(PyDict_Copy(kwds));
            static PyObject *const key_name = Shiboken::String::createStaticString("name");
            if (PyDict_Contains(kwds, key_name)) {
                value = PyDict_GetItem(kwds, key_name);
                if (value && pyArgs[1]) {
                    errInfo.reset(key_name);
                    Py_INCREF(errInfo.object());
                    goto Sbk_QtVariantPropertyManagerFunc_addProperty_TypeError;
                }
                if (value) {
                    pyArgs[1] = value;
                    if (!(pythonToCpp[1] = Shiboken::Conversions::pythonToCppConversion(SbkPySide6_QtCoreTypeConverters[SBK_QSTRING_IDX], (pyArgs[1]))))
                        goto Sbk_QtVariantPropertyManagerFunc_addProperty_TypeError;
                }
                PyDict_DelItem(kwds_dup, key_name);
            }
            if (PyDict_Size(kwds_dup) > 0) {
                errInfo.reset(kwds_dup.release());
                goto Sbk_QtVariantPropertyManagerFunc_addProperty_TypeError;
            }
        }
        int cppArg0;
        pythonToCpp[0](pyArgs[0], &cppArg0);
        ::QString cppArg1 = QString();
        if (pythonToCpp[1])
            pythonToCpp[1](pyArgs[1], &cppArg1);

        if (!PyErr_Occurred()) {
            // addProperty(int,QString)
            QtVariantProperty * cppResult = Shiboken::Object::hasCppWrapper(reinterpret_cast<SbkObject *>(self))
                ? cppSelf->::QtVariantPropertyManager::addProperty(cppArg0, cppArg1)
                : cppSelf->addProperty(cppArg0, cppArg1);
            pyResult = Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTVARIANTPROPERTY_IDX], cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtVariantPropertyManagerFunc_addProperty_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtVariantPropertyManagerFunc_attributeType(PyObject *self, PyObject *args)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtVariantPropertyManagerWrapper *>(reinterpret_cast< ::QtVariantPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTVARIANTPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtVariantPropertyManager.attributeType";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp[2];
    SBK_UNUSED(pythonToCpp)
    const Py_ssize_t numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {nullptr, nullptr};

    // invalid argument lengths

    if (!PyArg_UnpackTuple(args, "attributeType", 2, 2, &(pyArgs[0]), &(pyArgs[1])))
        return {};


    // Overloaded function decisor
    // 0: QtVariantPropertyManager::attributeType(int,QString)const->int
    if (numArgs == 2
        && (pythonToCpp[0] = Shiboken::Conversions::pythonToCppConversion(Shiboken::Conversions::PrimitiveTypeConverter<int>(), (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::pythonToCppConversion(SbkPySide6_QtCoreTypeConverters[SBK_QSTRING_IDX], (pyArgs[1])))) {
        overloadId = 0; // attributeType(int,QString)const
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtVariantPropertyManagerFunc_attributeType_TypeError;

    // Call function/method
    {
        int cppArg0;
        pythonToCpp[0](pyArgs[0], &cppArg0);
        ::QString cppArg1;
        pythonToCpp[1](pyArgs[1], &cppArg1);

        if (!PyErr_Occurred()) {
            // attributeType(int,QString)const
            int cppResult = Shiboken::Object::hasCppWrapper(reinterpret_cast<SbkObject *>(self))
                ? const_cast<const ::QtVariantPropertyManagerWrapper *>(cppSelf)->::QtVariantPropertyManager::attributeType(cppArg0, cppArg1)
                : const_cast<const ::QtVariantPropertyManagerWrapper *>(cppSelf)->attributeType(cppArg0, cppArg1);
            pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<int>(), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtVariantPropertyManagerFunc_attributeType_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtVariantPropertyManagerFunc_attributeValue(PyObject *self, PyObject *args)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtVariantPropertyManagerWrapper *>(reinterpret_cast< ::QtVariantPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTVARIANTPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtVariantPropertyManager.attributeValue";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp[2];
    SBK_UNUSED(pythonToCpp)
    const Py_ssize_t numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {nullptr, nullptr};

    // invalid argument lengths

    if (!PyArg_UnpackTuple(args, "attributeValue", 2, 2, &(pyArgs[0]), &(pyArgs[1])))
        return {};


    // Overloaded function decisor
    // 0: QtVariantPropertyManager::attributeValue(const QtProperty*,QString)const->QVariant
    if (numArgs == 2
        && (pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::pythonToCppConversion(SbkPySide6_QtCoreTypeConverters[SBK_QSTRING_IDX], (pyArgs[1])))) {
        overloadId = 0; // attributeValue(const QtProperty*,QString)const
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtVariantPropertyManagerFunc_attributeValue_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp[0](pyArgs[0], &cppArg0);
        ::QString cppArg1;
        pythonToCpp[1](pyArgs[1], &cppArg1);

        if (!PyErr_Occurred()) {
            // attributeValue(const QtProperty*,QString)const
            QVariant cppResult = Shiboken::Object::hasCppWrapper(reinterpret_cast<SbkObject *>(self))
                ? const_cast<const ::QtVariantPropertyManagerWrapper *>(cppSelf)->::QtVariantPropertyManager::attributeValue(cppArg0, cppArg1)
                : const_cast<const ::QtVariantPropertyManagerWrapper *>(cppSelf)->attributeValue(cppArg0, cppArg1);
            pyResult = Shiboken::Conversions::copyToPython(SbkPySide6_QtCoreTypeConverters[SBK_QVARIANT_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtVariantPropertyManagerFunc_attributeValue_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtVariantPropertyManagerFunc_attributes(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtVariantPropertyManagerWrapper *>(reinterpret_cast< ::QtVariantPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTVARIANTPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtVariantPropertyManager.attributes";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtVariantPropertyManager::attributes(int)const->QStringList
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppConversion(Shiboken::Conversions::PrimitiveTypeConverter<int>(), (pyArg)))) {
        overloadId = 0; // attributes(int)const
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtVariantPropertyManagerFunc_attributes_TypeError;

    // Call function/method
    {
        int cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // attributes(int)const
            QStringList cppResult = Shiboken::Object::hasCppWrapper(reinterpret_cast<SbkObject *>(self))
                ? const_cast<const ::QtVariantPropertyManagerWrapper *>(cppSelf)->::QtVariantPropertyManager::attributes(cppArg0)
                : const_cast<const ::QtVariantPropertyManagerWrapper *>(cppSelf)->attributes(cppArg0);
            pyResult = Shiboken::Conversions::copyToPython(SbkPySide6_QtCoreTypeConverters[SBK_QSTRINGLIST_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtVariantPropertyManagerFunc_attributes_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtVariantPropertyManagerFunc_createProperty(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtVariantPropertyManagerWrapper *>(reinterpret_cast< ::QtVariantPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTVARIANTPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // createProperty()
            QtProperty * cppResult = static_cast<::QtVariantPropertyManagerWrapper *>(cppSelf)->QtVariantPropertyManagerWrapper::createProperty_protected();
            pyResult = Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtVariantPropertyManagerFunc_enumTypeId(PyObject *self)
{
    SBK_UNUSED(self)
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // enumTypeId()
            int cppResult = ::QtVariantPropertyManager::enumTypeId();
            pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<int>(), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtVariantPropertyManagerFunc_flagTypeId(PyObject *self)
{
    SBK_UNUSED(self)
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // flagTypeId()
            int cppResult = ::QtVariantPropertyManager::flagTypeId();
            pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<int>(), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtVariantPropertyManagerFunc_groupTypeId(PyObject *self)
{
    SBK_UNUSED(self)
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // groupTypeId()
            int cppResult = ::QtVariantPropertyManager::groupTypeId();
            pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<int>(), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtVariantPropertyManagerFunc_hasValue(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtVariantPropertyManagerWrapper *>(reinterpret_cast< ::QtVariantPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTVARIANTPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtVariantPropertyManager.hasValue";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtAbstractPropertyManager::hasValue(const QtProperty*)const->bool
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArg)))) {
        overloadId = 0; // hasValue(const QtProperty*)const
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtVariantPropertyManagerFunc_hasValue_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // hasValue(const QtProperty*)const
            bool cppResult = static_cast<::QtVariantPropertyManagerWrapper *>(cppSelf)->QtVariantPropertyManagerWrapper::hasValue_protected(cppArg0);
            pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtVariantPropertyManagerFunc_hasValue_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtVariantPropertyManagerFunc_iconMapTypeId(PyObject *self)
{
    SBK_UNUSED(self)
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // iconMapTypeId()
            int cppResult = ::QtVariantPropertyManager::iconMapTypeId();
            pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<int>(), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtVariantPropertyManagerFunc_initializeProperty(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtVariantPropertyManagerWrapper *>(reinterpret_cast< ::QtVariantPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTVARIANTPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtVariantPropertyManager.initializeProperty";
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
    if (overloadId == -1) goto Sbk_QtVariantPropertyManagerFunc_initializeProperty_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // initializeProperty(QtProperty*)
            static_cast<::QtVariantPropertyManagerWrapper *>(cppSelf)->QtVariantPropertyManagerWrapper::initializeProperty_protected(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtVariantPropertyManagerFunc_initializeProperty_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtVariantPropertyManagerFunc_isPropertyTypeSupported(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtVariantPropertyManagerWrapper *>(reinterpret_cast< ::QtVariantPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTVARIANTPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtVariantPropertyManager.isPropertyTypeSupported";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtVariantPropertyManager::isPropertyTypeSupported(int)const->bool
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppConversion(Shiboken::Conversions::PrimitiveTypeConverter<int>(), (pyArg)))) {
        overloadId = 0; // isPropertyTypeSupported(int)const
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtVariantPropertyManagerFunc_isPropertyTypeSupported_TypeError;

    // Call function/method
    {
        int cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // isPropertyTypeSupported(int)const
            bool cppResult = Shiboken::Object::hasCppWrapper(reinterpret_cast<SbkObject *>(self))
                ? const_cast<const ::QtVariantPropertyManagerWrapper *>(cppSelf)->::QtVariantPropertyManager::isPropertyTypeSupported(cppArg0)
                : const_cast<const ::QtVariantPropertyManagerWrapper *>(cppSelf)->isPropertyTypeSupported(cppArg0);
            pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtVariantPropertyManagerFunc_isPropertyTypeSupported_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtVariantPropertyManagerFunc_propertyType(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtVariantPropertyManagerWrapper *>(reinterpret_cast< ::QtVariantPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTVARIANTPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtVariantPropertyManager.propertyType";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtVariantPropertyManager::propertyType(const QtProperty*)const->int
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArg)))) {
        overloadId = 0; // propertyType(const QtProperty*)const
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtVariantPropertyManagerFunc_propertyType_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // propertyType(const QtProperty*)const
            int cppResult = const_cast<const ::QtVariantPropertyManagerWrapper *>(cppSelf)->propertyType(cppArg0);
            pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<int>(), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtVariantPropertyManagerFunc_propertyType_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtVariantPropertyManagerFunc_setAttribute(PyObject *self, PyObject *args)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtVariantPropertyManagerWrapper *>(reinterpret_cast< ::QtVariantPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTVARIANTPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtVariantPropertyManager.setAttribute";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp[3];
    SBK_UNUSED(pythonToCpp)
    const Py_ssize_t numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {nullptr, nullptr, nullptr};

    // invalid argument lengths

    if (!PyArg_UnpackTuple(args, "setAttribute", 3, 3, &(pyArgs[0]), &(pyArgs[1]), &(pyArgs[2])))
        return {};


    // Overloaded function decisor
    // 0: QtVariantPropertyManager::setAttribute(QtProperty*,QString,QVariant)
    if (numArgs == 3
        && (pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::pythonToCppConversion(SbkPySide6_QtCoreTypeConverters[SBK_QSTRING_IDX], (pyArgs[1])))
        && (pythonToCpp[2] = Shiboken::Conversions::pythonToCppConversion(SbkPySide6_QtCoreTypeConverters[SBK_QVARIANT_IDX], (pyArgs[2])))) {
        overloadId = 0; // setAttribute(QtProperty*,QString,QVariant)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtVariantPropertyManagerFunc_setAttribute_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp[0](pyArgs[0], &cppArg0);
        ::QString cppArg1;
        pythonToCpp[1](pyArgs[1], &cppArg1);
        ::QVariant cppArg2;
        pythonToCpp[2](pyArgs[2], &cppArg2);

        if (!PyErr_Occurred()) {
            // setAttribute(QtProperty*,QString,QVariant)
            Shiboken::Object::hasCppWrapper(reinterpret_cast<SbkObject *>(self))
                ? cppSelf->::QtVariantPropertyManager::setAttribute(cppArg0, cppArg1, cppArg2)
                : cppSelf->setAttribute(cppArg0, cppArg1, cppArg2);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtVariantPropertyManagerFunc_setAttribute_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtVariantPropertyManagerFunc_setValue(PyObject *self, PyObject *args)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtVariantPropertyManagerWrapper *>(reinterpret_cast< ::QtVariantPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTVARIANTPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtVariantPropertyManager.setValue";
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
    // 0: QtVariantPropertyManager::setValue(QtProperty*,QVariant)
    if (numArgs == 2
        && (pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::pythonToCppConversion(SbkPySide6_QtCoreTypeConverters[SBK_QVARIANT_IDX], (pyArgs[1])))) {
        overloadId = 0; // setValue(QtProperty*,QVariant)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtVariantPropertyManagerFunc_setValue_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp[0](pyArgs[0], &cppArg0);
        ::QVariant cppArg1;
        pythonToCpp[1](pyArgs[1], &cppArg1);

        if (!PyErr_Occurred()) {
            // setValue(QtProperty*,QVariant)
            Shiboken::Object::hasCppWrapper(reinterpret_cast<SbkObject *>(self))
                ? cppSelf->::QtVariantPropertyManager::setValue(cppArg0, cppArg1)
                : cppSelf->setValue(cppArg0, cppArg1);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtVariantPropertyManagerFunc_setValue_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtVariantPropertyManagerFunc_uninitializeProperty(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtVariantPropertyManagerWrapper *>(reinterpret_cast< ::QtVariantPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTVARIANTPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtVariantPropertyManager.uninitializeProperty";
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
    if (overloadId == -1) goto Sbk_QtVariantPropertyManagerFunc_uninitializeProperty_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // uninitializeProperty(QtProperty*)
            static_cast<::QtVariantPropertyManagerWrapper *>(cppSelf)->QtVariantPropertyManagerWrapper::uninitializeProperty_protected(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtVariantPropertyManagerFunc_uninitializeProperty_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtVariantPropertyManagerFunc_value(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtVariantPropertyManagerWrapper *>(reinterpret_cast< ::QtVariantPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTVARIANTPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtVariantPropertyManager.value";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtVariantPropertyManager::value(const QtProperty*)const->QVariant
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArg)))) {
        overloadId = 0; // value(const QtProperty*)const
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtVariantPropertyManagerFunc_value_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // value(const QtProperty*)const
            QVariant cppResult = Shiboken::Object::hasCppWrapper(reinterpret_cast<SbkObject *>(self))
                ? const_cast<const ::QtVariantPropertyManagerWrapper *>(cppSelf)->::QtVariantPropertyManager::value(cppArg0)
                : const_cast<const ::QtVariantPropertyManagerWrapper *>(cppSelf)->value(cppArg0);
            pyResult = Shiboken::Conversions::copyToPython(SbkPySide6_QtCoreTypeConverters[SBK_QVARIANT_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtVariantPropertyManagerFunc_value_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtVariantPropertyManagerFunc_valueIcon(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtVariantPropertyManagerWrapper *>(reinterpret_cast< ::QtVariantPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTVARIANTPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtVariantPropertyManager.valueIcon";
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
    if (overloadId == -1) goto Sbk_QtVariantPropertyManagerFunc_valueIcon_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // valueIcon(const QtProperty*)const
            QIcon cppResult = static_cast<::QtVariantPropertyManagerWrapper *>(cppSelf)->QtVariantPropertyManagerWrapper::valueIcon_protected(cppArg0);
            pyResult = Shiboken::Conversions::copyToPython(SbkPySide6_QtGuiTypes[SBK_QICON_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtVariantPropertyManagerFunc_valueIcon_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtVariantPropertyManagerFunc_valueText(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtVariantPropertyManagerWrapper *>(reinterpret_cast< ::QtVariantPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTVARIANTPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtVariantPropertyManager.valueText";
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
    if (overloadId == -1) goto Sbk_QtVariantPropertyManagerFunc_valueText_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // valueText(const QtProperty*)const
            QString cppResult = static_cast<::QtVariantPropertyManagerWrapper *>(cppSelf)->QtVariantPropertyManagerWrapper::valueText_protected(cppArg0);
            pyResult = Shiboken::Conversions::copyToPython(SbkPySide6_QtCoreTypeConverters[SBK_QSTRING_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtVariantPropertyManagerFunc_valueText_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtVariantPropertyManagerFunc_valueType(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtVariantPropertyManagerWrapper *>(reinterpret_cast< ::QtVariantPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTVARIANTPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtVariantPropertyManager.valueType";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtVariantPropertyManager::valueType(int)const->int
    // 1: QtVariantPropertyManager::valueType(const QtProperty*)const->int
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArg)))) {
        overloadId = 1; // valueType(const QtProperty*)const
    } else if ((pythonToCpp = Shiboken::Conversions::pythonToCppConversion(Shiboken::Conversions::PrimitiveTypeConverter<int>(), (pyArg)))) {
        overloadId = 0; // valueType(int)const
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtVariantPropertyManagerFunc_valueType_TypeError;

    // Call function/method
    switch (overloadId) {
        case 0: // valueType(int propertyType) const
        {
            int cppArg0;
            pythonToCpp(pyArg, &cppArg0);

            if (!PyErr_Occurred()) {
                // valueType(int)const
                int cppResult = Shiboken::Object::hasCppWrapper(reinterpret_cast<SbkObject *>(self))
                    ? const_cast<const ::QtVariantPropertyManagerWrapper *>(cppSelf)->::QtVariantPropertyManager::valueType(cppArg0)
                    : const_cast<const ::QtVariantPropertyManagerWrapper *>(cppSelf)->valueType(cppArg0);
                pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<int>(), &cppResult);
            }
            break;
        }
        case 1: // valueType(const QtProperty * property) const
        {
            if (!Shiboken::Object::isValid(pyArg))
                return {};
            ::QtProperty *cppArg0;
            pythonToCpp(pyArg, &cppArg0);

            if (!PyErr_Occurred()) {
                // valueType(const QtProperty*)const
                int cppResult = const_cast<const ::QtVariantPropertyManagerWrapper *>(cppSelf)->valueType(cppArg0);
                pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<int>(), &cppResult);
            }
            break;
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtVariantPropertyManagerFunc_valueType_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtVariantPropertyManagerFunc_variantProperty(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtVariantPropertyManagerWrapper *>(reinterpret_cast< ::QtVariantPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTVARIANTPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtVariantPropertyManager.variantProperty";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtVariantPropertyManager::variantProperty(const QtProperty*)const->QtVariantProperty*
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArg)))) {
        overloadId = 0; // variantProperty(const QtProperty*)const
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtVariantPropertyManagerFunc_variantProperty_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // variantProperty(const QtProperty*)const
            QtVariantProperty * cppResult = const_cast<const ::QtVariantPropertyManagerWrapper *>(cppSelf)->variantProperty(cppArg0);
            pyResult = Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTVARIANTPROPERTY_IDX], cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtVariantPropertyManagerFunc_variantProperty_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}


static const char *Sbk_QtVariantPropertyManager_PropertyStrings[] = {
    nullptr // Sentinel
};

static PyMethodDef Sbk_QtVariantPropertyManager_methods[] = {
    {"addProperty", reinterpret_cast<PyCFunction>(Sbk_QtVariantPropertyManagerFunc_addProperty), METH_VARARGS|METH_KEYWORDS, nullptr},
    {"attributeType", reinterpret_cast<PyCFunction>(Sbk_QtVariantPropertyManagerFunc_attributeType), METH_VARARGS, nullptr},
    {"attributeValue", reinterpret_cast<PyCFunction>(Sbk_QtVariantPropertyManagerFunc_attributeValue), METH_VARARGS, nullptr},
    {"attributes", reinterpret_cast<PyCFunction>(Sbk_QtVariantPropertyManagerFunc_attributes), METH_O, nullptr},
    {"createProperty", reinterpret_cast<PyCFunction>(Sbk_QtVariantPropertyManagerFunc_createProperty), METH_NOARGS, nullptr},
    {"enumTypeId", reinterpret_cast<PyCFunction>(Sbk_QtVariantPropertyManagerFunc_enumTypeId), METH_NOARGS|METH_STATIC, nullptr},
    {"flagTypeId", reinterpret_cast<PyCFunction>(Sbk_QtVariantPropertyManagerFunc_flagTypeId), METH_NOARGS|METH_STATIC, nullptr},
    {"groupTypeId", reinterpret_cast<PyCFunction>(Sbk_QtVariantPropertyManagerFunc_groupTypeId), METH_NOARGS|METH_STATIC, nullptr},
    {"hasValue", reinterpret_cast<PyCFunction>(Sbk_QtVariantPropertyManagerFunc_hasValue), METH_O, nullptr},
    {"iconMapTypeId", reinterpret_cast<PyCFunction>(Sbk_QtVariantPropertyManagerFunc_iconMapTypeId), METH_NOARGS|METH_STATIC, nullptr},
    {"initializeProperty", reinterpret_cast<PyCFunction>(Sbk_QtVariantPropertyManagerFunc_initializeProperty), METH_O, nullptr},
    {"isPropertyTypeSupported", reinterpret_cast<PyCFunction>(Sbk_QtVariantPropertyManagerFunc_isPropertyTypeSupported), METH_O, nullptr},
    {"propertyType", reinterpret_cast<PyCFunction>(Sbk_QtVariantPropertyManagerFunc_propertyType), METH_O, nullptr},
    {"setAttribute", reinterpret_cast<PyCFunction>(Sbk_QtVariantPropertyManagerFunc_setAttribute), METH_VARARGS, nullptr},
    {"setValue", reinterpret_cast<PyCFunction>(Sbk_QtVariantPropertyManagerFunc_setValue), METH_VARARGS, nullptr},
    {"uninitializeProperty", reinterpret_cast<PyCFunction>(Sbk_QtVariantPropertyManagerFunc_uninitializeProperty), METH_O, nullptr},
    {"value", reinterpret_cast<PyCFunction>(Sbk_QtVariantPropertyManagerFunc_value), METH_O, nullptr},
    {"valueIcon", reinterpret_cast<PyCFunction>(Sbk_QtVariantPropertyManagerFunc_valueIcon), METH_O, nullptr},
    {"valueText", reinterpret_cast<PyCFunction>(Sbk_QtVariantPropertyManagerFunc_valueText), METH_O, nullptr},
    {"valueType", reinterpret_cast<PyCFunction>(Sbk_QtVariantPropertyManagerFunc_valueType), METH_O, nullptr},
    {"variantProperty", reinterpret_cast<PyCFunction>(Sbk_QtVariantPropertyManagerFunc_variantProperty), METH_O, nullptr},

    {nullptr, nullptr, 0, nullptr} // Sentinel
};

static int Sbk_QtVariantPropertyManager_setattro(PyObject *self, PyObject *name, PyObject *value)
{
    PySide::Feature::Select(self);
    if (value && PyCallable_Check(value)) {
        auto plain_inst = reinterpret_cast< ::QtVariantPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTVARIANTPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self)));
        auto inst = dynamic_cast<QtVariantPropertyManagerWrapper *>(plain_inst);
        if (inst)
            inst->resetPyMethodCache();
    }
    Shiboken::AutoDecRef pp(reinterpret_cast<PyObject *>(PySide::Property::getObject(self, name)));
    if (!pp.isNull())
        return PySide::Property::setValue(reinterpret_cast<PySideProperty *>(pp.object()), self, value);
    return PyObject_GenericSetAttr(self, name, value);
}

} // extern "C"

static int Sbk_QtVariantPropertyManager_traverse(PyObject *self, visitproc visit, void *arg)
{
    return SbkObject_TypeF()->tp_traverse(self, visit, arg);
}
static int Sbk_QtVariantPropertyManager_clear(PyObject *self)
{
    return reinterpret_cast<PyTypeObject *>(SbkObject_TypeF())->tp_clear(self);
}
// Class Definition -----------------------------------------------
extern "C" {
static PyTypeObject *_Sbk_QtVariantPropertyManager_Type = nullptr;
static PyTypeObject *Sbk_QtVariantPropertyManager_TypeF(void)
{
    return _Sbk_QtVariantPropertyManager_Type;
}

static PyType_Slot Sbk_QtVariantPropertyManager_slots[] = {
    {Py_tp_base,        nullptr}, // inserted by introduceWrapperType
    {Py_tp_dealloc,     reinterpret_cast<void *>(&SbkDeallocWrapper)},
    {Py_tp_repr,        nullptr},
    {Py_tp_hash,        nullptr},
    {Py_tp_call,        nullptr},
    {Py_tp_str,         nullptr},
    {Py_tp_getattro,    nullptr},
    {Py_tp_setattro,    reinterpret_cast<void *>(Sbk_QtVariantPropertyManager_setattro)},
    {Py_tp_traverse,    reinterpret_cast<void *>(Sbk_QtVariantPropertyManager_traverse)},
    {Py_tp_clear,       reinterpret_cast<void *>(Sbk_QtVariantPropertyManager_clear)},
    {Py_tp_richcompare, nullptr},
    {Py_tp_iter,        nullptr},
    {Py_tp_iternext,    nullptr},
    {Py_tp_methods,     reinterpret_cast<void *>(Sbk_QtVariantPropertyManager_methods)},
    {Py_tp_getset,      nullptr},
    {Py_tp_init,        reinterpret_cast<void *>(Sbk_QtVariantPropertyManager_Init)},
    {Py_tp_new,         reinterpret_cast<void *>(SbkObject_tp_new)},
    {0, nullptr}
};
static PyType_Spec Sbk_QtVariantPropertyManager_spec = {
    "1:qtpropertybrowser.QtVariantPropertyManager",
    sizeof(SbkObject),
    0,
    Py_TPFLAGS_DEFAULT|Py_TPFLAGS_BASETYPE|Py_TPFLAGS_HAVE_GC,
    Sbk_QtVariantPropertyManager_slots
};

} //extern "C"

static void *Sbk_QtVariantPropertyManager_typeDiscovery(void *cptr, PyTypeObject *instanceType)
{
    SBK_UNUSED(cptr)
    SBK_UNUSED(instanceType)
    if (instanceType == Shiboken::SbkType< ::QObject >())
        return dynamic_cast< ::QtVariantPropertyManager *>(reinterpret_cast< ::QObject *>(cptr));
    return {};
}


// Type conversion functions.

// Python to C++ pointer conversion - returns the C++ object of the Python wrapper (keeps object identity).
static void QtVariantPropertyManager_PythonToCpp_QtVariantPropertyManager_PTR(PyObject *pyIn, void *cppOut)
{
    Shiboken::Conversions::pythonToCppPointer(Sbk_QtVariantPropertyManager_TypeF(), pyIn, cppOut);
}
static PythonToCppFunc is_QtVariantPropertyManager_PythonToCpp_QtVariantPropertyManager_PTR_Convertible(PyObject *pyIn)
{
    if (pyIn == Py_None)
        return Shiboken::Conversions::nonePythonToCppNullPtr;
    if (PyObject_TypeCheck(pyIn, Sbk_QtVariantPropertyManager_TypeF()))
        return QtVariantPropertyManager_PythonToCpp_QtVariantPropertyManager_PTR;
    return {};
}

// C++ to Python pointer conversion - tries to find the Python wrapper for the C++ object (keeps object identity).
static PyObject *QtVariantPropertyManager_PTR_CppToPython_QtVariantPropertyManager(const void *cppIn)
{
    return PySide::getWrapperForQObject(reinterpret_cast<::QtVariantPropertyManager *>(const_cast<void *>(cppIn)), Sbk_QtVariantPropertyManager_TypeF());

}

// The signatures string for the functions.
// Multiple signatures have their index "n:" in front.
static const char *QtVariantPropertyManager_SignatureStrings[] = {
    "qtpropertybrowser.QtVariantPropertyManager(self,parent:PySide6.QtCore.QObject=nullptr)",
    "qtpropertybrowser.QtVariantPropertyManager.addProperty(self,propertyType:int,name:QString=QString())->qtpropertybrowser.QtVariantProperty",
    "qtpropertybrowser.QtVariantPropertyManager.attributeType(self,propertyType:int,attribute:QString)->int",
    "qtpropertybrowser.QtVariantPropertyManager.attributeValue(self,property:qtpropertybrowser.QtProperty,attribute:QString)->QVariant",
    "qtpropertybrowser.QtVariantPropertyManager.attributes(self,propertyType:int)->QStringList",
    "qtpropertybrowser.QtVariantPropertyManager.createProperty(self)->qtpropertybrowser.QtProperty",
    "qtpropertybrowser.QtVariantPropertyManager.enumTypeId()->int",
    "qtpropertybrowser.QtVariantPropertyManager.flagTypeId()->int",
    "qtpropertybrowser.QtVariantPropertyManager.groupTypeId()->int",
    "qtpropertybrowser.QtVariantPropertyManager.hasValue(self,property:qtpropertybrowser.QtProperty)->bool",
    "qtpropertybrowser.QtVariantPropertyManager.iconMapTypeId()->int",
    "qtpropertybrowser.QtVariantPropertyManager.initializeProperty(self,property:qtpropertybrowser.QtProperty)",
    "qtpropertybrowser.QtVariantPropertyManager.isPropertyTypeSupported(self,propertyType:int)->bool",
    "qtpropertybrowser.QtVariantPropertyManager.propertyType(self,property:qtpropertybrowser.QtProperty)->int",
    "qtpropertybrowser.QtVariantPropertyManager.setAttribute(self,property:qtpropertybrowser.QtProperty,attribute:QString,value:QVariant)",
    "qtpropertybrowser.QtVariantPropertyManager.setValue(self,property:qtpropertybrowser.QtProperty,val:QVariant)",
    "qtpropertybrowser.QtVariantPropertyManager.uninitializeProperty(self,property:qtpropertybrowser.QtProperty)",
    "qtpropertybrowser.QtVariantPropertyManager.value(self,property:qtpropertybrowser.QtProperty)->QVariant",
    "qtpropertybrowser.QtVariantPropertyManager.valueIcon(self,property:qtpropertybrowser.QtProperty)->PySide6.QtGui.QIcon",
    "qtpropertybrowser.QtVariantPropertyManager.valueText(self,property:qtpropertybrowser.QtProperty)->QString",
    "1:qtpropertybrowser.QtVariantPropertyManager.valueType(self,propertyType:int)->int",
    "0:qtpropertybrowser.QtVariantPropertyManager.valueType(self,property:qtpropertybrowser.QtProperty)->int",
    "qtpropertybrowser.QtVariantPropertyManager.variantProperty(self,property:qtpropertybrowser.QtProperty)->qtpropertybrowser.QtVariantProperty",
    nullptr}; // Sentinel

void init_QtVariantPropertyManager(PyObject *module)
{
    _Sbk_QtVariantPropertyManager_Type = Shiboken::ObjectType::introduceWrapperType(
        module,
        "QtVariantPropertyManager",
        "QtVariantPropertyManager*",
        &Sbk_QtVariantPropertyManager_spec,
        &Shiboken::callCppDestructor< ::QtVariantPropertyManager >,
        SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYMANAGER_IDX],
        0,
        0);
    auto *pyType = Sbk_QtVariantPropertyManager_TypeF(); // references _Sbk_QtVariantPropertyManager_Type
    InitSignatureStrings(pyType, QtVariantPropertyManager_SignatureStrings);
    SbkObjectType_SetPropertyStrings(pyType, Sbk_QtVariantPropertyManager_PropertyStrings);
    SbkqtpropertybrowserTypes[SBK_QTVARIANTPROPERTYMANAGER_IDX] = pyType;

    // Register Converter
    SbkConverter *converter = Shiboken::Conversions::createConverter(pyType,
        QtVariantPropertyManager_PythonToCpp_QtVariantPropertyManager_PTR,
        is_QtVariantPropertyManager_PythonToCpp_QtVariantPropertyManager_PTR_Convertible,
        QtVariantPropertyManager_PTR_CppToPython_QtVariantPropertyManager);

    Shiboken::Conversions::registerConverterName(converter, "QtVariantPropertyManager");
    Shiboken::Conversions::registerConverterName(converter, "QtVariantPropertyManager*");
    Shiboken::Conversions::registerConverterName(converter, "QtVariantPropertyManager&");
    Shiboken::Conversions::registerConverterName(converter, typeid(::QtVariantPropertyManager).name());
    Shiboken::Conversions::registerConverterName(converter, typeid(::QtVariantPropertyManagerWrapper).name());


    Shiboken::ObjectType::setTypeDiscoveryFunctionV2(Sbk_QtVariantPropertyManager_TypeF(), &Sbk_QtVariantPropertyManager_typeDiscovery);

    PySide::Signal::registerSignals(pyType, &::QtVariantPropertyManager::staticMetaObject);
    QtVariantPropertyManagerWrapper::pysideInitQtMetaTypes();
    Shiboken::ObjectType::setSubTypeInitHook(pyType, &PySide::initQObjectSubType);
    PySide::initDynamicMetaObject(pyType, &::QtVariantPropertyManager::staticMetaObject, sizeof(QtVariantPropertyManagerWrapper));
}
