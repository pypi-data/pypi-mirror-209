
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
#include "qtlocaleeditorfactory_wrapper.h"

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

void QtLocaleEditorFactoryWrapper::pysideInitQtMetaTypes()
{
    qRegisterMetaType< ::QtLocaleEditorFactory *>();
}

void QtLocaleEditorFactoryWrapper::resetPyMethodCache()
{
    std::fill_n(m_PyMethodCache, sizeof(m_PyMethodCache) / sizeof(m_PyMethodCache[0]), false);
}

QtLocaleEditorFactoryWrapper::QtLocaleEditorFactoryWrapper(QObject * parent) : QtLocaleEditorFactory(parent)
{
    resetPyMethodCache();
    // ... middle
}

void QtLocaleEditorFactoryWrapper::connectPropertyManager(QtLocalePropertyManager * manager)
{
    if (m_PyMethodCache[0]) {
        return this->::QtLocaleEditorFactory::connectPropertyManager(manager);
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
        return this->::QtLocaleEditorFactory::connectPropertyManager(manager);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTLOCALEPROPERTYMANAGER_IDX], manager)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

QWidget * QtLocaleEditorFactoryWrapper::createAttributeEditor(QtLocalePropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute)
{
    if (m_PyMethodCache[1])
        return this->::QtLocaleEditorFactory::createAttributeEditor(manager, property, parent, attribute);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return nullptr;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "createAttributeEditor";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[1] = true;
        gil.release();
        return this->::QtLocaleEditorFactory::createAttributeEditor(manager, property, parent, attribute);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(NNNN)",
        Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTLOCALEPROPERTYMANAGER_IDX], manager),
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
        Shiboken::Warnings::warnInvalidReturnValue("QtLocaleEditorFactory", "createAttributeEditor", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QWidget >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return nullptr;
    }
    ::QWidget *cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QWidget * QtLocaleEditorFactoryWrapper::createEditor(QtLocalePropertyManager * manager, QtProperty * property, QWidget * parent)
{
    if (m_PyMethodCache[2])
        return this->::QtLocaleEditorFactory::createEditor(manager, property, parent);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return nullptr;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "createEditor";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[2] = true;
        gil.release();
        return this->::QtLocaleEditorFactory::createEditor(manager, property, parent);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(NNN)",
        Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTLOCALEPROPERTYMANAGER_IDX], manager),
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
        Shiboken::Warnings::warnInvalidReturnValue("QtLocaleEditorFactory", "createEditor", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QWidget >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return nullptr;
    }
    ::QWidget *cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtLocaleEditorFactoryWrapper::disconnectPropertyManager(QtLocalePropertyManager * manager)
{
    if (m_PyMethodCache[3]) {
        return this->::QtLocaleEditorFactory::disconnectPropertyManager(manager);
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
        return this->::QtLocaleEditorFactory::disconnectPropertyManager(manager);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTLOCALEPROPERTYMANAGER_IDX], manager)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

QtLocaleEditorFactoryWrapper::~QtLocaleEditorFactoryWrapper()
{
    SbkObject *wrapper = Shiboken::BindingManager::instance().retrieveWrapper(this);
    Shiboken::Object::destroy(wrapper, this);
}

// Target ---------------------------------------------------------

