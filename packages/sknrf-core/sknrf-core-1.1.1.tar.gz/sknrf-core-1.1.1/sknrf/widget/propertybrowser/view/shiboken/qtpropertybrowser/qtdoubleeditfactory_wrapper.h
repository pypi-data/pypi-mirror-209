#ifndef SBK_QTDOUBLEEDITFACTORYWRAPPER_H
#define SBK_QTDOUBLEEDITFACTORYWRAPPER_H

#include <qteditorfactory.h>


// Argument includes
#include <qobject.h>
#include <qobjectdefs.h>
#include <qtpropertybrowser.h>
#include <qtpropertybrowserutils_p.h>
#include <qtpropertymanager.h>
#include <qwidget.h>
class QtDoubleEditFactoryWrapper : public QtDoubleEditFactory
{
public:
    QtDoubleEditFactoryWrapper(QObject * parent = 0);
    inline void connectPropertyManager_protected(QtDoublePropertyManager * manager) { QtDoubleEditFactory::connectPropertyManager(manager); }
    void connectPropertyManager(QtDoublePropertyManager * manager) override;
    inline QWidget * createAttributeEditor_protected(QtDoublePropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) { return QtDoubleEditFactory::createAttributeEditor(manager, property, parent, BrowserCol(attribute)); }
    QWidget * createAttributeEditor(QtDoublePropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) override;
    inline QWidget * createEditor_protected(QtDoublePropertyManager * manager, QtProperty * property, QWidget * parent) { return QtDoubleEditFactory::createEditor(manager, property, parent); }
    QWidget * createEditor(QtDoublePropertyManager * manager, QtProperty * property, QWidget * parent) override;
    inline void disconnectPropertyManager_protected(QtDoublePropertyManager * manager) { QtDoubleEditFactory::disconnectPropertyManager(manager); }
    void disconnectPropertyManager(QtDoublePropertyManager * manager) override;
    ~QtDoubleEditFactoryWrapper();
    static void pysideInitQtMetaTypes();
    void resetPyMethodCache();
private:
    mutable bool m_PyMethodCache[4];
};

#endif // SBK_QTDOUBLEEDITFACTORYWRAPPER_H

