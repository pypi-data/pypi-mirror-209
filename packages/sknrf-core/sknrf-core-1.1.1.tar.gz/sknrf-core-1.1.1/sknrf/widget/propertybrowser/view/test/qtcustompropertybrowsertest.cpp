//
// Created by dylan_bespalko on 3/14/23.
//
#include <string>

#include <QtCore/QObject>
#include <QtCore/QVector>
#include <QtWidgets/QLabel>
#include <QtTest>
#include <QtTest/QSignalSpy>

#include "qtcustompropertybrowsertest.h"

QT_BEGIN_NAMESPACE

void QtDoublePropertyManagerQtDoubleEditFactoryTest::testPrecision()
{
    QSignalSpy spy(qtDoublePropertyManager, SIGNAL(valueChanged(QtProperty *, double)));
    double startValue = qtDoublePropertyManager->value(property);
    double actualValue = qtDoublePropertyManager->value(property);
    double expectedValue;
    int precision = 16;
    double minimum = qtDoublePropertyManager->minimum(property);
    double maximum = qtDoublePropertyManager->maximum(property);
    double absTolSW = std::numeric_limits<double>::epsilon();
    double absTolHWP1, absTolHW, absTolHWM1;
    absTolHWP1 = atolCalc(precision + 1, minimum, maximum);
    absTolHW = atolCalc(precision + 0, minimum, maximum);
    absTolHWM1 = atolCalc(precision - 1, minimum, maximum);
    double relTolSW = std::numeric_limits<double>::min();
    double relTolHWP1, relTolHW, relTolHWM1;
    relTolHWP1 = rtolCalc(precision + 1, minimum, maximum);
    relTolHW = rtolCalc(precision + 0, minimum, maximum);
    relTolHWM1 = rtolCalc(precision - 1, minimum, maximum);
    qtDoublePropertyManager->setPrecision(property, precision);

    qtDoublePropertyManager->setValue(property, startValue + absTolHWP1);
    actualValue = qtDoublePropertyManager->value(property);
    expectedValue = startValue;
    QCOMPARE(spy.count(), 0);
    QVERIFY(isclose(actualValue, expectedValue, absTolSW, relTolSW));

    qtDoublePropertyManager->setValue(property, startValue + absTolHWM1);
    actualValue = qtDoublePropertyManager->value(property);
    expectedValue = startValue + absTolHWM1;
    QCOMPARE(spy.count(), 1);
    QVERIFY(isclose(actualValue, expectedValue, absTolHWM1, relTolHWM1));
}

void QtDoublePropertyManagerQtDoubleEditFactoryTest::testPrecisionAbsTol()
{
    qtDoublePropertyManager->setValue(property, double(0));
    QSignalSpy spy(qtDoublePropertyManager, SIGNAL(valueChanged(QtProperty *, double)));
    double startValue = qtDoublePropertyManager->value(property);
    double actualValue = qtDoublePropertyManager->value(property);
    double expectedValue;
    int precision = 16;
    double minimum = qtDoublePropertyManager->minimum(property);
    double maximum = qtDoublePropertyManager->maximum(property);
    double absTolSW = std::numeric_limits<double>::epsilon();
    double absTolHWP1, absTolHW, absTolHWM1;
    absTolHWP1 = atolCalc(precision + 1, minimum, maximum);
    absTolHW = atolCalc(precision + 0, minimum, maximum);
    absTolHWM1 = atolCalc(precision - 1, minimum, maximum);
    double relTolSW = std::numeric_limits<double>::min();
    double relTolHWP1, relTolHW, relTolHWM1;
    relTolHWP1 = INFINITY;
    relTolHW = INFINITY;
    relTolHWM1 = INFINITY;
    qtDoublePropertyManager->setPrecision(property, precision);

    qtDoublePropertyManager->setValue(property, startValue + absTolHWP1);
    actualValue = qtDoublePropertyManager->value(property);
    expectedValue = startValue;
    QCOMPARE(spy.count(), 0);
    QVERIFY(isclose(actualValue, expectedValue, absTolSW, relTolSW));

    qtDoublePropertyManager->setValue(property, startValue + absTolHWM1);
    actualValue = qtDoublePropertyManager->value(property);
    expectedValue = startValue + absTolHWM1;
    QCOMPARE(spy.count(), 1);
    QVERIFY(isclose(actualValue, expectedValue, absTolHWM1, relTolHWM1));
}

