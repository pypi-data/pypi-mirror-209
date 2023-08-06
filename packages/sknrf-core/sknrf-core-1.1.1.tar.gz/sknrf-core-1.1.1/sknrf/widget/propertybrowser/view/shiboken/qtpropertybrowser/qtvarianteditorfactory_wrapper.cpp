
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
#include "qtvarianteditorfactory_wrapper.h"

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

void QtVariantEditorFactoryWrapper::pysideInitQtMetaTypes()
{
    qRegisterMetaType< ::QtVariantEditorFactory *>();
}

void QtVariantEditorFactoryWrapper::resetPyMethodCache()
{
    std::fill_n(m_PyMethodCache, sizeof(m_PyMethodCache) / sizeof(m_PyMethodCache[0]), false);
}

QtVariantEditorFactoryWrapper::QtVariantEditorFactoryWrapper(QObject * parent) : QtVariantEditorFactory(parent)
{
    resetPyMethodCache();
    // ... middle
}

void QtVariantEditorFactoryWrapper::connectPropertyManager(QtVariantPropertyManager * manager)
{
    if (m_PyMethodCache[0]) {
        return this->::QtVariantEditorFactory::connectPropertyManager(manager);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "connectPropertyManager";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[0] = true;
        gil.release();
        return this->::QtVariantEditorFactory::connectPropertyManager(manager);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTVARIANTPROPERTYMANAGER_IDX], manager)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

QWidget * QtVariantEditorFactoryWrapper::createEditor(QtVariantPropertyManager * manager, QtProperty * property, QWidget * parent)
{
    if (m_PyMethodCache[1])
        return this->::QtVariantEditorFactory::createEditor(manager, property, parent);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return nullptr;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "createEditor";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[1] = true;
        gil.release();
        return this->::QtVariantEditorFactory::createEditor(manager, property, parent);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(NNN)",
        Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTVARIANTPROPERTYMANAGER_IDX], manager),
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
        Shiboken::Warnings::warnInvalidReturnValue("QtVariantEditorFactory", "createEditor", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QWidget >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return nullptr;
    }
    ::QWidget *cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtVariantEditorFactoryWrapper::disconnectPropertyManager(QtVariantPropertyManager * manager)
{
    if (m_PyMethodCache[2]) {
        return this->::QtVariantEditorFactory::disconnectPropertyManager(manager);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "disconnectPropertyManager";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[2] = true;
        gil.release();
        return this->::QtVariantEditorFactory::disconnectPropertyManager(manager);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTVARIANTPROPERTYMANAGER_IDX], manager)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

QtVariantEditorFactoryWrapper::~QtVariantEditorFactoryWrapper()
{
    SbkObject *wrapper = Shiboken::BindingManager::instance().retrieveWrapper(this);
    Shiboken::Object::destroy(wrapper, this);
}

// Target ---------------------------------------------------------

extern "C" {
static int
Sbk_QtVariantEditorFactory_Init(PyObject *self, PyObject *args, PyObject *kwds)
{
    SBK_UNUSED(kwds)
    SbkObject *sbkSelf = reinterpret_cast<SbkObject *>(self);
    PySide::Feature::Select(self);
    if (Shiboken::Object::isUserType(self) && !Shiboken::ObjectType::canCallConstructor(self->ob_type, Shiboken::SbkType< ::QtVariantEditorFactory >()))
        return -1;

    ::QtVariantEditorFactoryWrapper *cptr{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtVariantEditorFactory.__init__";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp[1];
    SBK_UNUSED(pythonToCpp)
    const Py_ssize_t numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {nullptr};

    // invalid argument lengths
    errInfo.reset(Shiboken::checkInvalidArgumentCount(numArgs, 0, 1));
    if (!errInfo.isNull())
        goto Sbk_QtVariantEditorFactory_Init_TypeError;

    if (!PyArg_ParseTuple(args, "|O:QtVariantEditorFactory", &(pyArgs[0])))
        return -1;


    // Overloaded function decisor
    // 0: QtVariantEditorFactory::QtVariantEditorFactory(QObject*)
    if (numArgs == 0) {
        overloadId = 0; // QtVariantEditorFactory(QObject*)
    } else if (numArgs >= 1
        && (pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkPySide6_QtCoreTypes[SBK_QOBJECT_IDX], (pyArgs[0])))) {
        overloadId = 0; // QtVariantEditorFactory(QObject*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtVariantEditorFactory_Init_TypeError;

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
                    goto Sbk_QtVariantEditorFactory_Init_TypeError;
                }
                if (value) {
                    pyArgs[0] = value;
                    if (!(pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkPySide6_QtCoreTypes[SBK_QOBJECT_IDX], (pyArgs[0]))))
                        goto Sbk_QtVariantEditorFactory_Init_TypeError;
                }
                PyDict_DelItem(kwds_dup, key_parent);
            }
            if (PyDict_Size(kwds_dup) > 0) {
                errInfo.reset(kwds_dup.release());
                goto Sbk_QtVariantEditorFactory_Init_TypeError;
            }
        }
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return -1;
        ::QObject *cppArg0 = nullptr;
        if (pythonToCpp[0])
            pythonToCpp[0](pyArgs[0], &cppArg0);

        if (!PyErr_Occurred()) {
            // QtVariantEditorFactory(QObject*)
            cptr = new ::QtVariantEditorFactoryWrapper(cppArg0);
        }
    }

    if (PyErr_Occurred() || !Shiboken::Object::setCppPointer(sbkSelf, Shiboken::SbkType< ::QtVariantEditorFactory >(), cptr)) {
        delete cptr;
        return -1;
    }
    if (!cptr) goto Sbk_QtVariantEditorFactory_Init_TypeError;

    Shiboken::Object::setValidCpp(sbkSelf, true);
    Shiboken::Object::setHasCppWrapper(sbkSelf, true);
    if (Shiboken::BindingManager::instance().hasWrapper(cptr)) {
        Shiboken::BindingManager::instance().releaseWrapper(Shiboken::BindingManager::instance().retrieveWrapper(cptr));
    }
    Shiboken::BindingManager::instance().registerWrapper(sbkSelf, cptr);


    return 1;

    Sbk_QtVariantEditorFactory_Init_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return -1;
}

