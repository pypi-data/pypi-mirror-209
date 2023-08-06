
// default includes
#include <shiboken.h>
#ifndef QT_NO_VERSION_TAGGING
#  define QT_NO_VERSION_TAGGING
#endif
#include <QtCore/QDebug>
#include <pysideqenum.h>
#include <pysideqflags.h>
#include <pysideqmetatype.h>
#include <pysideutils.h>
#include <feature_select.h>
QT_WARNING_DISABLE_DEPRECATED


// module include
#include "qtpropertybrowser_python.h"

// main header
#include "qttimeeditfactory_wrapper.h"

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

void QtTimeEditFactoryWrapper::pysideInitQtMetaTypes()
{
    qRegisterMetaType< ::QtTimeEditFactory *>();
}

void QtTimeEditFactoryWrapper::resetPyMethodCache()
{
    std::fill_n(m_PyMethodCache, sizeof(m_PyMethodCache) / sizeof(m_PyMethodCache[0]), false);
}

QtTimeEditFactoryWrapper::QtTimeEditFactoryWrapper(QObject * parent) : QtTimeEditFactory(parent)
{
    resetPyMethodCache();
    // ... middle
}

void QtTimeEditFactoryWrapper::connectPropertyManager(QtTimePropertyManager * manager)
{
    if (m_PyMethodCache[0]) {
        return this->::QtTimeEditFactory::connectPropertyManager(manager);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "connectPropertyManager";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[0] = true;
        gil.release();
        return this->::QtTimeEditFactory::connectPropertyManager(manager);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTTIMEPROPERTYMANAGER_IDX], manager)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

QWidget * QtTimeEditFactoryWrapper::createAttributeEditor(QtTimePropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute)
{
    if (m_PyMethodCache[1])
        return this->::QtTimeEditFactory::createAttributeEditor(manager, property, parent, attribute);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return nullptr;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "createAttributeEditor";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[1] = true;
        gil.release();
        return this->::QtTimeEditFactory::createAttributeEditor(manager, property, parent, attribute);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(NNNN)",
        Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTTIMEPROPERTYMANAGER_IDX], manager),
        Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], property),
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtWidgetsTypes[SBK_QWIDGET_IDX], parent),
        Shiboken::Conversions::copyToPython(PepType_SETP(reinterpret_cast<SbkEnumType *>(SbkqtpropertybrowserTypes[SBK_BROWSERCOL_IDX]))->converter, &attribute)
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
        Shiboken::Warnings::warnInvalidReturnValue("QtTimeEditFactory", "createAttributeEditor", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QWidget >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return nullptr;
    }
    ::QWidget *cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QWidget * QtTimeEditFactoryWrapper::createEditor(QtTimePropertyManager * manager, QtProperty * property, QWidget * parent)
{
    if (m_PyMethodCache[2])
        return this->::QtTimeEditFactory::createEditor(manager, property, parent);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return nullptr;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "createEditor";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[2] = true;
        gil.release();
        return this->::QtTimeEditFactory::createEditor(manager, property, parent);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(NNN)",
        Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTTIMEPROPERTYMANAGER_IDX], manager),
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
        Shiboken::Warnings::warnInvalidReturnValue("QtTimeEditFactory", "createEditor", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QWidget >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return nullptr;
    }
    ::QWidget *cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtTimeEditFactoryWrapper::disconnectPropertyManager(QtTimePropertyManager * manager)
{
    if (m_PyMethodCache[3]) {
        return this->::QtTimeEditFactory::disconnectPropertyManager(manager);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "disconnectPropertyManager";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[3] = true;
        gil.release();
        return this->::QtTimeEditFactory::disconnectPropertyManager(manager);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTTIMEPROPERTYMANAGER_IDX], manager)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

QtTimeEditFactoryWrapper::~QtTimeEditFactoryWrapper()
{
    SbkObject *wrapper = Shiboken::BindingManager::instance().retrieveWrapper(this);
    Shiboken::Object::destroy(wrapper, this);
}

