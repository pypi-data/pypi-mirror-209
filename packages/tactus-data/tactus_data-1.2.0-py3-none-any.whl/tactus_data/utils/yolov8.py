from typing import Union, Tuple, List
from pathlib import Path

import numpy as np
import torch
import cv2

from ultralytics import YOLO
from ultralytics.yolo.engine.results import Results
from ultralytics.nn.autobackend import AutoBackend
from ultralytics.yolo.utils import downloads
from ultralytics.yolo.utils.torch_utils import select_device
from ultralytics.yolo.utils.ops import non_max_suppression, scale_boxes, scale_coords
from ultralytics.yolo.data.augment import LetterBox

from tactus_data.utils.skeleton import Skeleton


class Yolov8:
    """custom interface to the yolov8 models"""
    def __init__(self, model_dir: Path, model_name: str, device: str, half: bool = False) -> None:
        """
        instanciate the model.

        Parameters
        ----------
        model_dir : Path
            directory where to find the model weights.
        model_name : str
            name of the model. Must be one of those: "yolov8n-pose.pt",
            "yolov8s-pose.pt", "yolov8m-pose.pt", "yolov8l-pose.pt",
            "yolov8x-pose.pt", "yolov8x-pose-p6.pt", "yolov8n.pt",
            "yolov8s.pt", "yolov8m.pt", "yolov8l.pt", "yolov8x.pt"
        device : str
            the device name to run the model on.
        half : bool, optional
            use half precision (float16) forthe model, by default False
        """
        self.device = select_device(device)
        self.half = half
        self.model_name = model_name
        self.model = AutoBackend(model_dir / model_name, device=self.device, fp16=half)
        self.model.eval()

    @classmethod
    def download_weights(cls, model_dir: Path, model_name: str):
        """
        download weights for a given model name to a specified directory.

        Parameters
        ----------
        model_dir : Path
            directory to save the model weights.
        model_name : str
            name of the model weights to download.
        """
        if model_name not in model_name_to_url:
            raise ValueError("invalid model name. Must be in ", ", ".join(model_name_to_url.keys()))

        url = model_name_to_url[model_name]
        downloads.safe_download(url, dir=model_dir)

    def _preprocess_img(self, img: Union[Path, np.ndarray]) -> Tuple[torch.Tensor, Tuple, Tuple]:
        """
        pad and transform an image to a tensor. Also compute the origin
        image size and the new size.

        Parameters
        ----------
        img : Union[Path, np.ndarray]
            image Path or numpy array reprenting the image.

        Returns
        -------
        Tuple[torch.Tensor, Tuple, Tuple]
            (
                tensor of shape [n_samples, 3, img_height, img_width],
                (original image height, original image width),
                (new image height, new image width),
            )
        """
        img = load_image(img)
        img0_size = img.shape[:2]
        img = correct_img_size(img, self.model.stride)
        img_size = img.shape[1:]
        imgs = img_to_tensor(img, self.device, self.half)

        return imgs, img0_size, img_size

    def predict(self, images: torch.Tensor) -> List[torch.Tensor]:
        """
        predict on a tensor containing single or multiple images.

        Parameters
        ----------
        images : torch.Tensor
            tensor of shape [n_samples, 3, img_height, img_width]

        Returns
        -------
        List[torch.Tensor]
            result tensor for each image.
        """
        with torch.no_grad():
            return self.model(images)


class BboxPredictionYolov8(Yolov8):
    """yolov8 interface to extract human bboxes from an image"""
    def __call__(self, img: Union[Path, np.ndarray]) -> List[Skeleton]:
        return self.predict(img)

    def predict(self, img: Union[Path, np.ndarray]) -> List[Skeleton]:
        """
        extract the bounding boxes from a given image.

        Parameters
        ----------
        img : Union[Path, np.ndarray]
            path to an image, or a numpy array representing the image.

        Returns
        -------
        Dict[str, List]
            return a dictionnary with
            - `bboxes` list containing every (x1, y1, x2, y2) coordinates.
            - `scores` list the score for each bounding box.
        """
        if "pose" in self.model_name:
            raise ValueError("wrong model selected. You can't predict bounding boxes "
                             "with a pose-prediction model.")

        _img, img0_size, img_size = self._preprocess_img(img)
        preds = super().predict(_img)
        preds = non_max_suppression(preds, conf_thres=0.25, iou_thres=0.45, classes=[0], max_det=300, max_time_img=5)

        results_skeleton = []
        for pred in preds:
            # scale the prediction back to the input image size
            pred[:, :4] = scale_boxes(img_size, pred[:, :4], img0_size).round()
            for det in pred:
                skeleton = Skeleton(bbox_lbrt=det[:4].tolist(),
                                    score=det[4].tolist())

                results_skeleton.append(skeleton)

        return results_skeleton


