
from module.base.timer import Timer
from module.logger.logger import logger


import cv2


from module.ocr.onnxocr.onnx_paddleocr import ONNXPaddleOcr, sav2Img, TxtBox
from tasks.base.page import page_main, page_mission
from tasks.base.ui import UI
from tasks.mission.assets.assets_mission import MISSION_CHECK, MISSION_RED_DOT, WORK_FINISHED, WORK, \
    MISSION_REWARD_CLAIM_ALL, MISSION_REWARD, REWARD_CLAIM_DONE


class Mission(UI):
    def handle_mission(self):
        self.ui_ensure(page_main)
        if not self._mission_enter():
            return False
        self._mission_reward_claim()
        self._mission_selected()


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
        self.ui_ensure(page_mission)
        model = ONNXPaddleOcr(use_angle_cls=True, use_gpu=False)
        self.device.screenshot()
        result=model.ocr(self.device.image)
        matched_res=model.matchKeys(result,['可领取'])
        if len(matched_res)<=0 and self.appear(REWARD_CLAIM_DONE):
            return True
        x_sorted_res=sorted(matched_res, key=lambda b:b.button[0])
        print(x_sorted_res)
        self.device.click(x_sorted_res[0])
        for _ in self.loop():
            if self.appear_then_click(MISSION_REWARD_CLAIM_ALL):
                continue
            if self.appear_then_click(MISSION_REWARD):
                continue
            if self.appear(REWARD_CLAIM_DONE):
                return True
            res=model.ocr(self.device.image)
            if model.matchArea(res,x_sorted_res[0].button):
                self.device.click(x_sorted_res[0])


















        #todo  1.适配TextBox的属性 和 click 要求属性的名字 2. 根据match res 点击领取奖励  3.如何接取任务，任务接取优先级考量

    def _mission_selected(self):
        self.ui_ensure(page_mission)
        ocr = ONNXPaddleOcr(use_angle_cls=True, use_gpu=False)
        result=ocr.ocr(self.device.image)



az=Mission('alas',task='Alas')
az.image_file=r'C:\Users\liuzy\Desktop\NarutoScript\tasks\mission\MuMu12-20250725-221132.png'
# #
# # print(az.appear(MISSION_CHECK))
model = ONNXPaddleOcr(use_angle_cls=True, use_gpu=False)
res=model.ocr(az.device.image)
print(model.matchKeys(res,['可领取']))
# az._mission_reward_claim()
# import os
# os.chdir(os.path.dirname(os.path.abspath(__file__)))
#
# img = cv2.imread('./1.jpg')
# rs=model.ocr(img)
# print(rs)