// Target ---------------------------------------------------------

extern "C" {
static int
Sbk_QtTimeEditFactory_Init(PyObject *self, PyObject *args, PyObject *kwds)
{
    SBK_UNUSED(kwds)
    SbkObject *sbkSelf = reinterpret_cast<SbkObject *>(self);
    PySide::Feature::Select(self);
    if (Shiboken::Object::isUserType(self) && !Shiboken::ObjectType::canCallConstructor(self->ob_type, Shiboken::SbkType< ::QtTimeEditFactory >()))
        return -1;

    ::QtTimeEditFactoryWrapper *cptr{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtTimeEditFactory.__init__";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp[1];
    SBK_UNUSED(pythonToCpp)
    const Py_ssize_t numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {nullptr};

    // invalid argument lengths
    errInfo.reset(Shiboken::checkInvalidArgumentCount(numArgs, 0, 1));
    if (!errInfo.isNull())
        goto Sbk_QtTimeEditFactory_Init_TypeError;

    if (!PyArg_ParseTuple(args, "|O:QtTimeEditFactory", &(pyArgs[0])))
        return -1;


    // Overloaded function decisor
    // 0: QtTimeEditFactory::QtTimeEditFactory(QObject*)
    if (numArgs == 0) {
        overloadId = 0; // QtTimeEditFactory(QObject*)
    } else if (numArgs >= 1
        && (pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkPySide6_QtCoreTypes[SBK_QOBJECT_IDX], (pyArgs[0])))) {
        overloadId = 0; // QtTimeEditFactory(QObject*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtTimeEditFactory_Init_TypeError;

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
                    goto Sbk_QtTimeEditFactory_Init_TypeError;
                }
                if (value) {
                    pyArgs[0] = value;
                    if (!(pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkPySide6_QtCoreTypes[SBK_QOBJECT_IDX], (pyArgs[0]))))
                        goto Sbk_QtTimeEditFactory_Init_TypeError;
                }
                PyDict_DelItem(kwds_dup, key_parent);
            }
            if (PyDict_Size(kwds_dup) > 0) {
                errInfo.reset(kwds_dup.release());
                goto Sbk_QtTimeEditFactory_Init_TypeError;
            }
        }
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return -1;
        ::QObject *cppArg0 = 0;
        if (pythonToCpp[0])
            pythonToCpp[0](pyArgs[0], &cppArg0);

        if (!PyErr_Occurred()) {
            // QtTimeEditFactory(QObject*)
            cptr = new ::QtTimeEditFactoryWrapper(cppArg0);
        }
    }

    if (PyErr_Occurred() || !Shiboken::Object::setCppPointer(sbkSelf, Shiboken::SbkType< ::QtTimeEditFactory >(), cptr)) {
        delete cptr;
        return -1;
    }
    if (!cptr) goto Sbk_QtTimeEditFactory_Init_TypeError;

    Shiboken::Object::setValidCpp(sbkSelf, true);
    Shiboken::Object::setHasCppWrapper(sbkSelf, true);
    if (Shiboken::BindingManager::instance().hasWrapper(cptr)) {
        Shiboken::BindingManager::instance().releaseWrapper(Shiboken::BindingManager::instance().retrieveWrapper(cptr));
    }
    Shiboken::BindingManager::instance().registerWrapper(sbkSelf, cptr);


    return 1;

    Sbk_QtTimeEditFactory_Init_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return -1;
}

