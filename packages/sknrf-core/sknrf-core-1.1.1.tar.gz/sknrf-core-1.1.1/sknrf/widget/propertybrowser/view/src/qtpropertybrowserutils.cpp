// Copyright (C) 2016 The Qt Company Ltd.
// SPDX-License-Identifier: LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only

#include "qtpropertybrowserutils_p.h"
#include <QtWidgets/QApplication>
#include <QtGui/QPainter>
#include <QtWidgets/QHBoxLayout>
#include <QtGui/QMouseEvent>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMenu>
#include <QtCore/QLocale>
#include <QtCore/QKeyCombination>
#include <QtGui/QKeyEvent>
#include <QtCore/QMap>
#include <QtGui/QPainter>
#include <QtWidgets/QStyleOption>
#include <QtWidgets/QSpinBox>
#include <QtWidgets/QSlider>
#include <QtWidgets/QDoubleSpinBox>
#include <QtWidgets/QScrollBar>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QAbstractItemView>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QDateTimeEdit>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QMenu>
#include <QtWidgets/QApplication>
#include <QtWidgets/QLabel>
#include <QtWidgets/QToolButton>
#include <QtWidgets/QColorDialog>
#include <QtWidgets/QFontDialog>
#include <QtWidgets/QFileDialog>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QStyleOption>

#include <cmath>
#include <float.h>
#include <complex>
#include <stdio.h>
#include <iostream>

#ifdef Q_CC_MSVC
    #define isnan(x) _isnan(x)
    #define isinfinite(x) (!_finite(x) && !isnan(x))
    #define fpu_error(x) (isinf(x) || isnan(x))
#else
    #define isnan(x) std::isnan(x)
    #define isinfinite(x) std::isinf(x)
    #define fpu_error(x) (isinf(x) || isnan(x))
#endif

double infinity(std::numeric_limits<double>::infinity());
double neg_infinity(-std::numeric_limits<double>::infinity());
double highest(std::numeric_limits<double>::max()/2); // Divide Dynamic Range by 2 to avoid overflow
double lowest(-std::numeric_limits<double>::max()/2); // Divide Dynamic Range by 2 to avoid overflow
double epsilon(std::numeric_limits<double>::epsilon());
double minest(std::numeric_limits<double>::min());

bool isclose(int a, int b, int atol, int rtol)
{
    Q_UNUSED(atol);
    Q_UNUSED(rtol);
    return a == b;
}

bool isclose(QtComplex a, QtComplex b, QtComplex atol, QtComplex rtol)
{
    if (std::abs(a-b) <= std::max( std::abs(rtol) * std::max(std::abs(a), std::abs(b)), std::abs(atol)))
        return true;
    else
        return false;
}

bool isclose(QtQuaternion a, QtQuaternion b, QtQuaternion atol, QtQuaternion rtol)
{
    if ((a-b).length() <= std::max( rtol.length() * std::max(a.length(), b.length()), atol.length()))
        return true;
    else
        return false;
}

bool isclose(QVector<QtComplex> a, QVector<QtComplex> b, QVector<QtComplex> atol, QVector<QtComplex> rtol)
{
    for (unsigned short idx=0; idx < a.size(); idx++) {
        if (!isclose(a[idx], b[idx], atol[idx], rtol[idx]))
            return false;
    }
    return true;
}

bool isclose(QDate a, QDate b, QDate atol, QDate rtol)
{
    Q_UNUSED(atol);
    Q_UNUSED(rtol);
    return a == b;
}

bool isclose(QSize a, QSize b, QSize atol, QSize rtol)
{
    return (isclose(a.width(), b.width(), atol.width(), rtol.width()) &&
            isclose(a.height(), b.height(), atol.height(), rtol.height()));
}

bool isclose(QPointF a, QPointF b, QPointF atol, QPointF rtol)
{
    return (isclose(a.x(), b.x(), atol.x(), rtol.x()) &&
            isclose(a.y(), b.y(), atol.y(), rtol.y()));
}

bool isclose(QSizeF a, QSizeF b, QSizeF atol, QSizeF rtol)
{
    return (isclose(a.width(), b.width(), atol.width(), rtol.width()) &&
            isclose(a.height(), b.height(), atol.height(), rtol.height()));
}

bool isclose(QRectF a, QRectF b, QRectF atol, QRectF rtol)
{
    return (isclose(a.x(), b.x(), atol.x(), rtol.x()) &&
            isclose(a.y(), b.y(), atol.y(), rtol.y()) &&
            isclose(a.width(), b.width(), atol.width(), rtol.width()) &&
            isclose(a.height(), b.height(), atol.height(), rtol.height()));
}

const QString regPrefix = "\\s*";
const QRegularExpression regDecimal = QRegularExpression(
        "(?:"
        "("
        "[+-]?(?:(?:\\d+(?:\\.\\d*)?)|\\.\\d+|inf)" // Decimal
        "(?:[eE][+-]?[0-9]+)?" // Optional Scientific Notation
        ")"
        "\\,?\\s*)+");  // Optional Comma Separated Values
const QString regSuffix = ".*";
const QRegularExpression regExps[4] = {
        QRegularExpression(regPrefix
                           + regDecimal.pattern()
                           + regSuffix),
        QRegularExpression(regPrefix
                           + regDecimal.pattern()+ "?"
                           + "(?:\\s*[+-]\\s*)?"
                           + "(?:" + regDecimal.pattern() + "[Ii])?"
                           + "(?:\\s*[+-]\\s*)?"
                           + "(?:" + regDecimal.pattern() + "[Jj])?"
                           + "(?:\\s*[+-]\\s*)?"
                           + "(?:" + regDecimal.pattern() + "[Kk])?"
                           + regSuffix),
        QRegularExpression(regPrefix
                           + regDecimal.pattern()
                           + "(?:\\s*[<∠]\\s*)?"
                           + regDecimal.pattern() + "?"
                           + regSuffix),
        QRegularExpression(regPrefix
                           + regDecimal.pattern()
                           + "(?:\\s*[<∠]\\s*)?"
                           + regDecimal.pattern() + "?"
                           + regSuffix),
};

const QRegularExpression regExpSeps[4] = {
        QRegularExpression("[+-]"),
        QRegularExpression("[+-]"),
        QRegularExpression("[<∠]"),
        QRegularExpression("[<∠]"),
};

QString double2str(double val, int precision)
{
    QString result;
    QTextStream text(&result);
    // "%0.*g" string format
    text.setFieldAlignment(QTextStream::AlignLeft);
    text.setNumberFlags(QTextStream::ForcePoint);
    text.setRealNumberNotation(QTextStream::SmartNotation);
    text.setRealNumberPrecision(precision + 1);
    text.setPadChar('0');
    if(val < lowest)
        text << "-inf";
    else if(val > highest)
        text << "inf";
    else
        text << val;
    return result;
}

QtComplex atolCalc(int precision, QtComplex minimum , QtComplex maximum){
    QtComplex atol = QtComplex((std::abs(maximum) - std::abs(minimum)) / (1 << precision));
    return atol;
}

QtQuaternion atolCalc(int precision, QtQuaternion minimum , QtQuaternion maximum){
    QtQuaternion atol = QtQuaternion(float((maximum.length() - minimum.length()) / float(1 << precision)));
    return atol;
}

QPointF atolCalc(int precision, const QPointF &minimum , const QPointF &maximum){
    QPointF atol;
    atol.setX(atolCalc(precision, minimum.x(), maximum.x()));
    atol.setY(atolCalc(precision, minimum.y(), maximum.y()));
    return atol;
}

QSizeF atolCalc(int precision, const QSizeF &minimum , const QSizeF &maximum){
    QSizeF atol;
    atol.setWidth(atolCalc(precision, minimum.width(), maximum.width()));
    atol.setHeight(atolCalc(precision, minimum.height(), maximum.height()));
    return atol;
}

QtComplex rtolCalc(int precision, QtComplex minimum , QtComplex maximum) {
    QtComplex rtol = QtComplex(rtolCalc(precision, std::abs(minimum), std::abs(maximum)));
    return rtol;
}

QtQuaternion rtolCalc(int precision, QtQuaternion minimum , QtQuaternion maximum) {
    QtQuaternion rtol = QtQuaternion(float(rtolCalc(precision, minimum.length(), maximum.length())));
    return rtol;
}

QPointF rtolCalc(int precision, const QPointF &minimum , const QPointF &maximum) {
    QPointF rtol;
    rtol.setX(rtolCalc(precision, minimum.x(), maximum.x()));
    rtol.setY(rtolCalc(precision, minimum.y(), maximum.y()));
    return rtol;
}

QSizeF rtolCalc(int precision, const QSizeF &minimum , const QSizeF &maximum) {
    QSizeF rtol;
    rtol.setWidth(rtolCalc(precision, minimum.width(), maximum.width()));
    rtol.setHeight(rtolCalc(precision, minimum.height(), maximum.height()));
    return rtol;
}

QPointF fmtCalc(Scale scale, Format format, const QPointF &val, bool inv){
    QPointF scaled_val;
    scaled_val.setX(fmtCalc(scale, format, val.x(), inv));
    scaled_val.setY(fmtCalc(scale, format, val.y(), inv));
    return scaled_val;
}

QSizeF fmtCalc(Scale scale, Format format, const QSizeF &val, bool inv){
    QSizeF scaled_val;
    scaled_val.setWidth(fmtCalc(scale, format, val.width(), inv));
    scaled_val.setHeight(fmtCalc(scale, format, val.height(), inv));
    return scaled_val;
}

int sigDigCalc(int precision, QtComplex minimum, QtComplex maximum, Scale scale, Format format, QtComplex ftol) {
    int sigDig = std::max(-int(std::floor(std::log10(std::abs(ftol)))), 1);
    return sigDig;
}

int sigDigCalc(int precision, QtQuaternion minimum, QtQuaternion maximum, Scale scale, Format format, QtQuaternion ftol) {
    int sigDig = std::max(-int(std::floor(std::log10(ftol.length()))), 1);
    return sigDig;
}

int sigDigCalc(int precision, const QPointF &minimum, const QPointF &maximum, Scale scale, Format format, const QPointF &ftol) {
    int sigDig = std::max(std::max(
            -int(std::floor(std::log10(ftol.x()))),
            -int(std::floor(std::log10(ftol.y())))),
                   1);
    return sigDig;
}

int sigDigCalc(int precision, const QSizeF &minimum, const QSizeF &maximum, Scale scale, Format format, const QSizeF &ftol) {
    int sigDig = std::max(std::max(
                                  -int(std::floor(std::log10(ftol.width()))),
                                  -int(std::floor(std::log10(ftol.height())))),
                          1);
    return sigDig;
}

QMap<Format, QString> FormatNameMap = {
    {Format::RE, "Re"},
    {Format::RE_IM, "Re+Imj"},
    {Format::LIN_DEG, QString("Lin∠Deg")},
    {Format::LOG_DEG, QString("Log∠Deg")}
};

QMap<Scale, QString> ScaleNameMap = {
    {Scale::T, "T"},
    {Scale::G, "G"},
    {Scale::M, "M"},
    {Scale::K, "K"},
    {Scale::_, " "},
    {Scale::m, "m"},
    {Scale::u, "u"},
    {Scale::n, "n"},
    {Scale::p, "p"},
};
QMap<Scale, int> ScaleValueMap = {
    {Scale::T, 12},
    {Scale::G, 9},
    {Scale::M, 6},
    {Scale::K, 3},
    {Scale::_, 0},
    {Scale::m, -3},
    {Scale::u, -6},
    {Scale::n, -9},
    {Scale::p, -12},
};
QMap<Scale, int> InvScaleValueMap = {
        {Scale::T, -12},
        {Scale::G, -9},
        {Scale::M, -6},
        {Scale::K, -3},
        {Scale::_, 0},
        {Scale::m, 3},
        {Scale::u, 6},
        {Scale::n, 9},
        {Scale::p, 12},
};

