# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'H2Oprops/H2Oprops.ui'
#
# Created: Thu Aug  7 15:19:44 2014
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
        MainWindow.resize(688, 709)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
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
        self.verticalLayout_3.addWidget(self.frame)
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
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 666, 504))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 688, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setAcceptDrops(True)
        self.menuHelp.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menuHelp.setTearOffEnabled(False)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
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
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionAbout.setShortcut(_translate("MainWindow", "Ctrl+H", None))
        self.actionAbout_Qt.setText(_translate("MainWindow", "About Qt", None))