void QtDoublePropertyManagerQtDoubleSpinBoxFactoryTest::testPrecision()
{
    QSignalSpy spy(qtDoublePropertyManager, SIGNAL(valueChanged(QtProperty *, double)));
    double startValue = qtDoublePropertyManager->value(property);
    double actualValue = qtDoublePropertyManager->value(property);
    double expectedValue;
    int precision = 16;
    double minimum = qtDoublePropertyManager->minimum(property);
    double maximum = qtDoublePropertyManager->maximum(property);
    double absTolSW = std::numeric_limits<double>::epsilon();
    double absTolHWP1, absTolHW, absTolHWM1;
    absTolHWP1 = atolCalc(precision + 1, minimum, maximum);
    absTolHW = atolCalc(precision + 0, minimum, maximum);
    absTolHWM1 = atolCalc(precision - 1, minimum, maximum);
    double relTolSW = std::numeric_limits<double>::min();
    double relTolHWP1, relTolHW, relTolHWM1;
    relTolHWP1 = rtolCalc(precision + 1, minimum, maximum);
    relTolHW = rtolCalc(precision + 0, minimum, maximum);
    relTolHWM1 = rtolCalc(precision - 1, minimum, maximum);
    qtDoublePropertyManager->setPrecision(property, precision);

    qtDoublePropertyManager->setValue(property, startValue + absTolHWP1);
    actualValue = qtDoublePropertyManager->value(property);
    expectedValue = startValue;
    QCOMPARE(spy.count(), 0);
    QVERIFY(isclose(actualValue, expectedValue, absTolSW, relTolSW));

    qtDoublePropertyManager->setValue(property, startValue + absTolHWM1);
    actualValue = qtDoublePropertyManager->value(property);
    expectedValue = startValue + absTolHWM1;
    QCOMPARE(spy.count(), 1);
    QVERIFY(isclose(actualValue, expectedValue, absTolHWM1, relTolHWM1));
}

void QtDoublePropertyManagerQtDoubleSpinBoxFactoryTest::testPrecisionAbsTol()
{
    qtDoublePropertyManager->setValue(property, double(0));
    QSignalSpy spy(qtDoublePropertyManager, SIGNAL(valueChanged(QtProperty *, double)));
    double startValue = qtDoublePropertyManager->value(property);
    double actualValue = qtDoublePropertyManager->value(property);
    double expectedValue;
    int precision = 16;
    double minimum = qtDoublePropertyManager->minimum(property);
    double maximum = qtDoublePropertyManager->maximum(property);
    double absTolSW = std::numeric_limits<double>::epsilon();
    double absTolHWP1, absTolHW, absTolHWM1;
    absTolHWP1 = atolCalc(precision + 1, minimum, maximum);
    absTolHW = atolCalc(precision + 0, minimum, maximum);
    absTolHWM1 = atolCalc(precision - 1, minimum, maximum);
    double relTolSW = std::numeric_limits<double>::min();
    double relTolHWP1, relTolHW, relTolHWM1;
    relTolHWP1 = INFINITY;
    relTolHW = INFINITY;
    relTolHWM1 = INFINITY;
    qtDoublePropertyManager->setPrecision(property, precision);

    qtDoublePropertyManager->setValue(property, startValue + absTolHWP1);
    actualValue = qtDoublePropertyManager->value(property);
    expectedValue = startValue;
    QCOMPARE(spy.count(), 0);
    QVERIFY(isclose(actualValue, expectedValue, absTolSW, relTolSW));

    qtDoublePropertyManager->setValue(property, startValue + absTolHWM1);
    actualValue = qtDoublePropertyManager->value(property);
    expectedValue = startValue + absTolHWM1;
    QCOMPARE(spy.count(), 1);
    QVERIFY(isclose(actualValue, expectedValue, absTolHWM1, relTolHWM1));
}

