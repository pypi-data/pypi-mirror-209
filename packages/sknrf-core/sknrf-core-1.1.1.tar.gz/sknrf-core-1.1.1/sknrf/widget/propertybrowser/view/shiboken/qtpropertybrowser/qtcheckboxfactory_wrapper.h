#ifndef SBK_QTCHECKBOXFACTORYWRAPPER_H
#define SBK_QTCHECKBOXFACTORYWRAPPER_H

#include <qteditorfactory.h>


// Argument includes
#include <qobject.h>
#include <qobjectdefs.h>
#include <qtpropertybrowser.h>
#include <qtpropertybrowserutils_p.h>
#include <qtpropertymanager.h>
#include <qwidget.h>
class QtCheckBoxFactoryWrapper : public QtCheckBoxFactory
{
public:
    QtCheckBoxFactoryWrapper(QObject * parent = 0);
    inline void connectPropertyManager_protected(QtBoolPropertyManager * manager) { QtCheckBoxFactory::connectPropertyManager(manager); }
    void connectPropertyManager(QtBoolPropertyManager * manager) override;
    inline QWidget * createAttributeEditor_protected(QtBoolPropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) { return QtCheckBoxFactory::createAttributeEditor(manager, property, parent, BrowserCol(attribute)); }
    QWidget * createAttributeEditor(QtBoolPropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) override;
    inline QWidget * createEditor_protected(QtBoolPropertyManager * manager, QtProperty * property, QWidget * parent) { return QtCheckBoxFactory::createEditor(manager, property, parent); }
    QWidget * createEditor(QtBoolPropertyManager * manager, QtProperty * property, QWidget * parent) override;
    inline void disconnectPropertyManager_protected(QtBoolPropertyManager * manager) { QtCheckBoxFactory::disconnectPropertyManager(manager); }
    void disconnectPropertyManager(QtBoolPropertyManager * manager) override;
    ~QtCheckBoxFactoryWrapper();
    static void pysideInitQtMetaTypes();
    void resetPyMethodCache();
private:
    mutable bool m_PyMethodCache[4];
};

#endif // SBK_QTCHECKBOXFACTORYWRAPPER_H

