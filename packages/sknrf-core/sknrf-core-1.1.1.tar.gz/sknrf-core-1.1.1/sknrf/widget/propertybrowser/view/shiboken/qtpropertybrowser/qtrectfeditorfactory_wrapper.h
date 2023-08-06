#ifndef SBK_QTRECTFEDITORFACTORYWRAPPER_H
#define SBK_QTRECTFEDITORFACTORYWRAPPER_H

#include <qteditorfactory.h>


// Argument includes
#include <qobject.h>
#include <qobjectdefs.h>
#include <qtpropertybrowser.h>
#include <qtpropertybrowserutils_p.h>
#include <qtpropertymanager.h>
#include <qwidget.h>
class QtRectFEditorFactoryWrapper : public QtRectFEditorFactory
{
public:
    QtRectFEditorFactoryWrapper(QObject * parent = 0);
    inline void connectPropertyManager_protected(QtRectFPropertyManager * manager) { QtRectFEditorFactory::connectPropertyManager(manager); }
    void connectPropertyManager(QtRectFPropertyManager * manager) override;
    inline QWidget * createAttributeEditor_protected(QtRectFPropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) { return QtRectFEditorFactory::createAttributeEditor(manager, property, parent, BrowserCol(attribute)); }
    QWidget * createAttributeEditor(QtRectFPropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) override;
    inline QWidget * createEditor_protected(QtRectFPropertyManager * manager, QtProperty * property, QWidget * parent) { return QtRectFEditorFactory::createEditor(manager, property, parent); }
    QWidget * createEditor(QtRectFPropertyManager * manager, QtProperty * property, QWidget * parent) override;
    inline void disconnectPropertyManager_protected(QtRectFPropertyManager * manager) { QtRectFEditorFactory::disconnectPropertyManager(manager); }
    void disconnectPropertyManager(QtRectFPropertyManager * manager) override;
    ~QtRectFEditorFactoryWrapper();
    static void pysideInitQtMetaTypes();
    void resetPyMethodCache();
private:
    mutable bool m_PyMethodCache[4];
};

#endif // SBK_QTRECTFEDITORFACTORYWRAPPER_H

