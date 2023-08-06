//
// Created by dylan_bespalko on 3/9/23.
//
#include <iostream>
#include <string>

#include <Qt>
#include <QtCore>
#include <QtCore/QObject>
#include <QtCore/QFlag>
#include <QtCore/QDate>
#include <QtCore/QDateTime>
#include <QtCore/QTime>
#include <QtCore/QLocale>
#include <QtCore/QPoint>
#include <QtCore/QPointF>
#include <QtCore/QSize>
#include <QtCore/QSizeF>
#include <QtCore/QRect>
#include <QtCore/QRectF>
#include <QtGui/QCursor>
#include <QtGui/QColor>
#include <QtGui/QFont>
#include <QtGui/QKeySequence>
#include <QtWidgets/QSizePolicy>
#include <QtWidgets/QApplication>
#include <QtWidgets/QDialog>
#include <QtWidgets/QLabel>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QScrollArea>

#include "qtpropertybrowserutils_p.h"
#include "qtpropertymanager.h"
#include "qteditorfactory.h"
#include "qttreepropertybrowser.h"
#include "qtgroupboxpropertybrowser.h"
#include "qtbuttonpropertybrowser.h"



class TestEnums : QObject
{
Q_OBJECT
public:
    enum Color {
        BLACK = 0,
        RED   = 1,
        GREEN = 2,
        BLUE  = 3
    };
    Q_ENUM(Color)
};


class TestFlags : QObject
{
Q_OBJECT
public:
    enum Color_ {
        BLACK = 0x0,
        RED = 0x1,
        YELLOW = 0x2,
        BLUE = 0x4,
        GREEN = YELLOW | BLUE,
        ORANGE = RED | YELLOW,
        PURPLE = RED | BLUE,
        WHITE = RED | YELLOW | BLUE
    };
    Q_DECLARE_FLAGS(Color, Color_)
};

Q_DECLARE_OPERATORS_FOR_FLAGS(TestFlags::Color)

#define INT_MIN_INIT_VECTOR -2
#define INT_MAX_TEST_VECTOR -1
#define INT_INIT_VECTOR 0
#define INT_TEST_VECTOR 1
#define INT_MIN_TEST_VECTOR 1
#define INT_MAX_INIT_VECTOR 2
#define DOUBLE_PRECISION 16
#define DOUBLE_MIN_INIT_VECTOR -1.500
#define DOUBLE_MAX_TEST_VECTOR -0.500
#define DOUBLE_INIT_VECTOR 0.000
#define DOUBLE_TEST_VECTOR 0.250
#define DOUBLE_MIN_TEST_VECTOR 0.500
#define DOUBLE_MAX_INIT_VECTOR 1.500
#define COMPLEX_PRECISION 16
#define COMPLEX_MIN_INIT_VECTOR 0.50
#define COMPLEX_MAX_TEST_VECTOR 1.50
#define COMPLEX_INIT_VECTOR 1.250, 1.250
#define COMPLEX_TEST_VECTOR 1.414, 1.414
#define COMPLEX_MIN_TEST_VECTOR 2.50
#define COMPLEX_MAX_INIT_VECTOR 3.50
#define QUATERNION_PRECISION 16
#define QUATERNION_MIN_INIT_VECTOR 0.50
#define QUATERNION_MAX_TEST_VECTOR 1.50
#define QUATERNION_INIT_VECTOR 0.8, 0.8, 0.8, 0.8
#define QUATERNION_TEST_VECTOR 1.0, 1.0, 1.0, 1.0
#define QUATERNION_MIN_TEST_VECTOR 2.50
#define QUATERNION_MAX_INIT_VECTOR 3.50
#define VECTOR_SIZE 3
#define STR_INIT_VECTOR ""
#define STR_TEST_VECTOR "b"
#define DATE_INIT_VECTOR 1983, 10, 03
#define DATE_TEST_VECTOR 1984, 10, 04
#define TIME_INIT_VECTOR 0, 0, 0
#define TIME_TEST_VECTOR 6, 3, 0
#define DATETIME_INIT_VECTOR QDate(DATE_INIT_VECTOR), QTime(TIME_INIT_VECTOR)
#define DATETIME_TEST_VECTOR QDate(DATE_TEST_VECTOR), QTime(TIME_TEST_VECTOR)
#define KEY_INIT_VECTOR "CTRL+A"
#define KEY_TEST_VECTOR "ALT+Y"
#define CHAR_INIT_VECTOR 'A'
#define CHAR_TEST_VECTOR 'b'
#define POINT_INIT_VECTOR 0, 0
#define POINT_TEST_VECTOR 1, 1
#define POINTF_MIN_INIT_VECTOR DOUBLE_MIN_INIT_VECTOR, DOUBLE_MIN_INIT_VECTOR
#define POINTF_INIT_VECTOR 0.000, 0.000
#define POINTF_TEST_VECTOR 0.250, 0.250
#define POINTF_MAX_INIT_VECTOR DOUBLE_MAX_INIT_VECTOR, DOUBLE_MAX_INIT_VECTOR
#define SIZE_INIT_VECTOR 0, 0
#define SIZE_TEST_VECTOR 1, 1
#define SIZEF_MIN_INIT_VECTOR DOUBLE_MIN_INIT_VECTOR, DOUBLE_MIN_INIT_VECTOR
#define SIZEF_INIT_VECTOR 0.000, 0.000
#define SIZEF_TEST_VECTOR 0.250, 0.250
#define SIZEF_MAX_INIT_VECTOR DOUBLE_MAX_INIT_VECTOR, DOUBLE_MAX_INIT_VECTOR
#define RECT_INIT_VECTOR 0, 0, 0, 0
#define RECT_TEST_VECTOR 1, 1, 1, 1
#define RECTF_CONST_INIT_VECTOR 0.000, 0.000, 0.500, 0.500
#define RECTF_INIT_VECTOR 0.00, 0.00, 0.00, 0.00
#define RECTF_TEST_VECTOR 0.250, 0.250, 0.250, 0.250
#define ENUM_INIT_VECTOR TestEnums::RED
#define ENUM_TEST_VECTOR TestEnums::BLUE
#define FLAG_INIT_VECTOR TestFlags::BLACK
#define FLAG_TEST_VECTOR TestFlags::WHITE
#define LANGUAGE_LOCALE_INIT_VECTOR QLocale::English
#define LANGUAGE_LOCALE_TEST_VECTOR QLocale::Arabic
#define TERRITORY_LOCALE_INIT_VECTOR QLocale::Canada
#define TERRITORY_LOCALE_TEST_VECTOR QLocale::Egypt
#define LOCALE_INIT_VECTOR QLocale::English, QLocale::Canada
#define LOCALE_TEST_VECTOR QLocale::Arabic, QLocale::Egypt
#define X_SIZE_POLICY_INIT_VECTOR QSizePolicy::Fixed
#define X_SIZE_POLICY_TEST_VECTOR QSizePolicy::Expanding
#define Y_SIZE_POLICY_INIT_VECTOR QSizePolicy::Fixed
#define Y_SIZE_POLICY_TEST_VECTOR QSizePolicy::MinimumExpanding
#define X_STRETCH_SIZE_POLICY_INIT_VECTOR 1
#define X_STRETCH_SIZE_POLICY_TEST_VECTOR 0
#define Y_STRETCH_SIZE_POLICY_INIT_VECTOR 1
#define Y_STRETCH_SIZE_POLICY_TEST_VECTOR 0
#define SIZE_POLICY_INIT_VECTOR QSizePolicy::Fixed, QSizePolicy::Fixed
#define SIZE_POLICY_TEST_VECTOR QSizePolicy::Expanding, QSizePolicy::MinimumExpanding
#define FONT_INIT_VECTOR "Arial"
#define FONT_TEST_VECTOR "Georgia"
#define COLOR_INIT_VECTOR "black"
#define COLOR_TEST_VECTOR "white"
#define CURSOR_INIT_VECTOR Qt::IBeamCursor
#define CURSOR_TEST_VECTOR Qt::ArrowCursor
#define FILE_INIT_VECTOR "/etc/resolv.conf"
#define FILE_TEST_VECTOR "/etc/hosts"