void QtComplexPropertyManagerQtComplexEditFactoryTest::testPrecision()
{
    QSignalSpy spy(qtComplexPropertyManager, SIGNAL(valueChanged(QtProperty *, const QtComplex &)));
    QtComplex startValue = qtComplexPropertyManager->value(property);
    QtComplex actualValue = qtComplexPropertyManager->value(property);
    QtComplex expectedValue;
    int precision = 16;
    QtComplex minimum = qtComplexPropertyManager->minimum(property);
    QtComplex maximum = qtComplexPropertyManager->maximum(property);
    QtComplex absTolSW = std::numeric_limits<double>::epsilon();
    QtComplex absTolHWP1, absTolHW, absTolHWM1;
    absTolHWP1 = atolCalc(precision + 1, minimum, maximum);
    absTolHW = atolCalc(precision + 0, minimum, maximum);
    absTolHWM1 = atolCalc(precision - 1, minimum, maximum);
    QtComplex relTolSW = std::numeric_limits<double>::min();
    QtComplex relTolHWP1, relTolHW, relTolHWM1;
    relTolHWP1 = rtolCalc(precision + 1, minimum, maximum);
    relTolHW = rtolCalc(precision + 0, minimum, maximum);
    relTolHWM1 = rtolCalc(precision - 1, minimum, maximum);
    qtComplexPropertyManager->setPrecision(property, precision);

    qtComplexPropertyManager->setValue(property, startValue + absTolHWP1);
    actualValue = qtComplexPropertyManager->value(property);
    expectedValue = startValue;
    QCOMPARE(spy.count(), 0);
    QVERIFY(isclose(actualValue, expectedValue, absTolSW, relTolSW));

    qtComplexPropertyManager->setValue(property, startValue + absTolHWM1);
    actualValue = qtComplexPropertyManager->value(property);
    expectedValue = startValue + absTolHWM1;
    QCOMPARE(spy.count(), 1);
    QVERIFY(isclose(actualValue, expectedValue, absTolHWM1, relTolHWM1));
}

void QtComplexPropertyManagerQtComplexEditFactoryTest::testPrecisionAbsTol()
{
    qtComplexPropertyManager->setValue(property, QtComplex(0, 0));
    QSignalSpy spy(qtComplexPropertyManager, SIGNAL(valueChanged(QtProperty *, const QtComplex &)));
    QtComplex startValue = qtComplexPropertyManager->value(property);
    QtComplex actualValue = qtComplexPropertyManager->value(property);
    QtComplex expectedValue;
    int precision = 16;
    QtComplex minimum = qtComplexPropertyManager->minimum(property);
    QtComplex maximum = qtComplexPropertyManager->maximum(property);
    QtComplex absTolSW = std::numeric_limits<double>::epsilon();
    QtComplex absTolHWP1, absTolHW, absTolHWM1;
    absTolHWP1 = atolCalc(precision + 1, minimum, maximum);
    absTolHW = atolCalc(precision + 0, minimum, maximum);
    absTolHWM1 = atolCalc(precision - 1, minimum, maximum);
    QtComplex relTolSW = std::numeric_limits<double>::min();
    QtComplex relTolHWP1, relTolHW, relTolHWM1;
    relTolHWP1 = INFINITY;
    relTolHW = INFINITY;
    relTolHWM1 = INFINITY;
    qtComplexPropertyManager->setPrecision(property, precision);

    qtComplexPropertyManager->setValue(property, startValue + absTolHWP1);
    actualValue = qtComplexPropertyManager->value(property);
    expectedValue = startValue;
    QCOMPARE(spy.count(), 0);
    QVERIFY(isclose(actualValue, expectedValue, absTolSW, relTolSW));

    qtComplexPropertyManager->setValue(property, startValue + absTolHWM1);
    actualValue = qtComplexPropertyManager->value(property);
    expectedValue = startValue + absTolHWM1;
    QCOMPARE(spy.count(), 1);
    QVERIFY(isclose(actualValue, expectedValue, absTolHWM1, relTolHWM1));
}

