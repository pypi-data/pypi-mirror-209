#ifndef SBK_QTSCROLLBARFACTORYWRAPPER_H
#define SBK_QTSCROLLBARFACTORYWRAPPER_H

#include <qteditorfactory.h>


// Argument includes
#include <qobject.h>
#include <qobjectdefs.h>
#include <qtpropertybrowser.h>
#include <qtpropertybrowserutils_p.h>
#include <qtpropertymanager.h>
#include <qwidget.h>
class QtScrollBarFactoryWrapper : public QtScrollBarFactory
{
public:
    QtScrollBarFactoryWrapper(QObject * parent = 0);
    inline void connectPropertyManager_protected(QtIntPropertyManager * manager) { QtScrollBarFactory::connectPropertyManager(manager); }
    void connectPropertyManager(QtIntPropertyManager * manager) override;
    inline QWidget * createAttributeEditor_protected(QtIntPropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) { return QtScrollBarFactory::createAttributeEditor(manager, property, parent, BrowserCol(attribute)); }
    QWidget * createAttributeEditor(QtIntPropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) override;
    inline QWidget * createEditor_protected(QtIntPropertyManager * manager, QtProperty * property, QWidget * parent) { return QtScrollBarFactory::createEditor(manager, property, parent); }
    QWidget * createEditor(QtIntPropertyManager * manager, QtProperty * property, QWidget * parent) override;
    inline void disconnectPropertyManager_protected(QtIntPropertyManager * manager) { QtScrollBarFactory::disconnectPropertyManager(manager); }
    void disconnectPropertyManager(QtIntPropertyManager * manager) override;
    ~QtScrollBarFactoryWrapper();
    static void pysideInitQtMetaTypes();
    void resetPyMethodCache();
private:
    mutable bool m_PyMethodCache[4];
};

#endif // SBK_QTSCROLLBARFACTORYWRAPPER_H

