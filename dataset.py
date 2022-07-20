import os

import fiftyone
import fiftyone.zoo as foz

# COCO_DATASET_YEAR can be '2014' or '2017'
COCO_DATASET_YEAR = '2017'
# COCO_DATASET_TYPE can be 'train' or 'validation'
COCO_DATASET_TYPE = 'train'
# Check below
COCO_DATASET_CLASS = 'car'
# scale of train dataset, "test dataset = 1 - train dataset"
scale_train = 0.8

dataset_name_raw = 'coco{}_{}_{}'.format(
    COCO_DATASET_YEAR, COCO_DATASET_TYPE, COCO_DATASET_CLASS)

paths = {
    'COCO_DATASET_PATH': os.path.join('fiftyone', 'coco-{}'.format(COCO_DATASET_YEAR)),
    'RESULT_PATH': os.path.join('fiftyone', 'coco-{}'.format(COCO_DATASET_YEAR), dataset_name_raw),
}
