

#ifndef SBK_QPROGRESSINDICATOR_PYTHON_H
#define SBK_QPROGRESSINDICATOR_PYTHON_H

#include <sbkpython.h>
#include <sbkconverter.h>
// Module Includes
#include <pyside6_qtcore_python.h>
#include <pyside6_qtgui_python.h>
#include <pyside6_qtwidgets_python.h>

// Bound library includes
#include <qprogressindicator.h>
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
    SBK_QPROGRESSINDICATOR_IDX                               = 0,
    SBK_qprogressindicator_IDX_COUNT                         = 1
};
// This variable stores all Python types exported by this module.
extern PyTypeObject **SbkqprogressindicatorTypes;

// This variable stores the Python module object exported by this module.
extern PyObject *SbkqprogressindicatorModuleObject;

// This variable stores all type converters exported by this module.
extern SbkConverter **SbkqprogressindicatorTypeConverters;

// Converter indices
enum : int {
    SBK_QPROGRESSINDICATOR_QLIST_INT_IDX                     = 0, // QList<int >
    SBK_QPROGRESSINDICATOR_QLIST_QACTIONPTR_IDX              = 1, // QList<QAction* >
    SBK_QPROGRESSINDICATOR_QLIST_QVARIANT_IDX                = 2, // QList<QVariant >
    SBK_QPROGRESSINDICATOR_QLIST_QSTRING_IDX                 = 3, // QList<QString >
    SBK_QPROGRESSINDICATOR_QMAP_QSTRING_QVARIANT_IDX         = 4, // QMap<QString,QVariant >
    SBK_qprogressindicator_CONVERTERS_IDX_COUNT              = 5
};
// Macros for type check

QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace Shiboken
{

// PyType functions, to get the PyObjectType for a type T
template<> inline PyTypeObject *SbkType< ::QProgressIndicator >() { return reinterpret_cast<PyTypeObject *>(SbkqprogressindicatorTypes[SBK_QPROGRESSINDICATOR_IDX]); }

} // namespace Shiboken

QT_WARNING_POP
#endif // SBK_QPROGRESSINDICATOR_PYTHON_H

