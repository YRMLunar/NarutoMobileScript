from tasks.base.page import page_main, page_friend_panel
from tasks.base.ui import UI
from tasks.freebies.assets.assets_freebies_friendgifts import MAIN_GOTO_FRIEND_PANEL, GIFTS_GIVE, GIFTS_CLAIM, \
    GIFTS_CLAIM_CHECK, GIFTS_CLAIM_CONFIRM, FRIEND_PANEL_RED_DOT
from module.base.timer import Timer
from module.logger.logger import logger

class FriendGifts(UI):
    def handle_friend_gifts(self):


        self.ui_ensure(page_main)
        if self.appear(FRIEND_PANEL_RED_DOT):
            self.ui_goto(page_friend_panel)
            self._friend_gifts_give_claim()
        self.ui_ensure(page_main)

    def _friend_gifts_give_claim(self):
        give=False
        claim=False
        timeout = Timer(6, count=10)  # 30秒超时
        for _ in self.loop():
            if timeout.reached():
                logger.warning("friend gift claim timeout")
                break
            if self.appear(GIFTS_GIVE,interval=3) and give==False:
                self._ui_button_confirm(GIFTS_GIVE)
                self.device.click(GIFTS_GIVE)
                give=True
            if self.appear(GIFTS_CLAIM,interval=3) and claim==False:
                self._ui_button_confirm(GIFTS_CLAIM)
                self.device.click(GIFTS_CLAIM)
                claim=True
            if self.appear(GIFTS_CLAIM_CONFIRM):
                self._ui_button_confirm(GIFTS_CLAIM_CONFIRM)
                self.device.click(GIFTS_CLAIM_CONFIRM)
                break

        self.ui_goto_main()



az=FriendGifts('alas',task='Alas')
az.handle_friend_gifts()