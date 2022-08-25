import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilites.logger import Logger


class Product_information_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    select_product_name = "//div[contains(@class, 'ProductCardForUpsale__name')]"
    select_product_price = "//span[contains(@class, 'ProductCardForUpsale__price-current_current-price')]"
    button_go_to_cart = "//div[contains(@class, 'UpsaleBasket__buttons')]//button[contains(@class, 'UpsaleBasket__order')]"



    # Getters

    def get_select_product_name(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.select_product_name)))

    def get_select_product_price(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.select_product_price)))

    def get_button_go_to_cart(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.button_go_to_cart)))



    # Actions


    def click_button_go_to_cart(self):
        self.get_button_go_to_cart().click()
        print("Click button : Перейти в корзину")




    # Methods

    def product_info(self):
        with allure.step("Product info"):
            Logger.add_start_step(method="product_info")
            self.get_current_url()
            self.assert_word(self.get_select_product_name(), 'Смартфон Xiaomi Poco F3 8/256Gb, черный')
            self.assert_word(self.get_select_product_price(), '34 990')
            self.click_button_go_to_cart()
            Logger.add_end_step(url=self.driver.current_url, method="product_info")
