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


class Main_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    paragraph_text = "//span[@class='title']"
    product_1_text = "//div[text()='Sauce Labs Backpack']"
    product_1_price = "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div"
    product_2_text = "//div[text()='Sauce Labs Bike Light']"
    product_2_price = "//*[@id='inventory_container']/div/div[2]/div[2]/div[2]/div"
    product_3_text = "//div[text()='Sauce Labs Bolt T-Shirt']"
    product_3_price = "//*[@id='inventory_container']/div/div[3]/div[2]/div[2]/div"
    product_4_text = "//div[text()='Sauce Labs Fleece Jacket']"
    product_4_price = "//*[@id='inventory_container']/div/div[4]/div[2]/div[2]/div"
    product_5_text = "//div[text()='Sauce Labs Onesie']"
    product_5_price = "//*[@id='inventory_container']/div/div[5]/div[2]/div[2]/div"
    product_6_text = "//div[text()='Test.allTheThings() T-Shirt (Red)']"
    product_6_price = "//*[@id='inventory_container']/div/div[6]/div[2]/div[2]/div"

    add_to_cart_button_product_1 = "//button[@id='add-to-cart-sauce-labs-backpack']"
    add_to_cart_button_product_2 = "//button[@id='add-to-cart-sauce-labs-bike-light']"
    add_to_cart_button_product_3 = "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"
    add_to_cart_button_product_4 = "//button[@id='add-to-cart-sauce-labs-fleece-jacket']"
    add_to_cart_button_product_5 = "//button[@id='add-to-cart-sauce-labs-onesie']"
    add_to_cart_button_product_6 = "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']"



    cart_icon_product = "//div[@id='shopping_cart_container']"
    burger_menu = "//button[@id='react-burger-menu-btn']"
    about_link = "//a[@id='about_sidebar_link']"

   # Constants (Just to know the names and prices)

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

    def get_products_paragraph_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.paragraph_text)))


    def get_product_1_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_1_text)))

    def get_product_1_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_1_price)))

    def get_product_2_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_2_text)))

    def get_product_2_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_2_price)))

    def get_product_3_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_3_text)))

    def get_product_3_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_3_price)))

    def get_product_4_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_4_text)))

    def get_product_4_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_4_price)))

    def get_product_5_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_5_text)))

    def get_product_5_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_5_price)))

    def get_product_6_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_6_text)))

    def get_product_6_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_6_price)))




    def get_add_to_cart_product_1_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button_product_1)))

    def get_add_to_cart_product_2_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button_product_2)))

    def get_add_to_cart_product_3_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button_product_3)))

    def get_add_to_cart_product_4_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button_product_4)))

    def get_add_to_cart_product_5_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button_product_5)))

    def get_add_to_cart_product_6_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button_product_6)))

    def get_cart_icon(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_icon_product)))

    def get_burger_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.burger_menu)))

    def get_about_link(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.about_link)))



    #Actions

    def click_add_to_cart_button(self):
        self.get_add_to_cart_product_1_button().click()
        print('Item 1 added to cart')

    def click_add_to_cart_button_2(self):
        self.get_add_to_cart_product_2_button().click()
        print('Item 2 added to cart')

    def click_add_to_cart_button_3(self):
        self.get_add_to_cart_product_3_button().click()
        print('Item 3 added to cart')

    def click_add_to_cart_button_4(self):
        self.get_add_to_cart_product_4_button().click()
        print('Item 3 added to cart')

    def click_add_to_cart_button_5(self):
        self.get_add_to_cart_product_5_button().click()
        print('Item 3 added to cart')

    def click_add_to_cart_button_6(self):
        self.get_add_to_cart_product_6_button().click()
        print('Item 3 added to cart')


    def cart_icon_click(self):
        self.get_cart_icon().click()
        print('Click cart icon')

    def burger_menu_click(self):
        self.get_burger_menu().click()
        print('Click burger menu')

    def about_link_click(self):
        self.get_about_link().click()
        print('Click about link')

    #Methods

    def verify_page(self):
        self.get_current_url()
        self.assert_url('https://www.saucedemo.com/inventory.html')
        self.check_text(self.get_products_paragraph_text(),'Products')

    def select_product_1(self):
        self.check_text(self.get_product_1_text(), 'Sauce Labs Backpack')
        self.check_text(self.get_product_1_price(), '$29.99')
        self.click_add_to_cart_button()
        self.cart_icon_click()

    def select_product_2(self):
        self.check_text(self.get_product_2_text(),'Sauce Labs Bike Light')
        self.check_text(self.get_product_2_price(),'$9.99')
        self.click_add_to_cart_button_2()
        self.cart_icon_click()

    def select_product_3(self):
        self.check_text(self.get_product_3_text(), 'Sauce Labs Bolt T-Shirt')
        self.check_text(self.get_product_3_price(), '$15.99')
        self.click_add_to_cart_button_3()
        self.cart_icon_click()

    def select_product_4(self):
        self.check_text(self.get_product_4_text(), 'Sauce Labs Fleece Jacket')
        self.check_text(self.get_product_4_price(), '$49.99')
        self.click_add_to_cart_button_4()
        self.cart_icon_click()

    def select_product_5(self):
        self.check_text(self.get_product_5_text(),'Sauce Labs Onesie')
        self.check_text(self.get_product_5_price(), '$7.99')
        self.click_add_to_cart_button_5()
        self.cart_icon_click()

    def select_product_6(self):
        self.check_text(self.get_product_6_text(),'Test.allTheThings() T-Shirt (Red)')
        self.check_text(self.get_product_6_price(), '$15.99')
        self.click_add_to_cart_button_6()
        self.cart_icon_click()

    def go_to_about_link(self):
        self.get_current_url()
        self.burger_menu_click()
        self.about_link_click()
        self.assert_url('https://saucelabs.com/')
        self.get_current_url()






