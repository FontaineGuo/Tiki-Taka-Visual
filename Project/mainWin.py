import sys
import mainUI
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import  QPixmap

from mainUI import Ui_MainWindow
from data_process import getTable,config, getJsonConfig,getDbData
from charts import singleGame, playerStatisticsOne
import requests


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
        self.init_single_game_main()
        self.init_goal_assists_main()
        # self.MainTabCtr.currentChanged.connect(self.main_tab_init)


# <----------------------------init specific widget------------------------------------------------------->
    def init_specical_widget(self):

        for item in league_name_lst:
            self.pts_leagueBox.addItem(item)
            self.ga_leagueBox.addItem(item)
            self.sg_leagueBox.addItem(item)
            self.team_leagueBox.addItem(item)
        for item in year_lst:
            self.pts_yearBox.addItem(item)
            self.ga_yearBox.addItem(item)
            self.sg_yearBox.addItem(item)

        for item in option_lst:
            self.ga_optionBox.addItem(item)

        for item in range(1,39):
            self.sg_roundBox.addItem(str(item))

        for item in getJsonConfig.select_round_gameinfo('Premier League', '2010-2011', 1):
            data = item['home'] + ' vs ' + item['away']
            self.sg_gameBox.addItem(data)

        for item in getJsonConfig.get_team_list('Premier League'):
            self.team_teamBox.addItem(item)

        # pts ui singal
        self.pts_leagueBox.activated.connect(self.pts_leagueBox_activate)
        self.pts_yearBox.activated.connect(self.pts_yearBox_activate)

        # ga ui singal
        self.ga_leagueBox.activated.connect(self.ga_leagueBox_activate)
        self.ga_yearBox.activated.connect(self.ga_yearBox_activate)
        self.ga_optionBox.activated.connect(self.ga_optionBox_activate)

        # single game singal
        self.sg_leagueBox.currentIndexChanged.connect(self.change_option)
        self.sg_roundBox.currentIndexChanged.connect(self.change_round_year)
        self.sg_yearBox.currentIndexChanged.connect(self.change_round_year)
        self.sg_checkBtn.clicked.connect(self.check_single_game)

        #team static singal
        self.team_leagueBox.currentIndexChanged.connect(self.team_leagueBox_activate)
        self.team_checkBtn.clicked.connect(self.team_check_team)
        # player data singal
        self.player_CheckBtn.clicked.connect(self.player_check)

        # init qwebviewengine
        self.charts_show = QWebEngineView()
        self.player_ChartShow_one = QWebEngineView()
        self.player_ChartShow_two = QWebEngineView()


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
        data = getTable.get_pandas_pts_table(self.pts_leagueBox.currentText(),self.pts_yearBox.currentText())
        model = getTable.PandasModel(data)
        self.pts_tableView.setModel(model)

    def pts_leagueBox_activate(self):
        data = getTable.get_pandas_pts_table(self.pts_leagueBox.currentText(),self.pts_yearBox.currentText())
        model = getTable.PandasModel(data)
        self.pts_tableView.setModel(model)

    def pts_yearBox_activate(self):
        data = getTable.get_pandas_pts_table(self.pts_leagueBox.currentText(),self.pts_yearBox.currentText())
        model = getTable.PandasModel(data)
        self.pts_tableView.setModel(model)

# <----------------------define the function of pts_ui------------------------------------------>

# <----------------------define the function of goalgetter_assists_ui------------------------------------------>
    def init_goal_assists_main(self):
        data = getTable.get_pandas_goalgetter_assists_table(self.ga_leagueBox.currentText(),
                                                            self.ga_yearBox.currentText(),
                                                            self.ga_optionBox.currentText())
        model = getTable.PandasModel(data)
        self.ga_tableView.setModel(model)




    def ga_leagueBox_activate(self):
        data = getTable.get_pandas_goalgetter_assists_table(self.ga_leagueBox.currentText(),
                                                            self.ga_yearBox.currentText(),
                                                            self.ga_optionBox.currentText())
        model = getTable.PandasModel(data)
        self.ga_tableView.setModel(model)

    def ga_yearBox_activate(self):
        data = getTable.get_pandas_goalgetter_assists_table(self.ga_leagueBox.currentText(),
                                                            self.ga_yearBox.currentText(),
                                                            self.ga_optionBox.currentText())
        model = getTable.PandasModel(data)
        self.ga_tableView.setModel(model)

    def ga_optionBox_activate(self):
        data = getTable.get_pandas_goalgetter_assists_table(self.ga_leagueBox.currentText(),
                                                            self.ga_yearBox.currentText(),
                                                            self.ga_optionBox.currentText())
        model = getTable.PandasModel(data)
        self.ga_tableView.setModel(model)
# <----------------------define the function of goalgetter_assists_ui------------------------------------------>
# <----------------------define the function of team_statics_ui------------------------------------------>
    def init_team_statics_main(self):
        print()

        # self.charts_show.show()


        # self.charts_test = QWebEngineView()
        # self.charts_test.load(QUrl.fromLocalFile(chartsTest.bar_test()))

        # self.setCentralWidget(self.charts_test)
        # self.charts_test.show()

