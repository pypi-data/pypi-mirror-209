//
// Created by dylan_bespalko on 3/14/23.
//

#ifndef QTCUSTOMPROPERTYBROWSERTEST_H
#define QTCUSTOMPROPERTYBROWSERTEST_H

#include <iostream>

#include <QObject>
#include <QDialog>
#include <QGridLayout>
#include <QScrollArea>
#include "QtTreePropertyBrowser"
#include "QtGroupBoxPropertyBrowser"
#include "QtButtonPropertyBrowser"
#include "QtGroupPropertyManager"
#include "QtGroupEditorFactory"

#include "qtpropertybrowsertest.h"

QT_BEGIN_NAMESPACE

class QtIntPropertyManagerQtIntEditFactoryTest : public QtIntPropertyManagerQtIntEditFactoryBaseTest
{
Q_OBJECT

public:

    void addProperty() {
        model = new QtModel();
        treePropertyBrowser->setFactoryForManager(qtIntPropertyManager, intEditFactory);
        boxPropertyBrowser->setFactoryForManager(qtIntPropertyManager, intEditFactory);
        buttonPropertyBrowser->setFactoryForManager(qtIntPropertyManager, intEditFactory);
        QObject::connect(qtIntPropertyManager, SIGNAL(valueChanged(QtProperty *, int) ),
                         model, SLOT(setValue(QtProperty *, int) ) );
        QObject::connect(model, SIGNAL(valueChanged(QtProperty *, int) ),
                         qtIntPropertyManager, SLOT(setValue(QtProperty *, int) ) );
        QObject::connect(qtIntPropertyManager, SIGNAL(checkChanged(QtProperty *, bool) ),
                         model, SLOT(setCheck(QtProperty *, bool) ) );

        property = qtIntPropertyManager->addProperty(("int_" + std::to_string(count + 1)).c_str());
        groupProperty->addSubProperty(property);
    };

private slots:

    void init() {
        qtIntPropertyManager->setMinimum(property, INT_MIN_INIT_VECTOR);
        qtIntPropertyManager->setMaximum(property, INT_MAX_INIT_VECTOR);
        qtIntPropertyManager->setValue(property, INT_INIT_VECTOR);
        qtIntPropertyManager->setCheck(property, false);
    };
    void cleanupTestCase() {
        qDebug("Deleting dialog");
        delete dialog;
    };
};

class QtIntPropertyManagerQtSpinBoxFactoryTest : public QtIntPropertyManagerQtSpinBoxFactoryBaseTest
{
Q_OBJECT

public:

    void addProperty() {
        model = new QtModel();
        treePropertyBrowser->setFactoryForManager(qtIntPropertyManager, spinBoxFactory);
        boxPropertyBrowser->setFactoryForManager(qtIntPropertyManager, spinBoxFactory);
        buttonPropertyBrowser->setFactoryForManager(qtIntPropertyManager, spinBoxFactory);
        QObject::connect(qtIntPropertyManager, SIGNAL(valueChanged(QtProperty *, int) ),
                         model, SLOT(setValue(QtProperty *, int) ) );
        QObject::connect(model, SIGNAL(valueChanged(QtProperty *, int) ),
                         qtIntPropertyManager, SLOT(setValue(QtProperty *, int) ) );
        QObject::connect(qtIntPropertyManager, SIGNAL(checkChanged(QtProperty *, bool) ),
                         model, SLOT(setCheck(QtProperty *, bool) ) );

        property = qtIntPropertyManager->addProperty(("int_" + std::to_string(count + 1)).c_str());
        groupProperty->addSubProperty(property);
    };

private slots:

    void init() {
        qtIntPropertyManager->setMinimum(property, INT_MIN_INIT_VECTOR);
        qtIntPropertyManager->setMaximum(property, INT_MAX_INIT_VECTOR);
        qtIntPropertyManager->setValue(property, INT_INIT_VECTOR);
        qtIntPropertyManager->setCheck(property, false);
    };
    void cleanupTestCase() {
        qDebug("Deleting dialog");
        delete dialog;
    };
};

class QtIntPropertyManagerQtSliderFactoryTest : public QtIntPropertyManagerQtSliderFactoryBaseTest
{
Q_OBJECT

public:

    void addProperty() {
        model = new QtModel();
        treePropertyBrowser->setFactoryForManager(qtIntPropertyManager, sliderFactory);
        boxPropertyBrowser->setFactoryForManager(qtIntPropertyManager, sliderFactory);
        buttonPropertyBrowser->setFactoryForManager(qtIntPropertyManager, sliderFactory);
        QObject::connect(qtIntPropertyManager, SIGNAL(valueChanged(QtProperty *, int) ),
                         model, SLOT(setValue(QtProperty *, int) ) );
        QObject::connect(model, SIGNAL(valueChanged(QtProperty *, int) ),
                         qtIntPropertyManager, SLOT(setValue(QtProperty *, int) ) );
        QObject::connect(qtIntPropertyManager, SIGNAL(checkChanged(QtProperty *, bool) ),
                         model, SLOT(setCheck(QtProperty *, bool) ) );

        property = qtIntPropertyManager->addProperty(("int_" + std::to_string(count + 1)).c_str());
        groupProperty->addSubProperty(property);
    };

private slots:

    void init() {
        qtIntPropertyManager->setMinimum(property, INT_MIN_INIT_VECTOR);
        qtIntPropertyManager->setMaximum(property, INT_MAX_INIT_VECTOR);
        qtIntPropertyManager->setValue(property, INT_INIT_VECTOR);
        qtIntPropertyManager->setCheck(property, false);
    };
    void cleanupTestCase() {
        qDebug("Deleting dialog");
        delete dialog;
    };
};

class QtBoolPropertyManagerQtCheckBoxFactoryTest : public QtBoolPropertyManagerQtCheckBoxFactoryBaseTest
{
    Q_OBJECT

public:

    void addProperty() {
        model = new QtModel();
        treePropertyBrowser->setFactoryForManager(qtBoolPropertyManager, checkBoxFactory);
        boxPropertyBrowser->setFactoryForManager(qtBoolPropertyManager, checkBoxFactory);
        buttonPropertyBrowser->setFactoryForManager(qtBoolPropertyManager, checkBoxFactory);
        QObject::connect(qtBoolPropertyManager, SIGNAL(valueChanged(QtProperty *, bool) ),
                         model, SLOT(setValue(QtProperty *, bool) ) );
        QObject::connect(model, SIGNAL(valueChanged(QtProperty *, bool) ),
                         qtBoolPropertyManager, SLOT(setValue(QtProperty *, bool) ) );
        QObject::connect(qtBoolPropertyManager, SIGNAL(checkChanged(QtProperty *, bool) ),
                         model, SLOT(setCheck(QtProperty *, bool) ) );

        property = qtBoolPropertyManager->addProperty(("bool_" + std::to_string(count + 1)).c_str());
        groupProperty->addSubProperty(property);
    };

private slots:

    void init() {
        qtBoolPropertyManager->setValue(property, false);
        qtBoolPropertyManager->setCheck(property, false);
    };
    void cleanupTestCase() {
        qDebug("Deleting dialog");
        delete dialog;
    };
};

