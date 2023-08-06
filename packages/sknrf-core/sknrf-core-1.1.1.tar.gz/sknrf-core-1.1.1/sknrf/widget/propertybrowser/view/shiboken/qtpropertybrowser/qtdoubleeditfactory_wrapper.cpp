
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
#include "qtdoubleeditfactory_wrapper.h"

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

void QtDoubleEditFactoryWrapper::pysideInitQtMetaTypes()
{
    qRegisterMetaType< ::QtDoubleEditFactory *>();
}

void QtDoubleEditFactoryWrapper::resetPyMethodCache()
{
    std::fill_n(m_PyMethodCache, sizeof(m_PyMethodCache) / sizeof(m_PyMethodCache[0]), false);
}

QtDoubleEditFactoryWrapper::QtDoubleEditFactoryWrapper(QObject * parent) : QtDoubleEditFactory(parent)
{
    resetPyMethodCache();
    // ... middle
}

void QtDoubleEditFactoryWrapper::connectPropertyManager(QtDoublePropertyManager * manager)
{
    if (m_PyMethodCache[0]) {
        return this->::QtDoubleEditFactory::connectPropertyManager(manager);
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
        return this->::QtDoubleEditFactory::connectPropertyManager(manager);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTDOUBLEPROPERTYMANAGER_IDX], manager)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

QWidget * QtDoubleEditFactoryWrapper::createAttributeEditor(QtDoublePropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute)
{
    if (m_PyMethodCache[1])
        return this->::QtDoubleEditFactory::createAttributeEditor(manager, property, parent, attribute);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return nullptr;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "createAttributeEditor";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[1] = true;
        gil.release();
        return this->::QtDoubleEditFactory::createAttributeEditor(manager, property, parent, attribute);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(NNNN)",
        Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTDOUBLEPROPERTYMANAGER_IDX], manager),
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
        Shiboken::Warnings::warnInvalidReturnValue("QtDoubleEditFactory", "createAttributeEditor", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QWidget >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return nullptr;
    }
    ::QWidget *cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QWidget * QtDoubleEditFactoryWrapper::createEditor(QtDoublePropertyManager * manager, QtProperty * property, QWidget * parent)
{
    if (m_PyMethodCache[2])
        return this->::QtDoubleEditFactory::createEditor(manager, property, parent);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return nullptr;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "createEditor";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[2] = true;
        gil.release();
        return this->::QtDoubleEditFactory::createEditor(manager, property, parent);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(NNN)",
        Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTDOUBLEPROPERTYMANAGER_IDX], manager),
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
        Shiboken::Warnings::warnInvalidReturnValue("QtDoubleEditFactory", "createEditor", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QWidget >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return nullptr;
    }
    ::QWidget *cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtDoubleEditFactoryWrapper::disconnectPropertyManager(QtDoublePropertyManager * manager)
{
    if (m_PyMethodCache[3]) {
        return this->::QtDoubleEditFactory::disconnectPropertyManager(manager);
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
        return this->::QtDoubleEditFactory::disconnectPropertyManager(manager);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTDOUBLEPROPERTYMANAGER_IDX], manager)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

QtDoubleEditFactoryWrapper::~QtDoubleEditFactoryWrapper()
{
    SbkObject *wrapper = Shiboken::BindingManager::instance().retrieveWrapper(this);
    Shiboken::Object::destroy(wrapper, this);
}

// Target ---------------------------------------------------------

