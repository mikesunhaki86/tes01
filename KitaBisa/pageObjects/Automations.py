import email
from unicodedata import name
import pytest
from selenium.webdriver.common.by import By



class AutomationsMenu:

    def __init__(self, driver):
        self.driver = driver

    campaign        = (By.XPATH, "//main[@id='home-page']/div[4]/div[1]/div/a[1]/div/div")
    donasi          = (By.ID, "campaign-detail_button_donasi-sekarang")
    amount          = (By.ID, "contribute_inputfield_amount-donation")
    lanjut          = (By.ID, "contribute_button_lanjutkan-pembayaran")
    bca             = (By.XPATH, "//main[@class='style__Main-sc-__sc-18nwpis-0 gajGMD']/div[6]/div[4]")
    name            = (By.XPATH, "//input[@name='fullname']")
    email           = (By.XPATH, "//input[@name='username']")
    back1           = (By.XPATH, "//button[@class='style__Arrow-sc-__sc-1qhccvk-2 enCWmr']")
    back2           = (By.XPATH, "//div[@id='plain-header']")


    def selectCampaign1(self):
        camp = self.driver.find_element(*AutomationsMenu.campaign)
        self.driver.execute_script("return arguments[0].scrollIntoView();", camp)
        return self.driver.find_element(*AutomationsMenu.campaign).click()

    def donasiButton(self):
        return self.driver.find_element(*AutomationsMenu.donasi).click()

    def donasiAmount(self):
        self.driver.find_element(*AutomationsMenu.amount).click()
        return self.driver.find_element(*AutomationsMenu.amount).send_keys("10000")

    def lanjutButton(self):
        return self.driver.find_element(*AutomationsMenu.lanjut).click()

    def bcaTransferMenu(self):
        return self.driver.find_element(*AutomationsMenu.bca).click()

    def userName(self):
        self.driver.find_element(*AutomationsMenu.name).click()
        return self.driver.find_element(*AutomationsMenu.name).send_keys("tes")    

    def userEmail(self):
        self.driver.find_element(*AutomationsMenu.name).click()
        return self.driver.find_element(*AutomationsMenu.email).send_keys("tes123@gmail.com")

    def backPenggalanganMenu(self):
        return self.driver.find_element(*AutomationsMenu.back1).click()

    def backCampaignMenu(self):
        return self.driver.find_element(*AutomationsMenu.back2).click()        
    