void QtQuaternionPropertyManagerQtQuaternionEditFactoryTest::testPrecision()
{
    QSignalSpy spy(qtQuaternionPropertyManager, SIGNAL(valueChanged(QtProperty *, const QtQuaternion &)));
    QtQuaternion startValue = qtQuaternionPropertyManager->value(property);
    QtQuaternion actualValue = qtQuaternionPropertyManager->value(property);
    QtQuaternion expectedValue;
    int precision = 16;
    QtQuaternion minimum = qtQuaternionPropertyManager->minimum(property);
    QtQuaternion maximum = qtQuaternionPropertyManager->maximum(property);
    QtQuaternion absTolSW = std::numeric_limits<double>::epsilon();
    QtQuaternion absTolHWP1, absTolHW, absTolHWM1;
    absTolHWP1 = atolCalc(precision + 1, minimum, maximum);
    absTolHW = atolCalc(precision + 0, minimum, maximum);
    absTolHWM1 = atolCalc(precision - 1, minimum, maximum);
    QtQuaternion relTolSW = std::numeric_limits<double>::min();
    QtQuaternion relTolHWP1, relTolHW, relTolHWM1;
    relTolHWP1 = rtolCalc(precision + 1, minimum, maximum);
    relTolHW = rtolCalc(precision + 0, minimum, maximum);
    relTolHWM1 = rtolCalc(precision - 1, minimum, maximum);
    qtQuaternionPropertyManager->setPrecision(property, precision);

    qtQuaternionPropertyManager->setValue(property, startValue + absTolHWP1);
    actualValue = qtQuaternionPropertyManager->value(property);
    expectedValue = startValue;
    QCOMPARE(spy.count(), 0);
    QVERIFY(isclose(actualValue, expectedValue, absTolSW, relTolSW));

    qtQuaternionPropertyManager->setValue(property, startValue + absTolHWM1);
    actualValue = qtQuaternionPropertyManager->value(property);
    expectedValue = startValue + absTolHWM1;
    QCOMPARE(spy.count(), 1);
    QVERIFY(isclose(actualValue, expectedValue, absTolHWM1, relTolHWM1));
}

void QtQuaternionPropertyManagerQtQuaternionEditFactoryTest::testPrecisionAbsTol()
{
    qtQuaternionPropertyManager->setValue(property, QtQuaternion(0, 0, 0, 0));
    QSignalSpy spy(qtQuaternionPropertyManager, SIGNAL(valueChanged(QtProperty *, const QtQuaternion &)));
    QtQuaternion startValue = qtQuaternionPropertyManager->value(property);
    QtQuaternion actualValue = qtQuaternionPropertyManager->value(property);
    QtQuaternion expectedValue;
    int precision = 16;
    QtQuaternion minimum = qtQuaternionPropertyManager->minimum(property);
    QtQuaternion maximum = qtQuaternionPropertyManager->maximum(property);
    QtQuaternion absTolSW = std::numeric_limits<double>::epsilon();
    QtQuaternion absTolHWP1, absTolHW, absTolHWM1;
    absTolHWP1 = atolCalc(precision + 1, minimum, maximum);
    absTolHW = atolCalc(precision + 0, minimum, maximum);
    absTolHWM1 = atolCalc(precision - 1, minimum, maximum);
    QtQuaternion relTolSW = std::numeric_limits<double>::min();
    QtQuaternion relTolHWP1, relTolHW, relTolHWM1;
    relTolHWP1 = INFINITY;
    relTolHW = INFINITY;
    relTolHWM1 = INFINITY;
    qtQuaternionPropertyManager->setPrecision(property, precision);

    qtQuaternionPropertyManager->setValue(property, startValue + absTolHWP1);
    actualValue = qtQuaternionPropertyManager->value(property);
    expectedValue = startValue;
    QCOMPARE(spy.count(), 0);
    QVERIFY(isclose(actualValue, expectedValue, absTolSW, relTolSW));

    qtQuaternionPropertyManager->setValue(property, startValue + absTolHWM1);
    actualValue = qtQuaternionPropertyManager->value(property);
    expectedValue = startValue + absTolHWM1;
    QCOMPARE(spy.count(), 1);
    QVERIFY(isclose(actualValue, expectedValue, absTolHWM1, relTolHWM1));
}