# <----------------------define the function of single game_statics_ui------------------------------------------>
    def init_single_game_main(self):

        self.sg_checkBtn.setToolTip('查询比赛数据')

        # self.charts_show.load(QUrl.fromLocalFile(singleGameGoalPie.single_game_goal_pie()))
        # self.charts_test.addWidget(self.charts_show)

    def check_single_game(self):
        index = int(self.sg_gameBox.currentIndex())
        id = getJsonConfig.select_round_gameinfo(self.sg_leagueBox.currentText(),
                                                 self.sg_yearBox.currentText(),
                                                int(self.sg_roundBox.currentText()))[index]['id']
        data = getDbData.get_single_game_db_data(self.sg_leagueBox.currentText(),str(id))
        self.sg_homeGoal_label.setText(str(data[4]))
        self.sg_awayGaol_label.setText(str(data[5]))
        self.sg_homeName_label.setText(data[2])
        self.sg_awayName_label.setText(data[3])
        self.charts_show.load(QUrl.fromLocalFile(singleGame.single_game_goal_pie(data)))
        self.sg_charts.addWidget(self.charts_show)

    def change_option(self,i):
        self.sg_gameBox.clear()
        if i == 4:
            self.sg_roundBox.blockSignals(True)
            self.sg_yearBox.blockSignals(True)
            self.sg_roundBox.clear()
            for item in getJsonConfig.select_round_gameinfo('Bundesliga',
                                                            self.sg_yearBox.currentText(),
                                                            1):
                data = item['home'] + ' vs ' + item['away']
                self.sg_gameBox.addItem(data)
            for item in range(1, 35):
                self.sg_roundBox.addItem(str(item))
            self.sg_roundBox.blockSignals(False)
            self.sg_yearBox.blockSignals(False)
        else:
            for item in getJsonConfig.select_round_gameinfo(self.sg_leagueBox.currentText(),
                                                            self.sg_yearBox.currentText(),
                                                            int(self.sg_roundBox.currentText())):
                data = item['home'] + ' vs ' + item['away']
                self.sg_gameBox.addItem(data)

    def change_round_year(self,i):
        print('Change round year')
        self.sg_gameBox.clear()
        for item in getJsonConfig.select_round_gameinfo(self.sg_leagueBox.currentText(),
                                                        self.sg_yearBox.currentText(),
                                                        int(self.sg_roundBox.currentText())):
            data = item['home'] + ' vs ' + item['away']
            self.sg_gameBox.addItem(data)


# <----------------------define the function of single_game_statics_ui------------------------------------------>

# <-----------------------define the funcation of team season data----------------------------------------------->
    def init_team_season_main(self):
        print()

    def team_leagueBox_activate(self):
        self.team_teamBox.clear()
        for item in getJsonConfig.get_team_list(self.team_leagueBox.currentText()):
            self.team_teamBox.addItem(item)

    def team_check_team(self):
        self.teamCountry_lb.setText(config.countryDict[self.team_leagueBox.currentText()])
        self.teamName_lb.setText(self.team_teamBox.currentText())
# <-----------------------define the funcation of team season data----------------------------------------------->
# <-----------------------define the funcation of player data----------------------------------------------->
    def player_check(self):
        player = getDbData.get_player_db_data(self.playerName_Input.text())
        if len(player) == 0:
            QMessageBox.information(self, "提示", "请输入正确的球员姓名")
        else:
            self.playerName_lb.setText(player[2])
            self.playerAge_lb.setText(str(player[3]))
            self.playerClub_lb.setText(player[9])
            self.playerCountry_lb.setText(player[5])
            self.playerPosition_lb.setText(player[58])
            self.playerPreferredFoot_lb.setText(player[60])
            req = requests.get(player[4])
            req2 = requests.get(player[6])
            req3 = requests.get(player[10])

            playerPhoto = QPixmap()
            countryPhoto = QPixmap()
            clubPhoto = QPixmap()

            playerPhoto.loadFromData(req.content)
            countryPhoto.loadFromData(req2.content)
            clubPhoto.loadFromData(req3.content)

            self.playerPhoto_lb.setPixmap(playerPhoto)
            self.playerCountryPhoto_lb.setPixmap(countryPhoto)
            self.playerClubPhoto_lb.setPixmap(clubPhoto)
            self.player_ChartShow_one.load(QUrl.fromLocalFile(playerStatisticsOne.player_statistics_One(player)))
            self.player_ChartOne.addWidget(self.player_ChartShow_one)

            self.player_ChartShow_two.load(QUrl.fromLocalFile(playerStatisticsOne.player_statistics_Two(player)))
            self.player_ChartTwo.addWidget(self.player_ChartShow_two)
            # self.playerHeight_lb.setText(player[])
            # self.playerWeight_lb.setText()
# <-----------------------define the funcation of player data----------------------------------------------->
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = TikiTaka()
    w.show()
    sys.exit(app.exec_())