class QtDoublePropertyManagerQtDoubleEditFactoryTest : public QtDoublePropertyManagerQtDoubleEditFactoryBaseTest
{
Q_OBJECT

public:

private slots:

    void addProperty() {
        model = new QtModel();
        model->setAtol(atolCalc(DOUBLE_PRECISION, DOUBLE_MAX_TEST_VECTOR, DOUBLE_MIN_TEST_VECTOR));
        treePropertyBrowser->setFactoryForManager(qtDoublePropertyManager, doubleEditFactory);
        boxPropertyBrowser->setFactoryForManager(qtDoublePropertyManager, doubleEditFactory);
        buttonPropertyBrowser->setFactoryForManager(qtDoublePropertyManager, doubleEditFactory);
        QObject::connect(qtDoublePropertyManager, SIGNAL(valueChanged(QtProperty *, double) ),
                         model, SLOT(setValue(QtProperty *, double) ) );
        QObject::connect(model, SIGNAL(valueChanged(QtProperty *, double) ),
                         qtDoublePropertyManager, SLOT(setValue(QtProperty *, double) ) );
        QObject::connect(qtDoublePropertyManager, SIGNAL(checkChanged(QtProperty *, bool) ),
                         model, SLOT(setCheck(QtProperty *, bool) ) );

        property = qtDoublePropertyManager->addProperty(("double_" + std::to_string(count + 1)).c_str());
        groupProperty->addSubProperty(property);
    };
    void init() {
        qtDoublePropertyManager->setMinimum(property, DOUBLE_MIN_INIT_VECTOR);
        qtDoublePropertyManager->setMaximum(property, DOUBLE_MAX_INIT_VECTOR);
        qtDoublePropertyManager->setPrecision(property, DOUBLE_PRECISION);
        qtDoublePropertyManager->setValue(property, DOUBLE_INIT_VECTOR);
        qtDoublePropertyManager->setCheck(property, false);
    };
    void testPrecision();
    void testPrecisionAbsTol();
    void cleanupTestCase() {
        qDebug("Deleting dialog");
        delete dialog;
    };
};

class QtDoublePropertyManagerQtDoubleSpinBoxFactoryTest : public QtDoublePropertyManagerQtDoubleSpinBoxFactoryBaseTest
{
Q_OBJECT

public:

    void addProperty() {
        model = new QtModel();
        model->setAtol(atolCalc(DOUBLE_PRECISION, DOUBLE_MAX_TEST_VECTOR, DOUBLE_MIN_TEST_VECTOR));
        treePropertyBrowser->setFactoryForManager(qtDoublePropertyManager, doubleSpinBoxFactory);
        boxPropertyBrowser->setFactoryForManager(qtDoublePropertyManager, doubleSpinBoxFactory);
        buttonPropertyBrowser->setFactoryForManager(qtDoublePropertyManager, doubleSpinBoxFactory);
        QObject::connect(qtDoublePropertyManager, SIGNAL(valueChanged(QtProperty *, double) ),
                         model, SLOT(setValue(QtProperty *, double) ) );
        QObject::connect(model, SIGNAL(valueChanged(QtProperty *, double) ),
                         qtDoublePropertyManager, SLOT(setValue(QtProperty *, double) ) );
        QObject::connect(qtDoublePropertyManager, SIGNAL(checkChanged(QtProperty *, bool) ),
                         model, SLOT(setCheck(QtProperty *, bool) ) );

        property = qtDoublePropertyManager->addProperty(("double_" + std::to_string(count + 1)).c_str());
        groupProperty->addSubProperty(property);
    }

private slots:

    void init() {
        qtDoublePropertyManager->setMinimum(property, DOUBLE_MIN_INIT_VECTOR);
        qtDoublePropertyManager->setMaximum(property, DOUBLE_MAX_INIT_VECTOR);
        qtDoublePropertyManager->setPrecision(property, DOUBLE_PRECISION);
        qtDoublePropertyManager->setValue(property, DOUBLE_INIT_VECTOR);
        qtDoublePropertyManager->setCheck(property, false);
    };
    void testPrecision();
    void testPrecisionAbsTol();
    void cleanupTestCase() {
        qDebug("Deleting dialog");
        delete dialog;
    };
};

class QtComplexPropertyManagerQtComplexEditFactoryTest : public QtComplexPropertyManagerQtComplexEditFactoryBaseTest
{
Q_OBJECT

public:

    void addProperty() {
        model = new QtModel();
        model->setAtol(atolCalc(COMPLEX_PRECISION, COMPLEX_MAX_TEST_VECTOR, COMPLEX_MIN_TEST_VECTOR));
        treePropertyBrowser->setFactoryForManager(qtComplexPropertyManager, complexEditFactory);
        boxPropertyBrowser->setFactoryForManager(qtComplexPropertyManager, complexEditFactory);
        buttonPropertyBrowser->setFactoryForManager(qtComplexPropertyManager, complexEditFactory);
        QObject::connect(qtComplexPropertyManager, SIGNAL(valueChanged(QtProperty *, const QtComplex &) ),
                         model, SLOT(setValue(QtProperty *, const QtComplex &) ) );
        QObject::connect(model, SIGNAL(valueChanged(QtProperty *, const QtComplex &) ),
                         qtComplexPropertyManager, SLOT(setValue(QtProperty *, const QtComplex &) ) );
        QObject::connect(qtComplexPropertyManager, SIGNAL(checkChanged(QtProperty *, bool) ),
                         model, SLOT(setCheck(QtProperty *, bool) ) );

        property = qtComplexPropertyManager->addProperty(("QtComplex_" + std::to_string(count + 1)).c_str());
        groupProperty->addSubProperty(property);
    }

private slots:

    void init() {
        qtComplexPropertyManager->setPrecision(property, COMPLEX_PRECISION);
        qtComplexPropertyManager->setMinimum(property, COMPLEX_MIN_INIT_VECTOR);
        qtComplexPropertyManager->setMaximum(property, COMPLEX_MAX_INIT_VECTOR);
        qtComplexPropertyManager->setValue(property, QtComplex(COMPLEX_INIT_VECTOR));
        qtComplexPropertyManager->setCheck(property, false);
    };
    void testPrecision();
    void testPrecisionAbsTol();
    void cleanupTestCase() {
        qDebug("Deleting dialog");
        delete dialog;
    };
};

class QtQuaternionPropertyManagerQtQuaternionEditFactoryTest : public QtQuaternionPropertyManagerQtQuaternionEditFactoryBaseTest
{
Q_OBJECT

public:

