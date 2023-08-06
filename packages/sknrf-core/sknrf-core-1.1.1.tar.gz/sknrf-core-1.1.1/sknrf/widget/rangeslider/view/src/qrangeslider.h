#ifndef QRANGESLIDER_H
#define QRANGESLIDER_H

#include <QtWidgets/QSlider>

#include "sknrfconfig.h"

#if defined(QRANGESLIDER_COMPILE_LIBRARY)
#  define QRANGESLIDER_DECL  Q_DECL_EXPORT
#elif defined(QRANGESLIDER_USE_LIBRARY)
#  define QRANGESLIDER_DECL Q_DECL_IMPORT
#else
#  define QRANGESLIDER_DECL
#endif

class QRangeSliderPrivate;

class QRANGESLIDER_DECL QRangeSlider : public QSlider
{
    Q_OBJECT
    Q_DECLARE_PRIVATE(QRangeSlider)
    Q_PROPERTY(int lowerValue READ lowerValue WRITE setLowerValue)
    Q_PROPERTY(int upperValue READ upperValue WRITE setUpperValue)
    Q_PROPERTY(int lowerPosition READ lowerPosition WRITE setLowerPosition)
    Q_PROPERTY(int upperPosition READ upperPosition WRITE setUpperPosition)
    Q_PROPERTY(HandleMovementMode handleMovementMode READ handleMovementMode WRITE setHandleMovementMode)

public:
    explicit QRangeSlider(QWidget *parent = nullptr);
    explicit QRangeSlider(Qt::Orientation orientation, QWidget* parent = nullptr);
    ~QRangeSlider() override;

    enum HandleMovementMode
    {
        FreeMovement,
        NoCrossing,
        NoOverlapping
    };
    Q_ENUM(HandleMovementMode)

    enum SpanHandle
    {
        NoHandle,
        LowerHandle,
        UpperHandle
    };
    Q_ENUM(SpanHandle)

    [[nodiscard]] HandleMovementMode handleMovementMode() const;
    void setHandleMovementMode(HandleMovementMode mode);

    [[nodiscard]] int lowerValue() const;
    [[nodiscard]] int upperValue() const;

    [[nodiscard]] int lowerPosition() const;
    [[nodiscard]] int upperPosition() const;

public Q_SLOTS:
    void setLowerValue(int lower);
    void setUpperValue(int upper);
    void setSpan(int lower, int upper);

    void setLowerPosition(int lower);
    void setUpperPosition(int upper);

Q_SIGNALS:
    void spanChanged(int lower, int upper);
    void lowerValueChanged(int lower);
    void upperValueChanged(int upper);

    void lowerPositionChanged(int lower);
    void upperPositionChanged(int upper);

    void sliderPressed(SpanHandle handle);

protected:
    void keyPressEvent(QKeyEvent* event) override;
    void mousePressEvent(QMouseEvent* event) override;
    void mouseMoveEvent(QMouseEvent* event) override;
    void mouseReleaseEvent(QMouseEvent* event) override;
    void paintEvent(QPaintEvent* event) override;

private:
    QRangeSliderPrivate *d_ptr;
};

#endif // QRANGESLIDER_H

