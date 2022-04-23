# Here I've used several locators for web elements
class AuthorizationLocators:
    FIND_USERNAME_FIELD_ID = 'user-name'
    FIND_PASSWORD_FIELD_ID = 'password'
    FIND_LOGIN_BUTTON_ID = 'login-button'
    FIND_LOGOUT_BUTTON_ID = 'logout_sidebar_link'
    FIND_WRONG_CREDENTIALS_ERROR_TEXT_TAG_NAME = '[data-test="error"]'


class PageElementLocators:
    FIND_PRODUCTS_TEXT_ON_LOGGED_PAGE_CLASS = 'title'
    FIND_BURGER_MENU_XPATH = '/html/body/div/div/div/div[1]/div[1]/div[1]/div/div[1]/div/button'
