import argparse, os, random
from tqdm import tqdm
from utils_fyzhu import GetFileLists, OsProcess

os_process = OsProcess()


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-src', type=str, required=True,
                        help='Input path.')

    parser.add_argument('-dst', type=str, required=True,
                        help='Output path.')

    parser.add_argument("-ratio", type=str, default="0.7  0.1  0.2",
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
    save_list_to_txt(img_list_train, dst, stage="Train")
    save_list_to_txt(img_list_valid, dst, stage="Validation")
    save_list_to_txt(img_list_test, dst, stage="Test")


def create_empty_label_txt_file_if_not_exit(filename):
    # check filename exist or not, if not, create an empty one
    if not filename or not os.path.exists(filename):
        f = open(filename, "w")
        f.close()


def save_list_to_txt(img_list, dst, stage="Train"):
    print(f"* Saving {stage} list to txt file ---------------------")

    dst_txt_file = os.path.join(dst, stage + ".txt")
    with open(dst_txt_file, "w") as f:
        for img in tqdm(img_list):
            src_img = img
            src_txt = os_process.change_ext_4_filename(src_img, ".txt")

            # check src_txt exist or not, if not, create an empty one
            create_empty_label_txt_file_if_not_exit(src_txt)

            f.write(f"{src_img}\n")


if __name__ == "__main__":
    dict0 = get_parser()
    split_train_val_test_set(**dict0)