extern "C" {
static int
Sbk_QtLocaleEditorFactory_Init(PyObject *self, PyObject *args, PyObject *kwds)
{
    SBK_UNUSED(kwds)
    SbkObject *sbkSelf = reinterpret_cast<SbkObject *>(self);
    PySide::Feature::Select(self);
    if (Shiboken::Object::isUserType(self) && !Shiboken::ObjectType::canCallConstructor(self->ob_type, Shiboken::SbkType< ::QtLocaleEditorFactory >()))
        return -1;

    ::QtLocaleEditorFactoryWrapper *cptr{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtLocaleEditorFactory.__init__";
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
        goto Sbk_QtLocaleEditorFactory_Init_TypeError;

    if (!PyArg_ParseTuple(args, "|O:QtLocaleEditorFactory", &(pyArgs[0])))
        return -1;


    // Overloaded function decisor
    // 0: QtLocaleEditorFactory::QtLocaleEditorFactory(QObject*)
    if (numArgs == 0) {
        overloadId = 0; // QtLocaleEditorFactory(QObject*)
    } else if (numArgs >= 1
        && (pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkPySide6_QtCoreTypes[SBK_QOBJECT_IDX], (pyArgs[0])))) {
        overloadId = 0; // QtLocaleEditorFactory(QObject*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtLocaleEditorFactory_Init_TypeError;

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
                    goto Sbk_QtLocaleEditorFactory_Init_TypeError;
                }
                if (value) {
                    pyArgs[0] = value;
                    if (!(pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkPySide6_QtCoreTypes[SBK_QOBJECT_IDX], (pyArgs[0]))))
                        goto Sbk_QtLocaleEditorFactory_Init_TypeError;
                }
                PyDict_DelItem(kwds_dup, key_parent);
            }
            if (PyDict_Size(kwds_dup) > 0) {
                errInfo.reset(kwds_dup.release());
                goto Sbk_QtLocaleEditorFactory_Init_TypeError;
            }
        }
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return -1;
        ::QObject *cppArg0 = 0;
        if (pythonToCpp[0])
            pythonToCpp[0](pyArgs[0], &cppArg0);

        if (!PyErr_Occurred()) {
            // QtLocaleEditorFactory(QObject*)
            cptr = new ::QtLocaleEditorFactoryWrapper(cppArg0);
        }
    }

    if (PyErr_Occurred() || !Shiboken::Object::setCppPointer(sbkSelf, Shiboken::SbkType< ::QtLocaleEditorFactory >(), cptr)) {
        delete cptr;
        return -1;
    }
    if (!cptr) goto Sbk_QtLocaleEditorFactory_Init_TypeError;

    Shiboken::Object::setValidCpp(sbkSelf, true);
    Shiboken::Object::setHasCppWrapper(sbkSelf, true);
    if (Shiboken::BindingManager::instance().hasWrapper(cptr)) {
        Shiboken::BindingManager::instance().releaseWrapper(Shiboken::BindingManager::instance().retrieveWrapper(cptr));
    }
    Shiboken::BindingManager::instance().registerWrapper(sbkSelf, cptr);


    return 1;

    Sbk_QtLocaleEditorFactory_Init_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return -1;
}

