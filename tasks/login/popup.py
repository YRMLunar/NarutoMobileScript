from module.base.base import ModuleBase
from module.base.timer import Timer
from tasks.base.page import page_main
from tasks.login.assets.assets_login_popup import Game_Main_Announcement, Game_In_Advertise, Daily_Bonus, RANK_UP


class GameInPopup(ModuleBase):
    def handle_game_popup(self):
        """
        Returns:
            bool: If clicked
        """
        # CN user agreement popup
        timer=Timer(2,count=2)
        for _ in  self.loop():
            if self.appear(page_main) and self.match_template_luma(page_main):
                break
            if self.appear_then_click(Game_Main_Announcement, interval=1):
                continue
            if self.appear_then_click(Game_In_Advertise, interval=1):
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
            if self.appear(Game_Main_Announcement, interval=1):
                return True
            if self.appear(Game_In_Advertise, interval=1):
                return True
            if self.appear(Daily_Bonus, interval=1):
                return True
            if self.appear(RANK_UP, interval=1):
                return True
            if timer.reached():
                return False



        return False

az=GameInPopup('alas',task='Alas')
az.image_file=r'C:\Users\刘振洋\Desktop\StarRailCopilot\tasks\login\MuMu12-20250721-131443.png'
print(az.appear_then_click(Game_In_Advertise, interval=3))