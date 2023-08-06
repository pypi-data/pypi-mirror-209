

#ifndef SBK_QRANGESLIDER_PYTHON_H
#define SBK_QRANGESLIDER_PYTHON_H

#include <sbkpython.h>
#include <sbkconverter.h>
// Module Includes
#include <pyside6_qtcore_python.h>
#include <pyside6_qtgui_python.h>
#include <pyside6_qtwidgets_python.h>

// Bound library includes
#include <qrangeslider.h>
// Conversion Includes - Primitive Types
#include <QAnyStringView>
#include <qbytearrayview.h>
#include <qchar.h>
#include <QString>
#include <QStringList>
#include <QStringView>
#include <qvariant.h>

// Conversion Includes - Container Types
#include <pysideqflags.h>
#include <QList>
#include <QMap>
#include <pysideqflags.h>
#include <QMultiMap>
#include <QPair>
#include <QQueue>
#include <QSet>
#include <QStack>
#include <list>
#include <map>
#include <utility>
#include <unordered_map>
#include <vector>

// Type indices
enum : int {
    SBK_QRANGESLIDER_HANDLEMOVEMENTMODE_IDX                  = 1,
    SBK_QRANGESLIDER_SPANHANDLE_IDX                          = 2,
    SBK_QRANGESLIDER_IDX                                     = 0,
    SBK_qrangeslider_IDX_COUNT                               = 3
};
// This variable stores all Python types exported by this module.
extern PyTypeObject **SbkqrangesliderTypes;

// This variable stores the Python module object exported by this module.
extern PyObject *SbkqrangesliderModuleObject;

// This variable stores all type converters exported by this module.
extern SbkConverter **SbkqrangesliderTypeConverters;

// Converter indices
enum : int {
    SBK_QRANGESLIDER_QLIST_INT_IDX                           = 0, // QList<int >
    SBK_QRANGESLIDER_QLIST_QVARIANT_IDX                      = 1, // QList<QVariant >
    SBK_QRANGESLIDER_QLIST_QSTRING_IDX                       = 2, // QList<QString >
    SBK_QRANGESLIDER_QMAP_QSTRING_QVARIANT_IDX               = 3, // QMap<QString,QVariant >
    SBK_qrangeslider_CONVERTERS_IDX_COUNT                    = 4
};
// Macros for type check

QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace Shiboken
{

// PyType functions, to get the PyObjectType for a type T
template<> inline PyTypeObject *SbkType< ::QRangeSlider::HandleMovementMode >() { return SbkqrangesliderTypes[SBK_QRANGESLIDER_HANDLEMOVEMENTMODE_IDX]; }
template<> inline PyTypeObject *SbkType< ::QRangeSlider::SpanHandle >() { return SbkqrangesliderTypes[SBK_QRANGESLIDER_SPANHANDLE_IDX]; }
template<> inline PyTypeObject *SbkType< ::QRangeSlider >() { return reinterpret_cast<PyTypeObject *>(SbkqrangesliderTypes[SBK_QRANGESLIDER_IDX]); }

} // namespace Shiboken

QT_WARNING_POP
#endif // SBK_QRANGESLIDER_PYTHON_H