    void addProperty() {
        model = new QtModel();
        model->setAtol(atolCalc(QUATERNION_PRECISION, QUATERNION_MAX_TEST_VECTOR, QUATERNION_MIN_TEST_VECTOR));
        treePropertyBrowser->setFactoryForManager(qtQuaternionPropertyManager, quaternionEditFactory);
        boxPropertyBrowser->setFactoryForManager(qtQuaternionPropertyManager, quaternionEditFactory);
        buttonPropertyBrowser->setFactoryForManager(qtQuaternionPropertyManager, quaternionEditFactory);
        QObject::connect(qtQuaternionPropertyManager, SIGNAL(valueChanged(QtProperty *, const QtQuaternion &) ),
                         model, SLOT(setValue(QtProperty *, const QtQuaternion &) ) );
        QObject::connect(model, SIGNAL(valueChanged(QtProperty *, const QtQuaternion &) ),
                         qtQuaternionPropertyManager, SLOT(setValue(QtProperty *, const QtQuaternion &) ) );
        QObject::connect(qtQuaternionPropertyManager, SIGNAL(checkChanged(QtProperty *, bool) ),
                         model, SLOT(setCheck(QtProperty *, bool) ) );

        property = qtQuaternionPropertyManager->addProperty(("Quaternion_" + std::to_string(count + 1)).c_str());
        groupProperty->addSubProperty(property);
    }

private slots:

    void init() {
        qtQuaternionPropertyManager->setPrecision(property, QUATERNION_PRECISION);
        qtQuaternionPropertyManager->setMinimum(property, QtQuaternion(QUATERNION_MIN_INIT_VECTOR));
        qtQuaternionPropertyManager->setMaximum(property, QtQuaternion(QUATERNION_MAX_INIT_VECTOR));
        qtQuaternionPropertyManager->setValue(property, QtQuaternion(QUATERNION_INIT_VECTOR));
        qtQuaternionPropertyManager->setCheck(property, false);
    };
    void testPrecision();
    void testPrecisionAbsTol();
    void cleanupTestCase() {
        qDebug("Deleting dialog");
        delete dialog;
    };
};

class QtVectorComplexPropertyManagerQtVectorComplexEditFactoryTest : public QtVectorComplexPropertyManagerQtVectorComplexEditFactoryBaseTest
{
Q_OBJECT

public:

    void addProperty() {
        model = new QtModel();
        model->setAtol(atolCalc(COMPLEX_PRECISION, COMPLEX_MAX_TEST_VECTOR, COMPLEX_MIN_TEST_VECTOR));
        vectorComplexEditFactory->setSubFactory(complexEditFactory);
        treePropertyBrowser->setFactoryForManager(qtVectorComplexPropertyManager, vectorComplexEditFactory);
        boxPropertyBrowser->setFactoryForManager(qtVectorComplexPropertyManager, vectorComplexEditFactory);
        buttonPropertyBrowser->setFactoryForManager(qtVectorComplexPropertyManager, vectorComplexEditFactory);
        treePropertyBrowser->setFactoryForManager(qtVectorComplexPropertyManager->subComplexPropertyManager(),complexEditFactory);
        boxPropertyBrowser->setFactoryForManager(qtVectorComplexPropertyManager->subComplexPropertyManager(), complexEditFactory);
        buttonPropertyBrowser->setFactoryForManager(qtVectorComplexPropertyManager->subComplexPropertyManager(), complexEditFactory);
        QObject::connect(qtVectorComplexPropertyManager, SIGNAL(valueChanged(QtProperty *, const QVector<QtComplex> &) ),
                         model, SLOT(setValue(QtProperty *, const QVector<QtComplex> &) ) );
        QObject::connect(model, SIGNAL(valueChanged(QtProperty *, const QVector<QtComplex> &) ),
                         qtVectorComplexPropertyManager, SLOT(setValue(QtProperty *, const QVector<QtComplex> &) ) );
        QObject::connect(qtVectorComplexPropertyManager, SIGNAL(checkChanged(QtProperty *, bool) ),
                         model, SLOT(setCheck(QtProperty *, bool) ) );

        property = qtVectorComplexPropertyManager->addProperty(("QVector<QtComplex>_" + std::to_string(count + 1)).c_str());
        groupProperty->addSubProperty(property);
    }

private slots:

    void init() {
        qtVectorComplexPropertyManager->setSize(property, VECTOR_SIZE);
        qtVectorComplexPropertyManager->setPrecision(property, COMPLEX_PRECISION);
        qtVectorComplexPropertyManager->setMinimum(property, QVector<QtComplex>(VECTOR_SIZE, QtComplex(COMPLEX_MIN_INIT_VECTOR)));
        qtVectorComplexPropertyManager->setMaximum(property, QVector<QtComplex>(VECTOR_SIZE, QtComplex(COMPLEX_MAX_INIT_VECTOR)));
        qtVectorComplexPropertyManager->setValue(property, QVector<QtComplex>(VECTOR_SIZE, {COMPLEX_INIT_VECTOR}));
        qtVectorComplexPropertyManager->setCheck(property, false);
    };
    void testPrecision();
    void testPrecisionAbsTol();
    void cleanupTestCase() {
        qDebug("Deleting dialog");
        delete dialog;
    };
};

class QtStringPropertyManagerQtLineEditFactoryTest : public QtStringPropertyManagerQtLineEditFactoryBaseTest
{
Q_OBJECT

public:

    void addProperty() {
        model = new QtModel();
        treePropertyBrowser->setFactoryForManager(qtStringPropertyManager, lineEditFactory);
        boxPropertyBrowser->setFactoryForManager(qtStringPropertyManager, lineEditFactory);
        buttonPropertyBrowser->setFactoryForManager(qtStringPropertyManager, lineEditFactory);
        QObject::connect(qtStringPropertyManager, SIGNAL(valueChanged(QtProperty *, const QString &) ),
                         model, SLOT(setValue(QtProperty *, const QString &) ) );
        QObject::connect(model, SIGNAL(valueChanged(QtProperty *, const QString &) ),
                         qtStringPropertyManager, SLOT(setValue(QtProperty *, const QString &) ) );
        QObject::connect(qtStringPropertyManager, SIGNAL(checkChanged(QtProperty *, bool) ),
                         model, SLOT(setCheck(QtProperty *, bool) ) );

        property = qtStringPropertyManager->addProperty(("QString_" + std::to_string(count + 1)).c_str());
        groupProperty->addSubProperty(property);
    }

private slots:

    void init() {
        qtStringPropertyManager->setValue(property, STR_INIT_VECTOR);
        qtStringPropertyManager->setCheck(property, false);
    };
    void cleanupTestCase() {
        qDebug("Deleting dialog");
        delete dialog;
    };
};

class QtDatePropertyManagerQtDateEditFactoryTest : public QtDatePropertyManagerQtDateEditFactoryBaseTest
{
Q_OBJECT

public:

    void addProperty() {
        model = new QtModel();
        treePropertyBrowser->setFactoryForManager(qtDatePropertyManager, dateEditFactory);
        boxPropertyBrowser->setFactoryForManager(qtDatePropertyManager, dateEditFactory);
        buttonPropertyBrowser->setFactoryForManager(qtDatePropertyManager, dateEditFactory);
        QObject::connect(qtDatePropertyManager, SIGNAL(valueChanged(QtProperty *, QDate) ),
                         model, SLOT(setValue(QtProperty *, QDate) ) );
        QObject::connect(model, SIGNAL(valueChanged(QtProperty *, QDate) ),
                         qtDatePropertyManager, SLOT(setValue(QtProperty *, QDate) ) );
        QObject::connect(qtDatePropertyManager, SIGNAL(checkChanged(QtProperty *, bool) ),
                         model, SLOT(setCheck(QtProperty *, bool) ) );

        property = qtDatePropertyManager->addProperty(("QDate_" + std::to_string(count + 1)).c_str());
        groupProperty->addSubProperty(property);
    }

private slots:

    void init() {
        qtDatePropertyManager->setValue(property, QDate(DATE_INIT_VECTOR));
        qtDatePropertyManager->setCheck(property, false);
    };
    void cleanupTestCase() {
        qDebug("Deleting dialog");
        delete dialog;
    };
};

class QtTimePropertyManagerQtTimeEditFactoryTest : public QtTimePropertyManagerQtTimeEditFactoryBaseTest
{
Q_OBJECT

public:

    void addProperty() {
        model = new QtModel();
        treePropertyBrowser->setFactoryForManager(qtTimePropertyManager, timeEditFactory);
        boxPropertyBrowser->setFactoryForManager(qtTimePropertyManager, timeEditFactory);
        buttonPropertyBrowser->setFactoryForManager(qtTimePropertyManager, timeEditFactory);
        QObject::connect(qtTimePropertyManager, SIGNAL(valueChanged(QtProperty *, QTime) ),
                         model, SLOT(setValue(QtProperty *, QTime) ) );
        QObject::connect(model, SIGNAL(valueChanged(QtProperty *, QTime) ),
                         qtTimePropertyManager, SLOT(setValue(QtProperty *, QTime) ) );
        QObject::connect(qtTimePropertyManager, SIGNAL(checkChanged(QtProperty *, bool) ),
                         model, SLOT(setCheck(QtProperty *, bool) ) );

        property = qtTimePropertyManager->addProperty(("QTime_" + std::to_string(count + 1)).c_str());
        groupProperty->addSubProperty(property);
    }

private slots:

    void init() {
        qtTimePropertyManager->setValue(property, QTime(TIME_INIT_VECTOR));
        qtTimePropertyManager->setCheck(property, false);
    };
    void cleanupTestCase() {
        qDebug("Deleting dialog");
        delete dialog;
    };
};

class QtDateTimePropertyManagerQtDateTimeEditFactoryTest : public QtDateTimePropertyManagerQtDateTimeEditFactoryBaseTest
{
Q_OBJECT

public:

    void addProperty() {
        model = new QtModel();
        treePropertyBrowser->setFactoryForManager(qtDateTimePropertyManager, dateTimeEditFactory);
        boxPropertyBrowser->setFactoryForManager(qtDateTimePropertyManager, dateTimeEditFactory);
        buttonPropertyBrowser->setFactoryForManager(qtDateTimePropertyManager, dateTimeEditFactory);
        QObject::connect(qtDateTimePropertyManager, SIGNAL(valueChanged(QtProperty *, QDateTime) ),
                         model, SLOT(setValue(QtProperty *, QDateTime) ) );
        QObject::connect(model, SIGNAL(valueChanged(QtProperty *, QDateTime) ),
                         qtDateTimePropertyManager, SLOT(setValue(QtProperty *, QDateTime) ) );
        QObject::connect(qtDateTimePropertyManager, SIGNAL(checkChanged(QtProperty *, bool) ),
                         model, SLOT(setCheck(QtProperty *, bool) ) );

        property = qtDateTimePropertyManager->addProperty(("QDateTime_" + std::to_string(count + 1)).c_str());
        groupProperty->addSubProperty(property);
    }

private slots:

    void init() {
        qtDateTimePropertyManager->setValue(property, QDateTime(DATETIME_INIT_VECTOR));
        qtDateTimePropertyManager->setCheck(property, false);
    };
    void cleanupTestCase() {
        qDebug("Deleting dialog");
        delete dialog;
    };
};

class QtKeySequencePropertyManagerQtKeySequenceEditorFactoryTest : public QtKeySequencePropertyManagerQtKeySequenceEditorFactoryBaseTest
{
Q_OBJECT

public:

    void addProperty() {
        model = new QtModel();
        treePropertyBrowser->setFactoryForManager(qtKeySequencePropertyManager, keySequenceEditorFactory);
        boxPropertyBrowser->setFactoryForManager(qtKeySequencePropertyManager, keySequenceEditorFactory);
        buttonPropertyBrowser->setFactoryForManager(qtKeySequencePropertyManager, keySequenceEditorFactory);
        QObject::connect(qtKeySequencePropertyManager, SIGNAL(valueChanged(QtProperty *, const QKeySequence &) ),
                         model, SLOT(setValue(QtProperty *, const QKeySequence &) ) );
        QObject::connect(model, SIGNAL(valueChanged(QtProperty *, const QKeySequence &) ),
                         qtKeySequencePropertyManager, SLOT(setValue(QtProperty *, const QKeySequence &) ) );
        QObject::connect(qtKeySequencePropertyManager, SIGNAL(checkChanged(QtProperty *, bool) ),
                         model, SLOT(setCheck(QtProperty *, bool) ) );

        property = qtKeySequencePropertyManager->addProperty(("QKeySequence_" + std::to_string(count + 1)).c_str());
        groupProperty->addSubProperty(property);
    }

private slots:

    void init() {
        qtKeySequencePropertyManager->setValue(property, QKeySequence(KEY_INIT_VECTOR));
        qtKeySequencePropertyManager->setCheck(property, false);
    };
    void cleanupTestCase() {
        qDebug("Deleting dialog");
        delete dialog;
    };
};

class QtCharPropertyManagerQtCharEditorFactoryTest : public QtCharPropertyManagerQtCharEditorFactoryBaseTest
{
Q_OBJECT

public:

    void addProperty() {
        model = new QtModel();
        treePropertyBrowser->setFactoryForManager(qtCharPropertyManager, charEditorFactory);
        boxPropertyBrowser->setFactoryForManager(qtCharPropertyManager, charEditorFactory);
        buttonPropertyBrowser->setFactoryForManager(qtCharPropertyManager, charEditorFactory);
        QObject::connect(qtCharPropertyManager, SIGNAL(valueChanged(QtProperty *, const QChar &) ),
                         model, SLOT(setValue(QtProperty *, const QChar &) ) );
        QObject::connect(model, SIGNAL(valueChanged(QtProperty *, const QChar &) ),
                         qtCharPropertyManager, SLOT(setValue(QtProperty *, const QChar &) ) );
        QObject::connect(qtCharPropertyManager, SIGNAL(checkChanged(QtProperty *, bool) ),
                         model, SLOT(setCheck(QtProperty *, bool) ) );

        property = qtCharPropertyManager->addProperty(("QChar_" + std::to_string(count + 1)).c_str());
        groupProperty->addSubProperty(property);
    }

private slots:

    void init() {
        qtCharPropertyManager->setValue(property, CHAR_INIT_VECTOR);
        qtCharPropertyManager->setCheck(property, false);
    };
    void cleanupTestCase() {
        qDebug("Deleting dialog");
        delete dialog;
    };
};