void QtVectorComplexPropertyManagerQtVectorComplexEditFactoryTest::testPrecision() {
    QSignalSpy spy(qtVectorComplexPropertyManager, SIGNAL(valueChanged(QtProperty *, const QVector<QtComplex> &)));
    QVector<QtComplex> startValue = qtVectorComplexPropertyManager->value(property);
    QVector<QtComplex> newValue = qtVectorComplexPropertyManager->value(property);
    QVector<QtComplex> actualValue = qtVectorComplexPropertyManager->value(property);
    QVector<QtComplex> expectedValue = qtVectorComplexPropertyManager->value(property);
    int precision = 16;
    QVector<QtComplex> minimum = qtVectorComplexPropertyManager->minimum(property);
    QVector<QtComplex> maximum = qtVectorComplexPropertyManager->maximum(property);
    QVector<QtComplex> absTolSW = QVector<QtComplex>(VECTOR_SIZE, QtComplex(std::numeric_limits<double>::epsilon()));
    QVector<QtComplex> absTolHWP1 = QVector<QtComplex>(VECTOR_SIZE, QtComplex(std::numeric_limits<double>::epsilon()));
    QVector<QtComplex> absTolHW = QVector<QtComplex>(VECTOR_SIZE, QtComplex(std::numeric_limits<double>::epsilon()));
    QVector<QtComplex> absTolHWM1 = QVector<QtComplex>(VECTOR_SIZE, QtComplex(std::numeric_limits<double>::epsilon()));
    absTolHWP1 = atolCalc(precision + 1, minimum, maximum);
    absTolHW = atolCalc(precision + 0, minimum, maximum);
    absTolHWM1 = atolCalc(precision - 1, minimum, maximum);
    QVector<QtComplex> relTolSW = QVector<QtComplex>(VECTOR_SIZE, QtComplex(std::numeric_limits<double>::min()));
    QVector<QtComplex> relTolHWP1 = QVector<QtComplex>(VECTOR_SIZE, QtComplex(std::numeric_limits<double>::min()));
    QVector<QtComplex> relTolHW = QVector<QtComplex>(VECTOR_SIZE, QtComplex(std::numeric_limits<double>::min()));
    QVector<QtComplex> relTolHWM1 = QVector<QtComplex>(VECTOR_SIZE, QtComplex(std::numeric_limits<double>::min()));
    relTolHWP1 = rtolCalc(precision + 1, minimum, maximum);
    relTolHW = rtolCalc(precision + 0, minimum, maximum);
    relTolHWM1 = rtolCalc(precision - 1, minimum, maximum);
    qtVectorComplexPropertyManager->setPrecision(property, precision);

    for (int idx = 1; idx < startValue.size(); idx+=2) {
        newValue[idx] = startValue[idx] + absTolHWP1[idx];
        expectedValue[idx] = startValue[idx];
    }
    qtVectorComplexPropertyManager->setValue(property, newValue);
    actualValue = qtVectorComplexPropertyManager->value(property);
    expectedValue = startValue;
    QCOMPARE(spy.count(), 0);
    QVERIFY(isclose(actualValue, expectedValue, absTolSW, relTolSW));

    for (int idx = 1; idx < startValue.size(); idx+=2) {
        newValue[idx] = startValue[idx] + absTolHWM1[idx];
        expectedValue[idx] = startValue[idx] + absTolHWM1[idx];
    }
    qtVectorComplexPropertyManager->setValue(property, newValue);
    actualValue = qtVectorComplexPropertyManager->value(property);
    QCOMPARE(spy.count(), 1);
    QVERIFY(isclose(actualValue, expectedValue, absTolHWM1, relTolHWM1));
}