QMap<PkAvg, QString> PkAvgNameMap = {
    {PkAvg::PK, "pk"},
    {PkAvg::AVG, "avg"},
};
QMap<Domain, QString> DomainNameMap = {
    {Domain::TF, "TF"},
    {Domain::FF, "FF"},
    {Domain::FT, "FT"},
    {Domain::TT, "TT"},
    {Domain::TH, "TH"},
};
QMap<BrowserCol, QString> AttributeNameMap = {
    {BrowserCol::MINIMUM, "Minimum"},
    {BrowserCol::MAXIMUM, "Maximum"},
    {BrowserCol::UNIT, "Unit"},
    {BrowserCol::PKAVG, "PkAvg"},
    {BrowserCol::FORMAT, "Format"},
    {BrowserCol::CHECK, "Check"},
};

// Set a hard coded left margin to account for the indentation
// of the tree view icon when switching to an editor
static inline void setupTreeViewEditorMargin(QLayout *lt)
{
    enum { DecorationMargin = 4 };
    if (QApplication::layoutDirection() == Qt::LeftToRight)
        lt->setContentsMargins(DecorationMargin, 0, 0, 0);
    else
        lt->setContentsMargins(0, 0, DecorationMargin, 0);
}

// QtComplex
QtComplex::QtComplex(std::complex<double> parent)
: std::complex<double>(parent)
{

}

QtComplex::QtComplex(double re, double im)
: std::complex<double>(re,im)
{

}

QT_BEGIN_NAMESPACE

QtCursorDatabase::QtCursorDatabase()
{
    appendCursor(Qt::ArrowCursor, QCoreApplication::translate("QtCursorDatabase", "Arrow"),
                 QIcon(QLatin1String(":/qt-project.org/qtpropertybrowser/images/cursor-arrow.png")));
    appendCursor(Qt::UpArrowCursor, QCoreApplication::translate("QtCursorDatabase", "Up Arrow"),
                 QIcon(QLatin1String(":/qt-project.org/qtpropertybrowser/images/cursor-uparrow.png")));
    appendCursor(Qt::CrossCursor, QCoreApplication::translate("QtCursorDatabase", "Cross"),
                 QIcon(QLatin1String(":/qt-project.org/qtpropertybrowser/images/cursor-cross.png")));
    appendCursor(Qt::WaitCursor, QCoreApplication::translate("QtCursorDatabase", "Wait"),
                 QIcon(QLatin1String(":/qt-project.org/qtpropertybrowser/images/cursor-wait.png")));
    appendCursor(Qt::IBeamCursor, QCoreApplication::translate("QtCursorDatabase", "IBeam"),
                 QIcon(QLatin1String(":/qt-project.org/qtpropertybrowser/images/cursor-ibeam.png")));
    appendCursor(Qt::SizeVerCursor, QCoreApplication::translate("QtCursorDatabase", "Size Vertical"),
                 QIcon(QLatin1String(":/qt-project.org/qtpropertybrowser/images/cursor-sizev.png")));
    appendCursor(Qt::SizeHorCursor, QCoreApplication::translate("QtCursorDatabase", "Size Horizontal"),
                 QIcon(QLatin1String(":/qt-project.org/qtpropertybrowser/images/cursor-sizeh.png")));
    appendCursor(Qt::SizeFDiagCursor, QCoreApplication::translate("QtCursorDatabase", "Size Backslash"),
                 QIcon(QLatin1String(":/qt-project.org/qtpropertybrowser/images/cursor-sizef.png")));
    appendCursor(Qt::SizeBDiagCursor, QCoreApplication::translate("QtCursorDatabase", "Size Slash"),
                 QIcon(QLatin1String(":/qt-project.org/qtpropertybrowser/images/cursor-sizeb.png")));
    appendCursor(Qt::SizeAllCursor, QCoreApplication::translate("QtCursorDatabase", "Size All"),
                 QIcon(QLatin1String(":/qt-project.org/qtpropertybrowser/images/cursor-sizeall.png")));
    appendCursor(Qt::BlankCursor, QCoreApplication::translate("QtCursorDatabase", "Blank"),
                 QIcon());
    appendCursor(Qt::SplitVCursor, QCoreApplication::translate("QtCursorDatabase", "Split Vertical"),
                 QIcon(QLatin1String(":/qt-project.org/qtpropertybrowser/images/cursor-vsplit.png")));
    appendCursor(Qt::SplitHCursor, QCoreApplication::translate("QtCursorDatabase", "Split Horizontal"),
                 QIcon(QLatin1String(":/qt-project.org/qtpropertybrowser/images/cursor-hsplit.png")));
    appendCursor(Qt::PointingHandCursor, QCoreApplication::translate("QtCursorDatabase", "Pointing Hand"),
                 QIcon(QLatin1String(":/qt-project.org/qtpropertybrowser/images/cursor-hand.png")));
    appendCursor(Qt::ForbiddenCursor, QCoreApplication::translate("QtCursorDatabase", "Forbidden"),
                 QIcon(QLatin1String(":/qt-project.org/qtpropertybrowser/images/cursor-forbidden.png")));
    appendCursor(Qt::OpenHandCursor, QCoreApplication::translate("QtCursorDatabase", "Open Hand"),
                 QIcon(QLatin1String(":/qt-project.org/qtpropertybrowser/images/cursor-openhand.png")));
    appendCursor(Qt::ClosedHandCursor, QCoreApplication::translate("QtCursorDatabase", "Closed Hand"),
                 QIcon(QLatin1String(":/qt-project.org/qtpropertybrowser/images/cursor-closedhand.png")));
    appendCursor(Qt::WhatsThisCursor, QCoreApplication::translate("QtCursorDatabase", "What's This"),
                 QIcon(QLatin1String(":/qt-project.org/qtpropertybrowser/images/cursor-whatsthis.png")));
    appendCursor(Qt::BusyCursor, QCoreApplication::translate("QtCursorDatabase", "Busy"),
                 QIcon(QLatin1String(":/qt-project.org/qtpropertybrowser/images/cursor-busy.png")));
}

void QtCursorDatabase::clear()
{
    m_cursorNames.clear();
    m_cursorIcons.clear();
    m_valueToCursorShape.clear();
    m_cursorShapeToValue.clear();
}

void QtCursorDatabase::appendCursor(Qt::CursorShape shape, const QString &name, const QIcon &icon)
{
    if (m_cursorShapeToValue.contains(shape))
        return;
    const int value = m_cursorNames.size();
    m_cursorNames.append(name);
    m_cursorIcons.insert(value, icon);
    m_valueToCursorShape.insert(value, shape);
    m_cursorShapeToValue.insert(shape, value);
}

QStringList QtCursorDatabase::cursorShapeNames() const
{
    return m_cursorNames;
}

QMap<int, QIcon> QtCursorDatabase::cursorShapeIcons() const
{
    return m_cursorIcons;
}

QString QtCursorDatabase::cursorToShapeName(const QCursor &cursor) const
{
    int val = cursorToValue(cursor);
    if (val >= 0)
        return m_cursorNames.at(val);
    return QString();
}

QIcon QtCursorDatabase::cursorToShapeIcon(const QCursor &cursor) const
{
    int val = cursorToValue(cursor);
    return m_cursorIcons.value(val);
}

int QtCursorDatabase::cursorToValue(const QCursor &cursor) const
{
#ifndef QT_NO_CURSOR
    Qt::CursorShape shape = cursor.shape();
    if (m_cursorShapeToValue.contains(shape))
        return m_cursorShapeToValue[shape];
#endif
    return -1;
}

#ifndef QT_NO_CURSOR
QCursor QtCursorDatabase::valueToCursor(int value) const
{
    if (m_valueToCursorShape.contains(value))
        return QCursor(m_valueToCursorShape[value]);
    return QCursor();
}
#endif

QPixmap QtPropertyBrowserUtils::brushValuePixmap(const QBrush &b)
{
    QImage img(16, 16, QImage::Format_ARGB32_Premultiplied);
    img.fill(0);

    QPainter painter(&img);
    painter.setCompositionMode(QPainter::CompositionMode_Source);
    painter.fillRect(0, 0, img.width(), img.height(), b);
    QColor color = b.color();
    if (color.alpha() != 255) { // indicate alpha by an inset
        QBrush  opaqueBrush = b;
        color.setAlpha(255);
        opaqueBrush.setColor(color);
        painter.fillRect(img.width() / 4, img.height() / 4,
                         img.width() / 2, img.height() / 2, opaqueBrush);
    }
    painter.end();
    return QPixmap::fromImage(img);
}

QIcon QtPropertyBrowserUtils::brushValueIcon(const QBrush &b)
{
    return QIcon(brushValuePixmap(b));
}

QString QtPropertyBrowserUtils::colorValueText(const QColor &c)
{
    return QCoreApplication::translate("QtPropertyBrowserUtils", "[%1, %2, %3] (%4)")
           .arg(c.red()).arg(c.green()).arg(c.blue()).arg(c.alpha());
}

QPixmap QtPropertyBrowserUtils::fontValuePixmap(const QFont &font)
{
    QFont f = font;
    QImage img(16, 16, QImage::Format_ARGB32_Premultiplied);
    img.fill(0);
    QPainter p(&img);
    p.setRenderHint(QPainter::TextAntialiasing, true);
    p.setRenderHint(QPainter::Antialiasing, true);
    f.setPointSize(13);
    p.setFont(f);
    QTextOption t;
    t.setAlignment(Qt::AlignCenter);
    p.drawText(QRect(0, 0, 16, 16), QString(QLatin1Char('A')), t);
    return QPixmap::fromImage(img);
}

QIcon QtPropertyBrowserUtils::fontValueIcon(const QFont &f)
{
    return QIcon(fontValuePixmap(f));
}

QString QtPropertyBrowserUtils::fontValueText(const QFont &f)
{
    return QCoreApplication::translate("QtPropertyBrowserUtils", "[%1, %2]")
           .arg(f.family()).arg(f.pointSize());
}

QString QtPropertyBrowserUtils::dateFormat()
{
    QLocale loc;
    QString format = loc.dateFormat(QLocale::ShortFormat);
    // Change dd.MM.yy, MM/dd/yy to 4 digit years
    if (format.count(QLatin1Char('y')) == 2)
        format.insert(format.indexOf(QLatin1Char('y')), QLatin1String("yy"));
    return format;
}

QString QtPropertyBrowserUtils::timeFormat()
{
    QLocale loc;
    // ShortFormat is missing seconds on UNIX.
    return loc.timeFormat(QLocale::LongFormat);
}

QString QtPropertyBrowserUtils::dateTimeFormat()
{
    QString format = dateFormat();
    format += QLatin1Char(' ');
    format += timeFormat();
    return format;
}

QtBoolEdit::QtBoolEdit(QWidget *parent) :
    QWidget(parent),
    m_checkBox(new QCheckBox(this)),
    m_textVisible(true)
{
    QHBoxLayout *lt = new QHBoxLayout;
    if (QApplication::layoutDirection() == Qt::LeftToRight)
        lt->setContentsMargins(4, 0, 0, 0);
    else
        lt->setContentsMargins(0, 0, 4, 0);
    lt->addWidget(m_checkBox);
    setLayout(lt);
    connect(m_checkBox, SIGNAL(toggled(bool)), this, SIGNAL(toggled(bool)));
    setFocusProxy(m_checkBox);
    m_checkBox->setText(tr("True"));
}

void QtBoolEdit::setTextVisible(bool textVisible)
{
    if (m_textVisible == textVisible)
        return;

    m_textVisible = textVisible;
    if (m_textVisible)
        m_checkBox->setText(isChecked() ? tr("True") : tr("False"));
    else
        m_checkBox->setText(QString());
}

Qt::CheckState QtBoolEdit::checkState() const
{
    return m_checkBox->checkState();
}

void QtBoolEdit::setCheckState(Qt::CheckState state)
{
    m_checkBox->setCheckState(state);
}

bool QtBoolEdit::isChecked() const
{
    return m_checkBox->isChecked();
}

void QtBoolEdit::setChecked(bool c)
{
    m_checkBox->setChecked(c);
    if (!m_textVisible)
        return;
    m_checkBox->setText(isChecked() ? tr("True") : tr("False"));
}

bool QtBoolEdit::blockCheckBoxSignals(bool block)
{
    return m_checkBox->blockSignals(block);
}

