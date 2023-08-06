// Copyright (C) 2016 The Qt Company Ltd.
// SPDX-License-Identifier: LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only

//
//  W A R N I N G
//  -------------
//
// This file is not part of the Qt API.  It exists for the convenience
// of Qt Designer.  This header
// file may change from version to version without notice, or even be removed.
//
// We mean it.
//

#ifndef QTPROPERTYBROWSERUTILS_H
#define QTPROPERTYBROWSERUTILS_H

#include <QtCore/QMap>
#include <QtCore/QMetaEnum>
#include <QtGui/QIcon>
#include <QtGui/QQuaternion>

#include <QtWidgets/QWidget>
#include <QtCore/QStringList>
#include <QtWidgets/QToolButton>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QFileDialog>

#include <QtGui/QPainter>
#include <QtWidgets/QApplication>
#include <QtWidgets/QStyle>
#include <QtWidgets/QStyleOptionButton>
#include <QtWidgets/QDoubleSpinBox>

#include <complex>
#include <qvalidator.h>
#include <QLabel>

#ifndef SKNRF_BUILD_EXTRA
    #define SKNRF_BUILD_EXTRA 1
#endif

extern double infinity;
extern double neg_infinity;
extern double highest;
extern double lowest;
extern double epsilon;
extern double minest;

class QtComplex : public std::complex<double>
{
public:
    QtComplex(double re = 0.0, double im = 0.0);
    QtComplex(std::complex<double> parent);
};

class QtQuaternion : public QQuaternion
{
public:
    QtQuaternion(double scalar = 0.0, double x = 0.0, double y = 0.0, double z = 0.0) : QQuaternion(scalar, x, y, z) {};
    QtQuaternion(QQuaternion val) : QQuaternion(val.scalar(), val.x(), val.y(), val.z()) {};
    explicit QtQuaternion(std::complex<double> a, std::complex<double> b) : QQuaternion(a.real(), a.imag(), b.real(), b.imag()) {};
};

enum Format
{
    RE,
    RE_IM,
    LIN_DEG,
    LOG_DEG
};
extern QMap<Format, QString> FormatNameMap;

enum Scale {
    T,
    G,
    M,
    K,
    _,
    m,
    u,
    n,
    p,
};
extern QMap<Scale, QString> ScaleNameMap;
extern QMap<Scale, int> ScaleValueMap;
extern QMap<Scale, int> InvScaleValueMap;

enum PkAvg
{
    PK,
    AVG
};
extern QMap<PkAvg, QString> PkAvgNameMap;

enum Domain
{
    TF,
    FF,
    FT,
    TT,
    TH,
};
extern QMap<Domain, QString> DomainNameMap;

enum BrowserCol
{
    NONE =    0x00,
    MINIMUM = 0x01,
    MAXIMUM = 0x02,
    UNIT =    0x04,
    PKAVG =   0x08,
    FORMAT =  0x10,
    CHECK =   0x20
};
Q_DECLARE_FLAGS(BrowserCols, BrowserCol)
Q_DECLARE_OPERATORS_FOR_FLAGS(BrowserCols)

extern QMap<BrowserCol, QString> AttributeNameMap;
// Matches the Python isclose() function in PEP 0485 and Boost Weak Approach

template <class Value>
bool isclose(Value a, Value b, Value atol, Value rtol)
{
    if (std::abs(a-b) <= std::max( rtol * std::max(std::abs(a), std::abs(b)), atol))
        return true;
    else
        return false;
}
bool isclose(int a, int b, int atol, int rtol);
bool isclose(QtComplex a, QtComplex b, QtComplex atol, QtComplex rtol);
bool isclose(QtQuaternion a, QtQuaternion b, QtQuaternion atol, QtQuaternion rtol);
bool isclose(QVector<QtComplex> a, QVector<QtComplex> b, QVector<QtComplex> atol, QVector<QtComplex> rtol);
bool isclose(QDate a, QDate b, QDate atol, QDate rtol);
bool isclose(QSize a, QSize b, QSize atol, QSize rtol);
bool isclose(QPointF a, QPointF b, QPointF atol, QPointF rtol);
bool isclose(QSizeF a, QSizeF b, QSizeF atol, QSizeF rtol);
bool isclose(QRectF a, QRectF b, QRectF atol, QRectF rtol);

QString double2str(double val, int precision);

template <typename T>
inline int sgn(T val) {
    return (T(0) < val) - (val < T(0));
}

