// Copyright (C) 2016 The Qt Company Ltd.
// SPDX-License-Identifier: LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only

#ifndef QTPROPERTYBROWSER_H
#define QTPROPERTYBROWSER_H

#include <QtWidgets/QWidget>
#include <QtCore/QSet>
#include <QtGui/QIcon>
#include <QtWidgets/QLineEdit>

#include "qtpropertybrowserutils_p.h"

QT_BEGIN_NAMESPACE

class QtAbstractPropertyManager;
class QtPropertyPrivate;

class QtProperty
{
public:
    virtual ~QtProperty();

    QList<QtProperty *> subProperties() const;

    QtAbstractPropertyManager *propertyManager() const;

    QString label() const;
    QString toolTip() const { return valueToolTip(); } // Compatibility
    QString valueToolTip() const;
    QString descriptionToolTip() const;
    QString statusTip() const;
    QString whatsThis() const;
    QString propertyName() const;
    bool isEnabled() const;
    bool isModified() const;

    bool hasValue() const;
    QIcon valueIcon() const;
    QIcon checkIcon() const;
    QString valueText() const;
    QString displayText() const;
    QString unitText() const;
    QString pkAvgText() const;
    QString formatText() const;
    QString minimumText() const;
    QString maximumText() const;
    bool check() const;
    QBrush foreground() const;

    void setLabel(const QString &text);
    void setToolTip(const QString &text) { setValueToolTip(text); }  // Compatibility
    void setValueToolTip(const QString &text);
    void setDescriptionToolTip(const QString &text);
    void setStatusTip(const QString &text);
    void setWhatsThis(const QString &text);
    void setPropertyName(const QString &text);
    void setEnabled(bool enable);
    void setModified(bool modified);

    void addSubProperty(QtProperty *property);
    void insertSubProperty(QtProperty *property, QtProperty *afterProperty);
    void removeSubProperty(QtProperty *property);
protected:
    explicit QtProperty(QtAbstractPropertyManager *manager);
    void propertyChanged();
private:
    friend class QtAbstractPropertyManager;
    QScopedPointer<QtPropertyPrivate> d_ptr;
};

class QtAbstractPropertyManagerPrivate;

class QtAbstractPropertyManager : public QObject
{
    Q_OBJECT
public:

    explicit QtAbstractPropertyManager(QObject *parent = 0);
    ~QtAbstractPropertyManager();
    void connect_signals() const{}
    void disconnect_signals() const{}

    QSet<QtProperty *> properties() const;
    void clear() const;
    virtual bool check(const QtProperty *property) const{return false;}

    QtProperty *addProperty(const QString &name = QString());
    virtual bool isReadOnly(const QtProperty *) const{return false;}
    virtual void setCheck(QtProperty *property, bool check){}
    bool attributeEditable(const BrowserCol) const;
    void setAttributeEditable(const BrowserCol, bool);
Q_SIGNALS:

    void propertyInserted(QtProperty *property,
                QtProperty *parent, QtProperty *after);
    void propertyChanged(QtProperty *property);
    void propertyRemoved(QtProperty *property, QtProperty *parent);
    void propertyDestroyed(QtProperty *property);
    void checkChanged(QtProperty *property, bool check);
protected:
    virtual bool hasValue(const QtProperty *property) const;
    virtual QIcon valueIcon(const QtProperty *property) const;
    virtual QIcon checkIcon(const QtProperty *property) const;
    virtual QString valueText(const QtProperty *property) const;
    virtual QString displayText(const QtProperty *property) const{Q_UNUSED(property); return QString();}
    virtual QString unitText(const QtProperty *property) const{Q_UNUSED(property); return QString();}
    virtual QString pkAvgText(const QtProperty *property) const{Q_UNUSED(property); return QString();}
    virtual QString formatText(const QtProperty *property) const{Q_UNUSED(property); return QString();}
    virtual QString minimumText(const QtProperty *property) const{Q_UNUSED(property); return QString();}
    virtual QString maximumText(const QtProperty *property) const{Q_UNUSED(property); return QString();}
    virtual QBrush foreground(const QtProperty *property) const{Q_UNUSED(property);return QBrush(QColor(Qt::black),Qt::SolidPattern);}
    virtual void initializeProperty(QtProperty *property) = 0;
    virtual void uninitializeProperty(QtProperty *property);
    virtual QtProperty *createProperty();
private:
    friend class QtProperty;
    QScopedPointer<QtAbstractPropertyManagerPrivate> d_ptr;
    Q_DECLARE_PRIVATE(QtAbstractPropertyManager)
    Q_DISABLE_COPY_MOVE(QtAbstractPropertyManager)
};