void QtBoolEdit::mousePressEvent(QMouseEvent *event)
{
    if (event->buttons() == Qt::LeftButton) {
        m_checkBox->click();
        event->accept();
    } else {
        QWidget::mousePressEvent(event);
    }
}

// QtSpinBox

/*!
    \class QtSpinBoxPrivate
    \internal
    \inmodule QtDesigner
    \since 4.4

    \brief A Private d_ptr of QtSpinBox.

    \sa QtSpinBox
*/
class QtSpinBoxPrivate
{
    QtSpinBox *q_ptr;
    Q_DECLARE_PUBLIC(QtSpinBox)
public:
    QtSpinBoxPrivate()
            : m_value(0),
              m_minimum(lowest),
              m_maximum(highest),
              m_atol(std::numeric_limits<double>::epsilon()),
              m_rtol(std::numeric_limits<double>::min()),
              m_readOnly(false),
              m_bounded(true),
              m_spinBox(nullptr){}

    int m_value;
    double m_minimum;
    double m_maximum;
    double m_atol;
    double m_rtol;
    bool m_readOnly;
    bool m_bounded;
    QSpinBox* m_spinBox;

private:
    QRegularExpressionValidator *validator;
};

/*!
    \class QtSpinBox
    \internal
    \inmodule QtDesigner
    \since 4.4

    \brief An editor that renders integer data using a QSpinbox.

    \sa QtSpinBoxPrivate, QSpinBox, int
*/
QtSpinBox::QtSpinBox(QWidget *parent) :
        QWidget(parent)
{
    d_ptr = new QtSpinBoxPrivate();
    d_ptr->q_ptr = this;

    d_ptr->m_spinBox = new QSpinBox();
    d_ptr->validator = new QRegularExpressionValidator(regExps[Format::RE], this);

    QHBoxLayout *lt = new QHBoxLayout(this);
    setupTreeViewEditorMargin(lt);
    lt->setSpacing(0);
    lt->addWidget(d_ptr->m_spinBox);
    this->setFocusProxy(d_ptr->m_spinBox);

    connect(d_ptr->m_spinBox, SIGNAL(valueChanged(int)), this, SLOT(setValue(int)));
}

QtSpinBox::~QtSpinBox()
{
    disconnect(d_ptr->m_spinBox, SIGNAL(valueChanged(int)), this, SLOT(setValue(int)));
    emit destroyed(this);
}

int QtSpinBox::value() const
{
    return d_ptr->m_value;
}

double QtSpinBox::minimum() const
{
    return d_ptr->m_minimum;
}

double QtSpinBox::maximum() const
{
    return d_ptr->m_maximum;
}

bool QtSpinBox::bounded() const
{
    return d_ptr->m_bounded;
}

void QtSpinBox::setValue()
{
    QString text = d_ptr->m_spinBox->text();
    int pos = 0;
    int val;

    if (!d_ptr->m_readOnly && validate(text,pos))
    {
        val = QtSpinBox::str2num(d_ptr->m_spinBox->text());
        if (d_ptr->m_value != val) {
            d_ptr->m_value = val;
            emit valueChanged(val);
        }
    }
}

void QtSpinBox::setValue(int val)
{
    if (d_ptr->m_value != val) {
        d_ptr->m_value = val;
        if (d_ptr->m_bounded)
            d_ptr->m_spinBox->setValue(val);
        emit valueChanged(val);
    }
}

void QtSpinBox::setMinimum(double min)
{
    if (!isclose(min, d_ptr->m_minimum, d_ptr->m_atol, d_ptr->m_rtol)){
        if(d_ptr->m_value < min)
            setValue(int(min));
        d_ptr->m_minimum = min;
        if (d_ptr->m_bounded)
            d_ptr->m_spinBox->setValue(d_ptr->m_value);
    }
}

void QtSpinBox::setMaximum(double max)
{
    if (!isclose(max, d_ptr->m_maximum, d_ptr->m_atol, d_ptr->m_rtol)){
        if(d_ptr->m_value > max)
            setValue(int(max));
        d_ptr->m_maximum = max;
        if (d_ptr->m_bounded)
            d_ptr->m_spinBox->setValue(d_ptr->m_value);
    }
}

void QtSpinBox::setRange(double min, double max)
{
    if (min < max)
    {
        setMinimum(min);
        setMaximum(max);
    }
}

void QtSpinBox::setReadOnly(bool readOnly)
{
    if (d_ptr->m_readOnly != readOnly)
        d_ptr->m_spinBox->setReadOnly(readOnly);
}

void QtSpinBox::setBounded(bool bounded)
{
    d_ptr->m_bounded = bounded;
}

bool QtSpinBox::eventFilter(QObject *obj, QEvent *ev)
{
    return QWidget::eventFilter(obj, ev);
}

QValidator::State QtSpinBox::validate(QString &text, int &pos) const
{
    return d_ptr->validator->validate(text, pos);

}

QString QtSpinBox::num2str() {
    return QtSpinBox::num2str(
            d_ptr->m_value, d_ptr->m_minimum, d_ptr->m_maximum);
}

QString QtSpinBox::num2str(int val, int minVal, int maxVal) {
    QString text = QString::number(val);
    return text;
}

int QtSpinBox::str2num(const QString &text)
{
    int val = text.toInt();
    return val;
}

// QtIntEdit

/*!
    \class QtIntEditPrivate
    \internal
    \inmodule QtDesigner
    \since 4.4

    \brief A Private d_ptr of QtIntEdit.

    \sa QtIntEdit
*/
class QtIntEditPrivate
{
    QtIntEdit *q_ptr;
    Q_DECLARE_PUBLIC(QtIntEdit)
public:
    QtIntEditPrivate()
        : m_value(0),
          m_minimum(lowest),
          m_maximum(highest),
          m_atol(std::numeric_limits<double>::epsilon()),
          m_rtol(std::numeric_limits<double>::min()),
          m_readOnly(false),
          m_bounded(true),
          m_edit(nullptr){}

    int m_value;
    double m_minimum;
    double m_maximum;
    double m_atol;
    double m_rtol;
    bool m_readOnly;
    bool m_bounded;
    QLineEdit* m_edit;

private:
    QRegularExpressionValidator *validator;
};

/*!
    \class QtIntEdit
    \internal
    \inmodule QtDesigner
    \since 4.4

    \brief An editor that renders integer data using a QLineEdit.

    \sa QtIntEditPrivate, QLineEdit, int
*/
QtIntEdit::QtIntEdit(QWidget *parent) :
QWidget(parent)
{
    d_ptr = new QtIntEditPrivate();
    d_ptr->q_ptr = this;

    d_ptr->m_edit = new QLineEdit("0");
    d_ptr->validator = new QRegularExpressionValidator(regExps[Format::LIN_DEG], this);

    QHBoxLayout *lt = new QHBoxLayout(this);
    setupTreeViewEditorMargin(lt);
    lt->setSpacing(0);
    lt->addWidget(d_ptr->m_edit);
    this->setFocusProxy(d_ptr->m_edit);

    connect(d_ptr->m_edit, SIGNAL(editingFinished()), this, SLOT(setValue()));
}

QtIntEdit::~QtIntEdit()
{
    disconnect(d_ptr->m_edit, SIGNAL(editingFinished()), this, SLOT(setValue()));
    emit destroyed(this);
}

int QtIntEdit::value() const
{
    return d_ptr->m_value;
}

double QtIntEdit::minimum() const
{
    return d_ptr->m_minimum;
}

double QtIntEdit::maximum() const
{
    return d_ptr->m_maximum;
}

bool QtIntEdit::bounded() const
{
    return d_ptr->m_bounded;
}

void QtIntEdit::setValue()
{
    QString text = d_ptr->m_edit->text();
    int pos = 0;
    int val;

    if (!d_ptr->m_readOnly && validate(text,pos))
    {
        val = QtIntEdit::str2num(d_ptr->m_edit->text());
        if (d_ptr->m_value != val) {
            d_ptr->m_value = val;
            emit valueChanged(val);
        }
    }
}

void QtIntEdit::setValue(int val)
{
    if (d_ptr->m_value != val) {
        d_ptr->m_value = val;
        if (d_ptr->m_bounded)
            d_ptr->m_edit->setText(num2str());
        emit valueChanged(val);
    }
}

void QtIntEdit::setMinimum(double min)
{
    if (!isclose(min, d_ptr->m_minimum, d_ptr->m_atol, d_ptr->m_rtol)){
        if(d_ptr->m_value < min)
            setValue(int(min));
        d_ptr->m_minimum = min;
        if (d_ptr->m_bounded)
            d_ptr->m_edit->setText(num2str());
    }
}

void QtIntEdit::setMaximum(double max)
{
    if (!isclose(max, d_ptr->m_maximum, d_ptr->m_atol, d_ptr->m_rtol)){
        if(d_ptr->m_value > max)
            setValue(int(max));
        d_ptr->m_maximum = max;
        if (d_ptr->m_bounded)
            d_ptr->m_edit->setText(num2str());
    }
}

void QtIntEdit::setRange(double min, double max)
{
    if (min < max)
    {
        setMinimum(min);
        setMaximum(max);
    }
}

void QtIntEdit::setReadOnly(bool readOnly)
{
    if (d_ptr->m_readOnly != readOnly)
        d_ptr->m_edit->setReadOnly(readOnly);
}

void QtIntEdit::setBounded(bool bounded)
{
    d_ptr->m_bounded = bounded;
}

bool QtIntEdit::eventFilter(QObject *obj, QEvent *ev)
{
    return QWidget::eventFilter(obj, ev);
}

QValidator::State QtIntEdit::validate(QString &text, int &pos) const
{
    return d_ptr->validator->validate(text, pos);

}

QString QtIntEdit::num2str() {
    return QtIntEdit::num2str(
            d_ptr->m_value, d_ptr->m_minimum, d_ptr->m_maximum);
}

QString QtIntEdit::num2str(int val, int minVal, int maxVal) {
    QString text = QString::number(val);
    return text;
}

int QtIntEdit::str2num(const QString &text)
{
    int val = text.toInt();
    return val;
}

// QtSlider

/*!
    \class QtSliderPrivate
    \internal
    \inmodule QtDesigner
    \since 4.4

    \brief A Private d_ptr of QtSlider.

    \sa QtSlider
*/
class QtSliderPrivate
{
    QtSlider *q_ptr;
    Q_DECLARE_PUBLIC(QtSlider)
public:
    QtSliderPrivate()
            : m_value(0),
              m_minimum(lowest),
              m_maximum(highest),
              m_atol(std::numeric_limits<double>::epsilon()),
              m_rtol(std::numeric_limits<double>::min()),
              m_bounded(true),
              m_slider(nullptr){}

    int m_value;
    double m_minimum;
    double m_maximum;
    double m_atol;
    double m_rtol;
    bool m_bounded;
    QSlider* m_slider;

private:
};

/*!
    \class QtSlider
    \internal
    \inmodule QtDesigner
    \since 4.4

    \brief An editor that renders integer data using a QSlider.

    \sa QtSliderPrivate, QSlider, int
*/
QtSlider::QtSlider(Qt::Orientation orientation, QWidget *parent) :
        QWidget(parent)
{
    d_ptr = new QtSliderPrivate();
    d_ptr->q_ptr = this;

    d_ptr->m_slider = new QSlider();
    d_ptr->m_slider->setOrientation(orientation);

    QHBoxLayout *lt = new QHBoxLayout(this);
    setupTreeViewEditorMargin(lt);
    lt->setSpacing(0);
    lt->addWidget(d_ptr->m_slider);
    this->setFocusProxy(d_ptr->m_slider);

    connect(d_ptr->m_slider, SIGNAL(valueChanged(int)), this, SLOT(setValue(int)));
}

QtSlider::~QtSlider()
{
    disconnect(d_ptr->m_slider, SIGNAL(valueChanged(int)), this, SLOT(setValue(int)));
    emit destroyed(this);
}

int QtSlider::value() const
{
    return d_ptr->m_value;
}

double QtSlider::minimum() const
{
    return d_ptr->m_minimum;
}

double QtSlider::maximum() const
{
    return d_ptr->m_maximum;
}

bool QtSlider::bounded() const
{
    return d_ptr->m_bounded;
}

