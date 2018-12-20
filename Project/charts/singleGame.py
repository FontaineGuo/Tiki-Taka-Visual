from pyecharts import Pie, Page, Style, Grid,Bar

import os
current_path = os.path.dirname(__file__)
file_path = current_path + '\\singleGameGoalPie.html'

WIDTH = 1000
HEIGHT = 300

def single_game_goal_pie(game_data):


    style = Style(width=WIDTH, height=HEIGHT )
    page = Page()
    chart = Pie('射门统计(主队/客队)',
                title_pos='left', **style.init_style)
    chart.add(game_data[2], ["门框范围外", "门框范围"], [game_data[10]-game_data[12], game_data[12]], center=[30, 50], radius=[40, 75],
              label_pos='left', is_legend_show= False,is_label_show=True, label_text_color=None, is_toolbox_show=False)
    chart.add(game_data[3], ["门框范围外", "门框范围"], [game_data[11]-game_data[13], game_data[13]], center=[75, 50], radius=[40, 75],
              label_pos='right', is_legend_show=False, is_label_show=True, label_text_color=None, is_toolbox_show=False)

    page.add(chart)
    attr = ['角球','犯规','黄牌','红牌']
    v1 = [game_data[16], game_data[14], game_data[18], game_data[20]]
    v2 = [game_data[17], game_data[13], game_data[19], game_data[21]]
    bar = Bar("本场数据统计", **style.init_style)
    bar.add(game_data[2], attr, v1, is_stack=False, is_toolbox_show=False)
    bar.add(game_data[3], attr, v2, is_stack=False, is_toolbox_show=False)
    page.add(bar)
    # grid = Grid()
    # # grid.add(chart, grid_top="25%")
    # grid.add(bar, grid_bottom="60%")
    # grid.add(chart, grid_top="100%")
    #
    # grid.render(file_path)
    page.render(file_path)

    return file_path

# test
# from data_process import getDbData
#
# data = getDbData.get_single_game_db_data('Serie A','2')
# print(data)
# data = getDbData.get_single_game_db_data('Premier League','2')
# print(data)
# # single_game_goal_pie(data)