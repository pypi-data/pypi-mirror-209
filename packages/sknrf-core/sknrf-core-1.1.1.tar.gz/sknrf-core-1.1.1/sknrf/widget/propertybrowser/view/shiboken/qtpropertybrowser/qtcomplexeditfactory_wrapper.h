#ifndef SBK_QTCOMPLEXEDITFACTORYWRAPPER_H
#define SBK_QTCOMPLEXEDITFACTORYWRAPPER_H

#include <qteditorfactory.h>


// Argument includes
#include <qobject.h>
#include <qobjectdefs.h>
#include <qtpropertybrowser.h>
#include <qtpropertybrowserutils_p.h>
#include <qtpropertymanager.h>
#include <qwidget.h>
class QtComplexEditFactoryWrapper : public QtComplexEditFactory
{
public:
    QtComplexEditFactoryWrapper(QObject * parent = 0);
    inline void connectPropertyManager_protected(QtComplexPropertyManager * manager) { QtComplexEditFactory::connectPropertyManager(manager); }
    void connectPropertyManager(QtComplexPropertyManager * manager) override;
    inline QWidget * createAttributeEditor_protected(QtComplexPropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) { return QtComplexEditFactory::createAttributeEditor(manager, property, parent, BrowserCol(attribute)); }
    QWidget * createAttributeEditor(QtComplexPropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) override;
    inline QWidget * createEditor_protected(QtComplexPropertyManager * manager, QtProperty * property, QWidget * parent) { return QtComplexEditFactory::createEditor(manager, property, parent); }
    QWidget * createEditor(QtComplexPropertyManager * manager, QtProperty * property, QWidget * parent) override;
    inline void disconnectPropertyManager_protected(QtComplexPropertyManager * manager) { QtComplexEditFactory::disconnectPropertyManager(manager); }
    void disconnectPropertyManager(QtComplexPropertyManager * manager) override;
    ~QtComplexEditFactoryWrapper();
    static void pysideInitQtMetaTypes();
    void resetPyMethodCache();
private:
    mutable bool m_PyMethodCache[4];
};

#endif // SBK_QTCOMPLEXEDITFACTORYWRAPPER_H