class QtAbstractEditorFactoryBase : public QObject
{
    Q_OBJECT
public:
    virtual QWidget *createEditor(QtProperty *property, QWidget *parent) = 0;
    virtual QWidget *createAttributeEditor(QtProperty *property, QWidget *parent, BrowserCol atttribute) = 0;
protected:
    explicit QtAbstractEditorFactoryBase(QObject *parent = 0)
        : QObject(parent) {}

    virtual void breakConnection(QtAbstractPropertyManager *manager) = 0;
protected Q_SLOTS:
    virtual void managerDestroyed(QObject *manager) = 0;

    friend class QtAbstractPropertyBrowser;
};

template <class PropertyManager>
class QtAbstractEditorFactory : public QtAbstractEditorFactoryBase
{
public:
    explicit QtAbstractEditorFactory(QObject *parent) : QtAbstractEditorFactoryBase(parent) {}
    QWidget *createEditor(QtProperty *property, QWidget *parent) override
    {
        for (PropertyManager *manager : std::as_const(m_managers)) {
            if (manager == property->propertyManager()) {
                return createEditor(manager, property, parent);
            }
        }
        return 0;
    }
    QWidget *createAttributeEditor(QtProperty *property, QWidget *parent, BrowserCol attribute) override
    {
        for (PropertyManager *manager : std::as_const(m_managers)) {
            if (manager == property->propertyManager()) {
                return createAttributeEditor(manager, property, parent, attribute);
            }
        }
        return 0;
    }
    void addPropertyManager(PropertyManager *manager)
    {
        if (m_managers.contains(manager))
            return;
        m_managers.insert(manager);
        connectPropertyManager(manager);
        connect(manager, SIGNAL(destroyed(QObject *)),
                    this, SLOT(managerDestroyed(QObject *)));
    }
    void removePropertyManager(PropertyManager *manager)
    {
        if (!m_managers.contains(manager))
            return;
        disconnect(manager, SIGNAL(destroyed(QObject *)),
                    this, SLOT(managerDestroyed(QObject *)));
        disconnectPropertyManager(manager);
        m_managers.remove(manager);
    }
    QSet<PropertyManager *> propertyManagers() const
    {
        return m_managers;
    }
    PropertyManager *propertyManager(QtProperty *property) const
    {
        QtAbstractPropertyManager *manager = property->propertyManager();
        for (PropertyManager *m : std::as_const(m_managers)) {
            if (m == manager) {
                return m;
            }
        }
        return 0;
    }
protected:
    virtual void connectPropertyManager(PropertyManager *manager) = 0;
    virtual QWidget *createEditor(PropertyManager *manager, QtProperty *property,
                QWidget *parent) = 0;
    virtual QWidget *createAttributeEditor(PropertyManager *manager, QtProperty *property,QWidget *parent, BrowserCol attribute)
    {Q_UNUSED(manager);Q_UNUSED(property);Q_UNUSED(parent);Q_UNUSED(attribute);return nullptr;}
    virtual void disconnectPropertyManager(PropertyManager *manager) = 0;
    void managerDestroyed(QObject *manager) override
    {
        for (PropertyManager *m : std::as_const(m_managers)) {
            if (m == manager) {
                m_managers.remove(m);
                return;
            }
        }
    }
private:
    void breakConnection(QtAbstractPropertyManager *manager) override
    {
        for (PropertyManager *m : std::as_const(m_managers)) {
            if (m == manager) {
                removePropertyManager(m);
                return;
            }
        }
    }
private:
    QSet<PropertyManager *> m_managers;
    friend class QtAbstractPropertyEditor;
};

