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
Copyright (C) 2014

cx_Freeze setup up for creating a executable on windows.
Only tested with winpython and from inside spyder.
@author: Nicolas Edh
@email: Nicolas.Edh@gmail.com
"""
import sys
from cx_Freeze import setup, Executable
from scipy.optimize import fsolve

apptitle = "Water properties" 


base = None
if sys.platform == "win32":
    base = "Win32GUI"

includes = [
#            "H2Oprops_GUI",
#            "atexit","re",
            "iapws",
#            "numpy",
#            "scipy","scipy.optimize",
            "scipy.sparse.csgraph._validation",
            "scipy.optimize.minpack", 
            "scipy.sparse.linalg.dsolve.umfpack"]
includefiles = [
#                ("iapws.py","src/iapws.py"),
                ("LICENSE", "src/LICENSE"),
                ("H2Oprops/H2Oprops.py","src/H2Oprops.py"),
                ("H2Oprops/H2Oprops_GUI.py","src/H2Oprops_GUI.py"),
                ("H2Oprops/H2Oprops.ui","src/H2Oprops.ui")
            ]
excludes = ["tk", "_tkagg", "_gtagg", "_gtk", "tcl"]
path=sys.path
path.append("H2Oprops")
exe = Executable("H2Oprops/H2Oprops.py", base = base,
                 excludes=excludes,
#                 path = path,
#                    includes="H2Oprops_GUI", 
                 compress = True,
                 copyDependentFiles = True)

setup(
        name = apptitle,
        version = "0.1",
        description = "Water and steam properties calculator",
        options = {"build_exe" : {"includes" : includes ,
                                  "include_files" : includefiles,
                                  "path" : path,
                                  "excludes" : excludes,
                                  "bin_excludes" : excludes,
                                  "include_msvcr":[]}},
        executables = [exe])
