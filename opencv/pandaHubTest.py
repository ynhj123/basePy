import cv2
import paddlehub as hub

ori_img = "D:\\a-yongyi\\pic-chat-robot\\women\\10\\168404274_106292144899218_3576773123622578167_n.jpeg"
base_url1 = "D:\\a-yongyi\\astrology\\dycWallpaper\\static\\27.JPG"

if __name__ == '__main__':
    cv_img = cv2.imread(ori_img)
    model = hub.Module(name='animegan_v2_hayao_99', use_gpu=True)
    # 模型预测
    result = model.style_transfer(images=[cv_img], visualization=True)
    #
    model = hub.Module(name='animegan_v2_shinkai_33', use_gpu=True)
    result = model.style_transfer(images=[cv_img], visualization=True)
    #
    model = hub.Module(name='animegan_v2_paprika_74', use_gpu=True)
    result = model.style_transfer(images=[cv_img], visualization=True)
    # face_landmark = hub.Module(name="face_landmark_localization")
    # result = face_landmark.keypoint_detection(images=[cv_img], visualization=True)
    # print(result)
