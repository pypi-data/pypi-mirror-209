
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
#include "qtpropertybrowser_python.h"

#include <qbytearray.h>
#include <qaction.h>
#include <QString>
#include <qobject.h>
#include <qvariant.h>
#include <qtpropertybrowser.h>
#include <qicon.h>
#include <complex>


// Current module's type array.
PyTypeObject **SbkqtpropertybrowserTypes = nullptr;
// Current module's PyObject pointer.
PyObject *SbkqtpropertybrowserModuleObject = nullptr;
// Current module's converter array.
SbkConverter **SbkqtpropertybrowserTypeConverters = nullptr;
void cleanTypesAttributes() {
    static PyObject *attrName = Shiboken::PyName::qtStaticMetaObject();
    for (int i = 0, imax = SBK_qtpropertybrowser_IDX_COUNT; i < imax; i++) {
        PyObject *pyType = reinterpret_cast<PyObject *>(SbkqtpropertybrowserTypes[i]);
        if (pyType && PyObject_HasAttr(pyType, attrName))
            PyObject_SetAttr(pyType, attrName, Py_None);
    }
}
// Global functions ------------------------------------------------------------

static PyMethodDef qtpropertybrowser_methods[] = {
    {nullptr, nullptr, 0, nullptr} // Sentinel
};

// Classes initialization functions ------------------------------------------------------------
void init_QtVectorComplexEditFactory(PyObject *module);
void init_QtVariantEditorFactory(PyObject *module);
void init_QtTimeEditFactory(PyObject *module);
void init_QtSpinBoxFactory(PyObject *module);
void init_QtSliderFactory(PyObject *module);
void init_QtSizePolicyEditorFactory(PyObject *module);
void init_QtSizeFEditorFactory(PyObject *module);
void init_QtSizeEditorFactory(PyObject *module);
void init_QtScrollBarFactory(PyObject *module);
void init_QtRectFEditorFactory(PyObject *module);
void init_QtRectEditorFactory(PyObject *module);
void init_QtProperty(PyObject *module);
void init_QtVariantProperty(PyObject *module);
void init_QtPointFEditorFactory(PyObject *module);
void init_QtPointEditorFactory(PyObject *module);
void init_QtLocaleEditorFactory(PyObject *module);
void init_QtLineEditFactory(PyObject *module);
void init_QtKeySequenceEditorFactory(PyObject *module);
void init_QtIntEditFactory(PyObject *module);
void init_QtGroupEditorFactory(PyObject *module);
void init_QtFontEditorFactory(PyObject *module);
void init_QtFlagEditorFactory(PyObject *module);
void init_QtFileEditorFactory(PyObject *module);
void init_QtEnumEditorFactory(PyObject *module);
void init_QtDoubleSpinBoxFactory(PyObject *module);
void init_QtDoubleEditFactory(PyObject *module);
void init_QtDateTimeEditFactory(PyObject *module);
void init_QtDateEditFactory(PyObject *module);
void init_QtCursorEditorFactory(PyObject *module);
void init_QtComplexEditFactory(PyObject *module);
void init_QtColorEditorFactory(PyObject *module);
void init_QtCheckBoxFactory(PyObject *module);
void init_QtCharEditorFactory(PyObject *module);
void init_QtBrowserItem(PyObject *module);
void init_QtAbstractPropertyManager(PyObject *module);
void init_QtVectorComplexPropertyManager(PyObject *module);
void init_QtVariantPropertyManager(PyObject *module);
void init_QtTimePropertyManager(PyObject *module);
void init_QtStringPropertyManager(PyObject *module);
void init_QtSizePropertyManager(PyObject *module);
void init_QtSizePolicyPropertyManager(PyObject *module);
void init_QtSizeFPropertyManager(PyObject *module);
void init_QtRectPropertyManager(PyObject *module);
void init_QtRectFPropertyManager(PyObject *module);
void init_QtPointPropertyManager(PyObject *module);
void init_QtPointFPropertyManager(PyObject *module);
void init_QtLocalePropertyManager(PyObject *module);
void init_QtKeySequencePropertyManager(PyObject *module);
void init_QtIntPropertyManager(PyObject *module);
void init_QtGroupPropertyManager(PyObject *module);
void init_QtFontPropertyManager(PyObject *module);
void init_QtFlagPropertyManager(PyObject *module);
void init_QtFilePropertyManager(PyObject *module);
void init_QtEnumPropertyManager(PyObject *module);
void init_QtDoublePropertyManager(PyObject *module);
void init_QtDateTimePropertyManager(PyObject *module);
void init_QtDatePropertyManager(PyObject *module);
void init_QtCursorPropertyManager(PyObject *module);
void init_QtComplexPropertyManager(PyObject *module);
void init_QtColorPropertyManager(PyObject *module);
void init_QtCharPropertyManager(PyObject *module);
void init_QtBoolPropertyManager(PyObject *module);
void init_QtAbstractEditorFactoryBase(PyObject *module);
void init_QtAbstractPropertyBrowser(PyObject *module);
void init_QtTreePropertyBrowser(PyObject *module);
void init_QtGroupBoxPropertyBrowser(PyObject *module);
void init_QtButtonPropertyBrowser(PyObject *module);

// Enum definitions ------------------------------------------------------------
static void BrowserCol_PythonToCpp_BrowserCol(PyObject *pyIn, void *cppOut)
{
    const auto value = static_cast<::BrowserCol>(Shiboken::Enum::getValue(pyIn));
    *reinterpret_cast<::BrowserCol *>(cppOut) = value;

}
static PythonToCppFunc is_BrowserCol_PythonToCpp_BrowserCol_Convertible(PyObject *pyIn)
{
    if (PyObject_TypeCheck(pyIn, SbkqtpropertybrowserTypes[SBK_BROWSERCOL_IDX]))
        return BrowserCol_PythonToCpp_BrowserCol;
    return {};
}
static PyObject *BrowserCol_CppToPython_BrowserCol(const void *cppIn)
{
    const int castCppIn = int(*reinterpret_cast<const ::BrowserCol *>(cppIn));
    return Shiboken::Enum::newItem(SbkqtpropertybrowserTypes[SBK_BROWSERCOL_IDX], castCppIn);

}

static void QFlags_BrowserCol__PythonToCpp_QFlags_BrowserCol_(PyObject *pyIn, void *cppOut)
{
    *reinterpret_cast<::QFlags<BrowserCol> *>(cppOut) =
        ::QFlags<BrowserCol>(QFlag(int(PySide::QFlags::getValue(reinterpret_cast<PySideQFlagsObject *>(pyIn)))));

}
static PythonToCppFunc is_QFlags_BrowserCol__PythonToCpp_QFlags_BrowserCol__Convertible(PyObject *pyIn)
{
    if (PyObject_TypeCheck(pyIn, SbkqtpropertybrowserTypes[SBK_QFLAGS_BROWSERCOL_IDX]))
        return QFlags_BrowserCol__PythonToCpp_QFlags_BrowserCol_;
    return {};
}
static PyObject *QFlags_BrowserCol__CppToPython_QFlags_BrowserCol_(const void *cppIn)
{
    const int castCppIn = int(*reinterpret_cast<const ::QFlags<BrowserCol> *>(cppIn));
    return reinterpret_cast<PyObject *>(PySide::QFlags::newObject(castCppIn, SbkqtpropertybrowserTypes[SBK_QFLAGS_BROWSERCOL_IDX]));

}

