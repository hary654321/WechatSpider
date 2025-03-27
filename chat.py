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
        #聊天大窗口
        chatbox = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/j8g')))

        chatItems=chatbox.find_elements(By.ID, "com.tencent.mm:id/cj1")
        i=0
        while True:
         for chatItem in chatItems:
            nameButon=chatItem.find_element(By.ID, 'com.tencent.mm:id/kbq')
            txt=nameButon.get_attribute('text')
            print("名字",txt)
            if txt=="订阅号消息" or txt=="公众号" :
                print ("过滤掉订阅号消息")
                continue
           # 检查特定元素是否存在
            try:
                # chatItem.find_element(By.ID, 'com.tencent.mm:id/a_h')
                chatItem.find_element(By.ID, 'com.tencent.mm:id/o_u')
                nameButon.click()   
                try:
                    # msgList = self.driver.find_elements('com.tencent.mm:id/bkl')
                    
                    msgList = self.wait.until( EC.visibility_of_all_elements_located((By.ID, 'com.tencent.mm:id/bkl')))
                    length=len( msgList)
                    # for msg in msgList:
                    #      msgtxt=msg.get_attribute('text')
                    #      print(msgtxt)
                    #      self.sendMsg(msgtxt)
                    lastMsg=msgList[length-1].get_attribute('text')
                    print(lastMsg)
                    self.sendMsg(lastMsg)
                    break
     
                except Exception as e:
                    print(e)
                    print("无消息")
            except Exception as e:
                # print(e)
                print("消息已读")
         print("第",i,"轮")
         i+=1
         time.sleep(5)
     

    def sendMsg(self,msg):
        input_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "android.widget.EditText"))
        )

        # 输入“你好”
        input_box.send_keys(msg)


        print('发送消息')
        tab = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@text='发送']"))) 
        time.sleep(0.1)
        tab.click()
        print('发送成功')
        
        print('返回')
        tab = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//android.widget.ImageView[@content-desc='返回']"))) 
        time.sleep(0.1)
        tab.click()
        print('返回成功')


if __name__ == "__main__":
    wechat = WeChatSpider()
    while True:
        try:
            wechat.chat()
        except Exception as e:
                print(e)
                print("出错了")
