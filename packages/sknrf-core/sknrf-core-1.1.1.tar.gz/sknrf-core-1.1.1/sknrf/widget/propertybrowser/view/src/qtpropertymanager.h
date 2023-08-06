// Copyright (C) 2016 The Qt Company Ltd.
// SPDX-License-Identifier: LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only

#ifndef QTPROPERTYMANAGER_H
#define QTPROPERTYMANAGER_H

#include <QtWidgets/QLineEdit>
#include <QtWidgets/QFileDialog>

#include "qtpropertybrowser.h"

QT_BEGIN_NAMESPACE

class QDate;
class QTime;
class QDateTime;
class QLocale;
class QRegularExpression;

class QtGroupPropertyManagerPrivate;

class QtGroupPropertyManager : public QtAbstractPropertyManager
{
    Q_OBJECT
public:
    QtGroupPropertyManager(QObject *parent = 0);
    ~QtGroupPropertyManager();

    bool check(const QtProperty *property) const override;

public Q_SLOTS:
    void setCheck(QtProperty *property, bool check) override;

Q_SIGNALS:
    void checkChanged(QtProperty *property, bool check);

protected:
    bool hasValue(const QtProperty *property) const override;

    void initializeProperty(QtProperty *property) override;
    void uninitializeProperty(QtProperty *property) override;

private:
    QScopedPointer<QtGroupPropertyManagerPrivate> d_ptr;
    Q_DECLARE_PRIVATE(QtGroupPropertyManager)
    Q_DISABLE_COPY_MOVE(QtGroupPropertyManager)
};

class QtIntPropertyManagerPrivate;

class QtIntPropertyManager : public QtAbstractPropertyManager
{
    Q_OBJECT
public:
    QtIntPropertyManager(QObject *parent = 0);
    ~QtIntPropertyManager();

    int value(const QtProperty *property) const;
    int minimum(const QtProperty *property) const;
    int maximum(const QtProperty *property) const;
    int singleStep(const QtProperty *property) const;
    int decimals(const QtProperty *property) const;
    int precision(const QtProperty *property) const;
    QString unit(const QtProperty *property) const;
    bool check(const QtProperty *property) const override;
    bool isReadOnly(const QtProperty *property) const override;
    QBrush foreground(const QtProperty *property) const override;

public Q_SLOTS:
    void setValue(QtProperty *property, int val);
    void setMinimum(QtProperty *property, int minVal);
    void setMaximum(QtProperty *property, int maxVal);
    void setRange(QtProperty *property, int minVal, int maxVal);
    void setSingleStep(QtProperty *property, int step);
    void setPrecision(QtProperty *property, int prec);
    void setUnit(QtProperty *property, const QString& unit);
    void setCheck(QtProperty *property, bool check) override;
    void setReadOnly(QtProperty *property, bool readOnly);
Q_SIGNALS:
    void valueChanged(QtProperty *property, int val);
    void rangeChanged(QtProperty *property, int minVal, int maxVal);
    void singleStepChanged(QtProperty *property, int step);
    void precisionChanged(QtProperty *property, int prec);
    void unitChanged(QtProperty *property, const QString& unit);
    void checkChanged(QtProperty *property, bool check);
    void readOnlyChanged(QtProperty *property, bool readOnly);
protected:
    QString valueText(const QtProperty *property) const override;
    QString minimumText(const QtProperty *property) const override;
    QString maximumText(const QtProperty *property) const override;
    QString unitText(const QtProperty *property) const override;
    void initializeProperty(QtProperty *property) override;
    void uninitializeProperty(QtProperty *property) override;
private:
    QScopedPointer<QtIntPropertyManagerPrivate> d_ptr;
    Q_DECLARE_PRIVATE(QtIntPropertyManager)
    Q_DISABLE_COPY_MOVE(QtIntPropertyManager)
};

class QtBoolPropertyManagerPrivate;

class QtBoolPropertyManager : public QtAbstractPropertyManager
{
    Q_OBJECT
public:
    QtBoolPropertyManager(QObject *parent = 0);
    ~QtBoolPropertyManager();

    bool value(const QtProperty *property) const;
    bool check(const QtProperty *property) const override;

public Q_SLOTS:
    void setValue(QtProperty *property, bool val);
    void setCheck(QtProperty *property, bool check) override;
Q_SIGNALS:
    void valueChanged(QtProperty *property, bool val);
    void checkChanged(QtProperty *property, bool check);
protected:
    QString valueText(const QtProperty *property) const override;
    QIcon valueIcon(const QtProperty *property) const override;
    void initializeProperty(QtProperty *property) override;
    void uninitializeProperty(QtProperty *property) override;
private:
    QScopedPointer<QtBoolPropertyManagerPrivate> d_ptr;
    Q_DECLARE_PRIVATE(QtBoolPropertyManager)
    Q_DISABLE_COPY_MOVE(QtBoolPropertyManager)
};

class QtDoublePropertyManagerPrivate;

class QtDoublePropertyManager : public QtAbstractPropertyManager
{
    Q_OBJECT
public:
    QtDoublePropertyManager(QObject *parent = 0);
    ~QtDoublePropertyManager();

