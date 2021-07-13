from appium import webdriver
from behave.contrib.scenario_autoretry import patch_scenario_with_autoretry
import time
from behave import *

@then(u'I should see "{btnID}" with this text "{text}"')
def verifyText(context,btnID,text):
    time.sleep(2)
    assert context.driver.find_element_by_id(btnID).text == text