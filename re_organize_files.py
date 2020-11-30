# Re-organize the files to easily test in Yolov5 enverinoment
# Author:  Feiyun Zhu,   feiyun.zhu@samsclub.com
# Date:  11/12/2020

import argparse
from tqdm import tqdm
import random, shutil
from pathlib import Path
from utils_fyzhu import GetFileLists, OsProcess


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--src', type=str, required=True, help='Input path.')
    parser.add_argument('--dst', type=str, required=True, help='Output path.')
    parser.add_argument("--num", type=int, default=1e20, help="The number of Selected Images.")
    parser.add_argument("--mode", type=str, default="cp", help="cp or mv?")
    parser.add_argument("--filetype", type=str, default="image", help="image, txt, video or *.txt")
    args = parser.parse_args()

    dict0 = dict(
        src=args.src,
        dst=args.dst,
        num=args.num,
        mode=args.mode,
        filetype=args.filetype)
    return dict0


def get_file_list(src, filetype: str = "image"):
    src = Path(src)
    if src.is_dir():  # get the img_list in the directory
        file_list = GetFileLists(src, interested_type=filetype).get_file_list_del_empty_files()
    elif src.is_file() and src.suffix == ".txt":  # get the img_list in the *.txt file
        with open(src, "r") as f:
            file_list = f.readlines()
        file_list = [x.strip("\n") for x in file_list]
    else:
        raise ValueError(f"src: {src}, should be a directory or a *.txt file!")
    return file_list


def deal_selected_files_2_dst(dst, file_list, mode: str = "cp"):
    dst_path = Path(dst)
    if not dst_path.exists():
        dst_path.mkdir(parents=True)

    for img in tqdm(file_list):
        img_path = Path(img)
        dst_filename = dst_path / img_path.name
        # print(f"src={img_path}\tdst={dst_filename}")
        # input()
        # print(mode)
        if mode == "cp":
            shutil.copy2(img_path, dst_filename)
        else:
            img_path.rename(dst_filename)


def re_organize_files(src, dst, num: int = 1e20, mode: str = "cp", filetype: str = "image"):
    # 1. Get the image file list
    file_list = get_file_list(src, filetype)

    # 2. Select the randomly selected image files.
    random.seed(0)
    random.shuffle(file_list)
    num = min(num, len(file_list))
    file_list = file_list[:num]

    # 3. Copy the selected files to dst
    deal_selected_files_2_dst(dst, file_list, mode)


if __name__ == "__main__":
    dict0 = get_parser()
    re_organize_files(**dict0)
