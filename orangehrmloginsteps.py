import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('I launch chrome browser')
def launchbrowser(context):
    context.driver = webdriver.Chrome(executable_path="C:\Program Files\Drivers\chromedriver.exe")
    time.sleep(10)


@when('I open orangehrm homepage')
def openhomepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(15)


def maximize(self):
    self._driver.maximize_window()
    time.sleep(10)


@when('Enter Username"{admin}" and Password "{admin123}"')
def username(context, admin, admin123):
    context.driver.find_element(By.NAME,"username").send_keys(admin)
    context.driver.find_element(By.NAME,"password").send_keys(admin123)


@when('click on login button')
def login(context):
    context.driver.find_element(By.XPATH,"//button[@type='submit']").click()


@then('user must successfully login to the orangehrm application')
def step_impl(context):
    try:
        text=context.driver.find_element(By.XPATH,"//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']").text
    except:
        context.driver.close()
    assert False,"Test Failed"
    if text=="Dashboard":
        context.driver.close()
    assert True, "Test Passed"
    