template <typename T>
T atolCalc(int precision, T minimum , T maximum){
    uint64_t num_values = uint64_t(1) << uint64_t(precision);
    T atol = (maximum - minimum) / num_values;
    return atol;
}

QtComplex atolCalc(int precision, QtComplex minimum , QtComplex maximum);
QtQuaternion atolCalc(int precision, QtQuaternion minimum , QtQuaternion maximum);
QPointF atolCalc(int precision, const QPointF &minimum , const QPointF &maximum);
QSizeF atolCalc(int precision, const QSizeF &minimum , const QSizeF &maximum);

template <typename T>
QVector<T> atolCalc(int precision, const QVector<T> &minimum , const QVector<T> &maximum) {
    QVector<T> atol(minimum.size());
    for (unsigned short idx=0; idx < minimum.size(); idx++)
        atol[idx] = atolCalc(precision, minimum[idx], maximum[idx]);
    return atol;
}

template <typename T>
T rtolCalc(int precision, T minimum , T maximum) {
    uint64_t num_values = uint64_t(1) << uint64_t(precision);
    T rtol = 1.0 / static_cast<double>(num_values);
    return rtol;
}

QtComplex rtolCalc(int precision, QtComplex minimum , QtComplex maximum);
QtQuaternion rtolCalc(int precision, QtQuaternion minimum , QtQuaternion maximum);
QPointF rtolCalc(int precision, const QPointF &minimum , const QPointF &maximum);
QSizeF rtolCalc(int precision, const QSizeF &minimum , const QSizeF &maximum);

template <typename T>
QVector<T> rtolCalc(int precision, const QVector<T> &minimum , const QVector<T> &maximum) {
    QVector<T> rtol(minimum.size());
    for (unsigned short idx=0; idx < minimum.size(); idx++)
        rtol[idx] = rtolCalc(precision, minimum[idx], maximum[idx]);
    return rtol;
}

template <typename T>
T fmtCalc(Scale scale, Format format, T val, bool inv=false){
    T scaled_val;
    int scale_ = (inv) ? InvScaleValueMap[scale] : ScaleValueMap[scale];
    switch (format) {
        case Format::LOG_DEG:
            scaled_val = val/sqrt(pow(10, scale_));
            break;
        default:
            scaled_val = val/pow(10, scale_);
            break;
    }
    return scaled_val;
}

QPointF fmtCalc(Scale scale, Format format, const QPointF &val, bool inv=false);
QSizeF fmtCalc(Scale scale, Format format, const QSizeF &val, bool inv=false);

template <typename T>
QVector<T> fmtCalc(Scale scale, Format format, const QVector<T> &val) {
    QVector<T> scaled_val(val.size());
    for (unsigned short idx=0; idx < val.size(); idx++)
        scaled_val[idx] = fmtCalc(scale, format, val[idx]);
    return scaled_val;
}

template <typename T>
int sigDigCalc(int precision, T minimum, T maximum, Scale scale, Format format, T ftol) {
    int sigDig = std::max(-int(std::floor(std::log10(ftol))), 1);
    return sigDig;
}

int sigDigCalc(int precision, QtComplex minimum, QtComplex maximum, Scale scale, Format format, QtComplex ftol);
int sigDigCalc(int precision, QtQuaternion minimum, QtQuaternion maximum, Scale scale, Format format, QtQuaternion ftol);
int sigDigCalc(int precision, const QPointF &minimum, const QPointF &maximum, Scale scale, Format format, const QPointF &ftol);
int sigDigCalc(int precision, const QSizeF &minimum, const QSizeF &maximum, Scale scale, Format format, const QSizeF &ftol);

template <typename T>
QVector<int> sigDigCalc(int precision, QVector<T> &minimum, QVector<T> &maximum, Scale scale, Format format, QVector<T> &ftol) {
    QVector<int> sigDig(ftol.size());
    for (unsigned short idx=0; idx < ftol.size(); idx++)
        sigDig[idx] = sigDigCalc(precision, minimum[idx], maximum[idx], scale, format, ftol[idx]);
    return sigDig;
}

QT_BEGIN_NAMESPACE

class QMouseEvent;
class QCheckBox;
class QLineEdit;

