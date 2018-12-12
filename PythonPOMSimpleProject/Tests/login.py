'''
Created on 22 Nov 2018

@author: nidhi
'''

from selenium import webdriver
import time
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from Pages.homePage import HomePage
from Pages.loginPage import LoginPage

import HtmlTestRunner



class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super(LoginTest, cls).setUpClass()
        chromedriver="C:\\Users\\nidhi\\Downloads\\chromedriver_win32\\chromedriver.exe"
        cls.driver = webdriver.Chrome(chromedriver)
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://apply.tesco-careers.com/members/index.php")
        
        login = LoginPage(driver)
        login.enter_username("nidhi155@gmail.com")
        login.enter_password("Reading123")
        login.click_login_button()
        
        home = HomePage(driver)
        home.click_welcome()
        home.click_logout()
        time.sleep(2)
        '''
        self.driver.find_element_by_id("login-email").send_keys("nidhi155@gmail.com")
        self.driver.find_element_by_id("password").send_keys("Reading123")
        self.driver.find_element_by_id("login-btn").click()
       # self.driver.find_element_by_class_name("welcomeMessage_bg")
        self.driver.find_element_by_link_text('Nidhi Varshney').click()
        self.driver.find_element_by_class_name("link_button").click()'''
        
    def test_login_invalid_password(self):
        driver = self.driver
        driver.get("https://apply.tesco-careers.com/members/index.php")
        
        login = LoginPage(driver)
        login.enter_username("nidhi155@gmail.com")
        login.enter_password("Reading")
        login.click_login_button()
        message = login.check_invalid_login()
        self.assertEqual(message, 'Incorrect username or password.\nClick here for help.')

        time.sleep(2)
    @classmethod
    def tearDownClass(cls):
        super(LoginTest, cls).tearDownClass()
        cls.driver.close()
        cls.driver.quit()
        print("test Completed!")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/learning_project/eclipse-workspace/PythonPOMSimpleProject/Reports'))