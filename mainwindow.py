# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Wed Jan 14 14:52:56 2015
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1300, 800)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.labelPathLeft = QtGui.QLabel(self.centralwidget)
        self.labelPathLeft.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.labelPathLeft.setObjectName(_fromUtf8("labelPathLeft"))
        self.verticalLayout.addWidget(self.labelPathLeft)
        self.comboBoxLeftSide = QtGui.QComboBox(self.centralwidget)
        self.comboBoxLeftSide.setObjectName(_fromUtf8("comboBoxLeftSide"))
        self.comboBoxLeftSide.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.comboBoxLeftSide)
        self.LeftEdit = QtGui.QPlainTextEdit(self.centralwidget)
        self.LeftEdit.setObjectName(_fromUtf8("LeftEdit"))
        self.verticalLayout.addWidget(self.LeftEdit)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.LeftLoadHeaderButton = QtGui.QPushButton(self.centralwidget)
        self.LeftLoadHeaderButton.setObjectName(_fromUtf8("LeftLoadHeaderButton"))
        self.horizontalLayout_3.addWidget(self.LeftLoadHeaderButton)
        self.LeftSaveHeaderButton = QtGui.QPushButton(self.centralwidget)
        self.LeftSaveHeaderButton.setObjectName(_fromUtf8("LeftSaveHeaderButton"))
        self.horizontalLayout_3.addWidget(self.LeftSaveHeaderButton)
        self.CopyToRightButton = QtGui.QPushButton(self.centralwidget)
        self.CopyToRightButton.setObjectName(_fromUtf8("CopyToRightButton"))
        self.horizontalLayout_3.addWidget(self.CopyToRightButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.labelPathRight = QtGui.QLabel(self.centralwidget)
        self.labelPathRight.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.labelPathRight.setObjectName(_fromUtf8("labelPathRight"))
        self.verticalLayout_2.addWidget(self.labelPathRight)
        self.comboBoxRightSide = QtGui.QComboBox(self.centralwidget)
        self.comboBoxRightSide.setObjectName(_fromUtf8("comboBoxRightSide"))
        self.comboBoxRightSide.addItem(_fromUtf8(""))
        self.verticalLayout_2.addWidget(self.comboBoxRightSide)
        self.RightEdit = QtGui.QPlainTextEdit(self.centralwidget)
        self.RightEdit.setObjectName(_fromUtf8("RightEdit"))
        self.verticalLayout_2.addWidget(self.RightEdit)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.CopyToLeftButton = QtGui.QPushButton(self.centralwidget)
        self.CopyToLeftButton.setObjectName(_fromUtf8("CopyToLeftButton"))
        self.horizontalLayout_4.addWidget(self.CopyToLeftButton)
        self.RightLoadHeaderButton = QtGui.QPushButton(self.centralwidget)
        self.RightLoadHeaderButton.setObjectName(_fromUtf8("RightLoadHeaderButton"))
        self.horizontalLayout_4.addWidget(self.RightLoadHeaderButton)
        self.RightSaveHeaderButton = QtGui.QPushButton(self.centralwidget)
        self.RightSaveHeaderButton.setObjectName(_fromUtf8("RightSaveHeaderButton"))
        self.horizontalLayout_4.addWidget(self.RightSaveHeaderButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addLayout(self.verticalLayout_4)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 861, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMenu = QtGui.QMenu(self.menubar)
        self.menuMenu.setObjectName(_fromUtf8("menuMenu"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionImportPresets = QtGui.QAction(MainWindow)
        self.actionImportPresets.setObjectName(_fromUtf8("actionImportPresets"))
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setSoftKeyRole(QtGui.QAction.NoSoftKey)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionExportPresets = QtGui.QAction(MainWindow)
        self.actionExportPresets.setObjectName(_fromUtf8("actionExportPresets"))
        self.actionHelp = QtGui.QAction(MainWindow)
        self.actionHelp.setObjectName(_fromUtf8("actionHelp"))
        self.menuMenu.addAction(self.actionImportPresets)
        self.menuMenu.addAction(self.actionExportPresets)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionHelp)
        #self.menuMenu.addAction(self.actionClose)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Dicom and Nifti Header Manipulator", None, QtGui.QApplication.UnicodeUTF8))
        self.labelPathLeft.setText(QtGui.QApplication.translate("MainWindow", "No file loaded", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxLeftSide.setItemText(0, QtGui.QApplication.translate("MainWindow", "None.", None, QtGui.QApplication.UnicodeUTF8))
        self.LeftLoadHeaderButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Load an image file and display its header.", None, QtGui.QApplication.UnicodeUTF8))
        self.LeftLoadHeaderButton.setText(QtGui.QApplication.translate("MainWindow", "Load Header", None, QtGui.QApplication.UnicodeUTF8))
        self.LeftSaveHeaderButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Replaces the header information of the given image file with the text above.", None, QtGui.QApplication.UnicodeUTF8))
        self.LeftSaveHeaderButton.setText(QtGui.QApplication.translate("MainWindow", "Save Header", None, QtGui.QApplication.UnicodeUTF8))
        self.CopyToRightButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Copies the header information above to right text field. Entries, which doubles, will be OVERWRITTEN.", None, QtGui.QApplication.UnicodeUTF8))
        self.CopyToRightButton.setText(QtGui.QApplication.translate("MainWindow", ">>>", None, QtGui.QApplication.UnicodeUTF8))
        self.labelPathRight.setText(QtGui.QApplication.translate("MainWindow", "No file loaded", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxRightSide.setItemText(0, QtGui.QApplication.translate("MainWindow", "None.", None, QtGui.QApplication.UnicodeUTF8))
        self.CopyToLeftButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Copies the header information above to left text field. Entries, which doubles, will be OVERWRITTEN.", None, QtGui.QApplication.UnicodeUTF8))
        self.CopyToLeftButton.setText(QtGui.QApplication.translate("MainWindow", "<<<", None, QtGui.QApplication.UnicodeUTF8))
        self.RightLoadHeaderButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Load an image file and display its header.", None, QtGui.QApplication.UnicodeUTF8))
        self.RightLoadHeaderButton.setText(QtGui.QApplication.translate("MainWindow", "Load Header", None, QtGui.QApplication.UnicodeUTF8))
        self.RightSaveHeaderButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Replaces the header information of the given image file with the text above.", None, QtGui.QApplication.UnicodeUTF8))
        self.RightSaveHeaderButton.setText(QtGui.QApplication.translate("MainWindow", "Save Header", None, QtGui.QApplication.UnicodeUTF8))
        self.menuMenu.setTitle(QtGui.QApplication.translate("MainWindow", "Menu", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImportPresets.setText(QtGui.QApplication.translate("MainWindow", "Import presets", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setText(QtGui.QApplication.translate("MainWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExportPresets.setText(QtGui.QApplication.translate("MainWindow", "Export presets", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHelp.setText(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
