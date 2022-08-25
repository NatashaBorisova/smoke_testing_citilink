import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilites.logger import Logger


class Main_page(Base):

    url = "https://www.citilink.ru/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    link_select_city = "//div[@class='MainHeader__city-block']//div[contains(@class, 'MainHeader__city')]"
    select_city_moscow = "//a[text()='Москва']"
    button_catalog = "//button[contains(@class, 'js--PopupCatalogMenu__button-open')]"
    button_smartphones = "//a[@data-category-alias='mobile']"
    category_name = "//h1[contains(@class, 'Category__title')]"


    # Getters


    def get_link_select_city(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.link_select_city)))

    def get_select_city_moscow(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.select_city_moscow)))

    def get_button_catalog(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.button_catalog)))

    def get_button_smartphones(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.button_smartphones)))

    def get_category_name(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.category_name)))


    # Actions

    def click_link_select_city(self):
        self.get_link_select_city().click()
        print("Click select city")

    def click_select_city_moscow(self):
        self.get_select_city_moscow().click()
        print("Click city Moscow")

    def click_button_catalog(self):
        self.get_button_catalog().click()
        print("Click button Catalog")

    def click_button_smartphones(self):
        self.get_button_smartphones().click()
        print("Click button Smartphones")



    # Methods

    def catalog(self):
        with allure.step("Catalog"):
            Logger.add_start_step(method="catalog")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_link_select_city()
            self.click_select_city_moscow()
            self.click_button_catalog()
            self.click_button_smartphones()
            self.assert_word(self.get_category_name(), 'Смартфоны и гаджеты')
            Logger.add_end_step(url=self.driver.current_url, method="catalog")