void QtSlider::setValue(int val)
{
    if (d_ptr->m_value != val) {
        d_ptr->m_value = val;
        if (d_ptr->m_bounded)
            d_ptr->m_slider->setValue(val);
        emit valueChanged(val);
    }
}

void QtSlider::setMinimum(double min)
{
    if (!isclose(min, d_ptr->m_minimum, d_ptr->m_atol, d_ptr->m_rtol)){
        if(d_ptr->m_value < min)
            setValue(int(min));
        d_ptr->m_minimum = min;
        if (d_ptr->m_bounded)
            d_ptr->m_slider->setValue(d_ptr->m_value);
    }
}

void QtSlider::setMaximum(double max)
{
    if (!isclose(max, d_ptr->m_maximum, d_ptr->m_atol, d_ptr->m_rtol)){
        if(d_ptr->m_value > max)
            setValue(int(max));
        d_ptr->m_maximum = max;
        if (d_ptr->m_bounded)
            d_ptr->m_slider->setValue(d_ptr->m_value);
    }
}

void QtSlider::setRange(double min, double max)
{
    if (min < max)
    {
        setMinimum(min);
        setMaximum(max);
    }
}

void QtSlider::setBounded(bool bounded)
{
    d_ptr->m_bounded = bounded;
}

bool QtSlider::eventFilter(QObject *obj, QEvent *ev)
{
    return QWidget::eventFilter(obj, ev);
}

QString QtSlider::num2str() {
    return QtSlider::num2str(
            d_ptr->m_value, d_ptr->m_minimum, d_ptr->m_maximum);
}

QString QtSlider::num2str(int val, int minVal, int maxVal) {
    QString text = QString::number(val);
    return text;
}

int QtSlider::str2num(const QString &text)
{
    int val = text.toInt();
    return val;
}

// QtDoubleSpinBox

/*!
    \class QtDoubleSpinBoxPrivate
    \internal
    \inmodule QtDesigner
    \since 4.4

    \brief A Private d_ptr of QtDoubleSpinBox.

    \sa QtDoubleSpinBox
*/
class QtDoubleSpinBoxPrivate
{
    QtDoubleSpinBox *q_ptr;
    Q_DECLARE_PUBLIC(QtDoubleSpinBox)
public:
    QtDoubleSpinBoxPrivate()
        : m_value(0),
          m_precision(63),
          m_atol(std::numeric_limits<double>::epsilon()),
          m_rtol(std::numeric_limits<double>::min()),
          m_ftol(std::numeric_limits<double>::epsilon()),
          m_decimals(2),
          m_format(Format::RE),
          m_scale(Scale::_),
          m_readOnly(false),
          m_bounded(true) {}

    double m_value;
    double m_minimum;
    double m_maximum;
    int m_precision;
    double m_atol;
    double m_rtol;
    double m_ftol;
    int m_decimals;
    Format m_format;
    Scale m_scale;
    bool m_readOnly;
    bool m_bounded;
    QSciDoubleSpinBox* m_sciDoubleSpinBox;

private:
    QRegularExpressionValidator *validator;
};

/*!
    \class QtDoubleSpinBox
    \internal
    \inmodule QtDesigner
    \since 4.4

    \brief An editor that renders double data using a QDoubleSpinBox.

    \sa QtDoubleSpinBoxPrivate, QDoubleSpinBox, double
*/
QtDoubleSpinBox::QtDoubleSpinBox(QWidget *parent) :
QWidget(parent)
{
    d_ptr = new QtDoubleSpinBoxPrivate();
    d_ptr->q_ptr = this;

    d_ptr->m_sciDoubleSpinBox = new QSciDoubleSpinBox();
    d_ptr->validator = new QRegularExpressionValidator(regExps[Format::RE], this);
    d_ptr->m_sciDoubleSpinBox->setData(d_ptr);

    QHBoxLayout *lt = new QHBoxLayout(this);
    setupTreeViewEditorMargin(lt);
    lt->setSpacing(0);
    lt->addWidget(d_ptr->m_sciDoubleSpinBox);
    this->setFocusProxy(d_ptr->m_sciDoubleSpinBox);

    connect(d_ptr->m_sciDoubleSpinBox, SIGNAL(editingFinished()), this, SLOT(setValue()));
}

QtDoubleSpinBox::~QtDoubleSpinBox()
{
    disconnect(d_ptr->m_sciDoubleSpinBox, SIGNAL(editingFinished()), this, SLOT(setValue()));
    emit destroyed(this);
}

double QtDoubleSpinBox::value() const
{
    return d_ptr->m_value;
}

double QtDoubleSpinBox::minimum() const
{
    return d_ptr->m_minimum;
}

double QtDoubleSpinBox::maximum() const
{
    return d_ptr->m_maximum;
}

int QtDoubleSpinBox::precision() const
{
    return d_ptr->m_precision;
}

Format QtDoubleSpinBox::format() const
{
    return d_ptr->m_format;
}

Scale QtDoubleSpinBox::scale() const
{
    return d_ptr->m_scale;
}

bool QtDoubleSpinBox::bounded() const
{
    return d_ptr->m_bounded;
}

void QtDoubleSpinBox::setValue()
{
    QString text = d_ptr->m_sciDoubleSpinBox->text();
    int pos = 0;
    double val;

    if (!d_ptr->m_readOnly && validate(text,pos))
    {
        val = str2num(d_ptr->m_sciDoubleSpinBox->text(), d_ptr->m_scale, d_ptr->m_format);
        setValue(val);
    }
}

void QtDoubleSpinBox::setValue(double val)
{
    if (!isclose(val, d_ptr->m_value, d_ptr->m_atol, d_ptr->m_rtol)){
        d_ptr->m_value = val;
        if (d_ptr->m_bounded)
            num2str();
        emit valueChanged(val);
    }
}

void QtDoubleSpinBox::setMinimum(double min)
{
    if (!isclose(min, d_ptr->m_minimum, d_ptr->m_atol, d_ptr->m_rtol)){
        if (d_ptr->m_value < min)
            setValue(min);
        d_ptr->m_minimum = min;
        d_ptr->m_sciDoubleSpinBox->setMinimum(min);
        if (d_ptr->m_bounded)
            num2str();
    }
}

void QtDoubleSpinBox::setMaximum(double max)
{
    if (!isclose(max, d_ptr->m_maximum, d_ptr->m_atol, d_ptr->m_rtol)){
        if (d_ptr->m_value > max)
            setValue(max);
        d_ptr->m_maximum = max;
        d_ptr->m_sciDoubleSpinBox->setMaximum(max);
        if (d_ptr->m_bounded)
            num2str();
    }
}

void QtDoubleSpinBox::setRange(double min, double max)
{
    if (min < max)
    {
        setMinimum(min);
        setMaximum(max);
    }
}

void QtDoubleSpinBox::setPrecision(int prec)
{
    d_ptr->m_precision = prec;
    if (d_ptr->m_bounded)
        num2str();
}

void QtDoubleSpinBox::setFormat(Format format_)
{
    if (d_ptr->m_format!= format_) {
        d_ptr->m_format = format_;
        d_ptr->validator->setRegularExpression(regExps[format_]);
        if (d_ptr->m_bounded)
            num2str();
    }
}

void QtDoubleSpinBox::setScale(Scale scale_)
{
    if (d_ptr->m_scale!= scale_) {
        d_ptr->m_scale = scale_;
        if (d_ptr->m_bounded)
            num2str();
    }
}

void QtDoubleSpinBox::setReadOnly(bool readOnly)
{
    if (d_ptr->m_readOnly != readOnly)
        d_ptr->m_sciDoubleSpinBox->setReadOnly(readOnly);
}

void QtDoubleSpinBox::setBounded(bool bounded)
{
    d_ptr->m_bounded = bounded;
}

bool QtDoubleSpinBox::eventFilter(QObject *obj, QEvent *ev)
{
    return QWidget::eventFilter(obj, ev);
}

QValidator::State QtDoubleSpinBox::validate(QString &text, int &pos) const
{
    return d_ptr->validator->validate(text, pos);
}

QString QtDoubleSpinBox::num2str() {
    QString text = QtDoubleEdit::num2str(
            d_ptr->m_value, d_ptr->m_scale, d_ptr->m_format, d_ptr->m_precision, d_ptr->m_minimum, d_ptr->m_maximum,
            d_ptr->m_atol, d_ptr->m_rtol, d_ptr->m_ftol, d_ptr->m_decimals);
    d_ptr->m_sciDoubleSpinBox->setDecimals(d_ptr->m_decimals);
    d_ptr->m_sciDoubleSpinBox->setValue(d_ptr->m_value);
    return text;
}

QString QtDoubleSpinBox::num2str(double val, Scale scale, Format format, int precision, double minVal, double maxVal,
                                 double &absTol, double &relTol, double &fmtTol, int &decimals) {
    QString text;
    double scaled_val = fmtCalc(scale, format, val);
    absTol = atolCalc(precision, minVal, maxVal);
    relTol = rtolCalc(precision, minVal, maxVal);
    fmtTol = fmtCalc(scale, format, absTol);
    decimals = sigDigCalc(precision, minVal, maxVal, scale, format, fmtTol);
    switch (format) {
        case Format::LOG_DEG:
            text = double2str(20*log10(scaled_val), decimals);
            break;
        default:
            text = double2str(scaled_val, decimals);
            break;
    }
    return text;
}

double QtDoubleSpinBox::str2num(const QString &text, const Scale scale, const Format format)
{
    int VALS_LENGTH = 1;
    QRegularExpressionMatch match;
    int scale_ = ScaleValueMap[scale];
    double val = 0;
    double vals[VALS_LENGTH];
    int valIndex = -1;
    for (QString seqStr : text.split(regExpSeps[format], Qt::SkipEmptyParts))
        for (QString subStr: seqStr.split("[,;]", Qt::SkipEmptyParts)) {
            valIndex += 1;
            match = regDecimal.match(subStr);
            if (!match.hasMatch() || valIndex > VALS_LENGTH)
                return 0;
            vals[valIndex] = match.captured(1).toDouble();
        }
    switch (format) {
        case Format::RE:
            val = double(vals[0]);
            val *= pow(10, scale_);
            break;
        case Format::RE_IM:
            val = double(vals[0]);
            val *= pow(10, scale_);
            break;
        case Format::LIN_DEG:
            val = double(vals[0]);
            val *= pow(10, scale_);
            break;
        case Format::LOG_DEG:
            val = double(std::pow(10, (vals[0]) / 20));
            val *= sqrt(pow(10, scale_));
            break;
        default:
            return 0;
    }
    if (isinfinite(std::abs(val)))
        val = 0;
    return val;
}

/*!
    \class QSciDoubleSpinBox
    \internal
    \inmodule QtDesigner
    \since 4.4

    \brief An editor that renders double data in Engineering Notation using a QDoubleSpinBox

    \sa QDoubleSpinBoxPrivate, double
*/
QSciDoubleSpinBox::QSciDoubleSpinBox(QWidget *parent) :
QDoubleSpinBox(parent) {
    validator = new QRegularExpressionValidator(regExps[Format::RE], this);
}

void QSciDoubleSpinBox::setValue(double val) {
    QDoubleSpinBox::setValue(val);
    switch (d_ptr->m_format) {
        case Format::LOG_DEG:
            setStepType(StepType::DefaultStepType);
            setSingleStep(0.0115794542598986* val); // 10**(0.1/20) = 0.1 dB step
            break;
        default:
            setStepType(StepType::AdaptiveDecimalStepType);
            break;
    }

}

void QSciDoubleSpinBox::setData(QtDoubleSpinBoxPrivate *data) {
    d_ptr = data;
}

double QSciDoubleSpinBox::valueFromText(const QString & text) const {
    return QtDoubleSpinBox::str2num(text, d_ptr->m_scale, d_ptr->m_format);
}

QString QSciDoubleSpinBox::textFromValue(double value) const {
    return QtDoubleSpinBox::num2str(
            value, d_ptr->m_scale, d_ptr->m_format, d_ptr->m_precision, d_ptr->m_minimum, d_ptr->m_maximum,
            d_ptr->m_atol, d_ptr->m_rtol, d_ptr->m_ftol, d_ptr->m_decimals);
}

