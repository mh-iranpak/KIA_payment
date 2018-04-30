from selenium import webdriver
import unittest


class PasswordsEqualityTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_passwords_equality(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8085/register/")
        first_name = driver.find_element_by_name("firstName")
        last_name = driver.find_element_by_name("lastName")
        password = driver.find_element_by_name("password")
        repassword = driver.find_element_by_name("repassword")
        email = driver.find_element_by_name("email")
        phone_number = driver.find_element_by_name("phoneNumber")
        register_button = driver.find_element_by_name("registerButton")
        first_name.send_keys("ali")
        last_name.send_keys("alavi")
        password.send_keys("1234")
        repassword.send_keys("123456")
        email.send_keys("aligmail.com")
        phone_number.send_keys("09121234567")
        register_button.click()
        assert driver.find_element_by_name("notEqualPasswords") is not None

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()