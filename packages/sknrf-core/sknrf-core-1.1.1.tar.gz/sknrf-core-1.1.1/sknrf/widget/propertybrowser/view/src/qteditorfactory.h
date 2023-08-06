// Copyright (C) 2016 The Qt Company Ltd.
// SPDX-License-Identifier: LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only

#ifndef QTEDITORFACTORY_H
#define QTEDITORFACTORY_H

#include "qtpropertybrowser.h"
#include "qtpropertymanager.h"

QT_BEGIN_NAMESPACE

class QRegularExpression;

class QtGroupEditorFactoryPrivate;

class QtGroupEditorFactory : public QtAbstractEditorFactory<QtGroupPropertyManager>
{
    Q_OBJECT
public:
    QtGroupEditorFactory(QObject *parent = 0);
    ~QtGroupEditorFactory();
protected:
    void connectPropertyManager(QtGroupPropertyManager *manager) override;
    QWidget *createEditor(QtGroupPropertyManager *manager, QtProperty *property,
                          QWidget *parent) override;
    QWidget *createAttributeEditor(QtGroupPropertyManager *manager, QtProperty *property,
                                   QWidget *parent, BrowserCol attribute) override;
    void disconnectPropertyManager(QtGroupPropertyManager *manager) override;
private:
    QtGroupEditorFactoryPrivate *d_ptr;
    Q_DECLARE_PRIVATE(QtGroupEditorFactory)
    Q_DISABLE_COPY_MOVE(QtGroupEditorFactory)
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
};

class QtSpinBoxFactoryPrivate;

class QtSpinBoxFactory : public QtAbstractEditorFactory<QtIntPropertyManager>
{
    Q_OBJECT
public:
    QtSpinBoxFactory(QObject *parent = 0);
    ~QtSpinBoxFactory();
protected:
    void connectPropertyManager(QtIntPropertyManager *manager) override;
    QWidget *createEditor(QtIntPropertyManager *manager, QtProperty *property,
                QWidget *parent) override;
    QWidget *createAttributeEditor(QtIntPropertyManager *manager, QtProperty *property,
                                   QWidget *parent, BrowserCol attribute) override;
    void disconnectPropertyManager(QtIntPropertyManager *manager) override;
private:
    QScopedPointer<QtSpinBoxFactoryPrivate> d_ptr;
    Q_DECLARE_PRIVATE(QtSpinBoxFactory)
    Q_DISABLE_COPY_MOVE(QtSpinBoxFactory)
    Q_PRIVATE_SLOT(d_func(), void slotPropertyChanged(QtProperty *, int))
    Q_PRIVATE_SLOT(d_func(), void slotRangeChanged(QtProperty *, int, int))
    Q_PRIVATE_SLOT(d_func(), void slotSingleStepChanged(QtProperty *, int))
    Q_PRIVATE_SLOT(d_func(), void slotReadOnlyChanged(QtProperty *, bool))
    Q_PRIVATE_SLOT(d_func(), void slotSetValue(int))
    Q_PRIVATE_SLOT(d_func(), void slotSetMinimum(int))
    Q_PRIVATE_SLOT(d_func(), void slotSetMaximum(int))
    Q_PRIVATE_SLOT(d_func(), void slotSetMinimum(double))
    Q_PRIVATE_SLOT(d_func(), void slotSetMaximum(double))
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotMinimumAttributeEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotMaximumAttributeEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
};

class QtIntEditFactoryPrivate;

class QtIntEditFactory : public QtAbstractEditorFactory<QtIntPropertyManager>
{
    Q_OBJECT
public:
    QtIntEditFactory(QObject *parent = 0);
    ~QtIntEditFactory();
protected:
    void connectPropertyManager(QtIntPropertyManager *manager) override;
    QWidget *createEditor(QtIntPropertyManager *manager, QtProperty *property,
                          QWidget *parent) override;
    QWidget *createAttributeEditor(QtIntPropertyManager *manager, QtProperty *property,
                                   QWidget *parent, BrowserCol attribute) override;
    void disconnectPropertyManager(QtIntPropertyManager *manager) override;
private:
    QScopedPointer<QtIntEditFactoryPrivate> d_ptr;
    Q_DECLARE_PRIVATE(QtIntEditFactory)
    Q_DISABLE_COPY_MOVE(QtIntEditFactory)
    Q_PRIVATE_SLOT(d_func(), void slotPropertyChanged(QtProperty *, int))
    Q_PRIVATE_SLOT(d_func(), void slotRangeChanged(QtProperty *, double, double))
    Q_PRIVATE_SLOT(d_func(), void slotRangeChanged(QtProperty *, int, int))
    Q_PRIVATE_SLOT(d_func(), void slotReadOnlyChanged(QtProperty *, bool))
    Q_PRIVATE_SLOT(d_func(), void slotSetValue(int))
    Q_PRIVATE_SLOT(d_func(), void slotSetMinimum(int))
    Q_PRIVATE_SLOT(d_func(), void slotSetMaximum(int))
    Q_PRIVATE_SLOT(d_func(), void slotSetMinimum(double))
    Q_PRIVATE_SLOT(d_func(), void slotSetMaximum(double))
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotMinimumAttributeEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotMaximumAttributeEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
};

class QtSliderFactoryPrivate;