    double value(const QtProperty *property) const;
    double atol(const QtProperty *property) const;
    double rtol(const QtProperty *property) const;
    double minimum(const QtProperty *property) const;
    double maximum(const QtProperty *property) const;
    double singleStep(const QtProperty *property) const;
    int decimals(const QtProperty *property) const;
    int precision(const QtProperty *property) const;
    Scale scale(const QtProperty *property) const;
    QString unit(const QtProperty *property) const;
    Format format(const QtProperty *property) const;
    bool check(const QtProperty *property) const override;
    bool isReadOnly(const QtProperty *property) const override;
    QBrush foreground(const QtProperty *property) const override;

public Q_SLOTS:
    void setValue(QtProperty *property, double val);
    void setMinimum(QtProperty *property, double minVal);
    void setMaximum(QtProperty *property, double maxVal);
    void setRange(QtProperty *property, double minVal, double maxVal);
    void setSingleStep(QtProperty *property, double step);
    void setPrecision(QtProperty *property, int prec);
    void setScale(QtProperty *property, Scale scale_);
    void setUnit(QtProperty *property, const QString& unit);
    void setFormat(QtProperty *property, Format format_);
    void setCheck(QtProperty *property, bool check) override;
    void setReadOnly(QtProperty *property, bool readOnly);
Q_SIGNALS:
    void valueChanged(QtProperty *property, double val);
    void rangeChanged(QtProperty *property, double minVal, double maxVal);
    void singleStepChanged(QtProperty *property, double step);
    void precisionChanged(QtProperty *property, int prec);
    void scaleChanged(QtProperty *property, Scale scale);
    void unitChanged(QtProperty *property, const QString& unit);
    void formatChanged(QtProperty *property, Format format_);
    void checkChanged(QtProperty *property, bool check);
    void readOnlyChanged(QtProperty *property, bool readOnly);
protected:
    QString valueText(const QtProperty *property) const override;
    QString minimumText(const QtProperty *property) const override;
    QString maximumText(const QtProperty *property) const override;
    QString unitText(const QtProperty *property) const override;
    QString formatText(const QtProperty *property) const override;
    void initializeProperty(QtProperty *property) override;
    void uninitializeProperty(QtProperty *property) override;
private:
    QScopedPointer<QtDoublePropertyManagerPrivate> d_ptr;
    Q_DECLARE_PRIVATE(QtDoublePropertyManager)
    Q_DISABLE_COPY_MOVE(QtDoublePropertyManager)
};

class QtComplexPropertyManagerPrivate;

class QtComplexPropertyManager : public QtAbstractPropertyManager
{
    Q_OBJECT
public:
    QtComplexPropertyManager(QObject *parent = 0);
    ~QtComplexPropertyManager();

    QtComplex value(const QtProperty *property) const;
    QtComplex atol(const QtProperty *property) const;
    QtComplex rtol(const QtProperty *property) const;
    QtComplex minimum(const QtProperty *property) const;
    QtComplex maximum(const QtProperty *property) const;
    QtComplex singleStep(const QtProperty *property) const;
    int decimals(const QtProperty *property) const;
    int precision(const QtProperty *property) const;
    Scale scale(const QtProperty *property) const;
    QString unit(const QtProperty *property) const;
    PkAvg pkAvg(const QtProperty *property) const;
    Format format(const QtProperty *property) const;
    bool check(const QtProperty *property) const override;
    bool isReadOnly(const QtProperty *property) const override;
    QBrush foreground(const QtProperty *property) const override;


public Q_SLOTS:
    void setValue(QtProperty *property, const QtComplex& val);
    void setMinimum(QtProperty *property, const QtComplex& minVal);
    void setMaximum(QtProperty *property, const QtComplex& maxVal);
    void setRange(QtProperty *property, const QtComplex& minVal, const QtComplex& maxVal);
    void setSingleStep(QtProperty *property, const QtComplex& step);
    void setPrecision(QtProperty *property, int prec);
    void setScale(QtProperty *property, Scale scale_);
    void setUnit(QtProperty *property, const QString& unit);
    void setPkAvg(QtProperty *property,PkAvg pkAvg);
    void setFormat(QtProperty *property,Format format_);
    void setCheck(QtProperty *property, bool check) override;
    void setReadOnly(QtProperty *property, bool readOnly);
Q_SIGNALS:
    void valueChanged(QtProperty *property, const QtComplex& val);
    void rangeChanged(QtProperty *property, const QtComplex& minVal, const QtComplex& maxVal);
    void singleStepChanged(QtProperty *property, const QtComplex& step);
    void precisionChanged(QtProperty *property, int prec);
    void scaleChanged(QtProperty *property, Scale scale);
    void unitChanged(QtProperty *property, const QString& unit);
    void pkAvgChanged(QtProperty *property,PkAvg pkAvg);
    void formatChanged(QtProperty *property,Format format_);
    void checkChanged(QtProperty *property, bool check);
    void readOnlyChanged(QtProperty *property, bool readOnly);
protected:
    QString valueText(const QtProperty *property) const override;
    QString minimumText(const QtProperty *property) const override;
    QString maximumText(const QtProperty *property) const override;
    QString unitText(const QtProperty *property) const override;
    QString pkAvgText(const QtProperty *property) const override;
    QString formatText(const QtProperty *property) const override;
    void initializeProperty(QtProperty *property) override;
    void uninitializeProperty(QtProperty *property) override;
private:
    QScopedPointer<QtComplexPropertyManagerPrivate> d_ptr;
    Q_DECLARE_PRIVATE(QtComplexPropertyManager)
    Q_DISABLE_COPY_MOVE(QtComplexPropertyManager)
};

class QtQuaternionPropertyManagerPrivate;

class QtQuaternionPropertyManager : public QtAbstractPropertyManager
{
Q_OBJECT
public:
    QtQuaternionPropertyManager(QObject *parent = 0);
    ~QtQuaternionPropertyManager();

