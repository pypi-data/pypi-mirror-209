#ifndef SBK_QTPOINTEDITORFACTORYWRAPPER_H
#define SBK_QTPOINTEDITORFACTORYWRAPPER_H

#include <qteditorfactory.h>


// Argument includes
#include <qobject.h>
#include <qobjectdefs.h>
#include <qtpropertybrowser.h>
#include <qtpropertybrowserutils_p.h>
#include <qtpropertymanager.h>
#include <qwidget.h>
class QtPointEditorFactoryWrapper : public QtPointEditorFactory
{
public:
    QtPointEditorFactoryWrapper(QObject * parent = 0);
    inline void connectPropertyManager_protected(QtPointPropertyManager * manager) { QtPointEditorFactory::connectPropertyManager(manager); }
    void connectPropertyManager(QtPointPropertyManager * manager) override;
    inline QWidget * createAttributeEditor_protected(QtPointPropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) { return QtPointEditorFactory::createAttributeEditor(manager, property, parent, BrowserCol(attribute)); }
    QWidget * createAttributeEditor(QtPointPropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) override;
    inline QWidget * createEditor_protected(QtPointPropertyManager * manager, QtProperty * property, QWidget * parent) { return QtPointEditorFactory::createEditor(manager, property, parent); }
    QWidget * createEditor(QtPointPropertyManager * manager, QtProperty * property, QWidget * parent) override;
    inline void disconnectPropertyManager_protected(QtPointPropertyManager * manager) { QtPointEditorFactory::disconnectPropertyManager(manager); }
    void disconnectPropertyManager(QtPointPropertyManager * manager) override;
    ~QtPointEditorFactoryWrapper();
    static void pysideInitQtMetaTypes();
    void resetPyMethodCache();
private:
    mutable bool m_PyMethodCache[4];
};

#endif // SBK_QTPOINTEDITORFACTORYWRAPPER_H

