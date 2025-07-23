
from module.base.timer import Timer
from module.logger.logger import logger


import cv2

from module.ocr.ocr import CommonOCR
from module.ocr.onnxocr.onnx_paddleocr import ONNXPaddleOcr
from tasks.base.page import page_main
from tasks.base.ui import UI
from tasks.mission.assets.assets_mission import MISSION_CHECK, MISSION_RED_DOT, WORK_FINISHED, WORK


class Mission(UI):
    def handle_mission(self):
        self.ui_ensure(page_main)
        self._mission_enter()



    def _mission_enter(self):
        self.device.swipe_maatouch([180,322],[1141,314])
        logger.info("left swipe")
        ocr=CommonOCR(MISSION_CHECK)
        timer = Timer(1.5,count=2)
        for _ in self.loop():
            resultbutton=ocr.matched_ocr(self.device.image,['任务集会所','集会所'])
            if resultbutton!=None:
                print(resultbutton)
                if self.appear(MISSION_RED_DOT):
                    self.device.click(resultbutton)
                    logger.info("Found Mission")
                    timer.clear()
                    return
            if timer.reached():
                timer.clear()
                break
        self.device.swipe_maatouch([1141,314],[180,322])
        timer = Timer(1.5,count=2)
        for _ in self.loop():
            resultbutton=ocr.matched_ocr(self.device,['任务集会所','集会所'])
            if resultbutton!=None:
                print(resultbutton)
                if not self.appear(MISSION_RED_DOT):
                    self.device.click(resultbutton)
                    logger.info("Found Mission")
                    timer.clear()
                    return
            if timer.reached():
                timer.clear()
                break




az=Mission('alas',task='Alas')
# az.image_file = r'C:\Users\刘振洋\Desktop\StarRailCopilot\tasks\mission\MuMu12-20250721-164727.png'
# #
# # print(az.appear(MISSION_CHECK))
az.handle_mission()


