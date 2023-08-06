
// default includes
#include <shiboken.h>

// module include
#include "universe_python.h"

// main header
#include "truck_wrapper.h"

// Argument includes
#include <icecream.h>
#include <truck.h>

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


// Target ---------------------------------------------------------

extern "C" {
static int
Sbk_Truck_Init(PyObject *self, PyObject *args, PyObject *kwds)
{
    SBK_UNUSED(kwds)
    SbkObject *sbkSelf = reinterpret_cast<SbkObject *>(self);
    if (Shiboken::Object::isUserType(self) && !Shiboken::ObjectType::canCallConstructor(self->ob_type, Shiboken::SbkType< ::Truck >()))
        return -1;

    ::Truck *cptr{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "universe.Truck.__init__";
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
        goto Sbk_Truck_Init_TypeError;

    if (!PyArg_ParseTuple(args, "|O:Truck", &(pyArgs[0])))
        return -1;


    // Overloaded function decisor
    // 0: Truck::Truck(bool)
    // 1: Truck::Truck(Truck)
    if (numArgs == 0) {
        overloadId = 0; // Truck(bool)
    } else if (numArgs >= 1
        && (pythonToCpp[0] = Shiboken::Conversions::pythonToCppConversion(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), (pyArgs[0])))) {
        overloadId = 0; // Truck(bool)
    } else if (numArgs == 1
        && (pythonToCpp[0] = Shiboken::Conversions::pythonToCppReferenceConversion(SbkuniverseTypes[SBK_TRUCK_IDX], (pyArgs[0])))) {
        overloadId = 1; // Truck(Truck)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_Truck_Init_TypeError;

    // Call function/method
    switch (overloadId) {
        case 0: // Truck(bool leaveOnDestruction)
        {
            if (kwds && PyDict_Size(kwds) > 0) {
                PyObject *value{};
                Shiboken::AutoDecRef kwds_dup(PyDict_Copy(kwds));
                static PyObject *const key_leaveOnDestruction = Shiboken::String::createStaticString("leaveOnDestruction");
                if (PyDict_Contains(kwds, key_leaveOnDestruction)) {
                    value = PyDict_GetItem(kwds, key_leaveOnDestruction);
                    if (value && pyArgs[0]) {
                        errInfo.reset(key_leaveOnDestruction);
                        Py_INCREF(errInfo.object());
                        goto Sbk_Truck_Init_TypeError;
                    }
                    if (value) {
                        pyArgs[0] = value;
                        if (!(pythonToCpp[0] = Shiboken::Conversions::pythonToCppConversion(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), (pyArgs[0]))))
                            goto Sbk_Truck_Init_TypeError;
                    }
                    PyDict_DelItem(kwds_dup, key_leaveOnDestruction);
                }
                if (PyDict_Size(kwds_dup) > 0) {
                    errInfo.reset(kwds_dup.release());
                    goto Sbk_Truck_Init_TypeError;
                }
            }
            bool cppArg0 = false;
            if (pythonToCpp[0])
                pythonToCpp[0](pyArgs[0], &cppArg0);

            if (!PyErr_Occurred()) {
                // Truck(bool)
                cptr = new ::Truck(cppArg0);
            }
            break;
        }
        case 1: // Truck(const Truck & other)
        {
            if (kwds && PyDict_Size(kwds) > 0) {
                errInfo.reset(kwds);
                Py_INCREF(errInfo.object());
                goto Sbk_Truck_Init_TypeError;
            }
            if (!Shiboken::Object::isValid(pyArgs[0]))
                return -1;
            ::Truck cppArg0_local;
            ::Truck *cppArg0 = &cppArg0_local;
            if (pythonToCpp[0].isValue())
                pythonToCpp[0](pyArgs[0], &cppArg0_local);
            else
                pythonToCpp[0](pyArgs[0], &cppArg0);


            if (!PyErr_Occurred()) {
                // Truck(Truck)
                cptr = new ::Truck(*cppArg0);
            }
            break;
        }
    }

    if (PyErr_Occurred() || !Shiboken::Object::setCppPointer(sbkSelf, Shiboken::SbkType< ::Truck >(), cptr)) {
        delete cptr;
        return -1;
    }
    if (!cptr) goto Sbk_Truck_Init_TypeError;

    Shiboken::Object::setValidCpp(sbkSelf, true);
    if (Shiboken::BindingManager::instance().hasWrapper(cptr)) {
        Shiboken::BindingManager::instance().releaseWrapper(Shiboken::BindingManager::instance().retrieveWrapper(cptr));
    }
    Shiboken::BindingManager::instance().registerWrapper(sbkSelf, cptr);


    return 1;

    Sbk_Truck_Init_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return -1;
}

static PyObject *Sbk_TruckFunc_addIcecreamFlavor(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = reinterpret_cast< ::Truck *>(Shiboken::Conversions::cppPointer(SbkuniverseTypes[SBK_TRUCK_IDX], reinterpret_cast<SbkObject *>(self)));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "universe.Truck.addIcecreamFlavor";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: Truck::addIcecreamFlavor(Icecream*)
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppPointerConversion(SbkuniverseTypes[SBK_ICECREAM_IDX], (pyArg)))) {
        overloadId = 0; // addIcecreamFlavor(Icecream*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_TruckFunc_addIcecreamFlavor_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::Icecream *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // addIcecreamFlavor(Icecream*)
            cppSelf->addIcecreamFlavor(cppArg0);

            // Ownership transferences.
            Shiboken::Object::releaseOwnership(pyArg);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_TruckFunc_addIcecreamFlavor_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_TruckFunc_arrive(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = reinterpret_cast< ::Truck *>(Shiboken::Conversions::cppPointer(SbkuniverseTypes[SBK_TRUCK_IDX], reinterpret_cast<SbkObject *>(self)));
    SBK_UNUSED(cppSelf)

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // arrive()const
            const_cast<const ::Truck *>(cppSelf)->arrive();
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;
}

static PyObject *Sbk_TruckFunc_deliver(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = reinterpret_cast< ::Truck *>(Shiboken::Conversions::cppPointer(SbkuniverseTypes[SBK_TRUCK_IDX], reinterpret_cast<SbkObject *>(self)));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // deliver()const
            bool cppResult = const_cast<const ::Truck *>(cppSelf)->deliver();
            pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_TruckFunc_leave(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = reinterpret_cast< ::Truck *>(Shiboken::Conversions::cppPointer(SbkuniverseTypes[SBK_TRUCK_IDX], reinterpret_cast<SbkObject *>(self)));
    SBK_UNUSED(cppSelf)

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // leave()const
            const_cast<const ::Truck *>(cppSelf)->leave();
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;
}

static PyObject *Sbk_TruckFunc_printAvailableFlavors(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = reinterpret_cast< ::Truck *>(Shiboken::Conversions::cppPointer(SbkuniverseTypes[SBK_TRUCK_IDX], reinterpret_cast<SbkObject *>(self)));
    SBK_UNUSED(cppSelf)

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // printAvailableFlavors()const
            const_cast<const ::Truck *>(cppSelf)->printAvailableFlavors();
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;
}

static PyObject *Sbk_TruckFunc_setArrivalMessage(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = reinterpret_cast< ::Truck *>(Shiboken::Conversions::cppPointer(SbkuniverseTypes[SBK_TRUCK_IDX], reinterpret_cast<SbkObject *>(self)));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "universe.Truck.setArrivalMessage";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: Truck::setArrivalMessage(std::string)
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppConversion(Shiboken::Conversions::PrimitiveTypeConverter<std::string>(), (pyArg)))) {
        overloadId = 0; // setArrivalMessage(std::string)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_TruckFunc_setArrivalMessage_TypeError;

    // Call function/method
    {
        ::std::string cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // setArrivalMessage(std::string)
            cppSelf->setArrivalMessage(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_TruckFunc_setArrivalMessage_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_TruckFunc_setLeaveOnDestruction(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = reinterpret_cast< ::Truck *>(Shiboken::Conversions::cppPointer(SbkuniverseTypes[SBK_TRUCK_IDX], reinterpret_cast<SbkObject *>(self)));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "universe.Truck.setLeaveOnDestruction";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: Truck::setLeaveOnDestruction(bool)
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppConversion(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), (pyArg)))) {
        overloadId = 0; // setLeaveOnDestruction(bool)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_TruckFunc_setLeaveOnDestruction_TypeError;

    // Call function/method
    {
        bool cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // setLeaveOnDestruction(bool)
            cppSelf->setLeaveOnDestruction(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_TruckFunc_setLeaveOnDestruction_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_Truck___copy__(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto &cppSelf = *reinterpret_cast< ::Truck *>(Shiboken::Conversions::cppPointer(SbkuniverseTypes[SBK_TRUCK_IDX], reinterpret_cast<SbkObject *>(self)));
    PyObject *pyResult = Shiboken::Conversions::copyToPython(SbkuniverseTypes[SBK_TRUCK_IDX], &cppSelf);
    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyMethodDef Sbk_Truck_methods[] = {
    {"addIcecreamFlavor", reinterpret_cast<PyCFunction>(Sbk_TruckFunc_addIcecreamFlavor), METH_O, nullptr},
    {"arrive", reinterpret_cast<PyCFunction>(Sbk_TruckFunc_arrive), METH_NOARGS, nullptr},
    {"deliver", reinterpret_cast<PyCFunction>(Sbk_TruckFunc_deliver), METH_NOARGS, nullptr},
    {"leave", reinterpret_cast<PyCFunction>(Sbk_TruckFunc_leave), METH_NOARGS, nullptr},
    {"printAvailableFlavors", reinterpret_cast<PyCFunction>(Sbk_TruckFunc_printAvailableFlavors), METH_NOARGS, nullptr},
    {"setArrivalMessage", reinterpret_cast<PyCFunction>(Sbk_TruckFunc_setArrivalMessage), METH_O, nullptr},
    {"setLeaveOnDestruction", reinterpret_cast<PyCFunction>(Sbk_TruckFunc_setLeaveOnDestruction), METH_O, nullptr},

    {"__copy__", reinterpret_cast<PyCFunction>(Sbk_Truck___copy__), METH_NOARGS, nullptr},
    {nullptr, nullptr, 0, nullptr} // Sentinel
};

} // extern "C"

static int Sbk_Truck_traverse(PyObject *self, visitproc visit, void *arg)
{
    return SbkObject_TypeF()->tp_traverse(self, visit, arg);
}
static int Sbk_Truck_clear(PyObject *self)
{
    return reinterpret_cast<PyTypeObject *>(SbkObject_TypeF())->tp_clear(self);
}
// Class Definition -----------------------------------------------
extern "C" {
static PyTypeObject *_Sbk_Truck_Type = nullptr;
static PyTypeObject *Sbk_Truck_TypeF(void)
{
    return _Sbk_Truck_Type;
}

static PyType_Slot Sbk_Truck_slots[] = {
    {Py_tp_base,        nullptr}, // inserted by introduceWrapperType
    {Py_tp_dealloc,     reinterpret_cast<void *>(&SbkDeallocWrapper)},
    {Py_tp_repr,        nullptr},
    {Py_tp_hash,        nullptr},
    {Py_tp_call,        nullptr},
    {Py_tp_str,         nullptr},
    {Py_tp_getattro,    nullptr},
    {Py_tp_setattro,    nullptr},
    {Py_tp_traverse,    reinterpret_cast<void *>(Sbk_Truck_traverse)},
    {Py_tp_clear,       reinterpret_cast<void *>(Sbk_Truck_clear)},
    {Py_tp_richcompare, nullptr},
    {Py_tp_iter,        nullptr},
    {Py_tp_iternext,    nullptr},
    {Py_tp_methods,     reinterpret_cast<void *>(Sbk_Truck_methods)},
    {Py_tp_getset,      nullptr},
    {Py_tp_init,        reinterpret_cast<void *>(Sbk_Truck_Init)},
    {Py_tp_new,         reinterpret_cast<void *>(SbkObject_tp_new)},
    {0, nullptr}
};
static PyType_Spec Sbk_Truck_spec = {
    "1:universe.Truck",
    sizeof(SbkObject),
    0,
    Py_TPFLAGS_DEFAULT|Py_TPFLAGS_BASETYPE|Py_TPFLAGS_HAVE_GC,
    Sbk_Truck_slots
};

} //extern "C"


// Type conversion functions.

// Python to C++ pointer conversion - returns the C++ object of the Python wrapper (keeps object identity).
static void Truck_PythonToCpp_Truck_PTR(PyObject *pyIn, void *cppOut)
{
    Shiboken::Conversions::pythonToCppPointer(Sbk_Truck_TypeF(), pyIn, cppOut);
}
static PythonToCppFunc is_Truck_PythonToCpp_Truck_PTR_Convertible(PyObject *pyIn)
{
    if (pyIn == Py_None)
        return Shiboken::Conversions::nonePythonToCppNullPtr;
    if (PyObject_TypeCheck(pyIn, Sbk_Truck_TypeF()))
        return Truck_PythonToCpp_Truck_PTR;
    return {};
}

// C++ to Python pointer conversion - tries to find the Python wrapper for the C++ object (keeps object identity).
static PyObject *Truck_PTR_CppToPython_Truck(const void *cppIn)
{
    auto pyOut = reinterpret_cast<PyObject *>(Shiboken::BindingManager::instance().retrieveWrapper(cppIn));
    if (pyOut) {
        Py_INCREF(pyOut);
        return pyOut;
    }
    bool changedTypeName = false;
    auto tCppIn = reinterpret_cast<const ::Truck *>(cppIn);
    const char *typeName = typeid(*tCppIn).name();
    auto sbkType = Shiboken::ObjectType::typeForTypeName(typeName);
    if (sbkType && Shiboken::ObjectType::hasSpecialCastFunction(sbkType)) {
        typeName = typeNameOf(tCppIn);
        changedTypeName = true;
    }
    PyObject *result = Shiboken::Object::newObject(Sbk_Truck_TypeF(), const_cast<void *>(cppIn), false, /* exactType */ changedTypeName, typeName);
    if (changedTypeName)
        delete [] typeName;
    return result;
}

// C++ to Python copy conversion.
static PyObject *Truck_COPY_CppToPython_Truck(const void *cppIn)
{
    auto *source = reinterpret_cast<const ::Truck *>(cppIn);
    return Shiboken::Object::newObject(Sbk_Truck_TypeF(), new ::Truck(*source), true, true);
}

// Python to C++ copy conversion.
static void Truck_PythonToCpp_Truck_COPY(PyObject *pyIn, void *cppOut)
{
    *reinterpret_cast<::Truck *>(cppOut) = *reinterpret_cast< ::Truck *>(Shiboken::Conversions::cppPointer(SbkuniverseTypes[SBK_TRUCK_IDX], reinterpret_cast<SbkObject *>(pyIn)));
}
static PythonToCppFunc is_Truck_PythonToCpp_Truck_COPY_Convertible(PyObject *pyIn)
{
    if (PyObject_TypeCheck(pyIn, Sbk_Truck_TypeF()))
        return Truck_PythonToCpp_Truck_COPY;
    return {};
}

// Implicit conversions.
static void bool_PythonToCpp_Truck(PyObject *pyIn, void *cppOut)
{
    bool cppIn;
    Shiboken::Conversions::pythonToCppCopy(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), pyIn, &cppIn);
    *reinterpret_cast<::Truck *>(cppOut) = ::Truck(cppIn);
}
static PythonToCppFunc is_bool_PythonToCpp_Truck_Convertible(PyObject *pyIn)
{
    if (PyBool_Check(pyIn))
        return bool_PythonToCpp_Truck;
    return {};
}

// The signatures string for the functions.
// Multiple signatures have their index "n:" in front.
static const char *Truck_SignatureStrings[] = {
    "1:universe.Truck(self,leaveOnDestruction:bool=false)",
    "0:universe.Truck(self,other:typing.Union[universe.Truck, bool])",
    "universe.Truck.addIcecreamFlavor(self,icecream:universe.Icecream)",
    "universe.Truck.arrive(self)",
    "universe.Truck.deliver(self)->bool",
    "universe.Truck.leave(self)",
    "universe.Truck.printAvailableFlavors(self)",
    "universe.Truck.setArrivalMessage(self,message:std.string)",
    "universe.Truck.setLeaveOnDestruction(self,value:bool)",
    "universe.Truck.__copy__()",
    nullptr}; // Sentinel

void init_Truck(PyObject *module)
{
    _Sbk_Truck_Type = Shiboken::ObjectType::introduceWrapperType(
        module,
        "Truck",
        "Truck",
        &Sbk_Truck_spec,
        &Shiboken::callCppDestructor< ::Truck >,
        0,
        0,
        0);
    auto *pyType = Sbk_Truck_TypeF(); // references _Sbk_Truck_Type
    InitSignatureStrings(pyType, Truck_SignatureStrings);
    SbkuniverseTypes[SBK_TRUCK_IDX] = pyType;

    // Register Converter
    SbkConverter *converter = Shiboken::Conversions::createConverter(pyType,
        Truck_PythonToCpp_Truck_PTR,
        is_Truck_PythonToCpp_Truck_PTR_Convertible,
        Truck_PTR_CppToPython_Truck,
        Truck_COPY_CppToPython_Truck);

    Shiboken::Conversions::registerConverterName(converter, "Truck");
    Shiboken::Conversions::registerConverterName(converter, "Truck*");
    Shiboken::Conversions::registerConverterName(converter, "Truck&");
    Shiboken::Conversions::registerConverterName(converter, typeid(::Truck).name());

    // Add Python to C++ copy (value, not pointer neither reference) conversion to type converter.
    Shiboken::Conversions::addPythonToCppValueConversion(converter,
        Truck_PythonToCpp_Truck_COPY,
        is_Truck_PythonToCpp_Truck_COPY_Convertible);
    // Add implicit conversions to type converter.
    Shiboken::Conversions::addPythonToCppValueConversion(converter,
        bool_PythonToCpp_Truck,
        is_bool_PythonToCpp_Truck_Convertible);

}