class QtModel : public QObject
{
Q_OBJECT

Q_SIGNALS:
    void valueChanged(QtProperty *property, int val);
    void valueChanged(QtProperty *property, bool val);
    void valueChanged(QtProperty *property, double val);
    void valueChanged(QtProperty *property, const QtComplex &val);
    void valueChanged(QtProperty *property, const QtQuaternion& val);
    void valueChanged(QtProperty *property, const QVector<QtComplex> &val);
    void valueChanged(QtProperty *property, const QString &val);
    void valueChanged(QtProperty *property, QDate val);
    void valueChanged(QtProperty *property, QTime val);
    void valueChanged(QtProperty *property, QDateTime val);
    void valueChanged(QtProperty *property, const QKeySequence &val);
    void valueChanged(QtProperty *property, const QChar &val);
    void valueChanged(QtProperty *property, const QLocale &val);
    void valueChanged(QtProperty *property, const QPoint &val);
    void valueChanged(QtProperty *property, const QPointF &val);
    void valueChanged(QtProperty *property, const QSize &val);
    void valueChanged(QtProperty *property, const QSizeF &val);
    void valueChanged(QtProperty *property, const QRect &val);
    void valueChanged(QtProperty *property, const QRectF &val);
    void valueChanged(QtProperty *property, const QSizePolicy &val);
    void valueChanged(QtProperty *property, const QFont &val);
    void valueChanged(QtProperty *property, const QColor &val);
    void valueChanged(QtProperty *property, const QCursor &val);

public:
    inline double atol() {return m_atol;};
    inline void setAtol(double atol) {m_atol = atol;};

public Q_SLOTS:
    inline void setValue(QtProperty *property, int val) {emit valueChanged(property, val);};
    inline void setValue(QtProperty *property, bool val) {emit valueChanged(property, val);};
    inline void setValue(QtProperty *property, double val) {emit valueChanged(property, val + atol());};
    inline void setValue(QtProperty *property, const QtComplex& val) {emit valueChanged(property, val + atol());};
    inline void setValue(QtProperty *property, const QtQuaternion& val) {emit valueChanged(property, val + QtQuaternion(atol()));};
    inline void setValue(QtProperty *property, const QVector<QtComplex>& val) {emit valueChanged(property, val);};
    inline void setValue(QtProperty *property, const QString &val) {emit valueChanged(property, val);};
    inline void setValue(QtProperty *property, QDate val) {emit valueChanged(property, val);};
    inline void setValue(QtProperty *property, QTime val) {emit valueChanged(property, val);};
    inline void setValue(QtProperty *property, QDateTime val) {emit valueChanged(property, val);};
    inline void setValue(QtProperty *property, const QKeySequence &val) {emit valueChanged(property, val);};
    inline void setValue(QtProperty *property, const QChar &val) {emit valueChanged(property, val);};
    inline void setValue(QtProperty *property, const QLocale &val) {emit valueChanged(property, val);};
    inline void setValue(QtProperty *property, const QPoint &val) {emit valueChanged(property, val);};
    inline void setValue(QtProperty *property, const QPointF &val) {emit valueChanged(property, val + QPointF(atol(), atol())) ;};
    inline void setValue(QtProperty *property, const QSize &val) {emit valueChanged(property, val);};
    inline void setValue(QtProperty *property, const QSizeF &val) {emit valueChanged(property, val + QSizeF(atol(), atol()));};
    inline void setValue(QtProperty *property, const QRect &val) {emit valueChanged(property, val);};
    inline void setValue(QtProperty *property, const QRectF &val) {emit valueChanged(property, val);};
    inline void setValue(QtProperty *property, const QSizePolicy &val) {emit valueChanged(property, val);};
    inline void setValue(QtProperty *property, const QFont &val) {emit valueChanged(property, val);};
    inline void setValue(QtProperty *property, const QColor &val) {emit valueChanged(property, val);};
    inline void setValue(QtProperty *property, const QCursor &val) {emit valueChanged(property, val);};
    inline void setCheck(QtProperty *property, bool check) {
//        std::clog << "INFO   : " << property->propertyName().toStdString() << std::endl;
    };

private:
    double m_atol = 0.0;
};


