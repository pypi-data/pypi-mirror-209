import glob
import os
import random
import shutil
import subprocess
import sys
import urllib.request

import cv2
import numpy as np
import supervision as sv
import torch
import yaml
from PIL import Image
from supervision import Detections

HOME = os.path.expanduser("~")
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

if not torch.cuda.is_available():
    print("WARNING: CUDA not available. GroundingDINO will run very slowly.")


def combine_detections(detections_list, overwrite_class_ids):
    if len(detections_list) == 0:
        return Detections.empty()

    if overwrite_class_ids is not None and len(overwrite_class_ids) != len(
        detections_list
    ):
        raise ValueError(
            "Length of overwrite_class_ids must match the length of detections_list."
        )

    xyxy = []
    mask = []
    confidence = []
    class_id = []
    tracker_id = []

    for idx, detection in enumerate(detections_list):
        xyxy.append(detection.xyxy)

        if detection.mask is not None:
            mask.append(detection.mask)

        if detection.confidence is not None:
            confidence.append(detection.confidence)

        if detection.class_id is not None:
            if overwrite_class_ids is not None:
                # Overwrite the class IDs for the current Detections object
                class_id.append(
                    np.full_like(
                        detection.class_id, overwrite_class_ids[idx], dtype=np.int64
                    )
                )
            else:
                class_id.append(detection.class_id)

        if detection.tracker_id is not None:
            tracker_id.append(detection.tracker_id)

    xyxy = np.vstack(xyxy)
    mask = np.vstack(mask) if mask else None
    confidence = np.hstack(confidence) if confidence else None
    class_id = np.hstack(class_id) if class_id else None
    tracker_id = np.hstack(tracker_id) if tracker_id else None

    return Detections(
        xyxy=xyxy,
        mask=mask,
        confidence=confidence,
        class_id=class_id,
        tracker_id=tracker_id,
    )


def load_grounding_dino():
    grounding_dino_path = os.path.join(HOME, "GroundingDINO")
    sys.path.append(grounding_dino_path)

    GROUNDING_DINO_CONFIG_PATH = os.path.join(
        HOME, "GroundingDINO/groundingdino/config/GroundingDINO_SwinT_OGC.py"
    )
    GROUNDING_DINO_CHECKPOINT_PATH = os.path.join(
        HOME, "weights", "groundingdino_swint_ogc.pth"
    )
    CHECKPOINT_DIR = os.path.join(HOME, "weights")

    try:
        import groundingdino
        from groundingdino.util.inference import Model

        grounding_dino_model = Model(
            model_config_path=GROUNDING_DINO_CONFIG_PATH,
            model_checkpoint_path=GROUNDING_DINO_CHECKPOINT_PATH,
        )
        return grounding_dino_model
    except:
        # install groundingdino
        print("attempting auto-install of Grounding DINO...")
        REPO_URL = "https://github.com/IDEA-Research/GroundingDINO.git"
        REPO_DIR = os.path.join(HOME, "GroundingDINO")

        # Clone the repository
        with open(os.devnull, "w") as devnull:
            subprocess.run(
                ["git", "clone", REPO_URL], cwd=HOME, stdout=devnull, stderr=devnull
            )
            # Checkout the specific hash
            subprocess.run(
                ["git", "checkout", "39b1472457b8264adc8581d354bb1d1956ec7ee7"],
                cwd=REPO_DIR,
                stdout=devnull,
                stderr=devnull,
            )
            # Install the package in editable mode
            subprocess.run(
                ["pip", "install", "-q", "-e", "."],
                cwd=REPO_DIR,
                stdout=devnull,
                stderr=devnull,
            )
            
            #re-upgrade supervision
            subprocess.run(
                ["pip", "install", "-q", "--upgrade", "supervision"],
                cwd=REPO_DIR,
                stdout=devnull,
                stderr=devnull,
            )

        if not os.path.exists(CHECKPOINT_DIR):
            os.makedirs(CHECKPOINT_DIR)
        GROUNDING_DINO_CHECKPOINT_PATH = os.path.join(
            CHECKPOINT_DIR, "groundingdino_swint_ogc.pth"
        )
        if not os.path.exists(GROUNDING_DINO_CHECKPOINT_PATH):
            url = "https://github.com/IDEA-Research/GroundingDINO/releases/download/v0.1.0-alpha/groundingdino_swint_ogc.pth"
            urllib.request.urlretrieve(url, GROUNDING_DINO_CHECKPOINT_PATH)

        try:
            import groundingdino
            from groundingdino.util.inference import Model
        except:
            raise("Failed to import groundingdino after installation. If you are in Google Colab, you must restart the runtime and run this cell again.")

        grounding_dino_model = Model(
            model_config_path=GROUNDING_DINO_CONFIG_PATH,
            model_checkpoint_path=GROUNDING_DINO_CHECKPOINT_PATH,
        )

        grounding_dino_model.to(DEVICE)

        return grounding_dino_model


