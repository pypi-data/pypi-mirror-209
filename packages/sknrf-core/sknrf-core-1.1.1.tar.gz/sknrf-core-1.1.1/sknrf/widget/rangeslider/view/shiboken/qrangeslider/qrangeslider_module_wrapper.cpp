
#include <sbkpython.h>
#include <shiboken.h>
#include <algorithm>
#include <signature.h>
#include <sbkcontainer.h>
#include <sbkstaticstrings.h>
#ifndef QT_NO_VERSION_TAGGING
#  define QT_NO_VERSION_TAGGING
#endif
#include <QtCore/QDebug>
#include <pysidecleanup.h>
#include <pysideqenum.h>
#include <feature_select.h>
#include <pysidestaticstrings.h>
#include "qrangeslider_python.h"

#include <QString>
#include <qvariant.h>


// Current module's type array.
PyTypeObject **SbkqrangesliderTypes = nullptr;
// Current module's PyObject pointer.
PyObject *SbkqrangesliderModuleObject = nullptr;
// Current module's converter array.
SbkConverter **SbkqrangesliderTypeConverters = nullptr;
void cleanTypesAttributes() {
    static PyObject *attrName = Shiboken::PyName::qtStaticMetaObject();
    for (int i = 0, imax = SBK_qrangeslider_IDX_COUNT; i < imax; i++) {
        PyObject *pyType = reinterpret_cast<PyObject *>(SbkqrangesliderTypes[i]);
        if (pyType && PyObject_HasAttr(pyType, attrName))
            PyObject_SetAttr(pyType, attrName, Py_None);
    }
}
// Global functions ------------------------------------------------------------

static PyMethodDef qrangeslider_methods[] = {
    {nullptr, nullptr, 0, nullptr} // Sentinel
};

// Classes initialization functions ------------------------------------------------------------
void init_QRangeSlider(PyObject *module);

// Required modules' type and converter arrays.
PyTypeObject **SbkPySide6_QtCoreTypes;
SbkConverter **SbkPySide6_QtCoreTypeConverters;
PyTypeObject **SbkPySide6_QtGuiTypes;
SbkConverter **SbkPySide6_QtGuiTypeConverters;
PyTypeObject **SbkPySide6_QtWidgetsTypes;
SbkConverter **SbkPySide6_QtWidgetsTypeConverters;

// Module initialization ------------------------------------------------------------
// Container Type converters.

// C++ to Python conversion for container type 'QList<int >'.
static PyObject *_QList_int__CppToPython__QList_int_(const void *cppIn)
{
    const auto &cppInRef = *reinterpret_cast<const ::QList<int > *>(cppIn);
    // TEMPLATE - shiboken_conversion_cppsequence_to_pylist - START
    PyObject *pyOut = PyList_New(Py_ssize_t(cppInRef.size()));
    Py_ssize_t idx = 0;
    for (auto it = cppInRef.cbegin(), end = cppInRef.cend(); it != end; ++it, ++idx) {
        const auto &cppItem = *it;
        PyList_SET_ITEM(pyOut, idx, Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<int>(), &cppItem));
    }
    return pyOut;
    // TEMPLATE - shiboken_conversion_cppsequence_to_pylist - END

}
static void _QList_int__PythonToCpp__QList_int_(PyObject *pyIn, void *cppOut)
{
    auto &cppOutRef = *reinterpret_cast<::QList<int > *>(cppOut);
    // TEMPLATE - shiboken_conversion_pyiterable_to_cppsequentialcontainer_reserve - START
    (cppOutRef).clear();
    if (PyList_Check(pyIn)) {
        const Py_ssize_t size = PySequence_Size(pyIn);
        if (size > 10)
            (cppOutRef).reserve(size);
    }

    Shiboken::AutoDecRef it(PyObject_GetIter(pyIn));
    while (true) {
        Shiboken::AutoDecRef pyItem(PyIter_Next(it.object()));
        if (pyItem.isNull()) {
            if (PyErr_Occurred() && PyErr_ExceptionMatches(PyExc_StopIteration))
                PyErr_Clear();
            break;
        }
        int cppItem;
    Shiboken::Conversions::pythonToCppCopy(Shiboken::Conversions::PrimitiveTypeConverter<int>(), pyItem, &(cppItem));
        (cppOutRef).push_back(cppItem);
    }
    // TEMPLATE - shiboken_conversion_pyiterable_to_cppsequentialcontainer_reserve - END

}
static PythonToCppFunc is__QList_int__PythonToCpp__QList_int__Convertible(PyObject *pyIn)
{
    if (Shiboken::Conversions::convertibleSequenceTypes(Shiboken::Conversions::PrimitiveTypeConverter<int>(), pyIn))
        return _QList_int__PythonToCpp__QList_int_;
    return {};
}


