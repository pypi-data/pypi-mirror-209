//
// Created by dylan_bespalko on 3/14/23.
//

#ifndef QTABSTRACTPROPERTYBROWSERTEST_H
#define QTABSTRACTPROPERTYBROWSERTEST_H

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

QT_BEGIN_NAMESPACE

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

class QtModel : public QObject
{
Q_OBJECT

public:
    inline double atol() {return m_atol;};
    inline void setAtol(double atol) {m_atol = atol;};

public Q_SLOTS:
    inline void setValue(QtProperty *property, int val) {emit valueChanged(property, val);};
    inline void setValue(QtProperty *property, bool val) {emit valueChanged(property, val);};
    inline void setValue(QtProperty *property, double val) {emit valueChanged(property, val + atol());};
    inline void setValue(QtProperty *property, const QtComplex& val) {emit valueChanged(property, val + atol());};
    inline void setValue(QtProperty *property, const QtQuaternion& val) {emit valueChanged(property, val
        + QtQuaternion(atol()));};
    inline void setValue(QtProperty *property, const QVector<QtComplex>& val) {emit valueChanged(property, val);};
    inline void setValue(QtProperty *property, const QString &val) {emit valueChanged(property, val);};
    inline void setValue(QtProperty *property, QDate val) {emit valueChanged(property, val);};
    inline void setValue(QtProperty *property, QTime val) {emit valueChanged(property, val);};
    inline void setValue(QtProperty *property, QDateTime val) {emit valueChanged(property, val);};
    inline void setValue(QtProperty *property, const QKeySequence &val) {emit valueChanged(property, val);};
    inline void setValue(QtProperty *property, const QChar &val) {emit valueChanged(property, val);};
    inline void setValue(QtProperty *property, const QLocale &val) {emit valueChanged(property, val);};
    inline void setValue(QtProperty *property, const QPoint &val) {emit valueChanged(property, val);};
    inline void setValue(QtProperty *property, const QPointF &val) {emit valueChanged(property, val
        + QPointF(atol(), atol())) ;};
    inline void setValue(QtProperty *property, const QSize &val) {emit valueChanged(property, val);};
    inline void setValue(QtProperty *property, const QSizeF &val) {emit valueChanged(property, val
        + QSizeF(atol(), atol()));};
    inline void setValue(QtProperty *property, const QRect &val) {emit valueChanged(property, val);};
    inline void setValue(QtProperty *property, const QRectF &val) {emit valueChanged(property, val);};
    inline void setValue(QtProperty *property, const QSizePolicy &val) {emit valueChanged(property, val);};
    inline void setValue(QtProperty *property, const QFont &val) {emit valueChanged(property, val);};
    inline void setValue(QtProperty *property, const QColor &val) {emit valueChanged(property, val);};
    inline void setValue(QtProperty *property, const QCursor &val) {emit valueChanged(property, val);};
    inline void setCheck(QtProperty *property, bool check) {
//        std::clog << "INFO   : " << property->propertyName().toStdString() << std::endl;
    };
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

private:
    double m_atol = 0.0;
};

class QtAbstractManagerEditorTest : public QObject
{
    Q_OBJECT
protected:

    QtModel *model;
    QDialog *dialog;
    QGridLayout *layout;
    QScrollArea *treeScrollArea;
    QtTreePropertyBrowser *treePropertyBrowser;
    QScrollArea *boxScrollArea;
    QtGroupBoxPropertyBrowser *boxPropertyBrowser;
    QScrollArea *buttonScrollArea;
    QtButtonPropertyBrowser *buttonPropertyBrowser;