static PyObject *Sbk_QtLocaleEditorFactoryFunc_connectPropertyManager(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtLocaleEditorFactoryWrapper *>(reinterpret_cast< ::QtLocaleEditorFactory *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTLOCALEEDITORFACTORY_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtLocaleEditorFactory.connectPropertyManager";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtLocaleEditorFactory::connectPropertyManager(QtLocalePropertyManager*)
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTLOCALEPROPERTYMANAGER_IDX], (pyArg)))) {
        overloadId = 0; // connectPropertyManager(QtLocalePropertyManager*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtLocaleEditorFactoryFunc_connectPropertyManager_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtLocalePropertyManager *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // connectPropertyManager(QtLocalePropertyManager*)
            static_cast<::QtLocaleEditorFactoryWrapper *>(cppSelf)->QtLocaleEditorFactoryWrapper::connectPropertyManager_protected(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtLocaleEditorFactoryFunc_connectPropertyManager_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtLocaleEditorFactoryFunc_createAttributeEditor(PyObject *self, PyObject *args)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtLocaleEditorFactoryWrapper *>(reinterpret_cast< ::QtLocaleEditorFactory *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTLOCALEEDITORFACTORY_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtLocaleEditorFactory.createAttributeEditor";
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
    // 0: QtLocaleEditorFactory::createAttributeEditor(QtLocalePropertyManager*,QtProperty*,QWidget*,BrowserCol)->QWidget*
    if (numArgs == 4
        && (pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTLOCALEPROPERTYMANAGER_IDX], (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArgs[1])))
        && (pythonToCpp[2] = Shiboken::Conversions::pythonToCppPointerConversion(SbkPySide6_QtWidgetsTypes[SBK_QWIDGET_IDX], (pyArgs[2])))
        && (pythonToCpp[3] = Shiboken::Conversions::pythonToCppConversion(PepType_SETP(reinterpret_cast<SbkEnumType *>(SbkqtpropertybrowserTypes[SBK_BROWSERCOL_IDX]))->converter, (pyArgs[3])))) {
        overloadId = 0; // createAttributeEditor(QtLocalePropertyManager*,QtProperty*,QWidget*,BrowserCol)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtLocaleEditorFactoryFunc_createAttributeEditor_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return {};
        ::QtLocalePropertyManager *cppArg0;
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
            // createAttributeEditor(QtLocalePropertyManager*,QtProperty*,QWidget*,BrowserCol)
            QWidget * cppResult = static_cast<::QtLocaleEditorFactoryWrapper *>(cppSelf)->QtLocaleEditorFactoryWrapper::createAttributeEditor_protected(cppArg0, cppArg1, cppArg2, cppArg3);
            pyResult = Shiboken::Conversions::pointerToPython(SbkPySide6_QtWidgetsTypes[SBK_QWIDGET_IDX], cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtLocaleEditorFactoryFunc_createAttributeEditor_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtLocaleEditorFactoryFunc_createEditor(PyObject *self, PyObject *args)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtLocaleEditorFactoryWrapper *>(reinterpret_cast< ::QtLocaleEditorFactory *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTLOCALEEDITORFACTORY_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtLocaleEditorFactory.createEditor";
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
    // 0: QtLocaleEditorFactory::createEditor(QtLocalePropertyManager*,QtProperty*,QWidget*)->QWidget*
    if (numArgs == 3
        && (pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTLOCALEPROPERTYMANAGER_IDX], (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArgs[1])))
        && (pythonToCpp[2] = Shiboken::Conversions::pythonToCppPointerConversion(SbkPySide6_QtWidgetsTypes[SBK_QWIDGET_IDX], (pyArgs[2])))) {
        overloadId = 0; // createEditor(QtLocalePropertyManager*,QtProperty*,QWidget*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtLocaleEditorFactoryFunc_createEditor_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return {};
        ::QtLocalePropertyManager *cppArg0;
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
            // createEditor(QtLocalePropertyManager*,QtProperty*,QWidget*)
            QWidget * cppResult = static_cast<::QtLocaleEditorFactoryWrapper *>(cppSelf)->QtLocaleEditorFactoryWrapper::createEditor_protected(cppArg0, cppArg1, cppArg2);
            pyResult = Shiboken::Conversions::pointerToPython(SbkPySide6_QtWidgetsTypes[SBK_QWIDGET_IDX], cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtLocaleEditorFactoryFunc_createEditor_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtLocaleEditorFactoryFunc_disconnectPropertyManager(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtLocaleEditorFactoryWrapper *>(reinterpret_cast< ::QtLocaleEditorFactory *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTLOCALEEDITORFACTORY_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtLocaleEditorFactory.disconnectPropertyManager";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtLocaleEditorFactory::disconnectPropertyManager(QtLocalePropertyManager*)
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTLOCALEPROPERTYMANAGER_IDX], (pyArg)))) {
        overloadId = 0; // disconnectPropertyManager(QtLocalePropertyManager*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtLocaleEditorFactoryFunc_disconnectPropertyManager_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtLocalePropertyManager *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // disconnectPropertyManager(QtLocalePropertyManager*)
            static_cast<::QtLocaleEditorFactoryWrapper *>(cppSelf)->QtLocaleEditorFactoryWrapper::disconnectPropertyManager_protected(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtLocaleEditorFactoryFunc_disconnectPropertyManager_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}


static const char *Sbk_QtLocaleEditorFactory_PropertyStrings[] = {
    nullptr // Sentinel
};

static PyMethodDef Sbk_QtLocaleEditorFactory_methods[] = {
    {"connectPropertyManager", reinterpret_cast<PyCFunction>(Sbk_QtLocaleEditorFactoryFunc_connectPropertyManager), METH_O, nullptr},
    {"createAttributeEditor", reinterpret_cast<PyCFunction>(Sbk_QtLocaleEditorFactoryFunc_createAttributeEditor), METH_VARARGS, nullptr},
    {"createEditor", reinterpret_cast<PyCFunction>(Sbk_QtLocaleEditorFactoryFunc_createEditor), METH_VARARGS, nullptr},
    {"disconnectPropertyManager", reinterpret_cast<PyCFunction>(Sbk_QtLocaleEditorFactoryFunc_disconnectPropertyManager), METH_O, nullptr},

    {nullptr, nullptr, 0, nullptr} // Sentinel
};

static int Sbk_QtLocaleEditorFactory_setattro(PyObject *self, PyObject *name, PyObject *value)
{
    PySide::Feature::Select(self);
    if (value && PyCallable_Check(value)) {
        auto plain_inst = reinterpret_cast< ::QtLocaleEditorFactory *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTLOCALEEDITORFACTORY_IDX], reinterpret_cast<SbkObject *>(self)));
        auto inst = dynamic_cast<QtLocaleEditorFactoryWrapper *>(plain_inst);
        if (inst)
            inst->resetPyMethodCache();
    }
    return PyObject_GenericSetAttr(self, name, value);
}

} // extern "C"

