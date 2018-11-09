import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class SearchPikabu():
    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome('/home/inna/Project/autotests/chromedriver', options = self.chrome_options)
        self.driver.implicitly_wait(10)
        self.driver.get('https://pikabu.ru/search?q=')

    def search_cat(self):
        #self.driver.find_element_by_xpath("//form[@action='/search']//button[@type ='submit']").click()
        input_word = self.driver.find_element_by_xpath("//section//span[@class='input__box']//input[@class='input__input']").send_keys('котики')
        #self.driver.find_element_by_xpath("//form[@action='/search']//button[@type ='submit']").click()
        #self.driver.find_element_by_xpath("//form[@action='/search']//button[@type='submit']").click()
        self.b = self.driver.find_element_by_xpath("//button[text()='Поиск']").click()
        self.driver.find_element_by_xpath("//a[@class='story__title-link']").click()


    def copy_url(self):
        self.search_cat()
        self.driver.switch_to.window(self.driver.window_handles[1])
        return self.driver.current_url
        



if __name__ == '__main__':
    unittest.main()