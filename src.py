from module.alas import AzurLaneAutoScript
from module.logger import logger


class StarRailCopilot(AzurLaneAutoScript):
    def restart(self):
        from tasks.login.login import Login
        Login(self.config, device=self.device).app_restart()

    def start(self):
        from tasks.login.login import Login
        Login(self.config, device=self.device).app_start()

    def stop(self):
        from tasks.login.login import Login
        Login(self.config, device=self.device).app_stop()

    def freebies(self):
        from tasks.freebies.freebies import Freebies

    def zhao_cai(self):
        from tasks.zhaocai.zhaocai import ZhaoCai
        ZhaoCai(self.config,device=self.device).handle_zhao_Cai()
    def friend_gifts(self):
        from tasks.freebies.friendgifts import FriendGifts
        FriendGifts(self.config,device=self.device).handle_friend_gifts()
    def mail_reward(self):
        from tasks.freebies.mail import MailReward
        MailReward(self.config,device=self.device).mail_claim_all()

    def goto_main(self):
        from tasks.login.login import Login
        from tasks.base.ui import UI
        if self.device.app_is_running():
            logger.info('App is already running, goto main page')
            UI(self.config, device=self.device).ui_goto_main()
        else:
            logger.info('App is not running, start app and goto main page')
            Login(self.config, device=self.device).app_start()
            UI(self.config, device=self.device).ui_goto_main()

    def error_postprocess(self):
        # Exit cloud game to reduce extra fee
        if self.config.is_cloud_game:
            from tasks.login.login import Login
            Login(self.config, device=self.device).app_stop()



if __name__ == '__main__':
    src = StarRailCopilot('src')
    src.loop()
