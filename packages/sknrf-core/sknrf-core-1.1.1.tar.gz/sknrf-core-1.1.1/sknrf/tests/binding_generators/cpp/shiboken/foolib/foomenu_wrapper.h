#ifndef SBK_FOOMENUWRAPPER_H
#define SBK_FOOMENUWRAPPER_H

#include <shiboken.h>

#include <fooclass.h>

namespace PySide { class DynamicQMetaObject; }

class FooMenuWrapper : public FooMenu
{
public:
    FooMenuWrapper(QWidget * parent = 0);
    inline void actionEvent_protected(QActionEvent * event) { FooMenu::actionEvent(event); }
    virtual void actionEvent(QActionEvent * event);
    inline void changeEvent_protected(QEvent * event) { FooMenu::changeEvent(event); }
    virtual void changeEvent(QEvent * event);
    inline void childEvent_protected(QChildEvent * arg__1) { FooMenu::childEvent(arg__1); }
    virtual void childEvent(QChildEvent * arg__1);
    inline void closeEvent_protected(QCloseEvent * event) { FooMenu::closeEvent(event); }
    virtual void closeEvent(QCloseEvent * event);
    inline void connectNotify_protected(const char * signal) { FooMenu::connectNotify(signal); }
    virtual void connectNotify(const char * signal);
    inline void contextMenuEvent_protected(QContextMenuEvent * event) { FooMenu::contextMenuEvent(event); }
    virtual void contextMenuEvent(QContextMenuEvent * event);
    inline void customEvent_protected(QEvent * arg__1) { FooMenu::customEvent(arg__1); }
    virtual void customEvent(QEvent * arg__1);
    inline void destroy_protected(bool destroyWindow = true, bool destroySubWindows = true) { FooMenu::destroy(destroyWindow, destroySubWindows); }
    virtual int devType() const;
    inline void disconnectNotify_protected(const char * signal) { FooMenu::disconnectNotify(signal); }
    virtual void disconnectNotify(const char * signal);
    inline void dragEnterEvent_protected(QDragEnterEvent * event) { FooMenu::dragEnterEvent(event); }
    virtual void dragEnterEvent(QDragEnterEvent * event);
    inline void dragLeaveEvent_protected(QDragLeaveEvent * event) { FooMenu::dragLeaveEvent(event); }
    virtual void dragLeaveEvent(QDragLeaveEvent * event);
    inline void dragMoveEvent_protected(QDragMoveEvent * event) { FooMenu::dragMoveEvent(event); }
    virtual void dragMoveEvent(QDragMoveEvent * event);
    inline void dropEvent_protected(QDropEvent * event) { FooMenu::dropEvent(event); }
    virtual void dropEvent(QDropEvent * event);
    inline void enterEvent_protected(QEvent * event) { FooMenu::enterEvent(event); }
    virtual void enterEvent(QEvent * event);
    inline bool event_protected(QEvent * arg__1) { return FooMenu::event(arg__1); }
    virtual bool event(QEvent * arg__1);
    virtual bool eventFilter(QObject * arg__1, QEvent * arg__2);
    inline void focusInEvent_protected(QFocusEvent * event) { FooMenu::focusInEvent(event); }
    virtual void focusInEvent(QFocusEvent * event);
    inline bool focusNextChild_protected() { return FooMenu::focusNextChild(); }
    inline bool focusNextPrevChild_protected(bool next) { return FooMenu::focusNextPrevChild(next); }
    virtual bool focusNextPrevChild(bool next);
    inline void focusOutEvent_protected(QFocusEvent * event) { FooMenu::focusOutEvent(event); }
    virtual void focusOutEvent(QFocusEvent * event);
    inline bool focusPreviousChild_protected() { return FooMenu::focusPreviousChild(); }
    virtual int heightForWidth(int arg__1) const;
    inline void hideEvent_protected(QHideEvent * event) { FooMenu::hideEvent(event); }
    virtual void hideEvent(QHideEvent * event);
    inline void inputMethodEvent_protected(QInputMethodEvent * event) { FooMenu::inputMethodEvent(event); }
    virtual void inputMethodEvent(QInputMethodEvent * event);
    virtual QVariant inputMethodQuery(Qt::InputMethodQuery arg__1) const;
    inline void keyPressEvent_protected(QKeyEvent * event) { FooMenu::keyPressEvent(event); }
    virtual void keyPressEvent(QKeyEvent * event);
    inline void keyReleaseEvent_protected(QKeyEvent * event) { FooMenu::keyReleaseEvent(event); }
    virtual void keyReleaseEvent(QKeyEvent * event);
    inline void languageChange_protected() { FooMenu::languageChange(); }
    virtual void languageChange();
    inline void leaveEvent_protected(QEvent * event) { FooMenu::leaveEvent(event); }
    virtual void leaveEvent(QEvent * event);
    virtual const QMetaObject * metaObject() const;
    inline int metric_protected(int arg__1) const { return FooMenu::metric(QPaintDevice::PaintDeviceMetric(arg__1)); }
    virtual int metric(QPaintDevice::PaintDeviceMetric arg__1) const;
    virtual QSize minimumSizeHint() const;
    inline void mouseDoubleClickEvent_protected(QMouseEvent * event) { FooMenu::mouseDoubleClickEvent(event); }
    virtual void mouseDoubleClickEvent(QMouseEvent * event);
    inline void mouseMoveEvent_protected(QMouseEvent * event) { FooMenu::mouseMoveEvent(event); }
    virtual void mouseMoveEvent(QMouseEvent * event);
    inline void mousePressEvent_protected(QMouseEvent * event) { FooMenu::mousePressEvent(event); }
    virtual void mousePressEvent(QMouseEvent * event);
    inline void mouseReleaseEvent_protected(QMouseEvent * event) { FooMenu::mouseReleaseEvent(event); }
    virtual void mouseReleaseEvent(QMouseEvent * event);
    inline void moveEvent_protected(QMoveEvent * event) { FooMenu::moveEvent(event); }
    virtual void moveEvent(QMoveEvent * event);
    virtual QPaintEngine * paintEngine() const;
    inline void paintEvent_protected(QPaintEvent * event) { FooMenu::paintEvent(event); }
    virtual void paintEvent(QPaintEvent * event);
    inline void resetInputContext_protected() { FooMenu::resetInputContext(); }
    inline void resizeEvent_protected(QResizeEvent * event) { FooMenu::resizeEvent(event); }
    virtual void resizeEvent(QResizeEvent * event);
    virtual void setVisible(bool visible);
    inline void showEvent_protected(QShowEvent * event) { FooMenu::showEvent(event); }
    virtual void showEvent(QShowEvent * event);
    virtual QSize sizeHint() const;
    inline void tabletEvent_protected(QTabletEvent * event) { FooMenu::tabletEvent(event); }
    virtual void tabletEvent(QTabletEvent * event);
    inline void timerEvent_protected(QTimerEvent * arg__1) { FooMenu::timerEvent(arg__1); }
    virtual void timerEvent(QTimerEvent * arg__1);
    inline void updateMicroFocus_protected() { FooMenu::updateMicroFocus(); }
    inline void wheelEvent_protected(QWheelEvent * event) { FooMenu::wheelEvent(event); }
    virtual void wheelEvent(QWheelEvent * event);
    virtual ~FooMenuWrapper();
public:
    virtual int qt_metacall(QMetaObject::Call call, int id, void** args);
    virtual void* qt_metacast(const char* _clname);
    static void pysideInitQtMetaTypes();
};

#endif // SBK_FOOMENUWRAPPER_H

