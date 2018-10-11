import unittest #Встроенная библиотека
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By



driver = webdriver.Chrome('/home/inna/Project/autotests/chromedriver')
url = 'https://yandex.ru/'


def test_open_login_form(url):
	driver.get(url)
	login_form = driver.find_element_by_link_text('Почта').click()
	input_login = driver.find_element_by_name('login')
	input_login.send_keys('STest777')
	input_password = driver.find_element_by_name('passwd')
	input_password.send_keys('Qwery123')
	press_enter = driver.find_element_by_xpath("//*[@class='passport-Button']").click()



def email_send():
	created_mail = driver.find_element_by_xpath('//*[@href="#compose"]').click()
	time.sleep(2)
	input_email = driver.find_element_by_class_name("mail-Bubbles")
	input_email.send_keys('innes1@ya.ru')
	head_email = driver.find_element_by_class_name("mail-Compose-Field-Input-Controller")
	head_email.send_keys('бла-бла')
	body_text_email = driver.find_element_by_class_name('cke_wysiwyg_div')
	body_text_email.send_keys('бла-бла')
	delivery_email = driver.find_element_by_class_name('_nb-large-action-button').click()

def main():
	test_open_login_form(url)
	time.sleep(5) 
	email_send()


main()


