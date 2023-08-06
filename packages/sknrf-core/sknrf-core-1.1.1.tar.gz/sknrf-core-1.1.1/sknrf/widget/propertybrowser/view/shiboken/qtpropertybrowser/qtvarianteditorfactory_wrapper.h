#ifndef SBK_QTVARIANTEDITORFACTORYWRAPPER_H
#define SBK_QTVARIANTEDITORFACTORYWRAPPER_H

#include <qtvariantproperty.h>


// Argument includes
#include <qobject.h>
#include <qobjectdefs.h>
#include <qtpropertybrowser.h>
#include <qtvariantproperty.h>
#include <qwidget.h>
class QtVariantEditorFactoryWrapper : public QtVariantEditorFactory
{
public:
    QtVariantEditorFactoryWrapper(QObject * parent = nullptr);
    inline void connectPropertyManager_protected(QtVariantPropertyManager * manager) { QtVariantEditorFactory::connectPropertyManager(manager); }
    void connectPropertyManager(QtVariantPropertyManager * manager) override;
    inline QWidget * createEditor_protected(QtVariantPropertyManager * manager, QtProperty * property, QWidget * parent) { return QtVariantEditorFactory::createEditor(manager, property, parent); }
    QWidget * createEditor(QtVariantPropertyManager * manager, QtProperty * property, QWidget * parent) override;
    inline void disconnectPropertyManager_protected(QtVariantPropertyManager * manager) { QtVariantEditorFactory::disconnectPropertyManager(manager); }
    void disconnectPropertyManager(QtVariantPropertyManager * manager) override;
    ~QtVariantEditorFactoryWrapper();
    static void pysideInitQtMetaTypes();
    void resetPyMethodCache();
private:
    mutable bool m_PyMethodCache[3];
};

#endif // SBK_QTVARIANTEDITORFACTORYWRAPPER_H

