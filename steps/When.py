from appium import webdriver
from behave.contrib.scenario_autoretry import patch_scenario_with_autoretry
import time
from behave import *

@when(u'I clicked "{btnID}"')
def clickIdOnWhen(context,btnID):
    context.driver.find_element_by_id(btnID).click()