static void BrowserCol_PythonToCpp_QFlags_BrowserCol_(PyObject *pyIn, void *cppOut)
{
    *reinterpret_cast<::QFlags<BrowserCol> *>(cppOut) =
        ::QFlags<BrowserCol>(QFlag(int(Shiboken::Enum::getValue(pyIn))));

}
static PythonToCppFunc is_BrowserCol_PythonToCpp_QFlags_BrowserCol__Convertible(PyObject *pyIn)
{
    if (PyObject_TypeCheck(pyIn, SbkqtpropertybrowserTypes[SBK_BROWSERCOL_IDX]))
        return BrowserCol_PythonToCpp_QFlags_BrowserCol_;
    return {};
}
static void number_PythonToCpp_QFlags_BrowserCol_(PyObject *pyIn, void *cppOut)
{
    Shiboken::AutoDecRef pyLong(PyNumber_Long(pyIn));
    *reinterpret_cast<::QFlags<BrowserCol> *>(cppOut) =
        ::QFlags<BrowserCol>(QFlag(int(PyLong_AsLong(pyLong.object()))));

}
static PythonToCppFunc is_number_PythonToCpp_QFlags_BrowserCol__Convertible(PyObject *pyIn)
{
    if (PyNumber_Check(pyIn) && PyObject_TypeCheck(pyIn, SbkqtpropertybrowserTypes[SBK_BROWSERCOL_IDX]))
        return number_PythonToCpp_QFlags_BrowserCol_;
    return {};
}
static void Domain_PythonToCpp_Domain(PyObject *pyIn, void *cppOut)
{
    const auto value = static_cast<::Domain>(Shiboken::Enum::getValue(pyIn));
    *reinterpret_cast<::Domain *>(cppOut) = value;

}
static PythonToCppFunc is_Domain_PythonToCpp_Domain_Convertible(PyObject *pyIn)
{
    if (PyObject_TypeCheck(pyIn, SbkqtpropertybrowserTypes[SBK_DOMAIN_IDX]))
        return Domain_PythonToCpp_Domain;
    return {};
}
static PyObject *Domain_CppToPython_Domain(const void *cppIn)
{
    const int castCppIn = int(*reinterpret_cast<const ::Domain *>(cppIn));
    return Shiboken::Enum::newItem(SbkqtpropertybrowserTypes[SBK_DOMAIN_IDX], castCppIn);

}

static void Format_PythonToCpp_Format(PyObject *pyIn, void *cppOut)
{
    const auto value = static_cast<::Format>(Shiboken::Enum::getValue(pyIn));
    *reinterpret_cast<::Format *>(cppOut) = value;

}
static PythonToCppFunc is_Format_PythonToCpp_Format_Convertible(PyObject *pyIn)
{
    if (PyObject_TypeCheck(pyIn, SbkqtpropertybrowserTypes[SBK_FORMAT_IDX]))
        return Format_PythonToCpp_Format;
    return {};
}
static PyObject *Format_CppToPython_Format(const void *cppIn)
{
    const int castCppIn = int(*reinterpret_cast<const ::Format *>(cppIn));
    return Shiboken::Enum::newItem(SbkqtpropertybrowserTypes[SBK_FORMAT_IDX], castCppIn);

}

static void PkAvg_PythonToCpp_PkAvg(PyObject *pyIn, void *cppOut)
{
    const auto value = static_cast<::PkAvg>(Shiboken::Enum::getValue(pyIn));
    *reinterpret_cast<::PkAvg *>(cppOut) = value;

}
static PythonToCppFunc is_PkAvg_PythonToCpp_PkAvg_Convertible(PyObject *pyIn)
{
    if (PyObject_TypeCheck(pyIn, SbkqtpropertybrowserTypes[SBK_PKAVG_IDX]))
        return PkAvg_PythonToCpp_PkAvg;
    return {};
}
static PyObject *PkAvg_CppToPython_PkAvg(const void *cppIn)
{
    const int castCppIn = int(*reinterpret_cast<const ::PkAvg *>(cppIn));
    return Shiboken::Enum::newItem(SbkqtpropertybrowserTypes[SBK_PKAVG_IDX], castCppIn);

}

static void Scale_PythonToCpp_Scale(PyObject *pyIn, void *cppOut)
{
    const auto value = static_cast<::Scale>(Shiboken::Enum::getValue(pyIn));
    *reinterpret_cast<::Scale *>(cppOut) = value;

}
static PythonToCppFunc is_Scale_PythonToCpp_Scale_Convertible(PyObject *pyIn)
{
    if (PyObject_TypeCheck(pyIn, SbkqtpropertybrowserTypes[SBK_SCALE_IDX]))
        return Scale_PythonToCpp_Scale;
    return {};
}
static PyObject *Scale_CppToPython_Scale(const void *cppIn)
{
    const int castCppIn = int(*reinterpret_cast<const ::Scale *>(cppIn));
    return Shiboken::Enum::newItem(SbkqtpropertybrowserTypes[SBK_SCALE_IDX], castCppIn);

}

PyObject *Sbkqtpropertybrowser_BrowserCol___and__(PyObject *self, PyObject *pyArg)
{
    ::BrowserCols cppResult, cppSelf, cppArg;
    cppSelf = static_cast<::BrowserCols>(int(PyLong_AsLong(self)));
    if (PyErr_Occurred())
        return nullptr;
    cppArg = static_cast<BrowserCols>(int(PyLong_AsLong(pyArg)));
    if (PyErr_Occurred())
        return nullptr;
    cppResult = cppSelf & cppArg;
    return Shiboken::Conversions::copyToPython(PepType_PFTP(reinterpret_cast<PySideQFlagsType *>(SbkqtpropertybrowserTypes[SBK_QFLAGS_BROWSERCOL_IDX]))->converter, &cppResult);
}

PyObject *Sbkqtpropertybrowser_BrowserCol___or__(PyObject *self, PyObject *pyArg)
{
    ::BrowserCols cppResult, cppSelf, cppArg;
    cppSelf = static_cast<::BrowserCols>(int(PyLong_AsLong(self)));
    if (PyErr_Occurred())
        return nullptr;
    cppArg = static_cast<BrowserCols>(int(PyLong_AsLong(pyArg)));
    if (PyErr_Occurred())
        return nullptr;
    cppResult = cppSelf | cppArg;
    return Shiboken::Conversions::copyToPython(PepType_PFTP(reinterpret_cast<PySideQFlagsType *>(SbkqtpropertybrowserTypes[SBK_QFLAGS_BROWSERCOL_IDX]))->converter, &cppResult);
}

PyObject *Sbkqtpropertybrowser_BrowserCol___xor__(PyObject *self, PyObject *pyArg)
{
    ::BrowserCols cppResult, cppSelf, cppArg;
    cppSelf = static_cast<::BrowserCols>(int(PyLong_AsLong(self)));
    if (PyErr_Occurred())
        return nullptr;
    cppArg = static_cast<BrowserCols>(int(PyLong_AsLong(pyArg)));
    if (PyErr_Occurred())
        return nullptr;
    cppResult = cppSelf ^ cppArg;
    return Shiboken::Conversions::copyToPython(PepType_PFTP(reinterpret_cast<PySideQFlagsType *>(SbkqtpropertybrowserTypes[SBK_QFLAGS_BROWSERCOL_IDX]))->converter, &cppResult);
}

