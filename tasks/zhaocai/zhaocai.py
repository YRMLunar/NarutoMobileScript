from itertools import count
from module.base.timer import Timer
from module.logger.logger import logger

from tasks.base.page import page_main, page_zhaocai
from tasks.base.ui import UI
from tasks.zhaocai.assets.assets_zhaocai import ZHAO_CAI_RED_DOT, ZHAO_CAI_FREE, ZHAO_CAI_PAIED


class ZhaoCai(UI):
    def handle_zhao_Cai(self):
        self.ui_ensure(page_main)
        if self.appear(ZHAO_CAI_RED_DOT):
            self.ui_goto(page_zhaocai)
            self.freezhaocai()

    def freezhaocai(self):
        time=Timer(5,count=8)
        for _ in self.loop():
            if self.appear_then_click(ZHAO_CAI_FREE,interval=2):
                continue
            if self.appear(ZHAO_CAI_PAIED):
                break
            if time.reached():
                logger.warning("ZhaoCai timeout")
                break

        self.ui_goto_main()



az=ZhaoCai('alas',task='Alas')
az.handle_zhao_Cai()