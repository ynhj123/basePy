import cv2
import matplotlib.pyplot as plt
import numpy as np

base_url1 = "D:\\a-yongyi\\astrology\\dycWallpaper\\static\\1.JPG"
base_url2 = "D:\\a-yongyi\\astrology\\dycWallpaper\\static\\2.JPG"


def gray_img(ori_img):
    print(ori_img.shape)
    image_gray = cv2.cvtColor(ori_img, cv2.COLOR_BGR2GRAY)
    ret, image_threshold = cv2.threshold(image_gray, 127, 255, cv2.THRESH_BINARY)
    cv2.imshow("img", ori_img)
    cv2.imshow("threshold", image_threshold)
    return image_threshold


def edit_pixel(ori_image):
    # 设置a
    pixel = ori_image[100, 100]  # [57 63 68],获取(100,100)处的像素值
    ori_image[100, 100] = [0, 0, 99]  # 设置像素值;
    # 设置b
    b = ori_image[100, 100, 0]  # 57, 获取(100,100)处，blue通道像素值
    g = ori_image[100, 100, 1]  # 63
    r = ori_image[100, 100, 2]  # 68
    r = ori_image[100, 100, 2] = 99  # 设置red通道值
    # 设置c
    # 获取和设置
    pixel = ori_image.item(100, 100, 2)
    ori_image.itemset((100, 100, 2), 255)
    cv2.imshow("img", ori_image)


def range_of_intercept(ori_image):
    roi = ori_image[100:200, 300:400]  # 截取100行到200行，列为300到400列的整块区域
    ori_image[50:150, 200:300] = roi  # 将截取的roi移动到该区域 （50到100行，200到300列）
    cv2.imshow("img", ori_image)
    b = ori_image[:, :, 0]  # 截取整个蓝色通道

    b, g, r = cv2.split(ori_image)  # 截取三个通道，比较耗时
    ori_image = cv2.merge((b, g, r))
    cv2.imshow("img1", ori_image)


def padding(ori_file):
    rgb_img = cv2.cvtColor(ori_file, cv2.COLOR_BGR2RGB)  # matplotlib的图像为RGB格式
    constant = cv2.copyMakeBorder(rgb_img, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=[0, 255, 0])  # 绿色
    reflect = cv2.copyMakeBorder(rgb_img, 20, 20, 20, 20, cv2.BORDER_REFLECT)
    reflect01 = cv2.copyMakeBorder(rgb_img, 20, 20, 20, 20, cv2.BORDER_REFLECT_101)
    replicate = cv2.copyMakeBorder(rgb_img, 20, 20, 20, 20, cv2.BORDER_REPLICATE)
    wrap = cv2.copyMakeBorder(rgb_img, 20, 20, 20, 20, cv2.BORDER_WRAP)
    titles = ["constant", "reflect", "reflect01", "replicate", "wrap"]
    images = [constant, reflect, reflect01, replicate, wrap]

    for i in range(5):
        plt.subplot(2, 3, i + 1), plt.imshow(images[i]), plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()


def add_mask(ori_file):
    roi_img = np.zeros(ori_file.shape[0:2], dtype=np.uint8)
    # print(img1.shape[0:2])
    roi_img[609:1827, 281:843] = 255

    img_add = cv2.add(ori_file, ori_file)
    img_add_mask = cv2.add(ori_file, ori_file, mask=roi_img)
    # cv.imshow("img1",img1)
    # cv.imshow("roi_img",roi_img)
    cv2.imshow("img_add", img_add)
    cv2.imshow("img_add_mask", img_add_mask)


def add_weighted(ori_file1, ori_file2):
    blend = cv2.addWeighted(ori_file1, 0.5, ori_file2, 0.9, 0)  # 两张图的大小和通道也应该相同
    cv2.imshow("blend", blend)


if __name__ == '__main__':
    print(cv2.__version__)
    img = cv2.imread(base_url1)
    # rows,cols,channels
    print(img.shape)  # 返回(280, 450, 3), 宽280(rows)，长450(cols)，3通道(channels)
    # size
    print(img.size)  # 返回378000，所有像素数量，=280*450*3
    # type
    print(img.dtype)  # dtype('uint8')
    # img_threshold = gray_img(img)

    #
    # cv2.imwrite("D:\\a-yongyi\\astrology\\dycWallpaper\\static\\out\\1.JPG", img_threshold)

    # edit_pixel(img)
    # range_of_intercept(img)
    # padding(img)
    # add_mask(img)
    add_weighted(img, cv2.imread(base_url2))
    key = cv2.waitKey(0)
    if key == 27:  # 按esc键时，关闭所有窗口
        print(key)
        cv2.destroyAllWindows()
