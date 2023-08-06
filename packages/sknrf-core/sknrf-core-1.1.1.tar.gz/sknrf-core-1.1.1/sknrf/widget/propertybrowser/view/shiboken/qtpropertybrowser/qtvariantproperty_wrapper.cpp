
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
#include "qtvariantproperty_wrapper.h"

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

void QtVariantPropertyWrapper::pysideInitQtMetaTypes()
{
    qRegisterMetaType< ::QtVariantProperty *>();
}

void QtVariantPropertyWrapper::resetPyMethodCache()
{
    std::fill_n(m_PyMethodCache, sizeof(m_PyMethodCache) / sizeof(m_PyMethodCache[0]), false);
}

QtVariantPropertyWrapper::QtVariantPropertyWrapper(QtVariantPropertyManager * manager) : QtVariantProperty(manager)
{
    resetPyMethodCache();
    // ... middle
}

QtVariantPropertyWrapper::~QtVariantPropertyWrapper()
{
    SbkObject *wrapper = Shiboken::BindingManager::instance().retrieveWrapper(this);
    Shiboken::Object::destroy(wrapper, this);
}

// Target ---------------------------------------------------------

extern "C" {
static int
Sbk_QtVariantProperty_Init(PyObject *self, PyObject *args, PyObject *kwds)
{
    SBK_UNUSED(kwds)
    SbkObject *sbkSelf = reinterpret_cast<SbkObject *>(self);
    PySide::Feature::Select(self);
    if (Shiboken::Object::isUserType(self) && !Shiboken::ObjectType::canCallConstructor(self->ob_type, Shiboken::SbkType< ::QtVariantProperty >()))
        return -1;

    ::QtVariantPropertyWrapper *cptr{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtVariantProperty.__init__";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp[1];
    SBK_UNUSED(pythonToCpp)
    const Py_ssize_t numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {nullptr};

    // invalid argument lengths

    if (!PyArg_UnpackTuple(args, "QtVariantProperty", 1, 1, &(pyArgs[0])))
        return -1;


    // Overloaded function decisor
    // 0: QtVariantProperty::QtVariantProperty(QtVariantPropertyManager*)
    if (numArgs == 1
        && (pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTVARIANTPROPERTYMANAGER_IDX], (pyArgs[0])))) {
        overloadId = 0; // QtVariantProperty(QtVariantPropertyManager*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtVariantProperty_Init_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return -1;
        ::QtVariantPropertyManager *cppArg0;
        pythonToCpp[0](pyArgs[0], &cppArg0);

        if (!PyErr_Occurred()) {
            // QtVariantProperty(QtVariantPropertyManager*)
            cptr = new ::QtVariantPropertyWrapper(cppArg0);
        }
    }

    if (PyErr_Occurred() || !Shiboken::Object::setCppPointer(sbkSelf, Shiboken::SbkType< ::QtVariantProperty >(), cptr)) {
        delete cptr;
        return -1;
    }
    if (!cptr) goto Sbk_QtVariantProperty_Init_TypeError;

    Shiboken::Object::setValidCpp(sbkSelf, true);
    Shiboken::Object::setHasCppWrapper(sbkSelf, true);
    if (Shiboken::BindingManager::instance().hasWrapper(cptr)) {
        Shiboken::BindingManager::instance().releaseWrapper(Shiboken::BindingManager::instance().retrieveWrapper(cptr));
    }
    Shiboken::BindingManager::instance().registerWrapper(sbkSelf, cptr);


    return 1;

    Sbk_QtVariantProperty_Init_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return -1;
}

