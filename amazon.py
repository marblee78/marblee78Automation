# Import unittest module for creating unit tests

import unittest

# Import time module to implement

import time

# Import the Selenium 2 module (aka "webdriver")

from selenium import webdriver

# For automating data input

from selenium.webdriver.common.keys import Keys

# For providing custom configurations for Chrome to run

from selenium.webdriver.chrome.options import Options


# --------------------------------------

# Provide a class for the unit test case

class PythonOrgSearchChrome(unittest.TestCase):

    # Anything declared in setUp will be executed for all test cases

    def setUp(self):
        # Define a variable to hold all the configurations we want

        chrome_options = webdriver.ChromeOptions()

        # Define chrome option configurations here ...

        # Create driver, pass it the path to the chromedriver file and the special configurations you want to run

        self.driver = webdriver.Chrome(
            executable_path=r'C:\Users\Marion\Downloads\chromedriver.exe',
            chrome_options=chrome_options)

        # Window management hacks because I'm using OS X. On Windows or Linux you could just specify these as a ChromeOption

        self.driver.set_window_size(1920, 1080)

        self.driver.maximize_window()

    # An individual test case. Must start with 'test_' (as per unittest module)

    def test_search_in_python_chrome(self):
        # Assigning a local variable for the global driver

        driver = self.driver

        # Go to amazon.com

        driver.get('http://www.amazon.com')

        # A test to ensure the page has keyword Amazon in the page title

        self.assertIn("Amazon", driver.title)

        # Pauses the screen for 5 seconds so we have time to confirm it arrived at the right page

        #time.sleep(5)

        # Find and select the search box element on the page

        search_box = driver.find_element_by_name('field-keywords')

        # Enter text into the search box

        search_box.send_keys('brown sneakers men')

        # Make sure the results page returned something

        #assert "No results found." not in driver.page_source

        self.assertNotIn('No results found.', driver.page_source)

        # Fine and select the cart element on the page

        nav_cart = driver.find_element_by_id('nav-cart')

        # Make sure value is 0 items in cart

        self.assertIn('0 items in cart', driver.page_source)

        self.assertTrue(0<1)

        self.assertFalse(1<0)

        # Make sure page title equals 'Amazon.com: Online...'

        self.assertEqual(driver.title, 'Amazon.com: Online Shopping for Electronics, Apparel, Computers, Books, DVDs & more', msg='Title fail')

        # Submit the search box form

        search_box.submit()

        # Can also use Keys function to submit

        # search_box.send_keys(Keys.RETURN)

        # Another pause so we can see what's going on

        time.sleep(1)

        # verify page title equals 'Amazon.com: brown sneakers men'

        self.assertEqual(driver.title, 'Amazon.com: brown sneakers men')

        driver.find_element_by_id("pdagDesktopSparkleAsinContainer1").click()

        time.sleep(3)

        driver.find_element_by_id("dropdown_selected_size_name").click()

        driver.find_element_by_id("native_dropdown_selected_size_name_3").click()

        time.sleep(1)

        driver.find_element_by_id("add-to-cart-button").click()

        time.sleep(2)

        self.assertEqual(driver.title,"Amazon.com Shopping Cart")

        driver.find_element_by_id("hlb-ptc-btn-native").click()

        time.sleep(1)

        email_box = driver.find_element_by_name('email')

        email_box.send_keys('marblee78')

        pass_box = driver.find_element_by_name("password")

        pass_box.send_keys('marion')

        driver.find_element_by_id("signInSubmit").click()

        time.sleep(1)

        driver.find_element_by_id("auth-error-message-box")

        # Take a screenshot of the results

        driver.save_screenshot('screenshot-deskto-chrome.png')

    # Anything declared in tearDown will be executed for all test cases

    def tearDown(self):
        # Close the browser.

        # Note close() will close the current tab, if its the last tab it will close the browser. To close the browser entirely use quit()

        self.driver.close()

# Boilerplate code to start the unit tests

if __name__ == "__main__":
    unittest.main()