    QtQuaternion value(const QtProperty *property) const;
    QtQuaternion atol(const QtProperty *property) const;
    QtQuaternion rtol(const QtProperty *property) const;
    QtQuaternion minimum(const QtProperty *property) const;
    QtQuaternion maximum(const QtProperty *property) const;
    QtQuaternion singleStep(const QtProperty *property) const;
    int decimals(const QtProperty *property) const;
    int precision(const QtProperty *property) const;
    Scale scale(const QtProperty *property) const;
    QString unit(const QtProperty *property) const;
    PkAvg pkAvg(const QtProperty *property) const;
    Format format(const QtProperty *property) const;
    bool polarized(const QtProperty *property) const;
    bool check(const QtProperty *property) const override;
    bool isReadOnly(const QtProperty *property) const override;
    QBrush foreground(const QtProperty *property) const override;


public Q_SLOTS:
    void setValue(QtProperty *property, const QtQuaternion& val);
    void setMinimum(QtProperty *property, const QtQuaternion& minVal);
    void setMaximum(QtProperty *property, const QtQuaternion& maxVal);
    void setRange(QtProperty *property, const QtQuaternion& minVal, const QtQuaternion& maxVal);
    void setSingleStep(QtProperty *property, const QtQuaternion& step);
    void setPrecision(QtProperty *property, int prec);
    void setScale(QtProperty *property, Scale scale_);
    void setUnit(QtProperty *property, const QString& unit);
    void setPkAvg(QtProperty *property,PkAvg pkAvg);
    void setFormat(QtProperty *property,Format format_);
    void setPolarized(QtProperty *property, bool polarized);
    void setCheck(QtProperty *property, bool check) override;
    void setReadOnly(QtProperty *property, bool readOnly);
Q_SIGNALS:
    void valueChanged(QtProperty *property, const QtQuaternion& val);
    void rangeChanged(QtProperty *property, const QtQuaternion& minVal, const QtQuaternion& maxVal);
    void singleStepChanged(QtProperty *property, const QtQuaternion& step);
    void precisionChanged(QtProperty *property, int prec);
    void scaleChanged(QtProperty *property, Scale scale);
    void unitChanged(QtProperty *property, const QString& unit);
    void pkAvgChanged(QtProperty *property,PkAvg pkAvg);
    void formatChanged(QtProperty *property,Format format_);
    void polarizedChanged(QtProperty *property, bool polarized);
    void checkChanged(QtProperty *property, bool check);
    void readOnlyChanged(QtProperty *property, bool readOnly);
protected:
    QString valueText(const QtProperty *property) const override;
    QString minimumText(const QtProperty *property) const override;
    QString maximumText(const QtProperty *property) const override;
    QString unitText(const QtProperty *property) const override;
    QString pkAvgText(const QtProperty *property) const override;
    QString formatText(const QtProperty *property) const override;
    void initializeProperty(QtProperty *property) override;
    void uninitializeProperty(QtProperty *property) override;
private:
    QScopedPointer<QtQuaternionPropertyManagerPrivate> d_ptr;
    Q_DECLARE_PRIVATE(QtQuaternionPropertyManager)
    Q_DISABLE_COPY_MOVE(QtQuaternionPropertyManager)
};

class QtVectorComplexPropertyManagerPrivate;

class QtVectorComplexPropertyManager : public QtAbstractPropertyManager
{
    Q_OBJECT
public:
    QtVectorComplexPropertyManager(QObject *parent = 0);
    ~QtVectorComplexPropertyManager();
    void connect_signals() const;
    void disconnect_signals() const;

    QtComplexPropertyManager *subComplexPropertyManager() const;

    QVector<QtComplex> value(const QtProperty *property) const;

    QVector<QtComplex> atol(const QtProperty *property) const;
    QVector<QtComplex> rtol(const QtProperty *property) const;
    QVector<QtComplex> minimum(const QtProperty *property) const;
    QVector<QtComplex> maximum(const QtProperty *property) const;
    QVector<QtComplex> singleStep(const QtProperty *property) const;
    int size(const QtProperty *property) const;
    QVector<int> decimals(const QtProperty *property) const;
    int precision(const QtProperty *property) const;
    Scale scale(const QtProperty *property) const;
    QString unit(const QtProperty *property) const;
    PkAvg pkAvg(const QtProperty *property) const;
    Format format(const QtProperty *property) const;
    bool check(const QtProperty *property) const override;
    bool isReadOnly(const QtProperty *property) const override;
    QBrush foreground(const QtProperty *property) const override;

public Q_SLOTS:
    void setValue(QtProperty *property, const QVector<QtComplex>& val);
    void setMinimum(QtProperty *property, const QVector<QtComplex>& minVal);
    void setMaximum(QtProperty *property, const QVector<QtComplex>& maxVal);
    void setRange(QtProperty *property, const QVector<QtComplex>& minVal, const QVector<QtComplex>& maxVal);
    void setSingleStep(QtProperty *property, const QVector<QtComplex>& step);
    void setSize(QtProperty * property, int size);
    void setPrecision(QtProperty *property, int prec);
    void setScale(QtProperty *property, Scale scale_);
    void setUnit(QtProperty *property, QString unit);
    void setPkAvg(QtProperty *property,PkAvg pkAvg);
    void setFormat(QtProperty *property,Format format_);
    void setCheck(QtProperty *property, bool check) override;
    void setReadOnly(QtProperty *property, bool readOnly);
Q_SIGNALS:
    void valueChanged(QtProperty *property, const QVector<QtComplex>& val);
    void sizeChanged(QtProperty *property, int size);
    void precisionChanged(QtProperty *property, int prec);
    void rangeChanged(QtProperty *property, const QVector<QtComplex>& minVal, const QVector<QtComplex>& maxVal);
    void singleStepChanged(QtProperty *property, const QVector<QtComplex>& step);
    void scaleChanged(QtProperty *property, Scale scale);
    void unitChanged(QtProperty *property, const QString& unit);
    void pkAvgChanged(QtProperty *property,PkAvg pkAvg);
    void formatChanged(QtProperty *property,Format format_);
    void checkChanged(QtProperty *property, bool check);
    void readOnlyChanged(QtProperty *property, bool readOnly);
protected:
    QString valueText(const QtProperty *property) const override;
    QString unitText(const QtProperty *property) const override;
    QString pkAvgText(const QtProperty *property) const override;
    QString formatText(const QtProperty *property) const override;

