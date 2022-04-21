import os

import matplotlib.pyplot as plt
import matplotlib.dates as mdate


def plat_draw(x_arr, y_arr):
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
    plt.rcParams['axes.unicode_minus'] = False
    plt.tight_layout()
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    # 设置标题
    ax1.set_title('Scatter Plot')
    # ax1.xaxis.set_major_formatter(mdate.DateFormatter('%YYYY-%mm'))
    # 设置X轴标签
    plt.xlabel('时间')
    plt.xticks(rotation=45)
    # 设置Y轴标签
    plt.ylabel('数目')
    # 画散点图
    ax1.scatter(x_arr, y_arr, c='r', marker='o')
    # 设置图标
    plt.legend('x1')
    # 显示所画的图
    plt.show()


if __name__ == '__main__':
    x_arr = []
    y_arr = []
    for home, dirs, files in os.walk('D:\\mamaData'):
        for filename in files:
            fullname = os.path.join(home, filename)
            file = open(fullname, "r", encoding='UTF-8')
            x_arr.append(fullname.split('_')[2][0:10])
            y_arr.append(len(file.readlines()))
    myDict = {}
    for i in range(0, len(x_arr)):
        key = x_arr[i][0:7]
        value = y_arr[i]
        if key in myDict:
            myDict[key] = myDict[key] + value
        else:
            myDict[key] = value
    plat_draw(myDict.keys(), myDict.values())
