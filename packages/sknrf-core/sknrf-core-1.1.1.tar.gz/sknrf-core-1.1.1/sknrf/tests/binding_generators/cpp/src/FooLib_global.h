#ifndef FOOLIB_GLOBAL_H
#define FOOLIB_GLOBAL_H

#include <QtCore/qglobal.h>

#if defined(FOOLIB_LIBRARY)
#  define FOOLIBSHARED_EXPORT Q_DECL_EXPORT
#else
#  define FOOLIBSHARED_EXPORT Q_DECL_IMPORT
#endif

#endif // FOOLIB_GLOBAL_H
