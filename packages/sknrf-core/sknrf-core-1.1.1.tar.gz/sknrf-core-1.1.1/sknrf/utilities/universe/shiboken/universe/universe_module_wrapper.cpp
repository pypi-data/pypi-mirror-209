
#include <sbkpython.h>
#include <shiboken.h>
#include <algorithm>
#include <signature.h>
#include "universe_python.h"



// Current module's type array.
PyTypeObject **SbkuniverseTypes = nullptr;
// Current module's PyObject pointer.
PyObject *SbkuniverseModuleObject = nullptr;
// Current module's converter array.
SbkConverter **SbkuniverseTypeConverters = nullptr;
// Global functions ------------------------------------------------------------

static PyMethodDef universe_methods[] = {
    {nullptr, nullptr, 0, nullptr} // Sentinel
};

// Classes initialization functions ------------------------------------------------------------
void init_Truck(PyObject *module);
void init_Icecream(PyObject *module);


// Module initialization ------------------------------------------------------------
static struct PyModuleDef moduledef = {
    /* m_base     */ PyModuleDef_HEAD_INIT,
    /* m_name     */ "universe",
    /* m_doc      */ nullptr,
    /* m_size     */ -1,
    /* m_methods  */ universe_methods,
    /* m_reload   */ nullptr,
    /* m_traverse */ nullptr,
    /* m_clear    */ nullptr,
    /* m_free     */ nullptr
};

// The signatures string for the global functions.
// Multiple signatures have their index "n:" in front.
static const char *universe_SignatureStrings[] = {
    nullptr}; // Sentinel

extern "C" LIBSHIBOKEN_EXPORT PyObject *PyInit_universe()
{
    if (SbkuniverseModuleObject != nullptr)
        return SbkuniverseModuleObject;
    // Create an array of wrapper types for the current module.
    static PyTypeObject *cppApi[SBK_universe_IDX_COUNT];
    SbkuniverseTypes = cppApi;

    // Create an array of primitive type converters for the current module.
    static SbkConverter *sbkConverters[SBK_universe_CONVERTERS_IDX_COUNT];
    SbkuniverseTypeConverters = sbkConverters;

    PyObject *module = Shiboken::Module::create("universe", &moduledef);

    // Make module available from global scope
    SbkuniverseModuleObject = module;

    // Initialize classes in the type system
    init_Truck(module);
    init_Icecream(module);
    // Register primitive types converters.
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<long>(), "__blkcnt64_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<long>(), "__blkcnt_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<long>(), "__blksize_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<char>(), "__caddr_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<long>(), "__clock_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<int>(), "__clockid_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<int>(), "__compar_d_fn_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<int>(), "__compar_fn_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<int>(), "__daddr_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned long>(), "__dev_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned long>(), "__fsblkcnt64_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned long>(), "__fsblkcnt_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned long>(), "__fsfilcnt64_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned long>(), "__fsfilcnt_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<long>(), "__fsword_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned int>(), "__gid_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned int>(), "__id_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned long>(), "__ino64_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned long>(), "__ino_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<short>(), "__int16_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<int>(), "__int32_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<long>(), "__int64_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<signed char>(), "__int8_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<short>(), "__int_least16_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<int>(), "__int_least32_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<long>(), "__int_least64_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<signed char>(), "__int_least8_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<long>(), "__intmax_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<long>(), "__intptr_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<int>(), "__key_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<long>(), "__loff_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned int>(), "__mode_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned long>(), "__nlink_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<long>(), "__off64_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<long>(), "__off_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<int>(), "__pid_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<long>(), "__quad_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned long>(), "__rlim64_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned long>(), "__rlim_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<int>(), "__sig_atomic_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned int>(), "__socklen_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<long>(), "__ssize_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<long>(), "__suseconds64_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<long>(), "__suseconds_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<long>(), "__syscall_slong_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned long>(), "__syscall_ulong_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<long>(), "__time_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned char>(), "__u_char");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned int>(), "__u_int");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned long>(), "__u_long");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned long>(), "__u_quad_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned short>(), "__u_short");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned int>(), "__uid_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned short>(), "__uint16_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned int>(), "__uint32_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned long>(), "__uint64_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned char>(), "__uint8_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned short>(), "__uint_least16_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned int>(), "__uint_least32_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned long>(), "__uint_least64_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned char>(), "__uint_least8_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned long>(), "__uintmax_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned int>(), "__useconds_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<long>(), "blkcnt64_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<long>(), "blkcnt_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<long>(), "blksize_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<char>(), "caddr_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<int>(), "comparison_fn_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<int>(), "daddr_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned long>(), "dev_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned long>(), "fsblkcnt64_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned long>(), "fsblkcnt_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned long>(), "fsfilcnt64_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned long>(), "fsfilcnt_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned int>(), "gid_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned int>(), "id_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned long>(), "ino64_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned long>(), "ino_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<short>(), "int16_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<int>(), "int32_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<long>(), "int64_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<signed char>(), "int8_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<long>(), "int_fast16_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<long>(), "int_fast32_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<long>(), "int_fast64_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<signed char>(), "int_fast8_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<short>(), "int_least16_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<int>(), "int_least32_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<long>(), "int_least64_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<signed char>(), "int_least8_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<long>(), "intmax_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<long>(), "intptr_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<int>(), "key_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<long>(), "loff_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned int>(), "mode_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned long>(), "nlink_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<long>(), "off64_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<long>(), "off_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<long>(), "quad_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<long>(), "register_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned long>(), "size_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<long>(), "ssize_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<long>(), "suseconds_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned char>(), "u_char");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned int>(), "u_int");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned short>(), "u_int16_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned int>(), "u_int32_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned long>(), "u_int64_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned char>(), "u_int8_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned long>(), "u_long");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned long>(), "u_quad_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned short>(), "u_short");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned int>(), "uid_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned int>(), "uint");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned short>(), "uint16_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned int>(), "uint32_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned long>(), "uint64_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned char>(), "uint8_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned long>(), "uint_fast16_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned long>(), "uint_fast32_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned long>(), "uint_fast64_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned char>(), "uint_fast8_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned short>(), "uint_least16_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned int>(), "uint_least32_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned long>(), "uint_least64_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned char>(), "uint_least8_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned long>(), "uintmax_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned long>(), "uintptr_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned long>(), "ulong");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned int>(), "useconds_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned short>(), "ushort");

    Shiboken::Module::registerTypes(module, SbkuniverseTypes);
    Shiboken::Module::registerTypeConverters(module, SbkuniverseTypeConverters);

    if (PyErr_Occurred()) {
        PyErr_Print();
        Py_FatalError("can't initialize module universe");
    }
    FinishSignatureInitialization(module, universe_SignatureStrings);

    return module;
}
