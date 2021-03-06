import unittest
import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import private
from hh_resume import HhResume


class YandexPost(unittest.TestCase):
    def setUp(self):
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option('detach', True)
        with pytest.allure.step("Launch site"):
            self.driver = webdriver.Chrome(PATH_CROME_DRIVER, options = self.chrome_options)
            self.driver.implicitly_wait(5)
        with pytest.allure.step("Verify Title loaded"):
            self.driver.get('https://yandex.ru/')
            self.hh_resume = HhResume()

    @pytest.allure.step("Launch site1")
    def open_login_form(self):
        self.driver.find_element_by_link_text('Почта').click()
        self.driver.find_element_by_name('login').send_keys(private.LOGIN_YA)
        self.driver.find_element_by_name('passwd').send_keys(private.PASS_YA)
        self.driver.find_element_by_xpath("//*[@class='passport-Button']").click()
    
    def click_botton_created_email(self):  # кнопка "Написать письмо"
        return self.driver.find_element_by_xpath('//*[@href="#compose"]').click()

    def input_address(self):  # ввод адреса получателя "Кому"
        return self.driver.find_element_by_class_name("mail-Bubbles").send_keys(private.MY_EMAIL) 

    def input_theme_email(self):  # ввод темы письма
        return self.driver.find_element_by_class_name("mail-Compose-Field-Input-Controller").send_keys('Резюме')

    def button_to_send(self): # нажать кнопку "Отправить"
        return self.driver.find_element_by_class_name('_nb-large-action-button').click() 

    def text_email(self): # возвращает ссылку на резюме 
        hh_link = self.hh_resume.copy_url_resume()
        return self.driver.find_element_by_class_name('cke_wysiwyg_div').send_keys(hh_link)

    def download_by_attach(self): # возвращает аттач в письмо
        return self.hh_resume.download_resume()
        #return self.driver.find_element_by_class_name('cke_wysiwyg_div').send_keys(hh_download)

    def email_send(self): #написать письмо
        self.click_botton_created_email()
        self.input_address()
        self.input_theme_email()
        self.text_email()
        self.button_to_send()

    def email_send_by_attach(self): #написать письмо с аттачем
        self.click_botton_created_email()
        self.input_address()
        self.input_theme_email()
        self.download_by_attach()
        self.file_input = self.driver.find_element_by_xpath("//*[@name='att']")
        self.file_input.send_keys("/home/inna/Загрузки/Кузьмина Инна Сергеевна.pdf")
        self.driver.find_element_by_class_name('cke_wysiwyg_div').send_keys(private.TEXT_MY_RESUME)
        self.button_to_send()

    def mail_send(self): #тест залогиниться и отправить письмо
        self.open_login_form()
        self.email_send()

    def test_mail_send_by_attche(self): #тест залогиниться и отправить письмо с вложением
        self.open_login_form()
        self.email_send_by_attach()

    def is_visible(self): 
        print(self.driver.find_element_by_link_text('Почта').is_displayed()) # проверяет наличие элемента на странице


if __name__ == '__main__':
    unittest.main()

