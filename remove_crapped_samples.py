import cv2
import argparse, os
from tqdm import tqdm
from utils_fyzhu import GetFileLists, OsProcess

os_process = OsProcess()


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-src', type=str, required=True, help='Input path.')
    args = parser.parse_args()
    return args.src


def remove_crapped_samples(src):
    # 1. Get the image file list
    img_list = GetFileLists(src, interested_type="image").get_file_list_del_empty_files()
    print(f"{len(img_list)} images to process")

    for img in tqdm(img_list):
        try:
            img_array = cv2.imread(img)
        except:
            print(f"Deleting: {img}")
            os.remove(img)
            txt = os_process.change_ext_4_filename(img, ".txt")
            os.remove(txt)


if __name__ == "__main__":
    src = get_parser()
    remove_crapped_samples(src)