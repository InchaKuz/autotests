import unittest #Встроенная библиотека
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 



import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='test.log'
                    )


class LoginAvito(unittest.TestCase): #класс наследую от Юниттест (способ сообщения что это тест)
    def setUp(self):
        self.driver = webdriver.Chrome('/Users/bladerrunner/projects/autotests/chromedriver 2') # открывает браузер перед тестом
        self.driver.get('https://www.avito.ru')

    def test_open_login_form(self):
        self.driver.find_element_by_link_text('Вход и регистрация').click()
        self.login_field = self.driver.find_element_by_name('login')
        self.login_field.send_keys('Byyy')
        self.login_field = self.driver.find_element_by_name('password')
        self.login_field.send_keys('Byyy')
        self.login_field.send_keys(Keys.ENTER)



if __name__ == '__main__':
    unittest.main()
        




