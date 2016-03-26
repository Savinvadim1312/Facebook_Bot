from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from general import *


class Friend_add():
    def __init__(self, user_name, password, hidden):
        self.user_name = user_name
        self.password = password
        self.hidden = hidden
        self.facebook_url = "https://www.facebook.com/"
        self.nr_of_success = 0
        self.nr_of_tries = 0
        
        self.setup()
        self.log_in()

    def setup(self):
        print(self.user_name + ':  Seting up WebDriver' )
        if self.hidden == 1:
            self.driver = webdriver.PhantomJS()
        elif self.hidden == 0:
            self.driver = webdriver.Firefox()
        self.driver.get(self.facebook_url)

    def log_in(self):
        ready = False
        while ready == False:
            ready = True
            try:
                self.driver.find_element_by_id("email").send_keys(self.user_name)
            except:
                ready = False

        self.driver.find_element_by_id("pass").send_keys(self.password)
        self.driver.find_element_by_id("pass").send_keys(Keys.RETURN)

        sleep(2)

        try:
            self.driver.find_element_by_xpath('//*[@id="u_0_2"]')
            print(self.user_name + ':  Conected')
        except:
            print('Unable to conect, Please do it manually')
            ready = False
            while ready == False:
                try:
                    self.driver.find_element_by_xpath('//*[@id="u_0_2"]')
                    ready = True
                except:
                    pass

    def invite_friend(self, link):
        self.nr_of_tries += 1
        self.link = link
        self.driver.get(self.link) 
        sleep(1)       
        
        delete_from_file("data/people_to_add.txt", self.link)
        if(self.is_friend() == False):
            self.click_add_btn()
            self.accept_decline()

    def click_add_btn(self):
        btns = self.driver.find_elements_by_class_name('FriendRequestAdd')
        while len(btns) == 0:
            btns = self.driver.find_elements_by_class_name('FriendRequestAdd')

        self.succes = False
        for btn in btns:
            try:
                btn.click()
                append_to_file("data/added_friends.txt", self.link)
                self.succes = True
                self.nr_of_success += 1
                print(self.user_name + ":  added   " + str(self.nr_of_success) + "/" + str(self.nr_of_tries))
                break
            except:
                pass

        if self.succes == False:
            append_to_file("data/errors.txt", self.link)
    
    def accept_decline(self):
        sleep(1)
        try:
            driver.find_element_by_class_name("layerConfirm").click()
        except:
            try:
                driver.find_element_by_class_name("layerCancel").click()
            except:
                pass

    def is_friend(self):
        try:
            self.driver.find_element_by_class_name('sx_614afa')
            append_to_file("data/added_friends.txt", self.link)    
            print(self.user_name + ':  Friend request already sent to this user')
        except:
                return False
        return True
