
from module.base.timer import Timer
from module.logger.logger import logger


import cv2


from module.ocr.onnxocr.onnx_paddleocr import ONNXPaddleOcr,sav2Img
from tasks.base.page import page_main
from tasks.base.ui import UI
from tasks.mission.assets.assets_mission import MISSION_CHECK, MISSION_RED_DOT, WORK_FINISHED, WORK


class Mission(UI):
    def handle_mission(self):
        self.ui_ensure(page_main)
        if not self._mission_enter():
            return False
        self._mission_reward_claim()


    def _mission_enter(self):
        self.device.swipe_maatouch([180,322],[1141,314])
        logger.info("left swipe")
        timer = Timer(1.5,count=4)
        for _ in self.loop():
            if self.appear(MISSION_CHECK):
                self.wait_until_stable(MISSION_CHECK)
                logger.info('mission entered')
                timer.clear()
                return True
            if self.appear(MISSION_RED_DOT):
                logger.info("Found Mission")
                self.device.click(MISSION_RED_DOT)
                continue
            if timer.reached():
                timer.clear()
                return False
        # self.device.swipe_maatouch([1141,314],[180,322])
        # timer = Timer(1.5,count=2)
        # for _ in self.loop():
        #     if self.appear(MISSION_RED_DOT):
        #         self.wait_until_stable(MISSION_RED_DOT)
        #         self.device.click(MISSION_RED_DOT)
        #         timer.clear()
        #         return
        #     if timer.reached():
        #         timer.clear()
        #         break

    def _mission_reward_claim(self):
        model = ONNXPaddleOcr(use_angle_cls=True, use_gpu=False)

        print(self.device.image)
        result=model.ocr(self.device.image)
        print(result)





az=Mission('alas',task='Alas')

# #
# # print(az.appear(MISSION_CHECK))
az._mission_reward_claim()
# import os
# os.chdir(os.path.dirname(os.path.abspath(__file__)))
#
# img = cv2.imread('./1.jpg')
# rs=model.ocr(img)
# print(rs)