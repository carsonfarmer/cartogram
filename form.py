# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created: Mon Mar 24 20:22:18 2014
#      by: PyQt4 UI code generator 4.10.3
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setWindowModality(QtCore.Qt.NonModal)
        Dialog.resize(374, 317)
        icon = QtGui.QIcon()
        icon.addFile(_fromUtf8("centroids.png"))
        Dialog.setWindowIcon(icon)
        Dialog.setSizeGripEnabled(True)
        self.gridlayout = QtGui.QGridLayout(Dialog)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridlayout.addWidget(self.label_3, 0, 0, 1, 2)
        self.inShape = QtGui.QComboBox(Dialog)
        self.inShape.setObjectName(_fromUtf8("inShape"))
        self.gridlayout.addWidget(self.inShape, 1, 0, 1, 2)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridlayout.addWidget(self.label_4, 2, 0, 1, 2)
        self.inFields = QtGui.QComboBox(Dialog)
        self.inFields.setObjectName(_fromUtf8("inFields"))
        self.gridlayout.addWidget(self.inFields, 3, 0, 1, 2)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridlayout.addWidget(self.label_2, 4, 0, 1, 2)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.outShape = QtGui.QLineEdit(Dialog)
        self.outShape.setReadOnly(True)
        self.outShape.setObjectName(_fromUtf8("outShape"))
        self.hboxlayout.addWidget(self.outShape)
        self.toolOut = QtGui.QToolButton(Dialog)
        self.toolOut.setObjectName(_fromUtf8("toolOut"))
        self.hboxlayout.addWidget(self.toolOut)
        self.gridlayout.addLayout(self.hboxlayout, 5, 0, 1, 2)
        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setObjectName(_fromUtf8("hboxlayout1"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.hboxlayout1.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem)
        self.spnIterations = QtGui.QSpinBox(Dialog)
        self.spnIterations.setProperty("value", 5)
        self.spnIterations.setObjectName(_fromUtf8("spnIterations"))
        self.hboxlayout1.addWidget(self.spnIterations)
        self.gridlayout.addLayout(self.hboxlayout1, 6, 0, 1, 2)
        self.chkKeep = QtGui.QCheckBox(Dialog)
        self.chkKeep.setChecked(True)
        self.chkKeep.setObjectName(_fromUtf8("chkKeep"))
        self.gridlayout.addWidget(self.chkKeep, 7, 0, 1, 2)
        spacerItem1 = QtGui.QSpacerItem(356, 31, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridlayout.addItem(spacerItem1, 8, 0, 1, 2)
        self.txtProgress = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtProgress.sizePolicy().hasHeightForWidth())
        self.txtProgress.setSizePolicy(sizePolicy)
        self.txtProgress.setMinimumSize(QtCore.QSize(113, 20))
        self.txtProgress.setText(_fromUtf8(""))
        self.txtProgress.setObjectName(_fromUtf8("txtProgress"))
        self.gridlayout.addWidget(self.txtProgress, 9, 0, 1, 1)
        self.buttonBox_2 = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox_2.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox_2.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.NoButton|QtGui.QDialogButtonBox.Ok)
        self.buttonBox_2.setObjectName(_fromUtf8("buttonBox_2"))
        self.gridlayout.addWidget(self.buttonBox_2, 9, 1, 1, 1)
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setAlignment(QtCore.Qt.AlignHCenter)
        self.progressBar.setTextVisible(False)
        self.progressBar.setFormat(_fromUtf8(""))
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.gridlayout.addWidget(self.progressBar, 10, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox_2, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox_2, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Generate Centroids", None))
        self.label_3.setText(_translate("Dialog", "Input Shapefile:", None))
        self.label_4.setText(_translate("Dialog", "Area Field:", None))
        self.label_2.setText(_translate("Dialog", "Output Shapefile:", None))
        self.toolOut.setText(_translate("Dialog", "Browse", None))
        self.label.setText(_translate("Dialog", "Number of iterations to perform:", None))
        self.chkKeep.setText(_translate("Dialog", "Keep intermediate shapefiles", None))