    void initializeProperty(QtProperty *property) override;
    virtual void reinitializeProperty(QtProperty *property);
    void uninitializeProperty(QtProperty *property) override;
private:
    QScopedPointer<QtVectorComplexPropertyManagerPrivate> d_ptr;
    Q_DECLARE_PRIVATE(QtVectorComplexPropertyManager)
    Q_DISABLE_COPY_MOVE(QtVectorComplexPropertyManager)
    Q_PRIVATE_SLOT(d_func(), void slotComplexChanged(QtProperty *, const QtComplex&))
    Q_PRIVATE_SLOT(d_func(), void slotRangeChanged(QtProperty *, const QtComplex&, const QtComplex&))
    Q_PRIVATE_SLOT(d_func(), void slotPropertyDestroyed(QtProperty *))
};

class QtStringPropertyManagerPrivate;

class QtStringPropertyManager : public QtAbstractPropertyManager
{
    Q_OBJECT
public:
    QtStringPropertyManager(QObject *parent = 0);
    ~QtStringPropertyManager();

    QString value(const QtProperty *property) const;
    QRegularExpression regExp(const QtProperty *property) const;
    bool check(const QtProperty *property) const override;
    bool isReadOnly(const QtProperty *property) const override;

public Q_SLOTS:
    void setValue(QtProperty *property, const QString &val);
    void setRegExp(QtProperty *property, const QRegularExpression &regExp);
    void setCheck(QtProperty *property, bool check) override;
    void setReadOnly(QtProperty *property, bool readOnly);

Q_SIGNALS:
    void valueChanged(QtProperty *property, const QString &val);
    void regExpChanged(QtProperty *property, const QRegularExpression &regExp);
    void checkChanged(QtProperty *property, bool check);
    void readOnlyChanged(QtProperty *property, bool);

protected:
    QString valueText(const QtProperty *property) const override;
    QString displayText(const QtProperty *property) const override;
    void initializeProperty(QtProperty *property) override;
    void uninitializeProperty(QtProperty *property) override;
private:
    QScopedPointer<QtStringPropertyManagerPrivate> d_ptr;
    Q_DECLARE_PRIVATE(QtStringPropertyManager)
    Q_DISABLE_COPY_MOVE(QtStringPropertyManager)
};

class QtDatePropertyManagerPrivate;

class QtDatePropertyManager : public QtAbstractPropertyManager
{
    Q_OBJECT
public:
    QtDatePropertyManager(QObject *parent = 0);
    ~QtDatePropertyManager();

    QDate value(const QtProperty *property) const;
    QDate minimum(const QtProperty *property) const;
    QDate maximum(const QtProperty *property) const;
    bool check(const QtProperty *property) const override;

public Q_SLOTS:
    void setValue(QtProperty *property, QDate val);
    void setMinimum(QtProperty *property, QDate minVal);
    void setMaximum(QtProperty *property, QDate maxVal);
    void setRange(QtProperty *property, QDate minVal, QDate maxVal);
    void setCheck(QtProperty *property, bool check) override;
Q_SIGNALS:
    void valueChanged(QtProperty *property, QDate val);
    void rangeChanged(QtProperty *property, QDate minVal, QDate maxVal);
    void checkChanged(QtProperty *property, bool check);
protected:
    QString valueText(const QtProperty *property) const override;
    void initializeProperty(QtProperty *property) override;
    void uninitializeProperty(QtProperty *property) override;
private:
    QScopedPointer<QtDatePropertyManagerPrivate> d_ptr;
    Q_DECLARE_PRIVATE(QtDatePropertyManager)
    Q_DISABLE_COPY_MOVE(QtDatePropertyManager)
};

class QtTimePropertyManagerPrivate;

class QtTimePropertyManager : public QtAbstractPropertyManager
{
    Q_OBJECT
public:
    QtTimePropertyManager(QObject *parent = 0);
    ~QtTimePropertyManager();

    QTime value(const QtProperty *property) const;
    bool check(const QtProperty *property) const override;

public Q_SLOTS:
    void setValue(QtProperty *property, QTime val);
    void setCheck(QtProperty *property, bool check) override;
Q_SIGNALS:
    void valueChanged(QtProperty *property, QTime val);
    void checkChanged(QtProperty *property, bool check);
protected:
    QString valueText(const QtProperty *property) const override;
    void initializeProperty(QtProperty *property) override;
    void uninitializeProperty(QtProperty *property) override;
private:
    QScopedPointer<QtTimePropertyManagerPrivate> d_ptr;
    Q_DECLARE_PRIVATE(QtTimePropertyManager)
    Q_DISABLE_COPY_MOVE(QtTimePropertyManager)
};

class QtDateTimePropertyManagerPrivate;

class QtDateTimePropertyManager : public QtAbstractPropertyManager
{
    Q_OBJECT
public:
    QtDateTimePropertyManager(QObject *parent = 0);
    ~QtDateTimePropertyManager();

    QDateTime value(const QtProperty *property) const;
    bool check(const QtProperty *property) const override;

public Q_SLOTS:
    void setValue(QtProperty *property, const QDateTime &val);
    void setCheck(QtProperty *property, bool check) override;
Q_SIGNALS:
    void valueChanged(QtProperty *property, const QDateTime &val);
    void checkChanged(QtProperty *property, bool check);
protected:
    QString valueText(const QtProperty *property) const override;
    void initializeProperty(QtProperty *property) override;
    void uninitializeProperty(QtProperty *property) override;
private:
    QScopedPointer<QtDateTimePropertyManagerPrivate> d_ptr;
    Q_DECLARE_PRIVATE(QtDateTimePropertyManager)
    Q_DISABLE_COPY_MOVE(QtDateTimePropertyManager)
};

class QtKeySequencePropertyManagerPrivate;

class QtKeySequencePropertyManager : public QtAbstractPropertyManager
{
    Q_OBJECT
public:
    QtKeySequencePropertyManager(QObject *parent = 0);
    ~QtKeySequencePropertyManager();

