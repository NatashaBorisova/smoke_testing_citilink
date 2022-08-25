import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilites.logger import Logger


class Cart_information_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    cart_product_name = "//div[contains(@class, 'ProductCardForBasket__header')]/a[not(contains(@class, 'name-mobile'))]"
    cart_product_price = "//span[contains(@class, 'ProductCardForBasket__price-current_current-price')]"
    cart_current_price = "//span[contains(@class, 'OrderFinalPrice__price-current_current-price')]"
    button_checkout = "//button[contains(@class, 'OrderFinalPrice__order-button')]"



    # Getters

    def get_cart_product_name(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.cart_product_name)))

    def get_cart_product_price(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.cart_product_price)))

    def get_cart_current_price(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.cart_current_price)))

    def get_button_checkout(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.button_checkout)))



    # Actions


    def click_button_checkout(self):
        self.get_button_checkout().click()
        print("Click button : Перейти к оформлению")




    # Methods

    def cart_info(self):
        with allure.step("Cart info"):
            Logger.add_start_step(method="cart_info")
            self.get_current_url()
            self.assert_word(self.get_cart_product_name(), 'Смартфон Xiaomi Poco F3 8/256Gb, черный')
            self.assert_word(self.get_cart_product_price(), '34 990')
            self.assert_word(self.get_cart_current_price(), '34 990')
            self.click_button_checkout()
            Logger.add_end_step(url=self.driver.current_url, method="cart_info")
