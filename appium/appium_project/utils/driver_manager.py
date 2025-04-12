from appium import webdriver
from appium.options.common import AppiumOptions
import json

def create_driver(config_path):
    """Creates and returns an instance of the Appium driver."""
    options = AppiumOptions()
    with open(config_path, "r") as config_file:
        config_data = json.load(config_file)
    for key, value in config_data.items():
        options.set_capability(key, value)
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    return driver

def quit_driver(driver):
    """Closes the Appium driver."""
    if driver:
        driver.quit()