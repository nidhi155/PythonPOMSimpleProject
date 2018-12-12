'''
Created on 22 Nov 2018

'''
from Locator.locator import Locators
class LoginPage():
    def __init__(self,driver):
        self.driver = driver
        self.username_textbox_id = Locators.username_textbox_id
        self.password_textbox_id = Locators.password_textbox_id
        self.login_button_id = Locators.login_button_id
        self.invalid_login_message_id = Locators.invalid_login_message_id
        #self.invalid_login_message_xpath="//span[@id='register_error']"
        
    def enter_username(self,username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)
    
    
    def enter_password(self,password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)
    
    def click_login_button(self):
        self.driver.find_element_by_id(self.login_button_id).click()
        
    def check_invalid_login(self):
        msg = self.driver.find_element_by_id(self.invalid_login_message_id).text
       # msg = self.driver.find_element_by_xpath(self.invalid_login_message_xpath).text
        return msg