from pyecharts import Pie, Page, Style, Grid

import os
current_path = os.path.dirname(__file__)
file_path = current_path + '\\singleGameGoalPie.html'

WIDTH = 300
HEIGHT = 300

def single_game_goal_pie():

    style = Style(width=WIDTH, height=HEIGHT )

    chart = Pie('进球射门统计(主队/客队)', "数据来源于网络",
                title_pos='left', **style.init_style)
    chart.add("主队", ["射门", "门框范围"], [25, 75], center=[20, 50], radius=[18, 24],rosetype='area',
              label_pos='left', is_legend_show= False,is_label_show=True, label_text_color=None, is_toolbox_show=False)
    chart.add("客队", ["射门", "门框范围"], [3, 1], center=[70, 50], radius=[18, 24], rosetype='area',
              label_pos='left', is_legend_show=False, is_label_show=True, label_text_color=None, is_toolbox_show=False)

    grid = Grid()
    grid.add(chart, grid_bottom="60%")
    grid.render(file_path)

    return file_path