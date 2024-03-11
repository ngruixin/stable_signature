import fiftyone.zoo as foz


dataset = foz.load_zoo_dataset(
    "coco-2017",
    splits=["train", "validation", "test"],
    label_types=["detections", "segmentations"],
    classes=["person"],
    # max_samples=50,
)

