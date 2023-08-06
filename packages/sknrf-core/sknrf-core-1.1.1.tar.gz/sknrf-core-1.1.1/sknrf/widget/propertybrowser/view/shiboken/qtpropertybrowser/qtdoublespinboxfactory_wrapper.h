#ifndef SBK_QTDOUBLESPINBOXFACTORYWRAPPER_H
#define SBK_QTDOUBLESPINBOXFACTORYWRAPPER_H

#include <qteditorfactory.h>


// Argument includes
#include <qobject.h>
#include <qobjectdefs.h>
#include <qtpropertybrowser.h>
#include <qtpropertybrowserutils_p.h>
#include <qtpropertymanager.h>
#include <qwidget.h>
class QtDoubleSpinBoxFactoryWrapper : public QtDoubleSpinBoxFactory
{
public:
    QtDoubleSpinBoxFactoryWrapper(QObject * parent = 0);
    inline void connectPropertyManager_protected(QtDoublePropertyManager * manager) { QtDoubleSpinBoxFactory::connectPropertyManager(manager); }
    void connectPropertyManager(QtDoublePropertyManager * manager) override;
    inline QWidget * createAttributeEditor_protected(QtDoublePropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) { return QtDoubleSpinBoxFactory::createAttributeEditor(manager, property, parent, BrowserCol(attribute)); }
    QWidget * createAttributeEditor(QtDoublePropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) override;
    inline QWidget * createEditor_protected(QtDoublePropertyManager * manager, QtProperty * property, QWidget * parent) { return QtDoubleSpinBoxFactory::createEditor(manager, property, parent); }
    QWidget * createEditor(QtDoublePropertyManager * manager, QtProperty * property, QWidget * parent) override;
    inline void disconnectPropertyManager_protected(QtDoublePropertyManager * manager) { QtDoubleSpinBoxFactory::disconnectPropertyManager(manager); }
    void disconnectPropertyManager(QtDoublePropertyManager * manager) override;
    ~QtDoubleSpinBoxFactoryWrapper();
    static void pysideInitQtMetaTypes();
    void resetPyMethodCache();
private:
    mutable bool m_PyMethodCache[4];
};

#endif // SBK_QTDOUBLESPINBOXFACTORYWRAPPER_H

