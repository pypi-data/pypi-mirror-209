import json
import logging
import os
from collections import defaultdict

from visionai_data_format.schemas.bdd_schema import AtrributeSchema
from visionai_data_format.schemas.visionai_schema import (
    Bbox,
    DynamicObjectData,
    Frame,
    FrameInterval,
    FrameProperties,
    FramePropertyStream,
    Object,
    ObjectDataPointer,
    ObjectType,
    ObjectUnderFrame,
    Stream,
    StreamType,
    VisionAI,
)

from .calculation import xywh2xyxy, xyxy2xywh
from .validator import save_as_json, validate_vai

logger = logging.getLogger(__name__)
VERSION = "00"


def convert_vai_to_bdd(
    folder_name: str,
    company_code: int,
    sequence_name: str,
    storage_name: str,
    container_name: str,
) -> dict:
    if not os.path.exists(folder_name) or len(os.listdir(folder_name)) == 0:
        logger.info("[convert_vai_to_bdd] Folder empty or doesn't exits")
    else:
        logger.info("[convert_vai_to_bdd] Convert started")

    frame_list = list()
    for file_name in sorted(os.listdir(folder_name)):
        raw_data = open(os.path.join(folder_name, file_name)).read()
        json_format = json.loads(raw_data)
        vai_data = validate_vai(json_format).visionai
        cur_frame_list = convert_vai_to_bdd_single(
            vai_data, sequence_name, storage_name, container_name
        )
        frame_list += cur_frame_list

    data = {"frame_list": frame_list, "company_code": company_code}
    logger.info("[convert_vai_to_bdd] Convert finished")
    if not frame_list:
        logger.info("[convert_vai_to_bdd] frame_list is empty")
    return data


def convert_vai_to_bdd_single(
    vai_data: VisionAI, sequence_name: str, storage_name: str, container_name: str
) -> list:
    cur_data = {}
    cur_data["sequence"] = sequence_name
    cur_data["storage"] = storage_name
    cur_data["dataset"] = container_name

    frame_list = list()
    for frame_key, frame_data in vai_data.frames.items():
        cur_data["name"] = frame_key + ".jpg"
        labels = []
        idx = 0
        objects = getattr(frame_data, "objects", None) or {}
        for obj_id, obj_data in objects.items():
            classes = vai_data.objects.get(obj_id).type
            bboxes = obj_data.object_data.bbox or [] if obj_data.object_data else []
            for bbox in bboxes:
                geometry = bbox.val

                label = dict()
                label["category"] = classes
                label["meta_ds"] = {}
                label["meta_se"] = {}
                x1, y1, x2, y2 = xywh2xyxy(geometry)
                box2d = {"x1": x1, "y1": y1, "x2": x2, "y2": y2}
                if bbox.confidence_score is not None:
                    label["meta_ds"]["score"] = bbox.confidence_score
                label["box2d"] = box2d

                object_id = {
                    "project": "General",
                    "function": "General",
                    "object": classes,
                    "version": VERSION,
                }
                label["objectId"] = object_id
                label["attributes"] = AtrributeSchema(INSTANCE_ID=idx).dict()
                labels.append(label)
                idx += 1

        cur_data["labels"] = labels
        frame_list.append(cur_data)
    return frame_list


def convert_bdd_to_vai(bdd_data: dict, vai_dest_folder: str, sensor_name: str) -> None:
    frame_list = bdd_data.get("frame_list", None)

    if not frame_list:
        logger.info(
            "[convert_bdd_to_vai] frame_list is empty, convert_bdd_to_vai will not be executed"
        )
        return

    try:
        logger.info("[convert_bdd_to_vai] Convert started ")
        for frame in frame_list:
            name = os.path.splitext(frame["name"])[0]
            frame_idx = f"{int(name.split('.')[0]):012d}"
            labels = frame["labels"]
            meta_ds = frame.get("meta_ds", None)
            url = meta_ds["coco_url"] if meta_ds else name

            frames: dict[str, Frame] = defaultdict(Frame)
            objects: dict[str, Object] = defaultdict(Object)
            frame_data: Frame = Frame(
                objects=defaultdict(DynamicObjectData),
                frame_properties=FrameProperties(
                    streams={sensor_name: FramePropertyStream(uri=url)}
                ),
            )
            frame_intervals = [
                FrameInterval(frame_end=frame_idx, frame_start=frame_idx)
            ]

            if not labels:
                logger.info(
                    f"[convert_bdd_to_vai] No labels in this frame : {frame['name']}"
                )

            for label in labels:
                # TODO: mapping attributes to the VAI
                attributes = label["attributes"]
                attributes.pop("cameraIndex", None)
                attributes.pop("INSTANCE_ID", None)

                category = label["category"]
                obj_uuid = label["uuid"]
                x, y, w, h = xyxy2xywh(label["box2d"])
                confidence_score = label.get("meta_ds", {}).get("score", None)
                object_under_frames = {
                    obj_uuid: ObjectUnderFrame(
                        object_data=DynamicObjectData(
                            bbox=[
                                Bbox(
                                    name="bbox_shape",
                                    val=[x, y, w, h],
                                    stream=sensor_name,
                                    confidence_score=confidence_score,
                                )
                            ]
                        )
                    )
                }
                frame_data.objects.update(object_under_frames)

                objects[obj_uuid] = Object(
                    name=category,
                    type=category,
                    frame_intervals=frame_intervals,
                    object_data_pointers={
                        "bbox_shape": ObjectDataPointer(
                            type=ObjectType.bbox, frame_intervals=frame_intervals
                        )
                    },
                )
            frames[frame_idx] = frame_data
            streams = {sensor_name: Stream(type=StreamType.camera)}
            vai_data = {
                "visionai": {
                    "frame_intervals": frame_intervals,
                    "objects": objects,
                    "frames": frames,
                    "streams": streams,
                    "metadata": {"schema_version": "1.0.0"},
                }
            }
            vai_data = validate_vai(vai_data).dict(exclude_none=True)
            save_as_json(
                vai_data,
                folder_name=vai_dest_folder,
                file_name=name + ".json",
            )

        logger.info("[convert_bdd_to_vai] Convert finished")
    except Exception as e:
        logger.error("[convert_bdd_to_vai] Convert failed : " + str(e))
