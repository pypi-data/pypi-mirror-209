#ifndef SBK_QTSIZEPOLICYEDITORFACTORYWRAPPER_H
#define SBK_QTSIZEPOLICYEDITORFACTORYWRAPPER_H

#include <qteditorfactory.h>


// Argument includes
#include <qobject.h>
#include <qobjectdefs.h>
#include <qtpropertybrowser.h>
#include <qtpropertybrowserutils_p.h>
#include <qtpropertymanager.h>
#include <qwidget.h>
class QtSizePolicyEditorFactoryWrapper : public QtSizePolicyEditorFactory
{
public:
    QtSizePolicyEditorFactoryWrapper(QObject * parent = 0);
    inline void connectPropertyManager_protected(QtSizePolicyPropertyManager * manager) { QtSizePolicyEditorFactory::connectPropertyManager(manager); }
    void connectPropertyManager(QtSizePolicyPropertyManager * manager) override;
    inline QWidget * createAttributeEditor_protected(QtSizePolicyPropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) { return QtSizePolicyEditorFactory::createAttributeEditor(manager, property, parent, BrowserCol(attribute)); }
    QWidget * createAttributeEditor(QtSizePolicyPropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) override;
    inline QWidget * createEditor_protected(QtSizePolicyPropertyManager * manager, QtProperty * property, QWidget * parent) { return QtSizePolicyEditorFactory::createEditor(manager, property, parent); }
    QWidget * createEditor(QtSizePolicyPropertyManager * manager, QtProperty * property, QWidget * parent) override;
    inline void disconnectPropertyManager_protected(QtSizePolicyPropertyManager * manager) { QtSizePolicyEditorFactory::disconnectPropertyManager(manager); }
    void disconnectPropertyManager(QtSizePolicyPropertyManager * manager) override;
    ~QtSizePolicyEditorFactoryWrapper();
    static void pysideInitQtMetaTypes();
    void resetPyMethodCache();
private:
    mutable bool m_PyMethodCache[4];
};

#endif // SBK_QTSIZEPOLICYEDITORFACTORYWRAPPER_H

