from pyecharts import Radar, Page, Style, Grid,Bar
import os
current_path = os.path.dirname(__file__)
file_path = current_path + '\\playerStatisticsOne.html'
file_path2 = current_path + '\\playerStatisticsTwo.html'

def player_statistics_One(playerData):
    style = Style(width=450, height=350)
    page = Page()

    schema_1 = [ ('Acceleration', 100), ('Aggression', 100),
               ('Agility', 100), ('Balance', 100), ('BallControl', 100)]
    v1 = [[playerData[14], playerData[15], playerData[16], playerData[17],playerData[18]]]
    skill_one_radar = Radar(**style.init_style)
    skill_one_radar.config(schema_1)
    skill_one_radar.add("", v1, is_splitline=True, is_axisline_show=True, is_toolbox_show=False,is_label_show=True, radar_text_size= 8)


    page.add(skill_one_radar)
    # grid = Grid()
    # grid.add(skill_one_radar, grid_left="30%")
    # grid.add(skill_two_radar, grid_right="30%")
    # grid.render(file_path)
    #  page.add(grid)
    page.render(file_path)
    return file_path


def player_statistics_Two(playerData):
    style = Style(width=450, height=350)
    page = Page()


    schema_2 = [ ('LongPassing', 100), ('LongShots', 100),
               ('Penalties', 100), ('ShortPassing', 100), ('Heading Accuracy', 100)]
    v2 = [[playerData[54], playerData[55], playerData[57], playerData[75],playerData[37]]]
    skill_two_radar = Radar(**style.init_style)
    skill_two_radar.config(schema_2)
    skill_two_radar.add("", v2, is_splitline=True, is_axisline_show=True, is_toolbox_show=False,is_label_show=True, radar_text_size=8)

    page.add(skill_two_radar)

    page.render(file_path2)
    return file_path2

#test
# from data_process import getDbData
# data = getDbData.get_player_db_data('L. Messi')
# player_statistics_One(data)
