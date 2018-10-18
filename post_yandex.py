import unittest 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import private
import hh_resume 

hh_object = hh_resume.HhResume
hh_link = hh_object.copy_url_resume()


class YandexPost(unittest.TestCase, hh_resume.HhResume):
	def setUp(self):
		self.chrome_options = Options()
		self.chrome_options.add_experimental_option('detach', True)
		self.driver = webdriver.Chrome('/home/inna/Project/autotests/chromedriver', options = self.chrome_options)
		self.driver.implicitly_wait(10)
		self.driver.get('https://yandex.ru/')

	def open_login_form(self):
		self.driver.find_element_by_link_text('Почта').click()
		self.driver.find_element_by_name('login').send_keys(private.LOGIN_YA)
		self.driver.find_element_by_name('passwd').send_keys(private.PASSWORD_YA)
		self.driver.find_element_by_xpath("//*[@class='passport-Button']").click()
	
	def click_botton_created_email(self):
		return self.driver.find_element_by_xpath('//*[@href="#compose"]').click()

	def text_email(self):
		return self.driver.find_element_by_class_name('cke_wysiwyg_div').send_keys(hh_link)

	def email_send(self):
		self.click_botton_created_email()
		self.driver.find_element_by_class_name("mail-Bubbles").send_keys(private.MY_EMAIL)
		self.driver.find_element_by_class_name("mail-Compose-Field-Input-Controller").send_keys('Резюме')
		self.text_email()
		self.driver.find_element_by_class_name('_nb-large-action-button').click()

	def test_email_send(self):
		self.open_login_form()
		self.email_send()




if __name__ == '__main__':
	unittest.main()

