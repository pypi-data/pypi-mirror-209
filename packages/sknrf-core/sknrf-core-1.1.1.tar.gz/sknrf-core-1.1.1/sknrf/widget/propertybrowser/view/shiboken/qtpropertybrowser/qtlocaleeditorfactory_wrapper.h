#ifndef SBK_QTLOCALEEDITORFACTORYWRAPPER_H
#define SBK_QTLOCALEEDITORFACTORYWRAPPER_H

#include <qteditorfactory.h>


// Argument includes
#include <qobject.h>
#include <qobjectdefs.h>
#include <qtpropertybrowser.h>
#include <qtpropertybrowserutils_p.h>
#include <qtpropertymanager.h>
#include <qwidget.h>
class QtLocaleEditorFactoryWrapper : public QtLocaleEditorFactory
{
public:
    QtLocaleEditorFactoryWrapper(QObject * parent = 0);
    inline void connectPropertyManager_protected(QtLocalePropertyManager * manager) { QtLocaleEditorFactory::connectPropertyManager(manager); }
    void connectPropertyManager(QtLocalePropertyManager * manager) override;
    inline QWidget * createAttributeEditor_protected(QtLocalePropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) { return QtLocaleEditorFactory::createAttributeEditor(manager, property, parent, BrowserCol(attribute)); }
    QWidget * createAttributeEditor(QtLocalePropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) override;
    inline QWidget * createEditor_protected(QtLocalePropertyManager * manager, QtProperty * property, QWidget * parent) { return QtLocaleEditorFactory::createEditor(manager, property, parent); }
    QWidget * createEditor(QtLocalePropertyManager * manager, QtProperty * property, QWidget * parent) override;
    inline void disconnectPropertyManager_protected(QtLocalePropertyManager * manager) { QtLocaleEditorFactory::disconnectPropertyManager(manager); }
    void disconnectPropertyManager(QtLocalePropertyManager * manager) override;
    ~QtLocaleEditorFactoryWrapper();
    static void pysideInitQtMetaTypes();
    void resetPyMethodCache();
private:
    mutable bool m_PyMethodCache[4];
};

#endif // SBK_QTLOCALEEDITORFACTORYWRAPPER_H

