#ifndef SBK_QTLINEEDITFACTORYWRAPPER_H
#define SBK_QTLINEEDITFACTORYWRAPPER_H

#include <qteditorfactory.h>


// Argument includes
#include <qobject.h>
#include <qobjectdefs.h>
#include <qtpropertybrowser.h>
#include <qtpropertybrowserutils_p.h>
#include <qtpropertymanager.h>
#include <qwidget.h>
class QtLineEditFactoryWrapper : public QtLineEditFactory
{
public:
    QtLineEditFactoryWrapper(QObject * parent = 0);
    inline void connectPropertyManager_protected(QtStringPropertyManager * manager) { QtLineEditFactory::connectPropertyManager(manager); }
    void connectPropertyManager(QtStringPropertyManager * manager) override;
    inline QWidget * createAttributeEditor_protected(QtStringPropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) { return QtLineEditFactory::createAttributeEditor(manager, property, parent, BrowserCol(attribute)); }
    QWidget * createAttributeEditor(QtStringPropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) override;
    inline QWidget * createEditor_protected(QtStringPropertyManager * manager, QtProperty * property, QWidget * parent) { return QtLineEditFactory::createEditor(manager, property, parent); }
    QWidget * createEditor(QtStringPropertyManager * manager, QtProperty * property, QWidget * parent) override;
    inline void disconnectPropertyManager_protected(QtStringPropertyManager * manager) { QtLineEditFactory::disconnectPropertyManager(manager); }
    void disconnectPropertyManager(QtStringPropertyManager * manager) override;
    ~QtLineEditFactoryWrapper();
    static void pysideInitQtMetaTypes();
    void resetPyMethodCache();
private:
    mutable bool m_PyMethodCache[4];
};

#endif // SBK_QTLINEEDITFACTORYWRAPPER_H

