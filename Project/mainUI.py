# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1121, 974)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MainTabCtr = QtWidgets.QTabWidget(self.centralwidget)
        self.MainTabCtr.setGeometry(QtCore.QRect(10, 0, 1131, 971))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(16)
        self.MainTabCtr.setFont(font)
        self.MainTabCtr.setIconSize(QtCore.QSize(32, 32))
        self.MainTabCtr.setObjectName("MainTabCtr")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pts_leagueBox = QtWidgets.QComboBox(self.tab)
        self.pts_leagueBox.setGeometry(QtCore.QRect(10, 30, 181, 31))
        self.pts_leagueBox.setObjectName("pts_leagueBox")
        self.pts_yearBox = QtWidgets.QComboBox(self.tab)
        self.pts_yearBox.setGeometry(QtCore.QRect(200, 30, 181, 31))
        self.pts_yearBox.setObjectName("pts_yearBox")
        self.pts_tableView = QtWidgets.QTableView(self.tab)
        self.pts_tableView.setGeometry(QtCore.QRect(10, 80, 1071, 821))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pts_tableView.setFont(font)
        self.pts_tableView.setObjectName("pts_tableView")
        self.MainTabCtr.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.ga_leagueBox = QtWidgets.QComboBox(self.tab_2)
        self.ga_leagueBox.setGeometry(QtCore.QRect(10, 30, 231, 31))
        self.ga_leagueBox.setObjectName("ga_leagueBox")
        self.ga_yearBox = QtWidgets.QComboBox(self.tab_2)
        self.ga_yearBox.setGeometry(QtCore.QRect(270, 30, 241, 31))
        self.ga_yearBox.setObjectName("ga_yearBox")
        self.ga_optionBox = QtWidgets.QComboBox(self.tab_2)
        self.ga_optionBox.setGeometry(QtCore.QRect(550, 30, 221, 31))
        self.ga_optionBox.setObjectName("ga_optionBox")
        self.ga_tableView = QtWidgets.QTableView(self.tab_2)
        self.ga_tableView.setGeometry(QtCore.QRect(10, 80, 1131, 971))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.ga_tableView.setFont(font)
        self.ga_tableView.setObjectName("ga_tableView")
        self.MainTabCtr.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_3)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 210, 1071, 721))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.sg_charts = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.sg_charts.setContentsMargins(0, 0, 0, 0)
        self.sg_charts.setObjectName("sg_charts")
        self.charts_show = QtWidgets.QWidget(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.charts_show.sizePolicy().hasHeightForWidth())
        self.charts_show.setSizePolicy(sizePolicy)
        self.charts_show.setObjectName("charts_show")
        self.sg_charts.addWidget(self.charts_show)
        self.sg_leagueBox = QtWidgets.QComboBox(self.tab_3)
        self.sg_leagueBox.setGeometry(QtCore.QRect(40, 31, 181, 31))
        self.sg_leagueBox.setObjectName("sg_leagueBox")
        self.sg_yearBox = QtWidgets.QComboBox(self.tab_3)
        self.sg_yearBox.setGeometry(QtCore.QRect(260, 31, 201, 31))
        self.sg_yearBox.setObjectName("sg_yearBox")
        self.sg_roundBox = QtWidgets.QComboBox(self.tab_3)
        self.sg_roundBox.setGeometry(QtCore.QRect(500, 31, 221, 31))
        self.sg_roundBox.setObjectName("sg_roundBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab_3)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(140, 80, 711, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sg_homeName_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.sg_homeName_label.setFont(font)
        self.sg_homeName_label.setFrameShape(QtWidgets.QFrame.Panel)
        self.sg_homeName_label.setText("")
        self.sg_homeName_label.setPixmap(QtGui.QPixmap("C:/Users/Fontaine/.designer/DataSets/FootballIcon/British-Football-Clubs-PNG/PNG/Liverpool FC.png"))
        self.sg_homeName_label.setScaledContents(True)
        self.sg_homeName_label.setObjectName("sg_homeName_label")
        self.horizontalLayout.addWidget(self.sg_homeName_label)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.sg_awayName_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.sg_awayName_label.setFont(font)
        self.sg_awayName_label.setFrameShape(QtWidgets.QFrame.Panel)
        self.sg_awayName_label.setText("")
        self.sg_awayName_label.setPixmap(QtGui.QPixmap("C:/Users/Fontaine/.designer/DataSets/FootballIcon/British-Football-Clubs-PNG/PNG/Manchester City.png"))
        self.sg_awayName_label.setScaledContents(True)
        self.sg_awayName_label.setObjectName("sg_awayName_label")
        self.horizontalLayout.addWidget(self.sg_awayName_label)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab_3)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(250, 150, 481, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.sg_homeGoal_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.sg_homeGoal_label.setFont(font)
        self.sg_homeGoal_label.setText("")
        self.sg_homeGoal_label.setAlignment(QtCore.Qt.AlignCenter)
        self.sg_homeGoal_label.setObjectName("sg_homeGoal_label")
        self.horizontalLayout_2.addWidget(self.sg_homeGoal_label)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.sg_awayGaol_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.sg_awayGaol_label.setFont(font)
        self.sg_awayGaol_label.setText("")
        self.sg_awayGaol_label.setAlignment(QtCore.Qt.AlignCenter)
        self.sg_awayGaol_label.setObjectName("sg_awayGaol_label")
        self.horizontalLayout_2.addWidget(self.sg_awayGaol_label)
        self.sg_gameBox = QtWidgets.QComboBox(self.tab_3)
        self.sg_gameBox.setGeometry(QtCore.QRect(760, 31, 221, 31))
        self.sg_gameBox.setObjectName("sg_gameBox")
        self.sg_checkBtn = QtWidgets.QPushButton(self.tab_3)
        self.sg_checkBtn.setGeometry(QtCore.QRect(900, 90, 81, 51))
        self.sg_checkBtn.setObjectName("sg_checkBtn")
        self.MainTabCtr.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.team_leagueBox = QtWidgets.QComboBox(self.tab_4)
        self.team_leagueBox.setGeometry(QtCore.QRect(20, 20, 191, 22))
        self.team_leagueBox.setObjectName("team_leagueBox")
        self.team_teamBox = QtWidgets.QComboBox(self.tab_4)
        self.team_teamBox.setGeometry(QtCore.QRect(250, 20, 191, 22))
        self.team_teamBox.setObjectName("team_teamBox")
        self.label_7 = QtWidgets.QLabel(self.tab_4)
        self.label_7.setGeometry(QtCore.QRect(20, 60, 261, 261))
        self.label_7.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("C:/Users/Fontaine/.designer/DataSets/FootballIcon/British-Football-Clubs-PNG/PNG/Liverpool FC.png"))
        self.label_7.setObjectName("label_7")
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.tab_4)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(20, 330, 1051, 601))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget_2 = QtWidgets.QWidget(self.verticalLayoutWidget_7)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_5.addWidget(self.widget_2)
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab_4)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(330, 60, 281, 261))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 1, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 1, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 1)
        self.team_checkBtn = QtWidgets.QPushButton(self.tab_4)
        self.team_checkBtn.setGeometry(QtCore.QRect(480, 20, 71, 31))
        self.team_checkBtn.setObjectName("team_checkBtn")
        self.MainTabCtr.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.playerPhoto_lb = QtWidgets.QLabel(self.tab_5)
        self.playerPhoto_lb.setGeometry(QtCore.QRect(30, 100, 51, 51))
        self.playerPhoto_lb.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.playerPhoto_lb.setText("")
        self.playerPhoto_lb.setObjectName("playerPhoto_lb")
        self.verticalLayoutWidget_9 = QtWidgets.QWidget(self.tab_5)
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(120, 100, 201, 191))
        self.verticalLayoutWidget_9.setObjectName("verticalLayoutWidget_9")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget_9)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_7.addWidget(self.label_14)
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget_9)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_7.addWidget(self.label_15)
        self.label_20 = QtWidgets.QLabel(self.verticalLayoutWidget_9)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_7.addWidget(self.label_20)
        self.label_21 = QtWidgets.QLabel(self.verticalLayoutWidget_9)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_7.addWidget(self.label_21)
        self.verticalLayoutWidget_10 = QtWidgets.QWidget(self.tab_5)
        self.verticalLayoutWidget_10.setGeometry(QtCore.QRect(330, 100, 251, 191))
        self.verticalLayoutWidget_10.setObjectName("verticalLayoutWidget_10")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_10)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.playerName_lb = QtWidgets.QLabel(self.verticalLayoutWidget_10)
        self.playerName_lb.setText("")
        self.playerName_lb.setObjectName("playerName_lb")
        self.verticalLayout_8.addWidget(self.playerName_lb)
        self.playerCountry_lb = QtWidgets.QLabel(self.verticalLayoutWidget_10)
        self.playerCountry_lb.setText("")
        self.playerCountry_lb.setObjectName("playerCountry_lb")
        self.verticalLayout_8.addWidget(self.playerCountry_lb)
        self.playerPosition_lb = QtWidgets.QLabel(self.verticalLayoutWidget_10)
        self.playerPosition_lb.setText("")
        self.playerPosition_lb.setObjectName("playerPosition_lb")
        self.verticalLayout_8.addWidget(self.playerPosition_lb)
        self.playerPreferredFoot_lb = QtWidgets.QLabel(self.verticalLayoutWidget_10)
        self.playerPreferredFoot_lb.setText("")
        self.playerPreferredFoot_lb.setObjectName("playerPreferredFoot_lb")
        self.verticalLayout_8.addWidget(self.playerPreferredFoot_lb)
        self.verticalLayoutWidget_11 = QtWidgets.QWidget(self.tab_5)
        self.verticalLayoutWidget_11.setGeometry(QtCore.QRect(670, 100, 61, 191))
        self.verticalLayoutWidget_11.setObjectName("verticalLayoutWidget_11")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_11)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_18 = QtWidgets.QLabel(self.verticalLayoutWidget_11)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_9.addWidget(self.label_18)
        self.label_19 = QtWidgets.QLabel(self.verticalLayoutWidget_11)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_9.addWidget(self.label_19)
        self.verticalLayoutWidget_12 = QtWidgets.QWidget(self.tab_5)
        self.verticalLayoutWidget_12.setGeometry(QtCore.QRect(740, 100, 331, 191))
        self.verticalLayoutWidget_12.setObjectName("verticalLayoutWidget_12")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_12)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.playerAge_lb = QtWidgets.QLabel(self.verticalLayoutWidget_12)
        self.playerAge_lb.setText("")
        self.playerAge_lb.setObjectName("playerAge_lb")
        self.verticalLayout_10.addWidget(self.playerAge_lb)
        self.playerClub_lb = QtWidgets.QLabel(self.verticalLayoutWidget_12)
        self.playerClub_lb.setText("")
        self.playerClub_lb.setObjectName("playerClub_lb")
        self.verticalLayout_10.addWidget(self.playerClub_lb)
        self.player_CheckBtn = QtWidgets.QPushButton(self.tab_5)
        self.player_CheckBtn.setGeometry(QtCore.QRect(324, 32, 81, 31))
        self.player_CheckBtn.setObjectName("player_CheckBtn")
        self.playerName_Input = QtWidgets.QLineEdit(self.tab_5)
        self.playerName_Input.setGeometry(QtCore.QRect(130, 30, 181, 31))
        self.playerName_Input.setObjectName("playerName_Input")
        self.playerCountryPhoto_lb = QtWidgets.QLabel(self.tab_5)
        self.playerCountryPhoto_lb.setGeometry(QtCore.QRect(50, 170, 23, 17))
        self.playerCountryPhoto_lb.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.playerCountryPhoto_lb.setText("")
        self.playerCountryPhoto_lb.setObjectName("playerCountryPhoto_lb")
        self.playerClubPhoto_lb = QtWidgets.QLabel(self.tab_5)
        self.playerClubPhoto_lb.setGeometry(QtCore.QRect(620, 240, 24, 24))
        self.playerClubPhoto_lb.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.playerClubPhoto_lb.setText("")
        self.playerClubPhoto_lb.setObjectName("playerClubPhoto_lb")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab_5)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(30, 300, 481, 591))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.player_ChartOne = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.player_ChartOne.setContentsMargins(0, 0, 0, 0)
        self.player_ChartOne.setObjectName("player_ChartOne")
        self.player_ChartShow_one = QtWidgets.QWidget(self.verticalLayoutWidget_2)
        self.player_ChartShow_one.setObjectName("player_ChartShow_one")
        self.player_ChartOne.addWidget(self.player_ChartShow_one)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.tab_5)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(590, 300, 481, 591))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.player_ChartTwo = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.player_ChartTwo.setContentsMargins(0, 0, 0, 0)
        self.player_ChartTwo.setObjectName("player_ChartTwo")
        self.player_ChartShow_two = QtWidgets.QWidget(self.verticalLayoutWidget_3)
        self.player_ChartShow_two.setObjectName("player_ChartShow_two")
        self.player_ChartTwo.addWidget(self.player_ChartShow_two)
        self.MainTabCtr.addTab(self.tab_5, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.MainTabCtr.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.MainTabCtr.setTabText(self.MainTabCtr.indexOf(self.tab), _translate("MainWindow", "积分"))
        self.MainTabCtr.setTabText(self.MainTabCtr.indexOf(self.tab_2), _translate("MainWindow", "射手榜/助攻榜"))
        self.label_3.setText(_translate("MainWindow", "VS"))
        self.label_5.setText(_translate("MainWindow", ":"))
        self.sg_checkBtn.setText(_translate("MainWindow", "查询"))
        self.MainTabCtr.setTabText(self.MainTabCtr.indexOf(self.tab_3), _translate("MainWindow", "单场统计"))
        self.label_9.setText(_translate("MainWindow", "country"))
        self.label_10.setText(_translate("MainWindow", "england"))
        self.label_11.setText(_translate("MainWindow", "Liverpool"))
        self.label_8.setText(_translate("MainWindow", "Name"))
        self.team_checkBtn.setText(_translate("MainWindow", "查询"))
        self.MainTabCtr.setTabText(self.MainTabCtr.indexOf(self.tab_4), _translate("MainWindow", "球队数据"))
        self.label_14.setText(_translate("MainWindow", "name:"))
        self.label_15.setText(_translate("MainWindow", "coutry:"))
        self.label_20.setText(_translate("MainWindow", "Position:"))
        self.label_21.setText(_translate("MainWindow", "PreferredFoot:"))
        self.label_18.setText(_translate("MainWindow", "Age:"))
        self.label_19.setText(_translate("MainWindow", "club:"))
        self.player_CheckBtn.setText(_translate("MainWindow", "搜索"))
        self.MainTabCtr.setTabText(self.MainTabCtr.indexOf(self.tab_5), _translate("MainWindow", "球员"))