class QtPointPropertyManagerQtPointEditorFactoryTest : public QtPointPropertyManagerQtPointEditorFactoryBaseTest
{
Q_OBJECT

public:

    void addProperty() {
        model = new QtModel();
        treePropertyBrowser->setFactoryForManager(qtPointPropertyManager, pointEditorFactory);
        boxPropertyBrowser->setFactoryForManager(qtPointPropertyManager, pointEditorFactory);
        buttonPropertyBrowser->setFactoryForManager(qtPointPropertyManager, pointEditorFactory);
        treePropertyBrowser->setFactoryForManager(qtPointPropertyManager->subIntPropertyManager(), intEditFactory);
        boxPropertyBrowser->setFactoryForManager(qtPointPropertyManager->subIntPropertyManager(), intEditFactory);
        buttonPropertyBrowser->setFactoryForManager(qtPointPropertyManager->subIntPropertyManager(), intEditFactory);
        QObject::connect(qtPointPropertyManager, SIGNAL(valueChanged(QtProperty *, const QPoint &) ),
                         model, SLOT(setValue(QtProperty *, const QPoint &) ) );
        QObject::connect(model, SIGNAL(valueChanged(QtProperty *, const QPoint &) ),
                         qtPointPropertyManager, SLOT(setValue(QtProperty *, const QPoint &) ) );
        QObject::connect(qtPointPropertyManager, SIGNAL(checkChanged(QtProperty *, bool) ),
                         model, SLOT(setCheck(QtProperty *, bool) ) );

        property = qtPointPropertyManager->addProperty(("QPoint_" + std::to_string(count + 1)).c_str());
        groupProperty->addSubProperty(property);
    }

private slots:

    void init() {
        qtPointPropertyManager->setValue(property, QPoint(POINT_INIT_VECTOR));
        qtPointPropertyManager->setCheck(property, false);
    };
    void cleanupTestCase() {
        qDebug("Deleting dialog");
        delete dialog;
    };
};

class QtPointFPropertyManagerQtPointFEditorFactoryTest : public QtPointFPropertyManagerQtPointFEditorFactoryBaseTest
{
Q_OBJECT

public:

    void addProperty() {
        model = new QtModel();
        model->setAtol(atolCalc(DOUBLE_PRECISION, DOUBLE_MAX_TEST_VECTOR, DOUBLE_MIN_TEST_VECTOR));
        treePropertyBrowser->setFactoryForManager(qtPointFPropertyManager, pointFEditorFactory);
        boxPropertyBrowser->setFactoryForManager(qtPointFPropertyManager, pointFEditorFactory);
        buttonPropertyBrowser->setFactoryForManager(qtPointFPropertyManager, pointFEditorFactory);
        treePropertyBrowser->setFactoryForManager(qtPointFPropertyManager->subDoublePropertyManager(),doubleEditFactory);
        boxPropertyBrowser->setFactoryForManager(qtPointFPropertyManager->subDoublePropertyManager(), doubleEditFactory);
        buttonPropertyBrowser->setFactoryForManager(qtPointFPropertyManager->subDoublePropertyManager(), doubleEditFactory);
        QObject::connect(qtPointFPropertyManager, SIGNAL(valueChanged(QtProperty *, const QPointF &) ),
                         model, SLOT(setValue(QtProperty *, const QPointF &) ) );
        QObject::connect(model, SIGNAL(valueChanged(QtProperty *, const QPointF &) ),
                         qtPointFPropertyManager, SLOT(setValue(QtProperty *, const QPointF &) ) );
        QObject::connect(qtPointFPropertyManager, SIGNAL(checkChanged(QtProperty *, bool) ),
                         model, SLOT(setCheck(QtProperty *, bool) ) );

        property = qtPointFPropertyManager->addProperty(("QPointF_" + std::to_string(count + 1)).c_str());
        groupProperty->addSubProperty(property);
    }

private slots:

    void init() {
        qtPointFPropertyManager->setMinimum(property, QPointF(POINTF_MIN_INIT_VECTOR));
        qtPointFPropertyManager->setMaximum(property, QPointF(POINTF_MAX_INIT_VECTOR));
        qtPointFPropertyManager->setPrecision(property, DOUBLE_PRECISION);
        qtPointFPropertyManager->setValue(property, QPointF(POINTF_INIT_VECTOR));
        qtPointFPropertyManager->setCheck(property, false);
    };
    void cleanupTestCase() {
        qDebug("Deleting dialog");
        delete dialog;
    };
};

class QtSizePropertyManagerQtSizeEditorFactoryTest : public QtSizePropertyManagerQtSizeEditorFactoryBaseTest
{
Q_OBJECT

public:

    void addProperty() {
        model = new QtModel();
        treePropertyBrowser->setFactoryForManager(qtSizePropertyManager, sizeEditorFactory);
        boxPropertyBrowser->setFactoryForManager(qtSizePropertyManager, sizeEditorFactory);
        buttonPropertyBrowser->setFactoryForManager(qtSizePropertyManager, sizeEditorFactory);
        treePropertyBrowser->setFactoryForManager(qtSizePropertyManager->subIntPropertyManager(), intEditFactory);
        boxPropertyBrowser->setFactoryForManager(qtSizePropertyManager->subIntPropertyManager(), intEditFactory);
        buttonPropertyBrowser->setFactoryForManager(qtSizePropertyManager->subIntPropertyManager(), intEditFactory);
        QObject::connect(qtSizePropertyManager, SIGNAL(valueChanged(QtProperty *, const QSize &) ),
                         model, SLOT(setValue(QtProperty *, const QSize &) ) );
        QObject::connect(model, SIGNAL(valueChanged(QtProperty *, const QSize &) ),
                         qtSizePropertyManager, SLOT(setValue(QtProperty *, const QSize &) ) );
        QObject::connect(qtSizePropertyManager, SIGNAL(checkChanged(QtProperty *, bool) ),
                         model, SLOT(setCheck(QtProperty *, bool) ) );

        property = qtSizePropertyManager->addProperty(("QSize_" + std::to_string(count + 1)).c_str());
        groupProperty->addSubProperty(property);
    }

private slots:

    void init() {
        qtSizePropertyManager->setValue(property, QSize(SIZE_INIT_VECTOR));
        qtSizePropertyManager->setCheck(property, false);
    };
    void cleanupTestCase() {
        qDebug("Deleting dialog");
        delete dialog;
    };
};

class QtSizeFPropertyManagerQtSizeFEditorFactoryTest : public QtSizeFPropertyManagerQtSizeFEditorFactoryBaseTest
{
Q_OBJECT

public:

    void addProperty() {
        model = new QtModel();
        model->setAtol(atolCalc(DOUBLE_PRECISION, DOUBLE_MAX_TEST_VECTOR, DOUBLE_MIN_TEST_VECTOR));
        treePropertyBrowser->setFactoryForManager(qtSizeFPropertyManager, sizeFEditorFactory);
        boxPropertyBrowser->setFactoryForManager(qtSizeFPropertyManager, sizeFEditorFactory);
        buttonPropertyBrowser->setFactoryForManager(qtSizeFPropertyManager, sizeFEditorFactory);
        treePropertyBrowser->setFactoryForManager(qtSizeFPropertyManager->subDoublePropertyManager(),doubleEditFactory);
        boxPropertyBrowser->setFactoryForManager(qtSizeFPropertyManager->subDoublePropertyManager(), doubleEditFactory);
        buttonPropertyBrowser->setFactoryForManager(qtSizeFPropertyManager->subDoublePropertyManager(), doubleEditFactory);
        QObject::connect(qtSizeFPropertyManager, SIGNAL(valueChanged(QtProperty *, const QSizeF &) ),
                         model, SLOT(setValue(QtProperty *, const QSizeF &) ) );
        QObject::connect(model, SIGNAL(valueChanged(QtProperty *, const QSizeF &) ),
                         qtSizeFPropertyManager, SLOT(setValue(QtProperty *, const QSizeF &) ) );
        QObject::connect(qtSizeFPropertyManager, SIGNAL(checkChanged(QtProperty *, bool) ),
                         model, SLOT(setCheck(QtProperty *, bool) ) );

        property = qtSizeFPropertyManager->addProperty(("QSizeF_" + std::to_string(count + 1)).c_str());
        groupProperty->addSubProperty(property);
    }

private slots:

    void init() {
        qtSizeFPropertyManager->setMinimum(property, QSizeF(SIZEF_MIN_INIT_VECTOR));
        qtSizeFPropertyManager->setMaximum(property, QSizeF(SIZEF_MAX_INIT_VECTOR));
        qtSizeFPropertyManager->setPrecision(property, DOUBLE_PRECISION);
        qtSizeFPropertyManager->setValue(property, QSizeF(SIZEF_INIT_VECTOR));
        qtSizeFPropertyManager->setCheck(property, false);
    };
    void cleanupTestCase() {
        qDebug("Deleting dialog");
        delete dialog;
    };
};

class QtRectPropertyManagerQtRectEditorFactoryTest : public QtRectPropertyManagerQtRectEditorFactoryBaseTest
{
Q_OBJECT

public:

    void addProperty() {
        model = new QtModel();
        treePropertyBrowser->setFactoryForManager(qtRectPropertyManager, rectEditorFactory);
        boxPropertyBrowser->setFactoryForManager(qtRectPropertyManager, rectEditorFactory);
        buttonPropertyBrowser->setFactoryForManager(qtRectPropertyManager, rectEditorFactory);
        treePropertyBrowser->setFactoryForManager(qtRectPropertyManager->subIntPropertyManager(), intEditFactory);
        boxPropertyBrowser->setFactoryForManager(qtRectPropertyManager->subIntPropertyManager(), intEditFactory);
        buttonPropertyBrowser->setFactoryForManager(qtRectPropertyManager->subIntPropertyManager(), intEditFactory);
        QObject::connect(qtRectPropertyManager, SIGNAL(valueChanged(QtProperty *, const QRect &) ),
                         model, SLOT(setValue(QtProperty *, const QRect &) ) );
        QObject::connect(model, SIGNAL(valueChanged(QtProperty *, const QRect &) ),
                         qtRectPropertyManager, SLOT(setValue(QtProperty *, const QRect &) ) );
        QObject::connect(qtRectPropertyManager, SIGNAL(checkChanged(QtProperty *, bool) ),
                         model, SLOT(setCheck(QtProperty *, bool) ) );

        property = qtRectPropertyManager->addProperty(("QRect_" + std::to_string(count + 1)).c_str());
        groupProperty->addSubProperty(property);
    }

private slots:

    void init() {
        qtRectPropertyManager->setValue(property, QRect(RECT_INIT_VECTOR));
        qtRectPropertyManager->setCheck(property, false);
    };
    void cleanupTestCase() {
        qDebug("Deleting dialog");
        delete dialog;
    };
};

class QtRectFPropertyManagerQtRectFEditorFactoryTest : public QtRectFPropertyManagerQtRectFEditorFactoryBaseTest
{
Q_OBJECT

public:

    void addProperty() {
        model = new QtModel();
        model->setAtol(atolCalc(DOUBLE_PRECISION, DOUBLE_MAX_TEST_VECTOR, DOUBLE_MIN_TEST_VECTOR));
        treePropertyBrowser->setFactoryForManager(qtRectFPropertyManager, rectFEditorFactory);
        boxPropertyBrowser->setFactoryForManager(qtRectFPropertyManager, rectFEditorFactory);
        buttonPropertyBrowser->setFactoryForManager(qtRectFPropertyManager, rectFEditorFactory);
        treePropertyBrowser->setFactoryForManager(qtRectFPropertyManager->subDoublePropertyManager(),doubleEditFactory);
        boxPropertyBrowser->setFactoryForManager(qtRectFPropertyManager->subDoublePropertyManager(), doubleEditFactory);
        buttonPropertyBrowser->setFactoryForManager(qtRectFPropertyManager->subDoublePropertyManager(), doubleEditFactory);
        QObject::connect(qtRectFPropertyManager, SIGNAL(valueChanged(QtProperty *, const QRectF &) ),
                         model, SLOT(setValue(QtProperty *, const QRectF &) ) );
        QObject::connect(model, SIGNAL(valueChanged(QtProperty *, const QRectF &) ),
                         qtRectFPropertyManager, SLOT(setValue(QtProperty *, const QRectF &) ) );
        QObject::connect(qtRectFPropertyManager, SIGNAL(checkChanged(QtProperty *, bool) ),
                         model, SLOT(setCheck(QtProperty *, bool) ) );

        property = qtRectFPropertyManager->addProperty(("QRectF_" + std::to_string(count + 1)).c_str());
        groupProperty->addSubProperty(property);
    }

private slots:

    void init() {
        qtRectFPropertyManager->setConstraint(property, QRectF(RECTF_CONST_INIT_VECTOR));
        qtRectFPropertyManager->setPrecision(property, DOUBLE_PRECISION);
        qtRectFPropertyManager->setValue(property, QRectF(RECTF_INIT_VECTOR));
        qtRectFPropertyManager->setCheck(property, false);
    };
    void cleanupTestCase() {
        qDebug("Deleting dialog");
        delete dialog;
    };
};

class QtEnumPropertyManagerQtEnumEditorFactoryTest : public QtEnumPropertyManagerQtEnumEditorFactoryBaseTest
{
Q_OBJECT

public:

    void addProperty() {
        model = new QtModel();
        treePropertyBrowser->setFactoryForManager(qtEnumPropertyManager, enumEditorFactory);
        boxPropertyBrowser->setFactoryForManager(qtEnumPropertyManager, enumEditorFactory);
        buttonPropertyBrowser->setFactoryForManager(qtEnumPropertyManager, enumEditorFactory);
        QObject::connect(qtEnumPropertyManager, SIGNAL(valueChanged(QtProperty *, int) ),
                         model, SLOT(setValue(QtProperty *, int) ) );
        QObject::connect(model, SIGNAL(valueChanged(QtProperty *, int) ),
                         qtEnumPropertyManager, SLOT(setValue(QtProperty *, int) ) );
        QObject::connect(qtEnumPropertyManager, SIGNAL(checkChanged(QtProperty *, bool) ),
                         model, SLOT(setCheck(QtProperty *, bool) ) );

        property = qtEnumPropertyManager->addProperty(("int_" + std::to_string(count + 1)).c_str());
        groupProperty->addSubProperty(property);
    }

private slots:

    void init() {
        QStringList enumNames;
        enumNames << "BLACK" << "RED" << "GREEN" << "BLUE";
        qtEnumPropertyManager->setEnumNames(property, enumNames);
        qtEnumPropertyManager->setValue(property, ENUM_INIT_VECTOR);
        qtEnumPropertyManager->setCheck(property, false);
    };
    void cleanupTestCase() {
        qDebug("Deleting dialog");
        delete dialog;
    };
};

class QtFlagPropertyManagerQtFlagEditorFactoryTest : public QtFlagPropertyManagerQtFlagEditorFactoryBaseTest
{
Q_OBJECT

public:

    void addProperty() {
        model = new QtModel();
        treePropertyBrowser->setFactoryForManager(qtFlagPropertyManager, flagEditorFactory);
        boxPropertyBrowser->setFactoryForManager(qtFlagPropertyManager, flagEditorFactory);
        buttonPropertyBrowser->setFactoryForManager(qtFlagPropertyManager, flagEditorFactory);
        treePropertyBrowser->setFactoryForManager(qtFlagPropertyManager->subBoolPropertyManager(), checkBoxFactory);
        boxPropertyBrowser->setFactoryForManager(qtFlagPropertyManager->subBoolPropertyManager(), checkBoxFactory);
        buttonPropertyBrowser->setFactoryForManager(qtFlagPropertyManager->subBoolPropertyManager(),checkBoxFactory);
        QObject::connect(qtFlagPropertyManager, SIGNAL(valueChanged(QtProperty *, int) ),
                         model, SLOT(setValue(QtProperty *, int) ) );
        QObject::connect(model, SIGNAL(valueChanged(QtProperty *, int) ),
                         qtFlagPropertyManager, SLOT(setValue(QtProperty *, int) ) );
        QObject::connect(qtFlagPropertyManager, SIGNAL(checkChanged(QtProperty *, bool) ),
                         model, SLOT(setCheck(QtProperty *, bool) ) );

        property = qtFlagPropertyManager->addProperty(("int_" + std::to_string(count + 1)).c_str());
        groupProperty->addSubProperty(property);
    }

private slots:

    void init() {
        QStringList flagNames;
        flagNames << "RED" << "GREEN" << "BLUE";
        qtFlagPropertyManager->setFlagNames(property, flagNames);
        qtFlagPropertyManager->setValue(property, int(FLAG_INIT_VECTOR));
        qtFlagPropertyManager->setCheck(property, false);
    };
    void cleanupTestCase() {
        qDebug("Deleting dialog");
        delete dialog;
    };
};

class QtLocalePropertyManagerQtLocaleEditorFactoryTest : public QtLocalePropertyManagerQtLocaleEditorFactoryBaseTest
{
Q_OBJECT

public:

    void addProperty() {
        model = new QtModel();
        treePropertyBrowser->setFactoryForManager(qtLocalePropertyManager, localeEditorFactory);
        boxPropertyBrowser->setFactoryForManager(qtLocalePropertyManager, localeEditorFactory);
        buttonPropertyBrowser->setFactoryForManager(qtLocalePropertyManager, localeEditorFactory);
        treePropertyBrowser->setFactoryForManager(qtLocalePropertyManager->subEnumPropertyManager(), enumEditorFactory);
        boxPropertyBrowser->setFactoryForManager(qtLocalePropertyManager->subEnumPropertyManager(),enumEditorFactory);
        buttonPropertyBrowser->setFactoryForManager(qtLocalePropertyManager->subEnumPropertyManager(),enumEditorFactory);
        QObject::connect(qtLocalePropertyManager, SIGNAL(valueChanged(QtProperty *, const QLocale &) ),
                         model, SLOT(setValue(QtProperty *, const QLocale &) ) );
        QObject::connect(model, SIGNAL(valueChanged(QtProperty *, const QLocale &) ),
                         qtLocalePropertyManager, SLOT(setValue(QtProperty *, const QLocale &) ) );
        QObject::connect(qtLocalePropertyManager, SIGNAL(checkChanged(QtProperty *, bool) ),
                         model, SLOT(setCheck(QtProperty *, bool) ) );

        property = qtLocalePropertyManager->addProperty(("QLocale_" + std::to_string(count + 1)).c_str());
        groupProperty->addSubProperty(property);
    }

private slots:

    void init() {
        qtLocalePropertyManager->setValue(property, QLocale(LOCALE_INIT_VECTOR));
        qtLocalePropertyManager->setCheck(property, false);
    };
    void cleanupTestCase() {
        qDebug("Deleting dialog");
        delete dialog;
    };
};

class QtSizePolicyPropertyManagerQtSizePolicyEditorFactoryTest : public QtSizePolicyPropertyManagerQtSizePolicyEditorFactoryBaseTest
{
Q_OBJECT

public:

    void addProperty() {
        model = new QtModel();
        treePropertyBrowser->setFactoryForManager(qtSizePolicyPropertyManager, sizePolicyEditorFactory);
        boxPropertyBrowser->setFactoryForManager(qtSizePolicyPropertyManager, sizePolicyEditorFactory);
        buttonPropertyBrowser->setFactoryForManager(qtSizePolicyPropertyManager, sizePolicyEditorFactory);
        treePropertyBrowser->setFactoryForManager(qtSizePolicyPropertyManager->subEnumPropertyManager(), enumEditorFactory);
        boxPropertyBrowser->setFactoryForManager(qtSizePolicyPropertyManager->subIntPropertyManager(), intEditFactory);
        buttonPropertyBrowser->setFactoryForManager(qtSizePolicyPropertyManager->subEnumPropertyManager(), enumEditorFactory);
        treePropertyBrowser->setFactoryForManager(qtSizePolicyPropertyManager->subIntPropertyManager(), intEditFactory);
        boxPropertyBrowser->setFactoryForManager(qtSizePolicyPropertyManager->subEnumPropertyManager(), enumEditorFactory);
        buttonPropertyBrowser->setFactoryForManager(qtSizePolicyPropertyManager->subIntPropertyManager(), intEditFactory);
        QObject::connect(qtSizePolicyPropertyManager, SIGNAL(valueChanged(QtProperty *, const QSizePolicy &) ),
                         model, SLOT(setValue(QtProperty *, const QSizePolicy &) ) );
        QObject::connect(model, SIGNAL(valueChanged(QtProperty *, const QSizePolicy &) ),
                         qtSizePolicyPropertyManager, SLOT(setValue(QtProperty *, const QSizePolicy &) ) );
        QObject::connect(qtSizePolicyPropertyManager, SIGNAL(checkChanged(QtProperty *, bool) ),
                         model, SLOT(setCheck(QtProperty *, bool) ) );

        property = qtSizePolicyPropertyManager->addProperty(("QSizePolicy_" + std::to_string(count + 1)).c_str());
        groupProperty->addSubProperty(property);
    }

private slots:

