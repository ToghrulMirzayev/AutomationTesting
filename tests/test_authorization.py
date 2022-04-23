import pytest
import allure
from pom.authorization import AuthorizationSteps, AuthorizationAsserts


@allure.story('Authorization test cases')
@pytest.mark.usefixtures('setup')
class TestAuthorization:

    @pytest.mark.ui
    @allure.label("owner", "QA Engineer")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('Checking successful login')
    def test_successful_login(self):
        driver = self.driver
        authorization_steps = AuthorizationSteps(driver)
        authorization_asserts = AuthorizationAsserts(driver)
        with allure.step('Enter correct username'):
            authorization_steps.enter_correct_username()
        with allure.step('Enter correct password'):
            authorization_steps.enter_correct_password()
        with allure.step('Clicking to login button'):
            authorization_steps.click_to_login_button()
        with allure.step('verification successful login'):
            authorization_asserts.assertion_text_product_on_main_page()

    @pytest.mark.ui
    @allure.label("owner", "QA Engineer")
    @allure.severity(allure.severity_level.MINOR)
    @allure.description('Checking unsuccessful login with incorrect username')
    def test_unsuccessful_login_with_incorrect_username(self):
        driver = self.driver
        authorization_steps = AuthorizationSteps(driver)
        authorization_asserts = AuthorizationAsserts(driver)
        with allure.step('Enter incorrect username'):
            authorization_steps.enter_incorrect_username()
        with allure.step('Enter correct password'):
            authorization_steps.enter_correct_password()
        with allure.step('Clicking to login button'):
            authorization_steps.click_to_login_button()
        with allure.step('Verification that login is unsuccessful due to incorrect credentials'):
            authorization_asserts.assertion_text_if_wrong_credentials_are_entered()

    @pytest.mark.ui
    @allure.label("owner", "QA Engineer")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('Checking unsuccessful login with incorrect password')
    def test_unsuccessful_login_with_incorrect_password(self):
        driver = self.driver
        authorization_steps = AuthorizationSteps(driver)
        authorization_asserts = AuthorizationAsserts(driver)
        with allure.step('Enter correct username'):
            authorization_steps.enter_correct_username()
        with allure.step('Enter incorrect password'):
            authorization_steps.enter_incorrect_password()
        with allure.step('Clicking to login button'):
            authorization_steps.click_to_login_button()
        with allure.step('Verification that login is unsuccessful due to incorrect credentials'):
            authorization_asserts.assertion_text_if_wrong_credentials_are_entered()

    @pytest.mark.ui
    @allure.label("owner", "QA Engineer")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description('Checking successful logIn')
    def test_successful_logout(self):
        driver = self.driver
        authorization_steps = AuthorizationSteps(driver)
        authorization_asserts = AuthorizationAsserts(driver)
        with allure.step('Enter correct username'):
            authorization_steps.enter_correct_username()
        with allure.step('Enter correct password'):
            authorization_steps.enter_correct_password()
        with allure.step('Clicking to login button'):
            authorization_steps.click_to_login_button()
        with allure.step('Clicking to burger menu'):
            authorization_steps.click_to_burger_menu()
        with allure.step('Clicking to logOut button'):
            authorization_steps.click_to_logout_button()
        with allure.step('Verify that logged out successfully'):
            authorization_asserts.assertion_login_button_on_main_page()
