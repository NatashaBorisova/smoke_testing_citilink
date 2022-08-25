import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilites.logger import Logger


class Order_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    checkout_product_name = "//div[contains(@class, 'CheckoutLayout__aside')]//span[contains(text(), 'Смартфон Xiaomi Poco F3 8/256Gb,  черный')]"
    checkout_product_price = "//div[contains(@class, 'CheckoutLayout__aside')]//span[text()='34 990']"
    first_name = "//input[@name='firstName']"
    last_name = "//input[@name='lastName']"
    phone = "//input[@name='phone']"
    additional_phone = "//input[@name='additionalPhone']"
    button_payment_card_online = "//label[text()='Банковской картой онлайн']"
    checkbox_confirm = "//div[text()='Данные получателя указаны верно']"
    check_email = "//div[contains(@class, 'ContactForCheckLayout__emailOrSms')]//input[contains(@class, 'inputStyledDecorator__input')]"





    # Getters

    def get_checkout_product_name(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.checkout_product_name)))

    def get_checkout_product_price(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.checkout_product_price)))

    def get_first_name(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_phone(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.phone)))

    def get_additional_phone(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.additional_phone)))

    def get_button_payment_card_online(self):
        return self.driver.find_element(By.XPATH, self.button_payment_card_online)

    def get_checkbox_confirm(self):
        return self.driver.find_element(By.XPATH, self.checkbox_confirm)

    def get_check_email(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.check_email)))





    # Actions

    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print("Input First Name")

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print("Input Last Name")

    def input_phone(self, phone):
        self.get_phone().send_keys(phone)
        print("Input Phone")

    def input_additional_phone(self, additional_phone):
        self.get_additional_phone().send_keys(additional_phone)
        print("Input Additional phone")

    def click_button_payment_card_online(self):
        self.get_button_payment_card_online().click()
        print("Click button : Банковской картой онлайн")

    def click_checkbox_confirm(self):
        self.get_checkbox_confirm().click()
        print("Click checkbox : Данные получателя указаны верно")

    def input_check_email(self, email):
        self.get_check_email().send_keys(email)
        print("Input Email")



    # Methods

    def order(self):
        with allure.step("Order"):
            Logger.add_start_step(method="order")
            self.get_current_url()
            self.assert_word(self.get_checkout_product_name(), 'Смартфон Xiaomi Poco F3 8/256Gb, черный')
            self.assert_word(self.get_checkout_product_price(), '34 990')
            self.driver.execute_script("window.scrollTo(0, 500)")
            self.input_first_name("Test")
            self.input_last_name("Test")
            self.input_phone("1111111111")
            self.input_additional_phone("1111111112")
            self.driver.execute_script("window.scrollTo(0, 1100)")
            self.click_button_payment_card_online()
            time.sleep(5)
            self.click_checkbox_confirm()
            self.input_check_email("test@test.ru")
            self.assert_url("https://www.citilink.ru/order/checkout/")
            Logger.add_end_step(url=self.driver.current_url, method="order")