QValidator::State QSciDoubleSpinBox::validate(QString &text, int &pos) const {
    return validator->validate(text, pos);
}

// QtDoubleEdit

/*!
    \class QtDoubleEditPrivate
    \internal
    \inmodule QtDesigner
    \since 4.4

    \brief A Private d_ptr of QtDoubleEdit.

    \sa QtDoubleEdit
*/
class QtDoubleEditPrivate
{
    QtDoubleEdit *q_ptr;
    Q_DECLARE_PUBLIC(QtDoubleEdit)
public:
    QtDoubleEditPrivate()
        : m_value(0),
          m_precision(63),
          m_atol(std::numeric_limits<double>::epsilon()),
          m_rtol(std::numeric_limits<double>::min()),
          m_ftol(std::numeric_limits<double>::epsilon()),
          m_decimals(2),
          m_format(Format::LIN_DEG),
          m_scale(Scale::_),
          m_readOnly(false),
          m_bounded(true) {}

    double m_value;
    double m_minimum;
    double m_maximum;
    int m_precision;
    double m_atol;
    double m_rtol;
    double m_ftol;
    int m_decimals;
    Format m_format;
    Scale m_scale;
    bool m_readOnly;
    bool m_bounded;
    QLineEdit* m_edit;

private:
    QRegularExpressionValidator *validator;
};

/*!
    \class QtDoubleEdit
    \internal
    \inmodule QtDesigner
    \since 4.4

    \brief An editor that renders double data using a QLineEdit.

    \sa QtDoubleEditPrivate, QLineEdit, double
*/
QtDoubleEdit::QtDoubleEdit(QWidget *parent) :
QWidget(parent)
{
    d_ptr = new QtDoubleEditPrivate();
    d_ptr->q_ptr = this;

    d_ptr->m_edit = new QLineEdit("0");
    d_ptr->validator = new QRegularExpressionValidator(regExps[Format::LIN_DEG], this);

    QHBoxLayout *lt = new QHBoxLayout(this);
    setupTreeViewEditorMargin(lt);
    lt->setSpacing(0);
    lt->addWidget(d_ptr->m_edit);
    this->setFocusProxy(d_ptr->m_edit);

    connect(d_ptr->m_edit, SIGNAL(editingFinished()), this, SLOT(setValue()));
}

QtDoubleEdit::~QtDoubleEdit()
{
    disconnect(d_ptr->m_edit, SIGNAL(editingFinished()), this, SLOT(setValue()));
    emit destroyed(this);
}

double QtDoubleEdit::value() const
{
    return d_ptr->m_value;
}

double QtDoubleEdit::minimum() const
{
    return d_ptr->m_minimum;
}

double QtDoubleEdit::maximum() const
{
    return d_ptr->m_maximum;
}

int QtDoubleEdit::precision() const
{
    return d_ptr->m_precision;
}

Format QtDoubleEdit::format() const
{
    return d_ptr->m_format;
}

Scale QtDoubleEdit::scale() const
{
    return d_ptr->m_scale;
}

bool QtDoubleEdit::bounded() const
{
    return d_ptr->m_bounded;
}

void QtDoubleEdit::setValue()
{
    QString text = d_ptr->m_edit->text();
    int pos = 0;
    double val;

    if (!d_ptr->m_readOnly && validate(text,pos))
    {
        val = str2num(d_ptr->m_edit->text(), d_ptr->m_scale, d_ptr->m_format);
        setValue(val);
    }
}

void QtDoubleEdit::setValue(double val)
{
    if (!isclose(val, d_ptr->m_value, d_ptr->m_atol, d_ptr->m_rtol)){
        d_ptr->m_value = val;
        if (d_ptr->m_bounded)
            d_ptr->m_edit->setText(num2str());
        emit valueChanged(val);
    }
}

void QtDoubleEdit::setMinimum(double min)
{
    if (!isclose(min, d_ptr->m_minimum, d_ptr->m_atol, d_ptr->m_rtol)){
        if (d_ptr->m_value < min)
            setValue(min);
        d_ptr->m_minimum = min;
        if (d_ptr->m_bounded)
            d_ptr->m_edit->setText(num2str());
    }
}

void QtDoubleEdit::setMaximum(double max)
{
    if (!isclose(max, d_ptr->m_maximum, d_ptr->m_atol, d_ptr->m_rtol)){
        if (d_ptr->m_value > max)
            setValue(max);
        d_ptr->m_maximum = max;
        if (d_ptr->m_bounded)
            d_ptr->m_edit->setText(num2str());
    }
}

void QtDoubleEdit::setRange(double min, double max)
{
    if (min < max)
    {
        setMinimum(min);
        setMaximum(max);
    }
}

void QtDoubleEdit::setPrecision(int prec)
{
    d_ptr->m_precision = prec;
    if (d_ptr->m_bounded)
        d_ptr->m_edit->setText(num2str());
}

void QtDoubleEdit::setFormat(Format format_)
{
    if (d_ptr->m_format!= format_) {
        d_ptr->m_format = format_;
        d_ptr->validator->setRegularExpression(regExps[format_]);
        if (d_ptr->m_bounded)
            d_ptr->m_edit->setText(num2str());
    }
}

void QtDoubleEdit::setScale(Scale scale_)
{
    if (d_ptr->m_scale!= scale_) {
        d_ptr->m_scale = scale_;
        if (d_ptr->m_bounded)
            d_ptr->m_edit->setText(num2str());
    }
}

void QtDoubleEdit::setReadOnly(bool readOnly)
{
    if (d_ptr->m_readOnly != readOnly)
        d_ptr->m_edit->setReadOnly(readOnly);
}

void QtDoubleEdit::setBounded(bool bounded)
{
    d_ptr->m_bounded = bounded;
}

bool QtDoubleEdit::eventFilter(QObject *obj, QEvent *ev)
{
    return QWidget::eventFilter(obj, ev);
}

QValidator::State QtDoubleEdit::validate(QString &text, int &pos) const
{
    return d_ptr->validator->validate(text, pos);

}

QString QtDoubleEdit::num2str() {
    return QtDoubleEdit::num2str(
            d_ptr->m_value, d_ptr->m_scale, d_ptr->m_format, d_ptr->m_precision, d_ptr->m_minimum, d_ptr->m_maximum,
            d_ptr->m_atol, d_ptr->m_rtol, d_ptr->m_ftol, d_ptr->m_decimals);
}

QString QtDoubleEdit::num2str(double val, Scale scale, Format format, int precision, double minVal, double maxVal,
                              double &absTol, double &relTol, double &fmtTol, int &decimals) {
    QString text;
    double scaled_val = fmtCalc(scale, format, val);
    absTol = atolCalc(precision, minVal, maxVal);
    relTol = rtolCalc(precision, minVal, maxVal);
    fmtTol = fmtCalc(scale, format, absTol);
    decimals = sigDigCalc(precision, minVal, maxVal, scale, format, fmtTol);
    switch (format) {
        case Format::LOG_DEG:
            text = double2str(20*log10(scaled_val), decimals);
            break;
        default:
            text = double2str(scaled_val, decimals);
            break;
    }
    return text;
}

double QtDoubleEdit::str2num(const QString &text, const Scale scale, const Format format)
{
    int VALS_LENGTH = 1;
    QRegularExpressionMatch match;
    int scale_ = ScaleValueMap[scale];
    double val = 0;
    double vals[VALS_LENGTH];
    int valIndex = -1;
    for (QString seqStr : text.split(regExpSeps[format], Qt::SkipEmptyParts))
        for (QString subStr: seqStr.split("[,;]", Qt::SkipEmptyParts)) {
            valIndex += 1;
            match = regDecimal.match(subStr);
            if (!match.hasMatch() || valIndex > VALS_LENGTH)
                return 0;
            vals[valIndex] = match.captured(1).toDouble();
        }
    switch (format) {
        case Format::RE:
            val = double(vals[0]);
            val *= pow(10, scale_);
            break;
        case Format::RE_IM:
            val = double(vals[0]);
            val *= pow(10, scale_);
            break;
        case Format::LIN_DEG:
            val = double(vals[0]);
            val *= pow(10, scale_);
            break;
        case Format::LOG_DEG:
            val = double(std::pow(10, (vals[0]) / 20));
            val *= sqrt(pow(10, scale_));
            break;
        default:
            return 0;
    }
    if (isinfinite(std::abs(val)))
        val = 0;
    return val;
}

// QtComplexEdit

/*!
    \class QtComplexEditPrivate
    \internal
    \inmodule QtDesigner
    \since 4.4

    \brief A Private d_ptr of QtComplexEdit.

    \sa QtComplexEdit
*/
class QtComplexEditPrivate
{
    QtComplexEdit *q_ptr;
    Q_DECLARE_PUBLIC(QtComplexEdit)
public:
    QtComplexEditPrivate()
        : m_value(0),
          m_precision(63),
          m_atol(std::numeric_limits<double>::epsilon()),
          m_rtol(std::numeric_limits<double>::min()),
          m_ftol(std::numeric_limits<double>::epsilon()),
          m_decimals(2),
          m_format(Format::RE_IM),
          m_scale(Scale::_),
          m_readOnly(false) {}

    QtComplex m_value;
    QtComplex m_minimum;
    QtComplex m_maximum;
    int m_precision;
    QtComplex m_atol;
    QtComplex m_rtol;
    QtComplex m_ftol;
    int m_decimals;
    Format m_format;
    Scale m_scale;
    bool m_readOnly;
    QLineEdit* m_edit;

private:
    QRegularExpressionValidator *validator;
};

/*!
    \class QtComplexEdit
    \internal
    \inmodule QtDesigner
    \since 4.4

    \brief An editor that renders complex data using a QLineEdit.

    \sa QtComplexEditPrivate, QLineEdit, QtComplex
*/
QtComplexEdit::QtComplexEdit(QWidget *parent) :
QWidget(parent)
{
    d_ptr = new QtComplexEditPrivate();
    d_ptr->q_ptr = this;

    d_ptr->m_edit = new QLineEdit("0");
    d_ptr->validator = new QRegularExpressionValidator(regExps[Format::RE_IM], this);

    QHBoxLayout *lt = new QHBoxLayout(this);
    setupTreeViewEditorMargin(lt);
    lt->setSpacing(0);
    lt->addWidget(d_ptr->m_edit);
    this->setFocusProxy(d_ptr->m_edit);

    connect(d_ptr->m_edit, SIGNAL(editingFinished()), this, SLOT(setValue()));
}

QtComplexEdit::~QtComplexEdit()
{
    disconnect(d_ptr->m_edit, SIGNAL(editingFinished()), this, SLOT(setValue()));
    emit destroyed(this);
}

QtComplex QtComplexEdit::value() const
{
    return d_ptr->m_value;
}

QtComplex QtComplexEdit::minimum() const
{
    return d_ptr->m_minimum;
}

QtComplex QtComplexEdit::maximum() const
{
    return d_ptr->m_maximum;
}

int QtComplexEdit::precision() const
{
    return d_ptr->m_precision;
}

Format QtComplexEdit::format() const
{
    return d_ptr->m_format;
}

Scale QtComplexEdit::scale() const
{
    return d_ptr->m_scale;
}

void QtComplexEdit::setValue()
{
    QString text = d_ptr->m_edit->text();
    int pos = 0;
    QtComplex val;

    if (!d_ptr->m_readOnly && validate(text,pos))
    {
        val = QtComplexEdit::str2num(d_ptr->m_edit->text(), d_ptr->m_scale, d_ptr->m_format);
        if (!isclose(val, d_ptr->m_value, d_ptr->m_atol, d_ptr->m_rtol)){
            d_ptr->m_value = val;
            emit valueChanged(val);
        }
    }
}

void QtComplexEdit::setValue(const QtComplex &val)
{
    if (!isclose(val, d_ptr->m_value, d_ptr->m_atol, d_ptr->m_rtol)){
        d_ptr->m_value = val;
        d_ptr->m_edit->setText(QtComplexEdit::num2str());
        emit valueChanged(val);
    }
}

