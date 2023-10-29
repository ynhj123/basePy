import os
import shutil

src_file_path = "D:\\ptotoshop\\ebs_test\\video"
dst_file_path = "D:\\ptotoshop\\ebs_test\\video1"
start_index = 1
suffix_file = ".png"


def rename_files():
    i = 1
    os.makedirs(dst_file_path, exist_ok=True)
    for filename in os.listdir(src_file_path):
        if filename.endswith(suffix_file):
            # os.rename(os.path.join(src_file_path, filename), os.path.join(directory, f"{i:03}" + suffix_file))
            shutil.copy(os.path.join(src_file_path, filename), os.path.join(dst_file_path, f"{i:03}" + suffix_file))
            i += 1


if __name__ == '__main__':
    rename_files()
