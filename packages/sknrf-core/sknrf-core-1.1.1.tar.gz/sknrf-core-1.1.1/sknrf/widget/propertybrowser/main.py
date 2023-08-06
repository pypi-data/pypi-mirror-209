import sys
from enum import Enum, Flag, unique
import numpy as np
import torch as th

from PySide6.QtCore import Signal, Slot
from PySide6.QtCore import Qt
from PySide6.QtCore import QObject
from PySide6.QtCore import QFlag
from PySide6.QtCore import QDate
from PySide6.QtCore import QDateTime
from PySide6.QtCore import QTime
from PySide6.QtCore import QLocale
from PySide6.QtCore import QPoint
from PySide6.QtCore import QPointF
from PySide6.QtCore import QSize
from PySide6.QtCore import QSizeF
from PySide6.QtCore import QRect
from PySide6.QtCore import QRectF
from PySide6.QtCore import QFile
from PySide6.QtGui import QCursor
from PySide6.QtGui import QColor
from PySide6.QtGui import QFont
from PySide6.QtGui import QKeySequence
from PySide6.QtWidgets import QSizePolicy
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QDialog
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QGridLayout
from PySide6.QtWidgets import QScrollArea

import sknrf
from qtpropertybrowser import QtGroupPropertyManager
from qtpropertybrowser import QtIntPropertyManager
from qtpropertybrowser import QtBoolPropertyManager
from qtpropertybrowser import QtDoublePropertyManager
from qtpropertybrowser import QtComplexPropertyManager
# from qtpropertybrowser import QtQuaternionPropertyManager
from qtpropertybrowser import QtVectorComplexPropertyManager
from qtpropertybrowser import QtStringPropertyManager
from qtpropertybrowser import QtDatePropertyManager
from qtpropertybrowser import QtTimePropertyManager
from qtpropertybrowser import QtDateTimePropertyManager
from qtpropertybrowser import QtKeySequencePropertyManager
from qtpropertybrowser import QtCharPropertyManager
from qtpropertybrowser import QtPointPropertyManager
from qtpropertybrowser import QtPointFPropertyManager
from qtpropertybrowser import QtSizePropertyManager
from qtpropertybrowser import QtSizeFPropertyManager
from qtpropertybrowser import QtRectPropertyManager
from qtpropertybrowser import QtRectFPropertyManager
from qtpropertybrowser import QtEnumPropertyManager
from qtpropertybrowser import QtFlagPropertyManager
from qtpropertybrowser import QtLocalePropertyManager
from qtpropertybrowser import QtSizePolicyPropertyManager
from qtpropertybrowser import QtFontPropertyManager
from qtpropertybrowser import QtColorPropertyManager
from qtpropertybrowser import QtCursorPropertyManager
from qtpropertybrowser import QtFilePropertyManager

from qtpropertybrowser import QtGroupEditorFactory
from qtpropertybrowser import QtSpinBoxFactory
from qtpropertybrowser import QtIntEditFactory
from qtpropertybrowser import QtSliderFactory
from qtpropertybrowser import QtCheckBoxFactory
from qtpropertybrowser import QtDoubleEditFactory
from qtpropertybrowser import QtDoubleSpinBoxFactory
from qtpropertybrowser import QtComplexEditFactory
# from qtpropertybrowser import QtQuaternionEditFactory
from qtpropertybrowser import QtVectorComplexEditFactory
from qtpropertybrowser import QtLineEditFactory
from qtpropertybrowser import QtDateEditFactory
from qtpropertybrowser import QtTimeEditFactory
from qtpropertybrowser import QtDateTimeEditFactory
from qtpropertybrowser import QtKeySequenceEditorFactory
from qtpropertybrowser import QtCharEditorFactory
from qtpropertybrowser import QtPointEditorFactory
from qtpropertybrowser import QtPointFEditorFactory
from qtpropertybrowser import QtSizeEditorFactory
from qtpropertybrowser import QtSizeFEditorFactory
from qtpropertybrowser import QtRectEditorFactory
from qtpropertybrowser import QtRectFEditorFactory
from qtpropertybrowser import QtEnumEditorFactory
from qtpropertybrowser import QtFlagEditorFactory
from qtpropertybrowser import QtLocaleEditorFactory
from qtpropertybrowser import QtSizePolicyEditorFactory
from qtpropertybrowser import QtFontEditorFactory
from qtpropertybrowser import QtColorEditorFactory
from qtpropertybrowser import QtCursorEditorFactory
from qtpropertybrowser import QtFileEditorFactory

from qtpropertybrowser import PkAvg, Scale, Format, Domain, BrowserCol
from qtpropertybrowser import QtTreePropertyBrowser
from qtpropertybrowser import QtGroupBoxPropertyBrowser
from qtpropertybrowser import QtButtonPropertyBrowser


@unique
class TestEnums(Enum):
    BLACK = 0
    RED   = 1
    GREEN = 2
    BLUE  = 3


@unique
class TestFlags(Flag):
    BLACK = 0x0
    RED = 0x1
    YELLOW = 0x2
    BLUE = 0x4
    GREEN = YELLOW | BLUE
    ORANGE = RED | YELLOW
    PURPLE = RED | BLUE
    WHITE = RED | YELLOW | BLUE


