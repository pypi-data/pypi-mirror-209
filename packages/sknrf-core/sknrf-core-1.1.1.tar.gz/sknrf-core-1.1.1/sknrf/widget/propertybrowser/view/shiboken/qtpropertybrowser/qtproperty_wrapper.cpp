
// default includes
#include <shiboken.h>
#ifndef QT_NO_VERSION_TAGGING
#  define QT_NO_VERSION_TAGGING
#endif
#include <QtCore/QDebug>
#include <pysideqenum.h>
#include <pysideqflags.h>
#include <pysideqmetatype.h>
#include <pysideutils.h>
#include <feature_select.h>
QT_WARNING_DISABLE_DEPRECATED


// module include
#include "qtpropertybrowser_python.h"

// main header
#include "qtproperty_wrapper.h"

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

void QtPropertyWrapper::pysideInitQtMetaTypes()
{
    qRegisterMetaType< ::QtProperty *>();
}

void QtPropertyWrapper::resetPyMethodCache()
{
    std::fill_n(m_PyMethodCache, sizeof(m_PyMethodCache) / sizeof(m_PyMethodCache[0]), false);
}

QtPropertyWrapper::QtPropertyWrapper(QtAbstractPropertyManager * manager) : QtProperty(manager)
{
    resetPyMethodCache();
    // ... middle
}

QtPropertyWrapper::~QtPropertyWrapper()
{
    SbkObject *wrapper = Shiboken::BindingManager::instance().retrieveWrapper(this);
    Shiboken::Object::destroy(wrapper, this);
}

// Target ---------------------------------------------------------

extern "C" {
static int
Sbk_QtProperty_Init(PyObject *self, PyObject *args, PyObject *kwds)
{
    SBK_UNUSED(kwds)
    SbkObject *sbkSelf = reinterpret_cast<SbkObject *>(self);
    PySide::Feature::Select(self);
    if (Shiboken::Object::isUserType(self) && !Shiboken::ObjectType::canCallConstructor(self->ob_type, Shiboken::SbkType< ::QtProperty >()))
        return -1;

    ::QtPropertyWrapper *cptr{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtProperty.__init__";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp[1];
    SBK_UNUSED(pythonToCpp)
    const Py_ssize_t numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {nullptr};

    // invalid argument lengths

    if (!PyArg_UnpackTuple(args, "QtProperty", 1, 1, &(pyArgs[0])))
        return -1;


    // Overloaded function decisor
    // 0: QtProperty::QtProperty(QtAbstractPropertyManager*)
    if (numArgs == 1
        && (pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYMANAGER_IDX], (pyArgs[0])))) {
        overloadId = 0; // QtProperty(QtAbstractPropertyManager*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtProperty_Init_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return -1;
        ::QtAbstractPropertyManager *cppArg0;
        pythonToCpp[0](pyArgs[0], &cppArg0);

        if (!PyErr_Occurred()) {
            // QtProperty(QtAbstractPropertyManager*)
            cptr = new ::QtPropertyWrapper(cppArg0);
        }
    }

    if (PyErr_Occurred() || !Shiboken::Object::setCppPointer(sbkSelf, Shiboken::SbkType< ::QtProperty >(), cptr)) {
        delete cptr;
        return -1;
    }
    if (!cptr) goto Sbk_QtProperty_Init_TypeError;

    Shiboken::Object::setValidCpp(sbkSelf, true);
    Shiboken::Object::setHasCppWrapper(sbkSelf, true);
    if (Shiboken::BindingManager::instance().hasWrapper(cptr)) {
        Shiboken::BindingManager::instance().releaseWrapper(Shiboken::BindingManager::instance().retrieveWrapper(cptr));
    }
    Shiboken::BindingManager::instance().registerWrapper(sbkSelf, cptr);


    return 1;

    Sbk_QtProperty_Init_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return -1;
}