//     Return an icon containing a check box indicator
static QIcon drawCheckBox(bool value)
{
    QStyleOptionButton opt;
    opt.state |= value ? QStyle::State_On : QStyle::State_Off;
    opt.state |= QStyle::State_Enabled;
    const QStyle *style = QApplication::style();
    // Figure out size of an indicator and make sure it is not scaled down in a list view item
    // by making the pixmap as big as a list view icon and centering the indicator in it.
    // (if it is smaller, it can't be helped)
    const int indicatorWidth = style->pixelMetric(QStyle::PM_IndicatorWidth, &opt);
    const int indicatorHeight = style->pixelMetric(QStyle::PM_IndicatorHeight, &opt);
    const int listViewIconSize = indicatorWidth;
    const int pixmapWidth = indicatorWidth;
    const int pixmapHeight = qMax(indicatorHeight, listViewIconSize);

    opt.rect = QRect(0, 0, indicatorWidth, indicatorHeight);
    QPixmap pixmap = QPixmap(pixmapWidth, pixmapHeight);
    pixmap.fill(Qt::transparent);
    {
        // Center?
        const int xoff = (pixmapWidth  > indicatorWidth)  ? (pixmapWidth  - indicatorWidth)  / 2 : 0;
        const int yoff = (pixmapHeight > indicatorHeight) ? (pixmapHeight - indicatorHeight) / 2 : 0;
        QPainter painter(&pixmap);
        painter.translate(xoff, yoff);
        style->drawPrimitive(QStyle::PE_IndicatorCheckBox, &opt, &painter);
    }
    return QIcon(pixmap);
}

class QtCursorDatabase
{
public:
    QtCursorDatabase();
    void clear();

    QStringList cursorShapeNames() const;
    QMap<int, QIcon> cursorShapeIcons() const;
    QString cursorToShapeName(const QCursor &cursor) const;
    QIcon cursorToShapeIcon(const QCursor &cursor) const;
    int cursorToValue(const QCursor &cursor) const;
#ifndef QT_NO_CURSOR
    QCursor valueToCursor(int value) const;
#endif
private:
    void appendCursor(Qt::CursorShape shape, const QString &name, const QIcon &icon);
    QStringList m_cursorNames;
    QMap<int, QIcon> m_cursorIcons;
    QMap<int, Qt::CursorShape> m_valueToCursorShape;
    QMap<Qt::CursorShape, int> m_cursorShapeToValue;
};

class QtPropertyBrowserUtils
{
public:
    static QPixmap brushValuePixmap(const QBrush &b);
    static QIcon brushValueIcon(const QBrush &b);
    static QString colorValueText(const QColor &c);
    static QPixmap fontValuePixmap(const QFont &f);
    static QIcon fontValueIcon(const QFont &f);
    static QString fontValueText(const QFont &f);
    static QString dateFormat();
    static QString timeFormat();
    static QString dateTimeFormat();
};

class QtBoolEdit : public QWidget {
    Q_OBJECT
public:
    QtBoolEdit(QWidget *parent = 0);

    bool textVisible() const { return m_textVisible; }
    void setTextVisible(bool textVisible);

    Qt::CheckState checkState() const;
    void setCheckState(Qt::CheckState state);

    bool isChecked() const;
    void setChecked(bool c);

    bool blockCheckBoxSignals(bool block);

Q_SIGNALS:
    void toggled(bool);

protected:
    void mousePressEvent(QMouseEvent * event) override;

private:
    QCheckBox *m_checkBox;
    bool m_textVisible;
};

class QtSpinBoxPrivate;

class QtSpinBox : public QWidget
{
Q_OBJECT
    Q_ENUMS(Format)
public:
    explicit QtSpinBox(QWidget *parent = nullptr);
    ~QtSpinBox();

    int value() const;
    double minimum() const;
    double maximum() const;
    bool bounded() const;

    QValidator::State validate(QString &input, int &pos) const;
    bool eventFilter(QObject *obj, QEvent *ev);

public Q_SLOTS:
    void setValue();
    void setValue(int val);
    void setMinimum(double min);
    void setMaximum(double max);
    void setRange(double min, double max);
    void setReadOnly(bool readOnly);
    void setBounded(bool bounded);

Q_SIGNALS:
    void valueChanged(int val);
    void destroyed(QObject *obj);

private:
    QtSpinBoxPrivate *d_ptr;
    Q_DISABLE_COPY(QtSpinBox)
    Q_DECLARE_PRIVATE(QtSpinBox)

public:
    QString num2str();
    static QString num2str(int val, int minVal, int maxVal);
    static int str2num(const QString &text);
};

class QtIntEditPrivate;

