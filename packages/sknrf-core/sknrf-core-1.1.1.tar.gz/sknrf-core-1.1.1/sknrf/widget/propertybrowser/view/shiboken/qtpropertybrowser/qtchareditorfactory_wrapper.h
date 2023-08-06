#ifndef SBK_QTCHAREDITORFACTORYWRAPPER_H
#define SBK_QTCHAREDITORFACTORYWRAPPER_H

#include <qteditorfactory.h>


// Argument includes
#include <qobject.h>
#include <qobjectdefs.h>
#include <qtpropertybrowser.h>
#include <qtpropertybrowserutils_p.h>
#include <qtpropertymanager.h>
#include <qwidget.h>
class QtCharEditorFactoryWrapper : public QtCharEditorFactory
{
public:
    QtCharEditorFactoryWrapper(QObject * parent = 0);
    inline void connectPropertyManager_protected(QtCharPropertyManager * manager) { QtCharEditorFactory::connectPropertyManager(manager); }
    void connectPropertyManager(QtCharPropertyManager * manager) override;
    inline QWidget * createAttributeEditor_protected(QtCharPropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) { return QtCharEditorFactory::createAttributeEditor(manager, property, parent, BrowserCol(attribute)); }
    QWidget * createAttributeEditor(QtCharPropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) override;
    inline QWidget * createEditor_protected(QtCharPropertyManager * manager, QtProperty * property, QWidget * parent) { return QtCharEditorFactory::createEditor(manager, property, parent); }
    QWidget * createEditor(QtCharPropertyManager * manager, QtProperty * property, QWidget * parent) override;
    inline void disconnectPropertyManager_protected(QtCharPropertyManager * manager) { QtCharEditorFactory::disconnectPropertyManager(manager); }
    void disconnectPropertyManager(QtCharPropertyManager * manager) override;
    ~QtCharEditorFactoryWrapper();
    static void pysideInitQtMetaTypes();
    void resetPyMethodCache();
private:
    mutable bool m_PyMethodCache[4];
};

#endif // SBK_QTCHAREDITORFACTORYWRAPPER_H

