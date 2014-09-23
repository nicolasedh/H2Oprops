# -*- coding: utf-8 -*-
#This file is part of H2Oprops.
#
#    H2Oprops is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    H2Oprops is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with H2Oprops.  If not, see <http://www.gnu.org/licenses/>.
"""
GUI application for calculating water and steam properties.
Cacluations are done by using Juan José Gómez Romera's iapws97 implementation
at https://github.com/jjgomera

@author: Nicolas Edh
@email: nicolas.edh@gmail.com
"""

from PyQt4 import QtCore, QtGui
from H2Oprops_GUI import Ui_MainWindow
from iapws import IAPWS97 as iapws

def columnIdToPropertyValue(colid,water):
    if colid == 0:
        value = water.P
    elif colid == 1:
        value = water.T
    elif colid == 2:
        value = water.rho
    elif colid == 3:
        value = water.x
    elif colid == 4:
        value = water.cp
    elif colid == 5:
        value = water.h
    elif colid == 6:
        value = water.s
    elif colid == 7:
        value = water.k
    elif colid == 8:
        value = water.alfa
    elif colid == 9:
        value = water.Prandt
    elif colid == 10:
        value = water.w
    elif colid == 11:
        value = water.nu
    elif colid == 12:
        value = water.mu
    else:
        value = -1.0
    return value

class WaterTableModel(QtCore.QAbstractTableModel):
    def __init__(self, parent=None, *args):
        self.waterData = list()       
        super(WaterTableModel,self).__init__(parent,*args)
        
        #shortname, tooltip
        self.header = [
            ("P","Pressure [MPa]"),
            ("T","Temperature [K]"),
            (u"\u03C1","Density [kg/m3]"),
            ("x", "Quality [-]"),
            ("Cp", "Cp [kJ/kgK]"),
            ("h","Enthalpy [kJ/kg]"),
            ("s","Entropy [kJ/kgK]"),
            ("k","Thermal Conductivity [W/mK]"),
            (u"\u03B1","Thermal Diffusivity [m2/s]"),
            ("Pr","Prandtl number [-]"),
            ("c","Speed of Sound [m/s]"),
            (u"\u03BD","Kinematic viscosity [m2/s2]"),
            (u"\u03BC","Dynamic viscosity [Pa s]")
            ]
        
    def rowCount(self,parent=None):
        return len(self.waterData)

    def columnCount(self,parent=None):
        return len(self.header)
            
    def data(self, index, role):
        if not index.isValid():
            return QtCore.QVariant()
        elif role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()
        
        col = index.column()
        water = self.waterData[index.row()]
        
        if not water.status:
            return QtCore.QVariant(-1)
        #2do lägg till fler variabler!
        value = columnIdToPropertyValue(col,water)
            
        return QtCore.QVariant(value)
        
    def headerData(self,section, orientation, role = QtCore.Qt.DisplayRole):
        if orientation == QtCore.Qt.Horizontal:
            if role == QtCore.Qt.DisplayRole:
               return QtCore.QVariant(self.header[section][0])
            elif role == QtCore.Qt.ToolTipRole:
                return QtCore.QVariant(self.header[section][1])
        else:
            return super(WaterTableModel,self).headerData(
                        section,orientation,role)
        
    def reset_table(self):
        """ when data has been changed outside this class
            call this function. """
        self.beginResetModel()
        self.endResetModel()
        
    def removeProps(self,indeces2rem):
        objsToRem = list()
        for index in indeces2rem:
            objsToRem.append(self.waterData[index])
        
        self.beginResetModel()
        for obj in objsToRem:
            self.waterData.remove(obj)
        self.endResetModel()
        
    def addWater(self,water):
        if not water.status:
            print "invalid status"
            return
        self.beginResetModel()
        self.waterData.append(water)
        self.endResetModel()
        