    QKeySequence value(const QtProperty *property) const;
    bool check(const QtProperty *property) const override;

public Q_SLOTS:
    void setValue(QtProperty *property, const QKeySequence &val);
    void setCheck(QtProperty *property, bool check) override;
Q_SIGNALS:
    void valueChanged(QtProperty *property, const QKeySequence &val);
    void checkChanged(QtProperty *property, bool check);
protected:
    QString valueText(const QtProperty *property) const override;
    void initializeProperty(QtProperty *property) override;
    void uninitializeProperty(QtProperty *property) override;
private:
    QScopedPointer<QtKeySequencePropertyManagerPrivate> d_ptr;
    Q_DECLARE_PRIVATE(QtKeySequencePropertyManager)
    Q_DISABLE_COPY_MOVE(QtKeySequencePropertyManager)
};

class QtCharPropertyManagerPrivate;

class QtCharPropertyManager : public QtAbstractPropertyManager
{
    Q_OBJECT
public:
    QtCharPropertyManager(QObject *parent = 0);
    ~QtCharPropertyManager();

    QChar value(const QtProperty *property) const;
    bool check(const QtProperty *property) const override;

public Q_SLOTS:
    void setValue(QtProperty *property, const QChar &val);
    void setCheck(QtProperty *property, bool check) override;
Q_SIGNALS:
    void valueChanged(QtProperty *property, const QChar &val);
    void checkChanged(QtProperty *property, bool check);
protected:
    QString valueText(const QtProperty *property) const override;
    void initializeProperty(QtProperty *property) override;
    void uninitializeProperty(QtProperty *property) override;
private:
    QScopedPointer<QtCharPropertyManagerPrivate> d_ptr;
    Q_DECLARE_PRIVATE(QtCharPropertyManager)
    Q_DISABLE_COPY_MOVE(QtCharPropertyManager)
};

class QtEnumPropertyManager;
class QtLocalePropertyManagerPrivate;

class QtLocalePropertyManager : public QtAbstractPropertyManager
{
    Q_OBJECT
public:
    QtLocalePropertyManager(QObject *parent = 0);
    ~QtLocalePropertyManager();

    QtEnumPropertyManager *subEnumPropertyManager() const;

    QLocale value(const QtProperty *property) const;
    bool check(const QtProperty *property) const override;

public Q_SLOTS:
    void setValue(QtProperty *property, const QLocale &val);
    void setCheck(QtProperty *property, bool check) override;
Q_SIGNALS:
    void valueChanged(QtProperty *property, const QLocale &val);
    void checkChanged(QtProperty *property, bool check);
protected:
    QString valueText(const QtProperty *property) const override;
    void initializeProperty(QtProperty *property) override;
    void uninitializeProperty(QtProperty *property) override;
private:
    QScopedPointer<QtLocalePropertyManagerPrivate> d_ptr;
    Q_DECLARE_PRIVATE(QtLocalePropertyManager)
    Q_DISABLE_COPY_MOVE(QtLocalePropertyManager)
    Q_PRIVATE_SLOT(d_func(), void slotEnumChanged(QtProperty *, int))
    Q_PRIVATE_SLOT(d_func(), void slotPropertyDestroyed(QtProperty *))
};

class QtPointPropertyManagerPrivate;

class QtPointPropertyManager : public QtAbstractPropertyManager
{
    Q_OBJECT
public:
    QtPointPropertyManager(QObject *parent = 0);
    ~QtPointPropertyManager();

    QtIntPropertyManager *subIntPropertyManager() const;

    QPoint value(const QtProperty *property) const;
    bool check(const QtProperty *property) const override;

public Q_SLOTS:
    void setValue(QtProperty *property, const QPoint &val);
    void setCheck(QtProperty *property, bool check) override;
Q_SIGNALS:
    void valueChanged(QtProperty *property, const QPoint &val);
    void checkChanged(QtProperty *property, bool check);
protected:
    QString valueText(const QtProperty *property) const override;
    void initializeProperty(QtProperty *property) override;
    void uninitializeProperty(QtProperty *property) override;
private:
    QScopedPointer<QtPointPropertyManagerPrivate> d_ptr;
    Q_DECLARE_PRIVATE(QtPointPropertyManager)
    Q_DISABLE_COPY_MOVE(QtPointPropertyManager)
    Q_PRIVATE_SLOT(d_func(), void slotIntChanged(QtProperty *, int))
    Q_PRIVATE_SLOT(d_func(), void slotPropertyDestroyed(QtProperty *))
};

class QtPointFPropertyManagerPrivate;

class QtPointFPropertyManager : public QtAbstractPropertyManager
{
    Q_OBJECT
public:
    QtPointFPropertyManager(QObject *parent = 0);
    ~QtPointFPropertyManager();

    QtDoublePropertyManager *subDoublePropertyManager() const;

    QPointF value(const QtProperty *property) const;
    QPointF minimum(const QtProperty *property) const;
    QPointF maximum(const QtProperty *property) const;
    int decimals(const QtProperty *property) const;
    int precision(const QtProperty *property) const;
    bool check(const QtProperty *property) const override;

public Q_SLOTS:
    void setValue(QtProperty *property, const QPointF &val);
    void setMinimum(QtProperty *property, const QPointF &minVal);
    void setMaximum(QtProperty *property, const QPointF &maxVal);
    void setRange(QtProperty *property, const QPointF &minVal, const QPointF &maxVal);
    void setPrecision(QtProperty *property, int prec);
    void setCheck(QtProperty *property, bool check) override;
Q_SIGNALS:
    void valueChanged(QtProperty *property, const QPointF &val);
    void rangeChanged(QtProperty *property, const QPointF &minVal, const QPointF &maxVal);
    void precisionChanged(QtProperty *property, int prec);
    void checkChanged(QtProperty *property, bool check);
protected:
    QString valueText(const QtProperty *property) const override;
    void initializeProperty(QtProperty *property) override;
    void uninitializeProperty(QtProperty *property) override;
private:
    QScopedPointer<QtPointFPropertyManagerPrivate> d_ptr;
    Q_DECLARE_PRIVATE(QtPointFPropertyManager)
    Q_DISABLE_COPY_MOVE(QtPointFPropertyManager)
    Q_PRIVATE_SLOT(d_func(), void slotDoubleChanged(QtProperty *, double))
    Q_PRIVATE_SLOT(d_func(), void slotPropertyDestroyed(QtProperty *))
};