static PyObject *Sbk_QtPropertyFunc_addSubProperty(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtProperty.addSubProperty";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtProperty::addSubProperty(QtProperty*)
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArg)))) {
        overloadId = 0; // addSubProperty(QtProperty*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtPropertyFunc_addSubProperty_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // addSubProperty(QtProperty*)
            cppSelf->addSubProperty(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtPropertyFunc_addSubProperty_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtPropertyFunc_check(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // check()const
            bool cppResult = const_cast<const ::QtPropertyWrapper *>(cppSelf)->check();
            pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtPropertyFunc_checkIcon(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // checkIcon()const
            QIcon cppResult = const_cast<const ::QtPropertyWrapper *>(cppSelf)->checkIcon();
            pyResult = Shiboken::Conversions::copyToPython(SbkPySide6_QtGuiTypes[SBK_QICON_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtPropertyFunc_descriptionToolTip(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // descriptionToolTip()const
            QString cppResult = const_cast<const ::QtPropertyWrapper *>(cppSelf)->descriptionToolTip();
            pyResult = Shiboken::Conversions::copyToPython(SbkPySide6_QtCoreTypeConverters[SBK_QSTRING_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtPropertyFunc_displayText(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // displayText()const
            QString cppResult = const_cast<const ::QtPropertyWrapper *>(cppSelf)->displayText();
            pyResult = Shiboken::Conversions::copyToPython(SbkPySide6_QtCoreTypeConverters[SBK_QSTRING_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtPropertyFunc_foreground(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // foreground()const
            QBrush cppResult = const_cast<const ::QtPropertyWrapper *>(cppSelf)->foreground();
            pyResult = Shiboken::Conversions::copyToPython(SbkPySide6_QtGuiTypes[SBK_QBRUSH_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtPropertyFunc_formatText(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // formatText()const
            QString cppResult = const_cast<const ::QtPropertyWrapper *>(cppSelf)->formatText();
            pyResult = Shiboken::Conversions::copyToPython(SbkPySide6_QtCoreTypeConverters[SBK_QSTRING_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtPropertyFunc_hasValue(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // hasValue()const
            bool cppResult = const_cast<const ::QtPropertyWrapper *>(cppSelf)->hasValue();
            pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtPropertyFunc_insertSubProperty(PyObject *self, PyObject *args)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtProperty.insertSubProperty";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp[2];
    SBK_UNUSED(pythonToCpp)
    const Py_ssize_t numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {nullptr, nullptr};

    // invalid argument lengths

    if (!PyArg_UnpackTuple(args, "insertSubProperty", 2, 2, &(pyArgs[0]), &(pyArgs[1])))
        return {};


    // Overloaded function decisor
    // 0: QtProperty::insertSubProperty(QtProperty*,QtProperty*)
    if (numArgs == 2
        && (pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArgs[1])))) {
        overloadId = 0; // insertSubProperty(QtProperty*,QtProperty*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtPropertyFunc_insertSubProperty_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp[0](pyArgs[0], &cppArg0);
        if (!Shiboken::Object::isValid(pyArgs[1]))
            return {};
        ::QtProperty *cppArg1;
        pythonToCpp[1](pyArgs[1], &cppArg1);

        if (!PyErr_Occurred()) {
            // insertSubProperty(QtProperty*,QtProperty*)
            cppSelf->insertSubProperty(cppArg0, cppArg1);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtPropertyFunc_insertSubProperty_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtPropertyFunc_isEnabled(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // isEnabled()const
            bool cppResult = const_cast<const ::QtPropertyWrapper *>(cppSelf)->isEnabled();
            pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtPropertyFunc_isModified(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // isModified()const
            bool cppResult = const_cast<const ::QtPropertyWrapper *>(cppSelf)->isModified();
            pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtPropertyFunc_label(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // label()const
            QString cppResult = const_cast<const ::QtPropertyWrapper *>(cppSelf)->label();
            pyResult = Shiboken::Conversions::copyToPython(SbkPySide6_QtCoreTypeConverters[SBK_QSTRING_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtPropertyFunc_maximumText(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // maximumText()const
            QString cppResult = const_cast<const ::QtPropertyWrapper *>(cppSelf)->maximumText();
            pyResult = Shiboken::Conversions::copyToPython(SbkPySide6_QtCoreTypeConverters[SBK_QSTRING_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtPropertyFunc_minimumText(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // minimumText()const
            QString cppResult = const_cast<const ::QtPropertyWrapper *>(cppSelf)->minimumText();
            pyResult = Shiboken::Conversions::copyToPython(SbkPySide6_QtCoreTypeConverters[SBK_QSTRING_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtPropertyFunc_pkAvgText(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // pkAvgText()const
            QString cppResult = const_cast<const ::QtPropertyWrapper *>(cppSelf)->pkAvgText();
            pyResult = Shiboken::Conversions::copyToPython(SbkPySide6_QtCoreTypeConverters[SBK_QSTRING_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtPropertyFunc_propertyChanged(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // propertyChanged()
            static_cast<::QtPropertyWrapper *>(cppSelf)->QtPropertyWrapper::propertyChanged_protected();
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;
}

static PyObject *Sbk_QtPropertyFunc_propertyManager(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // propertyManager()const
            QtAbstractPropertyManager * cppResult = const_cast<const ::QtPropertyWrapper *>(cppSelf)->propertyManager();
            pyResult = Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYMANAGER_IDX], cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtPropertyFunc_propertyName(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // propertyName()const
            QString cppResult = const_cast<const ::QtPropertyWrapper *>(cppSelf)->propertyName();
            pyResult = Shiboken::Conversions::copyToPython(SbkPySide6_QtCoreTypeConverters[SBK_QSTRING_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtPropertyFunc_removeSubProperty(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtProperty.removeSubProperty";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtProperty::removeSubProperty(QtProperty*)
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArg)))) {
        overloadId = 0; // removeSubProperty(QtProperty*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtPropertyFunc_removeSubProperty_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // removeSubProperty(QtProperty*)
            cppSelf->removeSubProperty(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtPropertyFunc_removeSubProperty_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtPropertyFunc_setDescriptionToolTip(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtProperty.setDescriptionToolTip";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtProperty::setDescriptionToolTip(QString)
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppConversion(SbkPySide6_QtCoreTypeConverters[SBK_QSTRING_IDX], (pyArg)))) {
        overloadId = 0; // setDescriptionToolTip(QString)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtPropertyFunc_setDescriptionToolTip_TypeError;

    // Call function/method
    {
        ::QString cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // setDescriptionToolTip(QString)
            cppSelf->setDescriptionToolTip(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtPropertyFunc_setDescriptionToolTip_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtPropertyFunc_setEnabled(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtProperty.setEnabled";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtProperty::setEnabled(bool)
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppConversion(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), (pyArg)))) {
        overloadId = 0; // setEnabled(bool)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtPropertyFunc_setEnabled_TypeError;

    // Call function/method
    {
        bool cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // setEnabled(bool)
            cppSelf->setEnabled(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtPropertyFunc_setEnabled_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtPropertyFunc_setLabel(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtProperty.setLabel";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtProperty::setLabel(QString)
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppConversion(SbkPySide6_QtCoreTypeConverters[SBK_QSTRING_IDX], (pyArg)))) {
        overloadId = 0; // setLabel(QString)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtPropertyFunc_setLabel_TypeError;

    // Call function/method
    {
        ::QString cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // setLabel(QString)
            cppSelf->setLabel(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtPropertyFunc_setLabel_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtPropertyFunc_setModified(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtProperty.setModified";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtProperty::setModified(bool)
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppConversion(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), (pyArg)))) {
        overloadId = 0; // setModified(bool)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtPropertyFunc_setModified_TypeError;

    // Call function/method
    {
        bool cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // setModified(bool)
            cppSelf->setModified(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtPropertyFunc_setModified_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtPropertyFunc_setPropertyName(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtProperty.setPropertyName";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtProperty::setPropertyName(QString)
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppConversion(SbkPySide6_QtCoreTypeConverters[SBK_QSTRING_IDX], (pyArg)))) {
        overloadId = 0; // setPropertyName(QString)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtPropertyFunc_setPropertyName_TypeError;

    // Call function/method
    {
        ::QString cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // setPropertyName(QString)
            cppSelf->setPropertyName(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtPropertyFunc_setPropertyName_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtPropertyFunc_setStatusTip(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtProperty.setStatusTip";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtProperty::setStatusTip(QString)
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppConversion(SbkPySide6_QtCoreTypeConverters[SBK_QSTRING_IDX], (pyArg)))) {
        overloadId = 0; // setStatusTip(QString)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtPropertyFunc_setStatusTip_TypeError;

    // Call function/method
    {
        ::QString cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // setStatusTip(QString)
            cppSelf->setStatusTip(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtPropertyFunc_setStatusTip_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtPropertyFunc_setToolTip(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtProperty.setToolTip";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtProperty::setToolTip(QString)
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppConversion(SbkPySide6_QtCoreTypeConverters[SBK_QSTRING_IDX], (pyArg)))) {
        overloadId = 0; // setToolTip(QString)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtPropertyFunc_setToolTip_TypeError;

    // Call function/method
    {
        ::QString cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // setToolTip(QString)
            cppSelf->setToolTip(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtPropertyFunc_setToolTip_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtPropertyFunc_setValueToolTip(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtProperty.setValueToolTip";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtProperty::setValueToolTip(QString)
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppConversion(SbkPySide6_QtCoreTypeConverters[SBK_QSTRING_IDX], (pyArg)))) {
        overloadId = 0; // setValueToolTip(QString)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtPropertyFunc_setValueToolTip_TypeError;

    // Call function/method
    {
        ::QString cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // setValueToolTip(QString)
            cppSelf->setValueToolTip(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtPropertyFunc_setValueToolTip_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtPropertyFunc_setWhatsThis(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtProperty.setWhatsThis";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtProperty::setWhatsThis(QString)
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppConversion(SbkPySide6_QtCoreTypeConverters[SBK_QSTRING_IDX], (pyArg)))) {
        overloadId = 0; // setWhatsThis(QString)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtPropertyFunc_setWhatsThis_TypeError;

    // Call function/method
    {
        ::QString cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // setWhatsThis(QString)
            cppSelf->setWhatsThis(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtPropertyFunc_setWhatsThis_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtPropertyFunc_statusTip(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // statusTip()const
            QString cppResult = const_cast<const ::QtPropertyWrapper *>(cppSelf)->statusTip();
            pyResult = Shiboken::Conversions::copyToPython(SbkPySide6_QtCoreTypeConverters[SBK_QSTRING_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtPropertyFunc_subProperties(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // subProperties()const
            QList<QtProperty* > cppResult = const_cast<const ::QtPropertyWrapper *>(cppSelf)->subProperties();
            pyResult = Shiboken::Conversions::copyToPython(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_QTPROPERTYPTR_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtPropertyFunc_toolTip(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // toolTip()const
            QString cppResult = const_cast<const ::QtPropertyWrapper *>(cppSelf)->toolTip();
            pyResult = Shiboken::Conversions::copyToPython(SbkPySide6_QtCoreTypeConverters[SBK_QSTRING_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtPropertyFunc_unitText(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // unitText()const
            QString cppResult = const_cast<const ::QtPropertyWrapper *>(cppSelf)->unitText();
            pyResult = Shiboken::Conversions::copyToPython(SbkPySide6_QtCoreTypeConverters[SBK_QSTRING_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtPropertyFunc_valueIcon(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // valueIcon()const
            QIcon cppResult = const_cast<const ::QtPropertyWrapper *>(cppSelf)->valueIcon();
            pyResult = Shiboken::Conversions::copyToPython(SbkPySide6_QtGuiTypes[SBK_QICON_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtPropertyFunc_valueText(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // valueText()const
            QString cppResult = const_cast<const ::QtPropertyWrapper *>(cppSelf)->valueText();
            pyResult = Shiboken::Conversions::copyToPython(SbkPySide6_QtCoreTypeConverters[SBK_QSTRING_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtPropertyFunc_valueToolTip(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // valueToolTip()const
            QString cppResult = const_cast<const ::QtPropertyWrapper *>(cppSelf)->valueToolTip();
            pyResult = Shiboken::Conversions::copyToPython(SbkPySide6_QtCoreTypeConverters[SBK_QSTRING_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtPropertyFunc_whatsThis(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // whatsThis()const
            QString cppResult = const_cast<const ::QtPropertyWrapper *>(cppSelf)->whatsThis();
            pyResult = Shiboken::Conversions::copyToPython(SbkPySide6_QtCoreTypeConverters[SBK_QSTRING_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}


static const char *Sbk_QtProperty_PropertyStrings[] = {
    nullptr // Sentinel
};

static PyMethodDef Sbk_QtProperty_methods[] = {
    {"addSubProperty", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_addSubProperty), METH_O, nullptr},
    {"check", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_check), METH_NOARGS, nullptr},
    {"checkIcon", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_checkIcon), METH_NOARGS, nullptr},
    {"descriptionToolTip", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_descriptionToolTip), METH_NOARGS, nullptr},
    {"displayText", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_displayText), METH_NOARGS, nullptr},
    {"foreground", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_foreground), METH_NOARGS, nullptr},
    {"formatText", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_formatText), METH_NOARGS, nullptr},
    {"hasValue", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_hasValue), METH_NOARGS, nullptr},
    {"insertSubProperty", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_insertSubProperty), METH_VARARGS, nullptr},
    {"isEnabled", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_isEnabled), METH_NOARGS, nullptr},
    {"isModified", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_isModified), METH_NOARGS, nullptr},
    {"label", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_label), METH_NOARGS, nullptr},
    {"maximumText", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_maximumText), METH_NOARGS, nullptr},
    {"minimumText", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_minimumText), METH_NOARGS, nullptr},
    {"pkAvgText", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_pkAvgText), METH_NOARGS, nullptr},
    {"propertyChanged", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_propertyChanged), METH_NOARGS, nullptr},
    {"propertyManager", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_propertyManager), METH_NOARGS, nullptr},
    {"propertyName", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_propertyName), METH_NOARGS, nullptr},
    {"removeSubProperty", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_removeSubProperty), METH_O, nullptr},
    {"setDescriptionToolTip", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_setDescriptionToolTip), METH_O, nullptr},
    {"setEnabled", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_setEnabled), METH_O, nullptr},
    {"setLabel", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_setLabel), METH_O, nullptr},
    {"setModified", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_setModified), METH_O, nullptr},
    {"setPropertyName", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_setPropertyName), METH_O, nullptr},
    {"setStatusTip", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_setStatusTip), METH_O, nullptr},
    {"setToolTip", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_setToolTip), METH_O, nullptr},
    {"setValueToolTip", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_setValueToolTip), METH_O, nullptr},
    {"setWhatsThis", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_setWhatsThis), METH_O, nullptr},
    {"statusTip", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_statusTip), METH_NOARGS, nullptr},
    {"subProperties", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_subProperties), METH_NOARGS, nullptr},
    {"toolTip", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_toolTip), METH_NOARGS, nullptr},
    {"unitText", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_unitText), METH_NOARGS, nullptr},
    {"valueIcon", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_valueIcon), METH_NOARGS, nullptr},
    {"valueText", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_valueText), METH_NOARGS, nullptr},
    {"valueToolTip", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_valueToolTip), METH_NOARGS, nullptr},
    {"whatsThis", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_whatsThis), METH_NOARGS, nullptr},

    {nullptr, nullptr, 0, nullptr} // Sentinel
};

static int Sbk_QtProperty_setattro(PyObject *self, PyObject *name, PyObject *value)
{
    PySide::Feature::Select(self);
    if (value && PyCallable_Check(value)) {
        auto plain_inst = reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self)));
        auto inst = dynamic_cast<QtPropertyWrapper *>(plain_inst);
        if (inst)
            inst->resetPyMethodCache();
    }
    return PyObject_GenericSetAttr(self, name, value);
}

} // extern "C"

static int Sbk_QtProperty_traverse(PyObject *self, visitproc visit, void *arg)
{
    return SbkObject_TypeF()->tp_traverse(self, visit, arg);
}
static int Sbk_QtProperty_clear(PyObject *self)
{
    return reinterpret_cast<PyTypeObject *>(SbkObject_TypeF())->tp_clear(self);
}
// Class Definition -----------------------------------------------
extern "C" {
static PyTypeObject *_Sbk_QtProperty_Type = nullptr;
static PyTypeObject *Sbk_QtProperty_TypeF(void)
{
    return _Sbk_QtProperty_Type;
}

static PyType_Slot Sbk_QtProperty_slots[] = {
    {Py_tp_base,        nullptr}, // inserted by introduceWrapperType
    {Py_tp_dealloc,     reinterpret_cast<void *>(&SbkDeallocWrapper)},
    {Py_tp_repr,        nullptr},
    {Py_tp_hash,        nullptr},
    {Py_tp_call,        nullptr},
    {Py_tp_str,         nullptr},
    {Py_tp_getattro,    nullptr},
    {Py_tp_setattro,    reinterpret_cast<void *>(Sbk_QtProperty_setattro)},
    {Py_tp_traverse,    reinterpret_cast<void *>(Sbk_QtProperty_traverse)},
    {Py_tp_clear,       reinterpret_cast<void *>(Sbk_QtProperty_clear)},
    {Py_tp_richcompare, nullptr},
    {Py_tp_iter,        nullptr},
    {Py_tp_iternext,    nullptr},
    {Py_tp_methods,     reinterpret_cast<void *>(Sbk_QtProperty_methods)},
    {Py_tp_getset,      nullptr},
    {Py_tp_init,        reinterpret_cast<void *>(Sbk_QtProperty_Init)},
    {Py_tp_new,         reinterpret_cast<void *>(SbkObject_tp_new)},
    {0, nullptr}
};
static PyType_Spec Sbk_QtProperty_spec = {
    "1:qtpropertybrowser.QtProperty",
    sizeof(SbkObject),
    0,
    Py_TPFLAGS_DEFAULT|Py_TPFLAGS_BASETYPE|Py_TPFLAGS_HAVE_GC,
    Sbk_QtProperty_slots
};

} //extern "C"


// Type conversion functions.

// Python to C++ pointer conversion - returns the C++ object of the Python wrapper (keeps object identity).
static void QtProperty_PythonToCpp_QtProperty_PTR(PyObject *pyIn, void *cppOut)
{
    Shiboken::Conversions::pythonToCppPointer(Sbk_QtProperty_TypeF(), pyIn, cppOut);
}
static PythonToCppFunc is_QtProperty_PythonToCpp_QtProperty_PTR_Convertible(PyObject *pyIn)
{
    if (pyIn == Py_None)
        return Shiboken::Conversions::nonePythonToCppNullPtr;
    if (PyObject_TypeCheck(pyIn, Sbk_QtProperty_TypeF()))
        return QtProperty_PythonToCpp_QtProperty_PTR;
    return {};
}

// C++ to Python pointer conversion - tries to find the Python wrapper for the C++ object (keeps object identity).
static PyObject *QtProperty_PTR_CppToPython_QtProperty(const void *cppIn)
{
    auto pyOut = reinterpret_cast<PyObject *>(Shiboken::BindingManager::instance().retrieveWrapper(cppIn));
    if (pyOut) {
        Py_INCREF(pyOut);
        return pyOut;
    }
    bool changedTypeName = false;
    auto tCppIn = reinterpret_cast<const ::QtProperty *>(cppIn);
    const char *typeName = typeid(*tCppIn).name();
    auto sbkType = Shiboken::ObjectType::typeForTypeName(typeName);
    if (sbkType && Shiboken::ObjectType::hasSpecialCastFunction(sbkType)) {
        typeName = typeNameOf(tCppIn);
        changedTypeName = true;
    }
    PyObject *result = Shiboken::Object::newObject(Sbk_QtProperty_TypeF(), const_cast<void *>(cppIn), false, /* exactType */ changedTypeName, typeName);
    if (changedTypeName)
        delete [] typeName;
    return result;
}

// The signatures string for the functions.
// Multiple signatures have their index "n:" in front.
static const char *QtProperty_SignatureStrings[] = {
    "qtpropertybrowser.QtProperty(self,manager:qtpropertybrowser.QtAbstractPropertyManager)",
    "qtpropertybrowser.QtProperty.addSubProperty(self,property:qtpropertybrowser.QtProperty)",
    "qtpropertybrowser.QtProperty.check(self)->bool",
    "qtpropertybrowser.QtProperty.checkIcon(self)->PySide6.QtGui.QIcon",
    "qtpropertybrowser.QtProperty.descriptionToolTip(self)->QString",
    "qtpropertybrowser.QtProperty.displayText(self)->QString",
    "qtpropertybrowser.QtProperty.foreground(self)->PySide6.QtGui.QBrush",
    "qtpropertybrowser.QtProperty.formatText(self)->QString",
    "qtpropertybrowser.QtProperty.hasValue(self)->bool",
    "qtpropertybrowser.QtProperty.insertSubProperty(self,property:qtpropertybrowser.QtProperty,afterProperty:qtpropertybrowser.QtProperty)",
    "qtpropertybrowser.QtProperty.isEnabled(self)->bool",
    "qtpropertybrowser.QtProperty.isModified(self)->bool",
    "qtpropertybrowser.QtProperty.label(self)->QString",
    "qtpropertybrowser.QtProperty.maximumText(self)->QString",
    "qtpropertybrowser.QtProperty.minimumText(self)->QString",
    "qtpropertybrowser.QtProperty.pkAvgText(self)->QString",
    "qtpropertybrowser.QtProperty.propertyChanged(self)",
    "qtpropertybrowser.QtProperty.propertyManager(self)->qtpropertybrowser.QtAbstractPropertyManager",
    "qtpropertybrowser.QtProperty.propertyName(self)->QString",
    "qtpropertybrowser.QtProperty.removeSubProperty(self,property:qtpropertybrowser.QtProperty)",
    "qtpropertybrowser.QtProperty.setDescriptionToolTip(self,text:QString)",
    "qtpropertybrowser.QtProperty.setEnabled(self,enable:bool)",
    "qtpropertybrowser.QtProperty.setLabel(self,text:QString)",
    "qtpropertybrowser.QtProperty.setModified(self,modified:bool)",
    "qtpropertybrowser.QtProperty.setPropertyName(self,text:QString)",
    "qtpropertybrowser.QtProperty.setStatusTip(self,text:QString)",
    "qtpropertybrowser.QtProperty.setToolTip(self,text:QString)",
    "qtpropertybrowser.QtProperty.setValueToolTip(self,text:QString)",
    "qtpropertybrowser.QtProperty.setWhatsThis(self,text:QString)",
    "qtpropertybrowser.QtProperty.statusTip(self)->QString",
    "qtpropertybrowser.QtProperty.subProperties(self)->QList[qtpropertybrowser.QtProperty]",
    "qtpropertybrowser.QtProperty.toolTip(self)->QString",
    "qtpropertybrowser.QtProperty.unitText(self)->QString",
    "qtpropertybrowser.QtProperty.valueIcon(self)->PySide6.QtGui.QIcon",
    "qtpropertybrowser.QtProperty.valueText(self)->QString",
    "qtpropertybrowser.QtProperty.valueToolTip(self)->QString",
    "qtpropertybrowser.QtProperty.whatsThis(self)->QString",
    nullptr}; // Sentinel

void init_QtProperty(PyObject *module)
{
    _Sbk_QtProperty_Type = Shiboken::ObjectType::introduceWrapperType(
        module,
        "QtProperty",
        "QtProperty*",
        &Sbk_QtProperty_spec,
        &Shiboken::callCppDestructor< ::QtProperty >,
        0,
        0,
        0);
    auto *pyType = Sbk_QtProperty_TypeF(); // references _Sbk_QtProperty_Type
    InitSignatureStrings(pyType, QtProperty_SignatureStrings);
    SbkObjectType_SetPropertyStrings(pyType, Sbk_QtProperty_PropertyStrings);
    SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX] = pyType;

    // Register Converter
    SbkConverter *converter = Shiboken::Conversions::createConverter(pyType,
        QtProperty_PythonToCpp_QtProperty_PTR,
        is_QtProperty_PythonToCpp_QtProperty_PTR_Convertible,
        QtProperty_PTR_CppToPython_QtProperty);

    Shiboken::Conversions::registerConverterName(converter, "QtProperty");
    Shiboken::Conversions::registerConverterName(converter, "QtProperty*");
    Shiboken::Conversions::registerConverterName(converter, "QtProperty&");
    Shiboken::Conversions::registerConverterName(converter, typeid(::QtProperty).name());
    Shiboken::Conversions::registerConverterName(converter, typeid(::QtPropertyWrapper).name());


    QtPropertyWrapper::pysideInitQtMetaTypes();
}
