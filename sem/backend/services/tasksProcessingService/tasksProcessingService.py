from models import Task
import os
import cv2
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator, colors
import shutil
from sqlalchemy.orm import Session

from services.db.parts import create_part
from services.db.results import create_result
from services.db.results import add_parts_to_result
from services.db.tasks import change_status

from models.tasks import StatusEnum

import settings


class TasksProcessingService:

    def __init__(self):
        self.detector = YOLO(settings.DETECTOR_MODEL_PATH)
        self.classificator = YOLO(settings.CLASSIFICATOR_MODEL_PATH)

        self.conf_detection = settings.DETECTION_CONF
        self.conf_classification = settings.CLASSIFICATION_CONF

        self.classificator_target_size = settings.CLASSIFICATOR_IMAGE_SIZE

    def process(self, task: Task, session: Session):

        change_status(session, task, StatusEnum.at_work)

        result_parts_dict, output_file_path = self.predict_on_img(task.file_path)

        for part_name in result_parts_dict.keys():
            create_part(session, part_name)

        result = create_result(session, task.id, file_in=task.file_path, out=output_file_path)

        for part_name in result_parts_dict.keys():
            add_parts_to_result(session, result, part_name, result_parts_dict[part_name])

        change_status(session, task, StatusEnum.finished)

        print("NEW TASK FINISHED")

    def classify_part(self, img):
        result_classification = self.classificator.predict(img, verbose=False)
        highest_prob_idx = result_classification[0].probs.top1
        prob = result_classification[0].probs.top1conf

        return highest_prob_idx, prob

    def predict_on_img(self, img_path, save_result_img=True):

        im0 = cv2.imread(img_path)
        class_names = self.classificator.names

        parts_dict = {}

        results = self.detector.predict(im0, show=False, conf=self.conf_detection, save=False, verbose=False)

        boxes = results[0].boxes.xyxy.cpu().tolist()
        probs = results[0].boxes.conf.cpu().tolist()

        output_img = im0.copy()
        annotator = Annotator(output_img, line_width=2, example=class_names)

        idx = 0
        if boxes is not None:
            for box, prob_detection in zip(boxes, probs):
                idx += 1
                crop_obj = im0[int(box[1]): int(box[3]), int(box[0]): int(box[2])]
                crop_obj = cv2.resize(crop_obj, self.classificator_target_size)

                part_class_index, prob = self.classify_part(crop_obj)

                part_class_name = class_names[part_class_index]

                if prob >= self.conf_classification:
                    if part_class_name in parts_dict.keys():
                        parts_dict[part_class_name] += 1
                    else:
                        parts_dict[part_class_name] = 1

                    if save_result_img:
                        annotator.box_label(box, color=colors(int(part_class_index), True),
                                            label=f"{part_class_name} {prob_detection:.1f} {prob:.1f}")

        if save_result_img:
            # annotator.display_analytics(output_img, parts_dict, (0, 0, 0), (255, 255, 255), 2)

            cv2.imwrite(f"./results/{img_path.split('.')[-2].split('/')[-1]}_output.png", output_img)

        return parts_dict, f"./results/{img_path.split('.')[-2].split('/')[-1]}_output.png"
