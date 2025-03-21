import unittest

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='22041211A',
    appPackage='com.tencent.mm',
    appActivity='.ui.LauncherUI',
    # language='en',
    # locale='US'
)

appium_server_url = 'http://127.0.0.1:4723/wd/hub'


class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_find_el(self) -> None:
        xpath = "new UiSelector().text(\"WeChat\")"
        el = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=xpath)
        el.click()


if __name__ == '__main__':
    unittest.main()