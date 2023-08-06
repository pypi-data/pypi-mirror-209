
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
#include "qtabstractpropertybrowser_wrapper.h"

#include <algorithm>
#include <cctype>
#include <cstring>
#include <iterator>
#include <set>
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

// Begin code injection
// ========================================================================
// START of custom code block [file: ./glue/qtpropertybrowser.cpp (qtabstractpropertybrowser-setFactoryForManager)]
template <int SBK_IDX, class PropertyManager>
static void setFactoryForManager_template(QtAbstractPropertyBrowser* self, PyObject* pyManager, PyObject* pyFactory )
{
    Shiboken::GilState gil;
    PythonToCppFunc pythonToCpp;
    SbkObjectType* shiboType;
    pythonToCpp = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_IDX]), pyManager);
    if (pythonToCpp) {
        PropertyManager* cppManager;
        QtAbstractEditorFactory< PropertyManager >* cppFactory;
        pythonToCpp( pyManager, &cppManager);
        if (pyFactory == Py_None)
            cppFactory = 0;
        shiboType = reinterpret_cast<SbkObjectType*>(pyFactory->ob_type);
        if (Shiboken::ObjectType::hasCast(shiboType))
            cppFactory = reinterpret_cast<QtAbstractEditorFactory< PropertyManager >*>(Shiboken::ObjectType::cast(shiboType, reinterpret_cast<SbkObject*>(pyFactory), Shiboken::SbkType<QtAbstractEditorFactory< PropertyManager >>()));
        cppFactory = (QtAbstractEditorFactory< PropertyManager >*) Shiboken::Object::cppPointer(reinterpret_cast<SbkObject*>(pyFactory), Shiboken::SbkType<QtAbstractEditorFactory< PropertyManager >>());
        gil.release();
        self->setFactoryForManager(cppManager, cppFactory);
        return;
    }
}
static void setFactoryForManager_glue(QtAbstractPropertyBrowser* self, PyObject* pyManager, PyObject* pyFactory )
{
    setFactoryForManager_template <SBK_QTGROUPPROPERTYMANAGER_IDX, QtGroupPropertyManager> (self, pyManager, pyFactory );
    setFactoryForManager_template <SBK_QTINTPROPERTYMANAGER_IDX, QtIntPropertyManager> (self, pyManager, pyFactory );
    setFactoryForManager_template <SBK_QTBOOLPROPERTYMANAGER_IDX, QtBoolPropertyManager> (self, pyManager, pyFactory );
    setFactoryForManager_template <SBK_QTDOUBLEPROPERTYMANAGER_IDX, QtDoublePropertyManager> (self, pyManager, pyFactory );
    setFactoryForManager_template <SBK_QTCOMPLEXPROPERTYMANAGER_IDX, QtComplexPropertyManager> (self, pyManager, pyFactory );
    setFactoryForManager_template <SBK_QTVECTORCOMPLEXPROPERTYMANAGER_IDX, QtVectorComplexPropertyManager> (self, pyManager, pyFactory );
    setFactoryForManager_template <SBK_QTSTRINGPROPERTYMANAGER_IDX, QtStringPropertyManager> (self, pyManager, pyFactory );
    setFactoryForManager_template <SBK_QTFILEPROPERTYMANAGER_IDX, QtFilePropertyManager> (self, pyManager, pyFactory );
    setFactoryForManager_template <SBK_QTDATEPROPERTYMANAGER_IDX, QtDatePropertyManager> (self, pyManager, pyFactory );
    setFactoryForManager_template <SBK_QTTIMEPROPERTYMANAGER_IDX, QtTimePropertyManager> (self, pyManager, pyFactory );
    setFactoryForManager_template <SBK_QTDATETIMEPROPERTYMANAGER_IDX, QtDateTimePropertyManager> (self, pyManager, pyFactory );
    setFactoryForManager_template <SBK_QTKEYSEQUENCEPROPERTYMANAGER_IDX, QtKeySequencePropertyManager> (self, pyManager, pyFactory );
    setFactoryForManager_template <SBK_QTCHARPROPERTYMANAGER_IDX, QtCharPropertyManager> (self, pyManager, pyFactory );
    setFactoryForManager_template <SBK_QTLOCALEPROPERTYMANAGER_IDX, QtLocalePropertyManager> (self, pyManager, pyFactory );
    setFactoryForManager_template <SBK_QTPOINTPROPERTYMANAGER_IDX, QtPointPropertyManager> (self, pyManager, pyFactory );
    setFactoryForManager_template <SBK_QTPOINTFPROPERTYMANAGER_IDX, QtPointFPropertyManager> (self, pyManager, pyFactory );
    setFactoryForManager_template <SBK_QTSIZEPROPERTYMANAGER_IDX, QtSizePropertyManager> (self, pyManager, pyFactory );
    setFactoryForManager_template <SBK_QTSIZEFPROPERTYMANAGER_IDX, QtSizeFPropertyManager> (self, pyManager, pyFactory );
    setFactoryForManager_template <SBK_QTRECTPROPERTYMANAGER_IDX, QtRectPropertyManager> (self, pyManager, pyFactory );
    setFactoryForManager_template <SBK_QTRECTFPROPERTYMANAGER_IDX, QtRectFPropertyManager> (self, pyManager, pyFactory );
    setFactoryForManager_template <SBK_QTENUMPROPERTYMANAGER_IDX, QtEnumPropertyManager> (self, pyManager, pyFactory );
    setFactoryForManager_template <SBK_QTFLAGPROPERTYMANAGER_IDX, QtFlagPropertyManager> (self, pyManager, pyFactory );
    setFactoryForManager_template <SBK_QTSIZEPOLICYPROPERTYMANAGER_IDX, QtSizePolicyPropertyManager> (self, pyManager, pyFactory );
    setFactoryForManager_template <SBK_QTCURSORPROPERTYMANAGER_IDX, QtCursorPropertyManager> (self, pyManager, pyFactory );
    setFactoryForManager_template <SBK_QTFONTPROPERTYMANAGER_IDX, QtFontPropertyManager> (self, pyManager, pyFactory );
    setFactoryForManager_template <SBK_QTCOLORPROPERTYMANAGER_IDX, QtColorPropertyManager> (self, pyManager, pyFactory );
    setFactoryForManager_template <SBK_QTVARIANTPROPERTYMANAGER_IDX, QtVariantPropertyManager> (self, pyManager, pyFactory );
}
// END of custom code block [file: ./glue/qtpropertybrowser.cpp (qtabstractpropertybrowser-setFactoryForManager)]
// ========================================================================
// End of code injection


// Native ---------------------------------------------------------

void QtAbstractPropertyBrowserWrapper::pysideInitQtMetaTypes()
{
}

void QtAbstractPropertyBrowserWrapper::resetPyMethodCache()
{
    std::fill_n(m_PyMethodCache, sizeof(m_PyMethodCache) / sizeof(m_PyMethodCache[0]), false);
}

QtAbstractPropertyBrowserWrapper::QtAbstractPropertyBrowserWrapper(QWidget * parent) : QtAbstractPropertyBrowser(parent)
{
    resetPyMethodCache();
    // ... middle
}

