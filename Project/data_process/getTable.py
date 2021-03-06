import csv
from data_process import config
from PyQt5 import QtCore, QtGui
import os
import prettytable as pt
import pandas as pd
current_path = os.path.dirname(__file__)

def get_pts_table(leaguename, year):
    path = config.table_root_path[leaguename]
    # csv_data = csv.reader(open(current_path + path + '\\table\\' + config.nameDict[leaguename] + '-' + year + '-table.csv' , 'r', encoding='utf-8'))
    # return path + config.nameDict[leaguename] + '-' + year + '-table.csv'
    # pts_table = ''
    # for _index, data in enumerate(csv_data):
    #     for item in data:
    #         pts_table = pts_table + ' ' + str(item)
    #     pts_table = pts_table + '\n'
    # return csv_data


    with open(current_path + path + '\\table\\' + config.nameDict[leaguename] + '-' + year + '-table.csv', "r", encoding='utf-8') as fp:
        pts_table = pt.from_csv(fp)
        pts_table.align = 'l'
        pts_table.padding_width = 0
        pts_table.set_style(pt.DEFAULT)
    pts_final_table = pts_table.get_string()

    # pts_final_table = pd.read_csv(current_path + path + '\\table\\' + config.nameDict[leaguename] + '-' + year + '-table.csv')

    return pts_final_table

def get_goalgetter_assists_table(leaguename, year, option):
    path = config.table_root_path[leaguename]
    # csv_data = csv.reader(open(current_path + path + '\\'+ option +'\\' + config.nameDict[leaguename] + '-' + year + '-'+ option + '.csv' , 'r', encoding='utf-8'))
    # return path + config.nameDict[leaguename] + '-' + year + '-table.csv'
    # goalgetter_assists_table = pt
    # for _index, data in enumerate(csv_data):
    #     if _index <= 20:
    #         for item in data:
    #             goalgetter_assists_table = goalgetter_assists_table + ' ' + str(item)
    #         goalgetter_assists_table = goalgetter_assists_table + '\n'
    # return csv_data


    with open(current_path + path + '\\'+ option +'\\' + config.nameDict[leaguename] + '-' + year + '-'+ option + '.csv', "r", encoding='utf-8') as fp:
        goalgetter_assists_table = pt.from_csv(fp)
        goalgetter_assists_table.align = 'l'
        goalgetter_assists_table.padding_width = 0
        goalgetter_assists_table.set_style(pt.DEFAULT)

    goalgetter_assists_final_table = goalgetter_assists_table.get_string( start=0, end=20)
    # goalgetter_assists_final_table = goalgetter_assists_table.get_string()
    return goalgetter_assists_final_table

class PandasModel(QtCore.QAbstractTableModel):
    def __init__(self, data, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self._data = data

    def rowCount(self, parent=None):
        return len(self._data.values)

    def columnCount(self, parent=None):
        return self._data.columns.size

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if index.isValid():
            if role == QtCore.Qt.DisplayRole:
                return QtCore.QVariant(str(
                    self._data.values[index.row()][index.column()]))
        return QtCore.QVariant()

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self._data.columns[col]
        return None

def get_pandas_pts_table(leaguename, year):
    path = config.table_root_path[leaguename]
    data = pd.read_csv(current_path + path + '\\table\\' + config.nameDict[leaguename] + '-' + year + '-table.csv')
    return data

def get_pandas_goalgetter_assists_table(leaguename, year, option):
    path = config.table_root_path[leaguename]
    data = pd.read_csv(current_path + path + '\\'+ option +'\\' + config.nameDict[leaguename] + '-' + year + '-'+ option + '.csv', nrows= 21)
    return data
# test
# print(get_pts_table('Premier League', '2010-2011'))
# print(get_goalgetter_table('Premier League', '2010-2011', 'goalgetter'))