// Binding for QList<int >

template <>
struct ShibokenContainerValueConverter<int>
{
    static bool checkValue(PyObject *pyArg)
    {
        return PyLong_Check(pyArg);
    }

    static PyObject *convertValueToPython(int cppArg)
    {
        return Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<int>(), &cppArg);
    }

    static std::optional<int> convertValueToCpp(PyObject *pyArg)
    {
        Shiboken::Conversions::PythonToCppConversion pythonToCpp;
        if (!(PyLong_Check(pyArg) && (pythonToCpp = Shiboken::Conversions::pythonToCppConversion(Shiboken::Conversions::PrimitiveTypeConverter<int>(), (pyArg))))) {
            Shiboken::Errors::setWrongContainerType();
            return {};
        }
        int cppArg;
        pythonToCpp(pyArg, &cppArg);
        return cppArg;
    }
};

static PyMethodDef QIntList_methods[] = {
    {"push_back", reinterpret_cast<PyCFunction>(ShibokenSequenceContainerPrivate<QList<int >>::push_back), METH_O, "push_back"},
    {"append", reinterpret_cast<PyCFunction>(ShibokenSequenceContainerPrivate<QList<int >>::push_back), METH_O, "append"},
    {"clear", reinterpret_cast<PyCFunction>(ShibokenSequenceContainerPrivate<QList<int >>::clear), METH_NOARGS, "clear"},
    {"pop_back", reinterpret_cast<PyCFunction>(ShibokenSequenceContainerPrivate<QList<int >>::pop_back), METH_NOARGS, "pop_back"},
    {"removeLast", reinterpret_cast<PyCFunction>(ShibokenSequenceContainerPrivate<QList<int >>::pop_back), METH_NOARGS, "removeLast"},
    {"push_front", reinterpret_cast<PyCFunction>(ShibokenSequenceContainerPrivate<QList<int >>::push_front), METH_O, "push_front"},
    {"prepend", reinterpret_cast<PyCFunction>(ShibokenSequenceContainerPrivate<QList<int >>::push_front), METH_O, "prepend"},
    {"pop_front", reinterpret_cast<PyCFunction>(ShibokenSequenceContainerPrivate<QList<int >>::pop_front), METH_NOARGS, "pop_front"},
    {"removeFirst", reinterpret_cast<PyCFunction>(ShibokenSequenceContainerPrivate<QList<int >>::pop_front), METH_O, "removeFirst"},
    {"reserve", reinterpret_cast<PyCFunction>(ShibokenSequenceContainerPrivate<QList<int >>::reserve), METH_O, "reserve"},
    {"capacity", reinterpret_cast<PyCFunction>(ShibokenSequenceContainerPrivate<QList<int >>::capacity), METH_NOARGS, "capacity"},
    {"data", reinterpret_cast<PyCFunction>(ShibokenSequenceContainerPrivate<QList<int >>::data), METH_NOARGS, "data"},
    {"constData", reinterpret_cast<PyCFunction>(ShibokenSequenceContainerPrivate<QList<int >>::constData), METH_NOARGS, "constData"},
    {nullptr, nullptr, 0, nullptr} // Sentinel
};