class QtAbstractPropertyBrowser;
class QtBrowserItemPrivate;

class QtBrowserItem
{
public:
    QtProperty *property() const;
    QtBrowserItem *parent() const;
    QList<QtBrowserItem *> children() const;
    QtAbstractPropertyBrowser *browser() const;
private:
    explicit QtBrowserItem(QtAbstractPropertyBrowser *browser, QtProperty *property, QtBrowserItem *parent);
    ~QtBrowserItem();
    QScopedPointer<QtBrowserItemPrivate> d_ptr;
    friend class QtAbstractPropertyBrowserPrivate;
};

class QtAbstractPropertyBrowserPrivate;

class QtAbstractPropertyBrowser : public QWidget
{
    Q_OBJECT
public:

    explicit QtAbstractPropertyBrowser(QWidget *parent = 0);
    ~QtAbstractPropertyBrowser();

    QList<QtProperty *> properties() const;
    QList<QtBrowserItem *> items(QtProperty *property) const;
    QtBrowserItem *topLevelItem(QtProperty *property) const;
    QList<QtBrowserItem *> topLevelItems() const;
    void clear();

    template <class PropertyManager>
    void setFactoryForManager(PropertyManager *manager,
                    QtAbstractEditorFactory<PropertyManager> *factory) {
        QtAbstractPropertyManager *abstractManager = manager;
        QtAbstractEditorFactoryBase *abstractFactory = factory;

        if (addFactory(abstractManager, abstractFactory))
            factory->addPropertyManager(manager);
    }

    void unsetFactoryForManager(QtAbstractPropertyManager *manager);

    QtBrowserItem *currentItem() const;
    void setCurrentItem(QtBrowserItem *);

Q_SIGNALS:
    void currentItemChanged(QtBrowserItem *);

public Q_SLOTS:

    QtBrowserItem *addProperty(QtProperty *property);
    QtBrowserItem *insertProperty(QtProperty *property, QtProperty *afterProperty);
    void removeProperty(QtProperty *property);

protected:

    virtual void itemInserted(QtBrowserItem *item, QtBrowserItem *afterItem) = 0;
    virtual void itemRemoved(QtBrowserItem *item) = 0;
    // can be tooltip, statustip, whatsthis, name, icon, text.
    virtual void itemChanged(QtBrowserItem *item) = 0;

    virtual QWidget *createEditor(QtProperty *property, QWidget *parent);
    virtual QWidget *createAttributeEditor(QtProperty *property, QWidget *parent, BrowserCol attribute);
private:

    bool addFactory(QtAbstractPropertyManager *abstractManager,
                QtAbstractEditorFactoryBase *abstractFactory);

    QScopedPointer<QtAbstractPropertyBrowserPrivate> d_ptr;
    Q_DECLARE_PRIVATE(QtAbstractPropertyBrowser)
    Q_DISABLE_COPY_MOVE(QtAbstractPropertyBrowser)
    Q_PRIVATE_SLOT(d_func(), void slotPropertyInserted(QtProperty *,
                            QtProperty *, QtProperty *))
    Q_PRIVATE_SLOT(d_func(), void slotPropertyRemoved(QtProperty *,
                            QtProperty *))
    Q_PRIVATE_SLOT(d_func(), void slotPropertyDestroyed(QtProperty *))
    Q_PRIVATE_SLOT(d_func(), void slotPropertyDataChanged(QtProperty *))

};

QT_END_NAMESPACE

#endif // QTPROPERTYBROWSER_H
