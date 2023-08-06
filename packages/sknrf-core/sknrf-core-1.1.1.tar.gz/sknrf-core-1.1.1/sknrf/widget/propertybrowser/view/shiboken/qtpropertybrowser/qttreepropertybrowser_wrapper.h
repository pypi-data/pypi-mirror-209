#ifndef SBK_QTTREEPROPERTYBROWSERWRAPPER_H
#define SBK_QTTREEPROPERTYBROWSERWRAPPER_H

#include <qttreepropertybrowser.h>


// Argument includes
#include <QList>
#include <QStringList>
#include <qbytearray.h>
#include <qcolor.h>
#include <qcoreevent.h>
#include <qmetaobject.h>
#include <qnamespace.h>
#include <qobject.h>
#include <qobjectdefs.h>
#include <qpaintdevice.h>
#include <qpainter.h>
#include <qpoint.h>
#include <qsize.h>
#include <qtpropertybrowser.h>
#include <qtpropertybrowserutils_p.h>
#include <qttreepropertybrowser.h>
#include <qvariant.h>
#include <qwidget.h>
namespace PySide { class DynamicQMetaObject; }

class QtTreePropertyBrowserWrapper : public QtTreePropertyBrowser
{
public:
    QtTreePropertyBrowserWrapper(QWidget * parent = 0);
    inline void actionEvent_protected(QActionEvent * event) { QWidget::actionEvent(event); }
    void actionEvent(QActionEvent * event) override;
    inline void changeEvent_protected(QEvent * event) { QWidget::changeEvent(event); }
    void changeEvent(QEvent * event) override;
    inline void childEvent_protected(QChildEvent * event) { QObject::childEvent(event); }
    void childEvent(QChildEvent * event) override;
    inline void closeEvent_protected(QCloseEvent * event) { QWidget::closeEvent(event); }
    void closeEvent(QCloseEvent * event) override;
    inline void connectNotify_protected(const QMetaMethod & signal) { QObject::connectNotify(signal); }
    void connectNotify(const QMetaMethod & signal) override;
    inline void contextMenuEvent_protected(QContextMenuEvent * event) { QWidget::contextMenuEvent(event); }
    void contextMenuEvent(QContextMenuEvent * event) override;
    inline QWidget * createAttributeEditor_protected(QtProperty * property, QWidget * parent, BrowserCol attribute) { return QtAbstractPropertyBrowser::createAttributeEditor(property, parent, BrowserCol(attribute)); }
    QWidget * createAttributeEditor(QtProperty * property, QWidget * parent, BrowserCol attribute) override;
    inline QWidget * createEditor_protected(QtProperty * property, QWidget * parent) { return QtAbstractPropertyBrowser::createEditor(property, parent); }
    QWidget * createEditor(QtProperty * property, QWidget * parent) override;
    inline void customEvent_protected(QEvent * event) { QObject::customEvent(event); }
    void customEvent(QEvent * event) override;
    int devType() const override;
    inline void disconnectNotify_protected(const QMetaMethod & signal) { QObject::disconnectNotify(signal); }
    void disconnectNotify(const QMetaMethod & signal) override;
    inline void dragEnterEvent_protected(QDragEnterEvent * event) { QWidget::dragEnterEvent(event); }
    void dragEnterEvent(QDragEnterEvent * event) override;
    inline void dragLeaveEvent_protected(QDragLeaveEvent * event) { QWidget::dragLeaveEvent(event); }
    void dragLeaveEvent(QDragLeaveEvent * event) override;
    inline void dragMoveEvent_protected(QDragMoveEvent * event) { QWidget::dragMoveEvent(event); }
    void dragMoveEvent(QDragMoveEvent * event) override;
    inline void dropEvent_protected(QDropEvent * event) { QWidget::dropEvent(event); }
    void dropEvent(QDropEvent * event) override;
    inline void enterEvent_protected(QEnterEvent * event) { QWidget::enterEvent(event); }
    void enterEvent(QEnterEvent * event) override;
    inline bool event_protected(QEvent * event) { return QWidget::event(event); }
    bool event(QEvent * event) override;
    bool eventFilter(QObject * watched, QEvent * event) override;
    inline void focusInEvent_protected(QFocusEvent * event) { QWidget::focusInEvent(event); }
    void focusInEvent(QFocusEvent * event) override;
    inline bool focusNextPrevChild_protected(bool next) { return QWidget::focusNextPrevChild(next); }
    bool focusNextPrevChild(bool next) override;
    inline void focusOutEvent_protected(QFocusEvent * event) { QWidget::focusOutEvent(event); }
    void focusOutEvent(QFocusEvent * event) override;
    bool hasHeightForWidth() const override;
    int heightForWidth(int arg__1) const override;
    inline void hideEvent_protected(QHideEvent * event) { QWidget::hideEvent(event); }
    void hideEvent(QHideEvent * event) override;
    inline void initPainter_protected(QPainter * painter) const { QWidget::initPainter(painter); }
    void initPainter(QPainter * painter) const override;
    inline void inputMethodEvent_protected(QInputMethodEvent * event) { QWidget::inputMethodEvent(event); }
    void inputMethodEvent(QInputMethodEvent * event) override;
    QVariant inputMethodQuery(Qt::InputMethodQuery arg__1) const override;
    inline void itemChanged_protected(QtBrowserItem * item) { QtTreePropertyBrowser::itemChanged(item); }
    void itemChanged(QtBrowserItem * item) override;
    inline void itemInserted_protected(QtBrowserItem * item, QtBrowserItem * afterItem) { QtTreePropertyBrowser::itemInserted(item, afterItem); }
    void itemInserted(QtBrowserItem * item, QtBrowserItem * afterItem) override;
    inline void itemRemoved_protected(QtBrowserItem * item) { QtTreePropertyBrowser::itemRemoved(item); }
    void itemRemoved(QtBrowserItem * item) override;
    inline void keyPressEvent_protected(QKeyEvent * event) { QWidget::keyPressEvent(event); }
    void keyPressEvent(QKeyEvent * event) override;
    inline void keyReleaseEvent_protected(QKeyEvent * event) { QWidget::keyReleaseEvent(event); }
    void keyReleaseEvent(QKeyEvent * event) override;
    inline void leaveEvent_protected(QEvent * event) { QWidget::leaveEvent(event); }
    void leaveEvent(QEvent * event) override;
    const QMetaObject * metaObject() const override;
    inline int metric_protected(QPaintDevice::PaintDeviceMetric arg__1) const { return QWidget::metric(QPaintDevice::PaintDeviceMetric(arg__1)); }
    int metric(QPaintDevice::PaintDeviceMetric arg__1) const override;
    QSize minimumSizeHint() const override;
    inline void mouseDoubleClickEvent_protected(QMouseEvent * event) { QWidget::mouseDoubleClickEvent(event); }
    void mouseDoubleClickEvent(QMouseEvent * event) override;
    inline void mouseMoveEvent_protected(QMouseEvent * event) { QWidget::mouseMoveEvent(event); }
    void mouseMoveEvent(QMouseEvent * event) override;
    inline void mousePressEvent_protected(QMouseEvent * event) { QWidget::mousePressEvent(event); }
    void mousePressEvent(QMouseEvent * event) override;
    inline void mouseReleaseEvent_protected(QMouseEvent * event) { QWidget::mouseReleaseEvent(event); }
    void mouseReleaseEvent(QMouseEvent * event) override;
    inline void moveEvent_protected(QMoveEvent * event) { QWidget::moveEvent(event); }
    void moveEvent(QMoveEvent * event) override;
    inline bool nativeEvent_protected(const QByteArray & eventType, void * message, qintptr * result) { return QWidget::nativeEvent(eventType, message, result); }
    bool nativeEvent(const QByteArray & eventType, void * message, qintptr * result) override;
    QPaintEngine * paintEngine() const override;
    inline void paintEvent_protected(QPaintEvent * event) { QWidget::paintEvent(event); }
    void paintEvent(QPaintEvent * event) override;
    inline QPaintDevice * redirected_protected(QPoint * offset) const { return QWidget::redirected(offset); }
    QPaintDevice * redirected(QPoint * offset) const override;
    inline void resizeEvent_protected(QResizeEvent * event) { QWidget::resizeEvent(event); }
    void resizeEvent(QResizeEvent * event) override;
    void setVisible(bool visible) override;
    inline QPainter * sharedPainter_protected() const { return QWidget::sharedPainter(); }
    QPainter * sharedPainter() const override;
    inline void showEvent_protected(QShowEvent * event) { QWidget::showEvent(event); }
    void showEvent(QShowEvent * event) override;
    QSize sizeHint() const override;
    inline void tabletEvent_protected(QTabletEvent * event) { QWidget::tabletEvent(event); }
    void tabletEvent(QTabletEvent * event) override;
    inline void timerEvent_protected(QTimerEvent * event) { QObject::timerEvent(event); }
    void timerEvent(QTimerEvent * event) override;
    inline void wheelEvent_protected(QWheelEvent * event) { QWidget::wheelEvent(event); }
    void wheelEvent(QWheelEvent * event) override;
    ~QtTreePropertyBrowserWrapper();
public:
    int qt_metacall(QMetaObject::Call call, int id, void **args) override;
    void *qt_metacast(const char *_clname) override;
    static void pysideInitQtMetaTypes();
    void resetPyMethodCache();
private:
    mutable bool m_PyMethodCache[52];
};

