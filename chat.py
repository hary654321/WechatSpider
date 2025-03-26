from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import re
from appium.options.android import UiAutomator2Options

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='23117RK66C',
    appPackage='com.tencent.mm',
    appActivity='.ui.LauncherUI',
    noReset=True,
    # language='en',
    # locale='US'
)

appium_server_url = 'http://127.0.0.1:4723/wd/hub'

class WeChatSpider():
    def __init__(self):
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
        self.wait = WebDriverWait(self.driver, 300)


    def chat(self):
        chatbox = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/j8g')))

        chatItems=chatbox.find_elements(By.ID, "com.tencent.mm:id/cj1")

        for chatItem in chatItems:
            nameButon=chatItem.find_element(By.ID, 'com.tencent.mm:id/kbq')
            txt=nameButon.get_attribute('text')
            print("名字",txt)
            if txt=="订阅号消息" :
                print ("过滤掉订阅号消息")
                continue
           # 检查特定元素是否存在
            try:
                # chatItem.find_element(By.ID, 'com.tencent.mm:id/a_h')
                chatItem.find_element(By.ID, 'com.tencent.mm:id/o_u')
                nameButon.click()   
                try:
                    msgList = self.driver.find_elements((By.ID, 'com.tencent.mm:id/bkl'))
                    for msg in msgList:
                         msgtxt=msg.get_attribute('text')
                         print(msgtxt)
                         self.sendMsg(msgtxt)
                except Exception:
                    print(Exception)
                    print("无消息")
            except Exception:
                print("消息已读")

     

    def sendMsg(self,msg):
        input_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "android.widget.EditText"))
        )

        # 输入“你好”
        input_box.send_keys(msg)


        print('发送消息')
        tab = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/fp'))) 
        print('发送成功')


if __name__ == "__main__":
    wechat = WeChatSpider()
    wechat.chat()
