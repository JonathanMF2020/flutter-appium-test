import pytest
from appium_project.utils.driver_manager import create_driver, quit_driver
from appium_project.utils.element_helpers import click_element, get_element_text
from appium_project.locators.flutter_locators import INCREMENT_BUTTON, COUNTER_TEXT

from dotenv import load_dotenv
import os


load_dotenv()
CONFIG_PATH = os.getenv("CONFIG_PATH")
if not CONFIG_PATH:
    raise ValueError("CONFIG_PATH environment variable is not set. Please check your .env file.")


@pytest.fixture(scope="function")
def driver():
    """Fixture to initialize and close the driver."""
    driver = create_driver(CONFIG_PATH)
    yield driver
    quit_driver(driver)

def test_increment_button(driver):
    """Test that the increment button increases the counter correctly."""
    click_element(driver, INCREMENT_BUTTON)
    click_element(driver, INCREMENT_BUTTON)
    click_element(driver, INCREMENT_BUTTON)
    counter_text = get_element_text(driver, COUNTER_TEXT)
    assert counter_text == "3", f"El contador no es 3, es {counter_text}"