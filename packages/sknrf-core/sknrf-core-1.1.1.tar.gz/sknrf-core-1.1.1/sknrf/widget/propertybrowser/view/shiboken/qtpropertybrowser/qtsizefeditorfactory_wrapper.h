#ifndef SBK_QTSIZEFEDITORFACTORYWRAPPER_H
#define SBK_QTSIZEFEDITORFACTORYWRAPPER_H

#include <qteditorfactory.h>


// Argument includes
#include <qobject.h>
#include <qobjectdefs.h>
#include <qtpropertybrowser.h>
#include <qtpropertybrowserutils_p.h>
#include <qtpropertymanager.h>
#include <qwidget.h>
class QtSizeFEditorFactoryWrapper : public QtSizeFEditorFactory
{
public:
    QtSizeFEditorFactoryWrapper(QObject * parent = 0);
    inline void connectPropertyManager_protected(QtSizeFPropertyManager * manager) { QtSizeFEditorFactory::connectPropertyManager(manager); }
    void connectPropertyManager(QtSizeFPropertyManager * manager) override;
    inline QWidget * createAttributeEditor_protected(QtSizeFPropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) { return QtSizeFEditorFactory::createAttributeEditor(manager, property, parent, BrowserCol(attribute)); }
    QWidget * createAttributeEditor(QtSizeFPropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) override;
    inline QWidget * createEditor_protected(QtSizeFPropertyManager * manager, QtProperty * property, QWidget * parent) { return QtSizeFEditorFactory::createEditor(manager, property, parent); }
    QWidget * createEditor(QtSizeFPropertyManager * manager, QtProperty * property, QWidget * parent) override;
    inline void disconnectPropertyManager_protected(QtSizeFPropertyManager * manager) { QtSizeFEditorFactory::disconnectPropertyManager(manager); }
    void disconnectPropertyManager(QtSizeFPropertyManager * manager) override;
    ~QtSizeFEditorFactoryWrapper();
    static void pysideInitQtMetaTypes();
    void resetPyMethodCache();
private:
    mutable bool m_PyMethodCache[4];
};

#endif // SBK_QTSIZEFEDITORFACTORYWRAPPER_H