class QtSliderFactory : public QtAbstractEditorFactory<QtIntPropertyManager>
{
    Q_OBJECT
public:
    QtSliderFactory(QObject *parent = 0);
    ~QtSliderFactory();
protected:
    void connectPropertyManager(QtIntPropertyManager *manager) override;
    QWidget *createEditor(QtIntPropertyManager *manager, QtProperty *property,
                QWidget *parent) override;
    QWidget *createAttributeEditor(QtIntPropertyManager *manager, QtProperty *property,
                                   QWidget *parent, BrowserCol attribute) override;
    void disconnectPropertyManager(QtIntPropertyManager *manager) override;
private:
    QScopedPointer<QtSliderFactoryPrivate> d_ptr;
    Q_DECLARE_PRIVATE(QtSliderFactory)
    Q_DISABLE_COPY_MOVE(QtSliderFactory)
    Q_PRIVATE_SLOT(d_func(), void slotPropertyChanged(QtProperty *, int))
    Q_PRIVATE_SLOT(d_func(), void slotRangeChanged(QtProperty *, int, int))
    Q_PRIVATE_SLOT(d_func(), void slotSingleStepChanged(QtProperty *, int))
    Q_PRIVATE_SLOT(d_func(), void slotSetValue(int))
    Q_PRIVATE_SLOT(d_func(), void slotSetMinimum(int))
    Q_PRIVATE_SLOT(d_func(), void slotSetMaximum(int))
    Q_PRIVATE_SLOT(d_func(), void slotSetMinimum(double))
    Q_PRIVATE_SLOT(d_func(), void slotSetMaximum(double))
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotMinimumAttributeEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotMaximumAttributeEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
};

class QtScrollBarFactoryPrivate;

class QtScrollBarFactory : public QtAbstractEditorFactory<QtIntPropertyManager>
{
    Q_OBJECT
public:
    QtScrollBarFactory(QObject *parent = 0);
    ~QtScrollBarFactory();
protected:
    void connectPropertyManager(QtIntPropertyManager *manager) override;
    QWidget *createEditor(QtIntPropertyManager *manager, QtProperty *property,
                QWidget *parent) override;
    QWidget *createAttributeEditor(QtIntPropertyManager *manager, QtProperty *property,
                                   QWidget *parent, BrowserCol attribute) override;
    void disconnectPropertyManager(QtIntPropertyManager *manager) override;
private:
    QScopedPointer<QtScrollBarFactoryPrivate> d_ptr;
    Q_DECLARE_PRIVATE(QtScrollBarFactory)
    Q_DISABLE_COPY_MOVE(QtScrollBarFactory)
    Q_PRIVATE_SLOT(d_func(), void slotPropertyChanged(QtProperty *, int))
    Q_PRIVATE_SLOT(d_func(), void slotRangeChanged(QtProperty *, int, int))
    Q_PRIVATE_SLOT(d_func(), void slotSingleStepChanged(QtProperty *, int))
    Q_PRIVATE_SLOT(d_func(), void slotSetValue(int))
    Q_PRIVATE_SLOT(d_func(), void slotSetMinimum(int))
    Q_PRIVATE_SLOT(d_func(), void slotSetMaximum(int))
    Q_PRIVATE_SLOT(d_func(), void slotSetMinimum(double))
    Q_PRIVATE_SLOT(d_func(), void slotSetMaximum(double))
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotMinimumAttributeEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotMaximumAttributeEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
};

class QtCheckBoxFactoryPrivate;

