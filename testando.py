from detectron2.model_zoo import get_config
from detectron2.config import LazyConfig
print(LazyConfig.to_py(get_config("common/models/mask_rcnn_vitdet.py")))