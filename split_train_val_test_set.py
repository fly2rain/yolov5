import shutil
import argparse, os, random
from tqdm import tqdm
from utils_fyzhu import GetFileLists, OsProcess


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-src', type=str, required=True,
                        help='Input path.')

    parser.add_argument('-dst', type=str, required=True,
                        help='Output path.')

    parser.add_argument("ratio", type=str, default="0.7  0.1  0.2",
                        help="The ratio of training, validation and testing sets")

    args = parser.parse_args()

    dict0 = dict(
        src=args.src,
        dst=args.dst,
        ratio=[float(x.strip()) for x in args.ratio.split()]
    )
    return dict0


def split_train_val_test_set(src, dst, ratio):
    # 1. Get the image file list
    img_list = GetFileLists(src, interested_type="image").get_file_list_del_empty_files()
    random.shuffle(img_list)
    n_smp = len(img_list)

    # 2. Get the image list for training, validation and testing respectively.
    total_ratio = sum(ratio)
    ratio = [x / total_ratio for x in ratio]
    sep_1 = int(n_smp * ratio[0])
    sep_2 = int(n_smp * (ratio[0] + ratio[1]))
    img_list_train = img_list[:sep_1]
    img_list_valid = img_list[sep_1:sep_2]
    img_list_test = img_list[sep_2:]

    # 3. Copy the lists to destination
    copy_dataset(img_list_train, src, dst, echo="1. Moving Training Set")
    copy_dataset(img_list_valid, src, dst, echo="1. Moving Training Set")
    copy_dataset(img_list_test, src, dst, echo="1. Moving Training Set")


def copy_dataset(img_list, src, dst, echo=None):
    if echo: print(f"{echo} stage ---------------------")
    for img in tqdm(img_list):
        src_img = img
        src_txt = OsProcess.change_ext_4_filename(src_img, ".txt")
        dst_img = OsProcess().get_outName_4_givenFile_standardize_mkdir(img, src, dst, True)
        dst_txt = OsProcess().change_ext_4_filename(dst_img, ".txt")

        shutil.copy(src_img, dst_img)
        shutil.copy(src_txt, dst_txt)


def main():
    dict0 = get_parser()
    split_train_val_test_set(**dict0)


if __name__ == "__main__":
    main()