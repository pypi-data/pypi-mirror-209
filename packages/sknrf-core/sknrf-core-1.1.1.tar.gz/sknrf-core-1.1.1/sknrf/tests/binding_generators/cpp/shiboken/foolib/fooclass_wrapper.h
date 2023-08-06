#ifndef SBK_FOOCLASSWRAPPER_H
#define SBK_FOOCLASSWRAPPER_H

#include <shiboken.h>

#include <fooclass.h>

namespace PySide { class DynamicQMetaObject; }

class FooClassWrapper : public FooClass
{
public:
    FooClassWrapper(QObject * parent = 0);
    inline void childEvent_protected(QChildEvent * arg__1) { FooClass::childEvent(arg__1); }
    virtual void childEvent(QChildEvent * arg__1);
    inline void connectNotify_protected(const char * signal) { FooClass::connectNotify(signal); }
    virtual void connectNotify(const char * signal);
    inline void customEvent_protected(QEvent * arg__1) { FooClass::customEvent(arg__1); }
    virtual void customEvent(QEvent * arg__1);
    inline void disconnectNotify_protected(const char * signal) { FooClass::disconnectNotify(signal); }
    virtual void disconnectNotify(const char * signal);
    virtual bool event(QEvent * arg__1);
    virtual bool eventFilter(QObject * arg__1, QEvent * arg__2);
    virtual const QMetaObject * metaObject() const;
    inline int receivers_protected(const char * signal) const { return FooClass::receivers(signal); }
    inline QObject * sender_protected() const { return FooClass::sender(); }
    inline int senderSignalIndex_protected() const { return FooClass::senderSignalIndex(); }
    inline void timerEvent_protected(QTimerEvent * arg__1) { FooClass::timerEvent(arg__1); }
    virtual void timerEvent(QTimerEvent * arg__1);
    virtual ~FooClassWrapper();
public:
    virtual int qt_metacall(QMetaObject::Call call, int id, void** args);
    virtual void* qt_metacast(const char* _clname);
    static void pysideInitQtMetaTypes();
};

#endif // SBK_FOOCLASSWRAPPER_H

