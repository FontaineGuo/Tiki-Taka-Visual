import sys
import mainUI
import json
from PyQt5.QtWidgets import QApplication, QMainWindow
from mainUI import Ui_MainWindow
from data_process import getPTS,config

class TikiTaka(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super(QMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.init_pts_main()

    def init_pts_main(self):
        league_name_lst = ["Premier League", "Serie A", "Ligue 1", "La Liga", "Bundesliga"]
        year_lst = ["2010-2011","2011-2012", "2012-2013","2013-2014","2014-2015","2015-2016","2016-2017"
                    ,"2017-2018"]
        self.pts_browser.setText("")
        self.pts_leagueBox.activated.connect(self.pts_leagueBox_activate)
        self.pts_yearBox.activated.connect(self.pts_yearBox_activate)
        for item in league_name_lst:
            self.pts_leagueBox.addItem(item)
        for item in year_lst:
            self.pts_yearBox.addItem(item)


# <----------------------define the function of pts_ui------------------------------------------>
    def pts_leagueBox_activate(self):
        print(self.pts_leagueBox.currentText())
        #print(getPTS.get_pts('Serie A', '2010-2011'))
        self.pts_browser.setText(getPTS.get_pts(self.pts_leagueBox.currentText(), self.pts_yearBox.currentText()))

    def pts_yearBox_activate(self):
        print(self.pts_yearBox.currentText())
        self.pts_browser.setText(getPTS.get_pts(self.pts_leagueBox.currentText(), self.pts_yearBox.currentText()))
    # 显示积分表
    def show_pts(self):
        print()
# <----------------------define the function of pts_ui------------------------------------------>
    def init_goal_assists_main(self):
        print()

    def init_team_statics_main(self):
        print()

    def init_single_game_main(self):
        print()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = TikiTaka()
    w.show()
    sys.exit(app.exec_())
