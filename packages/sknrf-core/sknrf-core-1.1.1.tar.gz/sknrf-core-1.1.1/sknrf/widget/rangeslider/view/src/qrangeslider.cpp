#include <QtGui/QKeyEvent>
#include <QtWidgets/QApplication>
#include <QtWidgets/QStylePainter>
#include <QtWidgets/QStyleOptionSlider>

#include "qrangeslider_p.h"


QRangeSliderPrivate::QRangeSliderPrivate(QRangeSlider *q)
    : q_ptr(q),
      lower(0),
      upper(0),
      lowerPos(0),
      upperPos(0),
      offset(0),
      position(0),
      lastPressed(QRangeSlider::NoHandle),
      mainControl(QRangeSlider::LowerHandle),
      lowerPressed(QStyle::SC_None),
      upperPressed(QStyle::SC_None),
      movement(QRangeSlider::FreeMovement),
      firstMovement(false),
      blockTracking(false)
{
}

void QRangeSliderPrivate::initStyleOption(QStyleOptionSlider* option, QRangeSlider::SpanHandle handle) const
{
    q_ptr->initStyleOption(option);
    option->sliderPosition = (handle == QRangeSlider::LowerHandle ? lowerPos : upperPos);
    option->sliderValue = (handle == QRangeSlider::LowerHandle ? lower : upper);
}

int QRangeSliderPrivate::pixelPosToRangeValue(int pos) const
{
    QStyleOptionSlider opt;
    initStyleOption(&opt);

    int sliderMin = 0;
    int sliderMax = 0;
    int sliderLength = 0;
    const QSlider* p = static_cast<QSlider*>(q_ptr);
    const QRect gr = p->style()->subControlRect(QStyle::CC_Slider, &opt, QStyle::SC_SliderGroove, p);
    const QRect sr = p->style()->subControlRect(QStyle::CC_Slider, &opt, QStyle::SC_SliderHandle, p);
    if (p->orientation() == Qt::Horizontal)
    {
        sliderLength = sr.width();
        sliderMin = gr.x();
        sliderMax = gr.right() - sliderLength + 1;
    }
    else
    {
        sliderLength = sr.height();
        sliderMin = gr.y();
        sliderMax = gr.bottom() - sliderLength + 1;
    }
    return QStyle::sliderValueFromPosition(p->minimum(), p->maximum(), pos - sliderMin,
                                           sliderMax - sliderMin, opt.upsideDown);
}

void QRangeSliderPrivate::handleMousePress(const QPoint& pos, QStyle::SubControl& control, int value, QRangeSlider::SpanHandle handle)
{
    QStyleOptionSlider opt;
    initStyleOption(&opt, handle);
    const QStyle::SubControl oldControl = control;
    control = q_ptr->style()->hitTestComplexControl(QStyle::CC_Slider, &opt, pos, q_ptr);
    const QRect sr = q_ptr->style()->subControlRect(QStyle::CC_Slider, &opt, QStyle::SC_SliderHandle, q_ptr);
    if (control == QStyle::SC_SliderHandle)
    {
        position = value;
        offset = pick(pos - sr.topLeft());
        lastPressed = handle;
        q_ptr->setSliderDown(true);
        emit q_ptr->sliderPressed(handle);
    }
    if (control != oldControl)
        q_ptr->update(sr);
}

void QRangeSliderPrivate::setupPainter(QPainter* painter, Qt::Orientation orientation, qreal x1, qreal y1, qreal x2, qreal y2) const
{
    QColor highlight = q_ptr->palette().color(QPalette::Highlight);
    QLinearGradient gradient(x1, y1, x2, y2);
    gradient.setColorAt(0, highlight.darker(120));
    gradient.setColorAt(1, highlight.lighter(108));
    painter->setBrush(gradient);

    if (orientation == Qt::Horizontal)
        painter->setPen(QPen(highlight.darker(130), 0));
    else
        painter->setPen(QPen(highlight.darker(150), 0));
}