PyObject *Sbkqtpropertybrowser_BrowserCol___invert__(PyObject *self, PyObject *pyArg)
{
    SBK_UNUSED(pyArg)
    ::BrowserCols cppSelf;
    Shiboken::Conversions::pythonToCppCopy(PepType_PFTP(reinterpret_cast<PySideQFlagsType *>(SbkqtpropertybrowserTypes[SBK_QFLAGS_BROWSERCOL_IDX]))->converter, self, &cppSelf);
    ::BrowserCols cppResult = ~cppSelf;
    return Shiboken::Conversions::copyToPython(PepType_PFTP(reinterpret_cast<PySideQFlagsType *>(SbkqtpropertybrowserTypes[SBK_QFLAGS_BROWSERCOL_IDX]))->converter, &cppResult);
}

static PyObject *Sbkqtpropertybrowser_BrowserCol_long(PyObject *self)
{
    int val;
    Shiboken::Conversions::pythonToCppCopy(PepType_PFTP(reinterpret_cast<PySideQFlagsType *>(SbkqtpropertybrowserTypes[SBK_QFLAGS_BROWSERCOL_IDX]))->converter, self, &val);
    return Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<int>(), &val);
}
static int Sbkqtpropertybrowser_BrowserCol__nonzero(PyObject *self)
{
    int val;
    Shiboken::Conversions::pythonToCppCopy(PepType_PFTP(reinterpret_cast<PySideQFlagsType *>(SbkqtpropertybrowserTypes[SBK_QFLAGS_BROWSERCOL_IDX]))->converter, self, &val);
    return val != 0;
}

static PyType_Slot Sbkqtpropertybrowser_BrowserCol_number_slots[] = {
    {Py_nb_bool,    reinterpret_cast<void *>(Sbkqtpropertybrowser_BrowserCol__nonzero)},
    {Py_nb_invert,  reinterpret_cast<void *>(Sbkqtpropertybrowser_BrowserCol___invert__)},
    {Py_nb_and,     reinterpret_cast<void *>(Sbkqtpropertybrowser_BrowserCol___and__)},
    {Py_nb_xor,     reinterpret_cast<void *>(Sbkqtpropertybrowser_BrowserCol___xor__)},
    {Py_nb_or,      reinterpret_cast<void *>(Sbkqtpropertybrowser_BrowserCol___or__)},
    {Py_nb_int,     reinterpret_cast<void *>(Sbkqtpropertybrowser_BrowserCol_long)},
    {Py_nb_index,   reinterpret_cast<void *>(Sbkqtpropertybrowser_BrowserCol_long)},
    {0, nullptr} // sentinel
};



// Required modules' type and converter arrays.
PyTypeObject **SbkPySide6_QtCoreTypes;
SbkConverter **SbkPySide6_QtCoreTypeConverters;
PyTypeObject **SbkPySide6_QtGuiTypes;
SbkConverter **SbkPySide6_QtGuiTypeConverters;
PyTypeObject **SbkPySide6_QtWidgetsTypes;
SbkConverter **SbkPySide6_QtWidgetsTypeConverters;

// Module initialization ------------------------------------------------------------

// Primitive Type converters.

// C++ to Python conversion for primitive type 'QtComplex'.
static PyObject *QtComplex_CppToPython_QtComplex(const void *cppIn)
{
    auto &cppInRef = *reinterpret_cast<::QtComplex *>(const_cast<void *>(cppIn));
    return PyComplex_FromDoubles(cppInRef.real(), cppInRef.imag());

}
// Python to C++ conversions for type 'QtComplex'.
static void PyComplex_PythonToCpp_QtComplex(PyObject *pyIn, void *cppOut)
{
    double real = PyComplex_RealAsDouble(pyIn);
    double imag = PyComplex_ImagAsDouble(pyIn);
    *reinterpret_cast<::QtComplex *>(cppOut) = QtComplex(real, imag);

}
static PythonToCppFunc is_PyComplex_PythonToCpp_QtComplex_Convertible(PyObject *pyIn)
{
    if (PyComplex_Check(pyIn))
        return PyComplex_PythonToCpp_QtComplex;
    return {};
}


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
    "1:qtpropertybrowser.QIntList",
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

// C++ to Python conversion for container type 'QList<QtProperty* >'.
static PyObject *_QList_QtPropertyPTR__CppToPython__QList_QtPropertyPTR_(const void *cppIn)
{
    const auto &cppInRef = *reinterpret_cast<const ::QList<QtProperty* > *>(cppIn);
    // TEMPLATE - shiboken_conversion_cppsequence_to_pylist - START
    PyObject *pyOut = PyList_New(Py_ssize_t(cppInRef.size()));
    Py_ssize_t idx = 0;
    for (auto it = cppInRef.cbegin(), end = cppInRef.cend(); it != end; ++it, ++idx) {
        const auto &cppItem = *it;
        PyList_SET_ITEM(pyOut, idx, Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], cppItem));
    }
    return pyOut;
    // TEMPLATE - shiboken_conversion_cppsequence_to_pylist - END

}
static void _QList_QtPropertyPTR__PythonToCpp__QList_QtPropertyPTR_(PyObject *pyIn, void *cppOut)
{
    auto &cppOutRef = *reinterpret_cast<::QList<QtProperty* > *>(cppOut);
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
        ::QtProperty* cppItem{nullptr};
    Shiboken::Conversions::pythonToCppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], pyItem, &(cppItem));
        (cppOutRef).push_back(cppItem);
    }
    // TEMPLATE - shiboken_conversion_pyiterable_to_cppsequentialcontainer_reserve - END

}
static PythonToCppFunc is__QList_QtPropertyPTR__PythonToCpp__QList_QtPropertyPTR__Convertible(PyObject *pyIn)
{
    if (Shiboken::Conversions::checkSequenceTypes(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], pyIn))
        return _QList_QtPropertyPTR__PythonToCpp__QList_QtPropertyPTR_;
    return {};
}

// C++ to Python conversion for container type 'QList<QtBrowserItem* >'.
static PyObject *_QList_QtBrowserItemPTR__CppToPython__QList_QtBrowserItemPTR_(const void *cppIn)
{
    const auto &cppInRef = *reinterpret_cast<const ::QList<QtBrowserItem* > *>(cppIn);
    // TEMPLATE - shiboken_conversion_cppsequence_to_pylist - START
    PyObject *pyOut = PyList_New(Py_ssize_t(cppInRef.size()));
    Py_ssize_t idx = 0;
    for (auto it = cppInRef.cbegin(), end = cppInRef.cend(); it != end; ++it, ++idx) {
        const auto &cppItem = *it;
        PyList_SET_ITEM(pyOut, idx, Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX], cppItem));
    }
    return pyOut;
    // TEMPLATE - shiboken_conversion_cppsequence_to_pylist - END

}
static void _QList_QtBrowserItemPTR__PythonToCpp__QList_QtBrowserItemPTR_(PyObject *pyIn, void *cppOut)
{
    auto &cppOutRef = *reinterpret_cast<::QList<QtBrowserItem* > *>(cppOut);
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
        ::QtBrowserItem* cppItem{nullptr};
    Shiboken::Conversions::pythonToCppPointer(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX], pyItem, &(cppItem));
        (cppOutRef).push_back(cppItem);
    }
    // TEMPLATE - shiboken_conversion_pyiterable_to_cppsequentialcontainer_reserve - END

}
static PythonToCppFunc is__QList_QtBrowserItemPTR__PythonToCpp__QList_QtBrowserItemPTR__Convertible(PyObject *pyIn)
{
    if (Shiboken::Conversions::checkSequenceTypes(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX], pyIn))
        return _QList_QtBrowserItemPTR__PythonToCpp__QList_QtBrowserItemPTR_;
    return {};
}

