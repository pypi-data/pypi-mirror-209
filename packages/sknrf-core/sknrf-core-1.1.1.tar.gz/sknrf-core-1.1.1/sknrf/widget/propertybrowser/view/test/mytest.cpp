#include <iostream>

#include <QtCore/QObject>
#include <QtWidgets/QApplication>
#include <QtWidgets/QLabel>
#include <QtWidgets/QCheckBox>
#include <QtTest>
#include <QtTest/QSignalSpy>

#include <qtpropertybrowserutils_p.h>
#include <qtpropertymanager.h>
#include <qteditorfactory.h>
#include <qttreepropertybrowser.h>
#include <qtgroupboxpropertybrowser.h>
#include <qtbuttonpropertybrowser.h>

#include "qtcustompropertybrowsertest.h"

//QTEST_MAIN(QtBoolPropertyManagerQtCheckBoxFactoryTest)
//https://alexhuszagh.github.io/2016/using-qttest-effectively/
int main(int argc, char *argv[])
{
    // Test Lambda
    int status = 0;
    auto runTest = [&status, argc, argv](QObject* obj) {
        status |= QTest::qExec(obj, argc, argv);
    };
    TESTLIB_SELFCOVERAGE_START(#QtAbstractManagerEditorTest)
    QT_PREPEND_NAMESPACE(QTest::Internal::callInitMain)<QtAbstractManagerEditorTest>();
    QTEST_MAIN_SETUP()
    QTEST_SET_MAIN_SOURCE_PATH

    // Run Multiple TestObjects
    runTest(new QtIntPropertyManagerQtIntEditFactoryTest);
    runTest(new QtIntPropertyManagerQtSpinBoxFactoryTest);
    runTest(new QtIntPropertyManagerQtSliderFactoryTest);
    runTest( new QtBoolPropertyManagerQtCheckBoxFactoryTest);
    runTest(new QtDoublePropertyManagerQtDoubleEditFactoryTest);
    runTest(new QtDoublePropertyManagerQtDoubleSpinBoxFactoryTest);
    runTest(new QtComplexPropertyManagerQtComplexEditFactoryTest);
    runTest(new QtQuaternionPropertyManagerQtQuaternionEditFactoryTest);
    runTest(new QtVectorComplexPropertyManagerQtVectorComplexEditFactoryTest);
    runTest(new QtStringPropertyManagerQtLineEditFactoryTest);
    runTest(new QtDatePropertyManagerQtDateEditFactoryTest);
    runTest(new QtTimePropertyManagerQtTimeEditFactoryTest);
    runTest(new QtDateTimePropertyManagerQtDateTimeEditFactoryTest);
    runTest(new QtKeySequencePropertyManagerQtKeySequenceEditorFactoryTest);
    runTest(new QtCharPropertyManagerQtCharEditorFactoryTest);
    runTest(new QtPointPropertyManagerQtPointEditorFactoryTest);
    runTest(new QtPointFPropertyManagerQtPointFEditorFactoryTest);
    runTest(new QtSizePropertyManagerQtSizeEditorFactoryTest);
    runTest(new QtSizeFPropertyManagerQtSizeFEditorFactoryTest);
    runTest(new QtRectPropertyManagerQtRectEditorFactoryTest);
    runTest(new QtRectFPropertyManagerQtRectFEditorFactoryTest);
    runTest(new QtEnumPropertyManagerQtEnumEditorFactoryTest);
    runTest(new QtFlagPropertyManagerQtFlagEditorFactoryTest);
    runTest(new QtLocalePropertyManagerQtLocaleEditorFactoryTest);
    runTest(new QtSizePolicyPropertyManagerQtSizePolicyEditorFactoryTest);
    runTest(new QtFontPropertyManagerQtFontEditorFactoryTest);
    runTest(new QtColorPropertyManagerQtColorEditorFactoryTest);
    runTest(new QtCursorPropertyManagerQtCursorEditorFactoryTest);
    runTest(new QtFilePropertyManagerQtFileEditorFactoryTest);
    return status;
}