INT_MIN_INIT_VECTOR = -2
INT_MAX_TEST_VECTOR = -1
INT_INIT_VECTOR = 0
INT_TEST_VECTOR = 1
INT_MIN_TEST_VECTOR = 1
INT_MAX_INIT_VECTOR = 2
DOUBLE_PRECISION = 16
DOUBLE_MIN_INIT_VECTOR = -1.500
DOUBLE_MAX_TEST_VECTOR = -0.500
DOUBLE_INIT_VECTOR = 0.000
DOUBLE_TEST_VECTOR = 0.250
DOUBLE_MIN_TEST_VECTOR = 0.500
DOUBLE_MAX_INIT_VECTOR = 1.500
COMPLEX_PRECISION = 16
COMPLEX_MIN_INIT_VECTOR = 0.50
COMPLEX_MAX_TEST_VECTOR = 1.50
COMPLEX_INIT_VECTOR = complex(1.250, 1.250)
COMPLEX_TEST_VECTOR = 1.414, 1.414
COMPLEX_MIN_TEST_VECTOR = 2.50
COMPLEX_MAX_INIT_VECTOR = 3.50
QUATERNION_PRECISION = 16
QUATERNION_MIN_INIT_VECTOR = 0.50
QUATERNION_MAX_TEST_VECTOR = 1.50
QUATERNION_INIT_VECTOR = (0.8, 0.8, 0.8, 0.8)
QUATERNION_TEST_VECTOR = (1.0, 1.0, 1.0, 1.0)
QUATERNION_MIN_TEST_VECTOR = 2.50
QUATERNION_MAX_INIT_VECTOR = 3.50
VECTOR_SIZE = 3
STR_INIT_VECTOR = ""
STR_TEST_VECTOR = "b"
DATE_INIT_VECTOR = QDate(1983, 10, 3)
DATE_TEST_VECTOR = QDate(1984, 10, 4)
TIME_INIT_VECTOR = QTime(0, 0, 0)
TIME_TEST_VECTOR = QTime(6, 3, 0)
DATETIME_INIT_VECTOR = QDateTime(QDate(DATE_INIT_VECTOR), QTime(TIME_INIT_VECTOR))
DATETIME_TEST_VECTOR = QDateTime(QDate(DATE_TEST_VECTOR), QTime(TIME_TEST_VECTOR))
KEY_INIT_VECTOR = QKeySequence("CTRL+A")
KEY_TEST_VECTOR = QKeySequence("ALT+Y")
CHAR_INIT_VECTOR = 'A'
CHAR_TEST_VECTOR = 'b'
POINT_INIT_VECTOR = QPoint(0, 0)
POINT_TEST_VECTOR = QPoint(1, 1)
POINTF_MIN_INIT_VECTOR = QPointF(DOUBLE_MIN_INIT_VECTOR, DOUBLE_MIN_INIT_VECTOR)
POINTF_INIT_VECTOR = QPointF(0.000, 0.000)
POINTF_TEST_VECTOR = QPointF(0.250, 0.250)
POINTF_MAX_INIT_VECTOR = QPointF(DOUBLE_MAX_INIT_VECTOR, DOUBLE_MAX_INIT_VECTOR)
SIZE_INIT_VECTOR = QSize(0, 0)
SIZE_TEST_VECTOR = QSize(1, 1)
SIZEF_MIN_INIT_VECTOR = QSizeF(DOUBLE_MIN_INIT_VECTOR, DOUBLE_MIN_INIT_VECTOR)
SIZEF_INIT_VECTOR = QSizeF(0.000, 0.000)
SIZEF_TEST_VECTOR = QSizeF(0.250, 0.250)
SIZEF_MAX_INIT_VECTOR = QSizeF(DOUBLE_MAX_INIT_VECTOR, DOUBLE_MAX_INIT_VECTOR)
RECT_INIT_VECTOR = QRect(0, 0, 0, 0)
RECT_TEST_VECTOR = QRect(1, 1, 1, 1)
RECTF_CONST_INIT_VECTOR = QRectF(0.000, 0.000, 0.500, 0.500)
RECTF_INIT_VECTOR = QRectF(0.00, 0.00, 0.00, 0.00)
RECTF_TEST_VECTOR = QRectF(0.250, 0.250, 0.250, 0.250)
ENUM_INIT_VECTOR = TestEnums.RED
ENUM_TEST_VECTOR = TestEnums.BLUE
FLAG_INIT_VECTOR = TestFlags.BLACK
FLAG_TEST_VECTOR = TestFlags.WHITE
LANGUAGE_LOCALE_INIT_VECTOR = QLocale.English
LANGUAGE_LOCALE_TEST_VECTOR = QLocale.Arabic
TERRITORY_LOCALE_INIT_VECTOR = QLocale.Canada
TERRITORY_LOCALE_TEST_VECTOR = QLocale.Egypt
LOCALE_INIT_VECTOR = QLocale(QLocale.English, QLocale.Canada)
LOCALE_TEST_VECTOR = QLocale(QLocale.Arabic, QLocale.Egypt)
X_SIZE_POLICY_INIT_VECTOR = QSizePolicy.Fixed
X_SIZE_POLICY_TEST_VECTOR = QSizePolicy.Expanding
Y_SIZE_POLICY_INIT_VECTOR = QSizePolicy.Fixed
Y_SIZE_POLICY_TEST_VECTOR = QSizePolicy.MinimumExpanding
X_STRETCH_SIZE_POLICY_INIT_VECTOR = 1
X_STRETCH_SIZE_POLICY_TEST_VECTOR = 0
Y_STRETCH_SIZE_POLICY_INIT_VECTOR = 1
Y_STRETCH_SIZE_POLICY_TEST_VECTOR = 0
SIZE_POLICY_INIT_VECTOR = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
SIZE_POLICY_TEST_VECTOR = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
FONT_INIT_VECTOR = "Arial"
FONT_TEST_VECTOR = "Georgia"
COLOR_INIT_VECTOR = "black"
COLOR_TEST_VECTOR = "white"
CURSOR_INIT_VECTOR = Qt.IBeamCursor
CURSOR_TEST_VECTOR = Qt.ArrowCursor
FILE_INIT_VECTOR = "/etc/resolv.conf"
FILE_TEST_VECTOR = "/etc/hosts"


class QtModel(QObject):
    '''
{
QOBJECT

Q_SIGNALS:
    '''
    intValueChanged = Signal(object, int)
    boolValueChanged = Signal(object, bool)
    floatValueChanged = Signal(object, float)
    complexValueChanged = Signal(object, complex)
    # quaternionValueChanged = Signal(object, quaternion)
    arrayValueChanged = Signal(object, np.ndarray)
    strValueChanged = Signal(object, str)
    qDateValueChanged = Signal(object, QDate)
    qTimeValueChanged = Signal(object, QTime)
    qDateTimeValueChanged = Signal(object, QDateTime)
    qKeySequenceValueChanged = Signal(object, QKeySequence)
    # qChar = Signal(object, QChar)
    qLocaleValueChanged = Signal(object, QLocale)
    qPointValueChanged = Signal(object, QPoint)
    qPointFValueChanged = Signal(object, QPointF)
    qSizeValueChanged = Signal(object, QSize)
    qSizeFValueChanged = Signal(object, QSizeF)
    qRectValueChanged = Signal(object, QRect)
    qRectFValueChanged = Signal(object, QRectF)
    enumValueChanged = Signal(object, Enum)
    flagValueChanged = Signal(object, Flag)
    qSizePolicyValueChanged = Signal(object, QSizePolicy)
    qFontValueChanged = Signal(object, QFont)
    qColorValueChanged = Signal(object, QColor)
    qCursorValueChanged = Signal(object, QCursor)
    '''
public:
    '''
    def atol(self) -> float: return self.m_atol
    def setAtol(self, atol) -> None: self.m_atol = atol
    '''
public Q_SLOTS:
    '''
    @Slot(object, int)
    def setValue(self, property_, val): self.intValueChanged.emit(property_, val)

    @Slot(object, bool)
    def setValue(self, property_, val): self.boolValueChanged.emit(property_, val)

    @Slot(object, float)
    def setValue(self, property_, val): self.floatValueChanged.emit(property_, val)

    @Slot(object, complex)
    def setValue(self, property_, val): self.complexValueChanged.emit(property_, val)

    # @Slot(object, quaternion)
    # def setValue(self, property_, val): self.quaternionValueChanged.emit(property_, val)

    @Slot(object, th.Tensor)
    def setValue(self, property_, val): self.arrayValueChanged.emit(property_, val)

    @Slot(object, str)
    def setValue(self, property_, val): self.strValueChanged.emit(property_, val)

    @Slot(object, QDate)
    def setValue(self, property_, val): self.qDateValueChanged.emit(property_, val)

    @Slot(object, QTime)
    def setValue(self, property_, val): self.qTimevalueChanged.emit(property_, val)

    @Slot(object, QDateTime)
    def setValue(self, property_, val): self.qDateTimeValueChanged.emit(property_, val)

    @Slot(object, QKeySequence)
    def setValue(self, property_, val): self.qKeySequenceValueChanged.emit(property_, val)

    @Slot(object, QLocale)
    def setValue(self, property_, val): self.qLocaleValueChanged.emit(property_, val)

    @Slot(object, QPoint)
    def setValue(self, property_, val): self.qPointValueChanged.emit(property_, val)

    @Slot(object, QPointF)
    def setValue(self, property_, val): self.qPointFValueChanged.emit(property_, val)

    @Slot(object, QSize)
    def setValue(self, property_, val): self.qSizeValueChanged.emit(property_, val)

    @Slot(object, QSizeF)
    def setValue(self, property_, val): self.qSizeFalueChanged.emit(property_, val)

    @Slot(object, QRect)
    def setValue(self, property_, val): self.qRectValueChanged.emit(property_, val)

    @Slot(object, QRectF)
    def setValue(self, property_, val): self.qRectFalueChanged.emit(property_, val)

    @Slot(object, QSizePolicy)
    def setValue(self, property_, val): self.qSizePolicyValueChanged.emit(property_, val)

    @Slot(object, QFont)
    def setValue(self, property_, val): self.qFontValueChanged.emit(property_, val)

    @Slot(object, QColor)
    def setValue(self, property_, val): self.qColoralueChanged.emit(property_, val)

    @Slot(object, QCursor)
    def setValue(self, property_, val): self.qCursorValueChanged.emit(property_, val)

    @Slot(object, bool)
    def setCheck(self, property_, val): print(f"INFO: {property_.propertyName():s}")

    '''
private:
    '''
    m_atol = 0.0


