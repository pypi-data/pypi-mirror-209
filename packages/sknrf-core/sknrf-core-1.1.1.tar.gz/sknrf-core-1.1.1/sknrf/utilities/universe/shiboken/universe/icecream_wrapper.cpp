
// default includes
#include <shiboken.h>

// module include
#include "universe_python.h"

// main header
#include "icecream_wrapper.h"

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

void IcecreamWrapper::resetPyMethodCache()
{
    std::fill_n(m_PyMethodCache, sizeof(m_PyMethodCache) / sizeof(m_PyMethodCache[0]), false);
}

IcecreamWrapper::IcecreamWrapper(const std::string & flavor) : Icecream(flavor)
{
    resetPyMethodCache();
    // ... middle
}

Icecream * IcecreamWrapper::clone()
{
    if (m_PyMethodCache[0])
        return this->::Icecream::clone();
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return nullptr;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "clone";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[0] = true;
        gil.release();
        return this->::Icecream::clone();
    }

    Shiboken::AutoDecRef pyArgs(PyTuple_New(0));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return nullptr;
    }
    bool invalidateArg0 = pyResult->ob_refcnt == 1;
    if (invalidateArg0)
        Shiboken::Object::releaseOwnership(pyResult.object());
    // Check return type
    Shiboken::Conversions::PythonToCppConversion pythonToCpp =
        Shiboken::Conversions::pythonToCppPointerConversion(SbkuniverseTypes[SBK_ICECREAM_IDX], pyResult);
    if (!pythonToCpp) {
        Shiboken::Warnings::warnInvalidReturnValue("Icecream", "clone", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< Icecream >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return nullptr;
    }
    ::Icecream *cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

const std::string IcecreamWrapper::getFlavor()
{
    if (m_PyMethodCache[1])
        return this->::Icecream::getFlavor();
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return ::std::string();
    static PyObject *nameCache[2] = {};
    static const char *funcName = "getFlavor";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[1] = true;
        gil.release();
        return this->::Icecream::getFlavor();
    }

    Shiboken::AutoDecRef pyArgs(PyTuple_New(0));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return ::std::string();
    }
    // Check return type
    Shiboken::Conversions::PythonToCppConversion pythonToCpp =
        Shiboken::Conversions::pythonToCppConversion(Shiboken::Conversions::PrimitiveTypeConverter<std::string>(), pyResult);
    if (!pythonToCpp) {
        Shiboken::Warnings::warnInvalidReturnValue("Icecream", "getFlavor", "std::string", Py_TYPE(pyResult)->tp_name);
        return ::std::string();
    }
    ::std::string cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

IcecreamWrapper::~IcecreamWrapper()
{
    SbkObject *wrapper = Shiboken::BindingManager::instance().retrieveWrapper(this);
    Shiboken::Object::destroy(wrapper, this);
}

// Target ---------------------------------------------------------