#  ifndef SBK_QTABSTRACTPROPERTYBROWSERWRAPPER_H
#  define SBK_QTABSTRACTPROPERTYBROWSERWRAPPER_H

// Inherited base class:
class QtAbstractPropertyBrowserWrapper : public QtAbstractPropertyBrowser
{
public:
    QtAbstractPropertyBrowserWrapper(QWidget * parent = 0);
    inline void actionEvent_protected(QActionEvent * event) { QWidget::actionEvent(event); }
    void actionEvent(QActionEvent * event) override;
    inline void changeEvent_protected(QEvent * event) { QWidget::changeEvent(event); }
    void changeEvent(QEvent * event) override;
    inline void childEvent_protected(QChildEvent * event) { QObject::childEvent(event); }
    void childEvent(QChildEvent * event) override;
    inline void closeEvent_protected(QCloseEvent * event) { QWidget::closeEvent(event); }
    void closeEvent(QCloseEvent * event) override;
    inline void connectNotify_protected(const QMetaMethod & signal) { QObject::connectNotify(signal); }
    void connectNotify(const QMetaMethod & signal) override;
    inline void contextMenuEvent_protected(QContextMenuEvent * event) { QWidget::contextMenuEvent(event); }
    void contextMenuEvent(QContextMenuEvent * event) override;
    inline void create_protected(WId arg__1 = 0, bool initializeWindow = true, bool destroyOldWindow = true) { QWidget::create(arg__1, initializeWindow, destroyOldWindow); }
    inline QWidget * createAttributeEditor_protected(QtProperty * property, QWidget * parent, BrowserCol attribute) { return QtAbstractPropertyBrowser::createAttributeEditor(property, parent, BrowserCol(attribute)); }
    QWidget * createAttributeEditor(QtProperty * property, QWidget * parent, BrowserCol attribute) override;
    inline QWidget * createEditor_protected(QtProperty * property, QWidget * parent) { return QtAbstractPropertyBrowser::createEditor(property, parent); }
    QWidget * createEditor(QtProperty * property, QWidget * parent) override;
    inline void customEvent_protected(QEvent * event) { QObject::customEvent(event); }
    void customEvent(QEvent * event) override;
    inline void destroy_protected(bool destroyWindow = true, bool destroySubWindows = true) { QWidget::destroy(destroyWindow, destroySubWindows); }
    int devType() const override;
    inline void disconnectNotify_protected(const QMetaMethod & signal) { QObject::disconnectNotify(signal); }
    void disconnectNotify(const QMetaMethod & signal) override;
    inline void dragEnterEvent_protected(QDragEnterEvent * event) { QWidget::dragEnterEvent(event); }
    void dragEnterEvent(QDragEnterEvent * event) override;
    inline void dragLeaveEvent_protected(QDragLeaveEvent * event) { QWidget::dragLeaveEvent(event); }
    void dragLeaveEvent(QDragLeaveEvent * event) override;
    inline void dragMoveEvent_protected(QDragMoveEvent * event) { QWidget::dragMoveEvent(event); }
    void dragMoveEvent(QDragMoveEvent * event) override;
    inline void dropEvent_protected(QDropEvent * event) { QWidget::dropEvent(event); }
    void dropEvent(QDropEvent * event) override;
    inline void enterEvent_protected(QEnterEvent * event) { QWidget::enterEvent(event); }
    void enterEvent(QEnterEvent * event) override;
    inline bool event_protected(QEvent * event) { return QWidget::event(event); }
    bool event(QEvent * event) override;
    bool eventFilter(QObject * watched, QEvent * event) override;
    inline void focusInEvent_protected(QFocusEvent * event) { QWidget::focusInEvent(event); }
    void focusInEvent(QFocusEvent * event) override;
    inline bool focusNextChild_protected() { return QWidget::focusNextChild(); }
    inline bool focusNextPrevChild_protected(bool next) { return QWidget::focusNextPrevChild(next); }
    bool focusNextPrevChild(bool next) override;
    inline void focusOutEvent_protected(QFocusEvent * event) { QWidget::focusOutEvent(event); }
    void focusOutEvent(QFocusEvent * event) override;
    inline bool focusPreviousChild_protected() { return QWidget::focusPreviousChild(); }
    bool hasHeightForWidth() const override;
    int heightForWidth(int arg__1) const override;
    inline void hideEvent_protected(QHideEvent * event) { QWidget::hideEvent(event); }
    void hideEvent(QHideEvent * event) override;
    inline void initPainter_protected(QPainter * painter) const { QWidget::initPainter(painter); }
    void initPainter(QPainter * painter) const override;
    inline void inputMethodEvent_protected(QInputMethodEvent * event) { QWidget::inputMethodEvent(event); }
    void inputMethodEvent(QInputMethodEvent * event) override;
    QVariant inputMethodQuery(Qt::InputMethodQuery arg__1) const override;
    inline void itemChanged_protected(QtBrowserItem * item) { itemChanged(item); }
    void itemChanged(QtBrowserItem * item) override;
    inline void itemInserted_protected(QtBrowserItem * item, QtBrowserItem * afterItem) { itemInserted(item, afterItem); }
    void itemInserted(QtBrowserItem * item, QtBrowserItem * afterItem) override;
    inline void itemRemoved_protected(QtBrowserItem * item) { itemRemoved(item); }
    void itemRemoved(QtBrowserItem * item) override;
    inline void keyPressEvent_protected(QKeyEvent * event) { QWidget::keyPressEvent(event); }
    void keyPressEvent(QKeyEvent * event) override;
    inline void keyReleaseEvent_protected(QKeyEvent * event) { QWidget::keyReleaseEvent(event); }
    void keyReleaseEvent(QKeyEvent * event) override;
    inline void leaveEvent_protected(QEvent * event) { QWidget::leaveEvent(event); }
    void leaveEvent(QEvent * event) override;
    const QMetaObject * metaObject() const override;
    inline int metric_protected(QPaintDevice::PaintDeviceMetric arg__1) const { return QWidget::metric(QPaintDevice::PaintDeviceMetric(arg__1)); }
    int metric(QPaintDevice::PaintDeviceMetric arg__1) const override;
    QSize minimumSizeHint() const override;
    inline void mouseDoubleClickEvent_protected(QMouseEvent * event) { QWidget::mouseDoubleClickEvent(event); }
    void mouseDoubleClickEvent(QMouseEvent * event) override;
    inline void mouseMoveEvent_protected(QMouseEvent * event) { QWidget::mouseMoveEvent(event); }
    void mouseMoveEvent(QMouseEvent * event) override;
    inline void mousePressEvent_protected(QMouseEvent * event) { QWidget::mousePressEvent(event); }
    void mousePressEvent(QMouseEvent * event) override;
    inline void mouseReleaseEvent_protected(QMouseEvent * event) { QWidget::mouseReleaseEvent(event); }
    void mouseReleaseEvent(QMouseEvent * event) override;
    inline void moveEvent_protected(QMoveEvent * event) { QWidget::moveEvent(event); }
    void moveEvent(QMoveEvent * event) override;
    inline bool nativeEvent_protected(const QByteArray & eventType, void * message, qintptr * result) { return QWidget::nativeEvent(eventType, message, result); }
    bool nativeEvent(const QByteArray & eventType, void * message, qintptr * result) override;
    QPaintEngine * paintEngine() const override;
    inline void paintEvent_protected(QPaintEvent * event) { QWidget::paintEvent(event); }
    void paintEvent(QPaintEvent * event) override;
    inline QPaintDevice * redirected_protected(QPoint * offset) const { return QWidget::redirected(offset); }
    QPaintDevice * redirected(QPoint * offset) const override;
    inline void resizeEvent_protected(QResizeEvent * event) { QWidget::resizeEvent(event); }
    void resizeEvent(QResizeEvent * event) override;
    void setVisible(bool visible) override;
    inline QPainter * sharedPainter_protected() const { return QWidget::sharedPainter(); }
    QPainter * sharedPainter() const override;
    inline void showEvent_protected(QShowEvent * event) { QWidget::showEvent(event); }
    void showEvent(QShowEvent * event) override;
    QSize sizeHint() const override;
    inline void tabletEvent_protected(QTabletEvent * event) { QWidget::tabletEvent(event); }
    void tabletEvent(QTabletEvent * event) override;
    inline void timerEvent_protected(QTimerEvent * event) { QObject::timerEvent(event); }
    void timerEvent(QTimerEvent * event) override;
    inline void updateMicroFocus_protected(Qt::InputMethodQuery query = Qt::ImQueryAll) { QWidget::updateMicroFocus(Qt::InputMethodQuery(query)); }
    inline void wheelEvent_protected(QWheelEvent * event) { QWidget::wheelEvent(event); }
    void wheelEvent(QWheelEvent * event) override;
    ~QtAbstractPropertyBrowserWrapper();
public:
    int qt_metacall(QMetaObject::Call call, int id, void **args) override;
    void *qt_metacast(const char *_clname) override;
    static void pysideInitQtMetaTypes();
    void resetPyMethodCache();
private:
    mutable bool m_PyMethodCache[52];
};

