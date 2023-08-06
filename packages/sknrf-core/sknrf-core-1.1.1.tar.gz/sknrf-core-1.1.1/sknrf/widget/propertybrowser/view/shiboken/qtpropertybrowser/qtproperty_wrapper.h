#ifndef SBK_QTPROPERTYWRAPPER_H
#define SBK_QTPROPERTYWRAPPER_H

#include <qtpropertybrowser.h>


// Argument includes
#include <QList>
#include <QString>
#include <qbrush.h>
#include <qicon.h>
#include <qtpropertybrowser.h>
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

#endif // SBK_QTPROPERTYWRAPPER_H

