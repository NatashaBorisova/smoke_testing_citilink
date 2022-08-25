import time
import allure

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from base.base_class import Base
from pages.cart_page import Cart_information_page
from pages.main_page import Main_page
from pages.order_page import Order_page
from pages.product_page import Product_information_page
from pages.select_smartphone_page import Select_smartphone_page


@allure.description("Test buy smartphone")
def test_buy_smartphone(set_group, set_up):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path='C:\\Users\\ILLUZIA\\PycharmProjects\\driver\\chromedriver.exe', chrome_options=options)



    # открываем главную страницу, переходим в каталог и выбираем категорию "Смартфоны"

    main_page = Main_page(driver)
    main_page.catalog()

    # выбираем товар

    select_smartphone = Select_smartphone_page(driver)
    select_smartphone.select_smartphone()

    # проверяем информацию о товаре и переходим в корзину

    product_information = Product_information_page(driver)
    product_information.product_info()

    # делаем скриншот

    screenshots = Base(driver)
    screenshots.get_screenshot()

    # проверяем информацию о товаре в корзине

    cart_information = Cart_information_page(driver)
    cart_information.cart_info()

    # делаем скриншот

    screenshots = Base(driver)
    screenshots.get_screenshot()

    # оформляем заказ

    order = Order_page(driver)
    order.order()

    # делаем скриншот

    screenshots = Base(driver)
    screenshots.get_screenshot()



    time.sleep(5)

