"""ImageNet-100 dataset generator

Symlinks the relevant folders from the ImageNet-1K dataset into a new
ImageNet-100 dataset folder.

Original source:
https://github.com/danielchyeh/ImageNet-100-Pytorch

Ellis Brown, 2023
"""

import os
import argparse


def generate_data(imagenet_root, IN100_path, class_file):
    print("Generating ImageNet-100 dataset")
    print("================================")
    print("imagenet_root: {}".format(imagenet_root))
    print("IN100_path: {}".format(IN100_path))
    print("class_file: {}".format(class_file))
    print()

    # validate args
    if not os.path.exists(imagenet_root) or not os.path.isdir(imagenet_root):
        raise ValueError(f"imagenet_root does not exist: {imagenet_root}")
    if not os.path.exists(class_file) or not os.path.isfile(class_file):
        raise ValueError(f"class_file does not exist: {class_file}")

    f = []
    txt_data = open(class_file, "r")
    for txt in txt_data:
        s = str(txt.split("\n")[0])
        f.append(s)

    print("target classes: {}".format(f))
    print()

    for split in ["train", "val"]:
        split_dir = os.path.join(imagenet_root, split)
        if not os.path.exists(split_dir) or not os.path.isdir(split_dir):
            raise ValueError(f"split directory does not exist: {split_dir}")
        os.makedirs(os.path.join(IN100_path, split), exist_ok=True)
        for dirs in os.listdir(split_dir):
            for tg_class in f:
                if dirs == tg_class:
                    src = os.path.abspath(os.path.join(split_dir, dirs))
                    dst = os.path.abspath(os.path.join(IN100_path, split, dirs))
                    os.symlink(src, dst)
                    print(f"symlinked {src} to {dst}")


if __name__ == "__main__":
    cur_dir = os.path.dirname(os.path.abspath(__file__))

    parser = argparse.ArgumentParser("argument for generating ImageNet-100")

    parser.add_argument(
        "--imagenet_root",
        type=str,
        default="imagenet",
        help="folder of ImageNet-1K dataset",
    )
    parser.add_argument(
        "--IN100_path", type=str, default="IN100", help="folder of ImageNet-100 dataset"
    )
    parser.add_argument(
        "--class_file",
        type=str,
        default=os.path.join(cur_dir, "IN100.txt"),
        help="class file of ImageNet-100",
    )

    args = parser.parse_args()
    generate_data(args.imagenet_root, args.IN100_path, args.class_file)
