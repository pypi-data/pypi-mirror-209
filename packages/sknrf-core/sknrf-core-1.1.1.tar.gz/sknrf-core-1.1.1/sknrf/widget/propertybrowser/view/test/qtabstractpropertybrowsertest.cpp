//
// Created by dylan_bespalko on 3/14/23.
//
#include <string>

#include <QtCore/QObject>
#include <QtCore/QVector>
#include <QtGui/QBrush>
#include <QtWidgets/QDialog>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QScrollArea>
#include <QtWidgets/QLabel>
#include <QtWidgets/QSpinBox>
#include <QtWidgets/QCheckBox>
#include <QtTest>
#include <QtTest/QSignalSpy>

#include "qtabstractpropertybrowsertest.h"

namespace std
{
    string to_string(const QtComplex &__val) {
        return std::to_string(__val.real()) + " + 1j*" + std::to_string(__val.imag());
    }
}

QT_BEGIN_NAMESPACE

void QtAbstractManagerEditorTest::initPropertyBrowsers()
{
    model = new QtModel();
    dialog = new QDialog();
    layout = new QGridLayout();
    treeScrollArea = new QScrollArea();
    treePropertyBrowser = new QtTreePropertyBrowser();
    treePropertyBrowser->setAttributes(static_cast<BrowserCol>(int(BrowserCol::MINIMUM | BrowserCol::MAXIMUM | \
                                       BrowserCol::UNIT | BrowserCol::FORMAT | BrowserCol::CHECK)));
    boxScrollArea = new QScrollArea();
    boxPropertyBrowser = new QtGroupBoxPropertyBrowser();
    boxPropertyBrowser->setAttributes(static_cast<BrowserCol>(int(BrowserCol::MINIMUM | BrowserCol::MAXIMUM | \
                                      BrowserCol::UNIT | BrowserCol::FORMAT | BrowserCol::CHECK)));
    buttonScrollArea = new QScrollArea();
    buttonPropertyBrowser = new QtButtonPropertyBrowser();
    buttonPropertyBrowser->setAttributes(static_cast<BrowserCol>(int(BrowserCol::MINIMUM | BrowserCol::MAXIMUM | \
                                         BrowserCol::UNIT | BrowserCol::FORMAT | BrowserCol::CHECK)));

    groupPropertyManager = new QtGroupPropertyManager();
    qtIntPropertyManager = new QtIntPropertyManager();
    qtBoolPropertyManager = new QtBoolPropertyManager();
    qtDoublePropertyManager = new QtDoublePropertyManager();
    qtComplexPropertyManager = new QtComplexPropertyManager();
    qtQuaternionPropertyManager = new QtQuaternionPropertyManager();
    qtVectorComplexPropertyManager = new QtVectorComplexPropertyManager();
    qtStringPropertyManager = new QtStringPropertyManager();
    qtDatePropertyManager = new QtDatePropertyManager();
    qtTimePropertyManager = new QtTimePropertyManager();
    qtDateTimePropertyManager = new QtDateTimePropertyManager();
    qtKeySequencePropertyManager = new QtKeySequencePropertyManager();
    qtCharPropertyManager = new QtCharPropertyManager();
    qtPointPropertyManager = new QtPointPropertyManager();
    qtPointFPropertyManager = new QtPointFPropertyManager();
    qtSizePropertyManager = new QtSizePropertyManager();
    qtSizeFPropertyManager = new QtSizeFPropertyManager();
    qtRectPropertyManager = new QtRectPropertyManager();
    qtRectFPropertyManager = new QtRectFPropertyManager();
    qtEnumPropertyManager = new QtEnumPropertyManager();
    qtFlagPropertyManager = new QtFlagPropertyManager();
    qtLocalePropertyManager = new QtLocalePropertyManager();
    qtSizePolicyPropertyManager = new QtSizePolicyPropertyManager();
    qtFontPropertyManager = new QtFontPropertyManager();
    qtColorPropertyManager = new QtColorPropertyManager();
    qtCursorPropertyManager = new QtCursorPropertyManager();
    qtFilePropertyManager = new QtFilePropertyManager();

    groupEditorFactory = new QtGroupEditorFactory();
    spinBoxFactory = new QtSpinBoxFactory();
    intEditFactory = new QtIntEditFactory();
    sliderFactory = new QtSliderFactory();
    checkBoxFactory = new QtCheckBoxFactory();
    doubleEditFactory = new QtDoubleEditFactory();
    doubleSpinBoxFactory = new QtDoubleSpinBoxFactory();
    complexEditFactory = new QtComplexEditFactory();
    quaternionEditFactory = new QtQuaternionEditFactory();
    vectorComplexEditFactory = new QtVectorComplexEditFactory();
    lineEditFactory = new QtLineEditFactory();
    dateEditFactory = new QtDateEditFactory();
    timeEditFactory = new QtTimeEditFactory();
    dateTimeEditFactory = new QtDateTimeEditFactory();
    keySequenceEditorFactory = new QtKeySequenceEditorFactory();
    charEditorFactory = new QtCharEditorFactory();
    pointEditorFactory = new QtPointEditorFactory();
    pointFEditorFactory = new QtPointFEditorFactory();
    sizeEditorFactory = new QtSizeEditorFactory();
    sizeFEditorFactory = new QtSizeFEditorFactory();
    rectEditorFactory = new QtRectEditorFactory();
    rectFEditorFactory = new QtRectFEditorFactory();
    enumEditorFactory = new QtEnumEditorFactory();
    flagEditorFactory = new QtFlagEditorFactory();
    localeEditorFactory = new QtLocaleEditorFactory();
    sizePolicyEditorFactory = new QtSizePolicyEditorFactory();
    fontEditorFactory = new QtFontEditorFactory();
    colorEditorFactory = new QtColorEditorFactory();
    cursorEditorFactory = new QtCursorEditorFactory();
    fileEditorFactory = new QtFileEditorFactory();

    treePropertyBrowser->setFactoryForManager(groupPropertyManager, groupEditorFactory);
    boxPropertyBrowser->setFactoryForManager(groupPropertyManager, groupEditorFactory);
    buttonPropertyBrowser->setFactoryForManager(groupPropertyManager, groupEditorFactory);
}

