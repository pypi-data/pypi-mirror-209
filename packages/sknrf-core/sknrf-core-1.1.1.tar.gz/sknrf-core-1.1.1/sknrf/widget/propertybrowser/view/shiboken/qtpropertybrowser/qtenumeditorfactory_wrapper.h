#ifndef SBK_QTENUMEDITORFACTORYWRAPPER_H
#define SBK_QTENUMEDITORFACTORYWRAPPER_H

#include <qteditorfactory.h>


// Argument includes
#include <qobject.h>
#include <qobjectdefs.h>
#include <qtpropertybrowser.h>
#include <qtpropertybrowserutils_p.h>
#include <qtpropertymanager.h>
#include <qwidget.h>
class QtEnumEditorFactoryWrapper : public QtEnumEditorFactory
{
public:
    QtEnumEditorFactoryWrapper(QObject * parent = 0);
    inline void connectPropertyManager_protected(QtEnumPropertyManager * manager) { QtEnumEditorFactory::connectPropertyManager(manager); }
    void connectPropertyManager(QtEnumPropertyManager * manager) override;
    inline QWidget * createAttributeEditor_protected(QtEnumPropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) { return QtEnumEditorFactory::createAttributeEditor(manager, property, parent, BrowserCol(attribute)); }
    QWidget * createAttributeEditor(QtEnumPropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) override;
    inline QWidget * createEditor_protected(QtEnumPropertyManager * manager, QtProperty * property, QWidget * parent) { return QtEnumEditorFactory::createEditor(manager, property, parent); }
    QWidget * createEditor(QtEnumPropertyManager * manager, QtProperty * property, QWidget * parent) override;
    inline void disconnectPropertyManager_protected(QtEnumPropertyManager * manager) { QtEnumEditorFactory::disconnectPropertyManager(manager); }
    void disconnectPropertyManager(QtEnumPropertyManager * manager) override;
    ~QtEnumEditorFactoryWrapper();
    static void pysideInitQtMetaTypes();
    void resetPyMethodCache();
private:
    mutable bool m_PyMethodCache[4];
};

#endif // SBK_QTENUMEDITORFACTORYWRAPPER_H