void QRangeSliderPrivate::drawSpan(QStylePainter* painter, const QRect& rect) const
{
    QStyleOptionSlider opt;
    initStyleOption(&opt);
    const QSlider* p = static_cast<QSlider*>(q_ptr);

    // area
    QRect groove = p->style()->subControlRect(QStyle::CC_Slider, &opt, QStyle::SC_SliderGroove, p);
    if (opt.orientation == Qt::Horizontal)
        groove.adjust(0, 0, -1, 0);
    else
        groove.adjust(0, 0, 0, -1);

    // pen & brush
    painter->setPen(QPen(p->palette().color(QPalette::Dark).lighter(110), 0));
    if (opt.orientation == Qt::Horizontal)
        setupPainter(painter, opt.orientation, groove.center().x(), groove.top(), groove.center().x(), groove.bottom());
    else
        setupPainter(painter, opt.orientation, groove.left(), groove.center().y(), groove.right(), groove.center().y());

    // draw groove
    painter->drawRect(rect.intersected(groove));
}

void QRangeSliderPrivate::drawHandle(QStylePainter* painter, QRangeSlider::SpanHandle handle) const
{
    QStyleOptionSlider opt;
    initStyleOption(&opt, handle);
    opt.subControls = QStyle::SC_SliderHandle;
    QStyle::SubControl pressed = (handle == QRangeSlider::LowerHandle ? lowerPressed : upperPressed);
    if (pressed == QStyle::SC_SliderHandle)
    {
        opt.activeSubControls = pressed;
        opt.state |= QStyle::State_Sunken;
    }
    painter->drawComplexControl(QStyle::CC_Slider, opt);
}

void QRangeSliderPrivate::triggerAction(QAbstractSlider::SliderAction action, bool main)
{
    int value = 0;
    bool no = false;
    bool up = false;
    const int min = q_ptr->minimum();
    const int max = q_ptr->maximum();
    const QRangeSlider::SpanHandle altControl = (mainControl == QRangeSlider::LowerHandle ? QRangeSlider::UpperHandle : QRangeSlider::LowerHandle);

    blockTracking = true;

    switch (action)
    {
    case QAbstractSlider::SliderSingleStepAdd:
        if ((main && mainControl == QRangeSlider::UpperHandle) || (!main && altControl == QRangeSlider::UpperHandle))
        {
            value = qBound(min, upper + q_ptr->singleStep(), max);
            up = true;
            break;
        }
        value = qBound(min, lower + q_ptr->singleStep(), max);
        break;
    case QAbstractSlider::SliderSingleStepSub:
        if ((main && mainControl == QRangeSlider::UpperHandle) || (!main && altControl == QRangeSlider::UpperHandle))
        {
            value = qBound(min, upper - q_ptr->singleStep(), max);
            up = true;
            break;
        }
        value = qBound(min, lower - q_ptr->singleStep(), max);
        break;
    case QAbstractSlider::SliderToMinimum:
        value = min;
        if ((main && mainControl == QRangeSlider::UpperHandle) || (!main && altControl == QRangeSlider::UpperHandle))
            up = true;
        break;
    case QAbstractSlider::SliderToMaximum:
        value = max;
        if ((main && mainControl == QRangeSlider::UpperHandle) || (!main && altControl == QRangeSlider::UpperHandle))
            up = true;
        break;
    case QAbstractSlider::SliderMove:
        if ((main && mainControl == QRangeSlider::UpperHandle) || (!main && altControl == QRangeSlider::UpperHandle))
            up = true;
    case QAbstractSlider::SliderNoAction:
        no = true;
        break;
    default:
        qWarning("QRangeSliderPrivate::triggerAction: Unknown action");
        break;
    }

    if (!no && !up)
    {
        if (movement == QRangeSlider::NoCrossing)
            value = qMin(value, upper);
        else if (movement == QRangeSlider::NoOverlapping)
            value = qMin(value, upper - 1);

        if (movement == QRangeSlider::FreeMovement && value > upper)
        {
            swapControls();
            q_ptr->setUpperPosition(value);
        }
        else
        {
            q_ptr->setLowerPosition(value);
        }
    }
    else if (!no)
    {
        if (movement == QRangeSlider::NoCrossing)
            value = qMax(value, lower);
        else if (movement == QRangeSlider::NoOverlapping)
            value = qMax(value, lower + 1);

        if (movement == QRangeSlider::FreeMovement && value < lower)
        {
            swapControls();
            q_ptr->setLowerPosition(value);
        }
        else
        {
            q_ptr->setUpperPosition(value);
        }
    }

    blockTracking = false;
    q_ptr->setLowerValue(lowerPos);
    q_ptr->setUpperValue(upperPos);
}

