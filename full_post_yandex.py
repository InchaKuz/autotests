from post_yandex import Yandex_Post.
from post_yandex import TestOpenLoginFform
from post_yandex import EmailSend

driver = webdriver.Chrome('/home/inna/Project/autotests/chromedriver')
url = 'https://yandex.ru/'


def criated_email(url):
	open_chrome = setUp()
	login_form = TestOpenLoginFform()
	time.sleep(5)
	send_email = EmailSend()


criated_email(url)
