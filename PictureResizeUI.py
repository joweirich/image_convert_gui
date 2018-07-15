# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PictureResize.ui'
#
# Created: Sat Sep 13 13:28:10 2014
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

class Ui_PictureResize(object):
    def setupUi(self, PictureResize):
        PictureResize.setObjectName(_fromUtf8("PictureResize"))
        PictureResize.resize(800, 735)
        self.centralwidget = QtGui.QWidget(PictureResize)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.button_open = QtGui.QPushButton(self.centralwidget)
        self.button_open.setGeometry(QtCore.QRect(10, 20, 98, 27))
        self.button_open.setObjectName(_fromUtf8("button_open"))
        self.Close = QtGui.QPushButton(self.centralwidget)
        self.Close.setGeometry(QtCore.QRect(600, 20, 98, 27))
        self.Close.setObjectName(_fromUtf8("Close"))
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 310, 181, 41))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.ProcessDisplay = QtGui.QTextBrowser(self.centralwidget)
        self.ProcessDisplay.setGeometry(QtCore.QRect(40, 470, 571, 221))
        self.ProcessDisplay.setObjectName(_fromUtf8("ProcessDisplay"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 290, 121, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.StartBtn = QtGui.QPushButton(self.centralwidget)
        self.StartBtn.setGeometry(QtCore.QRect(10, 380, 181, 71))
        self.StartBtn.setObjectName(_fromUtf8("StartBtn"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 60, 151, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.NewFilesSaveDir = QtGui.QTextEdit(self.centralwidget)
        self.NewFilesSaveDir.setGeometry(QtCore.QRect(210, 310, 401, 41))
        self.NewFilesSaveDir.setObjectName(_fromUtf8("NewFilesSaveDir"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 290, 121, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.ChangeSaveDir = QtGui.QPushButton(self.centralwidget)
        self.ChangeSaveDir.setGeometry(QtCore.QRect(510, 280, 98, 27))
        self.ChangeSaveDir.setObjectName(_fromUtf8("ChangeSaveDir"))
        self.FileList = QtGui.QTextBrowser(self.centralwidget)
        self.FileList.setGeometry(QtCore.QRect(40, 80, 571, 191))
        self.FileList.setObjectName(_fromUtf8("FileList"))
        PictureResize.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(PictureResize)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        PictureResize.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(PictureResize)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        PictureResize.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(PictureResize)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(PictureResize)
        QtCore.QObject.connect(self.Close, QtCore.SIGNAL(_fromUtf8("clicked()")), PictureResize.close)
        QtCore.QObject.connect(self.comboBox, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.ProcessDisplay.insertPlainText)
        QtCore.QMetaObject.connectSlotsByName(PictureResize)

    def retranslateUi(self, PictureResize):
        PictureResize.setWindowTitle(_translate("PictureResize", "MainWindow", None))
        self.button_open.setText(_translate("PictureResize", "Open Files", None))
        self.Close.setText(_translate("PictureResize", "Close", None))
        self.comboBox.setItemText(0, _translate("PictureResize", "800x600", None))
        self.comboBox.setItemText(1, _translate("PictureResize", "1500x1000 ", None))
        self.comboBox.setItemText(2, _translate("PictureResize", "3000x2000 ", None))
        self.label.setText(_translate("PictureResize", "New Resolution", None))
        self.StartBtn.setText(_translate("PictureResize", "START!", None))
        self.label_2.setText(_translate("PictureResize", "Files to convert", None))
        self.NewFilesSaveDir.setToolTip(_translate("PictureResize", "enter directory or press change, default current dir", None))
        self.NewFilesSaveDir.setWhatsThis(_translate("PictureResize", "test", None))
        self.label_3.setText(_translate("PictureResize", "Saving directory", None))
        self.ChangeSaveDir.setText(_translate("PictureResize", "Change...", None))
        self.menuFile.setTitle(_translate("PictureResize", "File", None))
        self.actionQuit.setText(_translate("PictureResize", "Quit", None))

