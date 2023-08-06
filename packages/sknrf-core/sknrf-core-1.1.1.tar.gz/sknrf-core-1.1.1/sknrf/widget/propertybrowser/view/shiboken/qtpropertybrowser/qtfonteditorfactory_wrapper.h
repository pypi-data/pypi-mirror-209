#ifndef SBK_QTFONTEDITORFACTORYWRAPPER_H
#define SBK_QTFONTEDITORFACTORYWRAPPER_H

#include <qteditorfactory.h>


// Argument includes
#include <qobject.h>
#include <qobjectdefs.h>
#include <qtpropertybrowser.h>
#include <qtpropertybrowserutils_p.h>
#include <qtpropertymanager.h>
#include <qwidget.h>
class QtFontEditorFactoryWrapper : public QtFontEditorFactory
{
public:
    QtFontEditorFactoryWrapper(QObject * parent = 0);
    inline void connectPropertyManager_protected(QtFontPropertyManager * manager) { QtFontEditorFactory::connectPropertyManager(manager); }
    void connectPropertyManager(QtFontPropertyManager * manager) override;
    inline QWidget * createAttributeEditor_protected(QtFontPropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) { return QtFontEditorFactory::createAttributeEditor(manager, property, parent, BrowserCol(attribute)); }
    QWidget * createAttributeEditor(QtFontPropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) override;
    inline QWidget * createEditor_protected(QtFontPropertyManager * manager, QtProperty * property, QWidget * parent) { return QtFontEditorFactory::createEditor(manager, property, parent); }
    QWidget * createEditor(QtFontPropertyManager * manager, QtProperty * property, QWidget * parent) override;
    inline void disconnectPropertyManager_protected(QtFontPropertyManager * manager) { QtFontEditorFactory::disconnectPropertyManager(manager); }
    void disconnectPropertyManager(QtFontPropertyManager * manager) override;
    ~QtFontEditorFactoryWrapper();
    static void pysideInitQtMetaTypes();
    void resetPyMethodCache();
private:
    mutable bool m_PyMethodCache[4];
};

#endif // SBK_QTFONTEDITORFACTORYWRAPPER_H