def main():

    count = 0
    app = QApplication()
    model = QtModel()
    dialog = QDialog()
    layout = QGridLayout()
    treeScrollArea = QScrollArea()
    treePropertyBrowser = QtTreePropertyBrowser()
    treePropertyBrowser.setAttributes(
        BrowserCol(BrowserCol.MINIMUM | BrowserCol.MAXIMUM | BrowserCol.UNIT | BrowserCol.FORMAT | BrowserCol.CHECK))
    boxScrollArea = QScrollArea()
    boxPropertyBrowser = QtGroupBoxPropertyBrowser()
    boxPropertyBrowser.setAttributes(
        BrowserCol(BrowserCol.MINIMUM | BrowserCol.MAXIMUM | BrowserCol.UNIT | BrowserCol.FORMAT | BrowserCol.CHECK))
    buttonScrollArea = QScrollArea()
    buttonPropertyBrowser = QtButtonPropertyBrowser()
    buttonPropertyBrowser.setAttributes(
        BrowserCol(BrowserCol.MINIMUM | BrowserCol.MAXIMUM | BrowserCol.UNIT | BrowserCol.FORMAT | BrowserCol.CHECK))

    groupPropertyManager = QtGroupPropertyManager()
    qtIntPropertyManager = QtIntPropertyManager()
    qtBoolPropertyManager =     QtBoolPropertyManager()
    qtDoublePropertyManager = QtDoublePropertyManager()
    qtComplexPropertyManager = QtComplexPropertyManager()
    # qtQuaternionPropertyManager = QtQuaternionPropertyManager()
    qtVectorComplexPropertyManager = QtVectorComplexPropertyManager()
    qtStringPropertyManager = QtStringPropertyManager()
    qtDatePropertyManager = QtDatePropertyManager()
    qtTimePropertyManager = QtTimePropertyManager()
    qtDateTimePropertyManager = QtDateTimePropertyManager()
    qtKeySequencePropertyManager = QtKeySequencePropertyManager()
    qtCharPropertyManager = QtCharPropertyManager()
    qtPointPropertyManager = QtPointPropertyManager()
    qtPointFPropertyManager = QtPointFPropertyManager()
    qtSizePropertyManager = QtSizePropertyManager()
    qtSizeFPropertyManager = QtSizeFPropertyManager()
    qtRectPropertyManager = QtRectPropertyManager()
    qtRectFPropertyManager = QtRectFPropertyManager()
    qtEnumPropertyManager = QtEnumPropertyManager()
    qtFlagPropertyManager = QtFlagPropertyManager()
    qtLocalePropertyManager = QtLocalePropertyManager()
    qtSizePolicyPropertyManager = QtSizePolicyPropertyManager()
    qtFontPropertyManager = QtFontPropertyManager()
    qtColorPropertyManager = QtColorPropertyManager()
    qtCursorPropertyManager = QtCursorPropertyManager()
    qtFilePropertyManager = QtFilePropertyManager()

    groupEditorFactory = QtGroupEditorFactory()
    spinBoxFactory = QtSpinBoxFactory()
    intEditFactory = QtIntEditFactory()
    sliderFactory = QtSliderFactory()
    checkBoxFactory = QtCheckBoxFactory()
    doubleEditFactory = QtDoubleEditFactory()
    doubleSpinBoxFactory = QtDoubleSpinBoxFactory()
    complexEditFactory = QtComplexEditFactory()
    # quaternionEditFactory = QtQuaternionEditFactory()
    vectorComplexEditFactory = QtVectorComplexEditFactory()
    lineEditFactory = QtLineEditFactory()
    dateEditFactory = QtDateEditFactory()
    timeEditFactory = QtTimeEditFactory()
    dateTimeEditFactory = QtDateTimeEditFactory()
    keySequenceEditorFactory = QtKeySequenceEditorFactory()
    charEditorFactory = QtCharEditorFactory()
    pointEditorFactory = QtPointEditorFactory()
    pointFEditorFactory = QtPointFEditorFactory()
    sizeEditorFactory = QtSizeEditorFactory()
    sizeFEditorFactory = QtSizeFEditorFactory()
    rectEditorFactory = QtRectEditorFactory()
    rectFEditorFactory = QtRectFEditorFactory()
    enumEditorFactory = QtEnumEditorFactory()
    flagEditorFactory = QtFlagEditorFactory()
    localeEditorFactory = QtLocaleEditorFactory()
    sizePolicyEditorFactory = QtSizePolicyEditorFactory()
    fontEditorFactory = QtFontEditorFactory()
    colorEditorFactory = QtColorEditorFactory()
    cursorEditorFactory = QtCursorEditorFactory()
    fileEditorFactory = QtFileEditorFactory()

    treePropertyBrowser.setFactoryForManager(groupPropertyManager, groupEditorFactory)
    boxPropertyBrowser.setFactoryForManager(groupPropertyManager, groupEditorFactory)
    buttonPropertyBrowser.setFactoryForManager(groupPropertyManager, groupEditorFactory)

    # Group
    groupProperty = groupPropertyManager.addProperty((f"group {count + 1: d}"))

    # QtIntPropertyManager/IntEditFactory
    # treePropertyBrowser.setFactoryForManager(qtIntPropertyManager, intEditFactory)
    # boxPropertyBrowser.setFactoryForManager(qtIntPropertyManager, intEditFactory)
    # buttonPropertyBrowser.setFactoryForManager(qtIntPropertyManager, intEditFactory)
    # qtIntPropertyManager.valueChanged.connect(model.setValue)
    # model.valueChanged[int].connect(qtIntPropertyManager.setValue)
    # qtIntPropertyManager.checkChanged.connect(model.setCheck)
    # property_ = qtIntPropertyManager.addProperty(f"int_{count + 1:d}")
    # groupProperty.addSubProperty(property_)
    # qtIntPropertyManager.setMinimum(property_, INT_MIN_INIT_VECTOR)
    # qtIntPropertyManager.setMaximum(property_, INT_MAX_INIT_VECTOR)
    # qtIntPropertyManager.setValue(property_, INT_INIT_VECTOR)
    # qtIntPropertyManager.setCheck(property_, False)

    # QtIntPropertyManager/SpinBoxFactory
    treePropertyBrowser.setFactoryForManager(qtIntPropertyManager, spinBoxFactory)
    boxPropertyBrowser.setFactoryForManager(qtIntPropertyManager, spinBoxFactory)
    buttonPropertyBrowser.setFactoryForManager(qtIntPropertyManager, spinBoxFactory)
    qtIntPropertyManager.valueChanged.connect(model.setValue)
    model.intValueChanged.connect(qtIntPropertyManager.setValue)
    qtIntPropertyManager.checkChanged.connect(model.setCheck)
    property_ = qtIntPropertyManager.addProperty(f"int_{count + 1:d}")
    groupProperty.addSubProperty(property_)
    qtIntPropertyManager.setMinimum(property_, INT_MIN_INIT_VECTOR)
    qtIntPropertyManager.setMaximum(property_, INT_MAX_INIT_VECTOR)
    qtIntPropertyManager.setValue(property_, INT_INIT_VECTOR)
    qtIntPropertyManager.setCheck(property_, False)

    # QtIntPropertyManager/SliderFactory
    treePropertyBrowser.setFactoryForManager(qtIntPropertyManager, sliderFactory)
    boxPropertyBrowser.setFactoryForManager(qtIntPropertyManager, sliderFactory)
    buttonPropertyBrowser.setFactoryForManager(qtIntPropertyManager, sliderFactory)
    qtIntPropertyManager.valueChanged.connect(model.setValue)
    model.intValueChanged.connect(qtIntPropertyManager.setValue)
    qtIntPropertyManager.checkChanged.connect(model.setCheck)
    property_ = qtIntPropertyManager.addProperty(f"int_{count + 1:d}")
    groupProperty.addSubProperty(property_)
    qtIntPropertyManager.setMinimum(property_, INT_MIN_INIT_VECTOR)
    qtIntPropertyManager.setMaximum(property_, INT_MAX_INIT_VECTOR)
    qtIntPropertyManager.setValue(property_, INT_INIT_VECTOR)
    qtIntPropertyManager.setCheck(property_, False)

    # QtBoolPropertyManager/CheckBoxFactory
    treePropertyBrowser.setFactoryForManager(qtBoolPropertyManager, checkBoxFactory)
    boxPropertyBrowser.setFactoryForManager(qtBoolPropertyManager, checkBoxFactory)
    buttonPropertyBrowser.setFactoryForManager(qtBoolPropertyManager, checkBoxFactory)
    qtBoolPropertyManager.valueChanged.connect(model.setValue)
    model.boolValueChanged.connect(qtBoolPropertyManager.setValue)
    qtBoolPropertyManager.checkChanged.connect(model.setCheck)
    property_ = qtBoolPropertyManager.addProperty(f"bool_{count + 1:d}")
    groupProperty.addSubProperty(property_)
    qtBoolPropertyManager.setValue(property_, False)
    qtBoolPropertyManager.setCheck(property_, False)

    # QtDoublePropertyManager/DoubleEditFactory
    # treePropertyBrowser.setFactoryForManager(qtDoublePropertyManager, doubleEditFactory)
    # boxPropertyBrowser.setFactoryForManager(qtDoublePropertyManager, doubleEditFactory)
    # buttonPropertyBrowser.setFactoryForManager(qtDoublePropertyManager, doubleEditFactory)
    # qtDoublePropertyManager.valueChanged.connect(model.setValue)
    # model.valueChanged[float].connect(qtDoublePropertyManager.setValue)
    # qtDoublePropertyManager.checkChanged.connect(model.setCheck)
    # property_ = qtDoublePropertyManager.addProperty(f"float_{count + 1:d}")
    # groupProperty.addSubProperty(property_)
    # qtDoublePropertyManager.setMinimum(property_, DOUBLE_MIN_INIT_VECTOR)
    # qtDoublePropertyManager.setMaximum(property_, DOUBLE_MAX_INIT_VECTOR)
    # qtDoublePropertyManager.setPrecision(property_, DOUBLE_PRECISION)
    # qtDoublePropertyManager.setValue(property_, DOUBLE_INIT_VECTOR)
    # qtDoublePropertyManager.setCheck(property_, False)

    # QtDoublePropertyManager/DoubleSpinBoxFactory
    treePropertyBrowser.setFactoryForManager(qtDoublePropertyManager, doubleSpinBoxFactory)
    boxPropertyBrowser.setFactoryForManager(qtDoublePropertyManager, doubleSpinBoxFactory)
    buttonPropertyBrowser.setFactoryForManager(qtDoublePropertyManager, doubleSpinBoxFactory)
    qtDoublePropertyManager.valueChanged.connect(model.setValue)
    model.floatValueChanged.connect(qtDoublePropertyManager.setValue)
    qtDoublePropertyManager.checkChanged.connect(model.setCheck)
    property_ = qtDoublePropertyManager.addProperty(f"float_{count + 1:d}")
    groupProperty.addSubProperty(property_)
    qtDoublePropertyManager.setMinimum(property_, DOUBLE_MIN_INIT_VECTOR)
    qtDoublePropertyManager.setMaximum(property_, DOUBLE_MAX_INIT_VECTOR)
    qtDoublePropertyManager.setPrecision(property_, DOUBLE_PRECISION)
    qtDoublePropertyManager.setValue(property_, DOUBLE_INIT_VECTOR)
    qtDoublePropertyManager.setCheck(property_, False)

    # QtComplexPropertyManager/ComplexEditFactory
    treePropertyBrowser.setFactoryForManager(qtComplexPropertyManager, complexEditFactory)
    boxPropertyBrowser.setFactoryForManager(qtComplexPropertyManager, complexEditFactory)
    buttonPropertyBrowser.setFactoryForManager(qtComplexPropertyManager, complexEditFactory)
    qtComplexPropertyManager.valueChanged.connect(model.setValue)
    model.complexValueChanged.connect(qtComplexPropertyManager.setValue)
    qtComplexPropertyManager.checkChanged.connect(model.setCheck)
    property_ = qtComplexPropertyManager.addProperty(f"complex_{count + 1:d}")
    groupProperty.addSubProperty(property_)
    qtComplexPropertyManager.setPrecision(property_, COMPLEX_PRECISION)
    qtComplexPropertyManager.setMinimum(property_, complex(COMPLEX_MIN_INIT_VECTOR))
    qtComplexPropertyManager.setMaximum(property_, complex(COMPLEX_MAX_INIT_VECTOR))
    qtComplexPropertyManager.setValue(property_, complex(COMPLEX_INIT_VECTOR))
    qtComplexPropertyManager.setCheck(property_, False)

    # QtQuaternionPropertyManager/QuaternionEditFactory
    # treePropertyBrowser.setFactoryForManager(qtQuaternionPropertyManager, quaternionEditFactory)
    # boxPropertyBrowser.setFactoryForManager(qtQuaternionPropertyManager, quaternionEditFactory)
    # buttonPropertyBrowser.setFactoryForManager(qtQuaternionPropertyManager, quaternionEditFactory)
    # qtQuaternionPropertyManager.valueChanged.connect(model.setValue)
    # model.quaternionValueChanged.connect(qtQuaternionPropertyManager.setValue)
    # qtQuaternionPropertyManager.checkChanged.connect(model.setCheck)
    # property_ = qtQuaternionPropertyManager.addProperty(f"quaternion_{count + 1:d}")
    # groupProperty.addSubProperty(property_)
    # qtQuaternionPropertyManager.setPrecision(property_, QUATERNION_PRECISION)
    # qtQuaternionPropertyManager.setMinimum(property_, QtQuaternion(QUATERNION_MIN_INIT_VECTOR))
    # qtQuaternionPropertyManager.setMaximum(property_, QtQuaternion(QUATERNION_MAX_INIT_VECTOR))
    # qtQuaternionPropertyManager.setValue(property_, QtQuaternion(QUATERNION_INIT_VECTOR))
    # qtQuaternionPropertyManager.setCheck(property_, False)

    # QtVectorComplexPropertyManager/vectorComplexEditFactory
    vectorComplexEditFactory.setSubFactory(complexEditFactory)
    treePropertyBrowser.setFactoryForManager(qtVectorComplexPropertyManager, vectorComplexEditFactory)
    boxPropertyBrowser.setFactoryForManager(qtVectorComplexPropertyManager, vectorComplexEditFactory)
    buttonPropertyBrowser.setFactoryForManager(qtVectorComplexPropertyManager, vectorComplexEditFactory)
    treePropertyBrowser.setFactoryForManager(qtVectorComplexPropertyManager.subComplexPropertyManager(), complexEditFactory)
    boxPropertyBrowser.setFactoryForManager(qtVectorComplexPropertyManager.subComplexPropertyManager(), complexEditFactory)
    buttonPropertyBrowser.setFactoryForManager(qtVectorComplexPropertyManager.subComplexPropertyManager(), complexEditFactory)
    qtVectorComplexPropertyManager.valueChanged.connect(model.setValue)
    model.arrayValueChanged.connect(qtVectorComplexPropertyManager.setValue)
    qtVectorComplexPropertyManager.checkChanged.connect(model.setCheck)
    property_ = qtVectorComplexPropertyManager.addProperty(f"th.tensor_{count + 1:d}")
    groupProperty.addSubProperty(property_)
    qtVectorComplexPropertyManager.setSize(property_, VECTOR_SIZE)
    qtVectorComplexPropertyManager.setPrecision(property_, COMPLEX_PRECISION)
    qtVectorComplexPropertyManager.setMinimum(property_, np.ones(VECTOR_SIZE, dtype=complex) * COMPLEX_MIN_INIT_VECTOR)
    qtVectorComplexPropertyManager.setMaximum(property_, np.ones(VECTOR_SIZE, dtype=complex) * COMPLEX_MAX_INIT_VECTOR)
    qtVectorComplexPropertyManager.setValue(property_, np.asarray(COMPLEX_TEST_VECTOR, dtype=complex))
    qtVectorComplexPropertyManager.setCheck(property_, False)

    # QtStringPropertyManager/LineEditFactory
    treePropertyBrowser.setFactoryForManager(qtStringPropertyManager, lineEditFactory)
    boxPropertyBrowser.setFactoryForManager(qtStringPropertyManager, lineEditFactory)
    buttonPropertyBrowser.setFactoryForManager(qtStringPropertyManager, lineEditFactory)
    qtStringPropertyManager.valueChanged.connect(model.setValue)
    model.strValueChanged.connect(qtStringPropertyManager.setValue)
    qtStringPropertyManager.checkChanged.connect(model.setCheck)
    property_ = qtStringPropertyManager.addProperty(f"str_{count + 1:d}")
    groupProperty.addSubProperty(property_)
    qtStringPropertyManager.setValue(property_, STR_INIT_VECTOR)
    qtStringPropertyManager.setCheck(property_, False)

    # QtDatePropertyManager/DateEditFactory
    treePropertyBrowser.setFactoryForManager(qtDatePropertyManager, dateEditFactory)
    boxPropertyBrowser.setFactoryForManager(qtDatePropertyManager, dateEditFactory)
    buttonPropertyBrowser.setFactoryForManager(qtDatePropertyManager, dateEditFactory)
    qtDatePropertyManager.valueChanged.connect(model.setValue)
    model.qDateValueChanged.connect(qtDatePropertyManager.setValue)
    qtDatePropertyManager.checkChanged.connect(model.setCheck)
    property_ = qtDatePropertyManager.addProperty(f"QDate_{count + 1:d}")
    groupProperty.addSubProperty(property_)
    qtDatePropertyManager.setValue(property_, QDate(DATE_INIT_VECTOR))
    qtDatePropertyManager.setCheck(property_, False)

    # QtTimePropertyManager/TimeEditFactory
    treePropertyBrowser.setFactoryForManager(qtTimePropertyManager, timeEditFactory)
    boxPropertyBrowser.setFactoryForManager(qtTimePropertyManager, timeEditFactory)
    buttonPropertyBrowser.setFactoryForManager(qtTimePropertyManager, timeEditFactory)
    qtTimePropertyManager.valueChanged.connect(model.setValue)
    model.qTimeValueChanged.connect(qtTimePropertyManager.setValue)
    qtTimePropertyManager.checkChanged.connect(model.setCheck)
    property_ = qtTimePropertyManager.addProperty(f"QTime_{count + 1:d}")
    groupProperty.addSubProperty(property_)
    qtTimePropertyManager.setValue(property_, QTime(TIME_INIT_VECTOR))
    qtTimePropertyManager.setCheck(property_, False)

    # QtDateTimePropertyManager/DateTimeEditFactory
    treePropertyBrowser.setFactoryForManager(qtDateTimePropertyManager, dateTimeEditFactory)
    boxPropertyBrowser.setFactoryForManager(qtDateTimePropertyManager, dateTimeEditFactory)
    buttonPropertyBrowser.setFactoryForManager(qtDateTimePropertyManager, dateTimeEditFactory)
    qtDateTimePropertyManager.valueChanged.connect(model.setValue)
    model.qDateTimeValueChanged.connect(qtDateTimePropertyManager.setValue)
    qtDateTimePropertyManager.checkChanged.connect(model.setCheck)
    property_ = qtDateTimePropertyManager.addProperty(f"QDateTime_{count + 1:d}")
    groupProperty.addSubProperty(property_)
    qtDateTimePropertyManager.setValue(property_, QDateTime(DATETIME_INIT_VECTOR))
    qtDateTimePropertyManager.setCheck(property_, False)

    # QtKeySequencePropertyManager/KeySequenceEditorFactory
    treePropertyBrowser.setFactoryForManager(qtKeySequencePropertyManager, keySequenceEditorFactory)
    boxPropertyBrowser.setFactoryForManager(qtKeySequencePropertyManager, keySequenceEditorFactory)
    buttonPropertyBrowser.setFactoryForManager(qtKeySequencePropertyManager, keySequenceEditorFactory)
    qtKeySequencePropertyManager.valueChanged.connect(model.setValue)
    model.qKeySequenceValueChanged.connect(qtKeySequencePropertyManager.setValue)
    qtKeySequencePropertyManager.checkChanged.connect(model.setCheck)
    property_ = qtKeySequencePropertyManager.addProperty(f"QKeySequence_{count + 1:d}")
    groupProperty.addSubProperty(property_)
    qtKeySequencePropertyManager.setValue(property_, QKeySequence(KEY_INIT_VECTOR))
    qtKeySequencePropertyManager.setCheck(property_, False)

    # QtCharPropertyManager/CharEditorFactory
    # treePropertyBrowser.setFactoryForManager(qtCharPropertyManager, charEditorFactory)
    # boxPropertyBrowser.setFactoryForManager(qtCharPropertyManager, charEditorFactory)
    # buttonPropertyBrowser.setFactoryForManager(qtCharPropertyManager, charEditorFactory)
    # qtCharPropertyManager.valueChanged.connect(model.setValue)
    # model.charValueChanged.connect(qtCharPropertyManager.setValue)
    # qtCharPropertyManager.checkChanged.connect(model.setCheck)
    # property_ = qtCharPropertyManager.addProperty(f"char{count + 1:d}")
    # groupProperty.addSubProperty(property_)
    # qtCharPropertyManager.setValue(property_, CHAR_INIT_VECTOR)
    # qtCharPropertyManager.setCheck(property_, False)

    # QtPointPropertyManager/PointEditorFactory
    treePropertyBrowser.setFactoryForManager(qtPointPropertyManager, pointEditorFactory)
    boxPropertyBrowser.setFactoryForManager(qtPointPropertyManager, pointEditorFactory)
    buttonPropertyBrowser.setFactoryForManager(qtPointPropertyManager, pointEditorFactory)
    treePropertyBrowser.setFactoryForManager(qtPointPropertyManager.subIntPropertyManager(), intEditFactory)
    boxPropertyBrowser.setFactoryForManager(qtPointPropertyManager.subIntPropertyManager(), intEditFactory)
    buttonPropertyBrowser.setFactoryForManager(qtPointPropertyManager.subIntPropertyManager(), intEditFactory)
    qtPointPropertyManager.valueChanged.connect(model.setValue)
    model.qPointValueChanged.connect(qtPointPropertyManager.setValue)
    qtPointPropertyManager.checkChanged.connect(model.setCheck)
    property_ = qtPointPropertyManager.addProperty(f"QPoint_{count + 1:d}")
    groupProperty.addSubProperty(property_)
    qtPointPropertyManager.setValue(property_, QPoint(POINT_INIT_VECTOR))
    qtPointPropertyManager.setCheck(property_, False)

    # QtPointFPropertyManager/PointFEditorFactory
    treePropertyBrowser.setFactoryForManager(qtPointFPropertyManager, pointFEditorFactory)
    boxPropertyBrowser.setFactoryForManager(qtPointFPropertyManager, pointFEditorFactory)
    buttonPropertyBrowser.setFactoryForManager(qtPointFPropertyManager, pointFEditorFactory)
    treePropertyBrowser.setFactoryForManager(qtPointFPropertyManager.subDoublePropertyManager(), doubleEditFactory)
    boxPropertyBrowser.setFactoryForManager(qtPointFPropertyManager.subDoublePropertyManager(), doubleEditFactory)
    buttonPropertyBrowser.setFactoryForManager(qtPointFPropertyManager.subDoublePropertyManager(), doubleEditFactory)
    qtPointFPropertyManager.valueChanged.connect(model.setValue)
    model.qPointFValueChanged.connect(qtPointFPropertyManager.setValue)
    qtPointFPropertyManager.checkChanged.connect(model.setCheck)
    property_ = qtPointFPropertyManager.addProperty(f"QPointF_{count + 1:d}")
    groupProperty.addSubProperty(property_)
    qtPointFPropertyManager.setMinimum(property_, QPointF(POINTF_MIN_INIT_VECTOR))
    qtPointFPropertyManager.setMaximum(property_, QPointF(POINTF_MAX_INIT_VECTOR))
    qtPointFPropertyManager.setPrecision(property_, DOUBLE_PRECISION)
    qtPointFPropertyManager.setValue(property_, QPointF(POINTF_INIT_VECTOR))
    qtPointFPropertyManager.setCheck(property_, False)

    # QtSizePropertyManager/SizeEditorFactory
    treePropertyBrowser.setFactoryForManager(qtSizePropertyManager, sizeEditorFactory)
    boxPropertyBrowser.setFactoryForManager(qtSizePropertyManager, sizeEditorFactory)
    buttonPropertyBrowser.setFactoryForManager(qtSizePropertyManager, sizeEditorFactory)
    treePropertyBrowser.setFactoryForManager(qtSizePropertyManager.subIntPropertyManager(), intEditFactory)
    boxPropertyBrowser.setFactoryForManager(qtSizePropertyManager.subIntPropertyManager(), intEditFactory)
    buttonPropertyBrowser.setFactoryForManager(qtSizePropertyManager.subIntPropertyManager(), intEditFactory)
    qtSizePropertyManager.valueChanged.connect(model.setValue)
    model.qSizeValueChanged.connect(qtSizePropertyManager.setValue)
    qtSizePropertyManager.checkChanged.connect(model.setCheck)
    property_ = qtSizePropertyManager.addProperty(f"QSize{count + 1:d}")
    groupProperty.addSubProperty(property_)
    qtSizePropertyManager.setValue(property_, QSize(SIZE_INIT_VECTOR))
    qtSizePropertyManager.setCheck(property_, False)

    # QtSizeFPropertyManager/SizeFEditorFactory
    treePropertyBrowser.setFactoryForManager(qtSizeFPropertyManager, sizeFEditorFactory)
    boxPropertyBrowser.setFactoryForManager(qtSizeFPropertyManager, sizeFEditorFactory)
    buttonPropertyBrowser.setFactoryForManager(qtSizeFPropertyManager, sizeFEditorFactory)
    treePropertyBrowser.setFactoryForManager(qtSizeFPropertyManager.subDoublePropertyManager(), doubleEditFactory)
    boxPropertyBrowser.setFactoryForManager(qtSizeFPropertyManager.subDoublePropertyManager(), doubleEditFactory)
    buttonPropertyBrowser.setFactoryForManager(qtSizeFPropertyManager.subDoublePropertyManager(), doubleEditFactory)
    qtSizeFPropertyManager.valueChanged.connect(model.setValue)
    model.qSizeFValueChanged.connect(qtSizeFPropertyManager.setValue)
    qtSizeFPropertyManager.checkChanged.connect(model.setCheck)
    property_ = qtSizeFPropertyManager.addProperty(f"QSizeF{count + 1:d}")
    groupProperty.addSubProperty(property_)
    qtSizeFPropertyManager.setMinimum(property_, QSizeF(SIZEF_MIN_INIT_VECTOR))
    qtSizeFPropertyManager.setMaximum(property_, QSizeF(SIZEF_MAX_INIT_VECTOR))
    qtSizeFPropertyManager.setPrecision(property_, DOUBLE_PRECISION)
    qtSizeFPropertyManager.setValue(property_, QSizeF(SIZEF_INIT_VECTOR))
    qtSizeFPropertyManager.setCheck(property_, False)

    # QtRectPropertyManager/RectEditorFactory
    treePropertyBrowser.setFactoryForManager(qtRectPropertyManager, rectEditorFactory)
    boxPropertyBrowser.setFactoryForManager(qtRectPropertyManager, rectEditorFactory)
    buttonPropertyBrowser.setFactoryForManager(qtRectPropertyManager, rectEditorFactory)
    treePropertyBrowser.setFactoryForManager(qtRectPropertyManager.subIntPropertyManager(), intEditFactory)
    boxPropertyBrowser.setFactoryForManager(qtRectPropertyManager.subIntPropertyManager(), intEditFactory)
    buttonPropertyBrowser.setFactoryForManager(qtRectPropertyManager.subIntPropertyManager(), intEditFactory)
    qtRectPropertyManager.valueChanged.connect(model.setValue)
    model.qRectValueChanged.connect(qtRectPropertyManager.setValue)
    qtRectPropertyManager.checkChanged.connect(model.setCheck)
    property_ = qtRectPropertyManager.addProperty(f"QRect{count + 1:d}")
    groupProperty.addSubProperty(property_)
    qtRectPropertyManager.setValue(property_, QRect(RECT_INIT_VECTOR))
    qtRectPropertyManager.setCheck(property_, False)

    # QtRectFPropertyManager/RectFEditorFactory
    treePropertyBrowser.setFactoryForManager(qtRectFPropertyManager, rectFEditorFactory)
    boxPropertyBrowser.setFactoryForManager(qtRectFPropertyManager, rectFEditorFactory)
    buttonPropertyBrowser.setFactoryForManager(qtRectFPropertyManager, rectFEditorFactory)
    treePropertyBrowser.setFactoryForManager(qtRectFPropertyManager.subDoublePropertyManager(), doubleEditFactory)
    boxPropertyBrowser.setFactoryForManager(qtRectFPropertyManager.subDoublePropertyManager(), doubleEditFactory)
    buttonPropertyBrowser.setFactoryForManager(qtRectFPropertyManager.subDoublePropertyManager(), doubleEditFactory)
    qtRectFPropertyManager.valueChanged.connect(model.setValue)
    model.qRectFValueChanged.connect(qtRectFPropertyManager.setValue)
    qtRectFPropertyManager.checkChanged.connect(model.setCheck)
    property_ = qtRectFPropertyManager.addProperty(f"QRectF{count + 1:d}")
    groupProperty.addSubProperty(property_)
    qtRectFPropertyManager.setConstraint(property_, QRectF(RECTF_CONST_INIT_VECTOR))
    qtRectFPropertyManager.setPrecision(property_, DOUBLE_PRECISION)
    qtRectFPropertyManager.setValue(property_, QRectF(RECTF_INIT_VECTOR))
    qtRectFPropertyManager.setCheck(property_, False)

    # QtEnumPropertyManager/EnumEditorFactory
    treePropertyBrowser.setFactoryForManager(qtEnumPropertyManager, enumEditorFactory)
    boxPropertyBrowser.setFactoryForManager(qtEnumPropertyManager, enumEditorFactory)
    buttonPropertyBrowser.setFactoryForManager(qtEnumPropertyManager, enumEditorFactory)
    qtEnumPropertyManager.valueChanged.connect(model.setValue)
    model.enumValueChanged.connect(qtEnumPropertyManager.setValue)
    qtEnumPropertyManager.checkChanged.connect(model.setCheck)
    property_ = qtEnumPropertyManager.addProperty(f"Enum_{count + 1:d}")
    groupProperty.addSubProperty(property_)
    enumNames = list()
    enumNames = ["BLACK", "RED", "GREEN", "BLUE"]
    qtEnumPropertyManager.setEnumNames(property_, enumNames)
    qtEnumPropertyManager.setValue(property_, int(ENUM_INIT_VECTOR.value))
    qtEnumPropertyManager.setCheck(property_, False)

    # QtFlagPropertyManager/FlagEditorFactory
    treePropertyBrowser.setFactoryForManager(qtFlagPropertyManager, flagEditorFactory)
    boxPropertyBrowser.setFactoryForManager(qtFlagPropertyManager, flagEditorFactory)
    buttonPropertyBrowser.setFactoryForManager(qtFlagPropertyManager, flagEditorFactory)
    treePropertyBrowser.setFactoryForManager(qtFlagPropertyManager.subBoolPropertyManager(), checkBoxFactory)
    boxPropertyBrowser.setFactoryForManager(qtFlagPropertyManager.subBoolPropertyManager(), checkBoxFactory)
    buttonPropertyBrowser.setFactoryForManager(qtFlagPropertyManager.subBoolPropertyManager(), checkBoxFactory)
    qtFlagPropertyManager.valueChanged.connect(model.setValue)
    model.flagValueChanged.connect(qtFlagPropertyManager.setValue)
    qtFlagPropertyManager.checkChanged.connect(model.setCheck)
    property_ = qtFlagPropertyManager.addProperty(f"Flag_{count + 1:d}")
    groupProperty.addSubProperty(property_)
    flagName = list()
    flagNames = ["RED", "GREEN", "BLUE"]
    qtFlagPropertyManager.setFlagNames(property_, flagNames)
    qtFlagPropertyManager.setValue(property_, int(FLAG_INIT_VECTOR.value))
    qtFlagPropertyManager.setCheck(property_, False)

    # QtLocalePropertyManager/LocaleEditorFactory
    treePropertyBrowser.setFactoryForManager(qtLocalePropertyManager, localeEditorFactory)
    boxPropertyBrowser.setFactoryForManager(qtLocalePropertyManager, localeEditorFactory)
    buttonPropertyBrowser.setFactoryForManager(qtLocalePropertyManager, localeEditorFactory)
    treePropertyBrowser.setFactoryForManager(qtLocalePropertyManager.subEnumPropertyManager(), enumEditorFactory)
    boxPropertyBrowser.setFactoryForManager(qtLocalePropertyManager.subEnumPropertyManager(), enumEditorFactory)
    buttonPropertyBrowser.setFactoryForManager(qtLocalePropertyManager.subEnumPropertyManager(), enumEditorFactory)
    qtLocalePropertyManager.valueChanged.connect(model.setValue)
    model.qLocaleValueChanged.connect(qtLocalePropertyManager.setValue)
    qtLocalePropertyManager.checkChanged.connect(model.setCheck)
    property_ = qtLocalePropertyManager.addProperty(f"QLocale_{count + 1:d}")
    groupProperty.addSubProperty(property_)
    qtLocalePropertyManager.setValue(property_, QLocale(LOCALE_INIT_VECTOR))
    qtLocalePropertyManager.setCheck(property_, False)

    # QtSizePolicyPropertyManager/SizePolicyEditorFactory
    treePropertyBrowser.setFactoryForManager(qtSizePolicyPropertyManager, sizePolicyEditorFactory)
    boxPropertyBrowser.setFactoryForManager(qtSizePolicyPropertyManager, sizePolicyEditorFactory)
    buttonPropertyBrowser.setFactoryForManager(qtSizePolicyPropertyManager, sizePolicyEditorFactory)
    treePropertyBrowser.setFactoryForManager(qtSizePolicyPropertyManager.subEnumPropertyManager(), enumEditorFactory)
    boxPropertyBrowser.setFactoryForManager(qtSizePolicyPropertyManager.subIntPropertyManager(), intEditFactory)
    buttonPropertyBrowser.setFactoryForManager(qtSizePolicyPropertyManager.subEnumPropertyManager(), enumEditorFactory)
    treePropertyBrowser.setFactoryForManager(qtSizePolicyPropertyManager.subIntPropertyManager(), intEditFactory)
    boxPropertyBrowser.setFactoryForManager(qtSizePolicyPropertyManager.subEnumPropertyManager(), enumEditorFactory)
    buttonPropertyBrowser.setFactoryForManager(qtSizePolicyPropertyManager.subIntPropertyManager(), intEditFactory)
    qtSizePolicyPropertyManager.valueChanged.connect(model.setValue)
    model.qSizePolicyValueChanged.connect(qtSizePolicyPropertyManager.setValue)
    qtSizePolicyPropertyManager.checkChanged.connect(model.setCheck)
    property_ = qtSizePolicyPropertyManager.addProperty(f"QSizePolicy_{count + 1:d}")
    groupProperty.addSubProperty(property_)
    sizePolicy = SIZE_POLICY_INIT_VECTOR
    sizePolicy.setHorizontalStretch(X_STRETCH_SIZE_POLICY_INIT_VECTOR)
    sizePolicy.setVerticalStretch(Y_STRETCH_SIZE_POLICY_INIT_VECTOR)
    qtSizePolicyPropertyManager.setValue(property_, sizePolicy)
    qtSizePolicyPropertyManager.setCheck(property_, False)

    # QtFontPropertyManager/FontEditorFactory
    treePropertyBrowser.setFactoryForManager(qtFontPropertyManager, fontEditorFactory)
    boxPropertyBrowser.setFactoryForManager(qtFontPropertyManager, fontEditorFactory)
    buttonPropertyBrowser.setFactoryForManager(qtFontPropertyManager, fontEditorFactory)
    qtFontPropertyManager.valueChanged.connect(model.setValue)
    model.qFontValueChanged.connect(qtFontPropertyManager.setValue)
    qtFontPropertyManager.checkChanged.connect(model.setCheck)
    property_ = qtFontPropertyManager.addProperty(f"QFont_{count + 1:d}")
    groupProperty.addSubProperty(property_)
    qtFontPropertyManager.setValue(property_, QFont(FONT_INIT_VECTOR))
    qtFontPropertyManager.setCheck(property_, False)

    # QtColorPropertyManager/ColorEditorFactory
    treePropertyBrowser.setFactoryForManager(qtColorPropertyManager, colorEditorFactory)
    boxPropertyBrowser.setFactoryForManager(qtColorPropertyManager, colorEditorFactory)
    buttonPropertyBrowser.setFactoryForManager(qtColorPropertyManager, colorEditorFactory)
    qtColorPropertyManager.valueChanged.connect(model.setValue)
    model.qColorValueChanged.connect(qtColorPropertyManager.setValue)
    qtColorPropertyManager.checkChanged.connect(model.setCheck)
    property_ = qtColorPropertyManager.addProperty(f"QColor_{count + 1:d}")
    groupProperty.addSubProperty(property_)
    qtColorPropertyManager.setValue(property_, COLOR_INIT_VECTOR)
    qtColorPropertyManager.setCheck(property_, False)

    # QtCursorPropertyManager/CursorEditorFactory
    treePropertyBrowser.setFactoryForManager(qtCursorPropertyManager, cursorEditorFactory)
    boxPropertyBrowser.setFactoryForManager(qtCursorPropertyManager, cursorEditorFactory)
    buttonPropertyBrowser.setFactoryForManager(qtCursorPropertyManager, cursorEditorFactory)
    qtCursorPropertyManager.valueChanged.connect(model.setValue)
    model.qCursorValueChanged.connect(qtCursorPropertyManager.setValue)
    qtCursorPropertyManager.checkChanged.connect(model.setCheck)
    property_ = qtCursorPropertyManager.addProperty(f"QCursor_{count + 1:d}")
    groupProperty.addSubProperty(property_)
    qtCursorPropertyManager.setValue(property_, QCursor(CURSOR_INIT_VECTOR))
    qtCursorPropertyManager.setCheck(property_, False)

    # QtFilePropertyManager/FileEditorFactory
    treePropertyBrowser.setFactoryForManager(qtFilePropertyManager, fileEditorFactory)
    boxPropertyBrowser.setFactoryForManager(qtFilePropertyManager, fileEditorFactory)
    buttonPropertyBrowser.setFactoryForManager(qtFilePropertyManager, fileEditorFactory)
    qtFilePropertyManager.valueChanged.connect(model.setValue)
    model.strValueChanged.connect(qtFilePropertyManager.setValue)
    qtFilePropertyManager.checkChanged.connect(model.setCheck)
    property_ = qtFilePropertyManager.addProperty(f"QFile_{count + 1:d}")
    groupProperty.addSubProperty(property_)
    qtFilePropertyManager.setValue(property_, FILE_INIT_VECTOR)
    qtFilePropertyManager.setCheck(property_, False)

    browserItem = treePropertyBrowser.addProperty(groupProperty)
    treePropertyBrowser.setExpanded(browserItem, True)
    browserItem = boxPropertyBrowser.addProperty(groupProperty)
    browserItem = buttonPropertyBrowser.addProperty(groupProperty)
    buttonPropertyBrowser.setExpanded(browserItem, True)

    treeScrollArea.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    treeScrollArea.setWidgetResizable(True)
    treeScrollArea.setWidget(treePropertyBrowser)
    layout.addWidget(QLabel("Tree Browser", dialog), 0, 0)
    layout.addWidget(treeScrollArea, 1, 0)

    boxScrollArea.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    boxScrollArea.setWidgetResizable(True)
    boxScrollArea.setWidget(boxPropertyBrowser)
    layout.addWidget(QLabel("Box Browser", dialog), 0, 1)
    layout.addWidget(boxScrollArea, 1, 1)

    buttonScrollArea.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    buttonScrollArea.setWidgetResizable(True)
    buttonScrollArea.setWidget(buttonPropertyBrowser)
    layout.addWidget(QLabel("Button Browser", dialog), 0, 2)
    layout.addWidget(buttonScrollArea, 1, 2)

    dialog.setLayout(layout)
    dialog.showMaximized()
    ret = QApplication.exec()
    del dialog;
    return ret


if __name__ == "__main__":
    main()