static PyType_Slot QIntList_slots[] = {
    {Py_tp_init, reinterpret_cast<void *>(ShibokenSequenceContainerPrivate<QList<int >>::tpInit)},
    {Py_tp_new, reinterpret_cast<void *>(ShibokenSequenceContainerPrivate<QList<int >>::tpNew)},
    {Py_tp_free, reinterpret_cast<void *>(ShibokenSequenceContainerPrivate<QList<int >>::tpFree)},
    {Py_tp_dealloc, reinterpret_cast<void *>(Sbk_object_dealloc)},
    {Py_tp_methods, reinterpret_cast<void *>(QIntList_methods)},
    {Py_sq_ass_item, reinterpret_cast<void *>(ShibokenSequenceContainerPrivate<QList<int >>::sqSetItem)},
    {Py_sq_length, reinterpret_cast<void *>(ShibokenSequenceContainerPrivate<QList<int >>::sqLen)},
    {Py_sq_item, reinterpret_cast<void *>(ShibokenSequenceContainerPrivate<QList<int >>::sqGetItem)},
    {0, nullptr}
};

static PyType_Spec QIntList_spec = {
    "1:qrangeslider.QIntList",
    sizeof(ShibokenContainer),
    0,
    Py_TPFLAGS_DEFAULT,
    QIntList_slots
};

static inline PyTypeObject *createQIntListType()
{
    auto *result = reinterpret_cast<PyTypeObject *>(SbkType_FromSpec(&QIntList_spec));
    Py_INCREF(Py_True);
    PyDict_SetItem(result->tp_dict, Shiboken::PyMagicName::opaque_container(), Py_True);
    return result;
}

static PyTypeObject *QIntList_TypeF()
{
    static PyTypeObject *type = createQIntListType();
    return type;
}

extern "C" PyObject *createQIntList(QList<int >* ct)
{
    auto *container = PyObject_New(ShibokenContainer, QIntList_TypeF());
    auto *d = new ShibokenSequenceContainerPrivate<QList<int >>();
    d->m_list = ct;
    container->d = d;
    return reinterpret_cast<PyObject *>(container);
}

extern "C" PyObject *createConstQIntList(const QList<int >* ct)
{
    auto *container = PyObject_New(ShibokenContainer, QIntList_TypeF());
    auto *d = new ShibokenSequenceContainerPrivate<QList<int >>();
    d->m_list = const_cast<QList<int > *>(ct);
    d->m_const = true;
    container->d = d;
    return reinterpret_cast<PyObject *>(container);
}

extern "C" int QIntList_Check(PyObject *pyArg)
{
    return pyArg != nullptr && pyArg != Py_None && pyArg->ob_type == QIntList_TypeF();
}

extern "C" void PythonToCppQIntList(PyObject *pyArg, void *cppOut)
{
    auto *d = ShibokenSequenceContainerPrivate<QList<int >>::get(pyArg);
    *reinterpret_cast<QList<int >**>(cppOut) = d->m_list;
}

extern "C" PythonToCppFunc isQIntListPythonToCppConvertible(PyObject *pyArg)
{
    if (QIntList_Check(pyArg))
        return PythonToCppQIntList;
    return {};
}