    void init() {
        QSizePolicy sizePolicy = QSizePolicy(SIZE_POLICY_INIT_VECTOR);
        sizePolicy.setHorizontalStretch(X_STRETCH_SIZE_POLICY_INIT_VECTOR);
        sizePolicy.setVerticalStretch(Y_STRETCH_SIZE_POLICY_INIT_VECTOR);
        qtSizePolicyPropertyManager->setValue(property, sizePolicy);
        qtSizePolicyPropertyManager->setCheck(property, false);
    };
    void cleanupTestCase() {
        qDebug("Deleting dialog");
        delete dialog;
    };
};

class QtFontPropertyManagerQtFontEditorFactoryTest : public QtFontPropertyManagerQtFontEditorFactoryBaseTest
{
Q_OBJECT

public:

    void addProperty() {
        model = new QtModel();
        treePropertyBrowser->setFactoryForManager(qtFontPropertyManager, fontEditorFactory);
        boxPropertyBrowser->setFactoryForManager(qtFontPropertyManager, fontEditorFactory);
        buttonPropertyBrowser->setFactoryForManager(qtFontPropertyManager, fontEditorFactory);
        QObject::connect(qtFontPropertyManager, SIGNAL(valueChanged(QtProperty *, const QFont &) ),
                         model, SLOT(setValue(QtProperty *, const QFont &) ) );
        QObject::connect(model, SIGNAL(valueChanged(QtProperty *, const QFont &) ),
                         qtFontPropertyManager, SLOT(setValue(QtProperty *, const QFont &) ) );
        QObject::connect(qtFontPropertyManager, SIGNAL(checkChanged(QtProperty *, bool) ),
                         model, SLOT(setCheck(QtProperty *, bool) ) );

        property = qtFontPropertyManager->addProperty(("QFont_" + std::to_string(count + 1)).c_str());
        groupProperty->addSubProperty(property);
    }

private slots:

    void init() {
        qtFontPropertyManager->setValue(property, QFont(FONT_INIT_VECTOR));
        qtFontPropertyManager->setCheck(property, false);
    };
    void cleanupTestCase() {
        qDebug("Deleting dialog");
        delete dialog;
    };
};

class QtColorPropertyManagerQtColorEditorFactoryTest : public QtColorPropertyManagerQtColorEditorFactoryBaseTest
{
Q_OBJECT

public:

    void addProperty() {
        model = new QtModel();
        treePropertyBrowser->setFactoryForManager(qtColorPropertyManager, colorEditorFactory);
        boxPropertyBrowser->setFactoryForManager(qtColorPropertyManager, colorEditorFactory);
        buttonPropertyBrowser->setFactoryForManager(qtColorPropertyManager, colorEditorFactory);
        QObject::connect(qtColorPropertyManager, SIGNAL(valueChanged(QtProperty *, const QColor &) ),
                         model, SLOT(setValue(QtProperty *, const QColor &) ) );
        QObject::connect(model, SIGNAL(valueChanged(QtProperty *, const QColor &) ),
                         qtColorPropertyManager, SLOT(setValue(QtProperty *, const QColor &) ) );
        QObject::connect(qtColorPropertyManager, SIGNAL(checkChanged(QtProperty *, bool) ),
                         model, SLOT(setCheck(QtProperty *, bool) ) );

        property = qtColorPropertyManager->addProperty(("QColor_" + std::to_string(count + 1)).c_str());
        groupProperty->addSubProperty(property);
    }

private slots:

    void init() {
        qtColorPropertyManager->setValue(property, COLOR_INIT_VECTOR);
        qtColorPropertyManager->setCheck(property, false);
    };
    void cleanupTestCase() {
        qDebug("Deleting dialog");
        delete dialog;
    };
};

class QtCursorPropertyManagerQtCursorEditorFactoryTest : public QtCursorPropertyManagerQtCursorEditorFactoryBaseTest
{
Q_OBJECT

public:

    void addProperty() {
        model = new QtModel();
        treePropertyBrowser->setFactoryForManager(qtCursorPropertyManager, cursorEditorFactory);
        boxPropertyBrowser->setFactoryForManager(qtCursorPropertyManager, cursorEditorFactory);
        buttonPropertyBrowser->setFactoryForManager(qtCursorPropertyManager, cursorEditorFactory);
        QObject::connect(qtCursorPropertyManager, SIGNAL(valueChanged(QtProperty *, const QCursor &) ),
                         model, SLOT(setValue(QtProperty *, const QCursor &) ) );
        QObject::connect(model, SIGNAL(valueChanged(QtProperty *, const QCursor &) ),
                         qtCursorPropertyManager, SLOT(setValue(QtProperty *, const QCursor &) ) );
        QObject::connect(qtCursorPropertyManager, SIGNAL(checkChanged(QtProperty *, bool) ),
                         model, SLOT(setCheck(QtProperty *, bool) ) );

        property = qtCursorPropertyManager->addProperty(("QCursor_" + std::to_string(count + 1)).c_str());
        groupProperty->addSubProperty(property);
    }

private slots:

    void init() {
        qtCursorPropertyManager->setValue(property, QCursor(CURSOR_INIT_VECTOR));
        qtCursorPropertyManager->setCheck(property, false);
    };
    void cleanupTestCase() {
        qDebug("Deleting dialog");
        delete dialog;
    };
};

class QtFilePropertyManagerQtFileEditorFactoryTest : public QtFilePropertyManagerQtFileEditorFactoryBaseTest
{
Q_OBJECT

public:

    void addProperty() {
        model = new QtModel();
        treePropertyBrowser->setFactoryForManager(qtFilePropertyManager, fileEditorFactory);
        boxPropertyBrowser->setFactoryForManager(qtFilePropertyManager, fileEditorFactory);
        buttonPropertyBrowser->setFactoryForManager(qtFilePropertyManager, fileEditorFactory);
        QObject::connect(qtFilePropertyManager, SIGNAL(valueChanged(QtProperty *, const QString &) ),
                         model, SLOT(setValue(QtProperty *, const QString &) ) );
        QObject::connect(model, SIGNAL(valueChanged(QtProperty *, const QString &) ),
                         qtFilePropertyManager, SLOT(setValue(QtProperty *, const QString &) ) );
        QObject::connect(qtFilePropertyManager, SIGNAL(checkChanged(QtProperty *, bool) ),
                         model, SLOT(setCheck(QtProperty *, bool) ) );

        property = qtFilePropertyManager->addProperty(("QString_" + std::to_string(count + 1)).c_str());
        groupProperty->addSubProperty(property);
    }

private slots:

    void init() {
        qtFilePropertyManager->setValue(property, FILE_INIT_VECTOR);
        qtFilePropertyManager->setCheck(property, false);
    };
    void cleanupTestCase() {
        qDebug("Deleting dialog");
        delete dialog;
    };
};

QT_END_NAMESPACE

#endif //QTCUSTOMPROPERTYBROWSERTEST_H
