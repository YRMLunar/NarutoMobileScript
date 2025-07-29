import re

import module.config.server as server
from module.base.base import ModuleBase

from module.logger import logger
from module.ocr.onnxocr.onnx_paddleocr import ONNXPaddleOcr




class OcrPlaneName(ONNXPaddleOcr):
    def after_process(self, result):
        # 通用文本清理
        result = re.sub(r'\d+$', '', result)  # 移除末尾数字
        result = result.replace(' ', '')      # 移除空格
        return super().after_process(result)

class MainPage(ModuleBase):
    # 移除星铁特定的默认平面
    plane = None  # 或者设置为您新游戏的默认区域

    _lang_checked = False
    _lang_check_success = True

    def check_lang_from_map_plane(self) -> str | None:
        # 简化的语言检测逻辑，不依赖星铁地图
        logger.info('Using configured language')
        if self.config.Emulator_GameLanguage != 'auto':
            server.set_lang(self.config.Emulator_GameLanguage)
            MainPage._lang_checked = True
            MainPage._lang_check_success = True
            return self.config.Emulator_GameLanguage
        else:
            # 默认使用中文
            server.set_lang('cn')
            MainPage._lang_checked = True
            MainPage._lang_check_success = True
            return 'cn'

def handle_lang_check(self, page):
    """处理语言检查"""
    if MainPage._lang_checked:
        return False

    self.check_lang_from_map_plane()
    return True

def acquire_lang_checked(self):
    """获取语言检查状态"""
    if MainPage._lang_checked:
        return False

    logger.info('acquire_lang_checked')
    self.check_lang_from_map_plane()
    return True