class Calculator(QtGui.QMainWindow):
    
    def __init__(self):
        super(Calculator,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.positive_float_validator = QtGui.QDoubleValidator(0,1e10,20)
        self.temperature_validator = QtGui.QDoubleValidator(-273.14,1000,20)
        self.unit_validator = QtGui.QDoubleValidator(0,1,20)
        
        self.ui.input1.setValidator(self.positive_float_validator)
        self.ui.input2.setValidator(self.temperature_validator)
        
        #set up connections
        self.ui.input_selector.currentIndexChanged.connect(
            self.input_properties_changed)
        self.ui.pushButton_calculate.clicked.connect(
            self.calculate_values)
        self.ui.delButton.clicked.connect(self.delRow)
        self.ui.clearButton.clicked.connect(self.clearTable)
        self.ui.actionExit.triggered.connect(QtGui.qApp.quit)
        self.ui.actionAbout.triggered.connect(self.show_about)
        self.ui.actionAbout_Qt.triggered.connect(lambda: QtGui.QMessageBox.aboutQt(self))
        
        self.water=iapws(T=283,P=0.1)
        self.initTable()
        self.calculate_values(None)
        self.show()
    
    def initTable(self):
        self.ui.verticalLayout_2 = QtGui.QVBoxLayout(self.ui.scrollAreaWidgetContents)
        self.ui.verticalLayout_2.setObjectName("verticalLayout_2")
        
        self.waterTableModel = WaterTableModel()
        self.table = QtGui.QTableView()
        self.table.setModel(self.waterTableModel)
        self.table.setObjectName("table")
        self.table.resizeColumnsToContents()
        self.table.installEventFilter(self)
        self.ui.verticalLayout_2.addWidget(self.table)
        
    def input_properties_changed(self,e):
        ind = self.ui.input_selector.currentIndex()
        if ind < 4:
            input1 = "Pressure"
            input1_unit = "[bar]"
            self.ui.input1.setText("%g" %self.water.P)
            self.ui.input1.setValidator(self.positive_float_validator)
            if ind == 0:
                input2 = "Temperature"
                input2_unit = "[C]"
                self.ui.input2.setText("%g" %self.water.T-273.14)
                self.ui.input2.setValidator(self.temperature_validator)
            elif ind == 1:
                input2 = "Enthalpy"
                input2_unit = "[kJ/kg]"
                self.ui.input2.setText("%g" %self.water.h)
                self.ui.input2.setValidator(self.positive_float_validator)
            elif ind == 2:
                input2 = "Enthropy"
                input2_unit = "[kJ/kg K]"
                self.ui.input2.setText("%g" %self.water.s)
                self.ui.input2.setValidator(self.positive_float_validator)
            elif ind == 3:
                input2 = "Quality"
                input2_unit = "[-]"
                self.ui.input2.setText("%g" %self.water.x)
                self.ui.input2.setValidator(self.unit_validator)
        elif ind == 4:
            input1 = "Temperature"
            input1_unit = "[C]"
            self.ui.input1.setText("%g" %self.water.T-273.14)
            self.ui.input1.setValidator(self.temperature_validator)
            input2 = "Quality"
            input2_unit = "[-]"
            self.ui.input2.setText("%g" %self.water.x)
            self.ui.input2.setValidator(self.unit_validator)
        elif ind == 5:
            input1 = "Enthalpy"
            input1_unit = "[kJ/kg]"
            self.ui.input1.setText("%g" %self.water.h)
            self.ui.input1.setValidator(self.positive_float_validator)
            input2 = "Enthropy"
            input2_unit = "[kJ/kg K]"
            self.ui.input2.setText("%g" %self.water.s)
            self.ui.input2.setValidator(self.positive_float_validator)
        self.ui.label_input1.setText(input1)
        self.ui.label_input1_unit.setText(input1_unit)
        self.ui.label_input2.setText(input2)
        self.ui.label_input2_unit.setText(input2_unit)
        
    def calculate_values(self,e):
        #toFloat returns tuple (value,status)
        input1 = self.ui.input1.text().toFloat()[0]
        input2 = self.ui.input2.text().toFloat()[0]
        self.calculate_values_from_input(input1,input2)

    def calculate_values_from_input(self,input1,input2):
        ind = self.ui.input_selector.currentIndex()
        try:
            if ind < 4:
                input1 /= 10.0 #convert bar to MPa
                if ind == 0:
                    water = iapws(P=input1,T=input2+273.14)
                elif ind == 1:
                    water = iapws(P=input1,h=input2)
                elif ind == 2:
                    water = iapws(P=input1,s=input2)
                elif ind == 3:
                    water = iapws(P=input1,x=input2)
            elif ind == 4:
                water = iapws(T=input1+273.14,x=input2)
            elif ind == 5:
                water = iapws(h=input1,s=input2)
        except NotImplementedError:
            QtGui.QMessageBox.warning(self,"Bad input",
            "You've input bad values either out of bounds or not yet implemented.",
                                      QtGui.QMessageBox.NoButton,
                                      QtGui.QMessageBox.Ok,
                                      QtGui.QMessageBox.NoButton)
        #Don't update if values are bad
        if not water.status:
            return
        self.waterTableModel.addWater(water)
        
    def delRow(self):
        propsToDel = list()
        for index in self.table.selectedIndexes():
            propsToDel.append(index.row())
        self.waterTableModel.removeProps(propsToDel)

    def clearTable(self):
        numProps = self.waterTableModel.rowCount()
        self.waterTableModel.removeProps(range(numProps))
        pass
        
#        self.table.setColumnHidden(0,True)
    def show_about(self,e):
        msg = """
Calculator of water and steam properties.
GUI written by Nicolas.Edh@gmail.com.

H2Oprops is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

H2Oprops is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details. 

You should have received a copy of the GNU General Public License along with H2Oprops.  If not, see <http://www.gnu.org/licenses/>.
        """
        QtGui.QMessageBox.about(self,"About H2Oprops",msg)

    def eventFilter(self,obj,event):
        if event.__class__ == QtGui.QKeyEvent and \
            event.matches(QtGui.QKeySequence.Copy):
#            print QtGui.QApplication.clipboard().setText("hej")
#            mimeData = 
            
            QtGui.QApplication.clipboard().setMimeData(self.tableToMimeData())
#            QtGui.QKeyEvent.
        return super(Calculator,self).eventFilter(obj,event)  
        
    def tableToMimeData(self):
        selectedCells = self.table.selectedIndexes()
        selRows=list()
        selCols=list()
        for cell in selectedCells:
            selRows.append(cell.row())
            selCols.append(cell.column())
        selRows=sorted(set(selRows))
        selCols=sorted(set(selCols))
        
        data = "<!--StartFragment-->\n"
        data += "<table>"
        data += "<tr>\n"
        for col in selCols:
            data += "  <td> " 
            data += self.waterTableModel.header[col][1]
            data += "</td>"
        data += "</tr>\n" 
        
        for row in selRows:
            data += "<tr>\n"
            water = self.waterTableModel.waterData[row]
            for col in selCols:
                data += " <td> "
                data += "%g" %columnIdToPropertyValue(col,water)
                data += " </td>\n"
            data += "</tr>\n"
        data += "</table>\n"
        data += "<!--EndFragment-->\n"
        
        mimeData = QtCore.QMimeData()
        mimeData.setHtml(data)
        return mimeData
#        QtCore.QModelIndex.row()
#class copyEventFilter(QObject):
#    def eventFilter()    
def main():
    import sys
    app = QtGui.QApplication(sys.argv)
#    app.aboutToQuit.connect(app.deleteLater)
    calc = Calculator()
    sys.exit(app.exec_())
    
#def calculate_values():
        
            
if __name__ == "__main__":
    main()
