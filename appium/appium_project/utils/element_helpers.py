from appium_flutter_finder.flutter_finder import FlutterElement

def click_element(driver, finder):
    """Clicks on an element found by the locator."""
    element = FlutterElement(driver, finder)
    element.click()

def get_element_text(driver, finder):
    """Gets the text of an element found by the locator."""
    element = FlutterElement(driver, finder)
    return element.text

def wait_for_element(driver, finder, timeout=10):
    """Waits for an element to be available."""
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    WebDriverWait(driver, timeout).until(
        lambda d: FlutterElement(d, finder).is_displayed()
    )