class QtSizePropertyManagerPrivate;

class QtSizePropertyManager : public QtAbstractPropertyManager
{
    Q_OBJECT
public:
    QtSizePropertyManager(QObject *parent = 0);
    ~QtSizePropertyManager();

    QtIntPropertyManager *subIntPropertyManager() const;

    QSize value(const QtProperty *property) const;
    QSize minimum(const QtProperty *property) const;
    QSize maximum(const QtProperty *property) const;
    bool check(const QtProperty *property) const override;
    bool isReadOnly(const QtProperty *property) const override;

public Q_SLOTS:
    void setValue(QtProperty *property, const QSize &val);
    void setMinimum(QtProperty *property, const QSize &minVal);
    void setMaximum(QtProperty *property, const QSize &maxVal);
    void setRange(QtProperty *property, const QSize &minVal, const QSize &maxVal);
    void setCheck(QtProperty *property, bool check) override;
    void setReadOnly(QtProperty *property, bool readOnly);
Q_SIGNALS:
    void valueChanged(QtProperty *property, const QSize &val);
    void rangeChanged(QtProperty *property, const QSize &minVal, const QSize &maxVal);
    void checkChanged(QtProperty *property, bool check);
    void readOnlyChanged(QtProperty *property, bool readOnly);
protected:
    QString valueText(const QtProperty *property) const override;
    void initializeProperty(QtProperty *property) override;
    void uninitializeProperty(QtProperty *property) override;
private:
    QScopedPointer<QtSizePropertyManagerPrivate> d_ptr;
    Q_DECLARE_PRIVATE(QtSizePropertyManager)
    Q_DISABLE_COPY_MOVE(QtSizePropertyManager)
    Q_PRIVATE_SLOT(d_func(), void slotIntChanged(QtProperty *, int))
    Q_PRIVATE_SLOT(d_func(), void slotPropertyDestroyed(QtProperty *))
};

class QtSizeFPropertyManagerPrivate;

class QtSizeFPropertyManager : public QtAbstractPropertyManager
{
    Q_OBJECT
public:
    QtSizeFPropertyManager(QObject *parent = 0);
    ~QtSizeFPropertyManager();

    QtDoublePropertyManager *subDoublePropertyManager() const;

    QSizeF value(const QtProperty *property) const;
    QSizeF minimum(const QtProperty *property) const;
    QSizeF maximum(const QtProperty *property) const;
    int decimals(const QtProperty *property) const;
    int precision(const QtProperty *property) const;
    bool check(const QtProperty *property) const override;
    bool isReadOnly(const QtProperty *property) const override;

public Q_SLOTS:
    void setValue(QtProperty *property, const QSizeF &val);
    void setMinimum(QtProperty *property, const QSizeF &minVal);
    void setMaximum(QtProperty *property, const QSizeF &maxVal);
    void setRange(QtProperty *property, const QSizeF &minVal, const QSizeF &maxVal);
    void setPrecision(QtProperty *property, int prec);
    void setCheck(QtProperty *property, bool check) override;
    void setReadOnly(QtProperty *property, bool readOnly);
Q_SIGNALS:
    void valueChanged(QtProperty *property, const QSizeF &val);
    void rangeChanged(QtProperty *property, const QSizeF &minVal, const QSizeF &maxVal);
    void precisionChanged(QtProperty *property, int prec);
    void checkChanged(QtProperty *property, bool check);
    void readOnlyChanged(QtProperty *property, bool readOnly);
protected:
    QString valueText(const QtProperty *property) const override;
    void initializeProperty(QtProperty *property) override;
    void uninitializeProperty(QtProperty *property) override;
private:
    QScopedPointer<QtSizeFPropertyManagerPrivate> d_ptr;
    Q_DECLARE_PRIVATE(QtSizeFPropertyManager)
    Q_DISABLE_COPY_MOVE(QtSizeFPropertyManager)
    Q_PRIVATE_SLOT(d_func(), void slotDoubleChanged(QtProperty *, double))
    Q_PRIVATE_SLOT(d_func(), void slotPropertyDestroyed(QtProperty *))
};

class QtRectPropertyManagerPrivate;

class QtRectPropertyManager : public QtAbstractPropertyManager
{
    Q_OBJECT
public:
    QtRectPropertyManager(QObject *parent = 0);
    ~QtRectPropertyManager();

    QtIntPropertyManager *subIntPropertyManager() const;

    QRect value(const QtProperty *property) const;
    QRect constraint(const QtProperty *property) const;
    bool check(const QtProperty *property) const override;

public Q_SLOTS:
    void setValue(QtProperty *property, const QRect &val);
    void setConstraint(QtProperty *property, const QRect &constraint);
    void setCheck(QtProperty *property, bool check) override;
Q_SIGNALS:
    void valueChanged(QtProperty *property, const QRect &val);
    void constraintChanged(QtProperty *property, const QRect &constraint);
    void checkChanged(QtProperty *property, bool check);
protected:
    QString valueText(const QtProperty *property) const override;
    void initializeProperty(QtProperty *property) override;
    void uninitializeProperty(QtProperty *property) override;
private:
    QScopedPointer<QtRectPropertyManagerPrivate> d_ptr;
    Q_DECLARE_PRIVATE(QtRectPropertyManager)
    Q_DISABLE_COPY_MOVE(QtRectPropertyManager)
    Q_PRIVATE_SLOT(d_func(), void slotIntChanged(QtProperty *, int))
    Q_PRIVATE_SLOT(d_func(), void slotPropertyDestroyed(QtProperty *))
};

class QtRectFPropertyManagerPrivate;

class QtRectFPropertyManager : public QtAbstractPropertyManager
{
    Q_OBJECT
public:
    QtRectFPropertyManager(QObject *parent = 0);
    ~QtRectFPropertyManager();

