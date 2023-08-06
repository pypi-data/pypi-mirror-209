#ifndef SBK_QTVARIANTPROPERTYWRAPPER_H
#define SBK_QTVARIANTPROPERTYWRAPPER_H

#include <qtvariantproperty.h>


// Argument includes
#include <QList>
#include <QString>
#include <qbrush.h>
#include <qicon.h>
#include <qtpropertybrowser.h>
#include <qtvariantproperty.h>
#include <qvariant.h>
class QtVariantPropertyWrapper : public QtVariantProperty
{
public:
    QtVariantPropertyWrapper(QtVariantPropertyManager * manager);
    inline void propertyChanged_protected() { QtProperty::propertyChanged(); }
    ~QtVariantPropertyWrapper();
    static void pysideInitQtMetaTypes();
    void resetPyMethodCache();
private:
    mutable bool m_PyMethodCache[1];
};

#  ifndef SBK_QTPROPERTYWRAPPER_H
#  define SBK_QTPROPERTYWRAPPER_H

// Inherited base class:
class QtPropertyWrapper : public QtProperty
{
public:
    QtPropertyWrapper(QtAbstractPropertyManager * manager);
    inline void propertyChanged_protected() { QtProperty::propertyChanged(); }
    ~QtPropertyWrapper();
    static void pysideInitQtMetaTypes();
    void resetPyMethodCache();
private:
    mutable bool m_PyMethodCache[1];
};

#  endif // SBK_QTPROPERTYWRAPPER_H

#endif // SBK_QTVARIANTPROPERTYWRAPPER_H

