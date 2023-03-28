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


class Cart_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators


    product_text = "//div[@class='inventory_item_name']"
    product_price = "//div[@class='inventory_item_price']"


    add_to_cart_paragraph_text = "//span[@class='title']"
    checkout_button = "//button[@id='checkout']"

    #Constants

    PRODUCT_1_TEXT = 'Sauce Labs Backpack'
    PRODUCT_1_PRICE = '$29.99'

    #Getters

    def get_product_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_text)))

    def get_product_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_price)))


    def get_paragraph_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_paragraph_text)))

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))



    #Actions

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print('Item added to cart')

    #Methods

    def cart_test_product_1(self):
        self.get_current_url()
        self.assert_url('https://www.saucedemo.com/cart.html')
        self.check_text(self.get_paragraph_text(), 'Your Cart')
        self.check_text(self.get_product_text(),'Sauce Labs Backpack')
        self.check_text(self.get_product_price(),'$29.99')
        self.click_checkout_button()

    def cart_test_product_2(self):
        self.get_current_url()
        self.assert_url('https://www.saucedemo.com/cart.html')
        self.check_text(self.get_paragraph_text(), 'Your Cart')
        self.check_text(self.get_product_text(),'Sauce Labs Bike Light')
        self.check_text(self.get_product_price(),'$9.99')
        self.click_checkout_button()

    def cart_test_product_3(self):
        self.get_current_url()
        self.assert_url('https://www.saucedemo.com/cart.html')
        self.check_text(self.get_paragraph_text(), 'Your Cart')
        self.check_text(self.get_product_text(),'Sauce Labs Bolt T-Shirt')
        self.check_text(self.get_product_price(),'$15.99')
        self.click_checkout_button()

    def cart_test_product_4(self):
        self.get_current_url()
        self.assert_url('https://www.saucedemo.com/cart.html')
        self.check_text(self.get_paragraph_text(), 'Your Cart')
        self.check_text(self.get_product_text(),'Sauce Labs Fleece Jacket')
        self.check_text(self.get_product_price(),'$49.99')
        self.click_checkout_button()

    def cart_test_product_5(self):
        self.get_current_url()
        self.assert_url('https://www.saucedemo.com/cart.html')
        self.check_text(self.get_paragraph_text(), 'Your Cart')
        self.check_text(self.get_product_text(),'Sauce Labs Onesie')
        self.check_text(self.get_product_price(),'$7.99')
        self.click_checkout_button()

    def cart_test_product_6(self):
        self.get_current_url()
        self.assert_url('https://www.saucedemo.com/cart.html')
        self.check_text(self.get_paragraph_text(), 'Your Cart')
        self.check_text(self.get_product_text(),'Test.allTheThings() T-Shirt (Red)')
        self.check_text(self.get_product_price(),'$15.99')
        self.click_checkout_button()







