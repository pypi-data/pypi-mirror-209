
// default includes
#include <shiboken.h>
#ifndef QT_NO_VERSION_TAGGING
#  define QT_NO_VERSION_TAGGING
#endif
#include <QtCore/QDebug>
#include <pysideqobject.h>
#include <pysidesignal.h>
#include <pysideproperty.h>
#include <signalmanager.h>
#include <pysidemetafunction.h>
#include <pysideqenum.h>
#include <pysideqflags.h>
#include <pysideqmetatype.h>
#include <pysideutils.h>
#include <feature_select.h>
QT_WARNING_DISABLE_DEPRECATED


// module include
#include "qtpropertybrowser_python.h"

// main header
#include "qtabstracteditorfactorybase_wrapper.h"

#include <cctype>
#include <cstring>
#include <iterator>
#include <typeinfo>

template <class T>
static const char *typeNameOf(const T &t)
{
    const char *typeName =  typeid(t).name();
    auto size = std::strlen(typeName);
#if defined(Q_CC_MSVC) // MSVC: "class QPaintDevice * __ptr64"
    if (auto lastStar = strchr(typeName, '*')) {
        // MSVC: "class QPaintDevice * __ptr64"
        while (*--lastStar == ' ') {
        }
        size = lastStar - typeName + 1;
    }
#else // g++, Clang: "QPaintDevice *" -> "P12QPaintDevice"
    if (size > 2 && typeName[0] == 'P' && std::isdigit(typeName[1])) {
        ++typeName;
        --size;
    }
#endif
    char *result = new char[size + 1];
    result[size] = '\0';
    memcpy(result, typeName, size);
    return result;
}

// Native ---------------------------------------------------------

void QtAbstractEditorFactoryBaseWrapper::pysideInitQtMetaTypes()
{
}

void QtAbstractEditorFactoryBaseWrapper::resetPyMethodCache()
{
    std::fill_n(m_PyMethodCache, sizeof(m_PyMethodCache) / sizeof(m_PyMethodCache[0]), false);
}

QtAbstractEditorFactoryBaseWrapper::QtAbstractEditorFactoryBaseWrapper(QObject * parent) : QtAbstractEditorFactoryBase(parent)
{
    resetPyMethodCache();
    // ... middle
}

void QtAbstractEditorFactoryBaseWrapper::breakConnection(QtAbstractPropertyManager * manager)
{
    if (m_PyMethodCache[0]) {
        Shiboken::GilState gil;
        Shiboken::Errors::setPureVirtualMethodError("QtAbstractEditorFactoryBase.breakConnection");
        return;
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "breakConnection";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[0] = true;
        Shiboken::Errors::setPureVirtualMethodError("QtAbstractEditorFactoryBase.breakConnection");
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYMANAGER_IDX], manager)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