void QtComplexEdit::setMinimum(double min)
{
    if (!isclose(min, d_ptr->m_minimum, d_ptr->m_atol, d_ptr->m_rtol)){
        if(abs(d_ptr->m_value) < min)
            setValue(min);
        d_ptr->m_minimum = min;
        d_ptr->m_edit->setText(num2str());
    }
}

void QtComplexEdit::setMaximum(double max)
{
    if (!isclose(max, d_ptr->m_maximum, d_ptr->m_atol, d_ptr->m_rtol)){
        if(abs(d_ptr->m_value) > max)
            setValue(max);
        d_ptr->m_maximum = max;
        d_ptr->m_edit->setText(num2str());
    }
}

void QtComplexEdit::setRange(double min, double max)
{
    if (min < max)
    {
        setMinimum(min);
        setMaximum(max);
    }
}

void QtComplexEdit::setPrecision(int prec)
{
    d_ptr->m_precision = prec;
    d_ptr->m_edit->setText(num2str());
}

void QtComplexEdit::setFormat(Format format_)
{
    if (d_ptr->m_format!= format_) {
        d_ptr->m_format = format_;
        d_ptr->validator->setRegularExpression(regExps[format_]);
        d_ptr->m_edit->setText(num2str());
    }
}

void QtComplexEdit::setScale(Scale scale_)
{
    if (d_ptr->m_scale!= scale_) {
        d_ptr->m_scale = scale_;
        d_ptr->m_edit->setText(num2str());
    }
}

void QtComplexEdit::setReadOnly(bool readOnly)
{
    if (d_ptr->m_readOnly != readOnly)
        d_ptr->m_edit->setReadOnly(readOnly);
}

bool QtComplexEdit::eventFilter(QObject *obj, QEvent *ev)
{
    return QWidget::eventFilter(obj, ev);
}

QValidator::State QtComplexEdit::validate(QString &text, int &pos) const
{
    return d_ptr->validator->validate(text, pos);
}

QString QtComplexEdit::num2str() {
    return QtComplexEdit::num2str(
            d_ptr->m_value, d_ptr->m_scale, d_ptr->m_format, d_ptr->m_precision, d_ptr->m_minimum, d_ptr->m_maximum,
            d_ptr->m_atol, d_ptr->m_rtol, d_ptr->m_ftol, d_ptr->m_decimals);
}

QString QtComplexEdit::num2str(QtComplex val, Scale scale, Format format, int precision, QtComplex minVal, QtComplex maxVal,
                               QtComplex &absTol, QtComplex &relTol, QtComplex &fmtTol, int &decimals) {
    QString text1, sep, text2;
    QtComplex scaled_val = fmtCalc(scale, format, val);
    absTol = atolCalc(precision, minVal, maxVal);
    relTol = rtolCalc(precision, minVal, maxVal);
    fmtTol = fmtCalc(scale, format, absTol);
    decimals = sigDigCalc(precision, minVal, maxVal, scale, format, fmtTol);
    switch (format) {
        case Format::RE:
            text1 = double2str(scaled_val.real(), decimals);
            sep = QString("");
            text2 = QString("");
            break;
        case Format::RE_IM:
            text1 = double2str(scaled_val.real(), decimals);
            sep = QString("+");
            text2 = double2str(scaled_val.imag(), decimals) + "i";
            break;
        case Format::LOG_DEG:
            text1 = double2str(20*log10(abs(scaled_val)), decimals);
            sep = QString("∠");
            text2 = double2str(arg(scaled_val) * 180 / M_PI, decimals);
            break;
        default:
            text1 = double2str(abs(scaled_val), decimals);
            sep = QString("∠");
            text2 = double2str(arg(scaled_val) * 180 / M_PI, decimals);
            break;
    }
    return text1 + sep + text2;
}

QtComplex QtComplexEdit::str2num(const QString &text, const Scale scale, const Format format)
{
    int VALS_LENGTH = 2;
    QRegularExpressionMatch match;
    int scale_ = ScaleValueMap[scale];
    QtComplex val = 0;
    double vals[VALS_LENGTH];
    int valIndex = -1;
    for (QString seqStr : text.split(regExpSeps[format], Qt::SkipEmptyParts))
        for (QString subStr: seqStr.split("[,;]", Qt::SkipEmptyParts)) {
            valIndex += 1;
            match = regDecimal.match(subStr);
            if (!match.hasMatch() || valIndex > VALS_LENGTH)
                return 0;
            vals[valIndex] = match.captured(1).toDouble();
        }
    switch (format) {
        case Format::RE:
            val = {vals[0], 0};
            val *= pow(10, scale_);
            break;
        case Format::RE_IM:
            val = {vals[0], vals[1]};
            val *= pow(10, scale_);
            break;
        case Format::LIN_DEG:
            val = std::polar(vals[0], vals[1] * M_PI / 180);
            val *= pow(10, scale_);
            break;
        case Format::LOG_DEG:
            val = std::polar(std::pow(10, (vals[0]) / 20), vals[1] * M_PI / 180);
            val *= sqrt(pow(10, scale_));
            break;
        default:
            return 0;
    }
    if (isinfinite(std::abs(val)))
        val = 0;
    return val;
}

// QtQuaternionEdit

/*!
    \class QtQuaternionEditPrivate
    \internal
    \inmodule QtDesigner
    \since 4.4

    \brief A Private d_ptr of QtQuaternionEdit.

    \sa QtQuaternionEdit
*/
class QtQuaternionEditPrivate
{
    QtQuaternionEdit *q_ptr;
    Q_DECLARE_PUBLIC(QtQuaternionEdit)
public:
    QtQuaternionEditPrivate()
            : m_value(0, 0, 0, 0),
              m_precision(31),
              m_atol(std::numeric_limits<float>::epsilon()),
              m_rtol(std::numeric_limits<float>::min()),
              m_ftol(std::numeric_limits<float>::epsilon()),
              m_decimals(2),
              m_format(Format::RE_IM),
              m_scale(Scale::_),
              m_readOnly(false),
              m_polarized(false) {}

    QtQuaternion m_value;
    QtQuaternion m_minimum;
    QtQuaternion m_maximum;
    int m_precision;
    QtQuaternion m_atol;
    QtQuaternion m_rtol;
    QtQuaternion m_ftol;
    int m_decimals;
    Format m_format;
    Scale m_scale;
    bool m_readOnly;
    bool m_polarized;
    QLineEdit* m_edit;

private:
    QRegularExpressionValidator *validator;
};

/*!
    \class QtQuaternionEdit
    \internal
    \inmodule QtDesigner
    \since 4.4

    \brief An editor that renders quaternion data using a QLineEdit.

    \sa QtQuaternionEditPrivate, QLineEdit, QtQaternion
*/
QtQuaternionEdit::QtQuaternionEdit(QWidget *parent) :
        QWidget(parent)
{
    d_ptr = new QtQuaternionEditPrivate();
    d_ptr->q_ptr = this;

    d_ptr->m_edit = new QLineEdit("0");
    d_ptr->validator = new QRegularExpressionValidator(regExps[Format::RE_IM], this);

    QHBoxLayout *lt = new QHBoxLayout(this);
    setupTreeViewEditorMargin(lt);
    lt->setSpacing(0);
    lt->addWidget(d_ptr->m_edit);
    this->setFocusProxy(d_ptr->m_edit);

    connect(d_ptr->m_edit, SIGNAL(editingFinished()), this, SLOT(setValue()));
}

QtQuaternionEdit::~QtQuaternionEdit()
{
    disconnect(d_ptr->m_edit, SIGNAL(editingFinished()), this, SLOT(setValue()));
    emit destroyed(this);
}

QtQuaternion QtQuaternionEdit::value() const
{
    return d_ptr->m_value;
}

QtQuaternion QtQuaternionEdit::minimum() const
{
    return d_ptr->m_minimum;
}

QtQuaternion QtQuaternionEdit::maximum() const
{
    return d_ptr->m_maximum;
}

int QtQuaternionEdit::precision() const
{
    return d_ptr->m_precision;
}

Format QtQuaternionEdit::format() const
{
    return d_ptr->m_format;
}

bool QtQuaternionEdit::polarized() const
{
    return d_ptr->m_polarized;
}

Scale QtQuaternionEdit::scale() const
{
    return d_ptr->m_scale;
}

void QtQuaternionEdit::setValue()
{
    QString text = d_ptr->m_edit->text();
    int pos = 0;
    QtQuaternion val;

    if (!d_ptr->m_readOnly && validate(text,pos))
    {
        val = QtQuaternionEdit::str2num(d_ptr->m_edit->text(), d_ptr->m_scale, d_ptr->m_format, d_ptr->m_polarized);
        if (!isclose(val, d_ptr->m_value, d_ptr->m_atol, d_ptr->m_rtol)){
            d_ptr->m_value = val;
            d_ptr->m_edit->setText(QtQuaternionEdit::num2str()); // This Normalizes Quaternions
            emit valueChanged(val);
        }
    }
}

void QtQuaternionEdit::setValue(const QtQuaternion &val)
{
    if (!isclose(val, d_ptr->m_value, d_ptr->m_atol, d_ptr->m_rtol)){
        d_ptr->m_value = val;
        d_ptr->m_edit->setText(QtQuaternionEdit::num2str());
        emit valueChanged(val);
    }
}

void QtQuaternionEdit::setMinimum(double min)
{
    QtQuaternion min_ = QtQuaternion(float(min));
    if (!isclose(min_, d_ptr->m_minimum, d_ptr->m_atol, d_ptr->m_rtol)){
        if(d_ptr->m_value.length() < min)
            setValue(min_);
        d_ptr->m_minimum = min_;
        d_ptr->m_edit->setText(num2str());
    }
}

void QtQuaternionEdit::setMaximum(double max)
{
    QtQuaternion max_ = QtQuaternion(float(max));
    if (!isclose(max_, d_ptr->m_maximum, d_ptr->m_atol, d_ptr->m_rtol)){
        if(d_ptr->m_value.length() > max)
            setValue(max_);
        d_ptr->m_maximum = max_;
        d_ptr->m_edit->setText(num2str());
    }
}

void QtQuaternionEdit::setRange(double min, double max)
{
    if (min < max)
    {
        setMinimum(min);
        setMaximum(max);
    }
}

void QtQuaternionEdit::setPrecision(int prec)
{
    d_ptr->m_precision = prec;
    d_ptr->m_edit->setText(num2str());
}

void QtQuaternionEdit::setFormat(Format format_)
{
    if (d_ptr->m_format!= format_) {
        d_ptr->m_format = format_;
        d_ptr->validator->setRegularExpression(regExps[format_]);
        d_ptr->m_edit->setText(num2str());
    }
}

void QtQuaternionEdit::setScale(Scale scale_)
{
    if (d_ptr->m_scale!= scale_) {
        d_ptr->m_scale = scale_;
        d_ptr->m_edit->setText(num2str());
    }
}

void QtQuaternionEdit::setReadOnly(bool readOnly)
{
    if (d_ptr->m_readOnly != readOnly) {
        d_ptr->m_readOnly = readOnly;
        d_ptr->m_edit->setReadOnly(readOnly);
    }
}

void QtQuaternionEdit::setPolarized(bool polarized)
{
    if (d_ptr->m_polarized != polarized) {
        d_ptr->m_polarized = polarized;
        d_ptr->m_edit->setText(num2str());
    }
}

bool QtQuaternionEdit::eventFilter(QObject *obj, QEvent *ev)
{
    return QWidget::eventFilter(obj, ev);
}

QValidator::State QtQuaternionEdit::validate(QString &text, int &pos) const
{
    return d_ptr->validator->validate(text, pos);
}

QString QtQuaternionEdit::num2str() {
    return QtQuaternionEdit::num2str(
            d_ptr->m_value, d_ptr->m_scale, d_ptr->m_format, d_ptr->m_polarized, d_ptr->m_precision, d_ptr->m_minimum, d_ptr->m_maximum,
            d_ptr->m_atol, d_ptr->m_rtol, d_ptr->m_ftol, d_ptr->m_decimals);
}