class QtIntEdit : public QWidget
{
    Q_OBJECT
    Q_ENUMS(Format)
public:
    explicit QtIntEdit(QWidget *parent = nullptr);
    ~QtIntEdit();

    int value() const;
    double minimum() const;
    double maximum() const;
    bool bounded() const;

    QValidator::State validate(QString &input, int &pos) const;
    bool eventFilter(QObject *obj, QEvent *ev);

public Q_SLOTS:
    void setValue();
    void setValue(int val);
    void setMinimum(double min);
    void setMaximum(double max);
    void setRange(double min, double max);
    void setReadOnly(bool readOnly);
    void setBounded(bool bounded);

Q_SIGNALS:
    void valueChanged(int val);
    void destroyed(QObject *obj);

private:
    QtIntEditPrivate *d_ptr;
    Q_DISABLE_COPY(QtIntEdit)
    Q_DECLARE_PRIVATE(QtIntEdit)

public:
    QString num2str();
    static QString num2str(int val, int minVal, int maxVal);
    static int str2num(const QString &text);
};

class QtSliderPrivate;

class QtSlider : public QWidget
{
Q_OBJECT
    Q_ENUMS(Format)
public:
    explicit QtSlider(Qt::Orientation orientation, QWidget *parent = nullptr);
    explicit QtSlider(QWidget *parent = nullptr) : QtSlider(Qt::Orientation::Horizontal, parent) {};
    ~QtSlider();

    int value() const;
    double minimum() const;
    double maximum() const;
    bool bounded() const;

    QValidator::State validate(QString &input, int &pos) const;
    bool eventFilter(QObject *obj, QEvent *ev);

public Q_SLOTS:
    void setValue(int val);
    void setMinimum(double min);
    void setMaximum(double max);
    void setRange(double min, double max);
    void setBounded(bool bounded);

Q_SIGNALS:
    void valueChanged(int val);
    void destroyed(QObject *obj);

private:
    QtSliderPrivate *d_ptr;
    Q_DISABLE_COPY(QtSlider)
    Q_DECLARE_PRIVATE(QtSlider)

public:
    QString num2str();
    static QString num2str(int val, int minVal, int maxVal);
    static int str2num(const QString &text);
};

class QtDoubleSpinBoxPrivate;

class QtDoubleSpinBox : public QWidget
{
    Q_OBJECT
    Q_ENUMS(Format)
public:

    explicit QtDoubleSpinBox(QWidget *parent = nullptr);
    ~QtDoubleSpinBox();

    double value() const;
    double minimum() const;
    double maximum() const;
    int precision() const;
    Scale scale() const;
    Format format() const;
    bool bounded() const;

    QValidator::State validate(QString &input, int &pos) const;
    bool eventFilter(QObject *obj, QEvent *ev);

public Q_SLOTS:
    void setValue();
    void setValue(double val);
    void setMinimum(double min);
    void setMaximum(double max);
    void setRange(double min, double max);
    void setPrecision(int);
    void setScale(Scale);
    void setFormat(Format);
    void setReadOnly(bool readOnly);
    void setBounded(bool bounded);

Q_SIGNALS:
    void valueChanged(double val);
    void destroyed(QObject *obj);

private:
    QtDoubleSpinBoxPrivate *d_ptr;
    Q_DISABLE_COPY(QtDoubleSpinBox)
    Q_DECLARE_PRIVATE(QtDoubleSpinBox)

public:
    QString num2str();
    static QString num2str(double val, Scale scale, Format format, int precision, double minVal, double maxVal,
                           double &atol, double &rTol, double &ftol, int &decimals);
    static double str2num(const QString &text, const Scale scale, const Format format);
};



class QSciDoubleSpinBox : public QDoubleSpinBox
{
Q_OBJECT
public:
    explicit QSciDoubleSpinBox(QWidget *parent = 0);

    void setData(QtDoubleSpinBoxPrivate *data);
    void setValue(double val);
    double valueFromText(const QString & text) const;
    QString textFromValue(double value) const;
    QValidator::State validate(QString &text, int &pos) const;
private:
    QtDoubleSpinBoxPrivate *d_ptr;
    friend QtDoubleSpinBoxPrivate;private:
    QRegularExpressionValidator *validator;
};

class QtDoubleEditPrivate;

class QtDoubleEdit : public QWidget
{
    Q_OBJECT
    Q_ENUMS(Format)
public:

