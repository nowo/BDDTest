import os
from appium import webdriver
from behave.contrib.scenario_autoretry import patch_scenario_with_autoretry
from appium.webdriver.common.touch_action import TouchAction
import time

def proceedTutorial(context):
    context.driver.find_element_by_id("com.allandroidprojects.getirsample:id/btn_next").click()
    context.driver.find_element_by_id("com.allandroidprojects.getirsample:id/btn_next").click()
    context.driver.find_element_by_id("com.allandroidprojects.getirsample:id/btn_next").click()
    context.driver.find_element_by_id("com.allandroidprojects.getirsample:id/btn_next").click()



def before_feature(context, feature):
    caps = {}
    caps["app"] = "/Users/ecinar/Desktop/BddAppiumExample/sampleGetir.apk"
    caps["deviceName"] = "emulator-5554"
    caps["platformName"] = "Android"
    caps["ensureWebviewsHavePages"] = True

    context.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
    context.driver.implicitly_wait(5)

    proceedTutorial(context)
    for scenario in feature.walk_scenarios():
            patch_scenario_with_autoretry(scenario, max_attempts=3)

def before_scenario(context, scenario):
    context.driver.reset()
    context.driver.implicitly_wait(5)

    proceedTutorial(context)