    QtGroupPropertyManager *groupPropertyManager;
    QtIntPropertyManager *qtIntPropertyManager;
    QtBoolPropertyManager *qtBoolPropertyManager;
    QtDoublePropertyManager *qtDoublePropertyManager;
    QtComplexPropertyManager *qtComplexPropertyManager;
    QtQuaternionPropertyManager *qtQuaternionPropertyManager;
    QtVectorComplexPropertyManager *qtVectorComplexPropertyManager;
    QtStringPropertyManager *qtStringPropertyManager;
    QtDatePropertyManager *qtDatePropertyManager;
    QtTimePropertyManager *qtTimePropertyManager;
    QtDateTimePropertyManager *qtDateTimePropertyManager;
    QtKeySequencePropertyManager *qtKeySequencePropertyManager;
    QtCharPropertyManager *qtCharPropertyManager;
    QtPointPropertyManager *qtPointPropertyManager;
    QtPointFPropertyManager *qtPointFPropertyManager;
    QtSizePropertyManager *qtSizePropertyManager;
    QtSizeFPropertyManager *qtSizeFPropertyManager;
    QtRectPropertyManager *qtRectPropertyManager;
    QtRectFPropertyManager *qtRectFPropertyManager;
    QtEnumPropertyManager *qtEnumPropertyManager;
    QtFlagPropertyManager *qtFlagPropertyManager;
    QtLocalePropertyManager *qtLocalePropertyManager;
    QtSizePolicyPropertyManager *qtSizePolicyPropertyManager;
    QtFontPropertyManager *qtFontPropertyManager;
    QtColorPropertyManager *qtColorPropertyManager;
    QtCursorPropertyManager *qtCursorPropertyManager;
    QtFilePropertyManager *qtFilePropertyManager;

    QtGroupEditorFactory *groupEditorFactory;
    QtSpinBoxFactory *spinBoxFactory;
    QtIntEditFactory *intEditFactory;
    QtSliderFactory *sliderFactory;
    QtCheckBoxFactory *checkBoxFactory;
    QtDoubleSpinBoxFactory *doubleSpinBoxFactory;
    QtDoubleEditFactory *doubleEditFactory;
    QtComplexEditFactory *complexEditFactory;
    QtQuaternionEditFactory *quaternionEditFactory;
    QtVectorComplexEditFactory *vectorComplexEditFactory;
    QtLineEditFactory *lineEditFactory;
    QtDateEditFactory *dateEditFactory;
    QtTimeEditFactory *timeEditFactory;
    QtDateTimeEditFactory *dateTimeEditFactory;
    QtKeySequenceEditorFactory *keySequenceEditorFactory;
    QtCharEditorFactory *charEditorFactory;
    QtPointEditorFactory *pointEditorFactory;
    QtPointFEditorFactory *pointFEditorFactory;
    QtSizeEditorFactory *sizeEditorFactory;
    QtSizeFEditorFactory *sizeFEditorFactory;
    QtRectEditorFactory *rectEditorFactory;
    QtRectFEditorFactory *rectFEditorFactory;
    QtEnumEditorFactory *enumEditorFactory;
    QtFlagEditorFactory *flagEditorFactory;
    QtLocaleEditorFactory *localeEditorFactory;
    QtSizePolicyEditorFactory *sizePolicyEditorFactory;
    QtFontEditorFactory *fontEditorFactory;
    QtColorEditorFactory *colorEditorFactory;
    QtCursorEditorFactory *cursorEditorFactory;
    QtFileEditorFactory *fileEditorFactory;

    QtProperty *groupProperty;
    QtProperty *property;
    unsigned int count = 0;

public:

    void initPropertyBrowsers();
    void addGroupProperty();
    virtual void addProperty();
    void finalizePropertyBrowser();

private slots:

    void initTestCase();
    virtual void init() {
        qtBoolPropertyManager->setValue(property, false);
        qtBoolPropertyManager->setCheck(property, false);
    };
    void cleanup(){};
    virtual void cleanupTestCase() {
        qDebug("Deleting dialog");
        delete dialog;
    };
};

QT_END_NAMESPACE

#endif //QTABSTRACTPROPERTYBROWSERTEST_H
