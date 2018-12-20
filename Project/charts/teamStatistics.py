from data_process import config, getDbData, getJsonConfig
from pyecharts import Bar, Page, HeatMap, Line, Timeline,Grid, Style
import datetime
import random
from collections import OrderedDict
import json

import os
current_path = os.path.dirname(__file__)
file_path = current_path + '\\teamDataVisual.html'

WIDTH = 1000
HEIGHT = 300
def team_data_visual(league, team):
    style = Style(width=WIDTH, height=HEIGHT)
    page = Page()
    table_datas = getDbData.get_team_season_data(league, team)
    game_datas = getDbData.get_team_games_data(league, team)
    season_flags = getJsonConfig.get_team_season_info(league, team)

    season_years = []
    for season in season_flags:
        temp = season.split('-')
        for t in temp:
            season_years.append(int(t))

    season_years.sort()
    season_years = set(season_years)
    season_years = list(season_years)
    season_years.sort()
    # print(season_years)

    # generate pts table
    rank_line_attr = []
    for year in season_flags:
        rank_line_attr.append(str(year))

    rank_line_data = []
    rank_markpoint_data = []
    for single_season_data, year in zip(table_datas, season_flags):
        rank_line_data.append(single_season_data[9])
        markpoint = {"coord":[], "name":""}
        temp = []
        temp.append(str(year))
        temp.append(single_season_data[9])
        markpoint["coord"] = temp
        markpoint["name"] = "排名: " + str(single_season_data[0]) + " 积分"
        rank_markpoint_data.append(markpoint)


    line = Line("积分走势", **style.init_style)
    line.add(team, rank_line_attr, rank_line_data, mark_point=rank_markpoint_data, is_toolbox_show=False, is_legend_show=False)

    # generate shot goal
    goal_lose_bar =  Bar('进球/失球', **style.init_style)
    attr = []
    goal_data = []
    lose_goal_data = []
    for single_season_data, year in zip(table_datas, season_flags):
        attr.append(year)
        goal_data.append(single_season_data[6])
        lose_goal_data.append(single_season_data[7])
    goal_lose_bar.add("进球", attr, goal_data, is_stack=True, is_toolbox_show=False)
    goal_lose_bar.add("失球", attr, lose_goal_data, is_stack=True, is_toolbox_show=False)

    # generate sh/ht
    sh_sht_bar =  Bar('射门/命中门框范围', **style.init_style)
    attr = []
    sh_data = []
    sht_data = []
    for single_season_data, year in zip(table_datas, season_flags):
        attr.append(year)
        sh_data.append(single_season_data[13])
        sht_data.append(single_season_data[14])
    sh_sht_bar.add("射门", attr, sh_data, is_stack=True, is_toolbox_show=False)
    sh_sht_bar.add("命中门框范围", attr, sht_data, is_stack=True, is_toolbox_show=False)


    # generate heatmap


    page.add(line)
    page.add(goal_lose_bar)
    page.add(sh_sht_bar)

    page.render(file_path)
    return file_path

team_data_visual('Bundesliga', 'Dortmund')