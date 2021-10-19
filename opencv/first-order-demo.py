#  Copyright (c) 2020 PaddlePaddle Authors. All Rights Reserve.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse

from first_order_prdictor import FirstOrderPredictor

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # parser.add_argument("--config", default=None, help="path to config")
    # parser.add_argument("--weight_path",
    #                     default=None,
    #                     help="path to checkpoint to restore")
    # parser.add_argument("--source_image", type=str, help="path to source image")
    # parser.add_argument("--driving_video", type=str, help="path to driving video")
    # parser.add_argument("--output", default='output', help="path to output")
    # parser.add_argument("--filename",
    #                     default='result.mp4',
    #                     help="filename to output")
    # parser.add_argument("--relative",
    #                     dest="relative",
    #                     action="store_true",
    #                     help="use relative or absolute keypoint coordinates")
    # parser.add_argument(
    #     "--adapt_scale",
    #     dest="adapt_scale",
    #     action="store_true",
    #     help="adapt movement scale based on convex hull of keypoints")
    #
    # parser.add_argument(
    #     "--find_best_frame",
    #     dest="find_best_frame",
    #     action="store_true",
    #     help=
    #     "Generate from the frame that is the most alligned with source. (Only for faces, requires face_aligment lib)"
    # )
    #
    # parser.add_argument("--best_frame",
    #                     dest="best_frame",
    #                     type=int,
    #                     default=None,
    #                     help="Set frame to start from.")
    # parser.add_argument("--cpu", dest="cpu", action="store_true", help="cpu mode.")
    # parser.add_argument("--ratio",
    #                     dest="ratio",
    #                     type=float,
    #                     default=0.4,
    #                     help="margin ratio")
    # parser.add_argument(
    #     "--face_detector",
    #     dest="face_detector",
    #     type=str,
    #     default='sfd',
    #     help="face detector to be used, can choose s3fd or blazeface")
    # parser.add_argument("--multi_person",
    #                     dest="multi_person",
    #                     action="store_true",
    #                     default=False,
    #                     help="whether there is only one person in the image or not")
    # parser.add_argument("--image_size",
    #                     dest="image_size",
    #                     type=int,
    #                     default=256,
    #                     help="size of image")
    # parser.add_argument("--batch_size",
    #                     dest="batch_size",
    #                     type=int,
    #                     default=1,
    #                     help="Batch size for fom model")
    # parser.add_argument(
    #     "--face_enhancement",
    #     dest="face_enhancement",
    #     action="store_true",
    #     help="use face enhance for face")
    # parser.add_argument(
    #     "--mobile_net",
    #     dest="mobile_net",
    #     action="store_true",
    #     help="use mobile_net for fom")
    parser.set_defaults(relative=False)
    parser.set_defaults(adapt_scale=False)
    parser.set_defaults(face_enhancement=False)
    parser.set_defaults(mobile_net=False)
    args = parser.parse_args()
    args.driving_video = 'vedios/test.avi'
    args.source_image = 'output/dst.mixing.png'
    args.relative = True
    args.adapt_scale = False
    args.output = 'output2'
    args.image_size = 512
    args.face_enhancement = True
    args.config = None
    args.weight_path = None
    args.filename = "test.mp4"
    args.find_best_frame = False
    args.best_frame = False
    args.ratio = 0.4
    args.face_detector = 'sfb'
    args.multi_person = False
    args.batch_size = 1
    args.mobile_net = False

    predictor = FirstOrderPredictor(output=args.output,
                                    filename=args.filename,
                                    weight_path=args.weight_path,
                                    config=args.config,
                                    relative=args.relative,
                                    adapt_scale=args.adapt_scale,
                                    find_best_frame=args.find_best_frame,
                                    best_frame=args.best_frame,
                                    ratio=args.ratio,
                                    face_detector=args.face_detector,
                                    multi_person=args.multi_person,
                                    image_size=args.image_size,
                                    batch_size=args.batch_size,
                                    face_enhancement=args.face_enhancement,
                                    mobile_net=args.mobile_net
                                    )
    predictor.run(args.source_image, args.driving_video)
