from module.base import button
from module.base.timer import Timer
from module.logger import logger
from tasks.base.assets.assets_base_page import  MAIN_GOTO_MAIL
from tasks.base.page import  page_main, page_mail
from tasks.base.ui import UI
from tasks.freebies.assets.assets_freebies_mail import *


class MailReward(UI):
    def _mail_enter(self):
        """
        Pages:
            in: page_menu
            out: MAIL_CHECK
        """
        logger.info('Mail enter')
        self.interval_clear([
            page_main.check_button
        ])

        for _ in self.loop():
            if self.appear(MAIL_CHECK):
                self.wait_until_stable(MAIL_CHECK)
                logger.info('Mail enter success')
                return True

            if self.is_in_main(interval=2):
                self.device.click(MAIN_GOTO_MAIL)
                continue


    def _mail_exit(self):
        """
        Pages:
            in: MAIL_CHECK
            out: page_menu
        """
        logger.info('Mail exit')
        self.interval_clear([
            MAIL_CHECK
        ])

        for _ in self.loop():
            if self.ui_page_appear(page_main):
                logger.info('go to page main')
                break
            if self.ui_page_appear(page_mail):
                self.appear_then_click(MAIL_EXIT)
                logger.info('Mail exit done')
                continue
        # clear state
        self.interval_clear([
            page_main.check_button
        ])


    def _mail_get_claim_button(self):
        """
        Returns:
            CLAIM_ALL or CLAIM_ALL_DONE or None
        """
        self.ui_ensure(page_mail)
        timeout = Timer(1.5, count=5).start()
        for _ in self.loop():
            if self.appear(CLAIM_ALL):
                logger.attr('MailClaim', CLAIM_ALL)
                return  CLAIM_ALL
            # CLAIM_ALL_DONE is transparent, use match_template_luma
            if timeout.reached():
                logger.warning('Get MailClaim timeout')
                return None

    def _mail_claim(self):
        """
        Pages:
            in: CLAIM_ALL
            out: CLAIM_ALL_DONE
        """
        logger.info('Mail claim all')
        for _ in self.loop():
            # CLAIM_ALL_DONE is transparent, use match_template_luma
            if self.match_template_luma(CLAIM_ALL_DONE):
                break

            if self.appear_then_click(CLAIM_ALL):
                continue





    def mail_claim_all(self):
        """
        Claim mails and exit

        Returns:
            bool: If claimed

        Pages:
            in: page_menu
            out: page_menu
        """
        self.ui_ensure(page_main)


        # #MAIL_RED_DOT
        # if not self.appear(MAIL_RED_DOT):
        #     logger.info("NOT FOUND MAIL_RED_DOT")
        #     return False


        # claim all
        if not self._mail_enter():
            return False

        button = self._mail_get_claim_button()
        if button is CLAIM_ALL :
            self._mail_claim()
            self._mail_exit()
            return True
        else:
            self._mail_exit()
            return False

    def _mail_delete(self):
        timeout = Timer(1.5, count=3).start()
        for _ in self.loop():
            if self.appear_then_click(CLAIM_DELETE,interval=1):
                continue
            if self.appear_then_click(CLAIM_DELETE_POPUP,interval=1):
                break
            if timeout.reached():
                break

az=MailReward('alas',task='Alas')
az.image_file=r'C:\Users\liuzy\Desktop\NarutoScript\tasks\login\MAIN_GOTO_CHARACTER.png'
#print(az.ui_page_appear(page_mail))
# print(az.appear(MAIL_RED_DOT))

az.mail_claim_all()