void QtAbstractManagerEditorTest::addGroupProperty()
{
    groupProperty = groupPropertyManager->addProperty(("group" + std::to_string(count + 1)).c_str());
}

void QtAbstractManagerEditorTest::addProperty()
{
    property = qtBoolPropertyManager->addProperty(("bool_" + std::to_string(count + 1)).c_str());
    groupProperty->addSubProperty(property);
}

void QtAbstractManagerEditorTest::finalizePropertyBrowser()
{
    QtBrowserItem * browserItem;
    browserItem = treePropertyBrowser->addProperty(groupProperty);
    treePropertyBrowser->setExpanded(browserItem, true);
    browserItem = boxPropertyBrowser->addProperty(groupProperty);
    browserItem = buttonPropertyBrowser->addProperty(groupProperty);
    buttonPropertyBrowser->setExpanded(browserItem, true);

    treeScrollArea->setSizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);
    treeScrollArea->setWidgetResizable(true);
    treeScrollArea->setWidget(treePropertyBrowser);
    layout->addWidget(new QLabel("Tree Browser", dialog), 0, 0);
    layout->addWidget(treeScrollArea, 1, 0);

    boxScrollArea->setSizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);
    boxScrollArea->setWidgetResizable(true);
    boxScrollArea->setWidget(boxPropertyBrowser);
    layout->addWidget(new QLabel("Box Browser", dialog), 0, 1);
    layout->addWidget(boxScrollArea, 1, 1);

    buttonScrollArea->setSizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);
    buttonScrollArea->setWidgetResizable(true);
    buttonScrollArea->setWidget(buttonPropertyBrowser);
    layout->addWidget(new QLabel("Button Browser", dialog), 0, 2);
    layout->addWidget(buttonScrollArea, 1, 2);

    dialog->setLayout(layout);
    dialog->showMaximized();
}

void QtAbstractManagerEditorTest::initTestCase()
{
    initPropertyBrowsers();
    addGroupProperty();
    addProperty();
    finalizePropertyBrowser();
}

QT_END_NAMESPACE
