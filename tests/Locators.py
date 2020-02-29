from selenium import webdriver
from selenium.webdriver.common.by import By


class Locators():
    SEARCH_TEXTBOX = (By.ID, "twotabsearchtextbox")
    SEARCH_SUBMIT_BUTTON = (By.XPATH, "//div[contains(@class,'nav-search-submit')]/input")
    SEARCH_RESULT_LINK = (By.XPATH, "(//div[@class='sg-col-inner']//img[contains(@data-image-latency,'s-product-image')])[2]")
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-button")
    DELETE_ITEM_LINK = (By.XPATH, "//div[contains(@class,'a-row sc-action-links')]//span[contains(@class,'sc-action-delete')]")
    # DELETE_ITEM_LINK = (By.XPATH, "//*[@class='a-size-small sc-action-delete']")
    SUB_CART_DIV = (By.ID, "hlb-subcart")
    PROCEED_TO_BUY_BUTTON = (By.ID, "hlb-ptc-btn-native")
    CART_COUNT = (By.ID, "nav-cart-count")
    CART_LINK = (By.ID, "nav-cart")
    PROCEED_TO_CHECKOUT_BUTTON = (By.NAME, "proceedToCheckout")
    USER_EMAIL_OR_MOBIL_NO_TEXTBOX = (By.ID, "ap_email")