    explicit QtDoubleEdit(QWidget *parent = nullptr);
    ~QtDoubleEdit();

    double value() const;
    double minimum() const;
    double maximum() const;
    int precision() const;
    Scale scale() const;
    Format format() const;
    bool bounded() const;

    QValidator::State validate(QString &input, int &pos) const;
    bool eventFilter(QObject *obj, QEvent *ev);

public Q_SLOTS:
    void setValue();
    void setValue(double val);
    void setMinimum(double min);
    void setMaximum(double max);
    void setRange(double min, double max);
    void setPrecision(int);
    void setScale(Scale);
    void setFormat(Format);
    void setReadOnly(bool readOnly);
    void setBounded(bool bounded);

Q_SIGNALS:
    void valueChanged(double val);
    void destroyed(QObject *obj);

private:
    QtDoubleEditPrivate *d_ptr;
    Q_DISABLE_COPY(QtDoubleEdit)
    Q_DECLARE_PRIVATE(QtDoubleEdit)

public:
    QString num2str();
    static QString num2str(double val, Scale scale, Format format, int precision, double minVal, double maxVal,
                           double &atol, double &rTol, double &ftol, int &decimals);
    static double str2num(const QString &text, const Scale scale, const Format format);
};

class QtComplexEditPrivate;

class QtComplexEdit : public QWidget
{
    Q_OBJECT
    Q_ENUMS(Format)
public:
    explicit QtComplexEdit(QWidget *parent = nullptr);
    ~QtComplexEdit();

    QtComplex value() const;
    QtComplex minimum() const;
    QtComplex maximum() const;
    int precision() const;
    Scale scale() const;
    Format format() const;

    QValidator::State validate(QString &input, int &pos) const;
    bool eventFilter(QObject *obj, QEvent *ev);

    public Q_SLOTS:
    void setValue();
    void setValue(const QtComplex &val);
    void setMinimum(double min);
    void setMaximum(double max);
    void setRange(double min, double max);
    void setPrecision(int);
    void setScale(Scale);
    void setFormat(Format);
    void setReadOnly(bool readOnly);

Q_SIGNALS:
    void valueChanged(const QtComplex &val);
    void destroyed(QObject *obj);

private:
    QtComplexEditPrivate *d_ptr;
    Q_DISABLE_COPY(QtComplexEdit)
    Q_DECLARE_PRIVATE(QtComplexEdit)

public:
    QString num2str();
    static QString num2str(QtComplex val, Scale scale, Format format, int precision, QtComplex minVal, QtComplex maxVal,
                           QtComplex &atol, QtComplex &rTol, QtComplex &ftol, int &decimals);
    static QtComplex str2num(const QString &text, const Scale scale, const Format format);
};

class QtQuaternionEditPrivate;

class QtQuaternionEdit : public QWidget
{
Q_OBJECT
    Q_ENUMS(Format)
public:
    explicit QtQuaternionEdit(QWidget *parent = nullptr);
    ~QtQuaternionEdit();

    QtQuaternion value() const;
    QtQuaternion minimum() const;
    QtQuaternion maximum() const;
    int precision() const;
    Scale scale() const;
    Format format() const;
    bool polarized() const;

    QValidator::State validate(QString &input, int &pos) const;
    bool eventFilter(QObject *obj, QEvent *ev);

public Q_SLOTS:
    void setValue();
    void setValue(const QtQuaternion &val);
    void setMinimum(double min);
    void setMaximum(double max);
    void setRange(double min, double max);
    void setPrecision(int);
    void setScale(Scale);
    void setFormat(Format);
    void setReadOnly(bool readOnly);
    void setPolarized(bool polarized);

Q_SIGNALS:
    void valueChanged(const QtQuaternion &val);
    void destroyed(QObject *obj);

private:
    QtQuaternionEditPrivate *d_ptr;
    Q_DISABLE_COPY(QtQuaternionEdit)
    Q_DECLARE_PRIVATE(QtQuaternionEdit)

public:
    QString num2str();
    static QString num2str(QtQuaternion val, Scale scale, Format format, bool polarized, int precision, QtQuaternion minVal, QtQuaternion maxVal,
                           QtQuaternion &atol, QtQuaternion &rTol, QtQuaternion &ftol, int &decimals);
    static QtQuaternion str2num(const QString &text, const Scale scale, const Format format, const bool polarized);
};

class QtCharEdit : public QWidget
{
Q_OBJECT
public:
    QtCharEdit(QWidget *parent = 0);

