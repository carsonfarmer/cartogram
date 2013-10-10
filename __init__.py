#-----------------------------------------------------------
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
#-----------------------------------------------------------
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
#---------------------------------------------------------------------

def name():
  return "Cartogram Creator"

def description():
  return "Create continuous cartogram"

def version():
  return "0.03"
  
def qgisMinimumVersion():
  return "1.3"

def classFactory(iface):
  from Cartogram import CartogramPlugin
  return CartogramPlugin(iface)
