
# ImageNet-100 dataset generator

Creates an ImageNet-100 dataset using the randomly selected 100 classes  of ImageNet from [Tian (2020)](https://arxiv.org/abs/1906.05849).

Symlinks the relevant folders from the ImageNet-1K dataset into a new
ImageNet-100 dataset folder. No need to duplicate the data.

Original source:
https://github.com/danielchyeh/ImageNet-100-Pytorch


## Usage

```bash
python generate_imagenet_IN100.py \
    --imagenet_root /path/to/imagenet \
    --IN100_path /path/to/IN100 \
    --class_file /path/to/IN100/IN100.txt
```
