#   Copyright (c) 2020 PaddlePaddle Authors. All Rights Reserve.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
import numpy as np
import cv2
from styleganv2mixing_predictor import StyleGANv2MixingPredictor
import paddle

out_one = "D:\\pyspace\\basePy\\opencv\\output\\src.fitting.png"
out_two = "D:\\pyspace\\basePy\\opencv\\output1\\src.fitting.png"
out_one_npy = "D:\\pyspace\\basePy\\opencv\\output\\dst.fitting.npy"
out_two_npy = "D:\\pyspace\\basePy\\opencv\\output1\\dst.fitting.npy"

def mixing(args):
    predictor = StyleGANv2MixingPredictor(
        output_path=args.output_path,
        weight_path=args.weight_path,
        model_type=args.model_type,
        seed=None,
        size=args.size,
        style_dim=args.style_dim,
        n_mlp=args.n_mlp,
        channel_multiplier=args.channel_multiplier)
    predictor.run(args.latent1, args.latent2, args.weights)


if __name__ == "__main__":
    # np.save("output\\a.npy", np.array(cv2.imread(out_one)))
    # np.save("output\\b.npy", np.array(cv2.imread(out_one)))
    args = argparse.ArgumentParser().parse_args()
    args.latent1 = out_one_npy
    args.latent2 = out_two_npy

    args.weights = [0.5] * 18
    args.output_path = 'output2'

    args.model_type = 'ffhq-config-f'
    args.size = 1024
    args.style_dim = 512
    args.n_mlp = 8
    args.channel_multiplier = 2

    args.weight_path = None

    mixing(args)
