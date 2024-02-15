from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestCustomer(unittest.TestCase):

    def testCase1(self):
        driver = None
        driver_path = "D:\\webdriver\\chromedriver.exe"
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-extensions")
        driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)
        
        driver.get("http://localhost/customer/form.html")
        
        firstNameInput = driver.find_element(By.ID, "first-name")
        lastNameInput = driver.find_element(By.ID, "last-name")
        ageInput = driver.find_element(By.ID, "age")
        submitButton = driver.find_element(By.ID, "sub")
        firstNameInput.send_keys("johnjohn")
        lastNameInput.send_keys("canonc")
        ageInput.send_keys("2")

        # Submit the form
        submitButton.click()
        
        result = driver.find_element(By.ID, "firstname").text
        self.assertEqual("First Name: johnjohn", result)

        driver.save_screenshot("test_case1.png")
        time.sleep(2)  # หน่วงเวลา 5 วินาที
        driver.close()  # แก้ไขเป็น driver.close() แทน self.driver.close()

if __name__ == "__main__":
    unittest.main()




        