def split_data(base_dir, split_ratio=0.8):
    images_dir = os.path.join(base_dir, "images")
    annotations_dir = os.path.join(base_dir, "annotations")

    # Correct the image file names if they have an extra dot before the extension
    for file in os.listdir(images_dir):
        if file.count(".") > 1:
            new_file_name = file.replace("..", ".")
            os.rename(
                os.path.join(images_dir, file), os.path.join(images_dir, new_file_name)
            )

    # Convert .png and .jpeg images to .jpg
    for file in os.listdir(images_dir):
        if file.endswith(".png"):
            img = Image.open(os.path.join(images_dir, file))
            rgb_img = img.convert("RGB")
            rgb_img.save(os.path.join(images_dir, file.replace(".png", ".jpg")))
            os.remove(os.path.join(images_dir, file))
        if file.endswith(".jpeg"):
            img = Image.open(os.path.join(images_dir, file))
            rgb_img = img.convert("RGB")
            rgb_img.save(os.path.join(images_dir, file.replace(".jpeg", ".jpg")))
            os.remove(os.path.join(images_dir, file))

    # Get list of all files (removing the image file extension)
    all_files = os.listdir(images_dir)
    all_files = [os.path.splitext(f)[0] for f in all_files if f.endswith(".jpg")]

    # Shuffle the files
    random.shuffle(all_files)

    # Compute the splitting index
    split_idx = int(len(all_files) * split_ratio)

    # Split the files
    train_files = all_files[:split_idx]
    valid_files = all_files[split_idx:]

    # Make directories for train and valid
    train_dir = os.path.join(base_dir, "train")
    valid_dir = os.path.join(base_dir, "valid")
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(valid_dir, exist_ok=True)

    # Make images and labels subdirectories
    train_images_dir = os.path.join(train_dir, "images")
    train_labels_dir = os.path.join(train_dir, "labels")
    valid_images_dir = os.path.join(valid_dir, "images")
    valid_labels_dir = os.path.join(valid_dir, "labels")
    os.makedirs(train_images_dir, exist_ok=True)
    os.makedirs(train_labels_dir, exist_ok=True)
    os.makedirs(valid_images_dir, exist_ok=True)
    os.makedirs(valid_labels_dir, exist_ok=True)

    # Move the files
    for file in train_files:
        shutil.move(os.path.join(images_dir, file + ".jpg"), train_images_dir)
        shutil.move(os.path.join(annotations_dir, file + ".txt"), train_labels_dir)

    for file in valid_files:
        shutil.move(os.path.join(images_dir, file + ".jpg"), valid_images_dir)
        shutil.move(os.path.join(annotations_dir, file + ".txt"), valid_labels_dir)

    # Load the existing YAML file to get the names
    with open(os.path.join(base_dir, "data.yaml"), "r") as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
        names = data["names"]

    # Rewrite the YAML file
    with open(os.path.join(base_dir, "data.yaml"), "w") as file:
        data = {
            "train": os.path.abspath(base_dir) + "/train/images",
            "val": os.path.abspath(base_dir) + "/valid/images",
            "nc": len(names),
            "names": names,
        }
        yaml.dump(data, file)
