from detectron2.data.datasets import register_coco_instances
register_coco_instances("COCO_test_vertebre", {}, "./vertebre_data/datasets/coco/annotations/test_segmentation.json", "./vertebre_data/datasets/coco/images")
register_coco_instances("COCO_train_vertebre", {}, "./vertebre_data/datasets/coco/annotations/train_segmentation.json", "./vertebre_data/datasets/coco/images")