#  endif // SBK_QTABSTRACTPROPERTYBROWSERWRAPPER_H

#  ifndef SBK_QWIDGETWRAPPER_H
#  define SBK_QWIDGETWRAPPER_H

// Inherited base class:
class QWidgetWrapper : public QWidget
{
public:
    QWidgetWrapper(QWidget * parent = nullptr, QFlags<Qt::WindowType> f = Qt::WindowFlags());
    inline void actionEvent_protected(QActionEvent * event) { QWidget::actionEvent(event); }
    void actionEvent(QActionEvent * event) override;
    inline void changeEvent_protected(QEvent * event) { QWidget::changeEvent(event); }
    void changeEvent(QEvent * event) override;
    inline void childEvent_protected(QChildEvent * event) { QObject::childEvent(event); }
    void childEvent(QChildEvent * event) override;
    inline void closeEvent_protected(QCloseEvent * event) { QWidget::closeEvent(event); }
    void closeEvent(QCloseEvent * event) override;
    inline void connectNotify_protected(const QMetaMethod & signal) { QObject::connectNotify(signal); }
    void connectNotify(const QMetaMethod & signal) override;
    inline void contextMenuEvent_protected(QContextMenuEvent * event) { QWidget::contextMenuEvent(event); }
    void contextMenuEvent(QContextMenuEvent * event) override;
    inline void create_protected(WId arg__1 = 0, bool initializeWindow = true, bool destroyOldWindow = true) { QWidget::create(arg__1, initializeWindow, destroyOldWindow); }
    inline void customEvent_protected(QEvent * event) { QObject::customEvent(event); }
    void customEvent(QEvent * event) override;
    inline void destroy_protected(bool destroyWindow = true, bool destroySubWindows = true) { QWidget::destroy(destroyWindow, destroySubWindows); }
    int devType() const override;
    inline void disconnectNotify_protected(const QMetaMethod & signal) { QObject::disconnectNotify(signal); }
    void disconnectNotify(const QMetaMethod & signal) override;
    inline void dragEnterEvent_protected(QDragEnterEvent * event) { QWidget::dragEnterEvent(event); }
    void dragEnterEvent(QDragEnterEvent * event) override;
    inline void dragLeaveEvent_protected(QDragLeaveEvent * event) { QWidget::dragLeaveEvent(event); }
    void dragLeaveEvent(QDragLeaveEvent * event) override;
    inline void dragMoveEvent_protected(QDragMoveEvent * event) { QWidget::dragMoveEvent(event); }
    void dragMoveEvent(QDragMoveEvent * event) override;
    inline void dropEvent_protected(QDropEvent * event) { QWidget::dropEvent(event); }
    void dropEvent(QDropEvent * event) override;
    inline void enterEvent_protected(QEnterEvent * event) { QWidget::enterEvent(event); }
    void enterEvent(QEnterEvent * event) override;
    inline bool event_protected(QEvent * event) { return QWidget::event(event); }
    bool event(QEvent * event) override;
    bool eventFilter(QObject * watched, QEvent * event) override;
    inline void focusInEvent_protected(QFocusEvent * event) { QWidget::focusInEvent(event); }
    void focusInEvent(QFocusEvent * event) override;
    inline bool focusNextChild_protected() { return QWidget::focusNextChild(); }
    inline bool focusNextPrevChild_protected(bool next) { return QWidget::focusNextPrevChild(next); }
    bool focusNextPrevChild(bool next) override;
    inline void focusOutEvent_protected(QFocusEvent * event) { QWidget::focusOutEvent(event); }
    void focusOutEvent(QFocusEvent * event) override;
    inline bool focusPreviousChild_protected() { return QWidget::focusPreviousChild(); }
    bool hasHeightForWidth() const override;
    int heightForWidth(int arg__1) const override;
    inline void hideEvent_protected(QHideEvent * event) { QWidget::hideEvent(event); }
    void hideEvent(QHideEvent * event) override;
    inline void initPainter_protected(QPainter * painter) const { QWidget::initPainter(painter); }
    void initPainter(QPainter * painter) const override;
    inline void inputMethodEvent_protected(QInputMethodEvent * event) { QWidget::inputMethodEvent(event); }
    void inputMethodEvent(QInputMethodEvent * event) override;
    QVariant inputMethodQuery(Qt::InputMethodQuery arg__1) const override;
    inline bool isSignalConnected_protected(const QMetaMethod & signal) const { return QObject::isSignalConnected(signal); }
    inline void keyPressEvent_protected(QKeyEvent * event) { QWidget::keyPressEvent(event); }
    void keyPressEvent(QKeyEvent * event) override;
    inline void keyReleaseEvent_protected(QKeyEvent * event) { QWidget::keyReleaseEvent(event); }
    void keyReleaseEvent(QKeyEvent * event) override;
    inline void leaveEvent_protected(QEvent * event) { QWidget::leaveEvent(event); }
    void leaveEvent(QEvent * event) override;
    const QMetaObject * metaObject() const override;
    inline int metric_protected(QPaintDevice::PaintDeviceMetric arg__1) const { return QWidget::metric(QPaintDevice::PaintDeviceMetric(arg__1)); }
    int metric(QPaintDevice::PaintDeviceMetric arg__1) const override;
    QSize minimumSizeHint() const override;
    inline void mouseDoubleClickEvent_protected(QMouseEvent * event) { QWidget::mouseDoubleClickEvent(event); }
    void mouseDoubleClickEvent(QMouseEvent * event) override;
    inline void mouseMoveEvent_protected(QMouseEvent * event) { QWidget::mouseMoveEvent(event); }
    void mouseMoveEvent(QMouseEvent * event) override;
    inline void mousePressEvent_protected(QMouseEvent * event) { QWidget::mousePressEvent(event); }
    void mousePressEvent(QMouseEvent * event) override;
    inline void mouseReleaseEvent_protected(QMouseEvent * event) { QWidget::mouseReleaseEvent(event); }
    void mouseReleaseEvent(QMouseEvent * event) override;
    inline void moveEvent_protected(QMoveEvent * event) { QWidget::moveEvent(event); }
    void moveEvent(QMoveEvent * event) override;
    inline bool nativeEvent_protected(const QByteArray & eventType, void * message, qintptr * result) { return QWidget::nativeEvent(eventType, message, result); }
    bool nativeEvent(const QByteArray & eventType, void * message, qintptr * result) override;
    QPaintEngine * paintEngine() const override;
    inline void paintEvent_protected(QPaintEvent * event) { QWidget::paintEvent(event); }
    void paintEvent(QPaintEvent * event) override;
    inline int receivers_protected(const char * signal) const { return QObject::receivers(signal); }
    inline QPaintDevice * redirected_protected(QPoint * offset) const { return QWidget::redirected(offset); }
    QPaintDevice * redirected(QPoint * offset) const override;
    inline void resizeEvent_protected(QResizeEvent * event) { QWidget::resizeEvent(event); }
    void resizeEvent(QResizeEvent * event) override;
    inline QObject * sender_protected() const { return QObject::sender(); }
    inline int senderSignalIndex_protected() const { return QObject::senderSignalIndex(); }
    void setVisible(bool visible) override;
    inline QPainter * sharedPainter_protected() const { return QWidget::sharedPainter(); }
    QPainter * sharedPainter() const override;
    inline void showEvent_protected(QShowEvent * event) { QWidget::showEvent(event); }
    void showEvent(QShowEvent * event) override;
    QSize sizeHint() const override;
    inline void tabletEvent_protected(QTabletEvent * event) { QWidget::tabletEvent(event); }
    void tabletEvent(QTabletEvent * event) override;
    inline void timerEvent_protected(QTimerEvent * event) { QObject::timerEvent(event); }
    void timerEvent(QTimerEvent * event) override;
    inline void updateMicroFocus_protected(Qt::InputMethodQuery query = Qt::ImQueryAll) { QWidget::updateMicroFocus(Qt::InputMethodQuery(query)); }
    inline void wheelEvent_protected(QWheelEvent * event) { QWidget::wheelEvent(event); }
    void wheelEvent(QWheelEvent * event) override;
    ~QWidgetWrapper();
public:
    int qt_metacall(QMetaObject::Call call, int id, void **args) override;
    void *qt_metacast(const char *_clname) override;
    static void pysideInitQtMetaTypes();
    void resetPyMethodCache();
private:
    mutable bool m_PyMethodCache[47];
};

