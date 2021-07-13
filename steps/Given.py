from appium import webdriver
from behave.contrib.scenario_autoretry import patch_scenario_with_autoretry
import time
from behave import *
@given(u'I clicked "{btnID}" button with acc id')
def clickWithAccID(context,btnID):
    context.driver.find_element_by_accessibility_id(btnID).click()

@given(u'I clicked "{btnID}" button with id')
def clickWithID(context,btnID):
    context.driver.find_element_by_id(btnID).click()
