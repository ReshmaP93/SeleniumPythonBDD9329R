import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome(executable_path="C:\Program Files\Drivers\chromedriver.exe")
    #context.driver=webdriver.Chrome

@when('open orangehrm homepage')
def openHomePage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(10)


def maximize(self):
    self._driver.maximize_window()
    time.sleep(10)


@then('verify that logo present on homepage')
def verifyLogo(context):
    status = context.driver.find_element(By.XPATH("//img[@alt='company-branding']").is_displayed())
    assert status is True


@then('close browser')
def closeBrowser(context):
    context.driver.close()
