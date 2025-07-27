from tasks.base.page import page_main, page_panel
from tasks.base.ui import UI
from tasks.freebies.assets.assets_freebies_dailyshare import MAIN_GOTO_PANEL, SHARE_BUTTON, SHARE_GOTO_QQ


class DaliyShare(UI):
    def handle_daily_share(self):
        self.ui_ensure(page_main)
        self.device.click(MAIN_GOTO_PANEL)
        self.ui_ensure(page_panel)
        for _ in self.loop():
            if self.appear_then_click(SHARE_BUTTON):
                continue
            if self.appear_then_click(SHARE_GOTO_QQ):
                continue
            if  self.device.app_is_running():
                continue
            else:
                self.device.app_stop_adb('com.tencent.mobileqq')
                break



az=DaliyShare('alas',task='Alas')
az.handle_daily_share()
