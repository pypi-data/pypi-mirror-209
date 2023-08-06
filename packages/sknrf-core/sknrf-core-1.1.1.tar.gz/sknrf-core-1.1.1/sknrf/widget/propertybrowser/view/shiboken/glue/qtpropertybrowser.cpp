// @snippet qtabstractpropertybrowser-setFactoryForManager
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
// @snippet qtabstractpropertybrowser-setFactoryForManager
