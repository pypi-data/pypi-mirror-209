#ifndef QRANGESLIDER_P_H
#define QRANGESLIDER_P_H

#include <QtCore/QObject>
#include <QtWidgets/QStyle>

#include "qrangeslider.h"

QT_FORWARD_DECLARE_CLASS(QStylePainter)
QT_FORWARD_DECLARE_CLASS(QStyleOptionSlider)

class QRangeSliderPrivate : public QObject
{
    Q_OBJECT

public:
    Q_DECLARE_PUBLIC(QRangeSlider)
    explicit QRangeSliderPrivate(QRangeSlider *q);
    QRangeSlider *q_ptr;

    void initStyleOption(QStyleOptionSlider* option, QRangeSlider::SpanHandle handle = QRangeSlider::UpperHandle) const;
    [[nodiscard]] int pick(const QPoint& pt) const
    {
        return q_ptr->orientation() == Qt::Horizontal ? pt.x() : pt.y();
    }
    [[nodiscard]] int pixelPosToRangeValue(int pos) const;
    void handleMousePress(const QPoint& pos, QStyle::SubControl& control, int value, QRangeSlider::SpanHandle handle);
    void drawHandle(QStylePainter* painter, QRangeSlider::SpanHandle handle) const;
    void setupPainter(QPainter* painter, Qt::Orientation orientation, qreal x1, qreal y1, qreal x2, qreal y2) const;
    void drawSpan(QStylePainter* painter, const QRect& rect) const;
    void triggerAction(QAbstractSlider::SliderAction action, bool main);
    void swapControls();

    int lower;
    int upper;
    int lowerPos;
    int upperPos;
    int offset;
    int position;
    QRangeSlider::SpanHandle lastPressed;
    QRangeSlider::SpanHandle mainControl;
    QStyle::SubControl lowerPressed;
    QStyle::SubControl upperPressed;
    QRangeSlider::HandleMovementMode movement;
    bool firstMovement;
    bool blockTracking;

public Q_SLOTS:
    void updateRange(int min, int max);
    void movePressedHandle();
};
#endif // QRANGESLIDER_P_H