extern "C" {
static int
Sbk_Icecream_Init(PyObject *self, PyObject *args, PyObject *kwds)
{
    SBK_UNUSED(kwds)
    SbkObject *sbkSelf = reinterpret_cast<SbkObject *>(self);
    if (Shiboken::Object::isUserType(self) && !Shiboken::ObjectType::canCallConstructor(self->ob_type, Shiboken::SbkType< ::Icecream >()))
        return -1;

    ::IcecreamWrapper *cptr{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "universe.Icecream.__init__";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp[1];
    SBK_UNUSED(pythonToCpp)
    const Py_ssize_t numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {nullptr};

    // invalid argument lengths

    if (!PyArg_UnpackTuple(args, "Icecream", 1, 1, &(pyArgs[0])))
        return -1;


    // Overloaded function decisor
    // 0: Icecream::Icecream(std::string)
    if (numArgs == 1
        && (pythonToCpp[0] = Shiboken::Conversions::pythonToCppConversion(Shiboken::Conversions::PrimitiveTypeConverter<std::string>(), (pyArgs[0])))) {
        overloadId = 0; // Icecream(std::string)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_Icecream_Init_TypeError;

    // Call function/method
    {
        ::std::string cppArg0;
        pythonToCpp[0](pyArgs[0], &cppArg0);

        if (!PyErr_Occurred()) {
            // Icecream(std::string)
            cptr = new ::IcecreamWrapper(cppArg0);
        }
    }

    if (PyErr_Occurred() || !Shiboken::Object::setCppPointer(sbkSelf, Shiboken::SbkType< ::Icecream >(), cptr)) {
        delete cptr;
        return -1;
    }
    if (!cptr) goto Sbk_Icecream_Init_TypeError;

    Shiboken::Object::setValidCpp(sbkSelf, true);
    Shiboken::Object::setHasCppWrapper(sbkSelf, true);
    if (Shiboken::BindingManager::instance().hasWrapper(cptr)) {
        Shiboken::BindingManager::instance().releaseWrapper(Shiboken::BindingManager::instance().retrieveWrapper(cptr));
    }
    Shiboken::BindingManager::instance().registerWrapper(sbkSelf, cptr);


    return 1;

    Sbk_Icecream_Init_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return -1;
}

static PyObject *Sbk_IcecreamFunc_clone(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = reinterpret_cast< ::Icecream *>(Shiboken::Conversions::cppPointer(SbkuniverseTypes[SBK_ICECREAM_IDX], reinterpret_cast<SbkObject *>(self)));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // clone()
            Icecream * cppResult = Shiboken::Object::hasCppWrapper(reinterpret_cast<SbkObject *>(self))
                ? cppSelf->::Icecream::clone()
                : cppSelf->clone();
            pyResult = Shiboken::Conversions::pointerToPython(SbkuniverseTypes[SBK_ICECREAM_IDX], cppResult);

            // Ownership transferences.
            Shiboken::Object::releaseOwnership(pyResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_IcecreamFunc_getFlavor(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = reinterpret_cast< ::Icecream *>(Shiboken::Conversions::cppPointer(SbkuniverseTypes[SBK_ICECREAM_IDX], reinterpret_cast<SbkObject *>(self)));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // getFlavor()
            const std::string cppResult = Shiboken::Object::hasCppWrapper(reinterpret_cast<SbkObject *>(self))
                ? cppSelf->::Icecream::getFlavor()
                : cppSelf->getFlavor();
            pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<std::string>(), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyMethodDef Sbk_Icecream_methods[] = {
    {"clone", reinterpret_cast<PyCFunction>(Sbk_IcecreamFunc_clone), METH_NOARGS, nullptr},
    {"getFlavor", reinterpret_cast<PyCFunction>(Sbk_IcecreamFunc_getFlavor), METH_NOARGS, nullptr},

    {nullptr, nullptr, 0, nullptr} // Sentinel
};

static int Sbk_Icecream_setattro(PyObject *self, PyObject *name, PyObject *value)
{
    if (value && PyCallable_Check(value)) {
        auto plain_inst = reinterpret_cast< ::Icecream *>(Shiboken::Conversions::cppPointer(SbkuniverseTypes[SBK_ICECREAM_IDX], reinterpret_cast<SbkObject *>(self)));
        auto inst = dynamic_cast<IcecreamWrapper *>(plain_inst);
        if (inst)
            inst->resetPyMethodCache();
    }
    return PyObject_GenericSetAttr(self, name, value);
}

} // extern "C"

static int Sbk_Icecream_traverse(PyObject *self, visitproc visit, void *arg)
{
    return SbkObject_TypeF()->tp_traverse(self, visit, arg);
}
static int Sbk_Icecream_clear(PyObject *self)
{
    return reinterpret_cast<PyTypeObject *>(SbkObject_TypeF())->tp_clear(self);
}
// Class Definition -----------------------------------------------
extern "C" {
static PyTypeObject *_Sbk_Icecream_Type = nullptr;
static PyTypeObject *Sbk_Icecream_TypeF(void)
{
    return _Sbk_Icecream_Type;
}

static PyType_Slot Sbk_Icecream_slots[] = {
    {Py_tp_base,        nullptr}, // inserted by introduceWrapperType
    {Py_tp_dealloc,     reinterpret_cast<void *>(&SbkDeallocWrapper)},
    {Py_tp_repr,        nullptr},
    {Py_tp_hash,        nullptr},
    {Py_tp_call,        nullptr},
    {Py_tp_str,         nullptr},
    {Py_tp_getattro,    nullptr},
    {Py_tp_setattro,    reinterpret_cast<void *>(Sbk_Icecream_setattro)},
    {Py_tp_traverse,    reinterpret_cast<void *>(Sbk_Icecream_traverse)},
    {Py_tp_clear,       reinterpret_cast<void *>(Sbk_Icecream_clear)},
    {Py_tp_richcompare, nullptr},
    {Py_tp_iter,        nullptr},
    {Py_tp_iternext,    nullptr},
    {Py_tp_methods,     reinterpret_cast<void *>(Sbk_Icecream_methods)},
    {Py_tp_getset,      nullptr},
    {Py_tp_init,        reinterpret_cast<void *>(Sbk_Icecream_Init)},
    {Py_tp_new,         reinterpret_cast<void *>(SbkObject_tp_new)},
    {0, nullptr}
};
static PyType_Spec Sbk_Icecream_spec = {
    "1:universe.Icecream",
    sizeof(SbkObject),
    0,
    Py_TPFLAGS_DEFAULT|Py_TPFLAGS_BASETYPE|Py_TPFLAGS_HAVE_GC,
    Sbk_Icecream_slots
};

} //extern "C"


// Type conversion functions.

// Python to C++ pointer conversion - returns the C++ object of the Python wrapper (keeps object identity).
static void Icecream_PythonToCpp_Icecream_PTR(PyObject *pyIn, void *cppOut)
{
    Shiboken::Conversions::pythonToCppPointer(Sbk_Icecream_TypeF(), pyIn, cppOut);
}
static PythonToCppFunc is_Icecream_PythonToCpp_Icecream_PTR_Convertible(PyObject *pyIn)
{
    if (pyIn == Py_None)
        return Shiboken::Conversions::nonePythonToCppNullPtr;
    if (PyObject_TypeCheck(pyIn, Sbk_Icecream_TypeF()))
        return Icecream_PythonToCpp_Icecream_PTR;
    return {};
}

// C++ to Python pointer conversion - tries to find the Python wrapper for the C++ object (keeps object identity).
static PyObject *Icecream_PTR_CppToPython_Icecream(const void *cppIn)
{
    auto pyOut = reinterpret_cast<PyObject *>(Shiboken::BindingManager::instance().retrieveWrapper(cppIn));
    if (pyOut) {
        Py_INCREF(pyOut);
        return pyOut;
    }
    bool changedTypeName = false;
    auto tCppIn = reinterpret_cast<const ::Icecream *>(cppIn);
    const char *typeName = typeid(*tCppIn).name();
    auto sbkType = Shiboken::ObjectType::typeForTypeName(typeName);
    if (sbkType && Shiboken::ObjectType::hasSpecialCastFunction(sbkType)) {
        typeName = typeNameOf(tCppIn);
        changedTypeName = true;
    }
    PyObject *result = Shiboken::Object::newObject(Sbk_Icecream_TypeF(), const_cast<void *>(cppIn), false, /* exactType */ changedTypeName, typeName);
    if (changedTypeName)
        delete [] typeName;
    return result;
}

// The signatures string for the functions.
// Multiple signatures have their index "n:" in front.
static const char *Icecream_SignatureStrings[] = {
    "universe.Icecream(self,flavor:std.string)",
    "universe.Icecream.clone(self)->universe.Icecream",
    "universe.Icecream.getFlavor(self)->std.string",
    nullptr}; // Sentinel

void init_Icecream(PyObject *module)
{
    _Sbk_Icecream_Type = Shiboken::ObjectType::introduceWrapperType(
        module,
        "Icecream",
        "Icecream*",
        &Sbk_Icecream_spec,
        &Shiboken::callCppDestructor< ::Icecream >,
        0,
        0,
        0);
    auto *pyType = Sbk_Icecream_TypeF(); // references _Sbk_Icecream_Type
    InitSignatureStrings(pyType, Icecream_SignatureStrings);
    SbkuniverseTypes[SBK_ICECREAM_IDX] = pyType;

    // Register Converter
    SbkConverter *converter = Shiboken::Conversions::createConverter(pyType,
        Icecream_PythonToCpp_Icecream_PTR,
        is_Icecream_PythonToCpp_Icecream_PTR_Convertible,
        Icecream_PTR_CppToPython_Icecream);

    Shiboken::Conversions::registerConverterName(converter, "Icecream");
    Shiboken::Conversions::registerConverterName(converter, "Icecream*");
    Shiboken::Conversions::registerConverterName(converter, "Icecream&");
    Shiboken::Conversions::registerConverterName(converter, typeid(::Icecream).name());
    Shiboken::Conversions::registerConverterName(converter, typeid(::IcecreamWrapper).name());


}