void QRangeSliderPrivate::swapControls()
{
    qSwap(lower, upper);
    qSwap(lowerPressed, upperPressed);
    lastPressed = (lastPressed == QRangeSlider::LowerHandle ? QRangeSlider::UpperHandle : QRangeSlider::LowerHandle);
    mainControl = (mainControl == QRangeSlider::LowerHandle ? QRangeSlider::UpperHandle : QRangeSlider::LowerHandle);
}

void QRangeSliderPrivate::updateRange(int min, int max)
{
    Q_UNUSED(min);
    Q_UNUSED(max);
    // setSpan() takes care of keeping span in range
    q_ptr->setSpan(lower, upper);
}

void QRangeSliderPrivate::movePressedHandle()
{
    switch (lastPressed)
    {
        case QRangeSlider::LowerHandle:
            if (lowerPos != lower)
            {
                bool main = (mainControl == QRangeSlider::LowerHandle);
                triggerAction(QAbstractSlider::SliderMove, main);
            }
            break;
        case QRangeSlider::UpperHandle:
            if (upperPos != upper)
            {
                bool main = (mainControl == QRangeSlider::UpperHandle);
                triggerAction(QAbstractSlider::SliderMove, main);
            }
            break;
        default:
            break;
    }
}



/*!
    Constructs a new QRangeSlider with \a parent.
 */
QRangeSlider::QRangeSlider(QWidget* parent)
    : QSlider(parent),
      d_ptr(new QRangeSliderPrivate(this))
{
    connect(this, SIGNAL(rangeChanged(int, int)), d_ptr, SLOT(updateRange(int, int)));
    connect(this, SIGNAL(sliderReleased()), d_ptr, SLOT(movePressedHandle()));
}

/*!
    Constructs a new QRangeSlider with \a orientation and \a parent.
 */
QRangeSlider::QRangeSlider(Qt::Orientation orientation, QWidget* parent)
    : QSlider(orientation, parent),
      d_ptr(new QRangeSliderPrivate(this))
{
    connect(this, SIGNAL(rangeChanged(int, int)), d_ptr, SLOT(updateRange(int, int)));
    connect(this, SIGNAL(sliderReleased()), d_ptr, SLOT(movePressedHandle()));
}

/*!
    Destructs the QRangeSlider.
 */
QRangeSlider::~QRangeSlider()
= default;

/*!
    \property QRangeSlider::handleMovementMode
    \brief the handle movement mode
 */
QRangeSlider::HandleMovementMode QRangeSlider::handleMovementMode() const
{
    return d_ptr->movement;
}

void QRangeSlider::setHandleMovementMode(QRangeSlider::HandleMovementMode mode)
{
    d_ptr->movement = mode;
}

/*!
    \property QRangeSlider::lowerValue
    \brief the lower value of the span
 */
int QRangeSlider::lowerValue() const
{
    return qMin(d_ptr->lower, d_ptr->upper);
}

void QRangeSlider::setLowerValue(int lower)
{
    setSpan(lower, d_ptr->upper);
}

/*!
    \property QRangeSlider::upperValue
    \brief the upper value of the span
 */
int QRangeSlider::upperValue() const
{
    return qMax(d_ptr->lower, d_ptr->upper);
}

void QRangeSlider::setUpperValue(int upper)
{
    setSpan(d_ptr->lower, upper);
}

/*!
    Sets the span from \a lower to \a upper.
 */
void QRangeSlider::setSpan(int lower, int upper)
{
    const int low = qBound(minimum(), qMin(lower, upper), maximum());
    const int upp = qBound(minimum(), qMax(lower, upper), maximum());
    if (low != d_ptr->lower || upp != d_ptr->upper)
    {
        if (low != d_ptr->lower)
        {
            d_ptr->lower = low;
            d_ptr->lowerPos = low;
            emit lowerValueChanged(low);
        }
        if (upp != d_ptr->upper)
        {
            d_ptr->upper = upp;
            d_ptr->upperPos = upp;
            emit upperValueChanged(upp);
        }
        emit spanChanged(d_ptr->lower, d_ptr->upper);
        update();
    }
}

