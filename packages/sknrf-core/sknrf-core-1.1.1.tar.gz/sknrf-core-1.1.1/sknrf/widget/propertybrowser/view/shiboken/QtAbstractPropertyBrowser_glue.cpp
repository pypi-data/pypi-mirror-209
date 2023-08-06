static void setFactoryForManager_glue(QtAbstractPropertyBrowser* self, PyObject* pyManager, PyObject* pyFactory )
{
    PythonToCppFunc pythonToCpp = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTBOOLPROPERTYMANAGER_IDX]), pyManager);
    if (pythonToCpp) {
        QtBoolPropertyManager* cppManager;
        pythonToCpp( pyManager, &cppManager);
        QtAbstractEditorFactory< QtBoolPropertyManager >* cppFactory;
        if (pyFactory == Py_None)
            cppFactory = 0;
        SbkObjectType* shiboType = reinterpret_cast<SbkObjectType*>(pyFactory->ob_type);
        if (Shiboken::ObjectType::hasCast(shiboType))
            cppFactory = reinterpret_cast<QtAbstractEditorFactory< QtBoolPropertyManager >*>(Shiboken::ObjectType::cast(shiboType, reinterpret_cast<SbkObject*>(pyFactory), Shiboken::SbkType<QtAbstractEditorFactory< QtBoolPropertyManager >>()));
        cppFactory = (QtAbstractEditorFactory< QtBoolPropertyManager >*) Shiboken::Object::cppPointer(reinterpret_cast<SbkObject*>(pyFactory), Shiboken::SbkType<QtAbstractEditorFactory< QtBoolPropertyManager >>());
        self->setFactoryForManager( cppManager, cppFactory );
    }
}
