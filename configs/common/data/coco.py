from omegaconf import OmegaConf

import detectron2.data.transforms as T
from detectron2.config import LazyCall as L
from detectron2.data import (
    DatasetMapper,
    build_detection_test_loader,
    build_detection_train_loader,
    get_detection_dataset_dicts,
)
from detectron2.evaluation import COCOEvaluator

dataloader = OmegaConf.create()

dataloader.train = L(build_detection_train_loader)(
    dataset=L(get_detection_dataset_dicts)(names="ball_train"),
    mapper=L(DatasetMapper)(
        is_train=True,
        augmentations=None,
        image_format="BGR",
        use_instance_mask=True,
    ),
    total_batch_size=1,
    num_workers=1,
)

dataloader.test = L(build_detection_test_loader)(
    dataset=L(get_detection_dataset_dicts)(names="ball_test", filter_empty=False),
    mapper=L(DatasetMapper)(
        is_train=False,
        augmentations=None,
        image_format="${...train.mapper.image_format}",
    ),
    num_workers=1,
)


dataloader.evaluator = L(COCOEvaluator)(
    dataset_name="${..test.dataset.names}",
)