void QtVectorComplexPropertyManagerQtVectorComplexEditFactoryTest::testPrecisionAbsTol() {
    QSignalSpy spy(qtVectorComplexPropertyManager, SIGNAL(valueChanged(QtProperty *, const QVector<QtComplex> &)));
    QVector<QtComplex> startValue = qtVectorComplexPropertyManager->value(property);
    QVector<QtComplex> newValue = qtVectorComplexPropertyManager->value(property);
    QVector<QtComplex> actualValue = qtVectorComplexPropertyManager->value(property);
    QVector<QtComplex> expectedValue = qtVectorComplexPropertyManager->value(property);
    int precision = 16;
    QVector<QtComplex> minimum = qtVectorComplexPropertyManager->minimum(property);
    QVector<QtComplex> maximum = qtVectorComplexPropertyManager->maximum(property);
    QVector<QtComplex> absTolSW = QVector<QtComplex>(VECTOR_SIZE, QtComplex(std::numeric_limits<double>::epsilon()));
    QVector<QtComplex> absTolHWP1 = QVector<QtComplex>(VECTOR_SIZE, QtComplex(std::numeric_limits<double>::epsilon()));
    QVector<QtComplex> absTolHW = QVector<QtComplex>(VECTOR_SIZE, QtComplex(std::numeric_limits<double>::epsilon()));
    QVector<QtComplex> absTolHWM1 = QVector<QtComplex>(VECTOR_SIZE, QtComplex(std::numeric_limits<double>::epsilon()));
    absTolHWP1 = atolCalc(precision + 1, minimum, maximum);
    absTolHW = atolCalc(precision + 0, minimum, maximum);
    absTolHWM1 = atolCalc(precision - 1, minimum, maximum);
    QVector<QtComplex> relTolSW = QVector<QtComplex>(VECTOR_SIZE, QtComplex(INFINITY));
    QVector<QtComplex> relTolHWP1 = QVector<QtComplex>(VECTOR_SIZE, QtComplex(INFINITY));
    QVector<QtComplex> relTolHW = QVector<QtComplex>(VECTOR_SIZE, QtComplex(INFINITY));
    QVector<QtComplex> relTolHWM1 = QVector<QtComplex>(VECTOR_SIZE, QtComplex(INFINITY));
    relTolHWP1 = rtolCalc(precision + 1, minimum, maximum);
    relTolHW = rtolCalc(precision + 0, minimum, maximum);
    relTolHWM1  = rtolCalc(precision - 1, minimum, maximum);
    qtVectorComplexPropertyManager->setPrecision(property, precision);

    for (int idx = 1; idx < startValue.size(); idx+=2) {
        newValue[idx] = startValue[idx] + absTolHWP1[idx];
        expectedValue[idx] = startValue[idx];
    }
    qtVectorComplexPropertyManager->setValue(property, newValue);
    actualValue = qtVectorComplexPropertyManager->value(property);
    expectedValue = startValue;
    QCOMPARE(spy.count(), 0);
    QVERIFY(isclose(actualValue, expectedValue, absTolSW, relTolSW));

    for (int idx = 1; idx < startValue.size(); idx+=2) {
        newValue[idx] = startValue[idx] + absTolHWM1[idx];
        expectedValue[idx] = startValue[idx] + absTolHWM1[idx];
    }
    qtVectorComplexPropertyManager->setValue(property, newValue);
    actualValue = qtVectorComplexPropertyManager->value(property);
    QCOMPARE(spy.count(), 1);
    QVERIFY(isclose(actualValue, expectedValue, absTolHWM1, relTolHWM1));
}

QT_END_NAMESPACE