static PyObject *Sbk_QtTimeEditFactoryFunc_connectPropertyManager(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtTimeEditFactoryWrapper *>(reinterpret_cast< ::QtTimeEditFactory *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTIMEEDITFACTORY_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtTimeEditFactory.connectPropertyManager";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtTimeEditFactory::connectPropertyManager(QtTimePropertyManager*)
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTTIMEPROPERTYMANAGER_IDX], (pyArg)))) {
        overloadId = 0; // connectPropertyManager(QtTimePropertyManager*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtTimeEditFactoryFunc_connectPropertyManager_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtTimePropertyManager *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // connectPropertyManager(QtTimePropertyManager*)
            static_cast<::QtTimeEditFactoryWrapper *>(cppSelf)->QtTimeEditFactoryWrapper::connectPropertyManager_protected(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtTimeEditFactoryFunc_connectPropertyManager_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtTimeEditFactoryFunc_createAttributeEditor(PyObject *self, PyObject *args)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtTimeEditFactoryWrapper *>(reinterpret_cast< ::QtTimeEditFactory *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTIMEEDITFACTORY_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtTimeEditFactory.createAttributeEditor";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp[4];
    SBK_UNUSED(pythonToCpp)
    const Py_ssize_t numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {nullptr, nullptr, nullptr, nullptr};

    // invalid argument lengths

    if (!PyArg_UnpackTuple(args, "createAttributeEditor", 4, 4, &(pyArgs[0]), &(pyArgs[1]), &(pyArgs[2]), &(pyArgs[3])))
        return {};


    // Overloaded function decisor
    // 0: QtTimeEditFactory::createAttributeEditor(QtTimePropertyManager*,QtProperty*,QWidget*,BrowserCol)->QWidget*
    if (numArgs == 4
        && (pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTTIMEPROPERTYMANAGER_IDX], (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArgs[1])))
        && (pythonToCpp[2] = Shiboken::Conversions::pythonToCppPointerConversion(SbkPySide6_QtWidgetsTypes[SBK_QWIDGET_IDX], (pyArgs[2])))
        && (pythonToCpp[3] = Shiboken::Conversions::pythonToCppConversion(PepType_SETP(reinterpret_cast<SbkEnumType *>(SbkqtpropertybrowserTypes[SBK_BROWSERCOL_IDX]))->converter, (pyArgs[3])))) {
        overloadId = 0; // createAttributeEditor(QtTimePropertyManager*,QtProperty*,QWidget*,BrowserCol)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtTimeEditFactoryFunc_createAttributeEditor_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return {};
        ::QtTimePropertyManager *cppArg0;
        pythonToCpp[0](pyArgs[0], &cppArg0);
        if (!Shiboken::Object::isValid(pyArgs[1]))
            return {};
        ::QtProperty *cppArg1;
        pythonToCpp[1](pyArgs[1], &cppArg1);
        if (!Shiboken::Object::isValid(pyArgs[2]))
            return {};
        ::QWidget *cppArg2;
        pythonToCpp[2](pyArgs[2], &cppArg2);
        ::BrowserCol cppArg3{NONE};
        pythonToCpp[3](pyArgs[3], &cppArg3);

        if (!PyErr_Occurred()) {
            // createAttributeEditor(QtTimePropertyManager*,QtProperty*,QWidget*,BrowserCol)
            QWidget * cppResult = static_cast<::QtTimeEditFactoryWrapper *>(cppSelf)->QtTimeEditFactoryWrapper::createAttributeEditor_protected(cppArg0, cppArg1, cppArg2, cppArg3);
            pyResult = Shiboken::Conversions::pointerToPython(SbkPySide6_QtWidgetsTypes[SBK_QWIDGET_IDX], cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtTimeEditFactoryFunc_createAttributeEditor_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtTimeEditFactoryFunc_createEditor(PyObject *self, PyObject *args)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtTimeEditFactoryWrapper *>(reinterpret_cast< ::QtTimeEditFactory *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTIMEEDITFACTORY_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtTimeEditFactory.createEditor";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp[3];
    SBK_UNUSED(pythonToCpp)
    const Py_ssize_t numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {nullptr, nullptr, nullptr};

    // invalid argument lengths

    if (!PyArg_UnpackTuple(args, "createEditor", 3, 3, &(pyArgs[0]), &(pyArgs[1]), &(pyArgs[2])))
        return {};


    // Overloaded function decisor
    // 0: QtTimeEditFactory::createEditor(QtTimePropertyManager*,QtProperty*,QWidget*)->QWidget*
    if (numArgs == 3
        && (pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTTIMEPROPERTYMANAGER_IDX], (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArgs[1])))
        && (pythonToCpp[2] = Shiboken::Conversions::pythonToCppPointerConversion(SbkPySide6_QtWidgetsTypes[SBK_QWIDGET_IDX], (pyArgs[2])))) {
        overloadId = 0; // createEditor(QtTimePropertyManager*,QtProperty*,QWidget*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtTimeEditFactoryFunc_createEditor_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return {};
        ::QtTimePropertyManager *cppArg0;
        pythonToCpp[0](pyArgs[0], &cppArg0);
        if (!Shiboken::Object::isValid(pyArgs[1]))
            return {};
        ::QtProperty *cppArg1;
        pythonToCpp[1](pyArgs[1], &cppArg1);
        if (!Shiboken::Object::isValid(pyArgs[2]))
            return {};
        ::QWidget *cppArg2;
        pythonToCpp[2](pyArgs[2], &cppArg2);

        if (!PyErr_Occurred()) {
            // createEditor(QtTimePropertyManager*,QtProperty*,QWidget*)
            QWidget * cppResult = static_cast<::QtTimeEditFactoryWrapper *>(cppSelf)->QtTimeEditFactoryWrapper::createEditor_protected(cppArg0, cppArg1, cppArg2);
            pyResult = Shiboken::Conversions::pointerToPython(SbkPySide6_QtWidgetsTypes[SBK_QWIDGET_IDX], cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtTimeEditFactoryFunc_createEditor_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtTimeEditFactoryFunc_disconnectPropertyManager(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtTimeEditFactoryWrapper *>(reinterpret_cast< ::QtTimeEditFactory *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTIMEEDITFACTORY_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtTimeEditFactory.disconnectPropertyManager";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtTimeEditFactory::disconnectPropertyManager(QtTimePropertyManager*)
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTTIMEPROPERTYMANAGER_IDX], (pyArg)))) {
        overloadId = 0; // disconnectPropertyManager(QtTimePropertyManager*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtTimeEditFactoryFunc_disconnectPropertyManager_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtTimePropertyManager *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // disconnectPropertyManager(QtTimePropertyManager*)
            static_cast<::QtTimeEditFactoryWrapper *>(cppSelf)->QtTimeEditFactoryWrapper::disconnectPropertyManager_protected(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtTimeEditFactoryFunc_disconnectPropertyManager_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}


static const char *Sbk_QtTimeEditFactory_PropertyStrings[] = {
    nullptr // Sentinel
};

static PyMethodDef Sbk_QtTimeEditFactory_methods[] = {
    {"connectPropertyManager", reinterpret_cast<PyCFunction>(Sbk_QtTimeEditFactoryFunc_connectPropertyManager), METH_O, nullptr},
    {"createAttributeEditor", reinterpret_cast<PyCFunction>(Sbk_QtTimeEditFactoryFunc_createAttributeEditor), METH_VARARGS, nullptr},
    {"createEditor", reinterpret_cast<PyCFunction>(Sbk_QtTimeEditFactoryFunc_createEditor), METH_VARARGS, nullptr},
    {"disconnectPropertyManager", reinterpret_cast<PyCFunction>(Sbk_QtTimeEditFactoryFunc_disconnectPropertyManager), METH_O, nullptr},

    {nullptr, nullptr, 0, nullptr} // Sentinel
};

static int Sbk_QtTimeEditFactory_setattro(PyObject *self, PyObject *name, PyObject *value)
{
    PySide::Feature::Select(self);
    if (value && PyCallable_Check(value)) {
        auto plain_inst = reinterpret_cast< ::QtTimeEditFactory *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTIMEEDITFACTORY_IDX], reinterpret_cast<SbkObject *>(self)));
        auto inst = dynamic_cast<QtTimeEditFactoryWrapper *>(plain_inst);
        if (inst)
            inst->resetPyMethodCache();
    }
    return PyObject_GenericSetAttr(self, name, value);
}

} // extern "C"

static int Sbk_QtTimeEditFactory_traverse(PyObject *self, visitproc visit, void *arg)
{
    return SbkObject_TypeF()->tp_traverse(self, visit, arg);
}
static int Sbk_QtTimeEditFactory_clear(PyObject *self)
{
    return reinterpret_cast<PyTypeObject *>(SbkObject_TypeF())->tp_clear(self);
}
// Class Definition -----------------------------------------------
extern "C" {
static PyTypeObject *_Sbk_QtTimeEditFactory_Type = nullptr;
static PyTypeObject *Sbk_QtTimeEditFactory_TypeF(void)
{
    return _Sbk_QtTimeEditFactory_Type;
}

static PyType_Slot Sbk_QtTimeEditFactory_slots[] = {
    {Py_tp_base,        nullptr}, // inserted by introduceWrapperType
    {Py_tp_dealloc,     reinterpret_cast<void *>(&SbkDeallocWrapper)},
    {Py_tp_repr,        nullptr},
    {Py_tp_hash,        nullptr},
    {Py_tp_call,        nullptr},
    {Py_tp_str,         nullptr},
    {Py_tp_getattro,    nullptr},
    {Py_tp_setattro,    reinterpret_cast<void *>(Sbk_QtTimeEditFactory_setattro)},
    {Py_tp_traverse,    reinterpret_cast<void *>(Sbk_QtTimeEditFactory_traverse)},
    {Py_tp_clear,       reinterpret_cast<void *>(Sbk_QtTimeEditFactory_clear)},
    {Py_tp_richcompare, nullptr},
    {Py_tp_iter,        nullptr},
    {Py_tp_iternext,    nullptr},
    {Py_tp_methods,     reinterpret_cast<void *>(Sbk_QtTimeEditFactory_methods)},
    {Py_tp_getset,      nullptr},
    {Py_tp_init,        reinterpret_cast<void *>(Sbk_QtTimeEditFactory_Init)},
    {Py_tp_new,         reinterpret_cast<void *>(SbkObject_tp_new)},
    {0, nullptr}
};
static PyType_Spec Sbk_QtTimeEditFactory_spec = {
    "1:qtpropertybrowser.QtTimeEditFactory",
    sizeof(SbkObject),
    0,
    Py_TPFLAGS_DEFAULT|Py_TPFLAGS_BASETYPE|Py_TPFLAGS_HAVE_GC,
    Sbk_QtTimeEditFactory_slots
};

} //extern "C"


// Type conversion functions.

// Python to C++ pointer conversion - returns the C++ object of the Python wrapper (keeps object identity).
static void QtTimeEditFactory_PythonToCpp_QtTimeEditFactory_PTR(PyObject *pyIn, void *cppOut)
{
    Shiboken::Conversions::pythonToCppPointer(Sbk_QtTimeEditFactory_TypeF(), pyIn, cppOut);
}
static PythonToCppFunc is_QtTimeEditFactory_PythonToCpp_QtTimeEditFactory_PTR_Convertible(PyObject *pyIn)
{
    if (pyIn == Py_None)
        return Shiboken::Conversions::nonePythonToCppNullPtr;
    if (PyObject_TypeCheck(pyIn, Sbk_QtTimeEditFactory_TypeF()))
        return QtTimeEditFactory_PythonToCpp_QtTimeEditFactory_PTR;
    return {};
}

// C++ to Python pointer conversion - tries to find the Python wrapper for the C++ object (keeps object identity).
static PyObject *QtTimeEditFactory_PTR_CppToPython_QtTimeEditFactory(const void *cppIn)
{
    auto pyOut = reinterpret_cast<PyObject *>(Shiboken::BindingManager::instance().retrieveWrapper(cppIn));
    if (pyOut) {
        Py_INCREF(pyOut);
        return pyOut;
    }
    bool changedTypeName = false;
    auto tCppIn = reinterpret_cast<const ::QtTimeEditFactory *>(cppIn);
    const char *typeName = typeid(*tCppIn).name();
    auto sbkType = Shiboken::ObjectType::typeForTypeName(typeName);
    if (sbkType && Shiboken::ObjectType::hasSpecialCastFunction(sbkType)) {
        typeName = typeNameOf(tCppIn);
        changedTypeName = true;
    }
    PyObject *result = Shiboken::Object::newObject(Sbk_QtTimeEditFactory_TypeF(), const_cast<void *>(cppIn), false, /* exactType */ changedTypeName, typeName);
    if (changedTypeName)
        delete [] typeName;
    return result;
}

// The signatures string for the functions.
// Multiple signatures have their index "n:" in front.
static const char *QtTimeEditFactory_SignatureStrings[] = {
    "qtpropertybrowser.QtTimeEditFactory(self,parent:PySide6.QtCore.QObject=0)",
    "qtpropertybrowser.QtTimeEditFactory.connectPropertyManager(self,manager:qtpropertybrowser.QtTimePropertyManager)",
    "qtpropertybrowser.QtTimeEditFactory.createAttributeEditor(self,manager:qtpropertybrowser.QtTimePropertyManager,property:qtpropertybrowser.QtProperty,parent:PySide6.QtWidgets.QWidget,attribute:qtpropertybrowser.BrowserCol)->PySide6.QtWidgets.QWidget",
    "qtpropertybrowser.QtTimeEditFactory.createEditor(self,manager:qtpropertybrowser.QtTimePropertyManager,property:qtpropertybrowser.QtProperty,parent:PySide6.QtWidgets.QWidget)->PySide6.QtWidgets.QWidget",
    "qtpropertybrowser.QtTimeEditFactory.disconnectPropertyManager(self,manager:qtpropertybrowser.QtTimePropertyManager)",
    nullptr}; // Sentinel

void init_QtTimeEditFactory(PyObject *module)
{
    _Sbk_QtTimeEditFactory_Type = Shiboken::ObjectType::introduceWrapperType(
        module,
        "QtTimeEditFactory",
        "QtTimeEditFactory*",
        &Sbk_QtTimeEditFactory_spec,
        &Shiboken::callCppDestructor< ::QtTimeEditFactory >,
        0,
        0,
        0);
    auto *pyType = Sbk_QtTimeEditFactory_TypeF(); // references _Sbk_QtTimeEditFactory_Type
    InitSignatureStrings(pyType, QtTimeEditFactory_SignatureStrings);
    SbkObjectType_SetPropertyStrings(pyType, Sbk_QtTimeEditFactory_PropertyStrings);
    SbkqtpropertybrowserTypes[SBK_QTTIMEEDITFACTORY_IDX] = pyType;

    // Register Converter
    SbkConverter *converter = Shiboken::Conversions::createConverter(pyType,
        QtTimeEditFactory_PythonToCpp_QtTimeEditFactory_PTR,
        is_QtTimeEditFactory_PythonToCpp_QtTimeEditFactory_PTR_Convertible,
        QtTimeEditFactory_PTR_CppToPython_QtTimeEditFactory);

    Shiboken::Conversions::registerConverterName(converter, "QtTimeEditFactory");
    Shiboken::Conversions::registerConverterName(converter, "QtTimeEditFactory*");
    Shiboken::Conversions::registerConverterName(converter, "QtTimeEditFactory&");
    Shiboken::Conversions::registerConverterName(converter, typeid(::QtTimeEditFactory).name());
    Shiboken::Conversions::registerConverterName(converter, typeid(::QtTimeEditFactoryWrapper).name());


    QtTimeEditFactoryWrapper::pysideInitQtMetaTypes();
}