static int Sbk_QtLocaleEditorFactory_traverse(PyObject *self, visitproc visit, void *arg)
{
    return SbkObject_TypeF()->tp_traverse(self, visit, arg);
}
static int Sbk_QtLocaleEditorFactory_clear(PyObject *self)
{
    return reinterpret_cast<PyTypeObject *>(SbkObject_TypeF())->tp_clear(self);
}
// Class Definition -----------------------------------------------
extern "C" {
static PyTypeObject *_Sbk_QtLocaleEditorFactory_Type = nullptr;
static PyTypeObject *Sbk_QtLocaleEditorFactory_TypeF(void)
{
    return _Sbk_QtLocaleEditorFactory_Type;
}

static PyType_Slot Sbk_QtLocaleEditorFactory_slots[] = {
    {Py_tp_base,        nullptr}, // inserted by introduceWrapperType
    {Py_tp_dealloc,     reinterpret_cast<void *>(&SbkDeallocWrapper)},
    {Py_tp_repr,        nullptr},
    {Py_tp_hash,        nullptr},
    {Py_tp_call,        nullptr},
    {Py_tp_str,         nullptr},
    {Py_tp_getattro,    nullptr},
    {Py_tp_setattro,    reinterpret_cast<void *>(Sbk_QtLocaleEditorFactory_setattro)},
    {Py_tp_traverse,    reinterpret_cast<void *>(Sbk_QtLocaleEditorFactory_traverse)},
    {Py_tp_clear,       reinterpret_cast<void *>(Sbk_QtLocaleEditorFactory_clear)},
    {Py_tp_richcompare, nullptr},
    {Py_tp_iter,        nullptr},
    {Py_tp_iternext,    nullptr},
    {Py_tp_methods,     reinterpret_cast<void *>(Sbk_QtLocaleEditorFactory_methods)},
    {Py_tp_getset,      nullptr},
    {Py_tp_init,        reinterpret_cast<void *>(Sbk_QtLocaleEditorFactory_Init)},
    {Py_tp_new,         reinterpret_cast<void *>(SbkObject_tp_new)},
    {0, nullptr}
};
static PyType_Spec Sbk_QtLocaleEditorFactory_spec = {
    "1:qtpropertybrowser.QtLocaleEditorFactory",
    sizeof(SbkObject),
    0,
    Py_TPFLAGS_DEFAULT|Py_TPFLAGS_BASETYPE|Py_TPFLAGS_HAVE_GC,
    Sbk_QtLocaleEditorFactory_slots
};

} //extern "C"


// Type conversion functions.

// Python to C++ pointer conversion - returns the C++ object of the Python wrapper (keeps object identity).
static void QtLocaleEditorFactory_PythonToCpp_QtLocaleEditorFactory_PTR(PyObject *pyIn, void *cppOut)
{
    Shiboken::Conversions::pythonToCppPointer(Sbk_QtLocaleEditorFactory_TypeF(), pyIn, cppOut);
}
static PythonToCppFunc is_QtLocaleEditorFactory_PythonToCpp_QtLocaleEditorFactory_PTR_Convertible(PyObject *pyIn)
{
    if (pyIn == Py_None)
        return Shiboken::Conversions::nonePythonToCppNullPtr;
    if (PyObject_TypeCheck(pyIn, Sbk_QtLocaleEditorFactory_TypeF()))
        return QtLocaleEditorFactory_PythonToCpp_QtLocaleEditorFactory_PTR;
    return {};
}

