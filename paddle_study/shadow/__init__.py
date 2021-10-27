import copy
import os

import cv2
import numpy as np
import paddlehub as hub
from tqdm import tqdm

os.environ["CUDA_VISIBLE_DEVICES"] = "0"
module = hub.Module(name="deeplabv3p_xception65_humanseg")
originname = "D:\\a-yongyi\\astrology\\videoMoudle\\13.mp4"
resultname = "shadow_test.avi"

shadowcount = 9

cap = cv2.VideoCapture(originname)
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
framecount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(resultname, fourcc, fps, (width, height))

tmpres = []


def do_seg(frame):
    result = module.segmentation(images=[frame])
    return result[0]['data']


if __name__ == '__main__':
    for index in tqdm(range(framecount)):
        ret, frame = cap.read()
        if not ret:
            break
        seg_mask = np.around(do_seg(frame) / 255)
        seg_mask3 = np.repeat(seg_mask[:, :, np.newaxis], 3, axis=2)
        background = copy.deepcopy(frame)
        stbackground = copy.deepcopy(frame)
        if len(tmpres) > shadowcount:
            tmpres = tmpres[1:]
        # tmpres.append([copy.deepcopy(seg_mask3), copy.deepcopy(cv2.GaussianBlur(seg_mask3 * background,(9,9),0))])
        tmpres.append([copy.deepcopy(seg_mask3), copy.deepcopy(seg_mask3 * background)])
        thuman = copy.deepcopy(seg_mask3 * background)
        if index > len(tmpres):
            for fi, [t_mask3, t_human] in enumerate(tmpres):
                background = t_human * (fi + 1) / len(tmpres) + t_mask3 * (len(tmpres) - 1 - fi) / len(
                    tmpres) * stbackground + (1 - t_mask3) * background
        result = background.astype(np.uint8)
        out.write(result)
    cap.release()
    out.release()
