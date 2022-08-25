import time

import allure
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilites.logger import Logger


class Select_smartphone_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators


    button_show_more = "//div[contains(@class, 'CatalogCategoryMenu__box')]/a[contains(text(), 'Смартфоны')]/..//div[contains(@class, 'Menu__subcategories_hidden')]//span"
    link_smartphones_android = "//div[contains(@class, 'CatalogCategoryMenu__box')]/a[contains(text(), 'Смартфоны')]/..//div[@class='CatalogCategoryMenu__subcategories-more']/div[2]/a"
    subcategory_name = "//h1[contains(@class, 'Subcategory__title')]"
    checkbox_available = "//input[@id='available.instore']"
    filter_price_min = "//div[@class='e1514ezh0 css-1tn5u6r elalcrq0']//input[@name='input-min']"
    filter_price_max = "//div[@class='e1514ezh0 css-1tn5u6r elalcrq0']//input[@name='input-max']"
    radiobutton_discount_10 = "//input[@name='discount.price1_10']"
    checkbox_256gb = "//div[@data-meta-value='256 ГБ']"
    sort_by_price = "//div[@data-alias='price']"
    select_product = "//a[@title='Смартфон Xiaomi Poco F3 8/256Gb,  черный']"
    button_add_to_cart = "//div[contains(@class, 'button')]/button[contains(@data-label, 'корзину')]"


    # Getters


    def get_button_show_more(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.button_show_more)))

    def get_link_smartphones_android(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.link_smartphones_android)))

    def get_subcategory_name(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.subcategory_name)))

    def get_checkbox_available(self):
        return self.driver.find_element(By.XPATH, self.checkbox_available)

    def get_filter_price_min(self):
        return self.driver.find_element(By.XPATH, self.filter_price_min)

    def get_filter_price_max(self):
        return self.driver.find_element(By.XPATH, self.filter_price_max)

    def get_radiobutton_discount_10(self):
        return self.driver.find_element(By.XPATH, self.radiobutton_discount_10)

    # def get_checkbox_256gb(self):
    #     return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_256gb)))

    def get_checkbox_256gb(self):
        return self.driver.find_element(By.XPATH, self.checkbox_256gb)

    def get_sort_by_price(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.sort_by_price)))

    def get_select_product(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.select_product)))

    def get_button_add_to_cart(self):
        return self.driver.find_element(By.XPATH, self.button_add_to_cart)




    # Actions

    def click_button_show_more(self):
        self.get_button_show_more().click()
        print("Click button: Показать еще")

    def click_link_smartphones_android(self):
        self.get_link_smartphones_android().click()
        print("Click Smartphones Android")

    def click_checkbox_available(self):
        self.get_checkbox_available().click()
        print("Click checkbox: Забрать через 5 минут")

    def input_filter_price_min(self, price_min):
        self.get_filter_price_min().click()
        self.get_filter_price_min().send_keys(Keys.CONTROL + "a")
        self.get_filter_price_min().send_keys(Keys.BACKSPACE)
        self.get_filter_price_min().send_keys(price_min)
        print("Input Filter price min")

    def input_filter_price_max(self, price_max):
        self.get_filter_price_max().click()
        self.get_filter_price_max().send_keys(Keys.CONTROL + "a")
        self.get_filter_price_max().send_keys(Keys.BACKSPACE)
        self.get_filter_price_max().send_keys(price_max)
        self.get_filter_price_min().send_keys(Keys.ENTER)
        print("Input Filter price max")

    def click_radiobutton_discount_10(self):
        self.get_radiobutton_discount_10().click()
        print("Click radiobutton : 10% и больше")

    def click_checkbox_256gb(self):
        self.get_checkbox_256gb().click()
        print("Click : 256 Гб")

    def click_sort_by_price(self):
        self.get_sort_by_price().click()
        print("По цене")

    def click_select_product(self):
        self.get_select_product().click()
        print("Click select product")


    def click_button_add_to_cart(self):
        self.get_button_add_to_cart().click()
        print("Click button : В корзину")




    # Methods

    def select_smartphone(self):
        with allure.step("Select smartphone"):
            Logger.add_start_step(method="select_smartphone")
            self.get_current_url()
            self.click_button_show_more()
            self.click_link_smartphones_android()
            self.assert_word(self.get_subcategory_name(), 'Смартфоны на Android')
            self.driver.execute_script("window.scrollTo(0, 500)")
            self.click_checkbox_available()
            time.sleep(5)
            self.input_filter_price_min("30000")
            self.input_filter_price_max("50000")
            self.driver.execute_script("window.scrollTo(0, 1000)")
            time.sleep(5)
            self.click_radiobutton_discount_10()
            self.driver.execute_script("window.scrollTo(0, 2500)")
            self.click_checkbox_256gb()
            self.driver.execute_script("window.scrollTo(0, 100)")
            self.click_sort_by_price()
            time.sleep(2)
            self.driver.execute_script("window.scrollTo(0, 200)")
            self.click_select_product()
            self.click_button_add_to_cart()
            Logger.add_end_step(url=self.driver.current_url, method="select_smartphone")




