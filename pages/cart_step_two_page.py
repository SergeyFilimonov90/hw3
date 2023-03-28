import time
import datetime
from datetime import date
import calendar
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import ActionChains,Keys
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class Cart_final_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators

    checkout_overview_paragraph = "//span[@class='title']"
    product_1_text = "//div[@class='inventory_item_name']"
    product_1_price = "//div[@class='inventory_item_price']"
    subtotal_price = "//div[@class='summary_subtotal_label']"
    finish_final_button = "//button[@id='finish']"

    #Constants

    PRODUCT_1_TEXT = 'Sauce Labs Backpack'
    PRODUCT_1_PRICE = '$29.99'
    PRODUCT_2_TEXT = 'Sauce Labs Bike Light'
    PRODUCT_2_PRICE = '$9.99'
    PRODUCT_3_TEXT = 'Sauce Labs Bolt T-Shirt'
    PRODUCT_3_PRICE = '$15.99'
    PRODUCT_4_TEXT = 'Sauce Labs Fleece Jacket'
    PRODUCT_4_PRICE = '$49.99'
    PRODUCT_5_TEXT = 'Sauce Labs Onesie'
    PRODUCT_5_PRICE = '$7.99'
    PRODUCT_6_TEXT = "Test.allTheThings() T-Shirt (Red)"
    PRODUCT_6_PRICE = "$15.99"

    #Getters


    def get_checkout_overview_paragraph_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_overview_paragraph)))


    def get_product_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_1_text)))

    def get_product_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_1_price)))

    def get_subtotal_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.subtotal_price)))

    def get_finish_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.finish_final_button)))



    #Actions

    def click_final_finish_button(self):
        self.get_finish_button().click()
        print('Click finish button')

    #Methods

    def cart_step_two_test_product_1(self):
        self.get_current_url()
        self.assert_url('https://www.saucedemo.com/checkout-step-two.html')
        self.check_text(self.get_checkout_overview_paragraph_text(), 'Checkout: Overview')
        self.check_text(self.get_product_text(),'Sauce Labs Backpack')
        self.check_text(self.get_product_price(),'$29.99')
        self.assert_final_cart_price(self.get_product_price())
        self.click_final_finish_button()

    def cart_step_two_test_product_2(self):
        self.get_current_url()
        self.assert_url('https://www.saucedemo.com/checkout-step-two.html')
        self.check_text(self.get_checkout_overview_paragraph_text(), 'Checkout: Overview')
        self.check_text(self.get_product_text(),'Sauce Labs Bike Light')
        self.check_text(self.get_product_price(),'$9.99')
        self.assert_final_cart_price(self.get_product_price())
        self.click_final_finish_button()

    def cart_step_two_test_product_3(self):
        self.get_current_url()
        self.assert_url('https://www.saucedemo.com/checkout-step-two.html')
        self.check_text(self.get_checkout_overview_paragraph_text(), 'Checkout: Overview')
        self.check_text(self.get_product_text(),'Sauce Labs Bolt T-Shirt')
        self.check_text(self.get_product_price(),'$15.99')
        self.assert_final_cart_price(self.get_product_price())
        self.click_final_finish_button()

    def cart_step_two_test_product_4(self):
        self.get_current_url()
        self.assert_url('https://www.saucedemo.com/checkout-step-two.html')
        self.check_text(self.get_checkout_overview_paragraph_text(), 'Checkout: Overview')
        self.check_text(self.get_product_text(),'Sauce Labs Fleece Jacket')
        self.check_text(self.get_product_price(),'$49.99')
        self.assert_final_cart_price(self.get_product_price())
        self.click_final_finish_button()


    def cart_step_two_test_product_5(self):
        self.get_current_url()
        self.assert_url('https://www.saucedemo.com/checkout-step-two.html')
        self.check_text(self.get_checkout_overview_paragraph_text(), 'Checkout: Overview')
        self.check_text(self.get_product_text(),'Sauce Labs Onesie')
        self.check_text(self.get_product_price(),'$7.99')
        self.assert_final_cart_price(self.get_product_price())
        self.click_final_finish_button()


    def cart_step_two_test_product_6(self):
        self.get_current_url()
        self.assert_url('https://www.saucedemo.com/checkout-step-two.html')
        self.check_text(self.get_checkout_overview_paragraph_text(), 'Checkout: Overview')
        self.check_text(self.get_product_text(),"Test.allTheThings() T-Shirt (Red)")
        self.check_text(self.get_product_price(),"$15.99")
        self.assert_final_cart_price(self.get_product_price())
        self.click_final_finish_button()








