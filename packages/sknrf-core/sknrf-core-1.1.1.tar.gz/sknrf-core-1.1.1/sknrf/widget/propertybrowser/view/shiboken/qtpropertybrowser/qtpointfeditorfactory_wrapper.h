#ifndef SBK_QTPOINTFEDITORFACTORYWRAPPER_H
#define SBK_QTPOINTFEDITORFACTORYWRAPPER_H

#include <qteditorfactory.h>


// Argument includes
#include <qobject.h>
#include <qobjectdefs.h>
#include <qtpropertybrowser.h>
#include <qtpropertybrowserutils_p.h>
#include <qtpropertymanager.h>
#include <qwidget.h>
class QtPointFEditorFactoryWrapper : public QtPointFEditorFactory
{
public:
    QtPointFEditorFactoryWrapper(QObject * parent = 0);
    inline void connectPropertyManager_protected(QtPointFPropertyManager * manager) { QtPointFEditorFactory::connectPropertyManager(manager); }
    void connectPropertyManager(QtPointFPropertyManager * manager) override;
    inline QWidget * createAttributeEditor_protected(QtPointFPropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) { return QtPointFEditorFactory::createAttributeEditor(manager, property, parent, BrowserCol(attribute)); }
    QWidget * createAttributeEditor(QtPointFPropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) override;
    inline QWidget * createEditor_protected(QtPointFPropertyManager * manager, QtProperty * property, QWidget * parent) { return QtPointFEditorFactory::createEditor(manager, property, parent); }
    QWidget * createEditor(QtPointFPropertyManager * manager, QtProperty * property, QWidget * parent) override;
    inline void disconnectPropertyManager_protected(QtPointFPropertyManager * manager) { QtPointFEditorFactory::disconnectPropertyManager(manager); }
    void disconnectPropertyManager(QtPointFPropertyManager * manager) override;
    ~QtPointFEditorFactoryWrapper();
    static void pysideInitQtMetaTypes();
    void resetPyMethodCache();
private:
    mutable bool m_PyMethodCache[4];
};

#endif // SBK_QTPOINTFEDITORFACTORYWRAPPER_H