    QtDoublePropertyManager *subDoublePropertyManager() const;

    QRectF value(const QtProperty *property) const;
    QRectF constraint(const QtProperty *property) const;
    int decimals(const QtProperty *property) const;
    int precision(const QtProperty *property) const;
    bool check(const QtProperty *property) const override;

public Q_SLOTS:
    void setValue(QtProperty *property, const QRectF &val);
    void setConstraint(QtProperty *property, const QRectF &constraint);
    void setPrecision(QtProperty *property, int prec);
    void setCheck(QtProperty *property, bool check) override;
Q_SIGNALS:
    void valueChanged(QtProperty *property, const QRectF &val);
    void constraintChanged(QtProperty *property, const QRectF &constraint);
    void precisionChanged(QtProperty *property, int prec);
    void checkChanged(QtProperty *property, bool check);
protected:
    QString valueText(const QtProperty *property) const override;
    void initializeProperty(QtProperty *property) override;
    void uninitializeProperty(QtProperty *property) override;
private:
    QScopedPointer<QtRectFPropertyManagerPrivate> d_ptr;
    Q_DECLARE_PRIVATE(QtRectFPropertyManager)
    Q_DISABLE_COPY_MOVE(QtRectFPropertyManager)
    Q_PRIVATE_SLOT(d_func(), void slotDoubleChanged(QtProperty *, double))
    Q_PRIVATE_SLOT(d_func(), void slotPropertyDestroyed(QtProperty *))
};

class QtEnumPropertyManagerPrivate;

class QtEnumPropertyManager : public QtAbstractPropertyManager
{
    Q_OBJECT
public:
    QtEnumPropertyManager(QObject *parent = 0);
    ~QtEnumPropertyManager();

    int value(const QtProperty *property) const;
    QStringList enumNames(const QtProperty *property) const;
    QMap<int, QIcon> enumIcons(const QtProperty *property) const;
    bool check(const QtProperty *property) const override;

public Q_SLOTS:
    void setValue(QtProperty *property, int val);
    void setEnumNames(QtProperty *property, const QStringList &names);
    void setEnumIcons(QtProperty *property, const QMap<int, QIcon> &icons);
    void setCheck(QtProperty *property, bool check) override;
Q_SIGNALS:
    void valueChanged(QtProperty *property, int val);
    void enumNamesChanged(QtProperty *property, const QStringList &names);
    void enumIconsChanged(QtProperty *property, const QMap<int, QIcon> &icons);
    void checkChanged(QtProperty *property, bool check);
protected:
    QString valueText(const QtProperty *property) const override;
    QIcon valueIcon(const QtProperty *property) const override;
    void initializeProperty(QtProperty *property) override;
    void uninitializeProperty(QtProperty *property) override;
private:
    QScopedPointer<QtEnumPropertyManagerPrivate> d_ptr;
    Q_DECLARE_PRIVATE(QtEnumPropertyManager)
    Q_DISABLE_COPY_MOVE(QtEnumPropertyManager)
};

class QtFlagPropertyManagerPrivate;

class QtFlagPropertyManager : public QtAbstractPropertyManager
{
    Q_OBJECT
public:
    QtFlagPropertyManager(QObject *parent = 0);
    ~QtFlagPropertyManager();

    QtBoolPropertyManager *subBoolPropertyManager() const;

    int value(const QtProperty *property) const;
    QStringList flagNames(const QtProperty *property) const;
    bool check(const QtProperty *property) const override;

public Q_SLOTS:
    void setValue(QtProperty *property, int val);
    void setFlagNames(QtProperty *property, const QStringList &names);
    void setCheck(QtProperty *property, bool check) override;
Q_SIGNALS:
    void valueChanged(QtProperty *property, int val);
    void flagNamesChanged(QtProperty *property, const QStringList &names);
    void checkChanged(QtProperty *property, bool check);
protected:
    QString valueText(const QtProperty *property) const override;
    void initializeProperty(QtProperty *property) override;
    void uninitializeProperty(QtProperty *property) override;
private:
    QScopedPointer<QtFlagPropertyManagerPrivate> d_ptr;
    Q_DECLARE_PRIVATE(QtFlagPropertyManager)
    Q_DISABLE_COPY_MOVE(QtFlagPropertyManager)
    Q_PRIVATE_SLOT(d_func(), void slotBoolChanged(QtProperty *, bool))
    Q_PRIVATE_SLOT(d_func(), void slotPropertyDestroyed(QtProperty *))
};

class QtSizePolicyPropertyManagerPrivate;

class QtSizePolicyPropertyManager : public QtAbstractPropertyManager
{
    Q_OBJECT
public:
    QtSizePolicyPropertyManager(QObject *parent = 0);
    ~QtSizePolicyPropertyManager();

    QtIntPropertyManager *subIntPropertyManager() const;
    QtEnumPropertyManager *subEnumPropertyManager() const;

    QSizePolicy value(const QtProperty *property) const;
    bool check(const QtProperty *property) const override;

public Q_SLOTS:
    void setValue(QtProperty *property, const QSizePolicy &val);
    void setCheck(QtProperty *property, bool check) override;
Q_SIGNALS:
    void valueChanged(QtProperty *property, const QSizePolicy &val);
    void checkChanged(QtProperty *property, bool check);
protected:
    QString valueText(const QtProperty *property) const override;
    void initializeProperty(QtProperty *property) override;
    void uninitializeProperty(QtProperty *property) override;
private:
    QScopedPointer<QtSizePolicyPropertyManagerPrivate> d_ptr;
    Q_DECLARE_PRIVATE(QtSizePolicyPropertyManager)
    Q_DISABLE_COPY_MOVE(QtSizePolicyPropertyManager)
    Q_PRIVATE_SLOT(d_func(), void slotIntChanged(QtProperty *, int))
    Q_PRIVATE_SLOT(d_func(), void slotEnumChanged(QtProperty *, int))
    Q_PRIVATE_SLOT(d_func(), void slotPropertyDestroyed(QtProperty *))
};