int main(int argc, char **argv)
{

    int count = 0;
    auto app = QApplication(argc, argv);
    auto *model = new QtModel();
    auto *dialog = new QDialog();
    auto *layout = new QGridLayout();
    auto *treeScrollArea = new QScrollArea();
    auto *treePropertyBrowser = new QtTreePropertyBrowser();
    treePropertyBrowser->setAttributes(
        static_cast<BrowserCol>(int(BrowserCol::MINIMUM | BrowserCol::MAXIMUM | BrowserCol::UNIT | BrowserCol::FORMAT | BrowserCol::CHECK)));
    auto *boxScrollArea = new QScrollArea();
    auto *boxPropertyBrowser = new QtGroupBoxPropertyBrowser();
    boxPropertyBrowser->setAttributes(
        static_cast<BrowserCol>(int(BrowserCol::MINIMUM | BrowserCol::MAXIMUM | BrowserCol::UNIT | BrowserCol::FORMAT | BrowserCol::CHECK)));
    auto *buttonScrollArea = new QScrollArea();
    auto *buttonPropertyBrowser = new QtButtonPropertyBrowser();
    buttonPropertyBrowser->setAttributes(
        static_cast<BrowserCol>(int(BrowserCol::MINIMUM | BrowserCol::MAXIMUM | BrowserCol::UNIT | BrowserCol::FORMAT | BrowserCol::CHECK)));

    auto *groupPropertyManager = new QtGroupPropertyManager();
    auto *qtIntPropertyManager = new QtIntPropertyManager();
    auto *qtBoolPropertyManager = new QtBoolPropertyManager();
    auto *qtDoublePropertyManager = new QtDoublePropertyManager();
    auto *qtComplexPropertyManager = new QtComplexPropertyManager();
    auto *qtQuaternionPropertyManager = new QtQuaternionPropertyManager();
    auto *qtVectorComplexPropertyManager = new QtVectorComplexPropertyManager();
    auto *qtStringPropertyManager = new QtStringPropertyManager();
    auto *qtDatePropertyManager = new QtDatePropertyManager();
    auto *qtTimePropertyManager = new QtTimePropertyManager();
    auto *qtDateTimePropertyManager = new QtDateTimePropertyManager();
    auto *qtKeySequencePropertyManager = new QtKeySequencePropertyManager();
    auto *qtCharPropertyManager = new QtCharPropertyManager();
    auto *qtPointPropertyManager = new QtPointPropertyManager();
    auto *qtPointFPropertyManager = new QtPointFPropertyManager();
    auto *qtSizePropertyManager = new QtSizePropertyManager();
    auto *qtSizeFPropertyManager = new QtSizeFPropertyManager();
    auto *qtRectPropertyManager = new QtRectPropertyManager();
    auto *qtRectFPropertyManager = new QtRectFPropertyManager();
    auto *qtEnumPropertyManager = new QtEnumPropertyManager();
    auto *qtFlagPropertyManager = new QtFlagPropertyManager();
    auto *qtLocalePropertyManager = new QtLocalePropertyManager();
    auto *qtSizePolicyPropertyManager = new QtSizePolicyPropertyManager();
    auto *qtFontPropertyManager = new QtFontPropertyManager();
    auto *qtColorPropertyManager = new QtColorPropertyManager();
    auto *qtCursorPropertyManager = new QtCursorPropertyManager();
    auto *qtFilePropertyManager = new QtFilePropertyManager();

    auto *groupEditorFactory = new QtGroupEditorFactory();
    auto *spinBoxFactory = new QtSpinBoxFactory();
    auto *intEditFactory = new QtIntEditFactory();
    auto *sliderFactory = new QtSliderFactory();
    auto *checkBoxFactory = new QtCheckBoxFactory();
    auto *doubleEditFactory = new QtDoubleEditFactory();
    auto *doubleSpinBoxFactory = new QtDoubleSpinBoxFactory();
    auto *complexEditFactory = new QtComplexEditFactory();
    auto *quaternionEditFactory = new QtQuaternionEditFactory();
    auto *vectorComplexEditFactory = new QtVectorComplexEditFactory();
    auto *lineEditFactory = new QtLineEditFactory();
    auto *dateEditFactory = new QtDateEditFactory();
    auto *timeEditFactory = new QtTimeEditFactory();
    auto *dateTimeEditFactory = new QtDateTimeEditFactory();
    auto *keySequenceEditorFactory = new QtKeySequenceEditorFactory();
    auto *charEditorFactory = new QtCharEditorFactory();
    auto *pointEditorFactory = new QtPointEditorFactory();
    auto *pointFEditorFactory = new QtPointFEditorFactory();
    auto *sizeEditorFactory = new QtSizeEditorFactory();
    auto *sizeFEditorFactory = new QtSizeFEditorFactory();
    auto *rectEditorFactory = new QtRectEditorFactory();
    auto *rectFEditorFactory = new QtRectFEditorFactory();
    auto *enumEditorFactory = new QtEnumEditorFactory();
    auto *flagEditorFactory = new QtFlagEditorFactory();
    auto *localeEditorFactory = new QtLocaleEditorFactory();
    auto *sizePolicyEditorFactory = new QtSizePolicyEditorFactory();
    auto *fontEditorFactory = new QtFontEditorFactory();
    auto *colorEditorFactory = new QtColorEditorFactory();
    auto *cursorEditorFactory = new QtCursorEditorFactory();
    auto *fileEditorFactory = new QtFileEditorFactory();
    QtProperty *property;

    treePropertyBrowser->setFactoryForManager(groupPropertyManager, groupEditorFactory);
    boxPropertyBrowser->setFactoryForManager(groupPropertyManager, groupEditorFactory);
    buttonPropertyBrowser->setFactoryForManager(groupPropertyManager, groupEditorFactory);

    // Group
    auto *groupProperty = groupPropertyManager->addProperty(("group" + std::to_string(count + 1)).c_str());

    // QtIntPropertyManager/IntEditFactory
//    treePropertyBrowser->setFactoryForManager(qtIntPropertyManager, intEditFactory);
//    boxPropertyBrowser->setFactoryForManager(qtIntPropertyManager, intEditFactory);
//    buttonPropertyBrowser->setFactoryForManager(qtIntPropertyManager, intEditFactory);
//    QObject::connect(qtIntPropertyManager, SIGNAL(valueChanged(QtProperty *, int) ), model, SLOT(setValue(QtProperty *, int) ) );
//    QObject::connect(model, SIGNAL(valueChanged(QtProperty *, int) ), qtIntPropertyManager, SLOT(setValue(QtProperty *, int) ) );
//    QObject::connect(qtIntPropertyManager, SIGNAL(checkChanged(QtProperty *, bool) ), model, SLOT(setCheck(QtProperty *, bool) ) );
//    property = qtIntPropertyManager->addProperty(("int_" + std::to_string(count + 1)).c_str());
//    groupProperty->addSubProperty(property);
//    qtIntPropertyManager->setMinimum(property, INT_MIN_INIT_VECTOR);
//    qtIntPropertyManager->setMaximum(property, INT_MAX_INIT_VECTOR);
//    qtIntPropertyManager->setValue(property, INT_INIT_VECTOR);
//    qtIntPropertyManager->setCheck(property, false);

    // QtIntPropertyManager/SpinBoxFactory
    treePropertyBrowser->setFactoryForManager(qtIntPropertyManager, spinBoxFactory);
    boxPropertyBrowser->setFactoryForManager(qtIntPropertyManager, spinBoxFactory);
    buttonPropertyBrowser->setFactoryForManager(qtIntPropertyManager, spinBoxFactory);
    QObject::connect(qtIntPropertyManager, SIGNAL(valueChanged(QtProperty *, int) ), model, SLOT(setValue(QtProperty *, int) ) );
    QObject::connect(model, SIGNAL(valueChanged(QtProperty *, int) ), qtIntPropertyManager, SLOT(setValue(QtProperty *, int) ) );
    QObject::connect(qtIntPropertyManager, SIGNAL(checkChanged(QtProperty *, bool) ), model, SLOT(setCheck(QtProperty *, bool) ) );
    property = qtIntPropertyManager->addProperty(("int_" + std::to_string(count + 1)).c_str());
    groupProperty->addSubProperty(property);
    qtIntPropertyManager->setMinimum(property, INT_MIN_INIT_VECTOR);
    qtIntPropertyManager->setMaximum(property, INT_MAX_INIT_VECTOR);
    qtIntPropertyManager->setValue(property, INT_INIT_VECTOR);
    qtIntPropertyManager->setCheck(property, false);

    // QtIntPropertyManager/SliderFactory
//    treePropertyBrowser->setFactoryForManager(qtIntPropertyManager, sliderFactory);
//    boxPropertyBrowser->setFactoryForManager(qtIntPropertyManager, sliderFactory);
//    buttonPropertyBrowser->setFactoryForManager(qtIntPropertyManager, sliderFactory);
//    QObject::connect(qtIntPropertyManager, SIGNAL(valueChanged(QtProperty *, int) ), model, SLOT(setValue(QtProperty *, int) ) );
//    QObject::connect(model, SIGNAL(valueChanged(QtProperty *, int) ), qtIntPropertyManager, SLOT(setValue(QtProperty *, int) ) );
//    QObject::connect(qtIntPropertyManager, SIGNAL(checkChanged(QtProperty *, bool) ), model, SLOT(setCheck(QtProperty *, bool) ) );
//    property = qtIntPropertyManager->addProperty(("int_" + std::to_string(count + 1)).c_str());
//    groupProperty->addSubProperty(property);
//    qtIntPropertyManager->setMinimum(property, INT_MIN_INIT_VECTOR);
//    qtIntPropertyManager->setMaximum(property, INT_MAX_INIT_VECTOR);
//    qtIntPropertyManager->setValue(property, INT_INIT_VECTOR);
//    qtIntPropertyManager->setCheck(property, false);

    // QtBoolPropertyManager/CheckBoxFactory
    treePropertyBrowser->setFactoryForManager(qtBoolPropertyManager, checkBoxFactory);
    boxPropertyBrowser->setFactoryForManager(qtBoolPropertyManager, checkBoxFactory);
    buttonPropertyBrowser->setFactoryForManager(qtBoolPropertyManager, checkBoxFactory);
    QObject::connect(qtBoolPropertyManager, SIGNAL(valueChanged(QtProperty *, bool) ), model, SLOT(setValue(QtProperty *, bool) ) );
    QObject::connect(model, SIGNAL(valueChanged(QtProperty *, bool) ), qtBoolPropertyManager, SLOT(setValue(QtProperty *, bool) ) );
    QObject::connect(qtBoolPropertyManager, SIGNAL(checkChanged(QtProperty *, bool) ), model, SLOT(setCheck(QtProperty *, bool) ) );
    property = qtBoolPropertyManager->addProperty(("bool_" + std::to_string(count + 1)).c_str());
    groupProperty->addSubProperty(property);
    qtBoolPropertyManager->setValue(property, false);
    qtBoolPropertyManager->setCheck(property, false);

    // QtDoublePropertyManager/DoubleEditFactory
//    treePropertyBrowser->setFactoryForManager(qtDoublePropertyManager, doubleEditFactory);
//    boxPropertyBrowser->setFactoryForManager(qtDoublePropertyManager, doubleEditFactory);
//    buttonPropertyBrowser->setFactoryForManager(qtDoublePropertyManager, doubleEditFactory);
//    QObject::connect(qtDoublePropertyManager, SIGNAL(valueChanged(QtProperty *, double) ), model, SLOT(setValue(QtProperty *, double) ) );
//    QObject::connect(model, SIGNAL(valueChanged(QtProperty *, double) ), qtDoublePropertyManager, SLOT(setValue(QtProperty *, double) ) );
//    QObject::connect(qtDoublePropertyManager, SIGNAL(checkChanged(QtProperty *, bool) ), model, SLOT(setCheck(QtProperty *, bool) ) );
//    property = qtDoublePropertyManager->addProperty(("double_" + std::to_string(count + 1)).c_str());
//    groupProperty->addSubProperty(property);
//    qtDoublePropertyManager->setMinimum(property, DOUBLE_MIN_INIT_VECTOR);
//    qtDoublePropertyManager->setMaximum(property, DOUBLE_MAX_INIT_VECTOR);
//    qtDoublePropertyManager->setPrecision(property, DOUBLE_PRECISION);
//    qtDoublePropertyManager->setValue(property, DOUBLE_INIT_VECTOR);
//    qtDoublePropertyManager->setCheck(property, false);

    // QtDoublePropertyManager/DoubleSpinBoxFactory
    treePropertyBrowser->setFactoryForManager(qtDoublePropertyManager, doubleSpinBoxFactory);
    boxPropertyBrowser->setFactoryForManager(qtDoublePropertyManager, doubleSpinBoxFactory);
    buttonPropertyBrowser->setFactoryForManager(qtDoublePropertyManager, doubleSpinBoxFactory);
    QObject::connect(qtDoublePropertyManager, SIGNAL(valueChanged(QtProperty *, double) ), model, SLOT(setValue(QtProperty *, double) ) );
    QObject::connect(model, SIGNAL(valueChanged(QtProperty *, double) ), qtDoublePropertyManager, SLOT(setValue(QtProperty *, double) ) );
    QObject::connect(qtDoublePropertyManager, SIGNAL(checkChanged(QtProperty *, bool) ), model, SLOT(setCheck(QtProperty *, bool) ) );
    property = qtDoublePropertyManager->addProperty(("double_" + std::to_string(count + 1)).c_str());
    groupProperty->addSubProperty(property);
    qtDoublePropertyManager->setMinimum(property, DOUBLE_MIN_INIT_VECTOR);
    qtDoublePropertyManager->setMaximum(property, DOUBLE_MAX_INIT_VECTOR);
    qtDoublePropertyManager->setPrecision(property, DOUBLE_PRECISION);
    qtDoublePropertyManager->setValue(property, DOUBLE_INIT_VECTOR);
    qtDoublePropertyManager->setCheck(property, false);

    // QtComplexPropertyManager/ComplexEditFactory
    treePropertyBrowser->setFactoryForManager(qtComplexPropertyManager, complexEditFactory);
    boxPropertyBrowser->setFactoryForManager(qtComplexPropertyManager, complexEditFactory);
    buttonPropertyBrowser->setFactoryForManager(qtComplexPropertyManager, complexEditFactory);
    QObject::connect(qtComplexPropertyManager, SIGNAL(valueChanged(QtProperty *, const QtComplex &) ), model, SLOT(setValue(QtProperty *, const QtComplex &) ) );
    QObject::connect(model, SIGNAL(valueChanged(QtProperty *, const QtComplex &) ), qtComplexPropertyManager, SLOT(setValue(QtProperty *, const QtComplex &) ) );
    QObject::connect(qtComplexPropertyManager, SIGNAL(checkChanged(QtProperty *, bool) ), model, SLOT(setCheck(QtProperty *, bool) ) );
    property = qtComplexPropertyManager->addProperty(("QtComplex_" + std::to_string(count + 1)).c_str());
    groupProperty->addSubProperty(property);
    qtComplexPropertyManager->setPrecision(property, COMPLEX_PRECISION);
    qtComplexPropertyManager->setMinimum(property, COMPLEX_MIN_INIT_VECTOR);
    qtComplexPropertyManager->setMaximum(property, COMPLEX_MAX_INIT_VECTOR);
    qtComplexPropertyManager->setValue(property, QtComplex(COMPLEX_INIT_VECTOR));
    qtComplexPropertyManager->setCheck(property, false);

    // QtQuaternionPropertyManager/QuaternionEditFactory
    treePropertyBrowser->setFactoryForManager(qtQuaternionPropertyManager, quaternionEditFactory);
    boxPropertyBrowser->setFactoryForManager(qtQuaternionPropertyManager, quaternionEditFactory);
    buttonPropertyBrowser->setFactoryForManager(qtQuaternionPropertyManager, quaternionEditFactory);
    QObject::connect(qtQuaternionPropertyManager, SIGNAL(valueChanged(QtProperty *, const QtQuaternion &) ), model, SLOT(setValue(QtProperty *, const QtQuaternion &) ) );
    QObject::connect(model, SIGNAL(valueChanged(QtProperty *, const QtQuaternion &) ), qtQuaternionPropertyManager, SLOT(setValue(QtProperty *, const QtQuaternion &) ) );
    QObject::connect(qtQuaternionPropertyManager, SIGNAL(checkChanged(QtProperty *, bool) ), model, SLOT(setCheck(QtProperty *, bool) ) );
    property = qtQuaternionPropertyManager->addProperty(("Quaternion_" + std::to_string(count + 1)).c_str());
    groupProperty->addSubProperty(property);
    qtQuaternionPropertyManager->setPrecision(property, QUATERNION_PRECISION);
    qtQuaternionPropertyManager->setMinimum(property, QtQuaternion(QUATERNION_MIN_INIT_VECTOR));
    qtQuaternionPropertyManager->setMaximum(property, QtQuaternion(QUATERNION_MAX_INIT_VECTOR));
    qtQuaternionPropertyManager->setValue(property, QtQuaternion(QUATERNION_INIT_VECTOR));
    qtQuaternionPropertyManager->setCheck(property, false);

    // QtVectorComplexPropertyManager/vectorComplexEditFactory
    vectorComplexEditFactory->setSubFactory(complexEditFactory);
    treePropertyBrowser->setFactoryForManager(qtVectorComplexPropertyManager, vectorComplexEditFactory);
    boxPropertyBrowser->setFactoryForManager(qtVectorComplexPropertyManager, vectorComplexEditFactory);
    buttonPropertyBrowser->setFactoryForManager(qtVectorComplexPropertyManager, vectorComplexEditFactory);
    treePropertyBrowser->setFactoryForManager(qtVectorComplexPropertyManager->subComplexPropertyManager(),complexEditFactory);
    boxPropertyBrowser->setFactoryForManager(qtVectorComplexPropertyManager->subComplexPropertyManager(), complexEditFactory);
    buttonPropertyBrowser->setFactoryForManager(qtVectorComplexPropertyManager->subComplexPropertyManager(), complexEditFactory);
    QObject::connect(qtVectorComplexPropertyManager, SIGNAL(valueChanged(QtProperty *, const QVector<QtComplex> &) ), model, SLOT(setValue(QtProperty *, const QVector<QtComplex> &) ) );
    QObject::connect(model, SIGNAL(valueChanged(QtProperty *, const QVector<QtComplex> &) ), qtVectorComplexPropertyManager, SLOT(setValue(QtProperty *, const QVector<QtComplex> &) ) );
    QObject::connect(qtVectorComplexPropertyManager, SIGNAL(checkChanged(QtProperty *, bool) ), model, SLOT(setCheck(QtProperty *, bool) ) );
    property = qtVectorComplexPropertyManager->addProperty(("QVector<QtComplex>_" + std::to_string(count + 1)).c_str());
    groupProperty->addSubProperty(property);
    qtVectorComplexPropertyManager->setSize(property, VECTOR_SIZE);
    qtVectorComplexPropertyManager->setPrecision(property, COMPLEX_PRECISION);
    qtVectorComplexPropertyManager->setMinimum(property, QVector<QtComplex>(VECTOR_SIZE, QtComplex(COMPLEX_MIN_INIT_VECTOR)));
    qtVectorComplexPropertyManager->setMaximum(property, QVector<QtComplex>(VECTOR_SIZE, QtComplex(COMPLEX_MAX_INIT_VECTOR)));
    qtVectorComplexPropertyManager->setValue(property, QVector<QtComplex>(VECTOR_SIZE, {COMPLEX_INIT_VECTOR}));
    qtVectorComplexPropertyManager->setCheck(property, false);

    // QtStringPropertyManager/LineEditFactory
    treePropertyBrowser->setFactoryForManager(qtStringPropertyManager, lineEditFactory);
    boxPropertyBrowser->setFactoryForManager(qtStringPropertyManager, lineEditFactory);
    buttonPropertyBrowser->setFactoryForManager(qtStringPropertyManager, lineEditFactory);
    QObject::connect(qtStringPropertyManager, SIGNAL(valueChanged(QtProperty *, const QString &) ), model, SLOT(setValue(QtProperty *, const QString &) ) );
    QObject::connect(model, SIGNAL(valueChanged(QtProperty *, const QString &) ), qtStringPropertyManager, SLOT(setValue(QtProperty *, const QString &) ) );
    QObject::connect(qtStringPropertyManager, SIGNAL(checkChanged(QtProperty *, bool) ), model, SLOT(setCheck(QtProperty *, bool) ) );
    property = qtStringPropertyManager->addProperty(("QString_" + std::to_string(count + 1)).c_str());
    groupProperty->addSubProperty(property);
    qtStringPropertyManager->setValue(property, STR_INIT_VECTOR);
    qtStringPropertyManager->setCheck(property, false);

    // QtDatePropertyManager/DateEditFactory
    treePropertyBrowser->setFactoryForManager(qtDatePropertyManager, dateEditFactory);
    boxPropertyBrowser->setFactoryForManager(qtDatePropertyManager, dateEditFactory);
    buttonPropertyBrowser->setFactoryForManager(qtDatePropertyManager, dateEditFactory);
    QObject::connect(qtDatePropertyManager, SIGNAL(valueChanged(QtProperty *, QDate) ), model, SLOT(setValue(QtProperty *, QDate) ) );
    QObject::connect(model, SIGNAL(valueChanged(QtProperty *, QDate) ), qtDatePropertyManager, SLOT(setValue(QtProperty *, QDate) ) );
    QObject::connect(qtDatePropertyManager, SIGNAL(checkChanged(QtProperty *, bool) ), model, SLOT(setCheck(QtProperty *, bool) ) );
    property = qtDatePropertyManager->addProperty(("QDate_" + std::to_string(count + 1)).c_str());
    groupProperty->addSubProperty(property);
    qtDatePropertyManager->setValue(property, QDate(DATE_INIT_VECTOR));
    qtDatePropertyManager->setCheck(property, false);

    // QtTimePropertyManager/TimeEditFactory
    treePropertyBrowser->setFactoryForManager(qtTimePropertyManager, timeEditFactory);
    boxPropertyBrowser->setFactoryForManager(qtTimePropertyManager, timeEditFactory);
    buttonPropertyBrowser->setFactoryForManager(qtTimePropertyManager, timeEditFactory);
    QObject::connect(qtTimePropertyManager, SIGNAL(valueChanged(QtProperty *, QTime) ), model, SLOT(setValue(QtProperty *, QTime) ) );
    QObject::connect(model, SIGNAL(valueChanged(QtProperty *, QTime) ), qtTimePropertyManager, SLOT(setValue(QtProperty *, QTime) ) );
    QObject::connect(qtTimePropertyManager, SIGNAL(checkChanged(QtProperty *, bool) ), model, SLOT(setCheck(QtProperty *, bool) ) );
    property = qtTimePropertyManager->addProperty(("QTime_" + std::to_string(count + 1)).c_str());
    groupProperty->addSubProperty(property);
    qtTimePropertyManager->setValue(property, QTime(TIME_INIT_VECTOR));
    qtTimePropertyManager->setCheck(property, false);

    // QtDateTimePropertyManager/DateTimeEditFactory
    treePropertyBrowser->setFactoryForManager(qtDateTimePropertyManager, dateTimeEditFactory);
    boxPropertyBrowser->setFactoryForManager(qtDateTimePropertyManager, dateTimeEditFactory);
    buttonPropertyBrowser->setFactoryForManager(qtDateTimePropertyManager, dateTimeEditFactory);
    QObject::connect(qtDateTimePropertyManager, SIGNAL(valueChanged(QtProperty *, QDateTime) ), model, SLOT(setValue(QtProperty *, QDateTime) ) );
    QObject::connect(model, SIGNAL(valueChanged(QtProperty *, QDateTime) ), qtDateTimePropertyManager, SLOT(setValue(QtProperty *, QDateTime) ) );
    QObject::connect(qtDateTimePropertyManager, SIGNAL(checkChanged(QtProperty *, bool) ), model, SLOT(setCheck(QtProperty *, bool) ) );
    property = qtDateTimePropertyManager->addProperty(("QDateTime_" + std::to_string(count + 1)).c_str());
    groupProperty->addSubProperty(property);
    qtDateTimePropertyManager->setValue(property, QDateTime(DATETIME_INIT_VECTOR));
    qtDateTimePropertyManager->setCheck(property, false);

    // QtKeySequencePropertyManager/KeySequenceEditorFactory
    treePropertyBrowser->setFactoryForManager(qtKeySequencePropertyManager, keySequenceEditorFactory);
    boxPropertyBrowser->setFactoryForManager(qtKeySequencePropertyManager, keySequenceEditorFactory);
    buttonPropertyBrowser->setFactoryForManager(qtKeySequencePropertyManager, keySequenceEditorFactory);
    QObject::connect(qtKeySequencePropertyManager, SIGNAL(valueChanged(QtProperty *, const QKeySequence &) ), model, SLOT(setValue(QtProperty *, const QKeySequence &) ) );
    QObject::connect(model, SIGNAL(valueChanged(QtProperty *, const QKeySequence &) ), qtKeySequencePropertyManager, SLOT(setValue(QtProperty *, const QKeySequence &) ) );
    QObject::connect(qtKeySequencePropertyManager, SIGNAL(checkChanged(QtProperty *, bool) ), model, SLOT(setCheck(QtProperty *, bool) ) );
    property = qtKeySequencePropertyManager->addProperty(("QKeySequence_" + std::to_string(count + 1)).c_str());
    groupProperty->addSubProperty(property);
    qtKeySequencePropertyManager->setValue(property, QKeySequence(KEY_INIT_VECTOR));
    qtKeySequencePropertyManager->setCheck(property, false);

    // QtCharPropertyManager/CharEditorFactory
    treePropertyBrowser->setFactoryForManager(qtCharPropertyManager, charEditorFactory);
    boxPropertyBrowser->setFactoryForManager(qtCharPropertyManager, charEditorFactory);
    buttonPropertyBrowser->setFactoryForManager(qtCharPropertyManager, charEditorFactory);
    QObject::connect(qtCharPropertyManager, SIGNAL(valueChanged(QtProperty *, const QChar &) ), model, SLOT(setValue(QtProperty *, const QChar &) ) );
    QObject::connect(model, SIGNAL(valueChanged(QtProperty *, const QChar &) ), qtCharPropertyManager, SLOT(setValue(QtProperty *, const QChar &) ) );
    QObject::connect(qtCharPropertyManager, SIGNAL(checkChanged(QtProperty *, bool) ), model, SLOT(setCheck(QtProperty *, bool) ) );
    property = qtCharPropertyManager->addProperty(("QChar_" + std::to_string(count + 1)).c_str());
    groupProperty->addSubProperty(property);
    qtCharPropertyManager->setValue(property, CHAR_INIT_VECTOR);
    qtCharPropertyManager->setCheck(property, false);

    // QtPointPropertyManager/PointEditorFactory
    treePropertyBrowser->setFactoryForManager(qtPointPropertyManager, pointEditorFactory);
    boxPropertyBrowser->setFactoryForManager(qtPointPropertyManager, pointEditorFactory);
    buttonPropertyBrowser->setFactoryForManager(qtPointPropertyManager, pointEditorFactory);
    treePropertyBrowser->setFactoryForManager(qtPointPropertyManager->subIntPropertyManager(), intEditFactory);
    boxPropertyBrowser->setFactoryForManager(qtPointPropertyManager->subIntPropertyManager(), intEditFactory);
    buttonPropertyBrowser->setFactoryForManager(qtPointPropertyManager->subIntPropertyManager(), intEditFactory);
    QObject::connect(qtPointPropertyManager, SIGNAL(valueChanged(QtProperty *, const QPoint &) ), model, SLOT(setValue(QtProperty *, const QPoint &) ) );
    QObject::connect(model, SIGNAL(valueChanged(QtProperty *, const QPoint &) ), qtPointPropertyManager, SLOT(setValue(QtProperty *, const QPoint &) ) );
    QObject::connect(qtPointPropertyManager, SIGNAL(checkChanged(QtProperty *, bool) ), model, SLOT(setCheck(QtProperty *, bool) ) );
    property = qtPointPropertyManager->addProperty(("QPoint_" + std::to_string(count + 1)).c_str());
    groupProperty->addSubProperty(property);
    qtPointPropertyManager->setValue(property, QPoint(POINT_INIT_VECTOR));
    qtPointPropertyManager->setCheck(property, false);

    // QtPointFPropertyManager/PointFEditorFactory
    treePropertyBrowser->setFactoryForManager(qtPointFPropertyManager, pointFEditorFactory);
    boxPropertyBrowser->setFactoryForManager(qtPointFPropertyManager, pointFEditorFactory);
    buttonPropertyBrowser->setFactoryForManager(qtPointFPropertyManager, pointFEditorFactory);
    treePropertyBrowser->setFactoryForManager(qtPointFPropertyManager->subDoublePropertyManager(),doubleEditFactory);
    boxPropertyBrowser->setFactoryForManager(qtPointFPropertyManager->subDoublePropertyManager(), doubleEditFactory);
    buttonPropertyBrowser->setFactoryForManager(qtPointFPropertyManager->subDoublePropertyManager(), doubleEditFactory);
    QObject::connect(qtPointFPropertyManager, SIGNAL(valueChanged(QtProperty *, const QPointF &) ), model, SLOT(setValue(QtProperty *, const QPointF &) ) );
    QObject::connect(model, SIGNAL(valueChanged(QtProperty *, const QPointF &) ), qtPointFPropertyManager, SLOT(setValue(QtProperty *, const QPointF &) ) );
    QObject::connect(qtPointFPropertyManager, SIGNAL(checkChanged(QtProperty *, bool) ), model, SLOT(setCheck(QtProperty *, bool) ) );
    property = qtPointFPropertyManager->addProperty(("QPointF_" + std::to_string(count + 1)).c_str());
    groupProperty->addSubProperty(property);
    qtPointFPropertyManager->setMinimum(property, QPointF(POINTF_MIN_INIT_VECTOR));
    qtPointFPropertyManager->setMaximum(property, QPointF(POINTF_MAX_INIT_VECTOR));
    qtPointFPropertyManager->setPrecision(property, DOUBLE_PRECISION);
    qtPointFPropertyManager->setValue(property, QPointF(POINTF_INIT_VECTOR));
    qtPointFPropertyManager->setCheck(property, false);

    // QtSizePropertyManager/SizeEditorFactory
    treePropertyBrowser->setFactoryForManager(qtSizePropertyManager, sizeEditorFactory);
    boxPropertyBrowser->setFactoryForManager(qtSizePropertyManager, sizeEditorFactory);
    buttonPropertyBrowser->setFactoryForManager(qtSizePropertyManager, sizeEditorFactory);
    treePropertyBrowser->setFactoryForManager(qtSizePropertyManager->subIntPropertyManager(), intEditFactory);
    boxPropertyBrowser->setFactoryForManager(qtSizePropertyManager->subIntPropertyManager(), intEditFactory);
    buttonPropertyBrowser->setFactoryForManager(qtSizePropertyManager->subIntPropertyManager(), intEditFactory);
    QObject::connect(qtSizePropertyManager, SIGNAL(valueChanged(QtProperty *, const QSize &) ), model, SLOT(setValue(QtProperty *, const QSize &) ) );
    QObject::connect(model, SIGNAL(valueChanged(QtProperty *, const QSize &) ), qtSizePropertyManager, SLOT(setValue(QtProperty *, const QSize &) ) );
    QObject::connect(qtSizePropertyManager, SIGNAL(checkChanged(QtProperty *, bool) ), model, SLOT(setCheck(QtProperty *, bool) ) );
    property = qtSizePropertyManager->addProperty(("QSize_" + std::to_string(count + 1)).c_str());
    groupProperty->addSubProperty(property);
    qtSizePropertyManager->setValue(property, QSize(SIZE_INIT_VECTOR));
    qtSizePropertyManager->setCheck(property, false);

    // QtSizeFPropertyManager/SizeFEditorFactory
    treePropertyBrowser->setFactoryForManager(qtSizeFPropertyManager, sizeFEditorFactory);
    boxPropertyBrowser->setFactoryForManager(qtSizeFPropertyManager, sizeFEditorFactory);
    buttonPropertyBrowser->setFactoryForManager(qtSizeFPropertyManager, sizeFEditorFactory);
    treePropertyBrowser->setFactoryForManager(qtSizeFPropertyManager->subDoublePropertyManager(),doubleEditFactory);
    boxPropertyBrowser->setFactoryForManager(qtSizeFPropertyManager->subDoublePropertyManager(), doubleEditFactory);
    buttonPropertyBrowser->setFactoryForManager(qtSizeFPropertyManager->subDoublePropertyManager(), doubleEditFactory);
    QObject::connect(qtSizeFPropertyManager, SIGNAL(valueChanged(QtProperty *, const QSizeF &) ), model, SLOT(setValue(QtProperty *, const QSizeF &) ) );
    QObject::connect(model, SIGNAL(valueChanged(QtProperty *, const QSizeF &) ), qtSizeFPropertyManager, SLOT(setValue(QtProperty *, const QSizeF &) ) );
    QObject::connect(qtSizeFPropertyManager, SIGNAL(checkChanged(QtProperty *, bool) ), model, SLOT(setCheck(QtProperty *, bool) ) );
    property = qtSizeFPropertyManager->addProperty(("QSizeF_" + std::to_string(count + 1)).c_str());
    groupProperty->addSubProperty(property);
    qtSizeFPropertyManager->setMinimum(property, QSizeF(SIZEF_MIN_INIT_VECTOR));
    qtSizeFPropertyManager->setMaximum(property, QSizeF(SIZEF_MAX_INIT_VECTOR));
    qtSizeFPropertyManager->setPrecision(property, DOUBLE_PRECISION);
    qtSizeFPropertyManager->setValue(property, QSizeF(SIZEF_INIT_VECTOR));
    qtSizeFPropertyManager->setCheck(property, false);

    // QtRectPropertyManager/RectEditorFactory
    treePropertyBrowser->setFactoryForManager(qtRectPropertyManager, rectEditorFactory);
    boxPropertyBrowser->setFactoryForManager(qtRectPropertyManager, rectEditorFactory);
    buttonPropertyBrowser->setFactoryForManager(qtRectPropertyManager, rectEditorFactory);
    treePropertyBrowser->setFactoryForManager(qtRectPropertyManager->subIntPropertyManager(), intEditFactory);
    boxPropertyBrowser->setFactoryForManager(qtRectPropertyManager->subIntPropertyManager(), intEditFactory);
    buttonPropertyBrowser->setFactoryForManager(qtRectPropertyManager->subIntPropertyManager(), intEditFactory);
    QObject::connect(qtRectPropertyManager, SIGNAL(valueChanged(QtProperty *, const QRect &) ), model, SLOT(setValue(QtProperty *, const QRect &) ) );
    QObject::connect(model, SIGNAL(valueChanged(QtProperty *, const QRect &) ), qtRectPropertyManager, SLOT(setValue(QtProperty *, const QRect &) ) );
    QObject::connect(qtRectPropertyManager, SIGNAL(checkChanged(QtProperty *, bool) ), model, SLOT(setCheck(QtProperty *, bool) ) );
    property = qtRectPropertyManager->addProperty(("QRect_" + std::to_string(count + 1)).c_str());
    groupProperty->addSubProperty(property);
    qtRectPropertyManager->setValue(property, QRect(RECT_INIT_VECTOR));
    qtRectPropertyManager->setCheck(property, false);

    // QtRectFPropertyManager/RectFEditorFactory
    treePropertyBrowser->setFactoryForManager(qtRectFPropertyManager, rectFEditorFactory);
    boxPropertyBrowser->setFactoryForManager(qtRectFPropertyManager, rectFEditorFactory);
    buttonPropertyBrowser->setFactoryForManager(qtRectFPropertyManager, rectFEditorFactory);
    treePropertyBrowser->setFactoryForManager(qtRectFPropertyManager->subDoublePropertyManager(),doubleEditFactory);
    boxPropertyBrowser->setFactoryForManager(qtRectFPropertyManager->subDoublePropertyManager(), doubleEditFactory);
    buttonPropertyBrowser->setFactoryForManager(qtRectFPropertyManager->subDoublePropertyManager(), doubleEditFactory);
    QObject::connect(qtRectFPropertyManager, SIGNAL(valueChanged(QtProperty *, const QRectF &) ), model, SLOT(setValue(QtProperty *, const QRectF &) ) );
    QObject::connect(model, SIGNAL(valueChanged(QtProperty *, const QRectF &) ), qtRectFPropertyManager, SLOT(setValue(QtProperty *, const QRectF &) ) );
    QObject::connect(qtRectFPropertyManager, SIGNAL(checkChanged(QtProperty *, bool) ), model, SLOT(setCheck(QtProperty *, bool) ) );
    property = qtRectFPropertyManager->addProperty(("QRectF_" + std::to_string(count + 1)).c_str());
    groupProperty->addSubProperty(property);
    qtRectFPropertyManager->setConstraint(property, QRectF(RECTF_CONST_INIT_VECTOR));
    qtRectFPropertyManager->setPrecision(property, DOUBLE_PRECISION);
    qtRectFPropertyManager->setValue(property, QRectF(RECTF_INIT_VECTOR));
    qtRectFPropertyManager->setCheck(property, false);

    // QtEnumPropertyManager/EnumEditorFactory
    treePropertyBrowser->setFactoryForManager(qtEnumPropertyManager, enumEditorFactory);
    boxPropertyBrowser->setFactoryForManager(qtEnumPropertyManager, enumEditorFactory);
    buttonPropertyBrowser->setFactoryForManager(qtEnumPropertyManager, enumEditorFactory);
    QObject::connect(qtEnumPropertyManager, SIGNAL(valueChanged(QtProperty *, int) ), model, SLOT(setValue(QtProperty *, int) ) );
    QObject::connect(model, SIGNAL(valueChanged(QtProperty *, int) ), qtEnumPropertyManager, SLOT(setValue(QtProperty *, int) ) );
    QObject::connect(qtEnumPropertyManager, SIGNAL(checkChanged(QtProperty *, bool) ), model, SLOT(setCheck(QtProperty *, bool) ) );
    property = qtEnumPropertyManager->addProperty(("int_" + std::to_string(count + 1)).c_str());
    groupProperty->addSubProperty(property);
    QStringList enumNames;
    enumNames << "BLACK" << "RED" << "GREEN" << "BLUE";
    qtEnumPropertyManager->setEnumNames(property, enumNames);
    qtEnumPropertyManager->setValue(property, ENUM_INIT_VECTOR);
    qtEnumPropertyManager->setCheck(property, false);

    // QtFlagPropertyManager/FlagEditorFactory
    treePropertyBrowser->setFactoryForManager(qtFlagPropertyManager, flagEditorFactory);
    boxPropertyBrowser->setFactoryForManager(qtFlagPropertyManager, flagEditorFactory);
    buttonPropertyBrowser->setFactoryForManager(qtFlagPropertyManager, flagEditorFactory);
    treePropertyBrowser->setFactoryForManager(qtFlagPropertyManager->subBoolPropertyManager(), checkBoxFactory);
    boxPropertyBrowser->setFactoryForManager(qtFlagPropertyManager->subBoolPropertyManager(), checkBoxFactory);
    buttonPropertyBrowser->setFactoryForManager(qtFlagPropertyManager->subBoolPropertyManager(),checkBoxFactory);
    QObject::connect(qtFlagPropertyManager, SIGNAL(valueChanged(QtProperty *, int) ), model, SLOT(setValue(QtProperty *, int) ) );
    QObject::connect(model, SIGNAL(valueChanged(QtProperty *, int) ), qtFlagPropertyManager, SLOT(setValue(QtProperty *, int) ) );
    QObject::connect(qtFlagPropertyManager, SIGNAL(checkChanged(QtProperty *, bool) ), model, SLOT(setCheck(QtProperty *, bool) ) );
    property = qtFlagPropertyManager->addProperty(("int_" + std::to_string(count + 1)).c_str());
    groupProperty->addSubProperty(property);
    QStringList flagNames;
    flagNames << "RED" << "GREEN" << "BLUE";
    qtFlagPropertyManager->setFlagNames(property, flagNames);
    qtFlagPropertyManager->setValue(property, int(FLAG_INIT_VECTOR));
    qtFlagPropertyManager->setCheck(property, false);

    // QtLocalePropertyManager/LocaleEditorFactory
    treePropertyBrowser->setFactoryForManager(qtLocalePropertyManager, localeEditorFactory);
    boxPropertyBrowser->setFactoryForManager(qtLocalePropertyManager, localeEditorFactory);
    buttonPropertyBrowser->setFactoryForManager(qtLocalePropertyManager, localeEditorFactory);
    treePropertyBrowser->setFactoryForManager(qtLocalePropertyManager->subEnumPropertyManager(), enumEditorFactory);
    boxPropertyBrowser->setFactoryForManager(qtLocalePropertyManager->subEnumPropertyManager(),enumEditorFactory);
    buttonPropertyBrowser->setFactoryForManager(qtLocalePropertyManager->subEnumPropertyManager(),enumEditorFactory);
    QObject::connect(qtLocalePropertyManager, SIGNAL(valueChanged(QtProperty *, const QLocale &) ), model, SLOT(setValue(QtProperty *, const QLocale &) ) );
    QObject::connect(model, SIGNAL(valueChanged(QtProperty *, const QLocale &) ), qtLocalePropertyManager, SLOT(setValue(QtProperty *, const QLocale &) ) );
    QObject::connect(qtLocalePropertyManager, SIGNAL(checkChanged(QtProperty *, bool) ), model, SLOT(setCheck(QtProperty *, bool) ) );
    property = qtLocalePropertyManager->addProperty(("QLocale_" + std::to_string(count + 1)).c_str());
    groupProperty->addSubProperty(property);
    qtLocalePropertyManager->setValue(property, QLocale(LOCALE_INIT_VECTOR));
    qtLocalePropertyManager->setCheck(property, false);

    // QtSizePolicyPropertyManager/SizePolicyEditorFactory
    treePropertyBrowser->setFactoryForManager(qtSizePolicyPropertyManager, sizePolicyEditorFactory);
    boxPropertyBrowser->setFactoryForManager(qtSizePolicyPropertyManager, sizePolicyEditorFactory);
    buttonPropertyBrowser->setFactoryForManager(qtSizePolicyPropertyManager, sizePolicyEditorFactory);
    treePropertyBrowser->setFactoryForManager(qtSizePolicyPropertyManager->subEnumPropertyManager(), enumEditorFactory);
    boxPropertyBrowser->setFactoryForManager(qtSizePolicyPropertyManager->subIntPropertyManager(), intEditFactory);
    buttonPropertyBrowser->setFactoryForManager(qtSizePolicyPropertyManager->subEnumPropertyManager(), enumEditorFactory);
    treePropertyBrowser->setFactoryForManager(qtSizePolicyPropertyManager->subIntPropertyManager(), intEditFactory);
    boxPropertyBrowser->setFactoryForManager(qtSizePolicyPropertyManager->subEnumPropertyManager(), enumEditorFactory);
    buttonPropertyBrowser->setFactoryForManager(qtSizePolicyPropertyManager->subIntPropertyManager(), intEditFactory);
    QObject::connect(qtSizePolicyPropertyManager, SIGNAL(valueChanged(QtProperty *, const QSizePolicy &) ), model, SLOT(setValue(QtProperty *, const QSizePolicy &) ) );
    QObject::connect(model, SIGNAL(valueChanged(QtProperty *, const QSizePolicy &) ), qtSizePolicyPropertyManager, SLOT(setValue(QtProperty *, const QSizePolicy &) ) );
    QObject::connect(qtSizePolicyPropertyManager, SIGNAL(checkChanged(QtProperty *, bool) ), model, SLOT(setCheck(QtProperty *, bool) ) );
    property = qtSizePolicyPropertyManager->addProperty(("QSizePolicy_" + std::to_string(count + 1)).c_str());
    groupProperty->addSubProperty(property);
    QSizePolicy sizePolicy = QSizePolicy(SIZE_POLICY_INIT_VECTOR);
    sizePolicy.setHorizontalStretch(X_STRETCH_SIZE_POLICY_INIT_VECTOR);
    sizePolicy.setVerticalStretch(Y_STRETCH_SIZE_POLICY_INIT_VECTOR);
    qtSizePolicyPropertyManager->setValue(property, sizePolicy);
    qtSizePolicyPropertyManager->setCheck(property, false);

    // QtFontPropertyManager/FontEditorFactory
    treePropertyBrowser->setFactoryForManager(qtFontPropertyManager, fontEditorFactory);
    boxPropertyBrowser->setFactoryForManager(qtFontPropertyManager, fontEditorFactory);
    buttonPropertyBrowser->setFactoryForManager(qtFontPropertyManager, fontEditorFactory);
    QObject::connect(qtFontPropertyManager, SIGNAL(valueChanged(QtProperty *, const QFont &) ), model, SLOT(setValue(QtProperty *, const QFont &) ) );
    QObject::connect(model, SIGNAL(valueChanged(QtProperty *, const QFont &) ), qtFontPropertyManager, SLOT(setValue(QtProperty *, const QFont &) ) );
    QObject::connect(qtFontPropertyManager, SIGNAL(checkChanged(QtProperty *, bool) ), model, SLOT(setCheck(QtProperty *, bool) ) );
    property = qtFontPropertyManager->addProperty(("QFont_" + std::to_string(count + 1)).c_str());
    groupProperty->addSubProperty(property);
    qtFontPropertyManager->setValue(property, QFont(FONT_INIT_VECTOR));
    qtFontPropertyManager->setCheck(property, false);

    // QtColorPropertyManager/ColorEditorFactory
    treePropertyBrowser->setFactoryForManager(qtColorPropertyManager, colorEditorFactory);
    boxPropertyBrowser->setFactoryForManager(qtColorPropertyManager, colorEditorFactory);
    buttonPropertyBrowser->setFactoryForManager(qtColorPropertyManager, colorEditorFactory);
    QObject::connect(qtColorPropertyManager, SIGNAL(valueChanged(QtProperty *, const QColor &) ), model, SLOT(setValue(QtProperty *, const QColor &) ) );
    QObject::connect(model, SIGNAL(valueChanged(QtProperty *, const QColor &) ), qtColorPropertyManager, SLOT(setValue(QtProperty *, const QColor &) ) );
    QObject::connect(qtColorPropertyManager, SIGNAL(checkChanged(QtProperty *, bool) ), model, SLOT(setCheck(QtProperty *, bool) ) );
    property = qtColorPropertyManager->addProperty(("QColor_" + std::to_string(count + 1)).c_str());
    groupProperty->addSubProperty(property);
    qtColorPropertyManager->setValue(property, COLOR_INIT_VECTOR);
    qtColorPropertyManager->setCheck(property, false);

    // QtCursorPropertyManager/CursorEditorFactory
    treePropertyBrowser->setFactoryForManager(qtCursorPropertyManager, cursorEditorFactory);
    boxPropertyBrowser->setFactoryForManager(qtCursorPropertyManager, cursorEditorFactory);
    buttonPropertyBrowser->setFactoryForManager(qtCursorPropertyManager, cursorEditorFactory);
    QObject::connect(qtCursorPropertyManager, SIGNAL(valueChanged(QtProperty *, const QCursor &) ), model, SLOT(setValue(QtProperty *, const QCursor &) ) );
    QObject::connect(model, SIGNAL(valueChanged(QtProperty *, const QCursor &) ), qtCursorPropertyManager, SLOT(setValue(QtProperty *, const QCursor &) ) );
    QObject::connect(qtCursorPropertyManager, SIGNAL(checkChanged(QtProperty *, bool) ), model, SLOT(setCheck(QtProperty *, bool) ) );
    property = qtCursorPropertyManager->addProperty(("QCursor_" + std::to_string(count + 1)).c_str());
    groupProperty->addSubProperty(property);
    qtCursorPropertyManager->setValue(property, QCursor(CURSOR_INIT_VECTOR));
    qtCursorPropertyManager->setCheck(property, false);

    // QtFilePropertyManager/FileEditorFactory
    treePropertyBrowser->setFactoryForManager(qtFilePropertyManager, fileEditorFactory);
    boxPropertyBrowser->setFactoryForManager(qtFilePropertyManager, fileEditorFactory);
    buttonPropertyBrowser->setFactoryForManager(qtFilePropertyManager, fileEditorFactory);
    QObject::connect(qtFilePropertyManager, SIGNAL(valueChanged(QtProperty *, const QString &) ), model, SLOT(setValue(QtProperty *, const QString &) ) );
    QObject::connect(model, SIGNAL(valueChanged(QtProperty *, const QString &) ), qtFilePropertyManager, SLOT(setValue(QtProperty *, const QString &) ) );
    QObject::connect(qtFilePropertyManager, SIGNAL(checkChanged(QtProperty *, bool) ), model, SLOT(setCheck(QtProperty *, bool) ) );
    property = qtFilePropertyManager->addProperty(("QString_" + std::to_string(count + 1)).c_str());
    groupProperty->addSubProperty(property);
    qtFilePropertyManager->setValue(property, FILE_INIT_VECTOR);
    qtFilePropertyManager->setCheck(property, false);

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
    int ret = QApplication::exec();
    delete dialog;
    return ret;

}
#include "main.moc"
