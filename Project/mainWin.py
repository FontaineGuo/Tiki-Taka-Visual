import sys
import mainUI
import json
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *

from mainUI import Ui_MainWindow
from data_process import getTable,config
from charts import chartsTest, singleGameGoalPie


league_name_lst = ["Premier League", "Serie A", "Ligue 1", "La Liga", "Bundesliga"]
year_lst = ["2010-2011", "2011-2012", "2012-2013", "2013-2014", "2014-2015", "2015-2016", "2016-2017", "2017-2018"]
option_lst = ["goalgetter", "assists"]

class TikiTaka(QMainWindow, Ui_MainWindow):

    def __init__(self, parent = None):
        super(QMainWindow, self).__init__(parent)
        self.setupUi(self)



        self.MainTabCtr.setCurrentIndex(0)
        self.init_specical_widget()
        self.init_pts_main()
        self.MainTabCtr.currentChanged.connect(self.main_tab_init)
        

# <----------------------------init specific widget------------------------------------------------------->
    def init_specical_widget(self):
        self.charts_show = QWebEngineView()
        for item in league_name_lst:
            self.pts_leagueBox.addItem(item)
        for item in year_lst:
            self.pts_yearBox.addItem(item)
        for item in league_name_lst:
            self.ga_leagueBox.addItem(item)
        for item in year_lst:
            self.ga_yearBox.addItem(item)
        for item in option_lst:
            self.ga_optionBox.addItem(item)

# <----------------------------init specific widget------------------------------------------------------->

# <--------------------------define the Qtabwidget function--------------------------------------------->
    def main_tab_init(self):
        tabindex = self.MainTabCtr.currentIndex()
        if tabindex == 0:
            self.init_pts_main()
        elif tabindex == 1:
            self.init_goal_assists_main()
        elif tabindex == 2:
            self.init_single_game_main()
        elif tabindex == 3:
            print(tabindex)



# <----------------------define the function of pts_ui------------------------------------------>
    def init_pts_main(self):
        self.pts_browser.setText(getTable.get_pts_table(self.pts_leagueBox.currentText(), self.pts_yearBox.currentText()))
        self.pts_leagueBox.activated.connect(self.pts_leagueBox_activate)
        self.pts_yearBox.activated.connect(self.pts_yearBox_activate)

    def pts_leagueBox_activate(self):
        # print(self.pts_leagueBox.currentText())
        #print(getPTS.get_pts('Serie A', '2010-2011'))
        self.pts_browser.setText(getTable.get_pts_table(self.pts_leagueBox.currentText(), self.pts_yearBox.currentText()))

    def pts_yearBox_activate(self):
        # print(self.pts_yearBox.currentText())
        self.pts_browser.setText(getTable.get_pts_table(self.pts_leagueBox.currentText(), self.pts_yearBox.currentText()))

# <----------------------define the function of pts_ui------------------------------------------>

# <----------------------define the function of goalgetter_assists_ui------------------------------------------>
    def init_goal_assists_main(self):

        self.ga_browser.setText(
            getTable.get_goalgetter_assists_table(self.ga_leagueBox.currentText(),
                                                  self.ga_yearBox.currentText(),
                                                  self.ga_optionBox.currentText()))

        self.ga_leagueBox.activated.connect(self.ga_leagueBox_activate)
        self.ga_yearBox.activated.connect(self.ga_yearBox_activate)
        self.ga_optionBox.activated.connect(self.ga_optionBox_activate)

    def ga_leagueBox_activate(self):
        self.ga_browser.setText(
            getTable.get_goalgetter_assists_table(self.ga_leagueBox.currentText(),
                                          self.ga_yearBox.currentText(),
                                          self.ga_optionBox.currentText()))

    def ga_yearBox_activate(self):
        self.ga_browser.setText(
            getTable.get_goalgetter_assists_table(self.ga_leagueBox.currentText(),
                                          self.ga_yearBox.currentText(),
                                          self.ga_optionBox.currentText()))

    def ga_optionBox_activate(self):
        self.ga_browser.setText(
            getTable.get_goalgetter_assists_table(self.ga_leagueBox.currentText(),
                                          self.ga_yearBox.currentText(),
                                          self.ga_optionBox.currentText()))
# <----------------------define the function of goalgetter_assists_ui------------------------------------------>
# <----------------------define the function of team_statics_ui------------------------------------------>
    def init_team_statics_main(self):
        print()

        # self.charts_show.show()


        # self.charts_test = QWebEngineView()
        # self.charts_test.load(QUrl.fromLocalFile(chartsTest.bar_test()))

        # self.setCentralWidget(self.charts_test)
        # self.charts_test.show()

# <----------------------define the function of team_statics_ui------------------------------------------>
    def init_single_game_main(self):
        self.charts_show.load(QUrl.fromLocalFile(singleGameGoalPie.single_game_goal_pie()))
        self.charts_test.addWidget(self.charts_show)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = TikiTaka()
    w.show()
    sys.exit(app.exec_())
