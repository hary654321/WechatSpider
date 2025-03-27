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
        chat_param = self.build_chat_param(user_id,username,msg)
        data = self.api_instance.chat(chat_param)
        
        if data.code != 200:
            return "调用失败"
        else:
            return data.data.choices[0].messages[0].content
        
        print(res.to_str())

if __name__ == "__main__":
    host = "http://nlp.aliyuncs.com"
    access_token = "lm-uV4SWxT9+Nn65wDszfj5AQ=="
    chat_client = ChatClient(host, access_token)
    
    res=chat_client.chat_sync("0a1ad3ff50c64e818eda2ce26719ec34","小明","你好")
    print(res)