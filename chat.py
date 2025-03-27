from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import re
from appium.options.android import UiAutomator2Options
from xingchen import Configuration, ApiClient, ChatApiSub, ChatReqParams, CharacterKey, Message, UserProfile, ChatContext, ModelParameters
import certifi
import ssl
import json

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

        host = "http://nlp.aliyuncs.com"
        access_token = "lm-uV4SWxT9+Nn65wDszfj5AQ=="
        self.chat_client = ChatClient(host, access_token)
    def chat(self):
        #聊天大窗口
        chatbox = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/j8g')))

        chatItems=chatbox.find_elements(By.ID, "com.tencent.mm:id/cj1")
        i=0
        while True:
         for chatItem in chatItems:
            nameButon=chatItem.find_element(By.ID, 'com.tencent.mm:id/kbq')
            name=nameButon.get_attribute('text')
            print("名字",name)
            if name=="订阅号消息" or name=="公众号" :
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
                    self.sendMsg(name,lastMsg)
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
     

    def sendMsg(self,name,msg):
        input_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "android.widget.EditText"))
        )

        anwser=self.chat_client.chat_sync(name,name,msg)

        # 输入“你好”
        input_box.send_keys(anwser)


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

class ChatClient:
    def __init__(self, host, access_token):
        self.host = host
        self.access_token = access_token
        self.api_instance = self.init_client()

    def init_client(self):
        configuration = Configuration(
            host=self.host,
            # ssl_ca_cert=certifi.where()
        )
        configuration.access_token = self.access_token
        with ApiClient(configuration) as api_client:
            api_instance = ChatApiSub(api_client)
        return api_instance
    
    def build_chat_param(self,user_id,username,msg):
        return ChatReqParams(
            bot_profile=CharacterKey(
                character_id="0a1ad3ff50c64e818eda2ce26719ec34"
            ),
            model_parameters=ModelParameters(
                seed=1683806810,
                incrementalOutput=False
            ),
            messages=[
                Message(
                    name=username,
                    role='user',
                    content=msg
                )
            ],
            context=ChatContext(
                use_chat_history=True
            ),
            user_profile=UserProfile(
                user_id=user_id,
                user_name=username
            )
        )


    def chat_sync(self,user_id,username,msg):
        print("user_id",user_id,"username",username,"msg",msg)
        chat_param = self.build_chat_param(user_id,username,msg)
        data = self.api_instance.chat(chat_param)
        
        print(data.to_str())
        if data.code != 200:
            return "调用失败"
        else:
            return data.data.choices[0].messages[0].content

if __name__ == "__main__":
    wechat = WeChatSpider()
    while True:
        try:
            wechat.chat()
        except Exception as e:
                print(e)
                print("出错了")
