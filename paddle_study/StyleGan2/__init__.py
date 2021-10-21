import argparse

from ppgan.apps import StyleGANv2Predictor


def handler(args):
    predictor = StyleGANv2Predictor(output_path=args.output_path,
                                    weight_path=args.weight_path,
                                    model_type=args.model_type,
                                    seed=args.seed,
                                    size=args.size,
                                    style_dim=args.style_dim,
                                    n_mlp=args.n_mlp,
                                    channel_multiplier=args.channel_multiplier)
    predictor.run(args.n_row, args.n_col)


if __name__ == '__main__':
    yy_params = argparse.ArgumentParser().parse_args()

    yy_params.model_type = 'ffhq-config-f'
    yy_params.seed = 102
    yy_params.size = 1024
    yy_params.style_dim = 512
    yy_params.n_mlp = 8
    yy_params.channel_multiplier = 3
    yy_params.n_row = 1
    yy_params.n_col = 1

    yy_params.output_path = 'output'
    yy_params.weight_path = None

    handler(yy_params)