static PyObject *Sbk_QtVariantEditorFactoryFunc_connectPropertyManager(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtVariantEditorFactoryWrapper *>(reinterpret_cast< ::QtVariantEditorFactory *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTVARIANTEDITORFACTORY_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtVariantEditorFactory.connectPropertyManager";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtVariantEditorFactory::connectPropertyManager(QtVariantPropertyManager*)
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTVARIANTPROPERTYMANAGER_IDX], (pyArg)))) {
        overloadId = 0; // connectPropertyManager(QtVariantPropertyManager*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtVariantEditorFactoryFunc_connectPropertyManager_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtVariantPropertyManager *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // connectPropertyManager(QtVariantPropertyManager*)
            static_cast<::QtVariantEditorFactoryWrapper *>(cppSelf)->QtVariantEditorFactoryWrapper::connectPropertyManager_protected(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtVariantEditorFactoryFunc_connectPropertyManager_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtVariantEditorFactoryFunc_createEditor(PyObject *self, PyObject *args)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtVariantEditorFactoryWrapper *>(reinterpret_cast< ::QtVariantEditorFactory *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTVARIANTEDITORFACTORY_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtVariantEditorFactory.createEditor";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp[3];
    SBK_UNUSED(pythonToCpp)
    const Py_ssize_t numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {nullptr, nullptr, nullptr};

    // invalid argument lengths

    if (!PyArg_UnpackTuple(args, "createEditor", 3, 3, &(pyArgs[0]), &(pyArgs[1]), &(pyArgs[2])))
        return {};


    // Overloaded function decisor
    // 0: QtVariantEditorFactory::createEditor(QtVariantPropertyManager*,QtProperty*,QWidget*)->QWidget*
    if (numArgs == 3
        && (pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTVARIANTPROPERTYMANAGER_IDX], (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArgs[1])))
        && (pythonToCpp[2] = Shiboken::Conversions::pythonToCppPointerConversion(SbkPySide6_QtWidgetsTypes[SBK_QWIDGET_IDX], (pyArgs[2])))) {
        overloadId = 0; // createEditor(QtVariantPropertyManager*,QtProperty*,QWidget*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtVariantEditorFactoryFunc_createEditor_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return {};
        ::QtVariantPropertyManager *cppArg0;
        pythonToCpp[0](pyArgs[0], &cppArg0);
        if (!Shiboken::Object::isValid(pyArgs[1]))
            return {};
        ::QtProperty *cppArg1;
        pythonToCpp[1](pyArgs[1], &cppArg1);
        if (!Shiboken::Object::isValid(pyArgs[2]))
            return {};
        ::QWidget *cppArg2;
        pythonToCpp[2](pyArgs[2], &cppArg2);

        if (!PyErr_Occurred()) {
            // createEditor(QtVariantPropertyManager*,QtProperty*,QWidget*)
            QWidget * cppResult = static_cast<::QtVariantEditorFactoryWrapper *>(cppSelf)->QtVariantEditorFactoryWrapper::createEditor_protected(cppArg0, cppArg1, cppArg2);
            pyResult = Shiboken::Conversions::pointerToPython(SbkPySide6_QtWidgetsTypes[SBK_QWIDGET_IDX], cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtVariantEditorFactoryFunc_createEditor_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtVariantEditorFactoryFunc_disconnectPropertyManager(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtVariantEditorFactoryWrapper *>(reinterpret_cast< ::QtVariantEditorFactory *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTVARIANTEDITORFACTORY_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtVariantEditorFactory.disconnectPropertyManager";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtVariantEditorFactory::disconnectPropertyManager(QtVariantPropertyManager*)
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTVARIANTPROPERTYMANAGER_IDX], (pyArg)))) {
        overloadId = 0; // disconnectPropertyManager(QtVariantPropertyManager*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtVariantEditorFactoryFunc_disconnectPropertyManager_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtVariantPropertyManager *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // disconnectPropertyManager(QtVariantPropertyManager*)
            static_cast<::QtVariantEditorFactoryWrapper *>(cppSelf)->QtVariantEditorFactoryWrapper::disconnectPropertyManager_protected(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtVariantEditorFactoryFunc_disconnectPropertyManager_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}


static const char *Sbk_QtVariantEditorFactory_PropertyStrings[] = {
    nullptr // Sentinel
};

static PyMethodDef Sbk_QtVariantEditorFactory_methods[] = {
    {"connectPropertyManager", reinterpret_cast<PyCFunction>(Sbk_QtVariantEditorFactoryFunc_connectPropertyManager), METH_O, nullptr},
    {"createEditor", reinterpret_cast<PyCFunction>(Sbk_QtVariantEditorFactoryFunc_createEditor), METH_VARARGS, nullptr},
    {"disconnectPropertyManager", reinterpret_cast<PyCFunction>(Sbk_QtVariantEditorFactoryFunc_disconnectPropertyManager), METH_O, nullptr},

    {nullptr, nullptr, 0, nullptr} // Sentinel
};

static int Sbk_QtVariantEditorFactory_setattro(PyObject *self, PyObject *name, PyObject *value)
{
    PySide::Feature::Select(self);
    if (value && PyCallable_Check(value)) {
        auto plain_inst = reinterpret_cast< ::QtVariantEditorFactory *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTVARIANTEDITORFACTORY_IDX], reinterpret_cast<SbkObject *>(self)));
        auto inst = dynamic_cast<QtVariantEditorFactoryWrapper *>(plain_inst);
        if (inst)
            inst->resetPyMethodCache();
    }
    return PyObject_GenericSetAttr(self, name, value);
}

} // extern "C"

