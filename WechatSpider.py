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
    def login(self):
        print('点击登陆按钮——————')
        login = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/drp')))
        login.click()

        # 输入手机号
        phone = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/ji')))
        phone_num = input('请输入手机号')
        phone.send_keys(phone_num)

        # 点击下一步
        print('点击下一步中')
        button = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/ast')))
        button.click()

        # 输入密码
        pass_w = input('请输入密码：')
        password = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@resource-id="com.tencent.mm:id/ji"][1]')))
        password.send_keys(pass_w)

        # 点击登录
        login = self.driver.find_element_by_id('com.tencent.mm:id/ast')
        login.click()

        # 通讯录提示
        tip = self.wait.until(EC.element_to_be_clickable((By.ID, 'com.tencent.mm:id/au9')))
        tip.click()


    def fj(self):
        # 通讯录提示
        # print('点击通讯录提示')
        # tip = self.wait.until(EC.element_to_be_clickable((By.ID, 'com.tencent.mm:id/au9')))
        # tip.click()
        # 点击加号
        print('发现')
        tab = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='发现']"))) 
        time.sleep(0.1)
        tab.click()
        print('发现done')

        print('附近')
        tab = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='附近']"))) 
        time.sleep(0.1)
        tab.click()
        print('附近done')


        print('附近的人')
        tab = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='附近的人']"))) 
        time.sleep(0.1)
        tab.click()
        print('附近的人done')


        # try:
        #     # 尝试查找按钮
        #     ok_button = self.driver.find_element(By.ID, "com.tencent.mm:id/mm_alert_ok_btn")
        #     # 如果找到了按钮，执行点击操作
        #     ok_button.click()
        #     print("按钮存在并已点击")
        # except Exception:
        #     # 如果按钮不存在，打印提示信息
        #     print("未找到按钮")

        # print('确定')
        # tab = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='确定']"))) 
        # time.sleep(0.1)
        # tab.click()
        # print('确定done')

        # 等待联系人列表的 ListView 元素加载完成
        contacts_list = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "com.tencent.mm:id/k5q"))
        )

        print('获取联系人列表成功')

        # 等待第一个联系人的名字元素可点击
        first_contact = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[2]/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView"))
        )
        first_contact.click()

        # 等待打招呼的按钮出现并点击（假设打招呼按钮的 resource-id 是 com.tencent.mm:id/say_hi）
        print('打招呼')
        tab = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='打招呼']"))) 
        time.sleep(0.1)
        tab.click()
        print('打招呼done')

        input_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "android.widget.EditText"))
        )

        # 输入“你好”
        input_box.send_keys("你好")


        print('发送消息')
        tab = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/fp'))) 
        print('发送成功')
        time.sleep(0.1)
        tab.click()

        return
        print('点击加号——')
        tab = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/plus_icon'))) 
        print('已经找到加号按钮')
        time.sleep(0.1)
        tab.click()



        print('添加朋友')
        tab = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/obc'))) 
        time.sleep(0.1)
        tab.click()
        print('添加朋友done')

        # print('添加朋友')
        # # tab = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/m79g'))) 

        # elements = self.driver.find_elements(By.ID, "com.tencent.mm:id/m79")
        # if len(elements) > 1:
        #     # 访问第二个元素（索引从0开始）
        #     second_element = elements[1]
        #     second_element.click()
        # print('添加朋友done')
        # time.sleep(0.1)
   

        print('发起群聊')
        tab = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/obc'))) 
        print('发起群聊')
        time.sleep(0.1)
        tab.click()


        # 搜索框1
        print('点击搜索框——')
        search1 = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/ji')))
        print('已找到搜索框')
        search1.click()

        # 搜索框2
        search2 = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/ji')))
        searchcon = input('请输入搜索帐号')
        search2.send_keys(searchcon)

        # 点击搜索
        print('点击搜索——')
        search = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/oj')))
        print('已找到搜索')
        search.click()
        time.sleep(0.1)

        # 获取用户基本资料
        self.name = self.driver.find_element_by_id('com.tencent.mm:id/u0').get_attribute('text')
        self.sex = self.driver.find_element_by_id('com.tencent.mm:id/awu').get_attribute('name')
        self.location = self.driver.find_element_by_xpath(
            '//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout['
            '1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout['
            '1]/android.view.ViewGroup[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout['
            '1]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout['
            '2]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout['
            '2]/android.widget.LinearLayout[1]/android.widget.TextView[1]').get_attribute('text')
        self.signature = self.driver.find_element_by_xpath(
            '//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout['
            '1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout['
            '1]/android.view.ViewGroup[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout['
            '1]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout['
            '3]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout['
            '2]/android.widget.LinearLayout[1]/android.widget.TextView[1]').get_attribute('text')

        # 添加到通讯录
        print('点击添加到通讯录——')
        addbook = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/awb')))
        print('已找到添加到通讯录')
        time.sleep(0.1)
        addbook.click()

        # 发送请求
        print('点击发送请求——')
        post = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/j0')))
        print('已找到发送请求')
        time.sleep(0.1)
        post.click()

        # 返回
        print('点击返回1——')
        rtn1 = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/jc')))
        print('已找到返回1')
        rtn1.click()
        time.sleep(0.1)

        print('点击返回2——')
        rtn2 = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/jg')))
        print('已找到返回2')
        rtn2.click()
        time.sleep(0.1)

        print('点击返回3——')
        rtn3 = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/jc')))
        print('已找到返回3')
        rtn3.click()



    def add_friend(self):
        # 通讯录提示
        # print('点击通讯录提示')
        # tip = self.wait.until(EC.element_to_be_clickable((By.ID, 'com.tencent.mm:id/au9')))
        # tip.click()
        # 点击加号
        print('发现')
        tab = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/h6y'))) 
        time.sleep(0.1)
        tab.click()
        print('发现done')
        return
        print('点击加号——')
        tab = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/plus_icon'))) 
        print('已经找到加号按钮')
        time.sleep(0.1)
        tab.click()



        print('添加朋友')
        tab = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/obc'))) 
        time.sleep(0.1)
        tab.click()
        print('添加朋友done')

        # print('添加朋友')
        # # tab = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/m79g'))) 

        # elements = self.driver.find_elements(By.ID, "com.tencent.mm:id/m79")
        # if len(elements) > 1:
        #     # 访问第二个元素（索引从0开始）
        #     second_element = elements[1]
        #     second_element.click()
        # print('添加朋友done')
        # time.sleep(0.1)
   

        print('发起群聊')
        tab = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/obc'))) 
        print('发起群聊')
        time.sleep(0.1)
        tab.click()


        # 搜索框1
        print('点击搜索框——')
        search1 = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/ji')))
        print('已找到搜索框')
        search1.click()

        # 搜索框2
        search2 = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/ji')))
        searchcon = input('请输入搜索帐号')
        search2.send_keys(searchcon)

        # 点击搜索
        print('点击搜索——')
        search = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/oj')))
        print('已找到搜索')
        search.click()
        time.sleep(0.1)

        # 获取用户基本资料
        self.name = self.driver.find_element_by_id('com.tencent.mm:id/u0').get_attribute('text')
        self.sex = self.driver.find_element_by_id('com.tencent.mm:id/awu').get_attribute('name')
        self.location = self.driver.find_element_by_xpath(
            '//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout['
            '1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout['
            '1]/android.view.ViewGroup[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout['
            '1]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout['
            '2]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout['
            '2]/android.widget.LinearLayout[1]/android.widget.TextView[1]').get_attribute('text')
        self.signature = self.driver.find_element_by_xpath(
            '//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout['
            '1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout['
            '1]/android.view.ViewGroup[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout['
            '1]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout['
            '3]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout['
            '2]/android.widget.LinearLayout[1]/android.widget.TextView[1]').get_attribute('text')

        # 添加到通讯录
        print('点击添加到通讯录——')
        addbook = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/awb')))
        print('已找到添加到通讯录')
        time.sleep(0.1)
        addbook.click()

        # 发送请求
        print('点击发送请求——')
        post = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/j0')))
        print('已找到发送请求')
        time.sleep(0.1)
        post.click()

        # 返回
        print('点击返回1——')
        rtn1 = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/jc')))
        print('已找到返回1')
        rtn1.click()
        time.sleep(0.1)

        print('点击返回2——')
        rtn2 = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/jg')))
        print('已找到返回2')
        rtn2.click()
        time.sleep(0.1)

        print('点击返回3——')
        rtn3 = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/jc')))
        print('已找到返回3')
        rtn3.click()

    def check_friendcircle(self):
        # 等待加好友
        print('等待加好友——')
        while True:
            friendwait = self.driver.find_element_by_xpath('//android.widget.FrameLayout['
                                                           '1]/android.widget.FrameLayout['
                                                           '1]/android.widget.LinearLayout['
                                                           '1]/android.widget.FrameLayout[1]/android.view.ViewGroup['
                                                           '1]/android.widget.FrameLayout['
                                                           '1]/android.widget.FrameLayout['
                                                           '1]/android.widget.FrameLayout['
                                                           '1]/com.tencent.mm.ui.mogic.WxViewPager['
                                                           '1]/android.widget.FrameLayout['
                                                           '1]/android.widget.RelativeLayout['
                                                           '1]/android.widget.ListView['
                                                           '1]/android.widget.LinearLayout['
                                                           '1]/android.widget.LinearLayout['
                                                           '1]/android.widget.LinearLayout['
                                                           '1]/android.widget.LinearLayout[1]/android.view.View['
                                                           '1]').get_attribute('text')
            if re.match(friendwait, self.name) is not None:
                print('已找到好友')
                click_friend = self.driver.find_element_by_xpath('//android.widget.FrameLayout['
                                                                 '1]/android.widget.FrameLayout['
                                                                 '1]/android.widget.LinearLayout['
                                                                 '1]/android.widget.FrameLayout['
                                                                 '1]/android.view.ViewGroup['
                                                                 '1]/android.widget.FrameLayout['
                                                                 '1]/android.widget.FrameLayout['
                                                                 '1]/android.widget.FrameLayout['
                                                                 '1]/com.tencent.mm.ui.mogic.WxViewPager['
                                                                 '1]/android.widget.FrameLayout['
                                                                 '1]/android.widget.RelativeLayout['
                                                                 '1]/android.widget.ListView['
                                                                 '1]/android.widget.LinearLayout[1]')
                break
        time.sleep(0.1)
        click_friend.click()
        print('点击好友聊天窗口')
        time.sleep(0.1)

        # 点击聊天窗口右上角
        print('点击省略号——')
        ellipsi = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/j1')))
        print('已找到省略号')
        ellipsi.click()
        time.sleep(0.1)

        # 点击头像
        print('点击头像——')
        photo = self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout['
                                                  '1]/android.widget.FrameLayout[1]/android.widget.LinearLayout['
                                                  '1]/android.widget.FrameLayout[1]/android.view.ViewGroup['
                                                  '1]/android.widget.FrameLayout[2]/android.widget.FrameLayout['
                                                  '1]/android.widget.LinearLayout[1]/android.widget.ListView['
                                                  '1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout['
                                                  '1]/android.widget.ImageView[1]')
        print('已找到头像')
        photo.click()
        time.sleep(0.1)

        # 获取微信号
        print('获取微信号——')
        self.wechatnum = self.driver.find_element_by_id('com.tencent.mm:id/awj').get_attribute('text')
        print('已找到微信号')
        time.sleep(0.1)

        # 点击个人相册
        print('点击个人相册——')
        album = self.driver.find_element_by_id('com.tencent.mm:id/cwl')
        print('已找到个人相册')
        album.click()
        time.sleep(0.1)

    def craw_friendcircle(self):
        # 开始爬取朋友圈
        diction = dict()
        temp = dict()
        count = 0
        while True:
            flag = True
            self.driver.swipe(500, 1700, 500, 1050, 2000)
            time.sleep(2)
            items = self.driver.find_elements_by_id('com.tencent.mm:id/e4v')
            time.sleep(0.1)
            for item in items:
                try:
                    item.click()
                    temp['time'] = self.driver.find_element_by_id('android:id/text1').get_attribute('text')
                    temp['content'] = self.driver.find_element_by_id('com.tencent.mm:id/e30').get_attribute('text')
                    if temp['content'] in diction.values():
                        rtn = self.driver.find_element_by_id('com.tencent.mm:id/jc')
                        rtn.click()
                        temp.clear()
                        time.sleep(0.1)
                    else:
                        diction['time%s' % count] = temp['time']
                        diction['content%s' % count] = temp['content']
                        print("日期：", temp['time'], "内容：", temp['content'])
                        rtn = self.driver.find_element_by_id('com.tencent.mm:id/jc')
                        rtn.click()
                        count += 1
                        temp.clear()
                        time.sleep(0.1)
                except Exception:
                    pass
            try:
                self.driver.find_element_by_id('com.tencent.mm:id/e4l')
                print('获取该用户朋友圈完毕')
                flag = False
            except Exception:
                pass

            try:
                self.driver.find_element_by_id('com.tencent.mm:id/e4m')
                print('获取该用户朋友圈完毕')
                flag = False
            except Exception:
                pass

            try:
                self.driver.find_element_by_id('com.tencent.mm:id/ae7')
                print('获取该用户朋友圈完毕')
                flag = False
            except Exception:
                pass

            if flag is False:
                break

    def print_info(self):
        print('网名：', self.name, self.wechatnum, '性别: ', self.sex, '地区：', self.location, '签名：', self.signature)


if __name__ == "__main__":
    wechat = WeChatSpider()
    # wechat.login()
    wechat.fj()
    # wechat.add_friend()
    # wechat.check_friendcircle()
    # wechat.craw_friendcircle()
    # wechat.print_info()
