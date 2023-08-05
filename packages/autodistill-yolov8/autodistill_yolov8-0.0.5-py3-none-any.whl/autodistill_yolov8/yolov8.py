from autodistill.target_models import TargetModel
from ultralytics import YOLO


class YOLOv8(TargetModel):
    def __init__(self, model_name):
        self.yolo = YOLO(model_name)

    def predict(self, img_path, conf=0.2):
        return self.yolo(img_path, conf=conf)

    def train(self, dataset_yaml, epochs=300):
        self.yolo.train(data=dataset_yaml, epochs=epochs)
