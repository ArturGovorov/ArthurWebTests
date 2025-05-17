from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FIELD = (By.ID, 'field_email')
    LOGIN_BUTTON = (By.XPATH, '//*[@data-l="t,sign_in"]')
    PASSWORD = (By.XPATH, '//*[@data-l="t,password"]')
    QR_CODE = (By.ID, 'qrCode-4467669758')
    QR_CODE_BUTTON = (By.XPATH, '//*[@data-l="t,get_qr"]')
    LOGIN_ERROR = (By.XPATH, '//*[@data-l="t,restore"]')
    REGISTER = (By.XPATH, '//*[@data-l="t,register"]')
    LOGIN_VIA_VK = (By.ID, 'tabpanel-login-4467669716')
    LOGIN_VIA_MAIL = (By.ID, 'tabpanel-login-4467669716')
    LOGIN_VIA_YANDEX = (By.ID, 'tabpanel-login-4467669716')



class LoginPageHelper(BasePage):
    pass
