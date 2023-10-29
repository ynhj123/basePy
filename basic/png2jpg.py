from PIL import Image
import os

src_file_path = "D:\\download\\EbSynth-Beta-Win\\EbsTest\\video"
dst_file_path = "D:\\download\\EbSynth-Beta-Win\\EbsTest\\video1"


if __name__ == '__main__':
    # Call the function with the path to your directory
    for filename in os.listdir(src_file_path):
        if filename.endswith(".png"):
            img = Image.open(os.path.join(src_file_path, filename))
            rgb_img = img.convert('RGB')
            rgb_img.save(os.path.join(src_file_path, filename[:-4] + '.jpg'), "JPEG")
