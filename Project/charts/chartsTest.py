from pyecharts import Bar
import os
current_path = os.path.dirname(__file__)

file_path = current_path + '\\test.html'
def bar_test():
    bar = Bar("我的第一个图表", "这里是副标题")
    bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
    # bar.print_echarts_options() # 该行只为了打印配置项，方便调试时使用
    bar.render(file_path)
    return file_path