extern "C" {
static int
Sbk_QtDoubleEditFactory_Init(PyObject *self, PyObject *args, PyObject *kwds)
{
    SBK_UNUSED(kwds)
    SbkObject *sbkSelf = reinterpret_cast<SbkObject *>(self);
    PySide::Feature::Select(self);
    if (Shiboken::Object::isUserType(self) && !Shiboken::ObjectType::canCallConstructor(self->ob_type, Shiboken::SbkType< ::QtDoubleEditFactory >()))
        return -1;

    ::QtDoubleEditFactoryWrapper *cptr{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtDoubleEditFactory.__init__";
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
        goto Sbk_QtDoubleEditFactory_Init_TypeError;

    if (!PyArg_ParseTuple(args, "|O:QtDoubleEditFactory", &(pyArgs[0])))
        return -1;


    // Overloaded function decisor
    // 0: QtDoubleEditFactory::QtDoubleEditFactory(QObject*)
    if (numArgs == 0) {
        overloadId = 0; // QtDoubleEditFactory(QObject*)
    } else if (numArgs >= 1
        && (pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkPySide6_QtCoreTypes[SBK_QOBJECT_IDX], (pyArgs[0])))) {
        overloadId = 0; // QtDoubleEditFactory(QObject*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtDoubleEditFactory_Init_TypeError;

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
                    goto Sbk_QtDoubleEditFactory_Init_TypeError;
                }
                if (value) {
                    pyArgs[0] = value;
                    if (!(pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkPySide6_QtCoreTypes[SBK_QOBJECT_IDX], (pyArgs[0]))))
                        goto Sbk_QtDoubleEditFactory_Init_TypeError;
                }
                PyDict_DelItem(kwds_dup, key_parent);
            }
            if (PyDict_Size(kwds_dup) > 0) {
                errInfo.reset(kwds_dup.release());
                goto Sbk_QtDoubleEditFactory_Init_TypeError;
            }
        }
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return -1;
        ::QObject *cppArg0 = 0;
        if (pythonToCpp[0])
            pythonToCpp[0](pyArgs[0], &cppArg0);

        if (!PyErr_Occurred()) {
            // QtDoubleEditFactory(QObject*)
            cptr = new ::QtDoubleEditFactoryWrapper(cppArg0);
        }
    }

    if (PyErr_Occurred() || !Shiboken::Object::setCppPointer(sbkSelf, Shiboken::SbkType< ::QtDoubleEditFactory >(), cptr)) {
        delete cptr;
        return -1;
    }
    if (!cptr) goto Sbk_QtDoubleEditFactory_Init_TypeError;

    Shiboken::Object::setValidCpp(sbkSelf, true);
    Shiboken::Object::setHasCppWrapper(sbkSelf, true);
    if (Shiboken::BindingManager::instance().hasWrapper(cptr)) {
        Shiboken::BindingManager::instance().releaseWrapper(Shiboken::BindingManager::instance().retrieveWrapper(cptr));
    }
    Shiboken::BindingManager::instance().registerWrapper(sbkSelf, cptr);


    return 1;

    Sbk_QtDoubleEditFactory_Init_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return -1;
}