// C++ to Python conversion for container type 'QList<QVariant >'.
static PyObject *_QList_QVariant__CppToPython__QList_QVariant_(const void *cppIn)
{
    const auto &cppInRef = *reinterpret_cast<const ::QList<QVariant > *>(cppIn);
    // TEMPLATE - shiboken_conversion_cppsequence_to_pylist - START
    PyObject *pyOut = PyList_New(Py_ssize_t(cppInRef.size()));
    Py_ssize_t idx = 0;
    for (auto it = cppInRef.cbegin(), end = cppInRef.cend(); it != end; ++it, ++idx) {
        const auto &cppItem = *it;
        PyList_SET_ITEM(pyOut, idx, Shiboken::Conversions::copyToPython(SbkPySide6_QtCoreTypeConverters[SBK_QVARIANT_IDX], &cppItem));
    }
    return pyOut;
    // TEMPLATE - shiboken_conversion_cppsequence_to_pylist - END

}
static void _QList_QVariant__PythonToCpp__QList_QVariant_(PyObject *pyIn, void *cppOut)
{
    auto &cppOutRef = *reinterpret_cast<::QList<QVariant > *>(cppOut);
    // TEMPLATE - shiboken_conversion_pyiterable_to_cppsequentialcontainer_reserve - START
    (cppOutRef).clear();
    if (PyList_Check(pyIn)) {
        const Py_ssize_t size = PySequence_Size(pyIn);
        if (size > 10)
            (cppOutRef).reserve(size);
    }

    Shiboken::AutoDecRef it(PyObject_GetIter(pyIn));
    while (true) {
        Shiboken::AutoDecRef pyItem(PyIter_Next(it.object()));
        if (pyItem.isNull()) {
            if (PyErr_Occurred() && PyErr_ExceptionMatches(PyExc_StopIteration))
                PyErr_Clear();
            break;
        }
        ::QVariant cppItem;
    Shiboken::Conversions::pythonToCppCopy(SbkPySide6_QtCoreTypeConverters[SBK_QVARIANT_IDX], pyItem, &(cppItem));
        (cppOutRef).push_back(cppItem);
    }
    // TEMPLATE - shiboken_conversion_pyiterable_to_cppsequentialcontainer_reserve - END

}
static PythonToCppFunc is__QList_QVariant__PythonToCpp__QList_QVariant__Convertible(PyObject *pyIn)
{
    if (Shiboken::Conversions::convertibleSequenceTypes(SbkPySide6_QtCoreTypeConverters[SBK_QVARIANT_IDX], pyIn))
        return _QList_QVariant__PythonToCpp__QList_QVariant_;
    return {};
}

// C++ to Python conversion for container type 'QList<QString >'.
static PyObject *_QList_QString__CppToPython__QList_QString_(const void *cppIn)
{
    const auto &cppInRef = *reinterpret_cast<const ::QList<QString > *>(cppIn);
    // TEMPLATE - shiboken_conversion_cppsequence_to_pylist - START
    PyObject *pyOut = PyList_New(Py_ssize_t(cppInRef.size()));
    Py_ssize_t idx = 0;
    for (auto it = cppInRef.cbegin(), end = cppInRef.cend(); it != end; ++it, ++idx) {
        const auto &cppItem = *it;
        PyList_SET_ITEM(pyOut, idx, Shiboken::Conversions::copyToPython(SbkPySide6_QtCoreTypeConverters[SBK_QSTRING_IDX], &cppItem));
    }
    return pyOut;
    // TEMPLATE - shiboken_conversion_cppsequence_to_pylist - END

}
static void _QList_QString__PythonToCpp__QList_QString_(PyObject *pyIn, void *cppOut)
{
    auto &cppOutRef = *reinterpret_cast<::QList<QString > *>(cppOut);
    // TEMPLATE - shiboken_conversion_pyiterable_to_cppsequentialcontainer_reserve - START
    (cppOutRef).clear();
    if (PyList_Check(pyIn)) {
        const Py_ssize_t size = PySequence_Size(pyIn);
        if (size > 10)
            (cppOutRef).reserve(size);
    }

    Shiboken::AutoDecRef it(PyObject_GetIter(pyIn));
    while (true) {
        Shiboken::AutoDecRef pyItem(PyIter_Next(it.object()));
        if (pyItem.isNull()) {
            if (PyErr_Occurred() && PyErr_ExceptionMatches(PyExc_StopIteration))
                PyErr_Clear();
            break;
        }
        ::QString cppItem;
    Shiboken::Conversions::pythonToCppCopy(SbkPySide6_QtCoreTypeConverters[SBK_QSTRING_IDX], pyItem, &(cppItem));
        (cppOutRef).push_back(cppItem);
    }
    // TEMPLATE - shiboken_conversion_pyiterable_to_cppsequentialcontainer_reserve - END

}
static PythonToCppFunc is__QList_QString__PythonToCpp__QList_QString__Convertible(PyObject *pyIn)
{
    if (Shiboken::Conversions::convertibleSequenceTypes(SbkPySide6_QtCoreTypeConverters[SBK_QSTRING_IDX], pyIn))
        return _QList_QString__PythonToCpp__QList_QString_;
    return {};
}

