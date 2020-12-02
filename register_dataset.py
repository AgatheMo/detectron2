from detectron2.data import DatasetCatalog, MetadataCatalog
from detectron2.data.datasets import register_coco_instances
register_coco_instances("COCO_test_vertebre", {}, "vertebre_data/datasets/coco/annotations/test_segmentation.json", "vertebre_data/datasets/coco/images")
register_coco_instances("COCO_train_vertebre", {}, "vertebre_data/datasets/coco/annotations/train_segmentation.json", "vertebre_data/datasets/coco/images")
COCO_vertebre_train = MetadataCatalog.get("COCO_train_vertebre")
COCO_vertebre_test = MetadataCatalog.get("COCO_test_vertebre")