static int Sbk_QtVariantEditorFactory_traverse(PyObject *self, visitproc visit, void *arg)
{
    return SbkObject_TypeF()->tp_traverse(self, visit, arg);
}
static int Sbk_QtVariantEditorFactory_clear(PyObject *self)
{
    return reinterpret_cast<PyTypeObject *>(SbkObject_TypeF())->tp_clear(self);
}
// Class Definition -----------------------------------------------
extern "C" {
static PyTypeObject *_Sbk_QtVariantEditorFactory_Type = nullptr;
static PyTypeObject *Sbk_QtVariantEditorFactory_TypeF(void)
{
    return _Sbk_QtVariantEditorFactory_Type;
}

static PyType_Slot Sbk_QtVariantEditorFactory_slots[] = {
    {Py_tp_base,        nullptr}, // inserted by introduceWrapperType
    {Py_tp_dealloc,     reinterpret_cast<void *>(&SbkDeallocWrapper)},
    {Py_tp_repr,        nullptr},
    {Py_tp_hash,        nullptr},
    {Py_tp_call,        nullptr},
    {Py_tp_str,         nullptr},
    {Py_tp_getattro,    nullptr},
    {Py_tp_setattro,    reinterpret_cast<void *>(Sbk_QtVariantEditorFactory_setattro)},
    {Py_tp_traverse,    reinterpret_cast<void *>(Sbk_QtVariantEditorFactory_traverse)},
    {Py_tp_clear,       reinterpret_cast<void *>(Sbk_QtVariantEditorFactory_clear)},
    {Py_tp_richcompare, nullptr},
    {Py_tp_iter,        nullptr},
    {Py_tp_iternext,    nullptr},
    {Py_tp_methods,     reinterpret_cast<void *>(Sbk_QtVariantEditorFactory_methods)},
    {Py_tp_getset,      nullptr},
    {Py_tp_init,        reinterpret_cast<void *>(Sbk_QtVariantEditorFactory_Init)},
    {Py_tp_new,         reinterpret_cast<void *>(SbkObject_tp_new)},
    {0, nullptr}
};
static PyType_Spec Sbk_QtVariantEditorFactory_spec = {
    "1:qtpropertybrowser.QtVariantEditorFactory",
    sizeof(SbkObject),
    0,
    Py_TPFLAGS_DEFAULT|Py_TPFLAGS_BASETYPE|Py_TPFLAGS_HAVE_GC,
    Sbk_QtVariantEditorFactory_slots
};

} //extern "C"


// Type conversion functions.

