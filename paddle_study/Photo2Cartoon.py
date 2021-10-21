import os

import cv2
import matplotlib.pyplot as plt
import numpy as np
from ppgan.apps import Photo2CartoonPredictor

out_one = "D:\\pyspace\\basePy\\opencv\\output\\src.fitting.png"
url = "D:\\pyspace\\basePy\\opencv\\imges\\aes.jpg"
ori_img = "D:\\a-yongyi\\pic-chat-robot\\women\\10\\168404274_106292144899218_3576773123622578167_n.jpeg"
if __name__ == '__main__':
    p2c = Photo2CartoonPredictor()
    p2c.run(ori_img)
    # # 训练数据统计
    # trainA_names = os.listdir('data/photo2cartoon/trainA')
    # print(f'训练集中真人照数据量: {len(trainA_names)}')
    #
    # trainB_names = os.listdir('data/photo2cartoon/trainB')
    # print(f'训练集中卡通画数据量: {len(trainB_names)}')
    #
    # testA_names = os.listdir('data/photo2cartoon/testA')
    # print(f'测试集中真人照数据量: {len(testA_names)}')
    #
    # testB_names = os.listdir('data/photo2cartoon/testB')
    # print(f'测试集中卡通画数据量: {len(testB_names)}')
    #
    # # 训练数据可视化
    # img_A = []
    # for img_name in np.random.choice(trainA_names, 5, replace=False):
    #     img_A.append(cv2.resize(cv2.imread('data/photo2cartoon/trainA/' + img_name), (256, 256)))
    #
    # img_B = []
    # for img_name in np.random.choice(trainB_names, 5, replace=False):
    #     img_B.append(cv2.resize(cv2.imread('data/photo2cartoon/trainB/' + img_name), (256, 256)))
    #
    # img_show = np.vstack([np.hstack(img_A), np.hstack(img_B)])[:, :, ::-1]
    # plt.figure(figsize=(20, 20))
    # plt.imshow(img_show)
    # plt.show()
