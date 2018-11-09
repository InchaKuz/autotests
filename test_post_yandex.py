import unittest
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from allure_commons.types import AttachmentType
import private
from hh_resume import HhResume
from pika_cat import SearchPikabu


class YandexPost(unittest.TestCase):
    def setUp(self):
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option('detach', True)
        with pytest.allure.step("Launch site"):
            self.driver = webdriver.Chrome('/home/inna/Project/autotests/chromedriver', options=self.chrome_options)
            self.driver.implicitly_wait(5)
        with pytest.allure.step("Verify Title loaded"):
            self.driver.get('https://yandex.ru/')
            #self.hh_resume = HhResume()
            self.pika_cat = SearchPikabu()

    @pytest.allure.step("Залогиниться в почту")
    def open_login_form(self):  # Войти в почту
        self.driver.find_element_by_link_text('Почта').click()
        self.driver.find_element_by_name('login').send_keys(private.LOGIN_YA)
        self.driver.find_element_by_name('passwd').send_keys(private.PASS_YA)
        allure.attach(self.driver.get_screenshot_as_png(), name='screenshot', attachment_type=AttachmentType.PNG)
        self.driver.find_element_by_xpath("//*[@class='passport-Button']").click()

    @pytest.allure.step("Написать письмо")
    def click_botton_created_email(self):  # кнопка "Написать письмо"
        return self.driver.find_element_by_xpath('//*[@href="#compose"]').click()

    def input_address(self):   # ввод адреса получателя "Кому"
        return self.driver.find_element_by_class_name("mail-Bubbles").send_keys(private.MY_EMAIL)

    def input_theme_email(self):  # ввод темы письма
        return self.driver.find_element_by_class_name("mail-Compose-Field-Input-Controller").send_keys('Резюме')

    @pytest.allure.step("Отправить")
    def button_to_send(self):  # нажать кнопку "Отправить"
        return self.driver.find_element_by_class_name('_nb-large-action-button').click()

    def text_email(self):  # возвращает ссылку на резюме
        hh_link = self.hh_resume.copy_url_resume()
        return self.driver.find_element_by_class_name('cke_wysiwyg_div').send_keys(hh_link)

    def download_by_attach(self):  # возвращает аттач в письмо
        return self.hh_resume.download_resume()

    def copy_url_pika(self):  # ссылка на пост с котиками
        pika_link = self.pika_cat.copy_url()
        return self.driver.find_element_by_class_name('cke_wysiwyg_div').send_keys(pika_link)

    def email_send(self):  # написать письмо
        allure.attach(self.click_botton_created_email(), name='screenshot', attachment_type=AttachmentType.PNG)
        self.input_address()
        self.input_theme_email()
        self.text_email()
        self.button_to_send()

    @pytest.allure.step("Создать письмо")
    def email_send_by_cat_pika(self):
        allure.attach(self.click_botton_created_email(), name='screenshot', attachment_type=AttachmentType.PNG)
        self.input_address()
        self.input_theme_email()
        self.copy_url_pika()
        self.button_to_send()

    def email_send_by_attach(self):  # написать письмо с аттачем
        self.click_botton_created_email()
        self.input_address()
        self.input_theme_email()
        self.download_by_attach()
        self.file_input = self.driver.find_element_by_xpath("//*[@name='att']")
        self.file_input.send_keys("/home/inna/Загрузки/Кузьмина Инна Сергеевна.pdf")
        self.driver.find_element_by_class_name('cke_wysiwyg_div').send_keys(private.TEXT_MY_RESUME)
        self.button_to_send()

    def mail_send(self):  # тест залогиниться и отправить письмо
        self.open_login_form()
        self.email_send()

    def mail_send_by_attche(self):  # тест залогиниться и отправить письмо с вложением
        self.open_login_form()
        self.email_send_by_attach()

    def is_visible(self):  # проверяет наличие элемента на странице
        print(self.driver.find_element_by_link_text('Почта').is_displayed())

    def test_email_pika_cat(self):  # тест залогинеться и отправить пост с Пикабу
        self.open_login_form()
        self.email_send_by_cat_pika()


if __name__ == '__main__':
    unittest.main()