// C++ to Python conversion for container type 'QList<QObject* >'.
static PyObject *_QList_QObjectPTR__CppToPython__QList_QObjectPTR_(const void *cppIn)
{
    const auto &cppInRef = *reinterpret_cast<const ::QList<QObject* > *>(cppIn);
    // TEMPLATE - shiboken_conversion_cppsequence_to_pylist - START
    PyObject *pyOut = PyList_New(Py_ssize_t(cppInRef.size()));
    Py_ssize_t idx = 0;
    for (auto it = cppInRef.cbegin(), end = cppInRef.cend(); it != end; ++it, ++idx) {
        const auto &cppItem = *it;
        PyList_SET_ITEM(pyOut, idx, Shiboken::Conversions::pointerToPython(SbkPySide6_QtCoreTypes[SBK_QOBJECT_IDX], cppItem));
    }
    return pyOut;
    // TEMPLATE - shiboken_conversion_cppsequence_to_pylist - END

}
static void _QList_QObjectPTR__PythonToCpp__QList_QObjectPTR_(PyObject *pyIn, void *cppOut)
{
    auto &cppOutRef = *reinterpret_cast<::QList<QObject* > *>(cppOut);
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
        ::QObject* cppItem{nullptr};
    Shiboken::Conversions::pythonToCppPointer(SbkPySide6_QtCoreTypes[SBK_QOBJECT_IDX], pyItem, &(cppItem));
        (cppOutRef).push_back(cppItem);
    }
    // TEMPLATE - shiboken_conversion_pyiterable_to_cppsequentialcontainer_reserve - END

}
static PythonToCppFunc is__QList_QObjectPTR__PythonToCpp__QList_QObjectPTR__Convertible(PyObject *pyIn)
{
    if (Shiboken::Conversions::checkSequenceTypes(SbkPySide6_QtCoreTypes[SBK_QOBJECT_IDX], pyIn))
        return _QList_QObjectPTR__PythonToCpp__QList_QObjectPTR_;
    return {};
}

// C++ to Python conversion for container type 'QList<QByteArray >'.
static PyObject *_QList_QByteArray__CppToPython__QList_QByteArray_(const void *cppIn)
{
    const auto &cppInRef = *reinterpret_cast<const ::QList<QByteArray > *>(cppIn);
    // TEMPLATE - shiboken_conversion_cppsequence_to_pylist - START
    PyObject *pyOut = PyList_New(Py_ssize_t(cppInRef.size()));
    Py_ssize_t idx = 0;
    for (auto it = cppInRef.cbegin(), end = cppInRef.cend(); it != end; ++it, ++idx) {
        const auto &cppItem = *it;
        PyList_SET_ITEM(pyOut, idx, Shiboken::Conversions::copyToPython(SbkPySide6_QtCoreTypes[SBK_QBYTEARRAY_IDX], &cppItem));
    }
    return pyOut;
    // TEMPLATE - shiboken_conversion_cppsequence_to_pylist - END

}
static void _QList_QByteArray__PythonToCpp__QList_QByteArray_(PyObject *pyIn, void *cppOut)
{
    auto &cppOutRef = *reinterpret_cast<::QList<QByteArray > *>(cppOut);
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
        ::QByteArray cppItem;
    Shiboken::Conversions::pythonToCppCopy(SbkPySide6_QtCoreTypes[SBK_QBYTEARRAY_IDX], pyItem, &(cppItem));
        (cppOutRef).push_back(cppItem);
    }
    // TEMPLATE - shiboken_conversion_pyiterable_to_cppsequentialcontainer_reserve - END

}
static PythonToCppFunc is__QList_QByteArray__PythonToCpp__QList_QByteArray__Convertible(PyObject *pyIn)
{
    if (Shiboken::Conversions::convertibleSequenceTypes(SbkPySide6_QtCoreTypes[SBK_QBYTEARRAY_IDX], pyIn))
        return _QList_QByteArray__PythonToCpp__QList_QByteArray_;
    return {};
}

// C++ to Python conversion for container type 'QSet<QtProperty* >'.
static PyObject *_QSet_QtPropertyPTR__CppToPython__QSet_QtPropertyPTR_(const void *cppIn)
{
    const auto &cppInRef = *reinterpret_cast<const ::QSet<QtProperty* > *>(cppIn);
    // TEMPLATE - shiboken_conversion_cppsequence_to_pyset - START
    PyObject *pyOut = PySet_New(nullptr);
    for (const auto &cppItem : cppInRef) {
        PySet_Add(pyOut, Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], cppItem));
    }
    return pyOut;
    // TEMPLATE - shiboken_conversion_cppsequence_to_pyset - END

}
static void _QSet_QtPropertyPTR__PythonToCpp__QSet_QtPropertyPTR_(PyObject *pyIn, void *cppOut)
{
    auto &cppOutRef = *reinterpret_cast<::QSet<QtProperty* > *>(cppOut);
    // TEMPLATE - shiboken_conversion_pyiterable_to_cppsetcontainer - START
    (cppOutRef).clear();
    Shiboken::AutoDecRef it(PyObject_GetIter(pyIn));
    while (true) {
        Shiboken::AutoDecRef pyItem(PyIter_Next(it.object()));
        if (pyItem.isNull()) {
            if (PyErr_Occurred() && PyErr_ExceptionMatches(PyExc_StopIteration))
                PyErr_Clear();
            break;
        }
        ::QtProperty* cppItem{nullptr};
    Shiboken::Conversions::pythonToCppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], pyItem, &(cppItem));
        (cppOutRef).insert(cppItem);
    }
    // TEMPLATE - shiboken_conversion_pyiterable_to_cppsetcontainer - END

}
static PythonToCppFunc is__QSet_QtPropertyPTR__PythonToCpp__QSet_QtPropertyPTR__Convertible(PyObject *pyIn)
{
    if (Shiboken::Conversions::checkIterableTypes(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], pyIn))
        return _QSet_QtPropertyPTR__PythonToCpp__QSet_QtPropertyPTR_;
    return {};
}

// C++ to Python conversion for container type 'QList<QtComplex >'.
static PyObject *_QList_QtComplex__CppToPython__QList_QtComplex_(const void *cppIn)
{
    const auto &cppInRef = *reinterpret_cast<const ::QList<QtComplex > *>(cppIn);
    // TEMPLATE - shiboken_conversion_cppsequence_to_pylist - START
    PyObject *pyOut = PyList_New(Py_ssize_t(cppInRef.size()));
    Py_ssize_t idx = 0;
    for (auto it = cppInRef.cbegin(), end = cppInRef.cend(); it != end; ++it, ++idx) {
        const auto &cppItem = *it;
        PyList_SET_ITEM(pyOut, idx, Shiboken::Conversions::copyToPython(SbkqtpropertybrowserTypeConverters[SBK_QTCOMPLEX_IDX], &cppItem));
    }
    return pyOut;
    // TEMPLATE - shiboken_conversion_cppsequence_to_pylist - END

}
static void _QList_QtComplex__PythonToCpp__QList_QtComplex_(PyObject *pyIn, void *cppOut)
{
    auto &cppOutRef = *reinterpret_cast<::QList<QtComplex > *>(cppOut);
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
        ::QtComplex cppItem;
    Shiboken::Conversions::pythonToCppCopy(SbkqtpropertybrowserTypeConverters[SBK_QTCOMPLEX_IDX], pyItem, &(cppItem));
        (cppOutRef).push_back(cppItem);
    }
    // TEMPLATE - shiboken_conversion_pyiterable_to_cppsequentialcontainer_reserve - END

}
static PythonToCppFunc is__QList_QtComplex__PythonToCpp__QList_QtComplex__Convertible(PyObject *pyIn)
{
    if (Shiboken::Conversions::convertibleSequenceTypes(SbkqtpropertybrowserTypeConverters[SBK_QTCOMPLEX_IDX], pyIn))
        return _QList_QtComplex__PythonToCpp__QList_QtComplex_;
    return {};
}