// C++ to Python conversion for container type 'QMap<QString,QVariant >'.
static PyObject *_QMap_QString_QVariant__CppToPython__QMap_QString_QVariant_(const void *cppIn)
{
    const auto &cppInRef = *reinterpret_cast<const ::QMap<QString,QVariant > *>(cppIn);
    // TEMPLATE - shiboken_conversion_qmap_to_pydict - START
    PyObject *pyOut = PyDict_New();
    for (auto it = cppInRef.cbegin(), end = cppInRef.cend(); it != end; ++it) {
        const auto &key = it.key();
        const auto &value = it.value();
        PyObject *pyKey = Shiboken::Conversions::copyToPython(SbkPySide6_QtCoreTypeConverters[SBK_QSTRING_IDX], &key);
        PyObject *pyValue = Shiboken::Conversions::copyToPython(SbkPySide6_QtCoreTypeConverters[SBK_QVARIANT_IDX], &value);
        PyDict_SetItem(pyOut, pyKey, pyValue);
        Py_DECREF(pyKey);
        Py_DECREF(pyValue);
    }
    return pyOut;
    // TEMPLATE - shiboken_conversion_qmap_to_pydict - END

}
static void _QMap_QString_QVariant__PythonToCpp__QMap_QString_QVariant_(PyObject *pyIn, void *cppOut)
{
    auto &cppOutRef = *reinterpret_cast<::QMap<QString,QVariant > *>(cppOut);
    // TEMPLATE - shiboken_conversion_pydict_to_qmap - START
    PyObject *key;
    PyObject *value;
    cppOutRef.clear();
    Py_ssize_t pos = 0;
    while (PyDict_Next(pyIn, &pos, &key, &value)) {
        ::QString cppKey;
    Shiboken::Conversions::pythonToCppCopy(SbkPySide6_QtCoreTypeConverters[SBK_QSTRING_IDX], key, &(cppKey));
        ::QVariant cppValue;
    Shiboken::Conversions::pythonToCppCopy(SbkPySide6_QtCoreTypeConverters[SBK_QVARIANT_IDX], value, &(cppValue));
        cppOutRef.insert(cppKey, cppValue);
    }
    // TEMPLATE - shiboken_conversion_pydict_to_qmap - END

}
static PythonToCppFunc is__QMap_QString_QVariant__PythonToCpp__QMap_QString_QVariant__Convertible(PyObject *pyIn)
{
    if (Shiboken::Conversions::convertibleDictTypes(SbkPySide6_QtCoreTypeConverters[SBK_QSTRING_IDX], false, SbkPySide6_QtCoreTypeConverters[SBK_QVARIANT_IDX], false, pyIn))
        return _QMap_QString_QVariant__PythonToCpp__QMap_QString_QVariant_;
    return {};
}


static struct PyModuleDef moduledef = {
    /* m_base     */ PyModuleDef_HEAD_INIT,
    /* m_name     */ "qrangeslider",
    /* m_doc      */ nullptr,
    /* m_size     */ -1,
    /* m_methods  */ qrangeslider_methods,
    /* m_reload   */ nullptr,
    /* m_traverse */ nullptr,
    /* m_clear    */ nullptr,
    /* m_free     */ nullptr
};

