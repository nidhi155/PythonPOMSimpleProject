'''
Created on 22 Nov 2018

@author: nidhi
'''

from Locator.locator import Locators
class HomePage():
    def __init__(self,driver):
        self.driver = driver
        self.welcome_msg_linktext = Locators.welcome_msg_linktext
        self.logout_link_class_name = Locators.logout_link_class_name        
    def click_welcome(self):
        self.driver.find_element_by_link_text(self.welcome_msg_linktext).click()
        
    def click_logout(self):
        self.driver.find_element_by_class_name(self.logout_link_class_name).click()
        