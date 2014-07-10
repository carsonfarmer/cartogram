# ----------------------------------------------------------------------------
#
# Cartogram Creator
#
# A QGIS plugin for creating cartograms based on polygon
# shapefile. Uses algorithm proposed in:
#     Dougenik, J. A, N. R. Chrisman, and D. R. Niemeyer. 1985.
#     "An algorithm to construct continuous cartograms."
#     Professional Geographer 37:75-81
#
# This plugin uses python code adapted from Eric Wolfs pyCartogram.py
# See plugin about dialog for more information.
#
# EMAIL: carson.farmer (at) gmail.com
# WEB  : www.carsonfarmer.com
#
# ----------------------------------------------------------------------------
#
# licensed under the terms of GNU GPL 2
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# ----------------------------------------------------------------------------

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *

import resources
import doCartogram

# Missing QString with Python 3.X
try:
    from PyQt4.QtCore import QString
except ImportError:
    # we are using Python3 so QString is not defined
    QString = str


class CartogramPlugin:

    def __init__(self, iface):
        # Save a reference to the QGIS iface
        self.iface = iface

    def initGui(self):
        # Create projection action
        self.action = QAction(QIcon(":/cartogram.png"),
                              "Cartogram Creator",
                              self.iface.mainWindow()
                              )
        self.action.setWhatsThis("Tool for creating rubber-sheet cartogram")
        QObject.connect(self.action, SIGNAL("activated()"), self.run)
        # Create about button
        self.helpaction = QAction(QIcon(":/cartogramhelp.png"),
                                  "About",
                                  self.iface.mainWindow()
                                  )
        self.helpaction.setWhatsThis("Help for Cartogram Creator")
        QObject.connect(self.helpaction, SIGNAL("activated()"), self.helprun)

        # Add to the main toolbar
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("&Cartogram Creator", self.action)
        self.iface.addPluginToMenu("&Cartogram Creator", self.helpaction)

        # connect to signal renderComplete which is emitted when canvas
        # rendering is done
        QObject.connect(self.iface.mapCanvas(),
                        SIGNAL("renderComplete(QPainter *)"),
                        self.render
                        )

    def unload(self):
        # Remove the plugin
        self.iface.removePluginMenu("&Cartogram Creator", self.action)
        self.iface.removePluginMenu("&Cartogram Creator", self.helpaction)
        self.iface.removeToolBarIcon(self.action)
        QObject.disconnect(self.iface.mapCanvas(),
                           SIGNAL("renderComplete(QPainter *)"),
                           self.render
                           )

    def helprun(self):
        # print "Help pressed..."
        infoString = QString("Written by Carson Farmer\n"
                             "carson.farmer@gmail.com\n")
        infoString = infoString.append("www.geog.uvic.ca/spar/carson\n")
        infoString = infoString.append("Code adapted from Eric Wolfs "
                                       "pyCartogram.py\n\n"
                                       "This tool creates a new shapefile "
                                       "based on the input shapefile with "
                                       "each polygon vertex shifted. "
                                       "Should be called iteratively to get "
                                       "the results desired.\n")
        infoString = infoString.append("Based on a translation of Andy "
                                       "Agenda's ESRI ArcScript for "
                                       "contiguous cartograms:\n"
                                       "http://arcscripts.esri.com/details.asp"
                                       "?dbid=10509\n"
                                       )
        infoString = infoString.append("He based the routine on Charles B. "
                                       "Jackel's script in:\n"
                                       "'Using ArcView to Create Contiguous "
                                       "and Noncontiguous Area Cartograms,'"
                                       "Cartography and Geographic "
                                       "Information Systems, vol. 24, no. 2, "
                                       "1997, pp. 101-109\n"
                                       )
        infoString = infoString.append("Charles B. Jackel based his script on "
                                       "the method proposed in:\n"
                                       "Dougenik, J. A, N. R. Chrisman, and "
                                       "D. R. Niemeyer. 1985. 'An algorithm "
                                       "to construct continuous cartograms.' "
                                       "Professional Geographer 37:75-81"
                                       )
        QMessageBox.information(self.iface.mainWindow(),
                                "About Cartogram Creator",
                                infoString
                                )

    def run(self):
        d = doCartogram.Dialog(self.iface)
        d.exec_()

    def render(self, painter):
        pass