// The signatures string for the global functions.
// Multiple signatures have their index "n:" in front.
static const char *qrangeslider_SignatureStrings[] = {
    nullptr}; // Sentinel

extern "C" LIBSHIBOKEN_EXPORT PyObject *PyInit_qrangeslider()
{
    if (SbkqrangesliderModuleObject != nullptr)
        return SbkqrangesliderModuleObject;
    {
        Shiboken::AutoDecRef requiredModule(Shiboken::Module::import("PySide6.QtCore"));
        if (requiredModule.isNull())
            return nullptr;
        SbkPySide6_QtCoreTypes = Shiboken::Module::getTypes(requiredModule);
        SbkPySide6_QtCoreTypeConverters = Shiboken::Module::getTypeConverters(requiredModule);
    }

    {
        Shiboken::AutoDecRef requiredModule(Shiboken::Module::import("PySide6.QtGui"));
        if (requiredModule.isNull())
            return nullptr;
        SbkPySide6_QtGuiTypes = Shiboken::Module::getTypes(requiredModule);
        SbkPySide6_QtGuiTypeConverters = Shiboken::Module::getTypeConverters(requiredModule);
    }

    {
        Shiboken::AutoDecRef requiredModule(Shiboken::Module::import("PySide6.QtWidgets"));
        if (requiredModule.isNull())
            return nullptr;
        SbkPySide6_QtWidgetsTypes = Shiboken::Module::getTypes(requiredModule);
        SbkPySide6_QtWidgetsTypeConverters = Shiboken::Module::getTypeConverters(requiredModule);
    }

    // Create an array of wrapper types for the current module.
    static PyTypeObject *cppApi[SBK_qrangeslider_IDX_COUNT];
    SbkqrangesliderTypes = cppApi;

    // Create an array of primitive type converters for the current module.
    static SbkConverter *sbkConverters[SBK_qrangeslider_CONVERTERS_IDX_COUNT];
    SbkqrangesliderTypeConverters = sbkConverters;

    PyObject *module = Shiboken::Module::create("qrangeslider", &moduledef);

    // Make module available from global scope
    SbkqrangesliderModuleObject = module;

    // Initialize classes in the type system
    init_QRangeSlider(module);

    // Register converter for type 'QList<int>'.
    SbkqrangesliderTypeConverters[SBK_QRANGESLIDER_QLIST_INT_IDX] = Shiboken::Conversions::createConverter(&PyList_Type, _QList_int__CppToPython__QList_int_);
    Shiboken::Conversions::registerConverterName(SbkqrangesliderTypeConverters[SBK_QRANGESLIDER_QLIST_INT_IDX], "QList<int>");
    Shiboken::Conversions::addPythonToCppValueConversion(SbkqrangesliderTypeConverters[SBK_QRANGESLIDER_QLIST_INT_IDX],
        _QList_int__PythonToCpp__QList_int_,
        is__QList_int__PythonToCpp__QList_int__Convertible);
    Shiboken::Conversions::setPythonToCppPointerFunctions(SbkqrangesliderTypeConverters[SBK_QRANGESLIDER_QLIST_INT_IDX],
        PythonToCppQIntList,
        isQIntListPythonToCppConvertible);

    // Register converter for type 'QList<QVariant>'.
    SbkqrangesliderTypeConverters[SBK_QRANGESLIDER_QLIST_QVARIANT_IDX] = Shiboken::Conversions::createConverter(&PyList_Type, _QList_QVariant__CppToPython__QList_QVariant_);
    Shiboken::Conversions::registerConverterName(SbkqrangesliderTypeConverters[SBK_QRANGESLIDER_QLIST_QVARIANT_IDX], "QList<QVariant>");
    Shiboken::Conversions::addPythonToCppValueConversion(SbkqrangesliderTypeConverters[SBK_QRANGESLIDER_QLIST_QVARIANT_IDX],
        _QList_QVariant__PythonToCpp__QList_QVariant_,
        is__QList_QVariant__PythonToCpp__QList_QVariant__Convertible);

    // Register converter for type 'QList<QString>'.
    SbkqrangesliderTypeConverters[SBK_QRANGESLIDER_QLIST_QSTRING_IDX] = Shiboken::Conversions::createConverter(&PyList_Type, _QList_QString__CppToPython__QList_QString_);
    Shiboken::Conversions::registerConverterName(SbkqrangesliderTypeConverters[SBK_QRANGESLIDER_QLIST_QSTRING_IDX], "QList<QString>");
    Shiboken::Conversions::addPythonToCppValueConversion(SbkqrangesliderTypeConverters[SBK_QRANGESLIDER_QLIST_QSTRING_IDX],
        _QList_QString__PythonToCpp__QList_QString_,
        is__QList_QString__PythonToCpp__QList_QString__Convertible);

    // Register converter for type 'QMap<QString,QVariant>'.
    SbkqrangesliderTypeConverters[SBK_QRANGESLIDER_QMAP_QSTRING_QVARIANT_IDX] = Shiboken::Conversions::createConverter(&PyDict_Type, _QMap_QString_QVariant__CppToPython__QMap_QString_QVariant_);
    Shiboken::Conversions::registerConverterName(SbkqrangesliderTypeConverters[SBK_QRANGESLIDER_QMAP_QSTRING_QVARIANT_IDX], "QMap<QString,QVariant>");
    Shiboken::Conversions::addPythonToCppValueConversion(SbkqrangesliderTypeConverters[SBK_QRANGESLIDER_QMAP_QSTRING_QVARIANT_IDX],
        _QMap_QString_QVariant__PythonToCpp__QMap_QString_QVariant_,
        is__QMap_QString_QVariant__PythonToCpp__QMap_QString_QVariant__Convertible);


    // Opaque container type registration
    PyObject *ob_type{};
    ob_type = reinterpret_cast<PyObject *>(QIntList_TypeF());
    Py_XINCREF(ob_type);
    PyModule_AddObject(module, "QIntList", ob_type);

    // Register primitive types converters.
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned int>(), "QRgb");
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
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<long>(), "int_fast16_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<long>(), "int_fast32_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<long>(), "int_fast64_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<signed char>(), "int_fast8_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<short>(), "int_least16_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<int>(), "int_least32_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<long>(), "int_least64_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<signed char>(), "int_least8_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<long>(), "intmax_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<int>(), "key_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<long>(), "loff_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned int>(), "mode_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned long>(), "nlink_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<long>(), "off64_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<long>(), "off_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<int>(), "pid_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<long>(), "ptrdiff_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), "qInternalCallback");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<long>(), "quad_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<long>(), "register_t");
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
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned long>(), "uint_fast16_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned long>(), "uint_fast32_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned long>(), "uint_fast64_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned char>(), "uint_fast8_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned short>(), "uint_least16_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned int>(), "uint_least32_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned long>(), "uint_least64_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned char>(), "uint_least8_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned long>(), "uintmax_t");
    Shiboken::Conversions::registerConverterName(Shiboken::Conversions::PrimitiveTypeConverter<unsigned int>(), "useconds_t");

    Shiboken::Module::registerTypes(module, SbkqrangesliderTypes);
    Shiboken::Module::registerTypeConverters(module, SbkqrangesliderTypeConverters);

    if (PyErr_Occurred()) {
        PyErr_Print();
        Py_FatalError("can't initialize module qrangeslider");
    }
    PySide::registerCleanupFunction(cleanTypesAttributes);

    FinishSignatureInitialization(module, qrangeslider_SignatureStrings);

    return module;
}