void QtAbstractEditorFactoryBaseWrapper::childEvent(QChildEvent * event)
{
    if (m_PyMethodCache[1]) {
        return this->::QObject::childEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "childEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[1] = true;
        gil.release();
        return this->::QObject::childEvent(event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtCoreTypes[SBK_QCHILDEVENT_IDX], event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

void QtAbstractEditorFactoryBaseWrapper::connectNotify(const QMetaMethod & signal)
{
    if (m_PyMethodCache[2]) {
        return this->::QObject::connectNotify(signal);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "connectNotify";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[2] = true;
        gil.release();
        return this->::QObject::connectNotify(signal);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::copyToPython(SbkPySide6_QtCoreTypes[SBK_QMETAMETHOD_IDX], &signal)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

QWidget * QtAbstractEditorFactoryBaseWrapper::createAttributeEditor(QtProperty * property, QWidget * parent, BrowserCol atttribute)
{
    if (m_PyMethodCache[3]) {
        Shiboken::GilState gil;
        Shiboken::Errors::setPureVirtualMethodError("QtAbstractEditorFactoryBase.createAttributeEditor");
        return nullptr;
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return nullptr;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "createAttributeEditor";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[3] = true;
        Shiboken::Errors::setPureVirtualMethodError("QtAbstractEditorFactoryBase.createAttributeEditor");
        return nullptr;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(NNN)",
        Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], property),
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtWidgetsTypes[SBK_QWIDGET_IDX], parent),
        Shiboken::Conversions::copyToPython(PepType_SETP(reinterpret_cast<SbkEnumType *>(SbkqtpropertybrowserTypes[SBK_BROWSERCOL_IDX]))->converter, &atttribute)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return nullptr;
    }
    // Check return type
    Shiboken::Conversions::PythonToCppConversion pythonToCpp =
        Shiboken::Conversions::pythonToCppPointerConversion(SbkPySide6_QtWidgetsTypes[SBK_QWIDGET_IDX], pyResult);
    if (!pythonToCpp) {
        Shiboken::Warnings::warnInvalidReturnValue("QtAbstractEditorFactoryBase", "createAttributeEditor", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QWidget >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return nullptr;
    }
    ::QWidget *cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QWidget * QtAbstractEditorFactoryBaseWrapper::createEditor(QtProperty * property, QWidget * parent)
{
    if (m_PyMethodCache[4]) {
        Shiboken::GilState gil;
        Shiboken::Errors::setPureVirtualMethodError("QtAbstractEditorFactoryBase.createEditor");
        return nullptr;
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return nullptr;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "createEditor";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[4] = true;
        Shiboken::Errors::setPureVirtualMethodError("QtAbstractEditorFactoryBase.createEditor");
        return nullptr;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(NN)",
        Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], property),
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtWidgetsTypes[SBK_QWIDGET_IDX], parent)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return nullptr;
    }
    // Check return type
    Shiboken::Conversions::PythonToCppConversion pythonToCpp =
        Shiboken::Conversions::pythonToCppPointerConversion(SbkPySide6_QtWidgetsTypes[SBK_QWIDGET_IDX], pyResult);
    if (!pythonToCpp) {
        Shiboken::Warnings::warnInvalidReturnValue("QtAbstractEditorFactoryBase", "createEditor", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QWidget >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return nullptr;
    }
    ::QWidget *cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtAbstractEditorFactoryBaseWrapper::customEvent(QEvent * event)
{
    if (m_PyMethodCache[5]) {
        return this->::QObject::customEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "customEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[5] = true;
        gil.release();
        return this->::QObject::customEvent(event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtCoreTypes[SBK_QEVENT_IDX], event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

void QtAbstractEditorFactoryBaseWrapper::disconnectNotify(const QMetaMethod & signal)
{
    if (m_PyMethodCache[6]) {
        return this->::QObject::disconnectNotify(signal);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "disconnectNotify";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[6] = true;
        gil.release();
        return this->::QObject::disconnectNotify(signal);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::copyToPython(SbkPySide6_QtCoreTypes[SBK_QMETAMETHOD_IDX], &signal)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

bool QtAbstractEditorFactoryBaseWrapper::event(QEvent * event)
{
    if (m_PyMethodCache[7])
        return this->::QObject::event(event);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return false;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "event";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[7] = true;
        gil.release();
        return this->::QObject::event(event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtCoreTypes[SBK_QEVENT_IDX], event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return false;
    }
    // Check return type
    Shiboken::Conversions::PythonToCppConversion pythonToCpp =
        Shiboken::Conversions::pythonToCppConversion(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), pyResult);
    if (!pythonToCpp) {
        Shiboken::Warnings::warnInvalidReturnValue("QtAbstractEditorFactoryBase", "event", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

bool QtAbstractEditorFactoryBaseWrapper::eventFilter(QObject * watched, QEvent * event)
{
    if (m_PyMethodCache[8])
        return this->::QObject::eventFilter(watched, event);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return false;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "eventFilter";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[8] = true;
        gil.release();
        return this->::QObject::eventFilter(watched, event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(NN)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtCoreTypes[SBK_QOBJECT_IDX], watched),
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtCoreTypes[SBK_QEVENT_IDX], event)
    ));
    bool invalidateArg2 = PyTuple_GET_ITEM(pyArgs, 1)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (invalidateArg2)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 1));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return false;
    }
    // Check return type
    Shiboken::Conversions::PythonToCppConversion pythonToCpp =
        Shiboken::Conversions::pythonToCppConversion(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), pyResult);
    if (!pythonToCpp) {
        Shiboken::Warnings::warnInvalidReturnValue("QtAbstractEditorFactoryBase", "eventFilter", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtAbstractEditorFactoryBaseWrapper::managerDestroyed(QObject * manager)
{
    if (m_PyMethodCache[9]) {
        Shiboken::GilState gil;
        Shiboken::Errors::setPureVirtualMethodError("QtAbstractEditorFactoryBase.managerDestroyed");
        return;
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "managerDestroyed";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[9] = true;
        Shiboken::Errors::setPureVirtualMethodError("QtAbstractEditorFactoryBase.managerDestroyed");
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtCoreTypes[SBK_QOBJECT_IDX], manager)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

void QtAbstractEditorFactoryBaseWrapper::timerEvent(QTimerEvent * event)
{
    if (m_PyMethodCache[10]) {
        return this->::QObject::timerEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "timerEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[10] = true;
        gil.release();
        return this->::QObject::timerEvent(event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtCoreTypes[SBK_QTIMEREVENT_IDX], event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

const QMetaObject *QtAbstractEditorFactoryBaseWrapper::metaObject() const
{
    if (QObject::d_ptr->metaObject)
        return QObject::d_ptr->dynamicMetaObject();
    SbkObject *pySelf = Shiboken::BindingManager::instance().retrieveWrapper(this);
    if (pySelf == nullptr)
        return QtAbstractEditorFactoryBase::metaObject();
    return PySide::SignalManager::retrieveMetaObject(reinterpret_cast<PyObject *>(pySelf));
}

int QtAbstractEditorFactoryBaseWrapper::qt_metacall(QMetaObject::Call call, int id, void **args)
{
    int result = QtAbstractEditorFactoryBase::qt_metacall(call, id, args);
    return result < 0 ? result : PySide::SignalManager::qt_metacall(this, call, id, args);
}

void *QtAbstractEditorFactoryBaseWrapper::qt_metacast(const char *_clname)
{
    if (!_clname)
        return {};
    SbkObject *pySelf = Shiboken::BindingManager::instance().retrieveWrapper(this);
    if (pySelf && PySide::inherits(Py_TYPE(pySelf), _clname))
        return static_cast<void *>(const_cast< QtAbstractEditorFactoryBaseWrapper *>(this));
    return QtAbstractEditorFactoryBase::qt_metacast(_clname);
}

QtAbstractEditorFactoryBaseWrapper::~QtAbstractEditorFactoryBaseWrapper()
{
    SbkObject *wrapper = Shiboken::BindingManager::instance().retrieveWrapper(this);
    Shiboken::Object::destroy(wrapper, this);
}

// Target ---------------------------------------------------------

extern "C" {
static int
Sbk_QtAbstractEditorFactoryBase_Init(PyObject *self, PyObject *args, PyObject *kwds)
{
    SBK_UNUSED(args)
    SBK_UNUSED(kwds)
    const QMetaObject *metaObject;
    SbkObject *sbkSelf = reinterpret_cast<SbkObject *>(self);
    PyTypeObject *type = self->ob_type;
    PyTypeObject *myType = SbkqtpropertybrowserTypes[SBK_QTABSTRACTEDITORFACTORYBASE_IDX];
    if (type == myType) {
        Shiboken::Errors::setInstantiateAbstractClass("QtAbstractEditorFactoryBase");
        return -1;
    }

    PySide::Feature::Select(self);
    if (Shiboken::Object::isUserType(self) && !Shiboken::ObjectType::canCallConstructor(self->ob_type, Shiboken::SbkType< ::QtAbstractEditorFactoryBase >()))
        return -1;

    ::QtAbstractEditorFactoryBaseWrapper *cptr{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtAbstractEditorFactoryBase.__init__";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp[1];
    SBK_UNUSED(pythonToCpp)
    const Py_ssize_t numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {nullptr};

    // invalid argument lengths

    if (!PyArg_ParseTuple(args, "|O:QtAbstractEditorFactoryBase", &(pyArgs[0])))
        return -1;


    // Overloaded function decisor
    // 0: QtAbstractEditorFactoryBase::QtAbstractEditorFactoryBase(QObject*)
    if (numArgs == 0) {
        overloadId = 0; // QtAbstractEditorFactoryBase(QObject*)
    } else if (numArgs >= 1
        && (pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkPySide6_QtCoreTypes[SBK_QOBJECT_IDX], (pyArgs[0])))) {
        overloadId = 0; // QtAbstractEditorFactoryBase(QObject*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtAbstractEditorFactoryBase_Init_TypeError;

    // Call function/method
    {
        if (kwds && PyDict_Size(kwds) > 0) {
            PyObject *value{};
            Shiboken::AutoDecRef kwds_dup(PyDict_Copy(kwds));
            static PyObject *const key_parent = Shiboken::String::createStaticString("parent");
            if (PyDict_Contains(kwds, key_parent)) {
                value = PyDict_GetItem(kwds, key_parent);
                if (value && pyArgs[0]) {
                    errInfo.reset(key_parent);
                    Py_INCREF(errInfo.object());
                    goto Sbk_QtAbstractEditorFactoryBase_Init_TypeError;
                }
                if (value) {
                    pyArgs[0] = value;
                    if (!(pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkPySide6_QtCoreTypes[SBK_QOBJECT_IDX], (pyArgs[0]))))
                        goto Sbk_QtAbstractEditorFactoryBase_Init_TypeError;
                }
                PyDict_DelItem(kwds_dup, key_parent);
            }
            if (PyDict_Size(kwds_dup) > 0) {
                errInfo.reset(kwds_dup.release());
                // fall through to handle extra keyword signals and properties
            }
        }
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return -1;
        ::QObject *cppArg0 = 0;
        if (pythonToCpp[0])
            pythonToCpp[0](pyArgs[0], &cppArg0);

        if (!PyErr_Occurred()) {
            // QtAbstractEditorFactoryBase(QObject*)
            void *addr = PySide::nextQObjectMemoryAddr();
            if (addr) {
                cptr = new (addr) ::QtAbstractEditorFactoryBaseWrapper(cppArg0);
                PySide::setNextQObjectMemoryAddr(nullptr);
            } else {
                cptr = new ::QtAbstractEditorFactoryBaseWrapper(cppArg0);
            }

            // Ownership transferences (constructor heuristics).
            Shiboken::Object::setParent(pyArgs[0], self);
        }
    }

    if (PyErr_Occurred() || !Shiboken::Object::setCppPointer(sbkSelf, Shiboken::SbkType< ::QtAbstractEditorFactoryBase >(), cptr)) {
        delete cptr;
        return -1;
    }
    if (!cptr) goto Sbk_QtAbstractEditorFactoryBase_Init_TypeError;

    Shiboken::Object::setValidCpp(sbkSelf, true);
    Shiboken::Object::setHasCppWrapper(sbkSelf, true);
    if (Shiboken::BindingManager::instance().hasWrapper(cptr)) {
        Shiboken::BindingManager::instance().releaseWrapper(Shiboken::BindingManager::instance().retrieveWrapper(cptr));
    }
    Shiboken::BindingManager::instance().registerWrapper(sbkSelf, cptr);

    // QObject setup
    PySide::Signal::updateSourceObject(self);
    metaObject = cptr->metaObject(); // <- init python qt properties
    if (!errInfo.isNull() && PyDict_Check(errInfo.object())) {
        if (!PySide::fillQtProperties(self, metaObject, errInfo))
            goto Sbk_QtAbstractEditorFactoryBase_Init_TypeError;
    };


    return 1;

    Sbk_QtAbstractEditorFactoryBase_Init_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return -1;
}

static PyObject *Sbk_QtAbstractEditorFactoryBaseFunc_breakConnection(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtAbstractEditorFactoryBaseWrapper *>(reinterpret_cast< ::QtAbstractEditorFactoryBase *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTABSTRACTEDITORFACTORYBASE_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtAbstractEditorFactoryBase.breakConnection";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtAbstractEditorFactoryBase::breakConnection(QtAbstractPropertyManager*)
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYMANAGER_IDX], (pyArg)))) {
        overloadId = 0; // breakConnection(QtAbstractPropertyManager*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtAbstractEditorFactoryBaseFunc_breakConnection_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtAbstractPropertyManager *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // breakConnection(QtAbstractPropertyManager*)
            if (Shiboken::Object::hasCppWrapper(reinterpret_cast<SbkObject *>(self))) {
                Shiboken::Errors::setPureVirtualMethodError("QtAbstractEditorFactoryBase.breakConnection");
                return {};
            }
            static_cast<::QtAbstractEditorFactoryBaseWrapper *>(cppSelf)->breakConnection_protected(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtAbstractEditorFactoryBaseFunc_breakConnection_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtAbstractEditorFactoryBaseFunc_createAttributeEditor(PyObject *self, PyObject *args)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtAbstractEditorFactoryBaseWrapper *>(reinterpret_cast< ::QtAbstractEditorFactoryBase *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTABSTRACTEDITORFACTORYBASE_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtAbstractEditorFactoryBase.createAttributeEditor";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp[3];
    SBK_UNUSED(pythonToCpp)
    const Py_ssize_t numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {nullptr, nullptr, nullptr};

    // invalid argument lengths

    if (!PyArg_UnpackTuple(args, "createAttributeEditor", 3, 3, &(pyArgs[0]), &(pyArgs[1]), &(pyArgs[2])))
        return {};


    // Overloaded function decisor
    // 0: QtAbstractEditorFactoryBase::createAttributeEditor(QtProperty*,QWidget*,BrowserCol)->QWidget*
    if (numArgs == 3
        && (pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::pythonToCppPointerConversion(SbkPySide6_QtWidgetsTypes[SBK_QWIDGET_IDX], (pyArgs[1])))
        && (pythonToCpp[2] = Shiboken::Conversions::pythonToCppConversion(PepType_SETP(reinterpret_cast<SbkEnumType *>(SbkqtpropertybrowserTypes[SBK_BROWSERCOL_IDX]))->converter, (pyArgs[2])))) {
        overloadId = 0; // createAttributeEditor(QtProperty*,QWidget*,BrowserCol)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtAbstractEditorFactoryBaseFunc_createAttributeEditor_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp[0](pyArgs[0], &cppArg0);
        if (!Shiboken::Object::isValid(pyArgs[1]))
            return {};
        ::QWidget *cppArg1;
        pythonToCpp[1](pyArgs[1], &cppArg1);
        ::BrowserCol cppArg2{NONE};
        pythonToCpp[2](pyArgs[2], &cppArg2);

        if (!PyErr_Occurred()) {
            // createAttributeEditor(QtProperty*,QWidget*,BrowserCol)
            if (Shiboken::Object::hasCppWrapper(reinterpret_cast<SbkObject *>(self))) {
                Shiboken::Errors::setPureVirtualMethodError("QtAbstractEditorFactoryBase.createAttributeEditor");
                return {};
            }
            QWidget * cppResult = cppSelf->createAttributeEditor(cppArg0, cppArg1, cppArg2);
            pyResult = Shiboken::Conversions::pointerToPython(SbkPySide6_QtWidgetsTypes[SBK_QWIDGET_IDX], cppResult);
            // Ownership transferences (return value heuristics).
            Shiboken::Object::setParent(self, pyResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtAbstractEditorFactoryBaseFunc_createAttributeEditor_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtAbstractEditorFactoryBaseFunc_createEditor(PyObject *self, PyObject *args)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtAbstractEditorFactoryBaseWrapper *>(reinterpret_cast< ::QtAbstractEditorFactoryBase *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTABSTRACTEDITORFACTORYBASE_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtAbstractEditorFactoryBase.createEditor";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp[2];
    SBK_UNUSED(pythonToCpp)
    const Py_ssize_t numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {nullptr, nullptr};

    // invalid argument lengths

    if (!PyArg_UnpackTuple(args, "createEditor", 2, 2, &(pyArgs[0]), &(pyArgs[1])))
        return {};


    // Overloaded function decisor
    // 0: QtAbstractEditorFactoryBase::createEditor(QtProperty*,QWidget*)->QWidget*
    if (numArgs == 2
        && (pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::pythonToCppPointerConversion(SbkPySide6_QtWidgetsTypes[SBK_QWIDGET_IDX], (pyArgs[1])))) {
        overloadId = 0; // createEditor(QtProperty*,QWidget*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtAbstractEditorFactoryBaseFunc_createEditor_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp[0](pyArgs[0], &cppArg0);
        if (!Shiboken::Object::isValid(pyArgs[1]))
            return {};
        ::QWidget *cppArg1;
        pythonToCpp[1](pyArgs[1], &cppArg1);

        if (!PyErr_Occurred()) {
            // createEditor(QtProperty*,QWidget*)
            if (Shiboken::Object::hasCppWrapper(reinterpret_cast<SbkObject *>(self))) {
                Shiboken::Errors::setPureVirtualMethodError("QtAbstractEditorFactoryBase.createEditor");
                return {};
            }
            QWidget * cppResult = cppSelf->createEditor(cppArg0, cppArg1);
            pyResult = Shiboken::Conversions::pointerToPython(SbkPySide6_QtWidgetsTypes[SBK_QWIDGET_IDX], cppResult);
            // Ownership transferences (return value heuristics).
            Shiboken::Object::setParent(self, pyResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtAbstractEditorFactoryBaseFunc_createEditor_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtAbstractEditorFactoryBaseFunc_managerDestroyed(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtAbstractEditorFactoryBaseWrapper *>(reinterpret_cast< ::QtAbstractEditorFactoryBase *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTABSTRACTEDITORFACTORYBASE_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtAbstractEditorFactoryBase.managerDestroyed";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtAbstractEditorFactoryBase::managerDestroyed(QObject*)
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppPointerConversion(SbkPySide6_QtCoreTypes[SBK_QOBJECT_IDX], (pyArg)))) {
        overloadId = 0; // managerDestroyed(QObject*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtAbstractEditorFactoryBaseFunc_managerDestroyed_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QObject *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // managerDestroyed(QObject*)
            if (Shiboken::Object::hasCppWrapper(reinterpret_cast<SbkObject *>(self))) {
                Shiboken::Errors::setPureVirtualMethodError("QtAbstractEditorFactoryBase.managerDestroyed");
                return {};
            }
            static_cast<::QtAbstractEditorFactoryBaseWrapper *>(cppSelf)->managerDestroyed_protected(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtAbstractEditorFactoryBaseFunc_managerDestroyed_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}


static const char *Sbk_QtAbstractEditorFactoryBase_PropertyStrings[] = {
    nullptr // Sentinel
};

static PyMethodDef Sbk_QtAbstractEditorFactoryBase_methods[] = {
    {"breakConnection", reinterpret_cast<PyCFunction>(Sbk_QtAbstractEditorFactoryBaseFunc_breakConnection), METH_O, nullptr},
    {"createAttributeEditor", reinterpret_cast<PyCFunction>(Sbk_QtAbstractEditorFactoryBaseFunc_createAttributeEditor), METH_VARARGS, nullptr},
    {"createEditor", reinterpret_cast<PyCFunction>(Sbk_QtAbstractEditorFactoryBaseFunc_createEditor), METH_VARARGS, nullptr},
    {"managerDestroyed", reinterpret_cast<PyCFunction>(Sbk_QtAbstractEditorFactoryBaseFunc_managerDestroyed), METH_O, nullptr},

    {nullptr, nullptr, 0, nullptr} // Sentinel
};

static int Sbk_QtAbstractEditorFactoryBase_setattro(PyObject *self, PyObject *name, PyObject *value)
{
    PySide::Feature::Select(self);
    if (value && PyCallable_Check(value)) {
        auto plain_inst = reinterpret_cast< ::QtAbstractEditorFactoryBase *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTABSTRACTEDITORFACTORYBASE_IDX], reinterpret_cast<SbkObject *>(self)));
        auto inst = dynamic_cast<QtAbstractEditorFactoryBaseWrapper *>(plain_inst);
        if (inst)
            inst->resetPyMethodCache();
    }
    Shiboken::AutoDecRef pp(reinterpret_cast<PyObject *>(PySide::Property::getObject(self, name)));
    if (!pp.isNull())
        return PySide::Property::setValue(reinterpret_cast<PySideProperty *>(pp.object()), self, value);
    return PyObject_GenericSetAttr(self, name, value);
}

} // extern "C"

static int Sbk_QtAbstractEditorFactoryBase_traverse(PyObject *self, visitproc visit, void *arg)
{
    return SbkObject_TypeF()->tp_traverse(self, visit, arg);
}
static int Sbk_QtAbstractEditorFactoryBase_clear(PyObject *self)
{
    return reinterpret_cast<PyTypeObject *>(SbkObject_TypeF())->tp_clear(self);
}
// Class Definition -----------------------------------------------
extern "C" {
static PyTypeObject *_Sbk_QtAbstractEditorFactoryBase_Type = nullptr;
static PyTypeObject *Sbk_QtAbstractEditorFactoryBase_TypeF(void)
{
    return _Sbk_QtAbstractEditorFactoryBase_Type;
}

static PyType_Slot Sbk_QtAbstractEditorFactoryBase_slots[] = {
    {Py_tp_base,        nullptr}, // inserted by introduceWrapperType
    {Py_tp_dealloc,     reinterpret_cast<void *>(&SbkDeallocWrapper)},
    {Py_tp_repr,        nullptr},
    {Py_tp_hash,        nullptr},
    {Py_tp_call,        nullptr},
    {Py_tp_str,         nullptr},
    {Py_tp_getattro,    nullptr},
    {Py_tp_setattro,    reinterpret_cast<void *>(Sbk_QtAbstractEditorFactoryBase_setattro)},
    {Py_tp_traverse,    reinterpret_cast<void *>(Sbk_QtAbstractEditorFactoryBase_traverse)},
    {Py_tp_clear,       reinterpret_cast<void *>(Sbk_QtAbstractEditorFactoryBase_clear)},
    {Py_tp_richcompare, nullptr},
    {Py_tp_iter,        nullptr},
    {Py_tp_iternext,    nullptr},
    {Py_tp_methods,     reinterpret_cast<void *>(Sbk_QtAbstractEditorFactoryBase_methods)},
    {Py_tp_getset,      nullptr},
    {Py_tp_init,        reinterpret_cast<void *>(Sbk_QtAbstractEditorFactoryBase_Init)},
    {Py_tp_new,         reinterpret_cast<void *>(SbkObject_tp_new)},
    {0, nullptr}
};
static PyType_Spec Sbk_QtAbstractEditorFactoryBase_spec = {
    "1:qtpropertybrowser.QtAbstractEditorFactoryBase",
    sizeof(SbkObject),
    0,
    Py_TPFLAGS_DEFAULT|Py_TPFLAGS_BASETYPE|Py_TPFLAGS_HAVE_GC,
    Sbk_QtAbstractEditorFactoryBase_slots
};

} //extern "C"

static void *Sbk_QtAbstractEditorFactoryBase_typeDiscovery(void *cptr, PyTypeObject *instanceType)
{
    SBK_UNUSED(cptr)
    SBK_UNUSED(instanceType)
    if (instanceType == Shiboken::SbkType< ::QObject >())
        return dynamic_cast< ::QtAbstractEditorFactoryBase *>(reinterpret_cast< ::QObject *>(cptr));
    return {};
}


// Type conversion functions.

// Python to C++ pointer conversion - returns the C++ object of the Python wrapper (keeps object identity).
static void QtAbstractEditorFactoryBase_PythonToCpp_QtAbstractEditorFactoryBase_PTR(PyObject *pyIn, void *cppOut)
{
    Shiboken::Conversions::pythonToCppPointer(Sbk_QtAbstractEditorFactoryBase_TypeF(), pyIn, cppOut);
}
static PythonToCppFunc is_QtAbstractEditorFactoryBase_PythonToCpp_QtAbstractEditorFactoryBase_PTR_Convertible(PyObject *pyIn)
{
    if (pyIn == Py_None)
        return Shiboken::Conversions::nonePythonToCppNullPtr;
    if (PyObject_TypeCheck(pyIn, Sbk_QtAbstractEditorFactoryBase_TypeF()))
        return QtAbstractEditorFactoryBase_PythonToCpp_QtAbstractEditorFactoryBase_PTR;
    return {};
}

// C++ to Python pointer conversion - tries to find the Python wrapper for the C++ object (keeps object identity).
static PyObject *QtAbstractEditorFactoryBase_PTR_CppToPython_QtAbstractEditorFactoryBase(const void *cppIn)
{
    return PySide::getWrapperForQObject(reinterpret_cast<::QtAbstractEditorFactoryBase *>(const_cast<void *>(cppIn)), Sbk_QtAbstractEditorFactoryBase_TypeF());

}

// The signatures string for the functions.
// Multiple signatures have their index "n:" in front.
static const char *QtAbstractEditorFactoryBase_SignatureStrings[] = {
    "qtpropertybrowser.QtAbstractEditorFactoryBase(self,parent:PySide6.QtCore.QObject=0)",
    "qtpropertybrowser.QtAbstractEditorFactoryBase.breakConnection(self,manager:qtpropertybrowser.QtAbstractPropertyManager)",
    "qtpropertybrowser.QtAbstractEditorFactoryBase.createAttributeEditor(self,property:qtpropertybrowser.QtProperty,parent:PySide6.QtWidgets.QWidget,atttribute:qtpropertybrowser.BrowserCol)->PySide6.QtWidgets.QWidget",
    "qtpropertybrowser.QtAbstractEditorFactoryBase.createEditor(self,property:qtpropertybrowser.QtProperty,parent:PySide6.QtWidgets.QWidget)->PySide6.QtWidgets.QWidget",
    "qtpropertybrowser.QtAbstractEditorFactoryBase.managerDestroyed(self,manager:PySide6.QtCore.QObject)",
    nullptr}; // Sentinel

void init_QtAbstractEditorFactoryBase(PyObject *module)
{
    _Sbk_QtAbstractEditorFactoryBase_Type = Shiboken::ObjectType::introduceWrapperType(
        module,
        "QtAbstractEditorFactoryBase",
        "QtAbstractEditorFactoryBase*",
        &Sbk_QtAbstractEditorFactoryBase_spec,
        &Shiboken::callCppDestructor< ::QtAbstractEditorFactoryBase >,
        SbkPySide6_QtCoreTypes[SBK_QOBJECT_IDX],
        0,
        0);
    auto *pyType = Sbk_QtAbstractEditorFactoryBase_TypeF(); // references _Sbk_QtAbstractEditorFactoryBase_Type
    InitSignatureStrings(pyType, QtAbstractEditorFactoryBase_SignatureStrings);
    SbkObjectType_SetPropertyStrings(pyType, Sbk_QtAbstractEditorFactoryBase_PropertyStrings);
    SbkqtpropertybrowserTypes[SBK_QTABSTRACTEDITORFACTORYBASE_IDX] = pyType;

    // Register Converter
    SbkConverter *converter = Shiboken::Conversions::createConverter(pyType,
        QtAbstractEditorFactoryBase_PythonToCpp_QtAbstractEditorFactoryBase_PTR,
        is_QtAbstractEditorFactoryBase_PythonToCpp_QtAbstractEditorFactoryBase_PTR_Convertible,
        QtAbstractEditorFactoryBase_PTR_CppToPython_QtAbstractEditorFactoryBase);

    Shiboken::Conversions::registerConverterName(converter, "QtAbstractEditorFactoryBase");
    Shiboken::Conversions::registerConverterName(converter, "QtAbstractEditorFactoryBase*");
    Shiboken::Conversions::registerConverterName(converter, "QtAbstractEditorFactoryBase&");
    Shiboken::Conversions::registerConverterName(converter, typeid(::QtAbstractEditorFactoryBase).name());
    Shiboken::Conversions::registerConverterName(converter, typeid(::QtAbstractEditorFactoryBaseWrapper).name());


    Shiboken::ObjectType::setTypeDiscoveryFunctionV2(Sbk_QtAbstractEditorFactoryBase_TypeF(), &Sbk_QtAbstractEditorFactoryBase_typeDiscovery);

    PySide::Signal::registerSignals(pyType, &::QtAbstractEditorFactoryBase::staticMetaObject);
    QtAbstractEditorFactoryBaseWrapper::pysideInitQtMetaTypes();
    Shiboken::ObjectType::setSubTypeInitHook(pyType, &PySide::initQObjectSubType);
    PySide::initDynamicMetaObject(pyType, &::QtAbstractEditorFactoryBase::staticMetaObject, sizeof(QtAbstractEditorFactoryBaseWrapper));
}