class QtFontPropertyManagerPrivate;

class QtFontPropertyManager : public QtAbstractPropertyManager
{
    Q_OBJECT
public:
    QtFontPropertyManager(QObject *parent = 0);
    ~QtFontPropertyManager();

    QtIntPropertyManager *subIntPropertyManager() const;
    QtEnumPropertyManager *subEnumPropertyManager() const;
    QtBoolPropertyManager *subBoolPropertyManager() const;

    QFont value(const QtProperty *property) const;
    bool check(const QtProperty *property) const override;

public Q_SLOTS:
    void setValue(QtProperty *property, const QFont &val);
    void setCheck(QtProperty *property, bool check) override;
Q_SIGNALS:
    void valueChanged(QtProperty *property, const QFont &val);
    void checkChanged(QtProperty *property, bool check);
protected:
    QString valueText(const QtProperty *property) const override;
    QIcon valueIcon(const QtProperty *property) const override;
    void initializeProperty(QtProperty *property) override;
    void uninitializeProperty(QtProperty *property) override;
private:
    QScopedPointer<QtFontPropertyManagerPrivate> d_ptr;
    Q_DECLARE_PRIVATE(QtFontPropertyManager)
    Q_DISABLE_COPY_MOVE(QtFontPropertyManager)
    Q_PRIVATE_SLOT(d_func(), void slotIntChanged(QtProperty *, int))
    Q_PRIVATE_SLOT(d_func(), void slotEnumChanged(QtProperty *, int))
    Q_PRIVATE_SLOT(d_func(), void slotBoolChanged(QtProperty *, bool))
    Q_PRIVATE_SLOT(d_func(), void slotPropertyDestroyed(QtProperty *))
    Q_PRIVATE_SLOT(d_func(), void slotFontDatabaseChanged())
    Q_PRIVATE_SLOT(d_func(), void slotFontDatabaseDelayedChange())
};

class QtColorPropertyManagerPrivate;

class QtColorPropertyManager : public QtAbstractPropertyManager
{
    Q_OBJECT
public:
    QtColorPropertyManager(QObject *parent = 0);
    ~QtColorPropertyManager();

    QtIntPropertyManager *subIntPropertyManager() const;

    QColor value(const QtProperty *property) const;
    bool check(const QtProperty *property) const override;

public Q_SLOTS:
    void setValue(QtProperty *property, const QColor &val);
    void setCheck(QtProperty *property, bool check) override;
Q_SIGNALS:
    void valueChanged(QtProperty *property, const QColor &val);
    void checkChanged(QtProperty *property, bool check);
protected:
    QString valueText(const QtProperty *property) const override;
    QIcon valueIcon(const QtProperty *property) const override;
    void initializeProperty(QtProperty *property) override;
    void uninitializeProperty(QtProperty *property) override;
private:
    QScopedPointer<QtColorPropertyManagerPrivate> d_ptr;
    Q_DECLARE_PRIVATE(QtColorPropertyManager)
    Q_DISABLE_COPY_MOVE(QtColorPropertyManager)
    Q_PRIVATE_SLOT(d_func(), void slotIntChanged(QtProperty *, int))
    Q_PRIVATE_SLOT(d_func(), void slotPropertyDestroyed(QtProperty *))
};

class QtCursorPropertyManagerPrivate;

class QtCursorPropertyManager : public QtAbstractPropertyManager
{
    Q_OBJECT
public:
    QtCursorPropertyManager(QObject *parent = 0);
    ~QtCursorPropertyManager();

#ifndef QT_NO_CURSOR
    QCursor value(const QtProperty *property) const;
#endif
    bool check(const QtProperty *property) const override;

public Q_SLOTS:
    void setValue(QtProperty *property, const QCursor &val);
    void setCheck(QtProperty *property, bool check) override;
Q_SIGNALS:
    void valueChanged(QtProperty *property, const QCursor &val);
    void checkChanged(QtProperty *property, bool check);
protected:
    QString valueText(const QtProperty *property) const override;
    QIcon valueIcon(const QtProperty *property) const override;
    void initializeProperty(QtProperty *property) override;
    void uninitializeProperty(QtProperty *property) override;
private:
    QScopedPointer<QtCursorPropertyManagerPrivate> d_ptr;
    Q_DECLARE_PRIVATE(QtCursorPropertyManager)
    Q_DISABLE_COPY_MOVE(QtCursorPropertyManager)
};

class QtFilePropertyManagerPrivate;

class QtFilePropertyManager : public QtAbstractPropertyManager
{
    Q_OBJECT
public:
    QtFilePropertyManager(QObject *parent = 0);
    ~QtFilePropertyManager();

    QString value(const QtProperty *property) const;
    QString filter(const QtProperty *property) const;
    QFileDialog::FileMode fileMode(const QtProperty *property) const;
    bool check(const QtProperty *property) const override;
    bool isReadOnly(const QtProperty *property) const override;
public Q_SLOTS:
    void setValue(QtProperty *, const QString &);
    void setFilter(QtProperty *, const QString &);
    void setFileMode(QtProperty *, const QFileDialog::FileMode mode);
    void setCheck(QtProperty *property, bool check) override;
    void setReadOnly(QtProperty *property, bool readOnly);
Q_SIGNALS:
    void valueChanged(QtProperty *, const QString &);
    void filterChanged(QtProperty *, const QString &);
    void checkChanged(QtProperty *property, bool check);
    void readOnlyChanged(QtProperty *property, bool readOnly);
protected:
    QString valueText(const QtProperty *property) const override;
    void initializeProperty(QtProperty *property) override;
    void uninitializeProperty(QtProperty *property) override;
private:
    QScopedPointer<QtFilePropertyManagerPrivate> d_ptr;
    Q_DECLARE_PRIVATE(QtFilePropertyManager)
    Q_DISABLE_COPY_MOVE(QtFilePropertyManager)
};

QT_END_NAMESPACE

#endif