static PyObject *Sbk_QtDoubleEditFactoryFunc_connectPropertyManager(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtDoubleEditFactoryWrapper *>(reinterpret_cast< ::QtDoubleEditFactory *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTDOUBLEEDITFACTORY_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtDoubleEditFactory.connectPropertyManager";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtDoubleEditFactory::connectPropertyManager(QtDoublePropertyManager*)
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTDOUBLEPROPERTYMANAGER_IDX], (pyArg)))) {
        overloadId = 0; // connectPropertyManager(QtDoublePropertyManager*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtDoubleEditFactoryFunc_connectPropertyManager_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtDoublePropertyManager *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // connectPropertyManager(QtDoublePropertyManager*)
            static_cast<::QtDoubleEditFactoryWrapper *>(cppSelf)->QtDoubleEditFactoryWrapper::connectPropertyManager_protected(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtDoubleEditFactoryFunc_connectPropertyManager_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtDoubleEditFactoryFunc_createAttributeEditor(PyObject *self, PyObject *args)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtDoubleEditFactoryWrapper *>(reinterpret_cast< ::QtDoubleEditFactory *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTDOUBLEEDITFACTORY_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtDoubleEditFactory.createAttributeEditor";
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
    // 0: QtDoubleEditFactory::createAttributeEditor(QtDoublePropertyManager*,QtProperty*,QWidget*,BrowserCol)->QWidget*
    if (numArgs == 4
        && (pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTDOUBLEPROPERTYMANAGER_IDX], (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArgs[1])))
        && (pythonToCpp[2] = Shiboken::Conversions::pythonToCppPointerConversion(SbkPySide6_QtWidgetsTypes[SBK_QWIDGET_IDX], (pyArgs[2])))
        && (pythonToCpp[3] = Shiboken::Conversions::pythonToCppConversion(PepType_SETP(reinterpret_cast<SbkEnumType *>(SbkqtpropertybrowserTypes[SBK_BROWSERCOL_IDX]))->converter, (pyArgs[3])))) {
        overloadId = 0; // createAttributeEditor(QtDoublePropertyManager*,QtProperty*,QWidget*,BrowserCol)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtDoubleEditFactoryFunc_createAttributeEditor_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return {};
        ::QtDoublePropertyManager *cppArg0;
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
            // createAttributeEditor(QtDoublePropertyManager*,QtProperty*,QWidget*,BrowserCol)
            QWidget * cppResult = static_cast<::QtDoubleEditFactoryWrapper *>(cppSelf)->QtDoubleEditFactoryWrapper::createAttributeEditor_protected(cppArg0, cppArg1, cppArg2, cppArg3);
            pyResult = Shiboken::Conversions::pointerToPython(SbkPySide6_QtWidgetsTypes[SBK_QWIDGET_IDX], cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtDoubleEditFactoryFunc_createAttributeEditor_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtDoubleEditFactoryFunc_createEditor(PyObject *self, PyObject *args)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtDoubleEditFactoryWrapper *>(reinterpret_cast< ::QtDoubleEditFactory *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTDOUBLEEDITFACTORY_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtDoubleEditFactory.createEditor";
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
    // 0: QtDoubleEditFactory::createEditor(QtDoublePropertyManager*,QtProperty*,QWidget*)->QWidget*
    if (numArgs == 3
        && (pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTDOUBLEPROPERTYMANAGER_IDX], (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArgs[1])))
        && (pythonToCpp[2] = Shiboken::Conversions::pythonToCppPointerConversion(SbkPySide6_QtWidgetsTypes[SBK_QWIDGET_IDX], (pyArgs[2])))) {
        overloadId = 0; // createEditor(QtDoublePropertyManager*,QtProperty*,QWidget*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtDoubleEditFactoryFunc_createEditor_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return {};
        ::QtDoublePropertyManager *cppArg0;
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
            // createEditor(QtDoublePropertyManager*,QtProperty*,QWidget*)
            QWidget * cppResult = static_cast<::QtDoubleEditFactoryWrapper *>(cppSelf)->QtDoubleEditFactoryWrapper::createEditor_protected(cppArg0, cppArg1, cppArg2);
            pyResult = Shiboken::Conversions::pointerToPython(SbkPySide6_QtWidgetsTypes[SBK_QWIDGET_IDX], cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtDoubleEditFactoryFunc_createEditor_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtDoubleEditFactoryFunc_disconnectPropertyManager(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtDoubleEditFactoryWrapper *>(reinterpret_cast< ::QtDoubleEditFactory *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTDOUBLEEDITFACTORY_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtDoubleEditFactory.disconnectPropertyManager";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtDoubleEditFactory::disconnectPropertyManager(QtDoublePropertyManager*)
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTDOUBLEPROPERTYMANAGER_IDX], (pyArg)))) {
        overloadId = 0; // disconnectPropertyManager(QtDoublePropertyManager*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtDoubleEditFactoryFunc_disconnectPropertyManager_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtDoublePropertyManager *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // disconnectPropertyManager(QtDoublePropertyManager*)
            static_cast<::QtDoubleEditFactoryWrapper *>(cppSelf)->QtDoubleEditFactoryWrapper::disconnectPropertyManager_protected(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtDoubleEditFactoryFunc_disconnectPropertyManager_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}


static const char *Sbk_QtDoubleEditFactory_PropertyStrings[] = {
    nullptr // Sentinel
};

static PyMethodDef Sbk_QtDoubleEditFactory_methods[] = {
    {"connectPropertyManager", reinterpret_cast<PyCFunction>(Sbk_QtDoubleEditFactoryFunc_connectPropertyManager), METH_O, nullptr},
    {"createAttributeEditor", reinterpret_cast<PyCFunction>(Sbk_QtDoubleEditFactoryFunc_createAttributeEditor), METH_VARARGS, nullptr},
    {"createEditor", reinterpret_cast<PyCFunction>(Sbk_QtDoubleEditFactoryFunc_createEditor), METH_VARARGS, nullptr},
    {"disconnectPropertyManager", reinterpret_cast<PyCFunction>(Sbk_QtDoubleEditFactoryFunc_disconnectPropertyManager), METH_O, nullptr},

    {nullptr, nullptr, 0, nullptr} // Sentinel
};

static int Sbk_QtDoubleEditFactory_setattro(PyObject *self, PyObject *name, PyObject *value)
{
    PySide::Feature::Select(self);
    if (value && PyCallable_Check(value)) {
        auto plain_inst = reinterpret_cast< ::QtDoubleEditFactory *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTDOUBLEEDITFACTORY_IDX], reinterpret_cast<SbkObject *>(self)));
        auto inst = dynamic_cast<QtDoubleEditFactoryWrapper *>(plain_inst);
        if (inst)
            inst->resetPyMethodCache();
    }
    return PyObject_GenericSetAttr(self, name, value);
}

} // extern "C"

