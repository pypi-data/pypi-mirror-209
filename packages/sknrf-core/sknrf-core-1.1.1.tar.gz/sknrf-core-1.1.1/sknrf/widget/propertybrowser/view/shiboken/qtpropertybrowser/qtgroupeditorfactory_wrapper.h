#ifndef SBK_QTGROUPEDITORFACTORYWRAPPER_H
#define SBK_QTGROUPEDITORFACTORYWRAPPER_H

#include <qteditorfactory.h>


// Argument includes
#include <qobject.h>
#include <qobjectdefs.h>
#include <qtpropertybrowser.h>
#include <qtpropertybrowserutils_p.h>
#include <qtpropertymanager.h>
#include <qwidget.h>
class QtGroupEditorFactoryWrapper : public QtGroupEditorFactory
{
public:
    QtGroupEditorFactoryWrapper(QObject * parent = 0);
    inline void connectPropertyManager_protected(QtGroupPropertyManager * manager) { QtGroupEditorFactory::connectPropertyManager(manager); }
    void connectPropertyManager(QtGroupPropertyManager * manager) override;
    inline QWidget * createAttributeEditor_protected(QtGroupPropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) { return QtGroupEditorFactory::createAttributeEditor(manager, property, parent, BrowserCol(attribute)); }
    QWidget * createAttributeEditor(QtGroupPropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) override;
    inline QWidget * createEditor_protected(QtGroupPropertyManager * manager, QtProperty * property, QWidget * parent) { return QtGroupEditorFactory::createEditor(manager, property, parent); }
    QWidget * createEditor(QtGroupPropertyManager * manager, QtProperty * property, QWidget * parent) override;
    inline void disconnectPropertyManager_protected(QtGroupPropertyManager * manager) { QtGroupEditorFactory::disconnectPropertyManager(manager); }
    void disconnectPropertyManager(QtGroupPropertyManager * manager) override;
    ~QtGroupEditorFactoryWrapper();
    static void pysideInitQtMetaTypes();
    void resetPyMethodCache();
private:
    mutable bool m_PyMethodCache[4];
};

#endif // SBK_QTGROUPEDITORFACTORYWRAPPER_H

