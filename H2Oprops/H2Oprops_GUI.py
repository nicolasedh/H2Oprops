# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'H2Oprops.ui'
#
# Created: Mon Jul 14 22:53:58 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(643, 644)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.frame = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.Box)
        self.frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame.setLineWidth(2)
        self.frame.setMidLineWidth(0)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.input_selector = QtGui.QComboBox(self.frame)
        self.input_selector.setObjectName(_fromUtf8("input_selector"))
        self.input_selector.addItem(_fromUtf8(""))
        self.input_selector.addItem(_fromUtf8(""))
        self.input_selector.addItem(_fromUtf8(""))
        self.input_selector.addItem(_fromUtf8(""))
        self.input_selector.addItem(_fromUtf8(""))
        self.input_selector.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.input_selector)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_input2 = QtGui.QLabel(self.frame)
        self.label_input2.setObjectName(_fromUtf8("label_input2"))
        self.gridLayout.addWidget(self.label_input2, 1, 0, 1, 1)
        self.input2 = QtGui.QLineEdit(self.frame)
        self.input2.setObjectName(_fromUtf8("input2"))
        self.gridLayout.addWidget(self.input2, 1, 1, 1, 1)
        self.label_input2_unit = QtGui.QLabel(self.frame)
        self.label_input2_unit.setObjectName(_fromUtf8("label_input2_unit"))
        self.gridLayout.addWidget(self.label_input2_unit, 1, 2, 1, 1)
        self.input1 = QtGui.QLineEdit(self.frame)
        self.input1.setObjectName(_fromUtf8("input1"))
        self.gridLayout.addWidget(self.input1, 0, 1, 1, 1)
        self.label_input1_unit = QtGui.QLabel(self.frame)
        self.label_input1_unit.setObjectName(_fromUtf8("label_input1_unit"))
        self.gridLayout.addWidget(self.label_input1_unit, 0, 2, 1, 1)
        self.label_input1 = QtGui.QLabel(self.frame)
        self.label_input1.setObjectName(_fromUtf8("label_input1"))
        self.gridLayout.addWidget(self.label_input1, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_calculate = QtGui.QPushButton(self.frame)
        self.pushButton_calculate.setObjectName(_fromUtf8("pushButton_calculate"))
        self.horizontalLayout.addWidget(self.pushButton_calculate)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.frame)
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea.setFrameShape(QtGui.QFrame.Box)
        self.scrollArea.setLineWidth(2)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 605, 408))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_2 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_pressure = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_pressure.setObjectName(_fromUtf8("label_pressure"))
        self.gridLayout_2.addWidget(self.label_pressure, 0, 0, 1, 1)
        self.pressure = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.pressure.setText(_fromUtf8(""))
        self.pressure.setReadOnly(True)
        self.pressure.setObjectName(_fromUtf8("pressure"))
        self.gridLayout_2.addWidget(self.pressure, 0, 1, 1, 1)
        self.label_pressure_unit = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_pressure_unit.setObjectName(_fromUtf8("label_pressure_unit"))
        self.gridLayout_2.addWidget(self.label_pressure_unit, 0, 2, 1, 1)
        self.label_cp = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_cp.setObjectName(_fromUtf8("label_cp"))
        self.gridLayout_2.addWidget(self.label_cp, 1, 0, 1, 1)
        self.cp = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.cp.setText(_fromUtf8(""))
        self.cp.setReadOnly(True)
        self.cp.setObjectName(_fromUtf8("cp"))
        self.gridLayout_2.addWidget(self.cp, 1, 1, 1, 1)
        self.label_cp_unit = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_cp_unit.setObjectName(_fromUtf8("label_cp_unit"))
        self.gridLayout_2.addWidget(self.label_cp_unit, 1, 2, 1, 1)
        self.label_temperature = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_temperature.setObjectName(_fromUtf8("label_temperature"))
        self.gridLayout_2.addWidget(self.label_temperature, 2, 0, 1, 1)
        self.temperature = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.temperature.setText(_fromUtf8(""))
        self.temperature.setReadOnly(True)
        self.temperature.setObjectName(_fromUtf8("temperature"))
        self.gridLayout_2.addWidget(self.temperature, 2, 1, 1, 1)
        self.label_temperature_unit = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_temperature_unit.setObjectName(_fromUtf8("label_temperature_unit"))
        self.gridLayout_2.addWidget(self.label_temperature_unit, 2, 2, 1, 1)
        self.label_density = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_density.setObjectName(_fromUtf8("label_density"))
        self.gridLayout_2.addWidget(self.label_density, 3, 0, 1, 1)
        self.density = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.density.setText(_fromUtf8(""))
        self.density.setReadOnly(True)
        self.density.setObjectName(_fromUtf8("density"))
        self.gridLayout_2.addWidget(self.density, 3, 1, 1, 1)
        self.label_density_unit = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_density_unit.setObjectName(_fromUtf8("label_density_unit"))
        self.gridLayout_2.addWidget(self.label_density_unit, 3, 2, 1, 1)
        self.label_enthalpy = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_enthalpy.setObjectName(_fromUtf8("label_enthalpy"))
        self.gridLayout_2.addWidget(self.label_enthalpy, 4, 0, 1, 1)
        self.enthalpy = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.enthalpy.setText(_fromUtf8(""))
        self.enthalpy.setReadOnly(True)
        self.enthalpy.setObjectName(_fromUtf8("enthalpy"))
        self.gridLayout_2.addWidget(self.enthalpy, 4, 1, 1, 1)
        self.label_enthalpy_unit = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_enthalpy_unit.setObjectName(_fromUtf8("label_enthalpy_unit"))
        self.gridLayout_2.addWidget(self.label_enthalpy_unit, 4, 2, 1, 1)
        self.label_entropy = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_entropy.setObjectName(_fromUtf8("label_entropy"))
        self.gridLayout_2.addWidget(self.label_entropy, 5, 0, 1, 1)
        self.entropy = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.entropy.setText(_fromUtf8(""))
        self.entropy.setReadOnly(True)
        self.entropy.setObjectName(_fromUtf8("entropy"))
        self.gridLayout_2.addWidget(self.entropy, 5, 1, 1, 1)
        self.label_entropy_unit = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_entropy_unit.setObjectName(_fromUtf8("label_entropy_unit"))
        self.gridLayout_2.addWidget(self.label_entropy_unit, 5, 2, 1, 1)
        self.label_dynamic_viscosity = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_dynamic_viscosity.setObjectName(_fromUtf8("label_dynamic_viscosity"))
        self.gridLayout_2.addWidget(self.label_dynamic_viscosity, 6, 0, 1, 1)
        self.dynamic_viscosity = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.dynamic_viscosity.setText(_fromUtf8(""))
        self.dynamic_viscosity.setReadOnly(True)
        self.dynamic_viscosity.setObjectName(_fromUtf8("dynamic_viscosity"))
        self.gridLayout_2.addWidget(self.dynamic_viscosity, 6, 1, 1, 1)
        self.label_dynamic_viscosity_unit = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_dynamic_viscosity_unit.setObjectName(_fromUtf8("label_dynamic_viscosity_unit"))
        self.gridLayout_2.addWidget(self.label_dynamic_viscosity_unit, 6, 2, 1, 1)
        self.label_kinematic_viscosity = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_kinematic_viscosity.setObjectName(_fromUtf8("label_kinematic_viscosity"))
        self.gridLayout_2.addWidget(self.label_kinematic_viscosity, 7, 0, 1, 1)
        self.kinematic_viscosity = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.kinematic_viscosity.setText(_fromUtf8(""))
        self.kinematic_viscosity.setReadOnly(True)
        self.kinematic_viscosity.setObjectName(_fromUtf8("kinematic_viscosity"))
        self.gridLayout_2.addWidget(self.kinematic_viscosity, 7, 1, 1, 1)
        self.label_kinematic_viscosity_unit = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_kinematic_viscosity_unit.setObjectName(_fromUtf8("label_kinematic_viscosity_unit"))
        self.gridLayout_2.addWidget(self.label_kinematic_viscosity_unit, 7, 2, 1, 1)
        self.label_thermal_diffusivity = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_thermal_diffusivity.setObjectName(_fromUtf8("label_thermal_diffusivity"))
        self.gridLayout_2.addWidget(self.label_thermal_diffusivity, 8, 0, 1, 1)
        self.thermal_diffusivity = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.thermal_diffusivity.setText(_fromUtf8(""))
        self.thermal_diffusivity.setReadOnly(True)
        self.thermal_diffusivity.setObjectName(_fromUtf8("thermal_diffusivity"))
        self.gridLayout_2.addWidget(self.thermal_diffusivity, 8, 1, 1, 1)
        self.label_thermal_diffusivity_unit = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_thermal_diffusivity_unit.setObjectName(_fromUtf8("label_thermal_diffusivity_unit"))
        self.gridLayout_2.addWidget(self.label_thermal_diffusivity_unit, 8, 2, 1, 1)
        self.label_thermal_conductivity = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_thermal_conductivity.setObjectName(_fromUtf8("label_thermal_conductivity"))
        self.gridLayout_2.addWidget(self.label_thermal_conductivity, 9, 0, 1, 1)
        self.thermal_conductivity = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.thermal_conductivity.setText(_fromUtf8(""))
        self.thermal_conductivity.setReadOnly(True)
        self.thermal_conductivity.setObjectName(_fromUtf8("thermal_conductivity"))
        self.gridLayout_2.addWidget(self.thermal_conductivity, 9, 1, 1, 1)
        self.label_thermal_conductivity_unit = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_thermal_conductivity_unit.setObjectName(_fromUtf8("label_thermal_conductivity_unit"))
        self.gridLayout_2.addWidget(self.label_thermal_conductivity_unit, 9, 2, 1, 1)
        self.quality = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.quality.setText(_fromUtf8(""))
        self.quality.setReadOnly(True)
        self.quality.setObjectName(_fromUtf8("quality"))
        self.gridLayout_2.addWidget(self.quality, 10, 1, 1, 1)
        self.label_quality_unit = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_quality_unit.setObjectName(_fromUtf8("label_quality_unit"))
        self.gridLayout_2.addWidget(self.label_quality_unit, 10, 2, 1, 1)
        self.label_prandtl = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_prandtl.setObjectName(_fromUtf8("label_prandtl"))
        self.gridLayout_2.addWidget(self.label_prandtl, 11, 0, 1, 1)
        self.prandtl = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.prandtl.setText(_fromUtf8(""))
        self.prandtl.setReadOnly(True)
        self.prandtl.setObjectName(_fromUtf8("prandtl"))
        self.gridLayout_2.addWidget(self.prandtl, 11, 1, 1, 1)
        self.label_prandtl_unit = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_prandtl_unit.setObjectName(_fromUtf8("label_prandtl_unit"))
        self.gridLayout_2.addWidget(self.label_prandtl_unit, 11, 2, 1, 1)
        self.label_quality = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_quality.setObjectName(_fromUtf8("label_quality"))
        self.gridLayout_2.addWidget(self.label_quality, 10, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        spacerItem1 = QtGui.QSpacerItem(618, 1, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 643, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setAcceptDrops(True)
        self.menuHelp.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menuHelp.setTearOffEnabled(False)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QtGui.QToolBar(MainWindow)
        self.toolBar_2.setObjectName(_fromUtf8("toolBar_2"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)
        self.toolBar_3 = QtGui.QToolBar(MainWindow)
        self.toolBar_3.setObjectName(_fromUtf8("toolBar_3"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_3)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionAbout_Qt = QtGui.QAction(MainWindow)
        self.actionAbout_Qt.setObjectName(_fromUtf8("actionAbout_Qt"))
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionAbout_Qt)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.input_selector, self.input1)
        MainWindow.setTabOrder(self.input1, self.input2)
        MainWindow.setTabOrder(self.input2, self.pushButton_calculate)
        MainWindow.setTabOrder(self.pushButton_calculate, self.pressure)
        MainWindow.setTabOrder(self.pressure, self.cp)
        MainWindow.setTabOrder(self.cp, self.temperature)
        MainWindow.setTabOrder(self.temperature, self.density)
        MainWindow.setTabOrder(self.density, self.enthalpy)
        MainWindow.setTabOrder(self.enthalpy, self.entropy)
        MainWindow.setTabOrder(self.entropy, self.dynamic_viscosity)
        MainWindow.setTabOrder(self.dynamic_viscosity, self.kinematic_viscosity)
        MainWindow.setTabOrder(self.kinematic_viscosity, self.thermal_diffusivity)
        MainWindow.setTabOrder(self.thermal_diffusivity, self.thermal_conductivity)
        MainWindow.setTabOrder(self.thermal_conductivity, self.quality)
        MainWindow.setTabOrder(self.quality, self.prandtl)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "H20props", None))
        self.input_selector.setItemText(0, _translate("MainWindow", "Pressure and Temperature", None))
        self.input_selector.setItemText(1, _translate("MainWindow", "Pressure and Enthalpy", None))
        self.input_selector.setItemText(2, _translate("MainWindow", "Pressure and Entropy", None))
        self.input_selector.setItemText(3, _translate("MainWindow", "Pressure and Quality", None))
        self.input_selector.setItemText(4, _translate("MainWindow", "Temperature and Quality", None))
        self.input_selector.setItemText(5, _translate("MainWindow", "Enthalpy and Entropy", None))
        self.label_input2.setText(_translate("MainWindow", "Temperature", None))
        self.input2.setText(_translate("MainWindow", "20", None))
        self.label_input2_unit.setText(_translate("MainWindow", "[C]", None))
        self.input1.setText(_translate("MainWindow", "1", None))
        self.label_input1_unit.setText(_translate("MainWindow", "[bar]", None))
        self.label_input1.setText(_translate("MainWindow", "Pressure ", None))
        self.pushButton_calculate.setText(_translate("MainWindow", "Calculate", None))
        self.label_pressure.setText(_translate("MainWindow", "Pressure", None))
        self.label_pressure_unit.setText(_translate("MainWindow", "[MPa]", None))
        self.label_cp.setText(_translate("MainWindow", "Cp", None))
        self.label_cp_unit.setText(_translate("MainWindow", "[kJ/kg K]", None))
        self.label_temperature.setText(_translate("MainWindow", "Temperature", None))
        self.label_temperature_unit.setText(_translate("MainWindow", "[K]", None))
        self.label_density.setText(_translate("MainWindow", "Density", None))
        self.label_density_unit.setText(_translate("MainWindow", "[kg/m^3]", None))
        self.label_enthalpy.setText(_translate("MainWindow", "Enthalpy", None))
        self.label_enthalpy_unit.setText(_translate("MainWindow", "[kJ/kg]", None))
        self.label_entropy.setText(_translate("MainWindow", "Entropy", None))
        self.label_entropy_unit.setText(_translate("MainWindow", "[kJ/kg K]", None))
        self.label_dynamic_viscosity.setText(_translate("MainWindow", "Dynamic viscosity", None))
        self.label_dynamic_viscosity_unit.setText(_translate("MainWindow", "[Pa s]", None))
        self.label_kinematic_viscosity.setText(_translate("MainWindow", "Kinematic viscosity", None))
        self.label_kinematic_viscosity_unit.setText(_translate("MainWindow", "[m^2/s^2]", None))
        self.label_thermal_diffusivity.setText(_translate("MainWindow", "Thermal diffusivity", None))
        self.label_thermal_diffusivity_unit.setText(_translate("MainWindow", "[m^2/s]", None))
        self.label_thermal_conductivity.setText(_translate("MainWindow", "Thermal conductivity", None))
        self.label_thermal_conductivity_unit.setText(_translate("MainWindow", "[W/m K]", None))
        self.label_quality_unit.setText(_translate("MainWindow", "[ - ]", None))
        self.label_prandtl.setText(_translate("MainWindow", "Prandtl Number", None))
        self.label_prandtl_unit.setText(_translate("MainWindow", "[ - ]", None))
        self.label_quality.setText(_translate("MainWindow", "Quality", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.toolBar_2.setWindowTitle(_translate("MainWindow", "toolBar_2", None))
        self.toolBar_3.setWindowTitle(_translate("MainWindow", "toolBar_3", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionAbout.setShortcut(_translate("MainWindow", "Ctrl+H", None))
        self.actionAbout_Qt.setText(_translate("MainWindow", "About Qt", None))

