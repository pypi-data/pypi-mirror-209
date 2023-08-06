#ifndef SBK_QTFLAGEDITORFACTORYWRAPPER_H
#define SBK_QTFLAGEDITORFACTORYWRAPPER_H

#include <qteditorfactory.h>


// Argument includes
#include <qobject.h>
#include <qobjectdefs.h>
#include <qtpropertybrowser.h>
#include <qtpropertybrowserutils_p.h>
#include <qtpropertymanager.h>
#include <qwidget.h>
class QtFlagEditorFactoryWrapper : public QtFlagEditorFactory
{
public:
    QtFlagEditorFactoryWrapper(QObject * parent = 0);
    inline void connectPropertyManager_protected(QtFlagPropertyManager * manager) { QtFlagEditorFactory::connectPropertyManager(manager); }
    void connectPropertyManager(QtFlagPropertyManager * manager) override;
    inline QWidget * createAttributeEditor_protected(QtFlagPropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) { return QtFlagEditorFactory::createAttributeEditor(manager, property, parent, BrowserCol(attribute)); }
    QWidget * createAttributeEditor(QtFlagPropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) override;
    inline QWidget * createEditor_protected(QtFlagPropertyManager * manager, QtProperty * property, QWidget * parent) { return QtFlagEditorFactory::createEditor(manager, property, parent); }
    QWidget * createEditor(QtFlagPropertyManager * manager, QtProperty * property, QWidget * parent) override;
    inline void disconnectPropertyManager_protected(QtFlagPropertyManager * manager) { QtFlagEditorFactory::disconnectPropertyManager(manager); }
    void disconnectPropertyManager(QtFlagPropertyManager * manager) override;
    ~QtFlagEditorFactoryWrapper();
    static void pysideInitQtMetaTypes();
    void resetPyMethodCache();
private:
    mutable bool m_PyMethodCache[4];
};

#endif // SBK_QTFLAGEDITORFACTORYWRAPPER_H

