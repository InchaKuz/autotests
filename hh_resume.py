import unittest 
from datetime import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import private



class HhResume():
	def __init__(self):
		self.chrome_options = Options()
		self.chrome_options.add_experimental_option('detach', True)
		self.driver = webdriver.Chrome('/home/inna/Project/autotests/chromedriver', options = self.chrome_options)
		self.driver.implicitly_wait(5)
		self.driver.get('https://hh.ru/')
		#self.my_time = time()

	def region_visible_applet(self):  # проверяет наличие элемента на странице(вопрос от регионе)
		self.element = self.driver.find_element_by_class_name('HH-Navi-RegionDropdown-Confirm')
		if self.element.is_displayed():
			self.element.click()

	def login_form_hh(self):
		self.region_visible_applet()
		self.driver.find_element_by_class_name('login-input').send_keys(private.MY_EMAIL)
		self.driver.find_element_by_xpath("(//*[@class='login-input'])[2]").send_keys(private.PASSWORD_HH)
		self.driver.find_element_by_name('action').click()
		self.driver.find_element_by_xpath("//div[text()='Резюме']").click()
		self.driver.find_element_by_xpath("//a[@class='navi-dropdown-link']//span[text()='Мои резюме']").click()
		self.driver.find_element_by_class_name('b-resumelist-vacancyname').click()

	def download_resume(self):
		self.login_form_hh()
		self.driver.find_element_by_class_name('HH-Resume-DownloadButton').click()
		self.driver.find_element_by_class_name('list-params__item_download-adobereader').click()
		#self.my_time = time.sleep(10)


	def copy_url_resume(self):
		self.login_form_hh()
		return self.driver.current_url
			


if __name__ == '__main__':
	unittest.main()