void QtAbstractPropertyBrowserWrapper::actionEvent(QActionEvent * event)
{
    if (m_PyMethodCache[0]) {
        return this->::QWidget::actionEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "actionEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[0] = true;
        gil.release();
        return this->::QWidget::actionEvent(event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtGuiTypes[SBK_QACTIONEVENT_IDX], event)
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

void QtAbstractPropertyBrowserWrapper::changeEvent(QEvent * event)
{
    if (m_PyMethodCache[1]) {
        return this->::QWidget::changeEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "changeEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[1] = true;
        gil.release();
        return this->::QWidget::changeEvent(event);
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

void QtAbstractPropertyBrowserWrapper::childEvent(QChildEvent * event)
{
    if (m_PyMethodCache[2]) {
        return this->::QObject::childEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "childEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[2] = true;
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

void QtAbstractPropertyBrowserWrapper::closeEvent(QCloseEvent * event)
{
    if (m_PyMethodCache[3]) {
        return this->::QWidget::closeEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "closeEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[3] = true;
        gil.release();
        return this->::QWidget::closeEvent(event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtGuiTypes[SBK_QCLOSEEVENT_IDX], event)
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

void QtAbstractPropertyBrowserWrapper::connectNotify(const QMetaMethod & signal)
{
    if (m_PyMethodCache[4]) {
        return this->::QObject::connectNotify(signal);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "connectNotify";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[4] = true;
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

void QtAbstractPropertyBrowserWrapper::contextMenuEvent(QContextMenuEvent * event)
{
    if (m_PyMethodCache[5]) {
        return this->::QWidget::contextMenuEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "contextMenuEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[5] = true;
        gil.release();
        return this->::QWidget::contextMenuEvent(event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtGuiTypes[SBK_QCONTEXTMENUEVENT_IDX], event)
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

QWidget * QtAbstractPropertyBrowserWrapper::createAttributeEditor(QtProperty * property, QWidget * parent, BrowserCol attribute)
{
    if (m_PyMethodCache[6])
        return this->::QtAbstractPropertyBrowser::createAttributeEditor(property, parent, attribute);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return nullptr;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "createAttributeEditor";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[6] = true;
        gil.release();
        return this->::QtAbstractPropertyBrowser::createAttributeEditor(property, parent, attribute);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(NNN)",
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
        Shiboken::Warnings::warnInvalidReturnValue("QtAbstractPropertyBrowser", "createAttributeEditor", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QWidget >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return nullptr;
    }
    ::QWidget *cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QWidget * QtAbstractPropertyBrowserWrapper::createEditor(QtProperty * property, QWidget * parent)
{
    if (m_PyMethodCache[7])
        return this->::QtAbstractPropertyBrowser::createEditor(property, parent);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return nullptr;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "createEditor";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[7] = true;
        gil.release();
        return this->::QtAbstractPropertyBrowser::createEditor(property, parent);
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
        Shiboken::Warnings::warnInvalidReturnValue("QtAbstractPropertyBrowser", "createEditor", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QWidget >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return nullptr;
    }
    ::QWidget *cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtAbstractPropertyBrowserWrapper::customEvent(QEvent * event)
{
    if (m_PyMethodCache[8]) {
        return this->::QObject::customEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "customEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[8] = true;
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

int QtAbstractPropertyBrowserWrapper::devType() const
{
    if (m_PyMethodCache[9])
        return this->::QWidget::devType();
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return 0;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "devType";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[9] = true;
        gil.release();
        return this->::QWidget::devType();
    }

    Shiboken::AutoDecRef pyArgs(PyTuple_New(0));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return 0;
    }
    // Check return type
    Shiboken::Conversions::PythonToCppConversion pythonToCpp =
        Shiboken::Conversions::pythonToCppConversion(Shiboken::Conversions::PrimitiveTypeConverter<int>(), pyResult);
    if (!pythonToCpp) {
        Shiboken::Warnings::warnInvalidReturnValue("QtAbstractPropertyBrowser", "devType", "int", Py_TYPE(pyResult)->tp_name);
        return 0;
    }
    int cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtAbstractPropertyBrowserWrapper::disconnectNotify(const QMetaMethod & signal)
{
    if (m_PyMethodCache[10]) {
        return this->::QObject::disconnectNotify(signal);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "disconnectNotify";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[10] = true;
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

void QtAbstractPropertyBrowserWrapper::dragEnterEvent(QDragEnterEvent * event)
{
    if (m_PyMethodCache[11]) {
        return this->::QWidget::dragEnterEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "dragEnterEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[11] = true;
        gil.release();
        return this->::QWidget::dragEnterEvent(event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtGuiTypes[SBK_QDRAGENTEREVENT_IDX], event)
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

void QtAbstractPropertyBrowserWrapper::dragLeaveEvent(QDragLeaveEvent * event)
{
    if (m_PyMethodCache[12]) {
        return this->::QWidget::dragLeaveEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "dragLeaveEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[12] = true;
        gil.release();
        return this->::QWidget::dragLeaveEvent(event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtGuiTypes[SBK_QDRAGLEAVEEVENT_IDX], event)
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

void QtAbstractPropertyBrowserWrapper::dragMoveEvent(QDragMoveEvent * event)
{
    if (m_PyMethodCache[13]) {
        return this->::QWidget::dragMoveEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "dragMoveEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[13] = true;
        gil.release();
        return this->::QWidget::dragMoveEvent(event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtGuiTypes[SBK_QDRAGMOVEEVENT_IDX], event)
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

void QtAbstractPropertyBrowserWrapper::dropEvent(QDropEvent * event)
{
    if (m_PyMethodCache[14]) {
        return this->::QWidget::dropEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "dropEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[14] = true;
        gil.release();
        return this->::QWidget::dropEvent(event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtGuiTypes[SBK_QDROPEVENT_IDX], event)
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

void QtAbstractPropertyBrowserWrapper::enterEvent(QEnterEvent * event)
{
    if (m_PyMethodCache[15]) {
        return this->::QWidget::enterEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "enterEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[15] = true;
        gil.release();
        return this->::QWidget::enterEvent(event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtGuiTypes[SBK_QENTEREVENT_IDX], event)
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

bool QtAbstractPropertyBrowserWrapper::event(QEvent * event)
{
    if (m_PyMethodCache[16])
        return this->::QWidget::event(event);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return false;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "event";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[16] = true;
        gil.release();
        return this->::QWidget::event(event);
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
        Shiboken::Warnings::warnInvalidReturnValue("QtAbstractPropertyBrowser", "event", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

bool QtAbstractPropertyBrowserWrapper::eventFilter(QObject * watched, QEvent * event)
{
    if (m_PyMethodCache[17])
        return this->::QObject::eventFilter(watched, event);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return false;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "eventFilter";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[17] = true;
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
        Shiboken::Warnings::warnInvalidReturnValue("QtAbstractPropertyBrowser", "eventFilter", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtAbstractPropertyBrowserWrapper::focusInEvent(QFocusEvent * event)
{
    if (m_PyMethodCache[18]) {
        return this->::QWidget::focusInEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "focusInEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[18] = true;
        gil.release();
        return this->::QWidget::focusInEvent(event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtGuiTypes[SBK_QFOCUSEVENT_IDX], event)
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

bool QtAbstractPropertyBrowserWrapper::focusNextPrevChild(bool next)
{
    if (m_PyMethodCache[19])
        return this->::QWidget::focusNextPrevChild(next);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return false;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "focusNextPrevChild";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[19] = true;
        gil.release();
        return this->::QWidget::focusNextPrevChild(next);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), &next)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return false;
    }
    // Check return type
    Shiboken::Conversions::PythonToCppConversion pythonToCpp =
        Shiboken::Conversions::pythonToCppConversion(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), pyResult);
    if (!pythonToCpp) {
        Shiboken::Warnings::warnInvalidReturnValue("QtAbstractPropertyBrowser", "focusNextPrevChild", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtAbstractPropertyBrowserWrapper::focusOutEvent(QFocusEvent * event)
{
    if (m_PyMethodCache[20]) {
        return this->::QWidget::focusOutEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "focusOutEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[20] = true;
        gil.release();
        return this->::QWidget::focusOutEvent(event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtGuiTypes[SBK_QFOCUSEVENT_IDX], event)
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

bool QtAbstractPropertyBrowserWrapper::hasHeightForWidth() const
{
    if (m_PyMethodCache[21])
        return this->::QWidget::hasHeightForWidth();
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return false;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "hasHeightForWidth";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[21] = true;
        gil.release();
        return this->::QWidget::hasHeightForWidth();
    }

    Shiboken::AutoDecRef pyArgs(PyTuple_New(0));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return false;
    }
    // Check return type
    Shiboken::Conversions::PythonToCppConversion pythonToCpp =
        Shiboken::Conversions::pythonToCppConversion(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), pyResult);
    if (!pythonToCpp) {
        Shiboken::Warnings::warnInvalidReturnValue("QtAbstractPropertyBrowser", "hasHeightForWidth", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

int QtAbstractPropertyBrowserWrapper::heightForWidth(int arg__1) const
{
    if (m_PyMethodCache[22])
        return this->::QWidget::heightForWidth(arg__1);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return 0;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "heightForWidth";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[22] = true;
        gil.release();
        return this->::QWidget::heightForWidth(arg__1);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(i)",
        arg__1
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return 0;
    }
    // Check return type
    Shiboken::Conversions::PythonToCppConversion pythonToCpp =
        Shiboken::Conversions::pythonToCppConversion(Shiboken::Conversions::PrimitiveTypeConverter<int>(), pyResult);
    if (!pythonToCpp) {
        Shiboken::Warnings::warnInvalidReturnValue("QtAbstractPropertyBrowser", "heightForWidth", "int", Py_TYPE(pyResult)->tp_name);
        return 0;
    }
    int cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtAbstractPropertyBrowserWrapper::hideEvent(QHideEvent * event)
{
    if (m_PyMethodCache[23]) {
        return this->::QWidget::hideEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "hideEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[23] = true;
        gil.release();
        return this->::QWidget::hideEvent(event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtGuiTypes[SBK_QHIDEEVENT_IDX], event)
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

void QtAbstractPropertyBrowserWrapper::initPainter(QPainter * painter) const
{
    if (m_PyMethodCache[24]) {
        return this->::QWidget::initPainter(painter);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "initPainter";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[24] = true;
        gil.release();
        return this->::QWidget::initPainter(painter);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtGuiTypes[SBK_QPAINTER_IDX], painter)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

void QtAbstractPropertyBrowserWrapper::inputMethodEvent(QInputMethodEvent * event)
{
    if (m_PyMethodCache[25]) {
        return this->::QWidget::inputMethodEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "inputMethodEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[25] = true;
        gil.release();
        return this->::QWidget::inputMethodEvent(event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtGuiTypes[SBK_QINPUTMETHODEVENT_IDX], event)
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

QVariant QtAbstractPropertyBrowserWrapper::inputMethodQuery(Qt::InputMethodQuery arg__1) const
{
    if (m_PyMethodCache[26])
        return this->::QWidget::inputMethodQuery(arg__1);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return ::QVariant();
    static PyObject *nameCache[2] = {};
    static const char *funcName = "inputMethodQuery";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[26] = true;
        gil.release();
        return this->::QWidget::inputMethodQuery(arg__1);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::copyToPython(PepType_SETP(reinterpret_cast<SbkEnumType *>(SbkPySide6_QtCoreTypes[SBK_QT_INPUTMETHODQUERY_IDX]))->converter, &arg__1)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return ::QVariant();
    }
    // Check return type
    Shiboken::Conversions::PythonToCppConversion pythonToCpp =
        Shiboken::Conversions::pythonToCppConversion(SbkPySide6_QtCoreTypeConverters[SBK_QVARIANT_IDX], pyResult);
    if (!pythonToCpp) {
        Shiboken::Warnings::warnInvalidReturnValue("QtAbstractPropertyBrowser", "inputMethodQuery", "QVariant", Py_TYPE(pyResult)->tp_name);
        return ::QVariant();
    }
    ::QVariant cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtAbstractPropertyBrowserWrapper::itemChanged(QtBrowserItem * item)
{
    if (m_PyMethodCache[27]) {
        Shiboken::GilState gil;
        Shiboken::Errors::setPureVirtualMethodError("QtAbstractPropertyBrowser.itemChanged");
        return;
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "itemChanged";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[27] = true;
        Shiboken::Errors::setPureVirtualMethodError("QtAbstractPropertyBrowser.itemChanged");
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX], item)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

void QtAbstractPropertyBrowserWrapper::itemInserted(QtBrowserItem * item, QtBrowserItem * afterItem)
{
    if (m_PyMethodCache[28]) {
        Shiboken::GilState gil;
        Shiboken::Errors::setPureVirtualMethodError("QtAbstractPropertyBrowser.itemInserted");
        return;
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "itemInserted";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[28] = true;
        Shiboken::Errors::setPureVirtualMethodError("QtAbstractPropertyBrowser.itemInserted");
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(NN)",
        Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX], item),
        Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX], afterItem)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

void QtAbstractPropertyBrowserWrapper::itemRemoved(QtBrowserItem * item)
{
    if (m_PyMethodCache[29]) {
        Shiboken::GilState gil;
        Shiboken::Errors::setPureVirtualMethodError("QtAbstractPropertyBrowser.itemRemoved");
        return;
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "itemRemoved";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[29] = true;
        Shiboken::Errors::setPureVirtualMethodError("QtAbstractPropertyBrowser.itemRemoved");
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX], item)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

void QtAbstractPropertyBrowserWrapper::keyPressEvent(QKeyEvent * event)
{
    if (m_PyMethodCache[30]) {
        return this->::QWidget::keyPressEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "keyPressEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[30] = true;
        gil.release();
        return this->::QWidget::keyPressEvent(event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtGuiTypes[SBK_QKEYEVENT_IDX], event)
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

void QtAbstractPropertyBrowserWrapper::keyReleaseEvent(QKeyEvent * event)
{
    if (m_PyMethodCache[31]) {
        return this->::QWidget::keyReleaseEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "keyReleaseEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[31] = true;
        gil.release();
        return this->::QWidget::keyReleaseEvent(event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtGuiTypes[SBK_QKEYEVENT_IDX], event)
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

void QtAbstractPropertyBrowserWrapper::leaveEvent(QEvent * event)
{
    if (m_PyMethodCache[32]) {
        return this->::QWidget::leaveEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "leaveEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[32] = true;
        gil.release();
        return this->::QWidget::leaveEvent(event);
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

int QtAbstractPropertyBrowserWrapper::metric(QPaintDevice::PaintDeviceMetric arg__1) const
{
    if (m_PyMethodCache[33])
        return this->::QWidget::metric(arg__1);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return 0;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "metric";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[33] = true;
        gil.release();
        return this->::QWidget::metric(arg__1);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::copyToPython(PepType_SETP(reinterpret_cast<SbkEnumType *>(SbkPySide6_QtGuiTypes[SBK_QPAINTDEVICE_PAINTDEVICEMETRIC_IDX]))->converter, &arg__1)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return 0;
    }
    // Check return type
    Shiboken::Conversions::PythonToCppConversion pythonToCpp =
        Shiboken::Conversions::pythonToCppConversion(Shiboken::Conversions::PrimitiveTypeConverter<int>(), pyResult);
    if (!pythonToCpp) {
        Shiboken::Warnings::warnInvalidReturnValue("QtAbstractPropertyBrowser", "metric", "int", Py_TYPE(pyResult)->tp_name);
        return 0;
    }
    int cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QSize QtAbstractPropertyBrowserWrapper::minimumSizeHint() const
{
    if (m_PyMethodCache[34])
        return this->::QWidget::minimumSizeHint();
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return {};
    static PyObject *nameCache[2] = {};
    // This method belongs to a property.
    static const char *funcName = "1:minimumSizeHint";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[34] = true;
        gil.release();
        return this->::QWidget::minimumSizeHint();
    }

    Shiboken::AutoDecRef pyArgs(PyTuple_New(0));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return {};
    }
    // Check return type
    Shiboken::Conversions::PythonToCppConversion pythonToCpp =
        Shiboken::Conversions::pythonToCppValueConversion(SbkPySide6_QtCoreTypes[SBK_QSIZE_IDX], pyResult);
    if (!pythonToCpp) {
        Shiboken::Warnings::warnInvalidReturnValue("QtAbstractPropertyBrowser", "minimumSizeHint", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QSize >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return {};
    }
    ::QSize cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtAbstractPropertyBrowserWrapper::mouseDoubleClickEvent(QMouseEvent * event)
{
    if (m_PyMethodCache[35]) {
        return this->::QWidget::mouseDoubleClickEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "mouseDoubleClickEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[35] = true;
        gil.release();
        return this->::QWidget::mouseDoubleClickEvent(event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtGuiTypes[SBK_QMOUSEEVENT_IDX], event)
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

void QtAbstractPropertyBrowserWrapper::mouseMoveEvent(QMouseEvent * event)
{
    if (m_PyMethodCache[36]) {
        return this->::QWidget::mouseMoveEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "mouseMoveEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[36] = true;
        gil.release();
        return this->::QWidget::mouseMoveEvent(event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtGuiTypes[SBK_QMOUSEEVENT_IDX], event)
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

void QtAbstractPropertyBrowserWrapper::mousePressEvent(QMouseEvent * event)
{
    if (m_PyMethodCache[37]) {
        return this->::QWidget::mousePressEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "mousePressEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[37] = true;
        gil.release();
        return this->::QWidget::mousePressEvent(event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtGuiTypes[SBK_QMOUSEEVENT_IDX], event)
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

void QtAbstractPropertyBrowserWrapper::mouseReleaseEvent(QMouseEvent * event)
{
    if (m_PyMethodCache[38]) {
        return this->::QWidget::mouseReleaseEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "mouseReleaseEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[38] = true;
        gil.release();
        return this->::QWidget::mouseReleaseEvent(event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtGuiTypes[SBK_QMOUSEEVENT_IDX], event)
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

void QtAbstractPropertyBrowserWrapper::moveEvent(QMoveEvent * event)
{
    if (m_PyMethodCache[39]) {
        return this->::QWidget::moveEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "moveEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[39] = true;
        gil.release();
        return this->::QWidget::moveEvent(event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtGuiTypes[SBK_QMOVEEVENT_IDX], event)
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

bool QtAbstractPropertyBrowserWrapper::nativeEvent(const QByteArray & eventType, void * message, qintptr * result)
{
    if (m_PyMethodCache[40]) {
        return this->::QWidget::nativeEvent(eventType, message, result);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return false;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "nativeEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[40] = true;
        gil.release();
        return this->::QWidget::nativeEvent(eventType, message, result);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(NN)",
        Shiboken::Conversions::copyToPython(SbkPySide6_QtCoreTypes[SBK_QBYTEARRAY_IDX], &eventType),
        Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<void *>(), message)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return false;
    }
    // Begin code injection
    // TEMPLATE - return_native_eventfilter_conversion - START
    bool cppResult = false;
    if (PySequence_Check(pyResult.object()) && (PySequence_Size(pyResult.object()) == 2)) {
        Shiboken::AutoDecRef pyItem(PySequence_GetItem(pyResult.object(), 0));
        Shiboken::Conversions::pythonToCppCopy(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), pyItem, &(cppResult));
        if (result) {
            Shiboken::AutoDecRef pyResultItem(PySequence_GetItem(pyResult, 1));
            Shiboken::Conversions::pythonToCppCopy(Shiboken::Conversions::PrimitiveTypeConverter<long>(), pyResultItem, (result));
        }
    }
    // TEMPLATE - return_native_eventfilter_conversion - END
    // End of code injection


    return cppResult;
}

QPaintEngine * QtAbstractPropertyBrowserWrapper::paintEngine() const
{
    if (m_PyMethodCache[41])
        return this->::QWidget::paintEngine();
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return nullptr;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "paintEngine";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[41] = true;
        gil.release();
        return this->::QWidget::paintEngine();
    }

    Shiboken::AutoDecRef pyArgs(PyTuple_New(0));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return nullptr;
    }
    // Check return type
    Shiboken::Conversions::PythonToCppConversion pythonToCpp =
        Shiboken::Conversions::pythonToCppPointerConversion(SbkPySide6_QtGuiTypes[SBK_QPAINTENGINE_IDX], pyResult);
    if (!pythonToCpp) {
        Shiboken::Warnings::warnInvalidReturnValue("QtAbstractPropertyBrowser", "paintEngine", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QPaintEngine >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return nullptr;
    }
    ::QPaintEngine *cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtAbstractPropertyBrowserWrapper::paintEvent(QPaintEvent * event)
{
    if (m_PyMethodCache[42]) {
        return this->::QWidget::paintEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "paintEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[42] = true;
        gil.release();
        return this->::QWidget::paintEvent(event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtGuiTypes[SBK_QPAINTEVENT_IDX], event)
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

QPaintDevice * QtAbstractPropertyBrowserWrapper::redirected(QPoint * offset) const
{
    if (m_PyMethodCache[43])
        return this->::QWidget::redirected(offset);
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return nullptr;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "redirected";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[43] = true;
        gil.release();
        return this->::QWidget::redirected(offset);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtCoreTypes[SBK_QPOINT_IDX], offset)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return nullptr;
    }
    // Check return type
    Shiboken::Conversions::PythonToCppConversion pythonToCpp =
        Shiboken::Conversions::pythonToCppPointerConversion(SbkPySide6_QtGuiTypes[SBK_QPAINTDEVICE_IDX], pyResult);
    if (!pythonToCpp) {
        Shiboken::Warnings::warnInvalidReturnValue("QtAbstractPropertyBrowser", "redirected", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QPaintDevice >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return nullptr;
    }
    ::QPaintDevice *cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtAbstractPropertyBrowserWrapper::resizeEvent(QResizeEvent * event)
{
    if (m_PyMethodCache[44]) {
        return this->::QWidget::resizeEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "resizeEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[44] = true;
        gil.release();
        return this->::QWidget::resizeEvent(event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtGuiTypes[SBK_QRESIZEEVENT_IDX], event)
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

void QtAbstractPropertyBrowserWrapper::setVisible(bool visible)
{
    if (m_PyMethodCache[45]) {
        return this->::QWidget::setVisible(visible);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    // This method belongs to a property.
    static const char *funcName = "2:setVisible";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[45] = true;
        gil.release();
        return this->::QWidget::setVisible(visible);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), &visible)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return;
    }
}

QPainter * QtAbstractPropertyBrowserWrapper::sharedPainter() const
{
    if (m_PyMethodCache[46])
        return this->::QWidget::sharedPainter();
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return nullptr;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "sharedPainter";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[46] = true;
        gil.release();
        return this->::QWidget::sharedPainter();
    }

    Shiboken::AutoDecRef pyArgs(PyTuple_New(0));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return nullptr;
    }
    // Check return type
    Shiboken::Conversions::PythonToCppConversion pythonToCpp =
        Shiboken::Conversions::pythonToCppPointerConversion(SbkPySide6_QtGuiTypes[SBK_QPAINTER_IDX], pyResult);
    if (!pythonToCpp) {
        Shiboken::Warnings::warnInvalidReturnValue("QtAbstractPropertyBrowser", "sharedPainter", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QPainter >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return nullptr;
    }
    ::QPainter *cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtAbstractPropertyBrowserWrapper::showEvent(QShowEvent * event)
{
    if (m_PyMethodCache[47]) {
        return this->::QWidget::showEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "showEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[47] = true;
        gil.release();
        return this->::QWidget::showEvent(event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtGuiTypes[SBK_QSHOWEVENT_IDX], event)
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

QSize QtAbstractPropertyBrowserWrapper::sizeHint() const
{
    if (m_PyMethodCache[48])
        return this->::QWidget::sizeHint();
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return {};
    static PyObject *nameCache[2] = {};
    // This method belongs to a property.
    static const char *funcName = "1:sizeHint";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[48] = true;
        gil.release();
        return this->::QWidget::sizeHint();
    }

    Shiboken::AutoDecRef pyArgs(PyTuple_New(0));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    if (pyResult.isNull()) {
        // An error happened in python code!
        PyErr_Print();
        return {};
    }
    // Check return type
    Shiboken::Conversions::PythonToCppConversion pythonToCpp =
        Shiboken::Conversions::pythonToCppValueConversion(SbkPySide6_QtCoreTypes[SBK_QSIZE_IDX], pyResult);
    if (!pythonToCpp) {
        Shiboken::Warnings::warnInvalidReturnValue("QtAbstractPropertyBrowser", "sizeHint", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QSize >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return {};
    }
    ::QSize cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtAbstractPropertyBrowserWrapper::tabletEvent(QTabletEvent * event)
{
    if (m_PyMethodCache[49]) {
        return this->::QWidget::tabletEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "tabletEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[49] = true;
        gil.release();
        return this->::QWidget::tabletEvent(event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtGuiTypes[SBK_QTABLETEVENT_IDX], event)
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

void QtAbstractPropertyBrowserWrapper::timerEvent(QTimerEvent * event)
{
    if (m_PyMethodCache[50]) {
        return this->::QObject::timerEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "timerEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[50] = true;
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

void QtAbstractPropertyBrowserWrapper::wheelEvent(QWheelEvent * event)
{
    if (m_PyMethodCache[51]) {
        return this->::QWidget::wheelEvent(event);
    }
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    static PyObject *nameCache[2] = {};
    static const char *funcName = "wheelEvent";
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, nameCache, funcName));
    if (pyOverride.isNull()) {
        m_PyMethodCache[51] = true;
        gil.release();
        return this->::QWidget::wheelEvent(event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(SbkPySide6_QtGuiTypes[SBK_QWHEELEVENT_IDX], event)
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

const QMetaObject *QtAbstractPropertyBrowserWrapper::metaObject() const
{
    if (QObject::d_ptr->metaObject)
        return QObject::d_ptr->dynamicMetaObject();
    SbkObject *pySelf = Shiboken::BindingManager::instance().retrieveWrapper(this);
    if (pySelf == nullptr)
        return QtAbstractPropertyBrowser::metaObject();
    return PySide::SignalManager::retrieveMetaObject(reinterpret_cast<PyObject *>(pySelf));
}

int QtAbstractPropertyBrowserWrapper::qt_metacall(QMetaObject::Call call, int id, void **args)
{
    int result = QtAbstractPropertyBrowser::qt_metacall(call, id, args);
    return result < 0 ? result : PySide::SignalManager::qt_metacall(this, call, id, args);
}

void *QtAbstractPropertyBrowserWrapper::qt_metacast(const char *_clname)
{
    if (!_clname)
        return {};
    SbkObject *pySelf = Shiboken::BindingManager::instance().retrieveWrapper(this);
    if (pySelf && PySide::inherits(Py_TYPE(pySelf), _clname))
        return static_cast<void *>(const_cast< QtAbstractPropertyBrowserWrapper *>(this));
    return QtAbstractPropertyBrowser::qt_metacast(_clname);
}

QtAbstractPropertyBrowserWrapper::~QtAbstractPropertyBrowserWrapper()
{
    SbkObject *wrapper = Shiboken::BindingManager::instance().retrieveWrapper(this);
    Shiboken::Object::destroy(wrapper, this);
}

// Target ---------------------------------------------------------

extern "C" {
static int
Sbk_QtAbstractPropertyBrowser_Init(PyObject *self, PyObject *args, PyObject *kwds)
{
    SBK_UNUSED(args)
    SBK_UNUSED(kwds)
    const QMetaObject *metaObject;
    SbkObject *sbkSelf = reinterpret_cast<SbkObject *>(self);
    PyTypeObject *type = self->ob_type;
    PyTypeObject *myType = SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYBROWSER_IDX];
    if (type == myType) {
        Shiboken::Errors::setInstantiateAbstractClass("QtAbstractPropertyBrowser");
        return -1;
    }

    PySide::Feature::Select(self);
    if (Shiboken::Object::isUserType(self) && !Shiboken::ObjectType::canCallConstructor(self->ob_type, Shiboken::SbkType< ::QtAbstractPropertyBrowser >()))
        return -1;

    ::QtAbstractPropertyBrowserWrapper *cptr{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtAbstractPropertyBrowser.__init__";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp[1];
    SBK_UNUSED(pythonToCpp)
    const Py_ssize_t numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {nullptr};

    // invalid argument lengths

    if (!PyArg_ParseTuple(args, "|O:QtAbstractPropertyBrowser", &(pyArgs[0])))
        return -1;


    // Overloaded function decisor
    // 0: QtAbstractPropertyBrowser::QtAbstractPropertyBrowser(QWidget*)
    if (numArgs == 0) {
        overloadId = 0; // QtAbstractPropertyBrowser(QWidget*)
    } else if (numArgs >= 1
        && (pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkPySide6_QtWidgetsTypes[SBK_QWIDGET_IDX], (pyArgs[0])))) {
        overloadId = 0; // QtAbstractPropertyBrowser(QWidget*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtAbstractPropertyBrowser_Init_TypeError;

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
                    goto Sbk_QtAbstractPropertyBrowser_Init_TypeError;
                }
                if (value) {
                    pyArgs[0] = value;
                    if (!(pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkPySide6_QtWidgetsTypes[SBK_QWIDGET_IDX], (pyArgs[0]))))
                        goto Sbk_QtAbstractPropertyBrowser_Init_TypeError;
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
        ::QWidget *cppArg0 = 0;
        if (pythonToCpp[0])
            pythonToCpp[0](pyArgs[0], &cppArg0);

        if (!PyErr_Occurred()) {
            // QtAbstractPropertyBrowser(QWidget*)
            void *addr = PySide::nextQObjectMemoryAddr();
            if (addr) {
                cptr = new (addr) ::QtAbstractPropertyBrowserWrapper(cppArg0);
                PySide::setNextQObjectMemoryAddr(nullptr);
            } else {
                cptr = new ::QtAbstractPropertyBrowserWrapper(cppArg0);
            }

            // Ownership transferences (constructor heuristics).
            Shiboken::Object::setParent(pyArgs[0], self);
        }
    }

    if (PyErr_Occurred() || !Shiboken::Object::setCppPointer(sbkSelf, Shiboken::SbkType< ::QtAbstractPropertyBrowser >(), cptr)) {
        delete cptr;
        return -1;
    }
    if (!cptr) goto Sbk_QtAbstractPropertyBrowser_Init_TypeError;

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
            goto Sbk_QtAbstractPropertyBrowser_Init_TypeError;
    };


    return 1;

    Sbk_QtAbstractPropertyBrowser_Init_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return -1;
}

static PyObject *Sbk_QtAbstractPropertyBrowserFunc_addProperty(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtAbstractPropertyBrowserWrapper *>(reinterpret_cast< ::QtAbstractPropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtAbstractPropertyBrowser.addProperty";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtAbstractPropertyBrowser::addProperty(QtProperty*)->QtBrowserItem*
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArg)))) {
        overloadId = 0; // addProperty(QtProperty*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtAbstractPropertyBrowserFunc_addProperty_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // addProperty(QtProperty*)
            QtBrowserItem * cppResult = cppSelf->addProperty(cppArg0);
            pyResult = Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX], cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtAbstractPropertyBrowserFunc_addProperty_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtAbstractPropertyBrowserFunc_clear(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtAbstractPropertyBrowserWrapper *>(reinterpret_cast< ::QtAbstractPropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // clear()
            cppSelf->clear();
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;
}

static PyObject *Sbk_QtAbstractPropertyBrowserFunc_createAttributeEditor(PyObject *self, PyObject *args)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtAbstractPropertyBrowserWrapper *>(reinterpret_cast< ::QtAbstractPropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtAbstractPropertyBrowser.createAttributeEditor";
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
    // 0: QtAbstractPropertyBrowser::createAttributeEditor(QtProperty*,QWidget*,BrowserCol)->QWidget*
    if (numArgs == 3
        && (pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::pythonToCppPointerConversion(SbkPySide6_QtWidgetsTypes[SBK_QWIDGET_IDX], (pyArgs[1])))
        && (pythonToCpp[2] = Shiboken::Conversions::pythonToCppConversion(PepType_SETP(reinterpret_cast<SbkEnumType *>(SbkqtpropertybrowserTypes[SBK_BROWSERCOL_IDX]))->converter, (pyArgs[2])))) {
        overloadId = 0; // createAttributeEditor(QtProperty*,QWidget*,BrowserCol)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtAbstractPropertyBrowserFunc_createAttributeEditor_TypeError;

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
            QWidget * cppResult = static_cast<::QtAbstractPropertyBrowserWrapper *>(cppSelf)->QtAbstractPropertyBrowserWrapper::createAttributeEditor_protected(cppArg0, cppArg1, cppArg2);
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

    Sbk_QtAbstractPropertyBrowserFunc_createAttributeEditor_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtAbstractPropertyBrowserFunc_createEditor(PyObject *self, PyObject *args)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtAbstractPropertyBrowserWrapper *>(reinterpret_cast< ::QtAbstractPropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtAbstractPropertyBrowser.createEditor";
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
    // 0: QtAbstractPropertyBrowser::createEditor(QtProperty*,QWidget*)->QWidget*
    if (numArgs == 2
        && (pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::pythonToCppPointerConversion(SbkPySide6_QtWidgetsTypes[SBK_QWIDGET_IDX], (pyArgs[1])))) {
        overloadId = 0; // createEditor(QtProperty*,QWidget*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtAbstractPropertyBrowserFunc_createEditor_TypeError;

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
            QWidget * cppResult = static_cast<::QtAbstractPropertyBrowserWrapper *>(cppSelf)->QtAbstractPropertyBrowserWrapper::createEditor_protected(cppArg0, cppArg1);
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

    Sbk_QtAbstractPropertyBrowserFunc_createEditor_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtAbstractPropertyBrowserFunc_currentItem(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtAbstractPropertyBrowserWrapper *>(reinterpret_cast< ::QtAbstractPropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // currentItem()const
            QtBrowserItem * cppResult = const_cast<const ::QtAbstractPropertyBrowserWrapper *>(cppSelf)->currentItem();
            pyResult = Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX], cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtAbstractPropertyBrowserFunc_insertProperty(PyObject *self, PyObject *args)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtAbstractPropertyBrowserWrapper *>(reinterpret_cast< ::QtAbstractPropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtAbstractPropertyBrowser.insertProperty";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp[2];
    SBK_UNUSED(pythonToCpp)
    const Py_ssize_t numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {nullptr, nullptr};

    // invalid argument lengths

    if (!PyArg_UnpackTuple(args, "insertProperty", 2, 2, &(pyArgs[0]), &(pyArgs[1])))
        return {};


    // Overloaded function decisor
    // 0: QtAbstractPropertyBrowser::insertProperty(QtProperty*,QtProperty*)->QtBrowserItem*
    if (numArgs == 2
        && (pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArgs[1])))) {
        overloadId = 0; // insertProperty(QtProperty*,QtProperty*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtAbstractPropertyBrowserFunc_insertProperty_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp[0](pyArgs[0], &cppArg0);
        if (!Shiboken::Object::isValid(pyArgs[1]))
            return {};
        ::QtProperty *cppArg1;
        pythonToCpp[1](pyArgs[1], &cppArg1);

        if (!PyErr_Occurred()) {
            // insertProperty(QtProperty*,QtProperty*)
            QtBrowserItem * cppResult = cppSelf->insertProperty(cppArg0, cppArg1);
            pyResult = Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX], cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtAbstractPropertyBrowserFunc_insertProperty_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtAbstractPropertyBrowserFunc_itemChanged(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtAbstractPropertyBrowserWrapper *>(reinterpret_cast< ::QtAbstractPropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtAbstractPropertyBrowser.itemChanged";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtAbstractPropertyBrowser::itemChanged(QtBrowserItem*)
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX], (pyArg)))) {
        overloadId = 0; // itemChanged(QtBrowserItem*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtAbstractPropertyBrowserFunc_itemChanged_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtBrowserItem *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // itemChanged(QtBrowserItem*)
            if (Shiboken::Object::hasCppWrapper(reinterpret_cast<SbkObject *>(self))) {
                Shiboken::Errors::setPureVirtualMethodError("QtAbstractPropertyBrowser.itemChanged");
                return {};
            }
            static_cast<::QtAbstractPropertyBrowserWrapper *>(cppSelf)->itemChanged_protected(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtAbstractPropertyBrowserFunc_itemChanged_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtAbstractPropertyBrowserFunc_itemInserted(PyObject *self, PyObject *args)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtAbstractPropertyBrowserWrapper *>(reinterpret_cast< ::QtAbstractPropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtAbstractPropertyBrowser.itemInserted";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp[2];
    SBK_UNUSED(pythonToCpp)
    const Py_ssize_t numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {nullptr, nullptr};

    // invalid argument lengths

    if (!PyArg_UnpackTuple(args, "itemInserted", 2, 2, &(pyArgs[0]), &(pyArgs[1])))
        return {};


    // Overloaded function decisor
    // 0: QtAbstractPropertyBrowser::itemInserted(QtBrowserItem*,QtBrowserItem*)
    if (numArgs == 2
        && (pythonToCpp[0] = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX], (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX], (pyArgs[1])))) {
        overloadId = 0; // itemInserted(QtBrowserItem*,QtBrowserItem*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtAbstractPropertyBrowserFunc_itemInserted_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return {};
        ::QtBrowserItem *cppArg0;
        pythonToCpp[0](pyArgs[0], &cppArg0);
        if (!Shiboken::Object::isValid(pyArgs[1]))
            return {};
        ::QtBrowserItem *cppArg1;
        pythonToCpp[1](pyArgs[1], &cppArg1);

        if (!PyErr_Occurred()) {
            // itemInserted(QtBrowserItem*,QtBrowserItem*)
            if (Shiboken::Object::hasCppWrapper(reinterpret_cast<SbkObject *>(self))) {
                Shiboken::Errors::setPureVirtualMethodError("QtAbstractPropertyBrowser.itemInserted");
                return {};
            }
            static_cast<::QtAbstractPropertyBrowserWrapper *>(cppSelf)->itemInserted_protected(cppArg0, cppArg1);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtAbstractPropertyBrowserFunc_itemInserted_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtAbstractPropertyBrowserFunc_itemRemoved(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtAbstractPropertyBrowserWrapper *>(reinterpret_cast< ::QtAbstractPropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtAbstractPropertyBrowser.itemRemoved";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtAbstractPropertyBrowser::itemRemoved(QtBrowserItem*)
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX], (pyArg)))) {
        overloadId = 0; // itemRemoved(QtBrowserItem*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtAbstractPropertyBrowserFunc_itemRemoved_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtBrowserItem *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // itemRemoved(QtBrowserItem*)
            if (Shiboken::Object::hasCppWrapper(reinterpret_cast<SbkObject *>(self))) {
                Shiboken::Errors::setPureVirtualMethodError("QtAbstractPropertyBrowser.itemRemoved");
                return {};
            }
            static_cast<::QtAbstractPropertyBrowserWrapper *>(cppSelf)->itemRemoved_protected(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtAbstractPropertyBrowserFunc_itemRemoved_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtAbstractPropertyBrowserFunc_items(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtAbstractPropertyBrowserWrapper *>(reinterpret_cast< ::QtAbstractPropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtAbstractPropertyBrowser.items";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtAbstractPropertyBrowser::items(QtProperty*)const->QList< QtBrowserItem* >
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArg)))) {
        overloadId = 0; // items(QtProperty*)const
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtAbstractPropertyBrowserFunc_items_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // items(QtProperty*)const
            QList<QtBrowserItem* > cppResult = const_cast<const ::QtAbstractPropertyBrowserWrapper *>(cppSelf)->items(cppArg0);
            pyResult = Shiboken::Conversions::copyToPython(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_QTBROWSERITEMPTR_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtAbstractPropertyBrowserFunc_items_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtAbstractPropertyBrowserFunc_properties(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtAbstractPropertyBrowserWrapper *>(reinterpret_cast< ::QtAbstractPropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // properties()const
            QList<QtProperty* > cppResult = const_cast<const ::QtAbstractPropertyBrowserWrapper *>(cppSelf)->properties();
            pyResult = Shiboken::Conversions::copyToPython(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_QTPROPERTYPTR_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtAbstractPropertyBrowserFunc_removeProperty(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtAbstractPropertyBrowserWrapper *>(reinterpret_cast< ::QtAbstractPropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtAbstractPropertyBrowser.removeProperty";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtAbstractPropertyBrowser::removeProperty(QtProperty*)
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArg)))) {
        overloadId = 0; // removeProperty(QtProperty*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtAbstractPropertyBrowserFunc_removeProperty_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // removeProperty(QtProperty*)
            cppSelf->removeProperty(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtAbstractPropertyBrowserFunc_removeProperty_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtAbstractPropertyBrowserFunc_setCurrentItem(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtAbstractPropertyBrowserWrapper *>(reinterpret_cast< ::QtAbstractPropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtAbstractPropertyBrowser.setCurrentItem";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtAbstractPropertyBrowser::setCurrentItem(QtBrowserItem*)
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX], (pyArg)))) {
        overloadId = 0; // setCurrentItem(QtBrowserItem*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtAbstractPropertyBrowserFunc_setCurrentItem_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtBrowserItem *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // setCurrentItem(QtBrowserItem*)
            cppSelf->setCurrentItem(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtAbstractPropertyBrowserFunc_setCurrentItem_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtAbstractPropertyBrowserFunc_setFactoryForManager(PyObject *self, PyObject *args)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtAbstractPropertyBrowserWrapper *>(reinterpret_cast< ::QtAbstractPropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtAbstractPropertyBrowser.setFactoryForManager";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp[2];
    SBK_UNUSED(pythonToCpp)
    const Py_ssize_t numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {nullptr, nullptr};

    // invalid argument lengths

    if (!PyArg_UnpackTuple(args, "setFactoryForManager", 2, 2, &(pyArgs[0]), &(pyArgs[1])))
        return {};


    // Overloaded function decisor
    // 0: QtAbstractPropertyBrowser::setFactoryForManager(PyObject*,PyObject*)
    if (numArgs == 2
        && true
        && true) {
        overloadId = 0; // setFactoryForManager(PyObject*,PyObject*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtAbstractPropertyBrowserFunc_setFactoryForManager_TypeError;

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // setFactoryForManager(PyObject*,PyObject*)
            // Begin code injection
            setFactoryForManager_glue( cppSelf, pyArgs[1-1], pyArgs[2-1] );
            // End of code injection

        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtAbstractPropertyBrowserFunc_setFactoryForManager_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtAbstractPropertyBrowserFunc_topLevelItem(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtAbstractPropertyBrowserWrapper *>(reinterpret_cast< ::QtAbstractPropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtAbstractPropertyBrowser.topLevelItem";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtAbstractPropertyBrowser::topLevelItem(QtProperty*)const->QtBrowserItem*
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], (pyArg)))) {
        overloadId = 0; // topLevelItem(QtProperty*)const
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtAbstractPropertyBrowserFunc_topLevelItem_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // topLevelItem(QtProperty*)const
            QtBrowserItem * cppResult = const_cast<const ::QtAbstractPropertyBrowserWrapper *>(cppSelf)->topLevelItem(cppArg0);
            pyResult = Shiboken::Conversions::pointerToPython(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX], cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtAbstractPropertyBrowserFunc_topLevelItem_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}

static PyObject *Sbk_QtAbstractPropertyBrowserFunc_topLevelItems(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtAbstractPropertyBrowserWrapper *>(reinterpret_cast< ::QtAbstractPropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // topLevelItems()const
            QList<QtBrowserItem* > cppResult = const_cast<const ::QtAbstractPropertyBrowserWrapper *>(cppSelf)->topLevelItems();
            pyResult = Shiboken::Conversions::copyToPython(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_QTBROWSERITEMPTR_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtAbstractPropertyBrowserFunc_unsetFactoryForManager(PyObject *self, PyObject *pyArg)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    auto *cppSelf = static_cast<QtAbstractPropertyBrowserWrapper *>(reinterpret_cast< ::QtAbstractPropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    SBK_UNUSED(cppSelf)
    Shiboken::AutoDecRef errInfo{};
    static const char fullName[] = "qtpropertybrowser.QtAbstractPropertyBrowser.unsetFactoryForManager";
    SBK_UNUSED(fullName)
    int overloadId = -1;
    Shiboken::Conversions::PythonToCppConversion pythonToCpp;
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtAbstractPropertyBrowser::unsetFactoryForManager(QtAbstractPropertyManager*)
    if ((pythonToCpp = Shiboken::Conversions::pythonToCppPointerConversion(SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYMANAGER_IDX], (pyArg)))) {
        overloadId = 0; // unsetFactoryForManager(QtAbstractPropertyManager*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtAbstractPropertyBrowserFunc_unsetFactoryForManager_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtAbstractPropertyManager *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // unsetFactoryForManager(QtAbstractPropertyManager*)
            cppSelf->unsetFactoryForManager(cppArg0);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtAbstractPropertyBrowserFunc_unsetFactoryForManager_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, fullName, errInfo);
        return {};
}


static const char *Sbk_QtAbstractPropertyBrowser_PropertyStrings[] = {
    nullptr // Sentinel
};

static PyMethodDef Sbk_QtAbstractPropertyBrowser_methods[] = {
    {"addProperty", reinterpret_cast<PyCFunction>(Sbk_QtAbstractPropertyBrowserFunc_addProperty), METH_O, nullptr},
    {"clear", reinterpret_cast<PyCFunction>(Sbk_QtAbstractPropertyBrowserFunc_clear), METH_NOARGS, nullptr},
    {"createAttributeEditor", reinterpret_cast<PyCFunction>(Sbk_QtAbstractPropertyBrowserFunc_createAttributeEditor), METH_VARARGS, nullptr},
    {"createEditor", reinterpret_cast<PyCFunction>(Sbk_QtAbstractPropertyBrowserFunc_createEditor), METH_VARARGS, nullptr},
    {"currentItem", reinterpret_cast<PyCFunction>(Sbk_QtAbstractPropertyBrowserFunc_currentItem), METH_NOARGS, nullptr},
    {"insertProperty", reinterpret_cast<PyCFunction>(Sbk_QtAbstractPropertyBrowserFunc_insertProperty), METH_VARARGS, nullptr},
    {"itemChanged", reinterpret_cast<PyCFunction>(Sbk_QtAbstractPropertyBrowserFunc_itemChanged), METH_O, nullptr},
    {"itemInserted", reinterpret_cast<PyCFunction>(Sbk_QtAbstractPropertyBrowserFunc_itemInserted), METH_VARARGS, nullptr},
    {"itemRemoved", reinterpret_cast<PyCFunction>(Sbk_QtAbstractPropertyBrowserFunc_itemRemoved), METH_O, nullptr},
    {"items", reinterpret_cast<PyCFunction>(Sbk_QtAbstractPropertyBrowserFunc_items), METH_O, nullptr},
    {"properties", reinterpret_cast<PyCFunction>(Sbk_QtAbstractPropertyBrowserFunc_properties), METH_NOARGS, nullptr},
    {"removeProperty", reinterpret_cast<PyCFunction>(Sbk_QtAbstractPropertyBrowserFunc_removeProperty), METH_O, nullptr},
    {"setCurrentItem", reinterpret_cast<PyCFunction>(Sbk_QtAbstractPropertyBrowserFunc_setCurrentItem), METH_O, nullptr},
    {"setFactoryForManager", reinterpret_cast<PyCFunction>(Sbk_QtAbstractPropertyBrowserFunc_setFactoryForManager), METH_VARARGS, nullptr},
    {"topLevelItem", reinterpret_cast<PyCFunction>(Sbk_QtAbstractPropertyBrowserFunc_topLevelItem), METH_O, nullptr},
    {"topLevelItems", reinterpret_cast<PyCFunction>(Sbk_QtAbstractPropertyBrowserFunc_topLevelItems), METH_NOARGS, nullptr},
    {"unsetFactoryForManager", reinterpret_cast<PyCFunction>(Sbk_QtAbstractPropertyBrowserFunc_unsetFactoryForManager), METH_O, nullptr},

    {nullptr, nullptr, 0, nullptr} // Sentinel
};

static int Sbk_QtAbstractPropertyBrowser_setattro(PyObject *self, PyObject *name, PyObject *value)
{
    PySide::Feature::Select(self);
    if (value && PyCallable_Check(value)) {
        auto plain_inst = reinterpret_cast< ::QtAbstractPropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self)));
        auto inst = dynamic_cast<QtAbstractPropertyBrowserWrapper *>(plain_inst);
        if (inst)
            inst->resetPyMethodCache();
    }
    Shiboken::AutoDecRef pp(reinterpret_cast<PyObject *>(PySide::Property::getObject(self, name)));
    if (!pp.isNull())
        return PySide::Property::setValue(reinterpret_cast<PySideProperty *>(pp.object()), self, value);
    return PyObject_GenericSetAttr(self, name, value);
}

} // extern "C"

static int Sbk_QtAbstractPropertyBrowser_traverse(PyObject *self, visitproc visit, void *arg)
{
    return SbkObject_TypeF()->tp_traverse(self, visit, arg);
}
static int Sbk_QtAbstractPropertyBrowser_clear(PyObject *self)
{
    return reinterpret_cast<PyTypeObject *>(SbkObject_TypeF())->tp_clear(self);
}
static void * Sbk_QtAbstractPropertyBrowserSpecialCastFunction(void *obj, PyTypeObject *desiredType)
{
    auto me = reinterpret_cast< ::QtAbstractPropertyBrowser *>(obj);
    if (desiredType == SbkPySide6_QtWidgetsTypes[SBK_QWIDGET_IDX])
        return static_cast< ::QWidget *>(me);
    else if (desiredType == SbkPySide6_QtCoreTypes[SBK_QOBJECT_IDX])
        return static_cast< ::QObject *>(me);
    else if (desiredType == SbkPySide6_QtGuiTypes[SBK_QPAINTDEVICE_IDX])
        return static_cast< ::QPaintDevice *>(me);
    return me;
}


// Class Definition -----------------------------------------------
extern "C" {
static PyTypeObject *_Sbk_QtAbstractPropertyBrowser_Type = nullptr;
static PyTypeObject *Sbk_QtAbstractPropertyBrowser_TypeF(void)
{
    return _Sbk_QtAbstractPropertyBrowser_Type;
}

static PyType_Slot Sbk_QtAbstractPropertyBrowser_slots[] = {
    {Py_tp_base,        nullptr}, // inserted by introduceWrapperType
    {Py_tp_dealloc,     reinterpret_cast<void *>(&SbkDeallocWrapper)},
    {Py_tp_repr,        nullptr},
    {Py_tp_hash,        nullptr},
    {Py_tp_call,        nullptr},
    {Py_tp_str,         nullptr},
    {Py_tp_getattro,    nullptr},
    {Py_tp_setattro,    reinterpret_cast<void *>(Sbk_QtAbstractPropertyBrowser_setattro)},
    {Py_tp_traverse,    reinterpret_cast<void *>(Sbk_QtAbstractPropertyBrowser_traverse)},
    {Py_tp_clear,       reinterpret_cast<void *>(Sbk_QtAbstractPropertyBrowser_clear)},
    {Py_tp_richcompare, nullptr},
    {Py_tp_iter,        nullptr},
    {Py_tp_iternext,    nullptr},
    {Py_tp_methods,     reinterpret_cast<void *>(Sbk_QtAbstractPropertyBrowser_methods)},
    {Py_tp_getset,      nullptr},
    {Py_tp_init,        reinterpret_cast<void *>(Sbk_QtAbstractPropertyBrowser_Init)},
    {Py_tp_new,         reinterpret_cast<void *>(SbkObject_tp_new)},
    {0, nullptr}
};
static PyType_Spec Sbk_QtAbstractPropertyBrowser_spec = {
    "1:qtpropertybrowser.QtAbstractPropertyBrowser",
    sizeof(SbkObject),
    0,
    Py_TPFLAGS_DEFAULT|Py_TPFLAGS_BASETYPE|Py_TPFLAGS_HAVE_GC,
    Sbk_QtAbstractPropertyBrowser_slots
};

} //extern "C"

static void *Sbk_QtAbstractPropertyBrowser_typeDiscovery(void *cptr, PyTypeObject *instanceType)
{
    SBK_UNUSED(cptr)
    SBK_UNUSED(instanceType)
    if (instanceType == Shiboken::SbkType< ::QObject >())
        return dynamic_cast< ::QtAbstractPropertyBrowser *>(reinterpret_cast< ::QObject *>(cptr));
    if (instanceType == Shiboken::SbkType< ::QPaintDevice >())
        return dynamic_cast< ::QtAbstractPropertyBrowser *>(reinterpret_cast< ::QPaintDevice *>(cptr));
    return {};
}


// Type conversion functions.

// Python to C++ pointer conversion - returns the C++ object of the Python wrapper (keeps object identity).
static void QtAbstractPropertyBrowser_PythonToCpp_QtAbstractPropertyBrowser_PTR(PyObject *pyIn, void *cppOut)
{
    Shiboken::Conversions::pythonToCppPointer(Sbk_QtAbstractPropertyBrowser_TypeF(), pyIn, cppOut);
}
static PythonToCppFunc is_QtAbstractPropertyBrowser_PythonToCpp_QtAbstractPropertyBrowser_PTR_Convertible(PyObject *pyIn)
{
    if (pyIn == Py_None)
        return Shiboken::Conversions::nonePythonToCppNullPtr;
    if (PyObject_TypeCheck(pyIn, Sbk_QtAbstractPropertyBrowser_TypeF()))
        return QtAbstractPropertyBrowser_PythonToCpp_QtAbstractPropertyBrowser_PTR;
    return {};
}

// C++ to Python pointer conversion - tries to find the Python wrapper for the C++ object (keeps object identity).
static PyObject *QtAbstractPropertyBrowser_PTR_CppToPython_QtAbstractPropertyBrowser(const void *cppIn)
{
    return PySide::getWrapperForQObject(reinterpret_cast<::QtAbstractPropertyBrowser *>(const_cast<void *>(cppIn)), Sbk_QtAbstractPropertyBrowser_TypeF());

}

// The signatures string for the functions.
// Multiple signatures have their index "n:" in front.
static const char *QtAbstractPropertyBrowser_SignatureStrings[] = {
    "qtpropertybrowser.QtAbstractPropertyBrowser(self,parent:PySide6.QtWidgets.QWidget=0)",
    "qtpropertybrowser.QtAbstractPropertyBrowser.addProperty(self,property:qtpropertybrowser.QtProperty)->qtpropertybrowser.QtBrowserItem",
    "qtpropertybrowser.QtAbstractPropertyBrowser.clear(self)",
    "qtpropertybrowser.QtAbstractPropertyBrowser.createAttributeEditor(self,property:qtpropertybrowser.QtProperty,parent:PySide6.QtWidgets.QWidget,attribute:qtpropertybrowser.BrowserCol)->PySide6.QtWidgets.QWidget",
    "qtpropertybrowser.QtAbstractPropertyBrowser.createEditor(self,property:qtpropertybrowser.QtProperty,parent:PySide6.QtWidgets.QWidget)->PySide6.QtWidgets.QWidget",
    "qtpropertybrowser.QtAbstractPropertyBrowser.currentItem(self)->qtpropertybrowser.QtBrowserItem",
    "qtpropertybrowser.QtAbstractPropertyBrowser.insertProperty(self,property:qtpropertybrowser.QtProperty,afterProperty:qtpropertybrowser.QtProperty)->qtpropertybrowser.QtBrowserItem",
    "qtpropertybrowser.QtAbstractPropertyBrowser.itemChanged(self,item:qtpropertybrowser.QtBrowserItem)",
    "qtpropertybrowser.QtAbstractPropertyBrowser.itemInserted(self,item:qtpropertybrowser.QtBrowserItem,afterItem:qtpropertybrowser.QtBrowserItem)",
    "qtpropertybrowser.QtAbstractPropertyBrowser.itemRemoved(self,item:qtpropertybrowser.QtBrowserItem)",
    "qtpropertybrowser.QtAbstractPropertyBrowser.items(self,property:qtpropertybrowser.QtProperty)->QList[qtpropertybrowser.QtBrowserItem]",
    "qtpropertybrowser.QtAbstractPropertyBrowser.properties(self)->QList[qtpropertybrowser.QtProperty]",
    "qtpropertybrowser.QtAbstractPropertyBrowser.removeProperty(self,property:qtpropertybrowser.QtProperty)",
    "qtpropertybrowser.QtAbstractPropertyBrowser.setCurrentItem(self,arg__1:qtpropertybrowser.QtBrowserItem)",
    "qtpropertybrowser.QtAbstractPropertyBrowser.setFactoryForManager(self,arg__1:PyObject,arg__2:PyObject)",
    "qtpropertybrowser.QtAbstractPropertyBrowser.topLevelItem(self,property:qtpropertybrowser.QtProperty)->qtpropertybrowser.QtBrowserItem",
    "qtpropertybrowser.QtAbstractPropertyBrowser.topLevelItems(self)->QList[qtpropertybrowser.QtBrowserItem]",
    "qtpropertybrowser.QtAbstractPropertyBrowser.unsetFactoryForManager(self,manager:qtpropertybrowser.QtAbstractPropertyManager)",
    nullptr}; // Sentinel

void init_QtAbstractPropertyBrowser(PyObject *module)
{
    _Sbk_QtAbstractPropertyBrowser_Type = Shiboken::ObjectType::introduceWrapperType(
        module,
        "QtAbstractPropertyBrowser",
        "QtAbstractPropertyBrowser*",
        &Sbk_QtAbstractPropertyBrowser_spec,
        &Shiboken::callCppDestructor< ::QtAbstractPropertyBrowser >,
        SbkPySide6_QtWidgetsTypes[SBK_QWIDGET_IDX],
        0,
        Shiboken::ObjectType::WrapperFlags::DeleteInMainThread);
    auto *pyType = Sbk_QtAbstractPropertyBrowser_TypeF(); // references _Sbk_QtAbstractPropertyBrowser_Type
    InitSignatureStrings(pyType, QtAbstractPropertyBrowser_SignatureStrings);
    SbkObjectType_SetPropertyStrings(pyType, Sbk_QtAbstractPropertyBrowser_PropertyStrings);
    SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYBROWSER_IDX] = pyType;

    // Register Converter
    SbkConverter *converter = Shiboken::Conversions::createConverter(pyType,
        QtAbstractPropertyBrowser_PythonToCpp_QtAbstractPropertyBrowser_PTR,
        is_QtAbstractPropertyBrowser_PythonToCpp_QtAbstractPropertyBrowser_PTR_Convertible,
        QtAbstractPropertyBrowser_PTR_CppToPython_QtAbstractPropertyBrowser);

    Shiboken::Conversions::registerConverterName(converter, "QtAbstractPropertyBrowser");
    Shiboken::Conversions::registerConverterName(converter, "QtAbstractPropertyBrowser*");
    Shiboken::Conversions::registerConverterName(converter, "QtAbstractPropertyBrowser&");
    Shiboken::Conversions::registerConverterName(converter, typeid(::QtAbstractPropertyBrowser).name());
    Shiboken::Conversions::registerConverterName(converter, typeid(::QtAbstractPropertyBrowserWrapper).name());



    MultipleInheritanceInitFunction func = Shiboken::ObjectType::getMultipleInheritanceFunction(SbkPySide6_QtWidgetsTypes[SBK_QWIDGET_IDX]);
    Shiboken::ObjectType::setMultipleInheritanceFunction(Sbk_QtAbstractPropertyBrowser_TypeF(), func);
    Shiboken::ObjectType::setCastFunction(Sbk_QtAbstractPropertyBrowser_TypeF(), &Sbk_QtAbstractPropertyBrowserSpecialCastFunction);
    Shiboken::ObjectType::setTypeDiscoveryFunctionV2(Sbk_QtAbstractPropertyBrowser_TypeF(), &Sbk_QtAbstractPropertyBrowser_typeDiscovery);

    PySide::Signal::registerSignals(pyType, &::QtAbstractPropertyBrowser::staticMetaObject);

    QtAbstractPropertyBrowserWrapper::pysideInitQtMetaTypes();
    Shiboken::ObjectType::setSubTypeInitHook(pyType, &PySide::initQObjectSubType);
    PySide::initDynamicMetaObject(pyType, &::QtAbstractPropertyBrowser::staticMetaObject, sizeof(QtAbstractPropertyBrowserWrapper));
}