/*!
    \property QRangeSlider::lowerPosition
    \brief the lower position of the span
 */
int QRangeSlider::lowerPosition() const
{
    return d_ptr->lowerPos;
}

void QRangeSlider::setLowerPosition(int lower)
{
    if (d_ptr->lowerPos != lower)
    {
        d_ptr->lowerPos = lower;
        if (!hasTracking())
            update();
        if (isSliderDown())
            emit lowerPositionChanged(lower);
        if (hasTracking() && !d_ptr->blockTracking)
        {
            bool main = (d_ptr->mainControl == QRangeSlider::LowerHandle);
            d_ptr->triggerAction(SliderMove, main);
        }
    }
}

/*!
    \property QRangeSlider::upperPosition
    \brief the upper position of the span
 */
int QRangeSlider::upperPosition() const
{
    return d_ptr->upperPos;
}

void QRangeSlider::setUpperPosition(int upper)
{
    if (d_ptr->upperPos != upper)
    {
        d_ptr->upperPos = upper;
        if (!hasTracking())
            update();
        if (isSliderDown())
            emit upperPositionChanged(upper);
        if (hasTracking() && !d_ptr->blockTracking)
        {
            bool main = (d_ptr->mainControl == QRangeSlider::UpperHandle);
            d_ptr->triggerAction(SliderMove, main);
        }
    }
}

/*!
    \reimp
 */
void QRangeSlider::keyPressEvent(QKeyEvent* event)
{
    QSlider::keyPressEvent(event);

    bool main = true;
    SliderAction action = SliderNoAction;
    switch (event->key())
    {
    case Qt::Key_Left:
        main   = (orientation() == Qt::Horizontal);
        action = !invertedAppearance() ? SliderSingleStepSub : SliderSingleStepAdd;
        break;
    case Qt::Key_Right:
        main   = (orientation() == Qt::Horizontal);
        action = !invertedAppearance() ? SliderSingleStepAdd : SliderSingleStepSub;
        break;
    case Qt::Key_Up:
        main   = (orientation() == Qt::Vertical);
        action = invertedControls() ? SliderSingleStepSub : SliderSingleStepAdd;
        break;
    case Qt::Key_Down:
        main   = (orientation() == Qt::Vertical);
        action = invertedControls() ? SliderSingleStepAdd : SliderSingleStepSub;
        break;
    case Qt::Key_Home:
        main   = (d_ptr->mainControl == QRangeSlider::LowerHandle);
        action = SliderToMinimum;
        break;
    case Qt::Key_End:
        main   = (d_ptr->mainControl == QRangeSlider::UpperHandle);
        action = SliderToMaximum;
        break;
    default:
        event->ignore();
        break;
    }

    if (action)
        d_ptr->triggerAction(action, main);
}

/*!
    \reimp
 */
void QRangeSlider::mousePressEvent(QMouseEvent* event)
{
    if (minimum() == maximum() || (event->buttons() ^ event->button()))
    {
        event->ignore();
        return;
    }

    d_ptr->handleMousePress(event->pos(), d_ptr->upperPressed, d_ptr->upper, QRangeSlider::UpperHandle);
    if (d_ptr->upperPressed != QStyle::SC_SliderHandle)
        d_ptr->handleMousePress(event->pos(), d_ptr->lowerPressed, d_ptr->lower, QRangeSlider::LowerHandle);

    d_ptr->firstMovement = true;
    event->accept();
}

/*!
    \reimp
 */
