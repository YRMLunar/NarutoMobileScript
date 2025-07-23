import cv2
import numpy as np

class DBPostProcess:
    def __init__(self, thresh=0.2, box_thresh=0.1, max_candidates=1000, unclip_ratio=1.6):
        self.thresh = thresh
        self.box_thresh = box_thresh
        self.max_candidates = max_candidates
        self.unclip_ratio = unclip_ratio

    def __call__(self, pred, bitmap=None, original_shape=None):
        pred = pred[0][0]
        if bitmap is None:
            bitmap = pred > self.thresh
        boxes, scores = self._extract_boxes(bitmap, pred, original_shape)
        return boxes, scores

    def _extract_boxes(self, bitmap, pred, original_shape):
        height, width = bitmap.shape
        boxes = []
        scores = []

        contours, _ = cv2.findContours((bitmap * 255).astype(np.uint8), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours[:self.max_candidates]:
            epsilon = 0.01 * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)

            if len(approx) < 4:
                continue

            box = approx.reshape(-1, 2).astype(np.float32)
            score = self.box_score_fast(pred, box)
            if score < self.box_thresh:
                continue

            box = self.unclip(box)
            if len(box) < 1:
                continue

            box = np.array(box).reshape(-1, 2)
            box[:, 0] = np.clip(np.round(box[:, 0]), 0, width)
            box[:, 1] = np.clip(np.round(box[:, 1]), 0, height)
            if self.is_valid_box(box):
                boxes.append(box.astype(np.int32))
                scores.append(score)
        return boxes, scores

    def box_score_fast(self, bitmap, box):
        h, w = bitmap.shape
        mask = np.zeros((h, w), dtype=np.uint8)
        cv2.fillPoly(mask, [np.round(box).astype(np.int32)], 1)
        return cv2.mean(bitmap, mask)[0]

    def unclip(self, box):
        from shapely.geometry import Polygon
        import pyclipper

        poly = Polygon(box)
        if poly.area <= 1:
            return []
        distance = poly.area * self.unclip_ratio / poly.length
        offset = pyclipper.PyclipperOffset()
        offset.AddPath(box, pyclipper.JT_ROUND, pyclipper.ET_CLOSEDPOLYGON)
        expanded = offset.Execute(distance)
        if len(expanded) == 0:
            return []
        return expanded[0]

    def is_valid_box(self, box):
        if len(box) != 4:
            return False
        return True