class QtCheckBoxFactory : public QtAbstractEditorFactory<QtBoolPropertyManager>
{
    Q_OBJECT
public:
    QtCheckBoxFactory(QObject *parent = 0);
    ~QtCheckBoxFactory();
protected:
    void connectPropertyManager(QtBoolPropertyManager *manager) override;
    QWidget *createEditor(QtBoolPropertyManager *manager, QtProperty *property,
                QWidget *parent) override;
    QWidget *createAttributeEditor(QtBoolPropertyManager *manager, QtProperty *property,
                                   QWidget *parent, BrowserCol attribute) override;
    void disconnectPropertyManager(QtBoolPropertyManager *manager) override;
private:
    QScopedPointer<QtCheckBoxFactoryPrivate> d_ptr;
    Q_DECLARE_PRIVATE(QtCheckBoxFactory)
    Q_DISABLE_COPY_MOVE(QtCheckBoxFactory)
    Q_PRIVATE_SLOT(d_func(), void slotPropertyChanged(QtProperty *, bool))
    Q_PRIVATE_SLOT(d_func(), void slotSetValue(bool))
    Q_PRIVATE_SLOT(d_func(), void slotEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
};

class QtDoubleSpinBoxFactoryPrivate;

class QtDoubleSpinBoxFactory : public QtAbstractEditorFactory<QtDoublePropertyManager>
{
    Q_OBJECT
public:
    QtDoubleSpinBoxFactory(QObject *parent = 0);
    ~QtDoubleSpinBoxFactory();
protected:
    void connectPropertyManager(QtDoublePropertyManager *manager) override;
    QWidget *createEditor(QtDoublePropertyManager *manager, QtProperty *property,
                QWidget *parent) override;
    QWidget *createAttributeEditor(QtDoublePropertyManager *manager, QtProperty *property,
                                   QWidget *parent, BrowserCol attribute) override;
    void disconnectPropertyManager(QtDoublePropertyManager *manager) override;
private:
    QScopedPointer<QtDoubleSpinBoxFactoryPrivate> d_ptr;
    Q_DECLARE_PRIVATE(QtDoubleSpinBoxFactory)
    Q_DISABLE_COPY_MOVE(QtDoubleSpinBoxFactory)
    Q_PRIVATE_SLOT(d_func(), void slotPropertyChanged(QtProperty *, double))
    Q_PRIVATE_SLOT(d_func(), void slotRangeChanged(QtProperty *, double, double))
    Q_PRIVATE_SLOT(d_func(), void slotSingleStepChanged(QtProperty *, double))
    Q_PRIVATE_SLOT(d_func(), void slotPrecisionChanged(QtProperty *, int))
    Q_PRIVATE_SLOT(d_func(), void slotReadOnlyChanged(QtProperty *, bool))
    Q_PRIVATE_SLOT(d_func(), void slotSetValue(double))
    Q_PRIVATE_SLOT(d_func(), void slotSetScale(int))
    Q_PRIVATE_SLOT(d_func(), void slotSetFormat(int))
    Q_PRIVATE_SLOT(d_func(), void slotSetMinimum(double))
    Q_PRIVATE_SLOT(d_func(), void slotSetMaximum(double))
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotUnitAttributeEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotFormatAttributeEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotMinimumAttributeEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotMaximumAttributeEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
};

class QtDoubleEditFactoryPrivate;

class QtDoubleEditFactory : public QtAbstractEditorFactory<QtDoublePropertyManager>
{
    Q_OBJECT
public:
    QtDoubleEditFactory(QObject *parent = 0);
    ~QtDoubleEditFactory();
protected:
    void connectPropertyManager(QtDoublePropertyManager *manager) override;
    QWidget *createEditor(QtDoublePropertyManager *manager, QtProperty *property,
                          QWidget *parent) override;
    QWidget *createAttributeEditor(QtDoublePropertyManager *manager, QtProperty *property,
                                   QWidget *parent, BrowserCol attribute) override;
    void disconnectPropertyManager(QtDoublePropertyManager *manager) override;
private:
    QScopedPointer<QtDoubleEditFactoryPrivate> d_ptr;
    Q_DECLARE_PRIVATE(QtDoubleEditFactory)
    Q_DISABLE_COPY_MOVE(QtDoubleEditFactory)
    Q_PRIVATE_SLOT(d_func(), void slotPropertyChanged(QtProperty *, double))
    Q_PRIVATE_SLOT(d_func(), void slotRangeChanged(QtProperty *, double, double))
    Q_PRIVATE_SLOT(d_func(), void slotPrecisionChanged(QtProperty *, int))
    Q_PRIVATE_SLOT(d_func(), void slotReadOnlyChanged(QtProperty *, bool))
    Q_PRIVATE_SLOT(d_func(), void slotSetValue(double))
    Q_PRIVATE_SLOT(d_func(), void slotSetScale(int))
    Q_PRIVATE_SLOT(d_func(), void slotSetFormat(int))
    Q_PRIVATE_SLOT(d_func(), void slotSetMinimum(double))
    Q_PRIVATE_SLOT(d_func(), void slotSetMaximum(double))
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotUnitAttributeEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotFormatAttributeEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotMinimumAttributeEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotMaximumAttributeEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
};

class QtComplexEditFactoryPrivate;

class QtComplexEditFactory : public QtAbstractEditorFactory<QtComplexPropertyManager>
{
    Q_OBJECT
public:
    QtComplexEditFactory(QObject *parent = 0);
    ~QtComplexEditFactory();
protected:
    void connectPropertyManager(QtComplexPropertyManager *manager) override;
    QWidget *createEditor(QtComplexPropertyManager *manager, QtProperty *property,
                          QWidget *parent) override;
    QWidget *createAttributeEditor(QtComplexPropertyManager *manager, QtProperty *property,
                                   QWidget *parent, BrowserCol attribute) override;
    void disconnectPropertyManager(QtComplexPropertyManager *manager) override;
private:
    QScopedPointer<QtComplexEditFactoryPrivate> d_ptr;
    Q_DECLARE_PRIVATE(QtComplexEditFactory)
    Q_DISABLE_COPY_MOVE(QtComplexEditFactory)
    Q_PRIVATE_SLOT(d_func(), void slotPropertyChanged(QtProperty *, const QtComplex&))
    Q_PRIVATE_SLOT(d_func(), void slotRangeChanged(QtProperty *, const QtComplex&, const QtComplex&))
    Q_PRIVATE_SLOT(d_func(), void slotPrecisionChanged(QtProperty *, int))
    Q_PRIVATE_SLOT(d_func(), void slotReadOnlyChanged(QtProperty *, bool))
    Q_PRIVATE_SLOT(d_func(), void slotSetValue(const QtComplex&))
    Q_PRIVATE_SLOT(d_func(), void slotSetScale(int))
    Q_PRIVATE_SLOT(d_func(), void slotSetPkAvg(int))
    Q_PRIVATE_SLOT(d_func(), void slotSetFormat(int))
    Q_PRIVATE_SLOT(d_func(), void slotSetMinimum(double))
    Q_PRIVATE_SLOT(d_func(), void slotSetMaximum(double))
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotUnitAttributeEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotFormatAttributeEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotMinimumAttributeEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotMaximumAttributeEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
    friend class QtVectorComplexEditFactoryPrivate;
};

class QtQuaternionEditFactoryPrivate;

class QtQuaternionEditFactory : public QtAbstractEditorFactory<QtQuaternionPropertyManager>
{
Q_OBJECT
public:
    QtQuaternionEditFactory(QObject *parent = 0);
    ~QtQuaternionEditFactory();
protected:
    void connectPropertyManager(QtQuaternionPropertyManager *manager) override;
    QWidget *createEditor(QtQuaternionPropertyManager *manager, QtProperty *property,
                          QWidget *parent) override;
    QWidget *createAttributeEditor(QtQuaternionPropertyManager *manager, QtProperty *property,
                                   QWidget *parent, BrowserCol attribute) override;
    void disconnectPropertyManager(QtQuaternionPropertyManager *manager) override;
private:
    QScopedPointer<QtQuaternionEditFactoryPrivate> d_ptr;
    Q_DECLARE_PRIVATE(QtQuaternionEditFactory)
    Q_DISABLE_COPY_MOVE(QtQuaternionEditFactory)
    Q_PRIVATE_SLOT(d_func(), void slotPropertyChanged(QtProperty *, const QtQuaternion&))
    Q_PRIVATE_SLOT(d_func(), void slotRangeChanged(QtProperty *, const QtQuaternion&, const QtQuaternion&))
    Q_PRIVATE_SLOT(d_func(), void slotPrecisionChanged(QtProperty *, int))
    Q_PRIVATE_SLOT(d_func(), void slotReadOnlyChanged(QtProperty *, bool))
    Q_PRIVATE_SLOT(d_func(), void slotSetValue(const QtQuaternion&))
    Q_PRIVATE_SLOT(d_func(), void slotSetScale(int))
    Q_PRIVATE_SLOT(d_func(), void slotSetPkAvg(int))
    Q_PRIVATE_SLOT(d_func(), void slotSetFormat(int))
    Q_PRIVATE_SLOT(d_func(), void slotSetMinimum(double))
    Q_PRIVATE_SLOT(d_func(), void slotSetMaximum(double))
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotUnitAttributeEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotFormatAttributeEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotMinimumAttributeEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotMaximumAttributeEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
    friend class QtVectorComplexEditFactoryPrivate;
};

class QtVectorComplexEditFactoryPrivate;

class QtVectorComplexEditFactory : public QtAbstractEditorFactory<QtVectorComplexPropertyManager>
{
    Q_OBJECT
public:
    QtVectorComplexEditFactory(QObject *parent = 0);
    ~QtVectorComplexEditFactory();
    void setSubFactory(QtComplexEditFactory* subFactory);
protected:
    void connectPropertyManager(QtVectorComplexPropertyManager *manager) override;
    QWidget *createEditor(QtVectorComplexPropertyManager *manager, QtProperty *property,
                          QWidget *parent) override;
    QWidget *createAttributeEditor(QtVectorComplexPropertyManager *manager, QtProperty *property,
                                   QWidget *parent, BrowserCol attribute) override;
    void disconnectPropertyManager(QtVectorComplexPropertyManager *manager) override;
    QtComplexEditFactory* subFactory() const;
private:
    QScopedPointer<QtVectorComplexEditFactoryPrivate> d_ptr;
    Q_DECLARE_PRIVATE(QtVectorComplexEditFactory)
    Q_DISABLE_COPY_MOVE(QtVectorComplexEditFactory)
    Q_PRIVATE_SLOT(d_func(), void slotPropertyChanged(QtProperty *, const QVector<QtComplex>& value))
    Q_PRIVATE_SLOT(d_func(), void slotSetScale(int))
    Q_PRIVATE_SLOT(d_func(), void slotSetPkAvg(int))
    Q_PRIVATE_SLOT(d_func(), void slotSetFormat(int))
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotUnitAttributeEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotPkAvgAttributeEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotFormatAttributeEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotMinimumAttributeEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotMaximumAttributeEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
};

class QtLineEditFactoryPrivate;

class QtLineEditFactory : public QtAbstractEditorFactory<QtStringPropertyManager>
{
    Q_OBJECT
public:
    QtLineEditFactory(QObject *parent = 0);
    ~QtLineEditFactory();
protected:
    void connectPropertyManager(QtStringPropertyManager *manager) override;
    QWidget *createEditor(QtStringPropertyManager *manager, QtProperty *property,
                QWidget *parent) override;
    QWidget *createAttributeEditor(QtStringPropertyManager *manager, QtProperty *property,
                                   QWidget *parent, BrowserCol attribute) override;
    void disconnectPropertyManager(QtStringPropertyManager *manager) override;
private:
    QScopedPointer<QtLineEditFactoryPrivate> d_ptr;
    Q_DECLARE_PRIVATE(QtLineEditFactory)
    Q_DISABLE_COPY_MOVE(QtLineEditFactory)
    Q_PRIVATE_SLOT(d_func(), void slotPropertyChanged(QtProperty *, const QString &))
    Q_PRIVATE_SLOT(d_func(), void slotRegExpChanged(QtProperty *, const QRegularExpression &))
    Q_PRIVATE_SLOT(d_func(), void slotReadOnlyChanged(QtProperty *, bool))
    Q_PRIVATE_SLOT(d_func(), void slotSetValue(const QString &))
    Q_PRIVATE_SLOT(d_func(), void slotEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
};

class QtDateEditFactoryPrivate;

class QtDateEditFactory : public QtAbstractEditorFactory<QtDatePropertyManager>
{
    Q_OBJECT
public:
    QtDateEditFactory(QObject *parent = 0);
    ~QtDateEditFactory();
protected:
    void connectPropertyManager(QtDatePropertyManager *manager) override;
    QWidget *createEditor(QtDatePropertyManager *manager, QtProperty *property,
                QWidget *parent) override;
    QWidget *createAttributeEditor(QtDatePropertyManager *manager, QtProperty *property,
                                   QWidget *parent, BrowserCol attribute) override;
    void disconnectPropertyManager(QtDatePropertyManager *manager) override;
private:
    QScopedPointer<QtDateEditFactoryPrivate> d_ptr;
    Q_DECLARE_PRIVATE(QtDateEditFactory)
    Q_DISABLE_COPY_MOVE(QtDateEditFactory)
    Q_PRIVATE_SLOT(d_func(), void slotPropertyChanged(QtProperty *, QDate))
    Q_PRIVATE_SLOT(d_func(), void slotRangeChanged(QtProperty *, QDate, QDate))
    Q_PRIVATE_SLOT(d_func(), void slotSetValue(QDate))
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
};

class QtTimeEditFactoryPrivate;

class QtTimeEditFactory : public QtAbstractEditorFactory<QtTimePropertyManager>
{
    Q_OBJECT
public:
    QtTimeEditFactory(QObject *parent = 0);
    ~QtTimeEditFactory();
protected:
    void connectPropertyManager(QtTimePropertyManager *manager) override;
    QWidget *createEditor(QtTimePropertyManager *manager, QtProperty *property,
                QWidget *parent) override;
    QWidget *createAttributeEditor(QtTimePropertyManager *manager, QtProperty *property,
                                   QWidget *parent, BrowserCol attribute) override;
    void disconnectPropertyManager(QtTimePropertyManager *manager) override;
private:
    QScopedPointer<QtTimeEditFactoryPrivate> d_ptr;
    Q_DECLARE_PRIVATE(QtTimeEditFactory)
    Q_DISABLE_COPY_MOVE(QtTimeEditFactory)
    Q_PRIVATE_SLOT(d_func(), void slotPropertyChanged(QtProperty *, QTime))
    Q_PRIVATE_SLOT(d_func(), void slotSetValue(QTime))
    Q_PRIVATE_SLOT(d_func(), void slotEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
};

class QtDateTimeEditFactoryPrivate;

class QtDateTimeEditFactory : public QtAbstractEditorFactory<QtDateTimePropertyManager>
{
    Q_OBJECT
public:
    QtDateTimeEditFactory(QObject *parent = 0);
    ~QtDateTimeEditFactory();
protected:
    void connectPropertyManager(QtDateTimePropertyManager *manager) override;
    QWidget *createEditor(QtDateTimePropertyManager *manager, QtProperty *property,
                QWidget *parent) override;
    QWidget *createAttributeEditor(QtDateTimePropertyManager *manager, QtProperty *property,
                                   QWidget *parent, BrowserCol attribute) override;
    void disconnectPropertyManager(QtDateTimePropertyManager *manager) override;
private:
    QScopedPointer<QtDateTimeEditFactoryPrivate> d_ptr;
    Q_DECLARE_PRIVATE(QtDateTimeEditFactory)
    Q_DISABLE_COPY_MOVE(QtDateTimeEditFactory)
    Q_PRIVATE_SLOT(d_func(), void slotPropertyChanged(QtProperty *, const QDateTime &))
    Q_PRIVATE_SLOT(d_func(), void slotSetValue(const QDateTime &))
    Q_PRIVATE_SLOT(d_func(), void slotEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
};

class QtKeySequenceEditorFactoryPrivate;

class QtKeySequenceEditorFactory : public QtAbstractEditorFactory<QtKeySequencePropertyManager>
{
    Q_OBJECT
public:
    QtKeySequenceEditorFactory(QObject *parent = 0);
    ~QtKeySequenceEditorFactory();
protected:
    void connectPropertyManager(QtKeySequencePropertyManager *manager) override;
    QWidget *createEditor(QtKeySequencePropertyManager *manager, QtProperty *property,
                QWidget *parent) override;
    QWidget *createAttributeEditor(QtKeySequencePropertyManager *manager, QtProperty *property,
                                   QWidget *parent, BrowserCol attribute) override;
    void disconnectPropertyManager(QtKeySequencePropertyManager *manager) override;
private:
    QScopedPointer<QtKeySequenceEditorFactoryPrivate> d_ptr;
    Q_DECLARE_PRIVATE(QtKeySequenceEditorFactory)
    Q_DISABLE_COPY_MOVE(QtKeySequenceEditorFactory)
    Q_PRIVATE_SLOT(d_func(), void slotPropertyChanged(QtProperty *, const QKeySequence &))
    Q_PRIVATE_SLOT(d_func(), void slotSetValue(const QKeySequence &))
    Q_PRIVATE_SLOT(d_func(), void slotEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
};

class QtCharEditorFactoryPrivate;

class QtCharEditorFactory : public QtAbstractEditorFactory<QtCharPropertyManager>
{
    Q_OBJECT
public:
    QtCharEditorFactory(QObject *parent = 0);
    ~QtCharEditorFactory();
protected:
    void connectPropertyManager(QtCharPropertyManager *manager) override;
    QWidget *createEditor(QtCharPropertyManager *manager, QtProperty *property,
                QWidget *parent) override;
    QWidget *createAttributeEditor(QtCharPropertyManager *manager, QtProperty *property,
                                   QWidget *parent, BrowserCol attribute) override;
    void disconnectPropertyManager(QtCharPropertyManager *manager) override;
private:
    QScopedPointer<QtCharEditorFactoryPrivate> d_ptr;
    Q_DECLARE_PRIVATE(QtCharEditorFactory)
    Q_DISABLE_COPY_MOVE(QtCharEditorFactory)
    Q_PRIVATE_SLOT(d_func(), void slotPropertyChanged(QtProperty *, const QChar &))
    Q_PRIVATE_SLOT(d_func(), void slotSetValue(const QChar &))
    Q_PRIVATE_SLOT(d_func(), void slotEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
};

class QtEnumEditorFactoryPrivate;

class QtEnumEditorFactory : public QtAbstractEditorFactory<QtEnumPropertyManager>
{
    Q_OBJECT
public:
    QtEnumEditorFactory(QObject *parent = 0);
    ~QtEnumEditorFactory();
protected:
    void connectPropertyManager(QtEnumPropertyManager *manager) override;
    QWidget *createEditor(QtEnumPropertyManager *manager, QtProperty *property,
                QWidget *parent) override;
    QWidget *createAttributeEditor(QtEnumPropertyManager *manager, QtProperty *property,
                                   QWidget *parent, BrowserCol attribute) override;
    void disconnectPropertyManager(QtEnumPropertyManager *manager) override;
private:
    QScopedPointer<QtEnumEditorFactoryPrivate> d_ptr;
    Q_DECLARE_PRIVATE(QtEnumEditorFactory)
    Q_DISABLE_COPY_MOVE(QtEnumEditorFactory)
    Q_PRIVATE_SLOT(d_func(), void slotPropertyChanged(QtProperty *, int))
    Q_PRIVATE_SLOT(d_func(), void slotEnumNamesChanged(QtProperty *,
                        const QStringList &))
    Q_PRIVATE_SLOT(d_func(), void slotEnumIconsChanged(QtProperty *,
                        const QMap<int, QIcon> &))
    Q_PRIVATE_SLOT(d_func(), void slotSetValue(int))
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
};

class QtFlagEditorFactoryPrivate;

class QtFlagEditorFactory : public QtAbstractEditorFactory<QtFlagPropertyManager>
{
Q_OBJECT
public:
    QtFlagEditorFactory(QObject *parent = 0);
    ~QtFlagEditorFactory();
protected:
    void connectPropertyManager(QtFlagPropertyManager *manager) override;
    QWidget *createEditor(QtFlagPropertyManager *manager, QtProperty *property,
                          QWidget *parent) override;
    QWidget *createAttributeEditor(QtFlagPropertyManager *manager, QtProperty *property,
                                   QWidget *parent, BrowserCol attribute) override;
    void disconnectPropertyManager(QtFlagPropertyManager *manager) override;
private:
    QScopedPointer<QtFlagEditorFactoryPrivate> d_ptr;
    Q_DECLARE_PRIVATE(QtFlagEditorFactory)
    Q_DISABLE_COPY_MOVE(QtFlagEditorFactory)
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
};

class QtLocaleEditorFactoryPrivate;

class QtLocaleEditorFactory : public QtAbstractEditorFactory<QtLocalePropertyManager>
{
    Q_OBJECT
public:
    QtLocaleEditorFactory(QObject *parent = 0);
    ~QtLocaleEditorFactory();
protected:
    void connectPropertyManager(QtLocalePropertyManager *manager) override;
    QWidget *createEditor(QtLocalePropertyManager *manager, QtProperty *property,
                          QWidget *parent) override;
    QWidget *createAttributeEditor(QtLocalePropertyManager *manager, QtProperty *property,
                                   QWidget *parent, BrowserCol attribute) override;
    void disconnectPropertyManager(QtLocalePropertyManager *manager) override;
private:
    QScopedPointer<QtLocaleEditorFactoryPrivate> d_ptr;
    Q_DECLARE_PRIVATE(QtLocaleEditorFactory)
    Q_DISABLE_COPY_MOVE(QtLocaleEditorFactory)
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
};

class QtPointEditorFactoryPrivate;

class QtPointEditorFactory : public QtAbstractEditorFactory<QtPointPropertyManager>
{
    Q_OBJECT
public:
    QtPointEditorFactory(QObject *parent = 0);
    ~QtPointEditorFactory();
protected:
    void connectPropertyManager(QtPointPropertyManager *manager) override;
    QWidget *createEditor(QtPointPropertyManager *manager, QtProperty *property,
                          QWidget *parent) override;
    QWidget *createAttributeEditor(QtPointPropertyManager *manager, QtProperty *property,
                                   QWidget *parent, BrowserCol attribute) override;
    void disconnectPropertyManager(QtPointPropertyManager *manager) override;
private:
    QScopedPointer<QtPointEditorFactoryPrivate> d_ptr;
    Q_DECLARE_PRIVATE(QtPointEditorFactory)
    Q_DISABLE_COPY_MOVE(QtPointEditorFactory)
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
};

class QtPointFEditorFactoryPrivate;

class QtPointFEditorFactory : public QtAbstractEditorFactory<QtPointFPropertyManager>
{
    Q_OBJECT
public:
    QtPointFEditorFactory(QObject *parent = 0);
    ~QtPointFEditorFactory();
protected:
    void connectPropertyManager(QtPointFPropertyManager *manager) override;
    QWidget *createEditor(QtPointFPropertyManager *manager, QtProperty *property,
                          QWidget *parent) override;
    QWidget *createAttributeEditor(QtPointFPropertyManager *manager, QtProperty *property,
                                   QWidget *parent, BrowserCol attribute) override;
    void disconnectPropertyManager(QtPointFPropertyManager *manager) override;
private:
    QScopedPointer<QtPointFEditorFactoryPrivate> d_ptr;
    Q_DECLARE_PRIVATE(QtPointFEditorFactory)
    Q_DISABLE_COPY_MOVE(QtPointFEditorFactory)
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
};

class QtSizeEditorFactoryPrivate;

class QtSizeEditorFactory : public QtAbstractEditorFactory<QtSizePropertyManager>
{
    Q_OBJECT
public:
    QtSizeEditorFactory(QObject *parent = 0);
    ~QtSizeEditorFactory();
protected:
    void connectPropertyManager(QtSizePropertyManager *manager) override;
    QWidget *createEditor(QtSizePropertyManager *manager, QtProperty *property,
                          QWidget *parent) override;
    QWidget *createAttributeEditor(QtSizePropertyManager *manager, QtProperty *property,
                                   QWidget *parent, BrowserCol attribute) override;
    void disconnectPropertyManager(QtSizePropertyManager *manager) override;
private:
    QScopedPointer<QtSizeEditorFactoryPrivate> d_ptr;
    Q_DECLARE_PRIVATE(QtSizeEditorFactory)
    Q_DISABLE_COPY_MOVE(QtSizeEditorFactory)
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
};

class QtSizeFEditorFactoryPrivate;

class QtSizeFEditorFactory : public QtAbstractEditorFactory<QtSizeFPropertyManager>
{
    Q_OBJECT
public:
    QtSizeFEditorFactory(QObject *parent = 0);
    ~QtSizeFEditorFactory();
protected:
    void connectPropertyManager(QtSizeFPropertyManager *manager) override;
    QWidget *createEditor(QtSizeFPropertyManager *manager, QtProperty *property,
                          QWidget *parent) override;
    QWidget *createAttributeEditor(QtSizeFPropertyManager *manager, QtProperty *property,
                                   QWidget *parent, BrowserCol attribute) override;
    void disconnectPropertyManager(QtSizeFPropertyManager *manager) override;
private:
    QScopedPointer<QtSizeFEditorFactoryPrivate> d_ptr;
    Q_DECLARE_PRIVATE(QtSizeFEditorFactory)
    Q_DISABLE_COPY_MOVE(QtSizeFEditorFactory)
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
};

class QtRectEditorFactoryPrivate;

class QtRectEditorFactory : public QtAbstractEditorFactory<QtRectPropertyManager>
{
    Q_OBJECT
public:
    QtRectEditorFactory(QObject *parent = 0);
    ~QtRectEditorFactory();
protected:
    void connectPropertyManager(QtRectPropertyManager *manager) override;
    QWidget *createEditor(QtRectPropertyManager *manager, QtProperty *property,
                          QWidget *parent) override;
    QWidget *createAttributeEditor(QtRectPropertyManager *manager, QtProperty *property,
                                   QWidget *parent, BrowserCol attribute) override;
    void disconnectPropertyManager(QtRectPropertyManager *manager) override;
private:
    QScopedPointer<QtRectEditorFactoryPrivate> d_ptr;
    Q_DECLARE_PRIVATE(QtRectEditorFactory)
    Q_DISABLE_COPY_MOVE(QtRectEditorFactory)
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
};

class QtRectFEditorFactoryPrivate;

class QtRectFEditorFactory : public QtAbstractEditorFactory<QtRectFPropertyManager>
{
    Q_OBJECT
public:
    QtRectFEditorFactory(QObject *parent = 0);
    ~QtRectFEditorFactory();
protected:
    void connectPropertyManager(QtRectFPropertyManager *manager) override;
    QWidget *createEditor(QtRectFPropertyManager *manager, QtProperty *property,
                          QWidget *parent) override;
    QWidget *createAttributeEditor(QtRectFPropertyManager *manager, QtProperty *property,
                                   QWidget *parent, BrowserCol attribute) override;
    void disconnectPropertyManager(QtRectFPropertyManager *manager) override;
private:
    QScopedPointer<QtRectFEditorFactoryPrivate> d_ptr;
    Q_DECLARE_PRIVATE(QtRectFEditorFactory)
    Q_DISABLE_COPY_MOVE(QtRectFEditorFactory)
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
};

class QtSizePolicyEditorFactoryPrivate;

class QtSizePolicyEditorFactory : public QtAbstractEditorFactory<QtSizePolicyPropertyManager>
{
    Q_OBJECT
public:
    QtSizePolicyEditorFactory(QObject *parent = 0);
    ~QtSizePolicyEditorFactory();
protected:
    void connectPropertyManager(QtSizePolicyPropertyManager *manager) override;
    QWidget *createEditor(QtSizePolicyPropertyManager *manager, QtProperty *property,
                          QWidget *parent) override;
    QWidget *createAttributeEditor(QtSizePolicyPropertyManager *manager, QtProperty *property,
                                   QWidget *parent, BrowserCol attribute) override;
    void disconnectPropertyManager(QtSizePolicyPropertyManager *manager) override;
private:
    QScopedPointer<QtSizePolicyEditorFactoryPrivate> d_ptr;
    Q_DECLARE_PRIVATE(QtSizePolicyEditorFactory)
    Q_DISABLE_COPY_MOVE(QtSizePolicyEditorFactory)
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
};

class QtCursorEditorFactoryPrivate;

class QtCursorEditorFactory : public QtAbstractEditorFactory<QtCursorPropertyManager>
{
    Q_OBJECT
public:
    QtCursorEditorFactory(QObject *parent = 0);
    ~QtCursorEditorFactory();
protected:
    void connectPropertyManager(QtCursorPropertyManager *manager) override;
    QWidget *createEditor(QtCursorPropertyManager *manager, QtProperty *property,
                QWidget *parent) override;
    QWidget *createAttributeEditor(QtCursorPropertyManager *manager, QtProperty *property,
                                   QWidget *parent, BrowserCol attribute) override;
    void disconnectPropertyManager(QtCursorPropertyManager *manager) override;
private:
    QScopedPointer<QtCursorEditorFactoryPrivate> d_ptr;
    Q_DECLARE_PRIVATE(QtCursorEditorFactory)
    Q_DISABLE_COPY_MOVE(QtCursorEditorFactory)
    Q_PRIVATE_SLOT(d_func(), void slotPropertyChanged(QtProperty *, const QCursor &))
    Q_PRIVATE_SLOT(d_func(), void slotEnumChanged(QtProperty *, int))
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
};

class QtColorEditorFactoryPrivate;

class QtColorEditorFactory : public QtAbstractEditorFactory<QtColorPropertyManager>
{
    Q_OBJECT
public:
    QtColorEditorFactory(QObject *parent = 0);
    ~QtColorEditorFactory();
protected:
    void connectPropertyManager(QtColorPropertyManager *manager) override;
    QWidget *createEditor(QtColorPropertyManager *manager, QtProperty *property,
                QWidget *parent) override;
    QWidget *createAttributeEditor(QtColorPropertyManager *manager, QtProperty *property,
                                   QWidget *parent, BrowserCol attribute) override;
    void disconnectPropertyManager(QtColorPropertyManager *manager) override;
private:
    QScopedPointer<QtColorEditorFactoryPrivate> d_ptr;
    Q_DECLARE_PRIVATE(QtColorEditorFactory)
    Q_DISABLE_COPY_MOVE(QtColorEditorFactory)
    Q_PRIVATE_SLOT(d_func(), void slotPropertyChanged(QtProperty *, const QColor &))
    Q_PRIVATE_SLOT(d_func(), void slotEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotSetValue(const QColor &))
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
};

class QtFontEditorFactoryPrivate;

class QtFontEditorFactory : public QtAbstractEditorFactory<QtFontPropertyManager>
{
    Q_OBJECT
public:
    QtFontEditorFactory(QObject *parent = 0);
    ~QtFontEditorFactory();
protected:
    void connectPropertyManager(QtFontPropertyManager *manager) override;
    QWidget *createEditor(QtFontPropertyManager *manager, QtProperty *property,
                QWidget *parent) override;
    QWidget *createAttributeEditor(QtFontPropertyManager *manager, QtProperty *property,
                                   QWidget *parent, BrowserCol attribute) override;
    void disconnectPropertyManager(QtFontPropertyManager *manager) override;
private:
    QScopedPointer<QtFontEditorFactoryPrivate> d_ptr;
    Q_DECLARE_PRIVATE(QtFontEditorFactory)
    Q_DISABLE_COPY_MOVE(QtFontEditorFactory)
    Q_PRIVATE_SLOT(d_func(), void slotPropertyChanged(QtProperty *, const QFont &))
    Q_PRIVATE_SLOT(d_func(), void slotEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotSetValue(const QFont &))
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
};

class QtFileEditorFactoryPrivate;

class QtFileEditorFactory: public QtAbstractEditorFactory<QtFilePropertyManager>
{
    Q_OBJECT
public:
    QtFileEditorFactory(QObject *parent = 0);
    ~QtFileEditorFactory();
protected:
    void connectPropertyManager(QtFilePropertyManager *manager) override;
    QWidget *createEditor(QtFilePropertyManager *manager, QtProperty *property,
                          QWidget *parent) override;
    QWidget *createAttributeEditor(QtFilePropertyManager *manager, QtProperty *property,
                                   QWidget *parent, BrowserCol attribute) override;
    void disconnectPropertyManager(QtFilePropertyManager *manager) override;
private:
    QScopedPointer<QtFileEditorFactoryPrivate> d_ptr;
    Q_DECLARE_PRIVATE(QtFileEditorFactory)
    Q_DISABLE_COPY_MOVE(QtFileEditorFactory)
    Q_PRIVATE_SLOT(d_func(), void slotPropertyChanged(QtProperty *, const QString &))
    Q_PRIVATE_SLOT(d_func(), void slotFilterChanged(QtProperty *, const QString &))
    Q_PRIVATE_SLOT(d_func(), void slotReadOnlyChanged(QtProperty *, bool))
    Q_PRIVATE_SLOT(d_func(), void slotEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotSetValue(const QString &))
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
};

QT_END_NAMESPACE

#endif
