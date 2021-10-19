import argparse

import paddle
import Styleganv2fitting_predictor

ori_img = "D:\\a-yongyi\\pic-chat-robot\\women\\10\\168404274_106292144899218_3576773123622578167_n.jpeg"
img2 = "D:\\a-yongyi\\pic-chat-robot\\women\\21\\166077933_10219908557440132_2638627150030183501_n.jpeg"


def fitting(params):
    paddle.set_device("gpu")
    predictor = Styleganv2fitting_predictor.StyleGANv2FittingPredictor(
        output_path=params.output_path,
        weight_path=params.weight_path,
        model_type=params.model_type,
        seed=None,
        size=params.size,
        style_dim=params.style_dim,
        n_mlp=params.n_mlp,
        channel_multiplier=params.channel_multiplier)
    predictor.run(params.input_image,
                  need_align=params.need_align,
                  start_lr=params.start_lr,
                  final_lr=params.final_lr,
                  latent_level=params.latent_level,
                  step=params.step,
                  mse_weight=params.mse_weight,
                  pre_latent=params.pre_latent)


if __name__ == '__main__':
    yy_params = argparse.ArgumentParser().parse_args()
    yy_params.input_image = "imges/img_1.png"
    yy_params.need_align = False
    yy_params.start_lr = 0.1
    yy_params.final_lr = 0.025
    yy_params.latent_level = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    yy_params.step = 100
    yy_params.mse_weight = 1
    yy_params.output_path = 'output'
    yy_params.model_type = 'ffhq-config-f'
    yy_params.size = 1024
    yy_params.style_dim = 1024
    yy_params.n_mlp = 4
    yy_params.channel_multiplier = 2

    yy_params.weight_path = None
    yy_params.pre_latent = None
    fitting(yy_params)