    QChar value() const;
    bool eventFilter(QObject *o, QEvent *e) override;
public Q_SLOTS:
    void setValue(const QChar &value);
Q_SIGNALS:
    void valueChanged(const QChar &value);
protected:
    void focusInEvent(QFocusEvent *e) override;
    void focusOutEvent(QFocusEvent *e) override;
    void keyPressEvent(QKeyEvent *e) override;
    void keyReleaseEvent(QKeyEvent *e) override;
    bool event(QEvent *e) override;
private slots:
    void slotClearChar();
private:
    void handleKeyEvent(QKeyEvent *e);

    QChar m_value;
    QLineEdit *m_lineEdit;
};

class QtColorEditWidget : public QWidget {
    Q_OBJECT

public:
    QtColorEditWidget(QWidget *parent);

    QColor value() const;
    bool eventFilter(QObject *obj, QEvent *ev) override;

public Q_SLOTS:
    void setValue(const QColor &value);

private Q_SLOTS:
    void buttonClicked();

Q_SIGNALS:
    void valueChanged(const QColor &value);

private:
    QColor m_color;
    QLabel *m_pixmapLabel;
    QLabel *m_label;
    QToolButton *m_button;
};

class QtFontEditWidget : public QWidget {
    Q_OBJECT

public:
    QtFontEditWidget(QWidget *parent);

    QFont value() const;
    bool eventFilter(QObject *obj, QEvent *ev) override;

public Q_SLOTS:
    void setValue(const QFont &value);

private Q_SLOTS:
    void buttonClicked();

Q_SIGNALS:
    void valueChanged(const QFont &value);

private:
    QFont m_font;
    QLabel *m_pixmapLabel;
    QLabel *m_label;
    QToolButton *m_button;
};

class QtFileEdit : public QWidget {
Q_OBJECT

public:
    QtFileEdit(QWidget *parent);
    ~QtFileEdit();

    QString value() const;
    QString filter() const;
    QFileDialog::FileMode fileMode() const;
    bool eventFilter(QObject *obj, QEvent *ev);

    bool fileExists(QString path) const;
    bool validExtension(QString path) const;

public Q_SLOTS:
    void setValue(const QString &value);
    void setFilter(const QString &filter);
    void setFileMode(const QFileDialog::FileMode mode);
    void setReadOnly(const bool readOnly);

Q_SIGNALS:
    void valueChanged(const QString &value);
    void destroyed(QObject *obj);

private Q_SLOTS:
    void slotEditFinished();
    void slotButtonClicked();

private:
    QString m_fileName;
    QString m_filter;
    QFileDialog::FileMode m_fileMode;
    bool m_readOnly;
    QLineEdit *m_edit;
    QToolButton *m_button;
};

class QtMetaEnumWrapper : public QObject
{
Q_OBJECT
    Q_PROPERTY(QSizePolicy::Policy policy READ policy)
public:
    QSizePolicy::Policy policy() const { return QSizePolicy::Ignored; }
private:
    QtMetaEnumWrapper(QObject *parent) : QObject(parent) {}
};

class QtMetaEnumProvider
{
public:
    QtMetaEnumProvider();

    QStringList policyEnumNames() const { return m_policyEnumNames; }
    QStringList languageEnumNames() const { return m_languageEnumNames; }
    QStringList territoryEnumNames(QLocale::Language language) const { return m_territoryEnumNames.value(language); }

    QSizePolicy::Policy indexToSizePolicy(int index) const;
    int sizePolicyToIndex(QSizePolicy::Policy policy) const;

    void indexToLocale(int languageIndex, int territoryIndex, QLocale::Language *language, QLocale::Territory *territory) const;
    void localeToIndex(QLocale::Language language, QLocale::Territory territory, int *languageIndex, int *territoryIndex) const;

private:
    void initLocale();

    QStringList m_policyEnumNames;
    QStringList m_languageEnumNames;
    QMap<QLocale::Language, QStringList> m_territoryEnumNames;
    QMap<int, QLocale::Language> m_indexToLanguage;
    QMap<QLocale::Language, int> m_languageToIndex;
    QMap<int, QMap<int, QLocale::Territory> > m_indexToTerritory;
    QMap<QLocale::Language, QMap<QLocale::Territory, int> > m_territoryToIndex;
    QMetaEnum m_policyEnum;
};

QT_END_NAMESPACE

#endif