#  endif // SBK_QWIDGETWRAPPER_H

#  ifndef SBK_QOBJECTWRAPPER_H
#  define SBK_QOBJECTWRAPPER_H

// Inherited base class:
class QObjectWrapper : public QObject
{
public:
    QObjectWrapper(QObject * parent = nullptr);
    inline void childEvent_protected(QChildEvent * event) { QObject::childEvent(event); }
    void childEvent(QChildEvent * event) override;
    inline void connectNotify_protected(const QMetaMethod & signal) { QObject::connectNotify(signal); }
    void connectNotify(const QMetaMethod & signal) override;
    inline void customEvent_protected(QEvent * event) { QObject::customEvent(event); }
    void customEvent(QEvent * event) override;
    inline void disconnectNotify_protected(const QMetaMethod & signal) { QObject::disconnectNotify(signal); }
    void disconnectNotify(const QMetaMethod & signal) override;
    bool event(QEvent * event) override;
    bool eventFilter(QObject * watched, QEvent * event) override;
    inline bool isSignalConnected_protected(const QMetaMethod & signal) const { return QObject::isSignalConnected(signal); }
    const QMetaObject * metaObject() const override;
    inline int receivers_protected(const char * signal) const { return QObject::receivers(signal); }
    inline QObject * sender_protected() const { return QObject::sender(); }
    inline int senderSignalIndex_protected() const { return QObject::senderSignalIndex(); }
    inline void timerEvent_protected(QTimerEvent * event) { QObject::timerEvent(event); }
    void timerEvent(QTimerEvent * event) override;
    ~QObjectWrapper();
public:
    int qt_metacall(QMetaObject::Call call, int id, void **args) override;
    void *qt_metacast(const char *_clname) override;
    static void pysideInitQtMetaTypes();
    void resetPyMethodCache();
private:
    mutable bool m_PyMethodCache[7];
};

#  endif // SBK_QOBJECTWRAPPER_H

#endif // SBK_QTTREEPROPERTYBROWSERWRAPPER_H