QString QtQuaternionEdit::num2str(QtQuaternion val, Scale scale, Format format, bool polarized, int precision, QtQuaternion minVal, QtQuaternion maxVal,
                              QtQuaternion &absTol, QtQuaternion &relTol, QtQuaternion &fmtTol, int &decimals) {
    QString text = "";
    float x, y, z, angle;
    QtComplex a, b;
    QtQuaternion scaled_val = fmtCalc(scale, format, val);
    absTol = atolCalc(precision, minVal, maxVal);
    relTol = rtolCalc(precision, minVal, maxVal);
    fmtTol = fmtCalc(scale, format, absTol);
    decimals = sigDigCalc(precision, minVal, maxVal, scale, format, fmtTol);
    switch (format) {
        case Format::RE:
            text.append(double2str(scaled_val.scalar(), decimals));
            break;
        case Format::RE_IM:
            text.append(double2str(scaled_val.scalar(), decimals));
            text.append('+');
            text.append(double2str(scaled_val.x(), decimals)).append('i');
            text.append('+');
            text.append(double2str(scaled_val.y(), decimals)).append('j');
            text.append('+');
            text.append(double2str(scaled_val.z(), decimals)).append('k');
            break;
        case Format::LOG_DEG:
            if (polarized) {
                a = QtComplex(scaled_val.scalar(), scaled_val.x());
                b = QtComplex(scaled_val.y(), scaled_val.z());
                text.append(double2str(20 * log10(abs(a)), decimals)).append(',');
                text.append(double2str(20 * log10(abs(b)), decimals));
                text.append("∠");
                text.append(double2str(arg(a) * 180 / M_PI, decimals)).append(',');
                text.append(double2str(arg(b) * 180 / M_PI, decimals));
            } else {
                val.getAxisAndAngle(&x, &y, &z, &angle);
                text.append(double2str(20 * log10(std::abs(double(x))), decimals)).append(',');
                text.append(double2str(20 * log10(std::abs(double(y))), decimals)).append(',');
                text.append(double2str(20 * log10(std::abs(double(z))), decimals));
                text.append("∠");
                text.append(double2str(angle, decimals));
            }
            break;
        default:
            if (polarized) {
                a = QtComplex(scaled_val.scalar(), scaled_val.x());
                b = QtComplex(scaled_val.y(), scaled_val.z());
                text.append(double2str(abs(a), decimals)).append(',');
                text.append(double2str(abs(b), decimals));
                text.append("∠");
                text.append(double2str(arg(a) * 180 / M_PI, decimals)).append(',');
                text.append(double2str(arg(b) * 180 / M_PI, decimals));
            } else {
                val.getAxisAndAngle(&x, &y, &z, &angle);
                text.append(double2str(std::abs(x), decimals)).append(',');
                text.append(double2str(std::abs(y), decimals)).append(',');
                text.append(double2str(std::abs(z), decimals));
                text.append("∠");
                text.append(double2str(angle, decimals));
            }
            break;
    }
    return text;
}

QtQuaternion QtQuaternionEdit::str2num(const QString &text, const Scale scale, const Format format, const bool polarized)
{
    int VALS_LENGTH = 4;
    QRegularExpressionMatch match;
    int scale_ = ScaleValueMap[scale];
    QtQuaternion val = 0;
    double vals[VALS_LENGTH];
    int valIndex = -1;
    for (QString seqStr : text.split(regExpSeps[format], Qt::SkipEmptyParts))
        for (QString subStr: seqStr.split(QRegularExpression("[\\,\\;]"), Qt::SkipEmptyParts)) {
            valIndex += 1;
            match = regDecimal.match(subStr);
            if (!match.hasMatch() || valIndex > VALS_LENGTH)
                return 0;
            vals[valIndex] = match.captured(1).toDouble();
        }
    switch (format) {
        case Format::RE:
            val = {vals[0], 0, 0, 0};
            val *= pow(10, scale_);
            break;
        case Format::RE_IM:
            val = {vals[0], vals[1], vals[2], vals[3]};
            val *= pow(10, scale_);
            break;
        case Format::LIN_DEG:
            if (polarized) {
                val = QtQuaternion(
                        std::polar(vals[0], vals[2] * M_PI / 180),
                        std::polar(vals[1], vals[3] * M_PI / 180));
            } else {
                val = QtQuaternion::fromAxisAndAngle(
                        vals[0],
                        vals[1],
                        vals[2],
                        vals[3]);
            }
            val *= pow(10, scale_);
            break;
        case Format::LOG_DEG:
            if (polarized) {
                val = QtQuaternion(
                        std::polar(std::pow(10, (vals[0]) / 20), vals[2] * M_PI / 180),
                        std::polar(std::pow(10, (vals[1]) / 20), vals[3] * M_PI / 180));
            } else {
                val = QtQuaternion::fromAxisAndAngle(
                        std::pow(10, (vals[0]) / 20),
                        std::pow(10, (vals[1]) / 20),
                        std::pow(10, (vals[2]) / 20),
                        vals[3]);
            }
            val *= sqrt(pow(10, scale_));
            break;
        default:
            return 0;
    }
    if (isinfinite(val.length()))
        val = 0;
    return val;
}

// QtCharEdit

/*!
    \class QtCharEdit
    \internal
    \inmodule QtDesigner
    \since 4.4

    \brief An editor that renders QChar data using a QLineEdit.

    \sa QLineEdit, QChar
*/
QtCharEdit::QtCharEdit(QWidget *parent)
        : QWidget(parent),  m_lineEdit(new QLineEdit(this))
{
    QHBoxLayout *layout = new QHBoxLayout(this);
    layout->addWidget(m_lineEdit);
    layout->setContentsMargins(QMargins());
    m_lineEdit->installEventFilter(this);
    m_lineEdit->setReadOnly(true);
    m_lineEdit->setFocusProxy(this);
    setFocusPolicy(m_lineEdit->focusPolicy());
    setAttribute(Qt::WA_InputMethodEnabled);
}

bool QtCharEdit::eventFilter(QObject *o, QEvent *e)
{
    if (o == m_lineEdit && e->type() == QEvent::ContextMenu) {
        QContextMenuEvent *c = static_cast<QContextMenuEvent *>(e);
        QMenu *menu = m_lineEdit->createStandardContextMenu();
        const auto actions = menu->actions();
        for (QAction *action : actions) {
            action->setShortcut(QKeySequence());
            QString actionString = action->text();
            const int pos = actionString.lastIndexOf(QLatin1Char('\t'));
            if (pos > 0)
                actionString = actionString.remove(pos, actionString.size() - pos);
            action->setText(actionString);
        }
        QAction *actionBefore = nullptr;
        if (actions.size() > 0)
            actionBefore = actions[0];
        QAction *clearAction = new QAction(tr("Clear Char"), menu);
        menu->insertAction(actionBefore, clearAction);
        menu->insertSeparator(actionBefore);
        clearAction->setEnabled(!m_value.isNull());
        connect(clearAction, SIGNAL(triggered()), this, SLOT(slotClearChar()));
        menu->exec(c->globalPos());
        delete menu;
        e->accept();
        return true;
    }

    return QWidget::eventFilter(o, e);
}

void QtCharEdit::slotClearChar()
{
    if (m_value.isNull())
        return;
    setValue(QChar());
    emit valueChanged(m_value);
}

void QtCharEdit::handleKeyEvent(QKeyEvent *e)
{
    const int key = e->key();
    switch (key) {
        case Qt::Key_Control:
        case Qt::Key_Shift:
        case Qt::Key_Meta:
        case Qt::Key_Alt:
        case Qt::Key_Super_L:
        case Qt::Key_Return:
            return;
        default:
            break;
    }

    const QString text = e->text();
    if (text.size() != 1)
        return;

    const QChar c = text.at(0);
    if (!c.isPrint())
        return;

    if (m_value == c)
        return;

    m_value = c;
    const QString str = m_value.isNull() ? QString() : QString(m_value);
    m_lineEdit->setText(str);
    e->accept();
    emit valueChanged(m_value);
}

void QtCharEdit::setValue(const QChar &value)
{
    if (value == m_value)
        return;

    m_value = value;
    QString str = value.isNull() ? QString() : QString(value);
    m_lineEdit->setText(str);
}

QChar QtCharEdit::value() const
{
    return m_value;
}

void QtCharEdit::focusInEvent(QFocusEvent *e)
{
    m_lineEdit->event(e);
    m_lineEdit->selectAll();
    QWidget::focusInEvent(e);
}

void QtCharEdit::focusOutEvent(QFocusEvent *e)
{
    m_lineEdit->event(e);
    QWidget::focusOutEvent(e);
}

void QtCharEdit::keyPressEvent(QKeyEvent *e)
{
    handleKeyEvent(e);
    e->accept();
}

void QtCharEdit::keyReleaseEvent(QKeyEvent *e)
{
    m_lineEdit->event(e);
}

bool QtCharEdit::event(QEvent *e)
{
    switch(e->type()) {
        case QEvent::Shortcut:
        case QEvent::ShortcutOverride:
        case QEvent::KeyRelease:
            e->accept();
            return true;
        default:
            break;
    }
    return QWidget::event(e);
}

// QtColorEditWidget

/*!
    \class QtColorEditWidget
    \internal
    \inmodule QtDesigner
    \since 4.4

    \brief An editor that renders QColor data using QLabels.

    \sa QLabel, QColor
*/
QtColorEditWidget::QtColorEditWidget(QWidget *parent) :
    QWidget(parent),
    m_pixmapLabel(new QLabel),
    m_label(new QLabel),
    m_button(new QToolButton)
{
    QHBoxLayout *lt = new QHBoxLayout(this);
    setupTreeViewEditorMargin(lt);
    lt->setSpacing(0);
    lt->addWidget(m_pixmapLabel);
    lt->addWidget(m_label);
    lt->addItem(new QSpacerItem(0, 0, QSizePolicy::Expanding, QSizePolicy::Ignored));

    m_button->setSizePolicy(QSizePolicy::Fixed, QSizePolicy::Ignored);
    m_button->setFixedWidth(20);
    setFocusProxy(m_button);
    setFocusPolicy(m_button->focusPolicy());
    m_button->setText(tr("..."));
    m_button->installEventFilter(this);
    connect(m_button, SIGNAL(clicked()), this, SLOT(buttonClicked()));
    lt->addWidget(m_button);
    m_pixmapLabel->setPixmap(QtPropertyBrowserUtils::brushValuePixmap(QBrush(m_color)));
    m_label->setText(QtPropertyBrowserUtils::colorValueText(m_color));
}

QColor QtColorEditWidget::value() const {
    return m_color;
}

void QtColorEditWidget::setValue(const QColor &c)
{
    if (m_color != c) {
        m_color = c;
        m_pixmapLabel->setPixmap(QtPropertyBrowserUtils::brushValuePixmap(QBrush(c)));
        m_label->setText(QtPropertyBrowserUtils::colorValueText(c));
        emit valueChanged(m_color);
    }
}

void QtColorEditWidget::buttonClicked()
{
    const QColor newColor = QColorDialog::getColor(m_color, this, QString(), QColorDialog::ShowAlphaChannel);
    if (newColor.isValid() && newColor != m_color) {
        setValue(newColor);
        emit valueChanged(m_color);
    }
}

bool QtColorEditWidget::eventFilter(QObject *obj, QEvent *ev)
{
    if (obj == m_button) {
        switch (ev->type()) {
        case QEvent::KeyPress:
        case QEvent::KeyRelease: { // Prevent the QToolButton from handling Enter/Escape meant control the delegate
            switch (static_cast<const QKeyEvent*>(ev)->key()) {
            case Qt::Key_Escape:
            case Qt::Key_Enter:
            case Qt::Key_Return:
                ev->ignore();
                return true;
            default:
                break;
            }
        }
            break;
        default:
            break;
        }
    }
    return QWidget::eventFilter(obj, ev);
}

// QtFontEditWidget

