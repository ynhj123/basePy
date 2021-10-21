import paddle
import paddle.nn as nn
from paddle.vision.transforms import Compose
from paddle.vision.transforms import Normalize
from paddle.vision.transforms import Resize


class Generator(nn.Layer):
    def __init__(self):
        super(Generator, self).__init__()
        self.gen = nn.Sequential(
            nn.Conv2DTranspose(100, 64 * 4, 4, 1, 0, bias_attr=False),
            nn.BatchNorm2D(64 * 4),
            nn.ReLU(True),
            nn.Conv2DTranspose(64 * 4, 64 * 2, 4, 2, 1, bias_attr=False),
            nn.BatchNorm2D(64 * 2),
            nn.ReLU(True),
            nn.Conv2DTranspose(64 * 2, 64, 4, 2, 1, bias_attr=False),
            nn.BatchNorm2D(64),
            nn.ReLU(True),
            nn.Conv2DTranspose(64, 1, 4, 2, 1, bias_attr=False),
            nn.Tanh()
        )

    def forward(self, x):
        return self.gen(x)


class Discriminator(nn.layer):
    def __init__(self):
        super(Discriminator, self).__init__()
        self.dis == nn.Sequential(
            nn.Conv2D(1, 64, 4, 2, 1, bias_attr=False),
            nn.LeakyReLU(0.2),
            nn.Conv2D(64, 64 * 2, 4, 2, 1, bias_attr=False),
            nn.BatchNorm2D(64 * 2),
            nn.LeakyReLU(0.2),
            nn.Conv2D(64 * 2, 64 * 4, 4, 2, 1, bias_attr=False),
            nn.BatchNorm2D(64 * 4),
            nn.LeakyReLU(0.2),
            nn.Conv2D(64 * 4, 1, 4, 1, 0, bias_attr=False),
            nn.Sigmoid()
        )

    def forward(self, x):
        return self.dis(x)


if __name__ == '__main__':
    train_dataset = paddle.vision.datasets.MNIST(mode='train',
                                                 transform=Compose([
                                                     Resize(size=(32, 32)),
                                                     Normalize(mean=[127.5], std=[127.5])
                                                 ]))
    dataloader = paddle.io.DataLoader(dataset=train_dataset, batch_size=32, shuffle=True, num_workers=4)

    for data in dataloader:
        break
    print(data[0].shape)
