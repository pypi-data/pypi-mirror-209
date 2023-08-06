#ifndef SBK_QTABSTRACTEDITORFACTORYBASEWRAPPER_H
#define SBK_QTABSTRACTEDITORFACTORYBASEWRAPPER_H

#include <qtpropertybrowser.h>


// Argument includes
#include <QAnyStringView>
#include <QList>
#include <QString>
#include <qbytearray.h>
#include <qcoreevent.h>
#include <qmetaobject.h>
#include <qnamespace.h>
#include <qobject.h>
#include <qobjectdefs.h>
#include <qtpropertybrowser.h>
#include <qtpropertybrowserutils_p.h>
#include <qvariant.h>
#include <qwidget.h>
namespace PySide { class DynamicQMetaObject; }

class QtAbstractEditorFactoryBaseWrapper : public QtAbstractEditorFactoryBase
{
public:
    QtAbstractEditorFactoryBaseWrapper(QObject * parent = 0);
    inline void breakConnection_protected(QtAbstractPropertyManager * manager) { breakConnection(manager); }
    void breakConnection(QtAbstractPropertyManager * manager) override;
    inline void childEvent_protected(QChildEvent * event) { QObject::childEvent(event); }
    void childEvent(QChildEvent * event) override;
    inline void connectNotify_protected(const QMetaMethod & signal) { QObject::connectNotify(signal); }
    void connectNotify(const QMetaMethod & signal) override;
    QWidget * createAttributeEditor(QtProperty * property, QWidget * parent, BrowserCol atttribute) override;
    QWidget * createEditor(QtProperty * property, QWidget * parent) override;
    inline void customEvent_protected(QEvent * event) { QObject::customEvent(event); }
    void customEvent(QEvent * event) override;
    inline void disconnectNotify_protected(const QMetaMethod & signal) { QObject::disconnectNotify(signal); }
    void disconnectNotify(const QMetaMethod & signal) override;
    bool event(QEvent * event) override;
    bool eventFilter(QObject * watched, QEvent * event) override;
    inline bool isSignalConnected_protected(const QMetaMethod & signal) const { return QObject::isSignalConnected(signal); }
    inline void managerDestroyed_protected(QObject * manager) { managerDestroyed(manager); }
    void managerDestroyed(QObject * manager) override;
    const QMetaObject * metaObject() const override;
    inline int receivers_protected(const char * signal) const { return QObject::receivers(signal); }
    inline QObject * sender_protected() const { return QObject::sender(); }
    inline int senderSignalIndex_protected() const { return QObject::senderSignalIndex(); }
    inline void timerEvent_protected(QTimerEvent * event) { QObject::timerEvent(event); }
    void timerEvent(QTimerEvent * event) override;
    ~QtAbstractEditorFactoryBaseWrapper();
public:
    int qt_metacall(QMetaObject::Call call, int id, void **args) override;
    void *qt_metacast(const char *_clname) override;
    static void pysideInitQtMetaTypes();
    void resetPyMethodCache();
private:
    mutable bool m_PyMethodCache[11];
};

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

#endif // SBK_QTABSTRACTEDITORFACTORYBASEWRAPPER_H