// C++ to Python conversion for container type 'QMap<int,QIcon >'.
static PyObject *_QMap_int_QIcon__CppToPython__QMap_int_QIcon_(const void *cppIn)
{
    const auto &cppInRef = *reinterpret_cast<const ::QMap<int,QIcon > *>(cppIn);
    // TEMPLATE - shiboken_conversion_qmap_to_pydict - START
    PyObject *pyOut = PyDict_New();
    for (auto it = cppInRef.cbegin(), end = cppInRef.cend(); it != end; ++it) {
        const auto &key = it.key();
        const auto &value = it.value();
        PyObject *pyKey = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<int>(), &key);
        PyObject *pyValue = Shiboken::Conversions::copyToPython(SbkPySide6_QtGuiTypes[SBK_QICON_IDX], &value);
        PyDict_SetItem(pyOut, pyKey, pyValue);
        Py_DECREF(pyKey);
        Py_DECREF(pyValue);
    }
    return pyOut;
    // TEMPLATE - shiboken_conversion_qmap_to_pydict - END

}
static void _QMap_int_QIcon__PythonToCpp__QMap_int_QIcon_(PyObject *pyIn, void *cppOut)
{
    auto &cppOutRef = *reinterpret_cast<::QMap<int,QIcon > *>(cppOut);
    // TEMPLATE - shiboken_conversion_pydict_to_qmap - START
    PyObject *key;
    PyObject *value;
    cppOutRef.clear();
    Py_ssize_t pos = 0;
    while (PyDict_Next(pyIn, &pos, &key, &value)) {
        int cppKey;
    Shiboken::Conversions::pythonToCppCopy(Shiboken::Conversions::PrimitiveTypeConverter<int>(), key, &(cppKey));
        ::QIcon cppValue;
    Shiboken::Conversions::pythonToCppCopy(SbkPySide6_QtGuiTypes[SBK_QICON_IDX], value, &(cppValue));
        cppOutRef.insert(cppKey, cppValue);
    }
    // TEMPLATE - shiboken_conversion_pydict_to_qmap - END

}
static PythonToCppFunc is__QMap_int_QIcon__PythonToCpp__QMap_int_QIcon__Convertible(PyObject *pyIn)
{
    if (Shiboken::Conversions::convertibleDictTypes(Shiboken::Conversions::PrimitiveTypeConverter<int>(), false, PepType_SOTP(reinterpret_cast<PyTypeObject *>(SbkPySide6_QtGuiTypes[SBK_QICON_IDX]))->converter, false, pyIn))
        return _QMap_int_QIcon__PythonToCpp__QMap_int_QIcon_;
    return {};
}

// C++ to Python conversion for container type 'QList<QAction* >'.
static PyObject *_QList_QActionPTR__CppToPython__QList_QActionPTR_(const void *cppIn)
{
    const auto &cppInRef = *reinterpret_cast<const ::QList<QAction* > *>(cppIn);
    // TEMPLATE - shiboken_conversion_cppsequence_to_pylist - START
    PyObject *pyOut = PyList_New(Py_ssize_t(cppInRef.size()));
    Py_ssize_t idx = 0;
    for (auto it = cppInRef.cbegin(), end = cppInRef.cend(); it != end; ++it, ++idx) {
        const auto &cppItem = *it;
        PyList_SET_ITEM(pyOut, idx, Shiboken::Conversions::pointerToPython(SbkPySide6_QtGuiTypes[SBK_QACTION_IDX], cppItem));
    }
    return pyOut;
    // TEMPLATE - shiboken_conversion_cppsequence_to_pylist - END

}
static void _QList_QActionPTR__PythonToCpp__QList_QActionPTR_(PyObject *pyIn, void *cppOut)
{
    auto &cppOutRef = *reinterpret_cast<::QList<QAction* > *>(cppOut);
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
        ::QAction* cppItem{nullptr};
    Shiboken::Conversions::pythonToCppPointer(SbkPySide6_QtGuiTypes[SBK_QACTION_IDX], pyItem, &(cppItem));
        (cppOutRef).push_back(cppItem);
    }
    // TEMPLATE - shiboken_conversion_pyiterable_to_cppsequentialcontainer_reserve - END

}
static PythonToCppFunc is__QList_QActionPTR__PythonToCpp__QList_QActionPTR__Convertible(PyObject *pyIn)
{
    if (Shiboken::Conversions::checkSequenceTypes(SbkPySide6_QtGuiTypes[SBK_QACTION_IDX], pyIn))
        return _QList_QActionPTR__PythonToCpp__QList_QActionPTR_;
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
    /* m_name     */ "qtpropertybrowser",
    /* m_doc      */ nullptr,
    /* m_size     */ -1,
    /* m_methods  */ qtpropertybrowser_methods,
    /* m_reload   */ nullptr,
    /* m_traverse */ nullptr,
    /* m_clear    */ nullptr,
    /* m_free     */ nullptr
};

// The signatures string for the global functions.
// Multiple signatures have their index "n:" in front.
static const char *qtpropertybrowser_SignatureStrings[] = {
    nullptr}; // Sentinel

