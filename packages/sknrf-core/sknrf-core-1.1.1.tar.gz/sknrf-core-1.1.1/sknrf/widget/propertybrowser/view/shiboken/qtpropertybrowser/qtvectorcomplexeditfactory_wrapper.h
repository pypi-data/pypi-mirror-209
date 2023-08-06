#ifndef SBK_QTVECTORCOMPLEXEDITFACTORYWRAPPER_H
#define SBK_QTVECTORCOMPLEXEDITFACTORYWRAPPER_H

#include <qteditorfactory.h>


// Argument includes
#include <qobject.h>
#include <qobjectdefs.h>
#include <qteditorfactory.h>
#include <qtpropertybrowser.h>
#include <qtpropertybrowserutils_p.h>
#include <qtpropertymanager.h>
#include <qwidget.h>
class QtVectorComplexEditFactoryWrapper : public QtVectorComplexEditFactory
{
public:
    QtVectorComplexEditFactoryWrapper(QObject * parent = 0);
    inline void connectPropertyManager_protected(QtVectorComplexPropertyManager * manager) { QtVectorComplexEditFactory::connectPropertyManager(manager); }
    void connectPropertyManager(QtVectorComplexPropertyManager * manager) override;
    inline QWidget * createAttributeEditor_protected(QtVectorComplexPropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) { return QtVectorComplexEditFactory::createAttributeEditor(manager, property, parent, BrowserCol(attribute)); }
    QWidget * createAttributeEditor(QtVectorComplexPropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) override;
    inline QWidget * createEditor_protected(QtVectorComplexPropertyManager * manager, QtProperty * property, QWidget * parent) { return QtVectorComplexEditFactory::createEditor(manager, property, parent); }
    QWidget * createEditor(QtVectorComplexPropertyManager * manager, QtProperty * property, QWidget * parent) override;
    inline void disconnectPropertyManager_protected(QtVectorComplexPropertyManager * manager) { QtVectorComplexEditFactory::disconnectPropertyManager(manager); }
    void disconnectPropertyManager(QtVectorComplexPropertyManager * manager) override;
    inline QtComplexEditFactory * subFactory_protected() const { return QtVectorComplexEditFactory::subFactory(); }
    ~QtVectorComplexEditFactoryWrapper();
    static void pysideInitQtMetaTypes();
    void resetPyMethodCache();
private:
    mutable bool m_PyMethodCache[4];
};

#endif // SBK_QTVECTORCOMPLEXEDITFACTORYWRAPPER_H

