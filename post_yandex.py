import unittest 
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By



class Yandex_Post(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome('/home/inna/Project/autotests/chromedriver')
		self.driver.get('https://yandex.ru/')

	def TestOpenLoginFform(self):
		self.login_form = self.driver.find_element_by_link_text('Почта').click()
		self.input_login = self.driver.find_element_by_name('login')
		self.input_login.send_keys('STest777')
		self.input_password = self.driver.find_element_by_name('passwd')
		self.input_password.send_keys('Qwery123')
		self.press_enter = self.driver.find_element_by_xpath("//*[@class='passport-Button']").click()

	def EmailSend(self):
		self.created_mail = self.driver.find_element_by_xpath('//*[@href="#compose"]').click()
		self.time.sleep(2)
		self.input_email = self.driver.find_element_by_class_name("mail-Bubbles")
		self.input_email.send_keys('innes1@ya.ru')
		self.head_email = self.driver.find_element_by_class_name("mail-Compose-Field-Input-Controller")
		self.head_email.send_keys('бла-бла')
		self.body_text_email = self.driver.find_element_by_class_name('cke_wysiwyg_div')
		self.body_text_email.send_keys('бла-бла')
		self.delivery_email = self.driver.find_element_by_class_name('_nb-large-action-button').click()


if __name__ == '__main__':
	unittest.main()