extern "C" LIBSHIBOKEN_EXPORT PyObject *PyInit_qtpropertybrowser()
{
    if (SbkqtpropertybrowserModuleObject != nullptr)
        return SbkqtpropertybrowserModuleObject;
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
    static PyTypeObject *cppApi[SBK_qtpropertybrowser_IDX_COUNT];
    SbkqtpropertybrowserTypes = cppApi;

    // Create an array of primitive type converters for the current module.
    static SbkConverter *sbkConverters[SBK_qtpropertybrowser_CONVERTERS_IDX_COUNT];
    SbkqtpropertybrowserTypeConverters = sbkConverters;

    PyObject *module = Shiboken::Module::create("qtpropertybrowser", &moduledef);

    // Make module available from global scope
    SbkqtpropertybrowserModuleObject = module;

    // Initialize classes in the type system
    init_QtVectorComplexEditFactory(module);
    init_QtVariantEditorFactory(module);
    init_QtTimeEditFactory(module);
    init_QtSpinBoxFactory(module);
    init_QtSliderFactory(module);
    init_QtSizePolicyEditorFactory(module);
    init_QtSizeFEditorFactory(module);
    init_QtSizeEditorFactory(module);
    init_QtScrollBarFactory(module);
    init_QtRectFEditorFactory(module);
    init_QtRectEditorFactory(module);
    init_QtProperty(module);
    init_QtVariantProperty(module);
    init_QtPointFEditorFactory(module);
    init_QtPointEditorFactory(module);
    init_QtLocaleEditorFactory(module);
    init_QtLineEditFactory(module);
    init_QtKeySequenceEditorFactory(module);
    init_QtIntEditFactory(module);
    init_QtGroupEditorFactory(module);
    init_QtFontEditorFactory(module);
    init_QtFlagEditorFactory(module);
    init_QtFileEditorFactory(module);
    init_QtEnumEditorFactory(module);
    init_QtDoubleSpinBoxFactory(module);
    init_QtDoubleEditFactory(module);
    init_QtDateTimeEditFactory(module);
    init_QtDateEditFactory(module);
    init_QtCursorEditorFactory(module);
    init_QtComplexEditFactory(module);
    init_QtColorEditorFactory(module);
    init_QtCheckBoxFactory(module);
    init_QtCharEditorFactory(module);
    init_QtBrowserItem(module);
    init_QtAbstractPropertyManager(module);
    init_QtVectorComplexPropertyManager(module);
    init_QtVariantPropertyManager(module);
    init_QtTimePropertyManager(module);
    init_QtStringPropertyManager(module);
    init_QtSizePropertyManager(module);
    init_QtSizePolicyPropertyManager(module);
    init_QtSizeFPropertyManager(module);
    init_QtRectPropertyManager(module);
    init_QtRectFPropertyManager(module);
    init_QtPointPropertyManager(module);
    init_QtPointFPropertyManager(module);
    init_QtLocalePropertyManager(module);
    init_QtKeySequencePropertyManager(module);
    init_QtIntPropertyManager(module);
    init_QtGroupPropertyManager(module);
    init_QtFontPropertyManager(module);
    init_QtFlagPropertyManager(module);
    init_QtFilePropertyManager(module);
    init_QtEnumPropertyManager(module);
    init_QtDoublePropertyManager(module);
    init_QtDateTimePropertyManager(module);
    init_QtDatePropertyManager(module);
    init_QtCursorPropertyManager(module);
    init_QtComplexPropertyManager(module);
    init_QtColorPropertyManager(module);
    init_QtCharPropertyManager(module);
    init_QtBoolPropertyManager(module);
    init_QtAbstractEditorFactoryBase(module);
    init_QtAbstractPropertyBrowser(module);
    init_QtTreePropertyBrowser(module);
    init_QtGroupBoxPropertyBrowser(module);
    init_QtButtonPropertyBrowser(module);

    // Register converter for type 'qtpropertybrowser.QtComplex'.
    SbkqtpropertybrowserTypeConverters[SBK_QTCOMPLEX_IDX] = Shiboken::Conversions::createConverter(&PyComplex_Type, QtComplex_CppToPython_QtComplex);
    Shiboken::Conversions::registerConverterName(SbkqtpropertybrowserTypeConverters[SBK_QTCOMPLEX_IDX], "QtComplex");
    // Add user defined implicit conversions to type converter.
    Shiboken::Conversions::addPythonToCppValueConversion(SbkqtpropertybrowserTypeConverters[SBK_QTCOMPLEX_IDX],
        PyComplex_PythonToCpp_QtComplex,
        is_PyComplex_PythonToCpp_QtComplex_Convertible);


    // Register converter for type 'QList<int>'.
    SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_INT_IDX] = Shiboken::Conversions::createConverter(&PyList_Type, _QList_int__CppToPython__QList_int_);
    Shiboken::Conversions::registerConverterName(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_INT_IDX], "QList<int>");
    Shiboken::Conversions::addPythonToCppValueConversion(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_INT_IDX],
        _QList_int__PythonToCpp__QList_int_,
        is__QList_int__PythonToCpp__QList_int__Convertible);
    Shiboken::Conversions::setPythonToCppPointerFunctions(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_INT_IDX],
        PythonToCppQIntList,
        isQIntListPythonToCppConvertible);

    // Register converter for type 'QList<QtProperty*>'.
    SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_QTPROPERTYPTR_IDX] = Shiboken::Conversions::createConverter(&PyList_Type, _QList_QtPropertyPTR__CppToPython__QList_QtPropertyPTR_);
    Shiboken::Conversions::registerConverterName(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_QTPROPERTYPTR_IDX], "QList<QtProperty*>");
    Shiboken::Conversions::addPythonToCppValueConversion(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_QTPROPERTYPTR_IDX],
        _QList_QtPropertyPTR__PythonToCpp__QList_QtPropertyPTR_,
        is__QList_QtPropertyPTR__PythonToCpp__QList_QtPropertyPTR__Convertible);

    // Register converter for type 'QList<QtBrowserItem*>'.
    SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_QTBROWSERITEMPTR_IDX] = Shiboken::Conversions::createConverter(&PyList_Type, _QList_QtBrowserItemPTR__CppToPython__QList_QtBrowserItemPTR_);
    Shiboken::Conversions::registerConverterName(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_QTBROWSERITEMPTR_IDX], "QList<QtBrowserItem*>");
    Shiboken::Conversions::addPythonToCppValueConversion(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_QTBROWSERITEMPTR_IDX],
        _QList_QtBrowserItemPTR__PythonToCpp__QList_QtBrowserItemPTR_,
        is__QList_QtBrowserItemPTR__PythonToCpp__QList_QtBrowserItemPTR__Convertible);

    // Register converter for type 'QList<QObject*>'.
    SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_QOBJECTPTR_IDX] = Shiboken::Conversions::createConverter(&PyList_Type, _QList_QObjectPTR__CppToPython__QList_QObjectPTR_);
    Shiboken::Conversions::registerConverterName(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_QOBJECTPTR_IDX], "QList<QObject*>");
    Shiboken::Conversions::addPythonToCppValueConversion(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_QOBJECTPTR_IDX],
        _QList_QObjectPTR__PythonToCpp__QList_QObjectPTR_,
        is__QList_QObjectPTR__PythonToCpp__QList_QObjectPTR__Convertible);

    // Register converter for type 'QList<QByteArray>'.
    SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_QBYTEARRAY_IDX] = Shiboken::Conversions::createConverter(&PyList_Type, _QList_QByteArray__CppToPython__QList_QByteArray_);
    Shiboken::Conversions::registerConverterName(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_QBYTEARRAY_IDX], "QList<QByteArray>");
    Shiboken::Conversions::addPythonToCppValueConversion(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_QBYTEARRAY_IDX],
        _QList_QByteArray__PythonToCpp__QList_QByteArray_,
        is__QList_QByteArray__PythonToCpp__QList_QByteArray__Convertible);

    // Register converter for type 'QSet<QtProperty*>'.
    SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QSET_QTPROPERTYPTR_IDX] = Shiboken::Conversions::createConverter(&PySet_Type, _QSet_QtPropertyPTR__CppToPython__QSet_QtPropertyPTR_);
    Shiboken::Conversions::registerConverterName(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QSET_QTPROPERTYPTR_IDX], "QSet<QtProperty*>");
    Shiboken::Conversions::addPythonToCppValueConversion(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QSET_QTPROPERTYPTR_IDX],
        _QSet_QtPropertyPTR__PythonToCpp__QSet_QtPropertyPTR_,
        is__QSet_QtPropertyPTR__PythonToCpp__QSet_QtPropertyPTR__Convertible);

    // Register converter for type 'QList<QtComplex>'.
    SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_QTCOMPLEX_IDX] = Shiboken::Conversions::createConverter(&PyList_Type, _QList_QtComplex__CppToPython__QList_QtComplex_);
    Shiboken::Conversions::registerConverterName(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_QTCOMPLEX_IDX], "QList<QtComplex>");
    Shiboken::Conversions::addPythonToCppValueConversion(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_QTCOMPLEX_IDX],
        _QList_QtComplex__PythonToCpp__QList_QtComplex_,
        is__QList_QtComplex__PythonToCpp__QList_QtComplex__Convertible);

    // Register converter for type 'QMap<int,QIcon>'.
    SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QMAP_INT_QICON_IDX] = Shiboken::Conversions::createConverter(&PyDict_Type, _QMap_int_QIcon__CppToPython__QMap_int_QIcon_);
    Shiboken::Conversions::registerConverterName(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QMAP_INT_QICON_IDX], "QMap<int,QIcon>");
    Shiboken::Conversions::addPythonToCppValueConversion(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QMAP_INT_QICON_IDX],
        _QMap_int_QIcon__PythonToCpp__QMap_int_QIcon_,
        is__QMap_int_QIcon__PythonToCpp__QMap_int_QIcon__Convertible);

    // Register converter for type 'QList<QAction*>'.
    SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_QACTIONPTR_IDX] = Shiboken::Conversions::createConverter(&PyList_Type, _QList_QActionPTR__CppToPython__QList_QActionPTR_);
    Shiboken::Conversions::registerConverterName(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_QACTIONPTR_IDX], "QList<QAction*>");
    Shiboken::Conversions::addPythonToCppValueConversion(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_QACTIONPTR_IDX],
        _QList_QActionPTR__PythonToCpp__QList_QActionPTR_,
        is__QList_QActionPTR__PythonToCpp__QList_QActionPTR__Convertible);

    // Register converter for type 'QList<QVariant>'.
    SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_QVARIANT_IDX] = Shiboken::Conversions::createConverter(&PyList_Type, _QList_QVariant__CppToPython__QList_QVariant_);
    Shiboken::Conversions::registerConverterName(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_QVARIANT_IDX], "QList<QVariant>");
    Shiboken::Conversions::addPythonToCppValueConversion(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_QVARIANT_IDX],
        _QList_QVariant__PythonToCpp__QList_QVariant_,
        is__QList_QVariant__PythonToCpp__QList_QVariant__Convertible);

    // Register converter for type 'QList<QString>'.
    SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_QSTRING_IDX] = Shiboken::Conversions::createConverter(&PyList_Type, _QList_QString__CppToPython__QList_QString_);
    Shiboken::Conversions::registerConverterName(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_QSTRING_IDX], "QList<QString>");
    Shiboken::Conversions::addPythonToCppValueConversion(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_QSTRING_IDX],
        _QList_QString__PythonToCpp__QList_QString_,
        is__QList_QString__PythonToCpp__QList_QString__Convertible);

    // Register converter for type 'QMap<QString,QVariant>'.
    SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QMAP_QSTRING_QVARIANT_IDX] = Shiboken::Conversions::createConverter(&PyDict_Type, _QMap_QString_QVariant__CppToPython__QMap_QString_QVariant_);
    Shiboken::Conversions::registerConverterName(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QMAP_QSTRING_QVARIANT_IDX], "QMap<QString,QVariant>");
    Shiboken::Conversions::addPythonToCppValueConversion(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QMAP_QSTRING_QVARIANT_IDX],
        _QMap_QString_QVariant__PythonToCpp__QMap_QString_QVariant_,
        is__QMap_QString_QVariant__PythonToCpp__QMap_QString_QVariant__Convertible);


    // Opaque container type registration
    PyObject *ob_type{};
    ob_type = reinterpret_cast<PyObject *>(QIntList_TypeF());
    Py_XINCREF(ob_type);
    PyModule_AddObject(module, "QIntList", ob_type);

    // Initialization of enums.
    PyTypeObject *EType{};

    // Initialization of enums, flags part.
    PyTypeObject *FType{};

    // Initialization of enum 'BrowserCol'.
    FType = PySide::QFlags::create("1:qtpropertybrowser.BrowserCols", 
        Sbkqtpropertybrowser_BrowserCol_number_slots);
    SbkqtpropertybrowserTypes[SBK_QFLAGS_BROWSERCOL_IDX] = FType;
    EType = Shiboken::Enum::createGlobalEnum(module,
        "BrowserCol",
        "1:qtpropertybrowser.BrowserCol",
        "BrowserCol",
        FType);
    if (!EType)
        return {};

    if (!Shiboken::Enum::createGlobalEnumItem(EType,
        module, "NONE", Shiboken::Enum::EnumValueType(BrowserCol::NONE)))
        return {};
    if (!Shiboken::Enum::createGlobalEnumItem(EType,
        module, "MINIMUM", Shiboken::Enum::EnumValueType(BrowserCol::MINIMUM)))
        return {};
    if (!Shiboken::Enum::createGlobalEnumItem(EType,
        module, "MAXIMUM", Shiboken::Enum::EnumValueType(BrowserCol::MAXIMUM)))
        return {};
    if (!Shiboken::Enum::createGlobalEnumItem(EType,
        module, "UNIT", Shiboken::Enum::EnumValueType(BrowserCol::UNIT)))
        return {};
    if (!Shiboken::Enum::createGlobalEnumItem(EType,
        module, "PKAVG", Shiboken::Enum::EnumValueType(BrowserCol::PKAVG)))
        return {};
    if (!Shiboken::Enum::createGlobalEnumItem(EType,
        module, "FORMAT", Shiboken::Enum::EnumValueType(BrowserCol::FORMAT)))
        return {};
    if (!Shiboken::Enum::createGlobalEnumItem(EType,
        module, "CHECK", Shiboken::Enum::EnumValueType(BrowserCol::CHECK)))
        return {};
    // PYSIDE-1735: Resolving the whole enum class at the end for API compatibility.
    EType = morphLastEnumToPython();
    SbkqtpropertybrowserTypes[SBK_BROWSERCOL_IDX] = EType;
    // PYSIDE-1735: Mapping the flags class to the same enum class.
    SbkqtpropertybrowserTypes[SBK_QFLAGS_BROWSERCOL_IDX] =
        mapFlagsToSameEnum(FType, EType);
    // Register converter for enum 'BrowserCol'.
    {
        SbkConverter *converter = Shiboken::Conversions::createConverter(EType,
            BrowserCol_CppToPython_BrowserCol);
        Shiboken::Conversions::addPythonToCppValueConversion(converter,
            BrowserCol_PythonToCpp_BrowserCol,
            is_BrowserCol_PythonToCpp_BrowserCol_Convertible);
        Shiboken::Enum::setTypeConverter(EType, converter, false);
        Shiboken::Conversions::registerConverterName(converter, "BrowserCol");
    }
    // Register converter for flag 'QFlags<BrowserCol>'.
    {
        SbkConverter *converter = Shiboken::Conversions::createConverter(FType,
            QFlags_BrowserCol__CppToPython_QFlags_BrowserCol_);
        Shiboken::Conversions::addPythonToCppValueConversion(converter,
            BrowserCol_PythonToCpp_QFlags_BrowserCol_,
            is_BrowserCol_PythonToCpp_QFlags_BrowserCol__Convertible);
        Shiboken::Conversions::addPythonToCppValueConversion(converter,
            QFlags_BrowserCol__PythonToCpp_QFlags_BrowserCol_,
            is_QFlags_BrowserCol__PythonToCpp_QFlags_BrowserCol__Convertible);
        Shiboken::Conversions::addPythonToCppValueConversion(converter,
            number_PythonToCpp_QFlags_BrowserCol_,
            is_number_PythonToCpp_QFlags_BrowserCol__Convertible);
        Shiboken::Enum::setTypeConverter(FType, converter, true);
        Shiboken::Conversions::registerConverterName(converter, "BrowserCols");
        Shiboken::Conversions::registerConverterName(converter, "QFlags<BrowserCol>");
    }
    // End of 'BrowserCol' enum/flags.

    // Initialization of enum 'Domain'.
    EType = Shiboken::Enum::createGlobalEnum(module,
        "Domain",
        "1:qtpropertybrowser.Domain",
        "Domain");
    if (!EType)
        return {};

    if (!Shiboken::Enum::createGlobalEnumItem(EType,
        module, "TF", Shiboken::Enum::EnumValueType(Domain::TF)))
        return {};
    if (!Shiboken::Enum::createGlobalEnumItem(EType,
        module, "FF", Shiboken::Enum::EnumValueType(Domain::FF)))
        return {};
    if (!Shiboken::Enum::createGlobalEnumItem(EType,
        module, "FT", Shiboken::Enum::EnumValueType(Domain::FT)))
        return {};
    if (!Shiboken::Enum::createGlobalEnumItem(EType,
        module, "TT", Shiboken::Enum::EnumValueType(Domain::TT)))
        return {};
    if (!Shiboken::Enum::createGlobalEnumItem(EType,
        module, "TH", Shiboken::Enum::EnumValueType(Domain::TH)))
        return {};
    // PYSIDE-1735: Resolving the whole enum class at the end for API compatibility.
    EType = morphLastEnumToPython();
    SbkqtpropertybrowserTypes[SBK_DOMAIN_IDX] = EType;
    // Register converter for enum 'Domain'.
    {
        SbkConverter *converter = Shiboken::Conversions::createConverter(EType,
            Domain_CppToPython_Domain);
        Shiboken::Conversions::addPythonToCppValueConversion(converter,
            Domain_PythonToCpp_Domain,
            is_Domain_PythonToCpp_Domain_Convertible);
        Shiboken::Enum::setTypeConverter(EType, converter, false);
        Shiboken::Conversions::registerConverterName(converter, "Domain");
    }
    // End of 'Domain' enum.

    // Initialization of enum 'Format'.
    EType = Shiboken::Enum::createGlobalEnum(module,
        "Format",
        "1:qtpropertybrowser.Format",
        "Format");
    if (!EType)
        return {};

    if (!Shiboken::Enum::createGlobalEnumItem(EType,
        module, "RE", Shiboken::Enum::EnumValueType(Format::RE)))
        return {};
    if (!Shiboken::Enum::createGlobalEnumItem(EType,
        module, "RE_IM", Shiboken::Enum::EnumValueType(Format::RE_IM)))
        return {};
    if (!Shiboken::Enum::createGlobalEnumItem(EType,
        module, "LIN_DEG", Shiboken::Enum::EnumValueType(Format::LIN_DEG)))
        return {};
    if (!Shiboken::Enum::createGlobalEnumItem(EType,
        module, "LOG_DEG", Shiboken::Enum::EnumValueType(Format::LOG_DEG)))
        return {};
    // PYSIDE-1735: Resolving the whole enum class at the end for API compatibility.
    EType = morphLastEnumToPython();
    SbkqtpropertybrowserTypes[SBK_FORMAT_IDX] = EType;
    // Register converter for enum 'Format'.
    {
        SbkConverter *converter = Shiboken::Conversions::createConverter(EType,
            Format_CppToPython_Format);
        Shiboken::Conversions::addPythonToCppValueConversion(converter,
            Format_PythonToCpp_Format,
            is_Format_PythonToCpp_Format_Convertible);
        Shiboken::Enum::setTypeConverter(EType, converter, false);
        Shiboken::Conversions::registerConverterName(converter, "Format");
    }
    // End of 'Format' enum.

    // Initialization of enum 'PkAvg'.
    EType = Shiboken::Enum::createGlobalEnum(module,
        "PkAvg",
        "1:qtpropertybrowser.PkAvg",
        "PkAvg");
    if (!EType)
        return {};

    if (!Shiboken::Enum::createGlobalEnumItem(EType,
        module, "PK", Shiboken::Enum::EnumValueType(PkAvg::PK)))
        return {};
    if (!Shiboken::Enum::createGlobalEnumItem(EType,
        module, "AVG", Shiboken::Enum::EnumValueType(PkAvg::AVG)))
        return {};
    // PYSIDE-1735: Resolving the whole enum class at the end for API compatibility.
    EType = morphLastEnumToPython();
    SbkqtpropertybrowserTypes[SBK_PKAVG_IDX] = EType;
    // Register converter for enum 'PkAvg'.
    {
        SbkConverter *converter = Shiboken::Conversions::createConverter(EType,
            PkAvg_CppToPython_PkAvg);
        Shiboken::Conversions::addPythonToCppValueConversion(converter,
            PkAvg_PythonToCpp_PkAvg,
            is_PkAvg_PythonToCpp_PkAvg_Convertible);
        Shiboken::Enum::setTypeConverter(EType, converter, false);
        Shiboken::Conversions::registerConverterName(converter, "PkAvg");
    }
    // End of 'PkAvg' enum.

    // Initialization of enum 'Scale'.
    EType = Shiboken::Enum::createGlobalEnum(module,
        "Scale",
        "1:qtpropertybrowser.Scale",
        "Scale");
    if (!EType)
        return {};

    if (!Shiboken::Enum::createGlobalEnumItem(EType,
        module, "T", Shiboken::Enum::EnumValueType(Scale::T)))
        return {};
    if (!Shiboken::Enum::createGlobalEnumItem(EType,
        module, "G", Shiboken::Enum::EnumValueType(Scale::G)))
        return {};
    if (!Shiboken::Enum::createGlobalEnumItem(EType,
        module, "M", Shiboken::Enum::EnumValueType(Scale::M)))
        return {};
    if (!Shiboken::Enum::createGlobalEnumItem(EType,
        module, "K", Shiboken::Enum::EnumValueType(Scale::K)))
        return {};
    if (!Shiboken::Enum::createGlobalEnumItem(EType,
        module, "_", Shiboken::Enum::EnumValueType(Scale::_)))
        return {};
    if (!Shiboken::Enum::createGlobalEnumItem(EType,
        module, "m", Shiboken::Enum::EnumValueType(Scale::m)))
        return {};
    if (!Shiboken::Enum::createGlobalEnumItem(EType,
        module, "u", Shiboken::Enum::EnumValueType(Scale::u)))
        return {};
    if (!Shiboken::Enum::createGlobalEnumItem(EType,
        module, "n", Shiboken::Enum::EnumValueType(Scale::n)))
        return {};
    if (!Shiboken::Enum::createGlobalEnumItem(EType,
        module, "p", Shiboken::Enum::EnumValueType(Scale::p)))
        return {};
    // PYSIDE-1735: Resolving the whole enum class at the end for API compatibility.
    EType = morphLastEnumToPython();
    SbkqtpropertybrowserTypes[SBK_SCALE_IDX] = EType;
    // Register converter for enum 'Scale'.
    {
        SbkConverter *converter = Shiboken::Conversions::createConverter(EType,
            Scale_CppToPython_Scale);
        Shiboken::Conversions::addPythonToCppValueConversion(converter,
            Scale_PythonToCpp_Scale,
            is_Scale_PythonToCpp_Scale_Convertible);
        Shiboken::Enum::setTypeConverter(EType, converter, false);
        Shiboken::Conversions::registerConverterName(converter, "Scale");
    }
    // End of 'Scale' enum.

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

    Shiboken::Module::registerTypes(module, SbkqtpropertybrowserTypes);
    Shiboken::Module::registerTypeConverters(module, SbkqtpropertybrowserTypeConverters);

    if (PyErr_Occurred()) {
        PyErr_Print();
        Py_FatalError("can't initialize module qtpropertybrowser");
    }
    qRegisterMetaType< ::BrowserCol >("BrowserCol");
    qRegisterMetaType< ::Domain >("Domain");
    qRegisterMetaType< ::Format >("Format");
    qRegisterMetaType< ::PkAvg >("PkAvg");
    qRegisterMetaType< ::Scale >("Scale");
    PySide::registerCleanupFunction(cleanTypesAttributes);

    FinishSignatureInitialization(module, qtpropertybrowser_SignatureStrings);

    return module;
}
