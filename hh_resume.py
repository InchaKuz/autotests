import unittest 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import private


class HhResume(unittest.TestCase):
	def setUp(self):
		self.chrome_options = Options()
		self.chrome_options.add_experimental_option('detach', True)
		self.driver = webdriver.Chrome('/home/inna/Project/autotests/chromedriver', options = self.chrome_options)
		self.driver.implicitly_wait(10)
		self.driver.get('https://hh.ru/')


	def test_login_form(self):
		self.driver.find_element_by_class_name('HH-Navi-RegionDropdown-Confirm').click()
		self.driver.find_element_by_class_name('login-input').send_keys(private.MY_EMAIL)
		self.driver.find_element_by_xpath("(//*[@class='login-input'])[2]").send_keys(private.PASSWORD_HH)
		self.driver.find_element_by_name('action').click()
		#self.driver.find_element_by_class_name('web-push-subscribe_controls').click()
		self.driver.find_element_by_class_name('HH-Navi-Menu-Item').click()
		self.driver.find_element_by_xpath('//*[@href="/applicant/resumes"]').click()

if __name__ == '__main__':
	unittest.main()