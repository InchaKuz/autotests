import unittest
import time
import allure
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType


class SearchPikabu():
    def __init__(self):
        self.driver = webdriver.Chrome('/home/inna/Project/autotests/chromedriver')
        self.driver.implicitly_wait(10)
        self.driver.get('https://pikabu.ru/search?q=')

    def search_cat(self):
        input_word = self.driver.find_element_by_xpath("//section//span[@class='input__box']//input[@class='input__input']").send_keys('котики')
        self.b = self.driver.find_element_by_xpath("//button[text()='Поиск']").click()
        self.driver.find_element_by_xpath("//a[@class='story__title-link']").click()

    def copy_url(self):
        self.search_cat()
        self.driver.switch_to.window(self.driver.window_handles[1])
        allure.attach(self.driver.get_screenshot_as_png(), name='Kotik', attachment_type=AttachmentType.PNG)
        return self.driver.current_url