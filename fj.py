from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import re
from appium.options.android import UiAutomator2Options
import sqlite3

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
        self.sqlite= SQLiteManager("wechat.sqlite")
        self.sqlite.connect()
        self.sqlite.create_table()

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
        
        print('筛选')
        tab = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//android.widget.ImageView[@content-desc='更多']"))) 
        time.sleep(0.1)
        tab.click()
        print('筛选done')
        
        print('只看男生')
        tab = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='只看男生']"))) 
        time.sleep(0.1)
        tab.click()
        print('筛选done')
        
        chatbox = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/k5r')))
        contacts_list = self.driver.find_elements(By.ID, "com.tencent.mm:id/k5r")

        while True:
            for chatItem in contacts_list:
                name=chatItem.get_attribute('text')
                print("名字",name)
                
                user=self.sqlite.select_user_by_name(name)
                
                if user is not None:
                    print("已发送消息:",user)
                    continue
                
                print("数据库用户信息:",user)
                
                self.sqlite.insert_user(name, 25, "alice@example.com")
        
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
                
                print('返回')
                tab = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/actionbar_up_indicator_btn'))) 
                time.sleep(0.1)
                tab.click()
                
                time.sleep(10)
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


class SQLiteManager:
    def __init__(self, db_name):
        """
        初始化 SQLite 管理器
        :param db_name: 数据库文件名
        """
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def connect(self):
        """
        连接到 SQLite 数据库
        """
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def close(self):
        """
        关闭数据库连接
        """
        if self.conn:
            self.conn.close()

    def create_table(self):
        """
        创建 users 表
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                email TEXT  NOT NULL
            )
        ''')
        self.conn.commit()

    def insert_user(self, name, age, email):
        """
        插入用户数据
        :param name: 用户姓名
        :param age: 用户年龄
        :param email: 用户邮箱
        """
        self.cursor.execute('''
            INSERT INTO users (name, age, email)
            VALUES (?, ?, ?)
        ''', (name, age, email))
        self.conn.commit()

    def select_all_users(self):
        """
        查询所有用户数据
        :return: 用户数据列表
        """
        self.cursor.execute('SELECT * FROM users')
        return self.cursor.fetchall()
    def select_user_by_name(self,name):
        """
        查询所有用户数据
        :return: 用户数据列表
        """
        self.cursor.execute('SELECT * FROM users WHERE name = ?', (name,))
        return self.cursor.fetchone()

    def update_user_age(self, user_id, new_age):
        """
        更新用户年龄
        :param user_id: 用户 ID
        :param new_age: 新的年龄
        """
        self.cursor.execute('''
            UPDATE users
            SET age = ?
            WHERE id = ?
        ''', (new_age, user_id))
        self.conn.commit()

    def delete_user(self, user_id):
        """
        删除用户数据
        :param user_id: 用户 ID
        """
        self.cursor.execute('''
            DELETE FROM users
            WHERE id = ?
        ''', (user_id,))
        self.conn.commit()


if __name__ == "__main__":
       
    wechat = WeChatSpider()
    # wechat.login()
    wechat.fj()
    # wechat.add_friend()
    # wechat.check_friendcircle()
    # wechat.craw_friendcircle()
    # wechat.print_info()
