from module.base.base import ModuleBase
from module.base.timer import Timer
from tasks.base.page import page_main
from tasks.base.ui import UI
from tasks.base.assets.assets_base_page import MAIN_GOTO_CHARACTER
from tasks.login.assets.assets_login_popup import GAME_MAIN_ANNOUNCEMENT, GAME_IN_ADVERTISE, Daily_Bonus, RANK_UP


class GameInPopup(ModuleBase):
    def handle_game_popup(self):
        """
        Returns:
            bool: If clicked
        """
        # CN user agreement popup
        timer=Timer(2,count=2)
        for _ in  self.loop():
            if  self.match_template_color(MAIN_GOTO_CHARACTER):
                break
            if self.appear_then_click(GAME_MAIN_ANNOUNCEMENT, interval=1):
                continue
            if self.appear_then_click(GAME_IN_ADVERTISE, interval=1):
                continue
            if self.appear_then_click(Daily_Bonus, interval=1):
                continue
            if self.appear_then_click(RANK_UP, interval=1):
                continue
            if timer.reached():
                break


    def is_game_popup(self):
        """
        Returns:
            bool: If clicked
        """
        # CN user agreement popup
        timer=Timer(2,count=2)
        for _ in  self.loop():
            if self.appear(GAME_MAIN_ANNOUNCEMENT, interval=1):
                return True
            if self.appear(GAME_IN_ADVERTISE, interval=1):
                return True
            if self.appear(Daily_Bonus, interval=1):
                return True
            if self.appear(RANK_UP, interval=1):
                return True
            if timer.reached():
                return False



        return False

az=GameInPopup('alas',task='Alas')
az.image_file=r'C:\Users\刘振洋\Desktop\NarutoScript\tasks\login\MuMu12-20250720-230752.png'
print(az.appear(GAME_IN_ADVERTISE, interval=3))