static int Sbk_QtDoubleEditFactory_traverse(PyObject *self, visitproc visit, void *arg)
{
    return SbkObject_TypeF()->tp_traverse(self, visit, arg);
}
static int Sbk_QtDoubleEditFactory_clear(PyObject *self)
{
    return reinterpret_cast<PyTypeObject *>(SbkObject_TypeF())->tp_clear(self);
}
// Class Definition -----------------------------------------------
extern "C" {
static PyTypeObject *_Sbk_QtDoubleEditFactory_Type = nullptr;
static PyTypeObject *Sbk_QtDoubleEditFactory_TypeF(void)
{
    return _Sbk_QtDoubleEditFactory_Type;
}

static PyType_Slot Sbk_QtDoubleEditFactory_slots[] = {
    {Py_tp_base,        nullptr}, // inserted by introduceWrapperType
    {Py_tp_dealloc,     reinterpret_cast<void *>(&SbkDeallocWrapper)},
    {Py_tp_repr,        nullptr},
    {Py_tp_hash,        nullptr},
    {Py_tp_call,        nullptr},
    {Py_tp_str,         nullptr},
    {Py_tp_getattro,    nullptr},
    {Py_tp_setattro,    reinterpret_cast<void *>(Sbk_QtDoubleEditFactory_setattro)},
    {Py_tp_traverse,    reinterpret_cast<void *>(Sbk_QtDoubleEditFactory_traverse)},
    {Py_tp_clear,       reinterpret_cast<void *>(Sbk_QtDoubleEditFactory_clear)},
    {Py_tp_richcompare, nullptr},
    {Py_tp_iter,        nullptr},
    {Py_tp_iternext,    nullptr},
    {Py_tp_methods,     reinterpret_cast<void *>(Sbk_QtDoubleEditFactory_methods)},
    {Py_tp_getset,      nullptr},
    {Py_tp_init,        reinterpret_cast<void *>(Sbk_QtDoubleEditFactory_Init)},
    {Py_tp_new,         reinterpret_cast<void *>(SbkObject_tp_new)},
    {0, nullptr}
};
static PyType_Spec Sbk_QtDoubleEditFactory_spec = {
    "1:qtpropertybrowser.QtDoubleEditFactory",
    sizeof(SbkObject),
    0,
    Py_TPFLAGS_DEFAULT|Py_TPFLAGS_BASETYPE|Py_TPFLAGS_HAVE_GC,
    Sbk_QtDoubleEditFactory_slots
};

} //extern "C"


// Type conversion functions.

// Python to C++ pointer conversion - returns the C++ object of the Python wrapper (keeps object identity).
static void QtDoubleEditFactory_PythonToCpp_QtDoubleEditFactory_PTR(PyObject *pyIn, void *cppOut)
{
    Shiboken::Conversions::pythonToCppPointer(Sbk_QtDoubleEditFactory_TypeF(), pyIn, cppOut);
}
static PythonToCppFunc is_QtDoubleEditFactory_PythonToCpp_QtDoubleEditFactory_PTR_Convertible(PyObject *pyIn)
{
    if (pyIn == Py_None)
        return Shiboken::Conversions::nonePythonToCppNullPtr;
    if (PyObject_TypeCheck(pyIn, Sbk_QtDoubleEditFactory_TypeF()))
        return QtDoubleEditFactory_PythonToCpp_QtDoubleEditFactory_PTR;
    return {};
}

