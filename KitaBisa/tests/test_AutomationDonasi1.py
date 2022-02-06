import pytest
import time

from pageObjects.Automations import AutomationsMenu
from utilities.BaseClass import BaseClass

class TestDonasi1(BaseClass):

    def test_donasi_satu(self, automation=None):
        automation = AutomationsMenu(self.driver)
        automation.selectCampaign1()
        time.sleep(5)
        automation.donasiButton()
        time.sleep(5)
        automation.donasiAmount()
        time.sleep(5)
        automation.lanjutButton()
        time.sleep(5)
        automation.bcaTransferMenu()
        time.sleep(5)
        automation.userName()
        time.sleep(3)
        automation.userEmail()
        time.sleep(3)
        automation.lanjutButton()
        time.sleep(5)
        automation.backPenggalanganMenu()
        time.sleep(5)
        automation.backCampaignMenu()
        time.sleep(5)
    