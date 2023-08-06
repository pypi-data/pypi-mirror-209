

#ifndef SBK_FOOLIB_PYTHON_H
#define SBK_FOOLIB_PYTHON_H

#include <sbkpython.h>
#include <conversions.h>
#include <sbkenum.h>
#include <basewrapper.h>
#include <bindingmanager.h>
#include <memory>

#include <pysidesignal.h>
// Module Includes
#include <pyside_qtcore_python.h>
#include <pyside_qtgui_python.h>

// Binded library includes
#include <fooclass.h>
// Conversion Includes - Primitive Types
#include <QStringList>
#include <qabstractitemmodel.h>
#include <QString>
#include <signalmanager.h>
#include <typeresolver.h>
#include <QTextDocument>
#include <QtConcurrentFilter>

// Conversion Includes - Container Types
#include <QMap>
#include <QStack>
#include <QLinkedList>
#include <QVector>
#include <QSet>
#include <QPair>
#include <pysideconversions.h>
#include <QQueue>
#include <QList>
#include <QMultiMap>

// Type indices
#define SBK_FOOMENU_IDX                                              1
#define SBK_FOOCLASS_IDX                                             0
#define SBK_foolib_IDX_COUNT                                         2

// This variable stores all Python types exported by this module.
extern PyTypeObject** SbkfoolibTypes;

// This variable stores all type converters exported by this module.
extern SbkConverter** SbkfoolibTypeConverters;

// Converter indices
#define SBK_FOOLIB_QLIST_QACTIONPTR_IDX                              0 // QList<QAction * >
#define SBK_FOOLIB_QLIST_QOBJECTPTR_IDX                              1 // const QList<QObject * > &
#define SBK_FOOLIB_QLIST_QBYTEARRAY_IDX                              2 // QList<QByteArray >
#define SBK_FOOLIB_QLIST_QVARIANT_IDX                                3 // QList<QVariant >
#define SBK_FOOLIB_QLIST_QSTRING_IDX                                 4 // QList<QString >
#define SBK_FOOLIB_QMAP_QSTRING_QVARIANT_IDX                         5 // QMap<QString, QVariant >
#define SBK_foolib_CONVERTERS_IDX_COUNT                              6

// Macros for type check

namespace Shiboken
{

// PyType functions, to get the PyObjectType for a type T
template<> inline PyTypeObject* SbkType< ::FooMenu >() { return reinterpret_cast<PyTypeObject*>(SbkfoolibTypes[SBK_FOOMENU_IDX]); }
template<> inline PyTypeObject* SbkType< ::FooClass >() { return reinterpret_cast<PyTypeObject*>(SbkfoolibTypes[SBK_FOOCLASS_IDX]); }

} // namespace Shiboken

#endif // SBK_FOOLIB_PYTHON_H

