from selenium import webdriver
import unittest

class ValidEmailTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_valid_email(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8085/register/")
        first_name = driver.find_element_by_name("firstName")
        last_name = driver.find_element_by_name("lastName")
        password = driver.find_element_by_name("password")
        repassword = driver.find_element_by_name("repassword")
        email = driver.find_element_by_name("email")
        phone_number = driver.find_element_by_name("phoneNumber")
        register_button = driver.find_element_by_name("sendButton")
        first_name.send_keys("ali")
        last_name.send_keys("alavi")
        password.send_keys("1234")
        repassword.send_keys("1234")
        email.send_keys("aligmail.com")
        phone_number.send_keys("09121234567")
        register_button.click()
        assert driver.find_element_by_name("invalidEmail") is not None

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()