// C++ to Python pointer conversion - tries to find the Python wrapper for the C++ object (keeps object identity).
static PyObject *QtDoubleEditFactory_PTR_CppToPython_QtDoubleEditFactory(const void *cppIn)
{
    auto pyOut = reinterpret_cast<PyObject *>(Shiboken::BindingManager::instance().retrieveWrapper(cppIn));
    if (pyOut) {
        Py_INCREF(pyOut);
        return pyOut;
    }
    bool changedTypeName = false;
    auto tCppIn = reinterpret_cast<const ::QtDoubleEditFactory *>(cppIn);
    const char *typeName = typeid(*tCppIn).name();
    auto sbkType = Shiboken::ObjectType::typeForTypeName(typeName);
    if (sbkType && Shiboken::ObjectType::hasSpecialCastFunction(sbkType)) {
        typeName = typeNameOf(tCppIn);
        changedTypeName = true;
    }
    PyObject *result = Shiboken::Object::newObject(Sbk_QtDoubleEditFactory_TypeF(), const_cast<void *>(cppIn), false, /* exactType */ changedTypeName, typeName);
    if (changedTypeName)
        delete [] typeName;
    return result;
}

// The signatures string for the functions.
// Multiple signatures have their index "n:" in front.
static const char *QtDoubleEditFactory_SignatureStrings[] = {
    "qtpropertybrowser.QtDoubleEditFactory(self,parent:PySide6.QtCore.QObject=0)",
    "qtpropertybrowser.QtDoubleEditFactory.connectPropertyManager(self,manager:qtpropertybrowser.QtDoublePropertyManager)",
    "qtpropertybrowser.QtDoubleEditFactory.createAttributeEditor(self,manager:qtpropertybrowser.QtDoublePropertyManager,property:qtpropertybrowser.QtProperty,parent:PySide6.QtWidgets.QWidget,attribute:qtpropertybrowser.BrowserCol)->PySide6.QtWidgets.QWidget",
    "qtpropertybrowser.QtDoubleEditFactory.createEditor(self,manager:qtpropertybrowser.QtDoublePropertyManager,property:qtpropertybrowser.QtProperty,parent:PySide6.QtWidgets.QWidget)->PySide6.QtWidgets.QWidget",
    "qtpropertybrowser.QtDoubleEditFactory.disconnectPropertyManager(self,manager:qtpropertybrowser.QtDoublePropertyManager)",
    nullptr}; // Sentinel

void init_QtDoubleEditFactory(PyObject *module)
{
    _Sbk_QtDoubleEditFactory_Type = Shiboken::ObjectType::introduceWrapperType(
        module,
        "QtDoubleEditFactory",
        "QtDoubleEditFactory*",
        &Sbk_QtDoubleEditFactory_spec,
        &Shiboken::callCppDestructor< ::QtDoubleEditFactory >,
        0,
        0,
        0);
    auto *pyType = Sbk_QtDoubleEditFactory_TypeF(); // references _Sbk_QtDoubleEditFactory_Type
    InitSignatureStrings(pyType, QtDoubleEditFactory_SignatureStrings);
    SbkObjectType_SetPropertyStrings(pyType, Sbk_QtDoubleEditFactory_PropertyStrings);
    SbkqtpropertybrowserTypes[SBK_QTDOUBLEEDITFACTORY_IDX] = pyType;

    // Register Converter
    SbkConverter *converter = Shiboken::Conversions::createConverter(pyType,
        QtDoubleEditFactory_PythonToCpp_QtDoubleEditFactory_PTR,
        is_QtDoubleEditFactory_PythonToCpp_QtDoubleEditFactory_PTR_Convertible,
        QtDoubleEditFactory_PTR_CppToPython_QtDoubleEditFactory);

    Shiboken::Conversions::registerConverterName(converter, "QtDoubleEditFactory");
    Shiboken::Conversions::registerConverterName(converter, "QtDoubleEditFactory*");
    Shiboken::Conversions::registerConverterName(converter, "QtDoubleEditFactory&");
    Shiboken::Conversions::registerConverterName(converter, typeid(::QtDoubleEditFactory).name());
    Shiboken::Conversions::registerConverterName(converter, typeid(::QtDoubleEditFactoryWrapper).name());


    QtDoubleEditFactoryWrapper::pysideInitQtMetaTypes();
}
