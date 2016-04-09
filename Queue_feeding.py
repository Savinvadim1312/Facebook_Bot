from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from time import sleep
from link_finder import LinkFinder


class Friends_finder():
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password
        self.facebook_url = "https://www.facebook.com/"
        self.more_clicks = 0
        self.existent_people_links = set()

        self.setup()
        self.log_in()
        while 1:
            self.scroll_down_mannualy()        
            self.gather_links()
            self.append_links_to_queue()
    
    def setup(self):
        print('Seting up WebDriver')
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
            print('Conected')
        except:
            print('Unable to conect, Please do it manually')
            ready = False
            while ready == False:
                try:
                    self.driver.find_element_by_xpath('//*[@id="u_0_2"]')
                    ready = True
                except:
                    pass
    
    def scroll_down_mannualy(self):
        print("please scroll down the page")
        print("When done, press any key to start gathering links")
        input()


    
    def gather_links(self):
        print('gathering links, please wait ...')
        self.link_finder = LinkFinder()
        self.link_finder.feed(self.driver.page_source)
        self.gathered_links = self.link_finder.get_links()
        print( str(len(self.gathered_links)) + ' Links was gathered')

    def append_links_to_queue(self):
        print('Apending links and updating the queue file...')
        self.get_existent_links()
        self.update_queue()
 
    def get_existent_links(self):
        with open("data/people_to_add.txt", "r") as f:
            for line in f:
                self.existent_people_links.add(line.replace('\n', ''))

        with open("data/errors.txt", "r") as f:
            for line in f:
                self.existent_people_links.add(line.replace('\n', ''))

        with open("data/added_friends.txt", "r") as f:
            for line in f:
                self.existent_people_links.add(line.replace('\n', ''))


    def update_queue(self):
        self.new_links_added = 0
        with open("data/people_to_add.txt", "a") as f:
            for item in self.gathered_links:
                if item not in self.existent_people_links:
                    self.new_links_added += 1
                    f.write(item + '\n')
        print( str(self.new_links_added) + ' Items were added to the queue file')

if __name__ == "__main__":   
    with open("data/accaunts.txt", "r") as file:
        line = file.readline()
        username = line.split()[0]
        passw = line.split()[1] 
    b = Friends_finder(
        username,
        passw,
        )
  