// Python to C++ pointer conversion - returns the C++ object of the Python wrapper (keeps object identity).
static void QtVariantEditorFactory_PythonToCpp_QtVariantEditorFactory_PTR(PyObject *pyIn, void *cppOut)
{
    Shiboken::Conversions::pythonToCppPointer(Sbk_QtVariantEditorFactory_TypeF(), pyIn, cppOut);
}
static PythonToCppFunc is_QtVariantEditorFactory_PythonToCpp_QtVariantEditorFactory_PTR_Convertible(PyObject *pyIn)
{
    if (pyIn == Py_None)
        return Shiboken::Conversions::nonePythonToCppNullPtr;
    if (PyObject_TypeCheck(pyIn, Sbk_QtVariantEditorFactory_TypeF()))
        return QtVariantEditorFactory_PythonToCpp_QtVariantEditorFactory_PTR;
    return {};
}

// C++ to Python pointer conversion - tries to find the Python wrapper for the C++ object (keeps object identity).
static PyObject *QtVariantEditorFactory_PTR_CppToPython_QtVariantEditorFactory(const void *cppIn)
{
    auto pyOut = reinterpret_cast<PyObject *>(Shiboken::BindingManager::instance().retrieveWrapper(cppIn));
    if (pyOut) {
        Py_INCREF(pyOut);
        return pyOut;
    }
    bool changedTypeName = false;
    auto tCppIn = reinterpret_cast<const ::QtVariantEditorFactory *>(cppIn);
    const char *typeName = typeid(*tCppIn).name();
    auto sbkType = Shiboken::ObjectType::typeForTypeName(typeName);
    if (sbkType && Shiboken::ObjectType::hasSpecialCastFunction(sbkType)) {
        typeName = typeNameOf(tCppIn);
        changedTypeName = true;
    }
    PyObject *result = Shiboken::Object::newObject(Sbk_QtVariantEditorFactory_TypeF(), const_cast<void *>(cppIn), false, /* exactType */ changedTypeName, typeName);
    if (changedTypeName)
        delete [] typeName;
    return result;
}

// The signatures string for the functions.
// Multiple signatures have their index "n:" in front.
static const char *QtVariantEditorFactory_SignatureStrings[] = {
    "qtpropertybrowser.QtVariantEditorFactory(self,parent:PySide6.QtCore.QObject=nullptr)",
    "qtpropertybrowser.QtVariantEditorFactory.connectPropertyManager(self,manager:qtpropertybrowser.QtVariantPropertyManager)",
    "qtpropertybrowser.QtVariantEditorFactory.createEditor(self,manager:qtpropertybrowser.QtVariantPropertyManager,property:qtpropertybrowser.QtProperty,parent:PySide6.QtWidgets.QWidget)->PySide6.QtWidgets.QWidget",
    "qtpropertybrowser.QtVariantEditorFactory.disconnectPropertyManager(self,manager:qtpropertybrowser.QtVariantPropertyManager)",
    nullptr}; // Sentinel

void init_QtVariantEditorFactory(PyObject *module)
{
    _Sbk_QtVariantEditorFactory_Type = Shiboken::ObjectType::introduceWrapperType(
        module,
        "QtVariantEditorFactory",
        "QtVariantEditorFactory*",
        &Sbk_QtVariantEditorFactory_spec,
        &Shiboken::callCppDestructor< ::QtVariantEditorFactory >,
        0,
        0,
        0);
    auto *pyType = Sbk_QtVariantEditorFactory_TypeF(); // references _Sbk_QtVariantEditorFactory_Type
    InitSignatureStrings(pyType, QtVariantEditorFactory_SignatureStrings);
    SbkObjectType_SetPropertyStrings(pyType, Sbk_QtVariantEditorFactory_PropertyStrings);
    SbkqtpropertybrowserTypes[SBK_QTVARIANTEDITORFACTORY_IDX] = pyType;

    // Register Converter
    SbkConverter *converter = Shiboken::Conversions::createConverter(pyType,
        QtVariantEditorFactory_PythonToCpp_QtVariantEditorFactory_PTR,
        is_QtVariantEditorFactory_PythonToCpp_QtVariantEditorFactory_PTR_Convertible,
        QtVariantEditorFactory_PTR_CppToPython_QtVariantEditorFactory);

    Shiboken::Conversions::registerConverterName(converter, "QtVariantEditorFactory");
    Shiboken::Conversions::registerConverterName(converter, "QtVariantEditorFactory*");
    Shiboken::Conversions::registerConverterName(converter, "QtVariantEditorFactory&");
    Shiboken::Conversions::registerConverterName(converter, typeid(::QtVariantEditorFactory).name());
    Shiboken::Conversions::registerConverterName(converter, typeid(::QtVariantEditorFactoryWrapper).name());


    QtVariantEditorFactoryWrapper::pysideInitQtMetaTypes();
}