// C++ to Python pointer conversion - tries to find the Python wrapper for the C++ object (keeps object identity).
static PyObject *QtLocaleEditorFactory_PTR_CppToPython_QtLocaleEditorFactory(const void *cppIn)
{
    auto pyOut = reinterpret_cast<PyObject *>(Shiboken::BindingManager::instance().retrieveWrapper(cppIn));
    if (pyOut) {
        Py_INCREF(pyOut);
        return pyOut;
    }
    bool changedTypeName = false;
    auto tCppIn = reinterpret_cast<const ::QtLocaleEditorFactory *>(cppIn);
    const char *typeName = typeid(*tCppIn).name();
    auto sbkType = Shiboken::ObjectType::typeForTypeName(typeName);
    if (sbkType && Shiboken::ObjectType::hasSpecialCastFunction(sbkType)) {
        typeName = typeNameOf(tCppIn);
        changedTypeName = true;
    }
    PyObject *result = Shiboken::Object::newObject(Sbk_QtLocaleEditorFactory_TypeF(), const_cast<void *>(cppIn), false, /* exactType */ changedTypeName, typeName);
    if (changedTypeName)
        delete [] typeName;
    return result;
}

// The signatures string for the functions.
// Multiple signatures have their index "n:" in front.
static const char *QtLocaleEditorFactory_SignatureStrings[] = {
    "qtpropertybrowser.QtLocaleEditorFactory(self,parent:PySide6.QtCore.QObject=0)",
    "qtpropertybrowser.QtLocaleEditorFactory.connectPropertyManager(self,manager:qtpropertybrowser.QtLocalePropertyManager)",
    "qtpropertybrowser.QtLocaleEditorFactory.createAttributeEditor(self,manager:qtpropertybrowser.QtLocalePropertyManager,property:qtpropertybrowser.QtProperty,parent:PySide6.QtWidgets.QWidget,attribute:qtpropertybrowser.BrowserCol)->PySide6.QtWidgets.QWidget",
    "qtpropertybrowser.QtLocaleEditorFactory.createEditor(self,manager:qtpropertybrowser.QtLocalePropertyManager,property:qtpropertybrowser.QtProperty,parent:PySide6.QtWidgets.QWidget)->PySide6.QtWidgets.QWidget",
    "qtpropertybrowser.QtLocaleEditorFactory.disconnectPropertyManager(self,manager:qtpropertybrowser.QtLocalePropertyManager)",
    nullptr}; // Sentinel

void init_QtLocaleEditorFactory(PyObject *module)
{
    _Sbk_QtLocaleEditorFactory_Type = Shiboken::ObjectType::introduceWrapperType(
        module,
        "QtLocaleEditorFactory",
        "QtLocaleEditorFactory*",
        &Sbk_QtLocaleEditorFactory_spec,
        &Shiboken::callCppDestructor< ::QtLocaleEditorFactory >,
        0,
        0,
        0);
    auto *pyType = Sbk_QtLocaleEditorFactory_TypeF(); // references _Sbk_QtLocaleEditorFactory_Type
    InitSignatureStrings(pyType, QtLocaleEditorFactory_SignatureStrings);
    SbkObjectType_SetPropertyStrings(pyType, Sbk_QtLocaleEditorFactory_PropertyStrings);
    SbkqtpropertybrowserTypes[SBK_QTLOCALEEDITORFACTORY_IDX] = pyType;

    // Register Converter
    SbkConverter *converter = Shiboken::Conversions::createConverter(pyType,
        QtLocaleEditorFactory_PythonToCpp_QtLocaleEditorFactory_PTR,
        is_QtLocaleEditorFactory_PythonToCpp_QtLocaleEditorFactory_PTR_Convertible,
        QtLocaleEditorFactory_PTR_CppToPython_QtLocaleEditorFactory);

    Shiboken::Conversions::registerConverterName(converter, "QtLocaleEditorFactory");
    Shiboken::Conversions::registerConverterName(converter, "QtLocaleEditorFactory*");
    Shiboken::Conversions::registerConverterName(converter, "QtLocaleEditorFactory&");
    Shiboken::Conversions::registerConverterName(converter, typeid(::QtLocaleEditorFactory).name());
    Shiboken::Conversions::registerConverterName(converter, typeid(::QtLocaleEditorFactoryWrapper).name());


    QtLocaleEditorFactoryWrapper::pysideInitQtMetaTypes();
}
