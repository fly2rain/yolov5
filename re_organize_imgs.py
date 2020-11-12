import argparse
from tqdm import tqdm
import random, shutil
from pathlib import Path
from utils_fyzhu import GetFileLists, OsProcess

os_process = OsProcess()


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--src', type=str, required=True, help='Input path.')
    parser.add_argument('--dst', type=str, required=True, help='Output path.')
    parser.add_argument("--num", type=int, default=1e20, help="The number of Selected Images.")
    args = parser.parse_args()

    dict0 = dict(
        src=args.src,
        dst=args.dst,
        num=args.num
    )
    return dict0


def re_organize_imgs(src, dst, num):
    # 1. Get the image file list
    src = Path(src)
    if src.is_dir():
        img_list = GetFileLists(src, interested_type="image").get_file_list_del_empty_files()
    elif src.is_file():
        with open(src, "r") as f:
            img_list = f.readlines()

    random.seed(0)
    random.shuffle(img_list)
    num = min(num, len(img_list))
    img_list = img_list[:num]

    dst_path = Path(dst)
    for img in tqdm(img_list):
        img_path = Path(img)
        dst_filename = dst_path / img_path.name
        shutil.copy(img, dst_filename)


if __name__ == "__main__":
    dict0 = get_parser()
    re_organize_imgs(**dict0)
