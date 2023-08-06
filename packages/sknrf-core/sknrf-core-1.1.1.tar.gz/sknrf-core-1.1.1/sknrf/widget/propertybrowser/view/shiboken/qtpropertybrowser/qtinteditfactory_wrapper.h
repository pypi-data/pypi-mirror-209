#ifndef SBK_QTINTEDITFACTORYWRAPPER_H
#define SBK_QTINTEDITFACTORYWRAPPER_H

#include <qteditorfactory.h>


// Argument includes
#include <qobject.h>
#include <qobjectdefs.h>
#include <qtpropertybrowser.h>
#include <qtpropertybrowserutils_p.h>
#include <qtpropertymanager.h>
#include <qwidget.h>
class QtIntEditFactoryWrapper : public QtIntEditFactory
{
public:
    QtIntEditFactoryWrapper(QObject * parent = 0);
    inline void connectPropertyManager_protected(QtIntPropertyManager * manager) { QtIntEditFactory::connectPropertyManager(manager); }
    void connectPropertyManager(QtIntPropertyManager * manager) override;
    inline QWidget * createAttributeEditor_protected(QtIntPropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) { return QtIntEditFactory::createAttributeEditor(manager, property, parent, BrowserCol(attribute)); }
    QWidget * createAttributeEditor(QtIntPropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) override;
    inline QWidget * createEditor_protected(QtIntPropertyManager * manager, QtProperty * property, QWidget * parent) { return QtIntEditFactory::createEditor(manager, property, parent); }
    QWidget * createEditor(QtIntPropertyManager * manager, QtProperty * property, QWidget * parent) override;
    inline void disconnectPropertyManager_protected(QtIntPropertyManager * manager) { QtIntEditFactory::disconnectPropertyManager(manager); }
    void disconnectPropertyManager(QtIntPropertyManager * manager) override;
    ~QtIntEditFactoryWrapper();
    static void pysideInitQtMetaTypes();
    void resetPyMethodCache();
private:
    mutable bool m_PyMethodCache[4];
};

#endif // SBK_QTINTEDITFACTORYWRAPPER_H

