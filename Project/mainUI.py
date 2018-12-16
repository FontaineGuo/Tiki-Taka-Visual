# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1121, 799)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MainTabCtr = QtWidgets.QTabWidget(self.centralwidget)
        self.MainTabCtr.setGeometry(QtCore.QRect(-4, -1, 1131, 801))
        self.MainTabCtr.setIconSize(QtCore.QSize(32, 32))
        self.MainTabCtr.setObjectName("MainTabCtr")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pts_leagueBox = QtWidgets.QComboBox(self.tab)
        self.pts_leagueBox.setGeometry(QtCore.QRect(10, 30, 181, 22))
        self.pts_leagueBox.setObjectName("pts_leagueBox")
        self.pts_yearBox = QtWidgets.QComboBox(self.tab)
        self.pts_yearBox.setGeometry(QtCore.QRect(200, 30, 181, 22))
        self.pts_yearBox.setObjectName("pts_yearBox")
        self.pts_browser = QtWidgets.QTextBrowser(self.tab)
        self.pts_browser.setGeometry(QtCore.QRect(10, 70, 1071, 671))
        self.pts_browser.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pts_browser.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.pts_browser.setObjectName("pts_browser")
        self.MainTabCtr.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.ga_leagueBox = QtWidgets.QComboBox(self.tab_2)
        self.ga_leagueBox.setGeometry(QtCore.QRect(10, 30, 231, 22))
        self.ga_leagueBox.setObjectName("ga_leagueBox")
        self.ga_yearBox = QtWidgets.QComboBox(self.tab_2)
        self.ga_yearBox.setGeometry(QtCore.QRect(270, 30, 241, 22))
        self.ga_yearBox.setObjectName("ga_yearBox")
        self.ga_optionBox = QtWidgets.QComboBox(self.tab_2)
        self.ga_optionBox.setGeometry(QtCore.QRect(550, 30, 221, 22))
        self.ga_optionBox.setObjectName("ga_optionBox")
        self.ga_browser = QtWidgets.QTextBrowser(self.tab_2)
        self.ga_browser.setGeometry(QtCore.QRect(10, 80, 1091, 681))
        self.ga_browser.setObjectName("ga_browser")
        self.MainTabCtr.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_3)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(230, 180, 821, 511))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.charts_test = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.charts_test.setContentsMargins(0, 0, 0, 0)
        self.charts_test.setObjectName("charts_test")
        self.charts_show = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.charts_show.setObjectName("charts_show")
        self.charts_test.addWidget(self.charts_show)
        self.MainTabCtr.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.MainTabCtr.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.MainTabCtr.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.MainTabCtr.setTabText(self.MainTabCtr.indexOf(self.tab), _translate("MainWindow", "积分"))
        self.MainTabCtr.setTabText(self.MainTabCtr.indexOf(self.tab_2), _translate("MainWindow", "射手榜/助攻榜"))
        self.MainTabCtr.setTabText(self.MainTabCtr.indexOf(self.tab_3), _translate("MainWindow", "球队统计"))
        self.MainTabCtr.setTabText(self.MainTabCtr.indexOf(self.tab_4), _translate("MainWindow", "单场统计"))