/*!
    \class QtFontEditWidget
    \internal
    \inmodule QtDesigner
    \since 4.4

    \brief An editor that renders QFont data using QLabels.

    \sa QLabel, QFont
*/
QtFontEditWidget::QtFontEditWidget(QWidget *parent) :
    QWidget(parent),
    m_pixmapLabel(new QLabel),
    m_label(new QLabel),
    m_button(new QToolButton)
{
    QHBoxLayout *lt = new QHBoxLayout(this);
    setupTreeViewEditorMargin(lt);
    lt->setSpacing(0);
    lt->addWidget(m_pixmapLabel);
    lt->addWidget(m_label);
    lt->addItem(new QSpacerItem(0, 0, QSizePolicy::Expanding, QSizePolicy::Ignored));

    m_button->setSizePolicy(QSizePolicy::Fixed, QSizePolicy::Ignored);
    m_button->setFixedWidth(20);
    setFocusProxy(m_button);
    setFocusPolicy(m_button->focusPolicy());
    m_button->setText(tr("..."));
    m_button->installEventFilter(this);
    connect(m_button, SIGNAL(clicked()), this, SLOT(buttonClicked()));
    lt->addWidget(m_button);
    m_pixmapLabel->setPixmap(QtPropertyBrowserUtils::fontValuePixmap(m_font));
    m_label->setText(QtPropertyBrowserUtils::fontValueText(m_font));
}

QFont QtFontEditWidget::value() const {
    return m_font;
}

void QtFontEditWidget::setValue(const QFont &f)
{
    if (m_font != f) {
        m_font = f;
        m_pixmapLabel->setPixmap(QtPropertyBrowserUtils::fontValuePixmap(f));
        m_label->setText(QtPropertyBrowserUtils::fontValueText(f));
        emit valueChanged(m_font);
    }
}

void QtFontEditWidget::buttonClicked()
{
    bool ok = false;
    QFont newFont = QFontDialog::getFont(&ok, m_font, this, tr("Select Font"));
    if (ok && newFont != m_font) {
        QFont f = m_font;
        // prevent mask for unchanged attributes, don't change other attributes (like kerning, etc...)
        if (m_font.family() != newFont.family())
            f.setFamily(newFont.family());
        if (m_font.pointSize() != newFont.pointSize())
            f.setPointSize(newFont.pointSize());
        if (m_font.bold() != newFont.bold())
            f.setBold(newFont.bold());
        if (m_font.italic() != newFont.italic())
            f.setItalic(newFont.italic());
        if (m_font.underline() != newFont.underline())
            f.setUnderline(newFont.underline());
        if (m_font.strikeOut() != newFont.strikeOut())
            f.setStrikeOut(newFont.strikeOut());
        setValue(f);
        emit valueChanged(m_font);
    }
}

bool QtFontEditWidget::eventFilter(QObject *obj, QEvent *ev)
{
    if (obj == m_button) {
        switch (ev->type()) {
        case QEvent::KeyPress:
        case QEvent::KeyRelease: { // Prevent the QToolButton from handling Enter/Escape meant control the delegate
            switch (static_cast<const QKeyEvent*>(ev)->key()) {
            case Qt::Key_Escape:
            case Qt::Key_Enter:
            case Qt::Key_Return:
                ev->ignore();
                return true;
            default:
                break;
            }
        }
            break;
        default:
            break;
        }
    }
    return QWidget::eventFilter(obj, ev);
}

// FileEditWidget

/*!
    \class QtFileEdit
    \internal
    \inmodule QtDesigner
    \since 4.4

    \brief An editor that renders QFile data using a QLineEdit.

    \sa QLineEdit, QFile
*/
QtFileEdit::QtFileEdit(QWidget *parent) : QWidget(parent),
                                          m_edit(new QLineEdit), m_button(new QToolButton)
{
    m_fileName = QString();
    m_filter = QString();
    m_fileMode = QFileDialog::AnyFile;
    m_readOnly = false;

    QHBoxLayout *lt = new QHBoxLayout(this);
    setupTreeViewEditorMargin(lt);
    lt->setSpacing(0);
    lt->addWidget(m_edit);

    m_button->setSizePolicy(QSizePolicy::Fixed, QSizePolicy::Ignored);
    m_button->setFixedWidth(20);
    setFocusProxy(m_button);
    setFocusPolicy(m_button->focusPolicy());
    m_button->setText(tr("..."));
    m_button->installEventFilter(this);

    connect(m_button, SIGNAL(clicked()), this, SLOT(slotButtonClicked()));
    connect(m_edit, SIGNAL(editingFinished()), this, SLOT(slotEditFinished()));

    lt->addWidget(m_button);
    m_edit->setText(m_fileName);
}

QtFileEdit::~QtFileEdit()
{
    emit destroyed(this);
}

QString QtFileEdit::value() const {
    return m_fileName;
}

QString QtFileEdit::filter() const {
    return m_filter;
}

QFileDialog::FileMode QtFileEdit::fileMode() const {
    return m_fileMode;
}

bool QtFileEdit::fileExists(QString path) const{
    QFileInfo checkFile(path);
    // check if file exists and if yes: Is it really a file and no directory?
    if (checkFile.exists() && m_fileMode != QFileDialog::Directory && checkFile.isFile())
        return true;
    else if (checkFile.exists() && m_fileMode == QFileDialog::Directory && checkFile.isDir())
        return true;
    else
        return false;
}

bool QtFileEdit::validExtension(QString path) const{
    QFileInfo fileInfo = QFileInfo(path);
    QString ext = fileInfo.completeSuffix();
    QRegularExpression regExp = QRegularExpression("\\*(?:[\\.\\w\\d]+)?");
    QRegularExpressionMatch match;
    int pos = 0;

    if (m_fileMode == QFileDialog::Directory){
        if (ext.isEmpty())
            return true;
        else
            return false;
    }
    else{
        if (m_filter.contains("All Files (*)"))
            return true;
        if (ext.isEmpty())
            return false;
        match = regExp.match(m_filter);
        for ( const auto& i : match.capturedTexts()) {
            if (i == QString("*." + ext) || i == "*")
                return true;
        }
    }
    return false;

}

void QtFileEdit::setValue(const QString &fileName)
{
    if (fileExists(fileName) && validExtension(fileName) && fileName != m_fileName) {
        m_fileName = fileName;
        m_edit->setText(fileName);
        emit valueChanged(fileName);
    }
}
void QtFileEdit::setFilter(const QString &filter)
{
    if (m_filter != filter) {
        m_filter = filter;
    }
}

void QtFileEdit::setFileMode(const QFileDialog::FileMode mode)
{
    if (m_fileMode != mode) {
        m_fileMode = mode;
    }
}

void QtFileEdit::setReadOnly(const bool readOnly)
{
    if (m_readOnly != readOnly) {
        m_edit->setReadOnly(readOnly);
    }
}

void QtFileEdit::slotEditFinished()
{
    QString fileName = m_edit->text();
    setValue(fileName);
}

void QtFileEdit::slotButtonClicked()
{
//    QString fileName = QFileDialog::getOpenFileName(this,
//                                                    tr("QFileDialog::getOpenFileName()"),
//                                                    m_fileName,
//                                                    m_filter);
    QStringList fileNames;
    QFileDialog dialog(this);
    if (m_fileMode != QFileDialog::Directory)
        dialog.setNameFilter(m_filter);
    dialog.setFileMode(m_fileMode);
    dialog.setViewMode(QFileDialog::Detail);


    if (dialog.exec())
        fileNames = dialog.selectedFiles();

    if ((!fileNames.isEmpty()) && (fileNames.at(0) != m_fileName)){
        setValue(fileNames.at(0));
    }
}

bool QtFileEdit::eventFilter(QObject *obj, QEvent *ev)
{
    if (obj == m_button) {
        switch (ev->type()) {
            case QEvent::KeyPress:
            case QEvent::KeyRelease: { // Prevent the QToolButton from handling Enter/Escape meant control the delegate
                switch (static_cast<const QKeyEvent*>(ev)->key()) {
                    case Qt::Key_Escape:
                    case Qt::Key_Enter:
                    case Qt::Key_Return:
                        ev->ignore();
                        return true;
                    default:
                        break;
                }
            }
                break;
            default:
                break;
        }
    }
    return QWidget::eventFilter(obj, ev);
}

static QList<QLocale::Territory> sortTerritories(const QList<QLocale::Territory> &territories)
{
    QMultiMap<QString, QLocale::Territory> nameToTerritory;
    for (QLocale::Territory territory : territories)
        nameToTerritory.insert(QLocale::territoryToString(territory), territory);
    return nameToTerritory.values();
}

void QtMetaEnumProvider::initLocale()
{
    QMultiMap<QString, QLocale::Language> nameToLanguage;
    for (int l = QLocale::C, last = QLocale::LastLanguage; l <= last; ++l) {
        const QLocale::Language language = static_cast<QLocale::Language>(l);
        QLocale locale(language);
        if (locale.language() == language)
            nameToLanguage.insert(QLocale::languageToString(language), language);
    }

    const QLocale system = QLocale::system();
    if (!nameToLanguage.contains(QLocale::languageToString(system.language())))
        nameToLanguage.insert(QLocale::languageToString(system.language()), system.language());

    const auto languages = nameToLanguage.values();
    for (QLocale::Language language : languages) {
        const auto localesForLanguage = QLocale::matchingLocales(language, QLocale::AnyScript, QLocale::AnyTerritory);
        QList<QLocale::Territory> territories;
        territories.reserve(localesForLanguage.size());
        for (const auto &locale : localesForLanguage)
            territories << locale.territory();
        if (territories.isEmpty() && language == system.language())
            territories << system.territory();

        if (!territories.isEmpty() && !m_languageToIndex.contains(language)) {
            territories = sortTerritories(territories);
            int langIdx = m_languageEnumNames.size();
            m_indexToLanguage[langIdx] = language;
            m_languageToIndex[language] = langIdx;
            QStringList territoryNames;
            int territoryIdx = 0;
            for (QLocale::Territory territory : std::as_const(territories)) {
                territoryNames << QLocale::territoryToString(territory);
                m_indexToTerritory[langIdx][territoryIdx] = territory;
                m_territoryToIndex[language][territory] = territoryIdx;
                ++territoryIdx;
            }
            m_languageEnumNames << QLocale::languageToString(language);
            m_territoryEnumNames[language] = territoryNames;
        }
    }
}

QtMetaEnumProvider::QtMetaEnumProvider()
{
    QMetaProperty p;

    p = QtMetaEnumWrapper::staticMetaObject.property(
                QtMetaEnumWrapper::staticMetaObject.propertyOffset() + 0);
    m_policyEnum = p.enumerator();
    const int keyCount = m_policyEnum.keyCount();
    for (int i = 0; i < keyCount; i++)
        m_policyEnumNames << QLatin1String(m_policyEnum.key(i));

    initLocale();
}

QSizePolicy::Policy QtMetaEnumProvider::indexToSizePolicy(int index) const
{
    return static_cast<QSizePolicy::Policy>(m_policyEnum.value(index));
}

int QtMetaEnumProvider::sizePolicyToIndex(QSizePolicy::Policy policy) const
{
     const int keyCount = m_policyEnum.keyCount();
    for (int i = 0; i < keyCount; i++)
        if (indexToSizePolicy(i) == policy)
            return i;
    return -1;
}

void QtMetaEnumProvider::indexToLocale(int languageIndex, int territoryIndex, QLocale::Language *language, QLocale::Territory *territory) const
{
    QLocale::Language l = QLocale::C;
    QLocale::Territory c = QLocale::AnyTerritory;
    if (m_indexToLanguage.contains(languageIndex)) {
        l = m_indexToLanguage[languageIndex];
        if (m_indexToTerritory.contains(languageIndex) && m_indexToTerritory[languageIndex].contains(territoryIndex))
            c = m_indexToTerritory[languageIndex][territoryIndex];
    }
    if (language)
        *language = l;
    if (territory)
        *territory = c;
}

void QtMetaEnumProvider::localeToIndex(QLocale::Language language, QLocale::Territory territory, int *languageIndex, int *territoryIndex) const
{
    int l = -1;
    int c = -1;
    if (m_languageToIndex.contains(language)) {
        l = m_languageToIndex[language];
        if (m_territoryToIndex.contains(language) && m_territoryToIndex[language].contains(territory))
            c = m_territoryToIndex[language][territory];
    }

    if (languageIndex)
        *languageIndex = l;
    if (territoryIndex)
        *territoryIndex = c;
}

QT_END_NAMESPACE