class PosePredictionYolov8(Yolov8):
    """yolov8 interface to extract pose from an image"""
    def __call__(self, img: Union[Path, np.ndarray]) -> List[Skeleton]:
        return self.predict(img)

    def predict(self, img: Union[Path, np.ndarray]) -> List[Skeleton]:
        """
        extract the skeletons from a given image.

        Parameters
        ----------
        img : Union[Path, np.ndarray]
            path to an image, or a numpy array representing the image.

        Returns
        -------
        Dict[str, List]
            return a dictionnary with
            - `bboxes` list containing every (x1, y1, x2, y2) coordinates.
            - `scores` list the score for each bounding box.
            - `keypoints` list containing (x1, y1, is_visible) coordinates.
        """
        if "pose" not in self.model_name:
            raise ValueError("wrong model selected. You can't predict poses"
                             "without a pose-prediction model.")

        _img, img0_size, img_size = self._preprocess_img(img)

        preds = super().predict(_img)
        preds = non_max_suppression(preds, conf_thres=0.25, iou_thres=0.7, classes=None, max_det=300, nc=1, max_time_img=5)

        results_skeleton = []
        for pred in preds:
            if pred == []:
                continue
            # scale the prediction back to the input image size
            pred[:, :4] = scale_boxes(img_size, pred[:, :4], img0_size).round()
            pred_kpts = pred[:, 6:].view(len(pred), *(17, 3))
            pred_kpts = scale_coords(img_size, pred_kpts, img0_size).round()

            for i, det in enumerate(pred):
                skeleton = Skeleton(bbox_lbrt=det[:4].tolist(),
                                    score=det[4].tolist(),
                                    keypoints=pred_kpts[i].tolist())
                results_skeleton.append(skeleton)

        return results_skeleton


def correct_img_size(img: np.ndarray, stride: int, imgsize: int = 640) -> np.ndarray:
    """
    pad the image if it does not have the correct size.

    Parameters
    ----------
    img : np.ndarray
        numpy array representing the image.
    stride : int
        stride to apply.

    Returns
    -------
    np.ndarray
        new resized image.
    """
    img = LetterBox(imgsize, auto=True, stride=stride)(image=img)
    img = img.transpose((2, 0, 1))[::-1]
    img = np.ascontiguousarray(img)

    return img


def img_to_tensor(img: np.ndarray, device: torch.device, half: bool) -> torch.Tensor:
    """
    convert a numpy image to a tensor

    Parameters
    ----------
    img : np.ndarray
         numpy array representing the image.
    device : torch.device
        the torch device to store the tensor on.
    half : bool
        whether or not to use half precision.

    Returns
    -------
    torch.Tensor
        tensor of shape [n_samples, 3, img_height, img_width] storing the images.
    """
    img = torch.from_numpy(img).to(device)
    img = img.half() if half else img.float()  # uint8 to fp16/32
    img /= 255.0  # 0 - 255 to 0.0 - 1.0
    if len(img.shape) == 3:
        img = img[None]  # expand for batch dim

    return img


def load_image(image: Union[Path, np.ndarray]) -> np.ndarray:
    """
    load the image from a Path, or do nothing if it is a numpy array.

    Parameters
    ----------
    image : Union[Path, np.ndarray]
        image Path or numpy array reprenting the image.

    Returns
    -------
    np.ndarray
        numpy array representing the image.
    """
    if isinstance(image, Path):
        return cv2.imread(str(image))

    return image


class Yolo(YOLO):
    """raw interface to the yolov8 model."""
    def __init__(self, model_dir: Path, model_name: str, device: str, half: bool = False) -> None:
        super().__init__(model_dir / model_name)
        self.to(device)

    def predict(self, img: Union[Path, np.ndarray]) -> List[Skeleton]:
        """
        extract the skeletons from a given image.

        Parameters
        ----------
        img : Union[Path, np.ndarray]
            path to an image, or a numpy array representing the image.

        Returns
        -------
        Dict[str, List]
            return a dictionnary with
            - `bboxes` list containing every (x1, y1, x2, y2) coordinates.
            - `scores` list the score for each bounding box.
            - `keypoints` list containing (x1, y1, is_visible) coordinates.
        """
        resultss: List[Results] = super().predict(img)

        results_skeleton = []
        for results in resultss:
            bboxes = results.boxes
            keypoints = results.keypoints

            for i_result in range(len(bboxes)):
                print(bboxes[i_result])
                bbox_lbrt = bboxes[i_result][:4]
                score = bboxes[i_result][4]
                skeleton_keypoints = keypoints[i_result]

                skeleton = Skeleton(bbox_lbrt=bbox_lbrt,
                                    score=score,
                                    keypoints=skeleton_keypoints)

                results_skeleton.append(skeleton)

        return results_skeleton


model_name_to_url = {
    "yolov8n-pose.pt": "https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n-pose.pt",
    "yolov8s-pose.pt": "https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8s-pose.pt",
    "yolov8m-pose.pt": "https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8m-pose.pt",
    "yolov8l-pose.pt": "https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8l-pose.pt",
    "yolov8x-pose.pt": "https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8x-pose.pt",
    "yolov8x-pose-p6.pt": "https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8x-pose-p6.pt",
    "yolov8n.pt": "https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt",
    "yolov8s.pt": "https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8s.pt",
    "yolov8m.pt": "https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8m.pt",
    "yolov8l.pt": "https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8l.pt",
    "yolov8x.pt": "https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8x.pt",
}
