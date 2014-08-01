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
@emal: nicolas.edh@gmail.com
"""

from PyQt4 import QtCore, QtGui
from H2Oprops_GUI import Ui_MainWindow
from iapws import IAPWS97 as iapws

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
        
        self.ui.input_selector.currentIndexChanged.connect(
            self.input_properties_changed)
        self.ui.pushButton_calculate.clicked.connect(
            self.calculate_values)
        self.ui.actionExit.triggered.connect(QtGui.qApp.quit)
        self.ui.actionAbout.triggered.connect(self.show_about)
        self.ui.actionAbout_Qt.triggered.connect(lambda: QtGui.QMessageBox.aboutQt(self))
        self.water=iapws(T=283,P=0.1)
        self.calculate_values(None)
        self.show()
        
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
                self.ui.input2.setText("%g" %self.water.T)
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
            self.ui.input1.setText("%g" %self.water.T)
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
        ind = self.ui.input_selector.currentIndex()
        #toFloat returns tuple (value,status)
        input1 = self.ui.input1.text().toFloat()[0]
        input2 = self.ui.input2.text().toFloat()[0]
#        input1.toFloat()
        try:
            if ind < 4:
                input1 /= 10.0 #convert bar to MPa
                if ind == 0:
                    self.water(P=input1,T=input2+273.14)
                elif ind == 1:
                    self.water(P=input1,h=input2)
                elif ind == 2:
                    self.water(P=input1,s=input2)
                elif ind == 3:
                    self.water(P=input1,x=input2)
            elif ind == 4:
                self.water(T=input1+273.14,x=input2)
            elif ind == 5:
                self.water(h=input1,s=input2)
        except NotImplementedError:
            QtGui.QMessageBox.warning(self,"Bad input",
            "You've input bad values either out of bounds or not yet implemented.",
                                      QtGui.QMessageBox.NoButton,
                                      QtGui.QMessageBox.Ok,
                                      QtGui.QMessageBox.NoButton)
        #Don't update if values are bad
        if not self.water.status:
            return
        self.ui.pressure.setText("%g" %self.water.P)
        self.ui.cp.setText("%g" %self.water.cp)
        self.ui.temperature.setText("%g" %self.water.T)
        self.ui.density.setText("%g" %self.water.rho)
        self.ui.enthalpy.setText("%g" %self.water.h)
        self.ui.entropy.setText("%g" %self.water.s)
        self.ui.dynamic_viscosity.setText("%g" %self.water.mu)
        self.ui.kinematic_viscosity.setText("%g" %self.water.nu)
        self.ui.thermal_diffusivity.setText("%g" %self.water.alfa)
        self.ui.thermal_conductivity.setText("%g" %self.water.k)
        self.ui.quality.setText("%g" %self.water.x)
        self.ui.prandtl.setText("%g" %self.water.Prandt)
        
    def show_about(self,e):
        msg = """
Calculator of water and steam properties.
GUI written by Nicolas.Edh@gmail.com.

H2Oprops is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

H2Oprops is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details. 

You should have received a copy of the GNU General Public License along with H2Oprops.  If not, see <http://www.gnu.org/licenses/>.
        """
        QtGui.QMessageBox.about(self,"About H2Oprops",msg)
    
def main():
    import sys
    app = QtGui.QApplication(sys.argv)
#    app.aboutToQuit.connect(app.deleteLater)
    calc = Calculator()
    sys.exit(app.exec_())

#def calculate_values():
        
            
if __name__ == "__main__":
    main()