void QRangeSlider::mouseMoveEvent(QMouseEvent* event)
{
    if (d_ptr->lowerPressed != QStyle::SC_SliderHandle && d_ptr->upperPressed != QStyle::SC_SliderHandle)
    {
        event->ignore();
        return;
    }

    QStyleOptionSlider opt;
    d_ptr->initStyleOption(&opt);
    const int m = style()->pixelMetric(QStyle::PM_MaximumDragDistance, &opt, this);
    int newPosition = d_ptr->pixelPosToRangeValue(d_ptr->pick(event->pos()) - d_ptr->offset);
    if (m >= 0)
    {
        const QRect r = rect().adjusted(-m, -m, m, m);
        if (!r.contains(event->pos()))
        {
            newPosition = d_ptr->position;
        }
    }

    // pick the preferred handle on the first movement
    if (d_ptr->firstMovement)
    {
        if (d_ptr->lower == d_ptr->upper)
        {
            if (newPosition < lowerValue())
            {
                d_ptr->swapControls();
                d_ptr->firstMovement = false;
            }
        }
        else
        {
            d_ptr->firstMovement = false;
        }
    }

    if (d_ptr->lowerPressed == QStyle::SC_SliderHandle)
    {
        if (d_ptr->movement == NoCrossing)
            newPosition = qMin(newPosition, upperValue());
        else if (d_ptr->movement == NoOverlapping)
            newPosition = qMin(newPosition, upperValue() - 1);

        if (d_ptr->movement == FreeMovement && newPosition > d_ptr->upper)
        {
            d_ptr->swapControls();
            setUpperPosition(newPosition);
        }
        else
        {
            setLowerPosition(newPosition);
        }
    }
    else if (d_ptr->upperPressed == QStyle::SC_SliderHandle)
    {
        if (d_ptr->movement == NoCrossing)
            newPosition = qMax(newPosition, lowerValue());
        else if (d_ptr->movement == NoOverlapping)
            newPosition = qMax(newPosition, lowerValue() + 1);

        if (d_ptr->movement == FreeMovement && newPosition < d_ptr->lower)
        {
            d_ptr->swapControls();
            setLowerPosition(newPosition);
        }
        else
        {
            setUpperPosition(newPosition);
        }
    }
    event->accept();
}

/*!
    \reimp
 */
void QRangeSlider::mouseReleaseEvent(QMouseEvent* event)
{
    QSlider::mouseReleaseEvent(event);
    setSliderDown(false);
    d_ptr->lowerPressed = QStyle::SC_None;
    d_ptr->upperPressed = QStyle::SC_None;
    update();
}

/*!
    \reimp
 */
void QRangeSlider::paintEvent(QPaintEvent* event)
{
    Q_UNUSED(event);
    QStylePainter painter(this);

    // groove & ticks
    QStyleOptionSlider opt;
    d_ptr->initStyleOption(&opt);
    opt.sliderValue = 0;
    opt.sliderPosition = 0;
    opt.subControls = QStyle::SC_SliderGroove | QStyle::SC_SliderTickmarks;
    painter.drawComplexControl(QStyle::CC_Slider, opt);

    // handle rects
    opt.sliderPosition = d_ptr->lowerPos;
    const QRect lr = style()->subControlRect(QStyle::CC_Slider, &opt, QStyle::SC_SliderHandle, this);
    const int lrv  = d_ptr->pick(lr.center());
    opt.sliderPosition = d_ptr->upperPos;
    const QRect ur = style()->subControlRect(QStyle::CC_Slider, &opt, QStyle::SC_SliderHandle, this);
    const int urv  = d_ptr->pick(ur.center());

    // span
    const int minv = qMin(lrv, urv);
    const int maxv = qMax(lrv, urv);
    const QPoint c = QRect(lr.center(), ur.center()).center();
    QRect spanRect;
    if (orientation() == Qt::Horizontal)
        spanRect = QRect(QPoint(minv, c.y() - 2), QPoint(maxv, c.y() + 1));
    else
        spanRect = QRect(QPoint(c.x() - 2, minv), QPoint(c.x() + 1, maxv));
    d_ptr->drawSpan(&painter, spanRect);

    // handles
    switch (d_ptr->lastPressed)
    {
    case QRangeSlider::LowerHandle:
        d_ptr->drawHandle(&painter, QRangeSlider::UpperHandle);
        d_ptr->drawHandle(&painter, QRangeSlider::LowerHandle);
        break;
    case QRangeSlider::UpperHandle:
    default:
        d_ptr->drawHandle(&painter, QRangeSlider::LowerHandle);
        d_ptr->drawHandle(&painter, QRangeSlider::UpperHandle);
        break;
    }
}