static PyObject *Sbk_QtVariantPropertyFunc_attributeValue(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtVariantPropertyWrapper *>(reinterpret_cast< ::QtVariantProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTVARIANTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtVariantProperty.attributeValue";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtVariantProperty::attributeValue(QString)const->QVariant
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppConversion(SbkPySide6_QtCoreTypeConverters[SBK_QSTRING_IDX], (pyArg)))) {
        overloadId = 0; // attributeValue(QString)const
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtVariantPropertyFunc_attributeValue_TypeError;

    // Call function/method
    {
        ::QString cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // attributeValue(QString)const
            QVariant cppResult = const_cast<const ::QtVariantPropertyWrapper *>(cppSelf)->attributeValue(cppArg0);
            pyResult = Shiboken::Conversions::copyToPython(SbkPySide6_QtCoreTypeConverters[SBK_QVARIANT_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtVariantPropertyFunc_attributeValue_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtVariantPropertyFunc_propertyType(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtVariantPropertyWrapper *>(reinterpret_cast< ::QtVariantProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTVARIANTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // propertyType()const
            int cppResult = const_cast<const ::QtVariantPropertyWrapper *>(cppSelf)->propertyType();
            pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<int>(), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtVariantPropertyFunc_setAttribute(PyObject *self, PyObject *args)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtVariantPropertyWrapper *>(reinterpret_cast< ::QtVariantProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTVARIANTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtVariantProperty.setAttribute";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp[2];
    SBK_UNUSED(pythonToCpp)
    const Py_ssize_t numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {nullptr, nullptr};

    // invalid argument lengths

    if (!PyArg_UnpackTuple(args, "setAttribute", 2, 2, &(pyArgs[0]), &(pyArgs[1])))
        return {};


    // Overloaded function decisor
    // 0: QtVariantProperty::setAttribute(QString,QVariant)
    if (numArgs == 2
        && (pythonToCpp[0] = Shiboken::Conversions::pythonToCppConversion(SbkPySide6_QtCoreTypeConverters[SBK_QSTRING_IDX], (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::pythonToCppConversion(SbkPySide6_QtCoreTypeConverters[SBK_QVARIANT_IDX], (pyArgs[1])))) {
        overloadId = 0; // setAttribute(QString,QVariant)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtVariantPropertyFunc_setAttribute_TypeError;

    // Call function/method
    {
        ::QString cppArg0;
        pythonToCpp[0](pyArgs[0], &cppArg0);
        ::QVariant cppArg1;
        pythonToCpp[1](pyArgs[1], &cppArg1);

        if (!PyErr_Occurred()) {
            // setAttribute(QString,QVariant)
            cppSelf->setAttribute(cppArg0, cppArg1);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtVariantPropertyFunc_setAttribute_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtVariantPropertyFunc_setValue(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtVariantPropertyWrapper *>(reinterpret_cast< ::QtVariantProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTVARIANTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtVariantProperty.setValue";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtVariantProperty::setValue(QVariant)
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppConversion(SbkPySide6_QtCoreTypeConverters[SBK_QVARIANT_IDX], (pyArg)))) {
        overloadId = 0; // setValue(QVariant)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtVariantPropertyFunc_setValue_TypeError;

    // Call function/method
    {
        ::QVariant cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // setValue(QVariant)
            cppSelf->setValue(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtVariantPropertyFunc_setValue_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtVariantPropertyFunc_value(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtVariantPropertyWrapper *>(reinterpret_cast< ::QtVariantProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTVARIANTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // value()const
            QVariant cppResult = const_cast<const ::QtVariantPropertyWrapper *>(cppSelf)->value();
            pyResult = Shiboken::Conversions::copyToPython(SbkPySide6_QtCoreTypeConverters[SBK_QVARIANT_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtVariantPropertyFunc_valueType(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtVariantPropertyWrapper *>(reinterpret_cast< ::QtVariantProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTVARIANTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // valueType()const
            int cppResult = const_cast<const ::QtVariantPropertyWrapper *>(cppSelf)->valueType();
            pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<int>(), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}


static const char *Sbk_QtVariantProperty_PropertyStrings[] = {
    nullptr // Sentinel
};

static PyMethodDef Sbk_QtVariantProperty_methods[] = {
    {"attributeValue", reinterpret_cast<PyCFunction>(Sbk_QtVariantPropertyFunc_attributeValue), METH_O, nullptr},
    {"propertyType", reinterpret_cast<PyCFunction>(Sbk_QtVariantPropertyFunc_propertyType), METH_NOARGS, nullptr},
    {"setAttribute", reinterpret_cast<PyCFunction>(Sbk_QtVariantPropertyFunc_setAttribute), METH_VARARGS, nullptr},
    {"setValue", reinterpret_cast<PyCFunction>(Sbk_QtVariantPropertyFunc_setValue), METH_O, nullptr},
    {"value", reinterpret_cast<PyCFunction>(Sbk_QtVariantPropertyFunc_value), METH_NOARGS, nullptr},
    {"valueType", reinterpret_cast<PyCFunction>(Sbk_QtVariantPropertyFunc_valueType), METH_NOARGS, nullptr},

    {nullptr, nullptr, 0, nullptr} // Sentinel
};

static int Sbk_QtVariantProperty_setattro(PyObject *self, PyObject *name, PyObject *value)
{
    PySide::Feature::Select(self);
    if (value && PyCallable_Check(value)) {
        auto plain_inst = reinterpret_cast< ::QtVariantProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTVARIANTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self)));
        auto inst = dynamic_cast<QtVariantPropertyWrapper *>(plain_inst);
        if (inst)
            inst->resetPyMethodCache();
    }
    return PyObject_GenericSetAttr(self, name, value);
}

} // extern "C"

static int Sbk_QtVariantProperty_traverse(PyObject *self, visitproc visit, void *arg)
{
    return SbkObject_TypeF()->tp_traverse(self, visit, arg);
}
static int Sbk_QtVariantProperty_clear(PyObject *self)
{
    return reinterpret_cast<PyTypeObject *>(SbkObject_TypeF())->tp_clear(self);
}
// Class Definition -----------------------------------------------
extern "C" {
static PyTypeObject *_Sbk_QtVariantProperty_Type = nullptr;
static PyTypeObject *Sbk_QtVariantProperty_TypeF(void)
{
    return _Sbk_QtVariantProperty_Type;
}

static PyType_Slot Sbk_QtVariantProperty_slots[] = {
    {Py_tp_base,        nullptr}, // inserted by introduceWrapperType
    {Py_tp_dealloc,     reinterpret_cast<void *>(&SbkDeallocWrapper)},
    {Py_tp_repr,        nullptr},
    {Py_tp_hash,        nullptr},
    {Py_tp_call,        nullptr},
    {Py_tp_str,         nullptr},
    {Py_tp_getattro,    nullptr},
    {Py_tp_setattro,    reinterpret_cast<void *>(Sbk_QtVariantProperty_setattro)},
    {Py_tp_traverse,    reinterpret_cast<void *>(Sbk_QtVariantProperty_traverse)},
    {Py_tp_clear,       reinterpret_cast<void *>(Sbk_QtVariantProperty_clear)},
    {Py_tp_richcompare, nullptr},
    {Py_tp_iter,        nullptr},
    {Py_tp_iternext,    nullptr},
    {Py_tp_methods,     reinterpret_cast<void *>(Sbk_QtVariantProperty_methods)},
    {Py_tp_getset,      nullptr},
    {Py_tp_init,        reinterpret_cast<void *>(Sbk_QtVariantProperty_Init)},
    {Py_tp_new,         reinterpret_cast<void *>(SbkObject_tp_new)},
    {0, nullptr}
};
static PyType_Spec Sbk_QtVariantProperty_spec = {
    "1:qtpropertybrowser.QtVariantProperty",
    sizeof(SbkObject),
    0,
    Py_TPFLAGS_DEFAULT|Py_TPFLAGS_BASETYPE|Py_TPFLAGS_HAVE_GC,
    Sbk_QtVariantProperty_slots
};

} //extern "C"

static void *Sbk_QtVariantProperty_typeDiscovery(void *cptr, PyTypeObject *instanceType)
{
    SBK_UNUSED(cptr)
    SBK_UNUSED(instanceType)
    if (instanceType == Shiboken::SbkType< ::QtProperty >())
        return dynamic_cast< ::QtVariantProperty *>(reinterpret_cast< ::QtProperty *>(cptr));
    return {};
}


// Type conversion functions.

// Python to C++ pointer conversion - returns the C++ object of the Python wrapper (keeps object identity).
static void QtVariantProperty_PythonToCpp_QtVariantProperty_PTR(PyObject *pyIn, void *cppOut)
{
    Shiboken::Conversions::pythonToCppPointer(Sbk_QtVariantProperty_TypeF(), pyIn, cppOut);
}
static PythonToCppFunc is_QtVariantProperty_PythonToCpp_QtVariantProperty_PTR_Convertible(PyObject *pyIn)
{
    if (pyIn == Py_None)
        return Shiboken::Conversions::nonePythonToCppNullPtr;
    if (PyObject_TypeCheck(pyIn, Sbk_QtVariantProperty_TypeF()))
        return QtVariantProperty_PythonToCpp_QtVariantProperty_PTR;
    return {};
}

// C++ to Python pointer conversion - tries to find the Python wrapper for the C++ object (keeps object identity).
static PyObject *QtVariantProperty_PTR_CppToPython_QtVariantProperty(const void *cppIn)
{
    auto pyOut = reinterpret_cast<PyObject *>(Shiboken::BindingManager::instance().retrieveWrapper(cppIn));
    if (pyOut) {
        Py_INCREF(pyOut);
        return pyOut;
    }
    bool changedTypeName = false;
    auto tCppIn = reinterpret_cast<const ::QtVariantProperty *>(cppIn);
    const char *typeName = typeid(*tCppIn).name();
    auto sbkType = Shiboken::ObjectType::typeForTypeName(typeName);
    if (sbkType && Shiboken::ObjectType::hasSpecialCastFunction(sbkType)) {
        typeName = typeNameOf(tCppIn);
        changedTypeName = true;
    }
    PyObject *result = Shiboken::Object::newObject(Sbk_QtVariantProperty_TypeF(), const_cast<void *>(cppIn), false, /* exactType */ changedTypeName, typeName);
    if (changedTypeName)
        delete [] typeName;
    return result;
}

// The signatures string for the functions.
// Multiple signatures have their index "n:" in front.
static const char *QtVariantProperty_SignatureStrings[] = {
    "qtpropertybrowser.QtVariantProperty(self,manager:qtpropertybrowser.QtVariantPropertyManager)",
    "qtpropertybrowser.QtVariantProperty.attributeValue(self,attribute:QString)->QVariant",
    "qtpropertybrowser.QtVariantProperty.propertyType(self)->int",
    "qtpropertybrowser.QtVariantProperty.setAttribute(self,attribute:QString,value:QVariant)",
    "qtpropertybrowser.QtVariantProperty.setValue(self,value:QVariant)",
    "qtpropertybrowser.QtVariantProperty.value(self)->QVariant",
    "qtpropertybrowser.QtVariantProperty.valueType(self)->int",
    nullptr}; // Sentinel

void init_QtVariantProperty(PyObject *module)
{
    _Sbk_QtVariantProperty_Type = Shiboken::ObjectType::introduceWrapperType(
        module,
        "QtVariantProperty",
        "QtVariantProperty*",
        &Sbk_QtVariantProperty_spec,
        &Shiboken::callCppDestructor< ::QtVariantProperty >,
        SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX],
        0,
        0);
    auto *pyType = Sbk_QtVariantProperty_TypeF(); // references _Sbk_QtVariantProperty_Type
    InitSignatureStrings(pyType, QtVariantProperty_SignatureStrings);
    SbkObjectType_SetPropertyStrings(pyType, Sbk_QtVariantProperty_PropertyStrings);
    SbkqtpropertybrowserTypes[SBK_QTVARIANTPROPERTY_IDX] = pyType;

    // Register Converter
    SbkConverter *converter = Shiboken::Conversions::createConverter(pyType,
        QtVariantProperty_PythonToCpp_QtVariantProperty_PTR,
        is_QtVariantProperty_PythonToCpp_QtVariantProperty_PTR_Convertible,
        QtVariantProperty_PTR_CppToPython_QtVariantProperty);

    Shiboken::Conversions::registerConverterName(converter, "QtVariantProperty");
    Shiboken::Conversions::registerConverterName(converter, "QtVariantProperty*");
    Shiboken::Conversions::registerConverterName(converter, "QtVariantProperty&");
    Shiboken::Conversions::registerConverterName(converter, typeid(::QtVariantProperty).name());
    Shiboken::Conversions::registerConverterName(converter, typeid(::QtVariantPropertyWrapper).name());


    Shiboken::ObjectType::setTypeDiscoveryFunctionV2(Sbk_QtVariantProperty_TypeF(), &Sbk_QtVariantProperty_typeDiscovery);

    QtVariantPropertyWrapper::pysideInitQtMetaTypes();
}
