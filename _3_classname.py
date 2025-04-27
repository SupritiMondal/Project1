'''
class name  :   If we are having class attribute, we can go for class name locator.
                Class is not unique

                DRAWBACKS
                1.  class is not unique.
                    Whenever we are having multiple occurances, class name will always consider the first occurance
                2.  class name cannot locate the spaces, so whenever we are having space, we should replace the space with dot
'''
import time

## Eg1
from selenium import webdriver
driver = webdriver.Firefox()

driver.get('https://demowebshop.tricentis.com/')
time.sleep(2)
driver.find_element('class name', 'ico-register').click()
time.sleep(2)
driver.find_element('class name', 'ico-login').click()
time.sleep(2)
driver.find_element('class name', 'cart-label').click()

##################################################################################################

## Eg2

from selenium import webdriver
driver = webdriver.Firefox()

driver.get('https://www.saucedemo.com/')
time.sleep(2)
driver.find_element('class name', 'input_error form_input').send_keys('standard_user')

## ERROR
## Because the class name value is having space in it.
## Class name locator cannot locate the elements if it is having space in it

## To overcome the above drawback, we will replace the soace with .(dot)

#-------------------------------------------------------


from selenium import webdriver
driver = webdriver.Firefox()

driver.get('https://www.saucedemo.com/')
time.sleep(2)
driver.find_element('class name', 'input_error.form_input').send_keys('standard_user')

## WORKS FINE

##########################################################################################

## Eg3

from selenium import webdriver
driver = webdriver.Firefox()

driver.get('https://www.saucedemo.com/')
time.sleep(2)
driver.find_element('class name', 'input_error.form_input').send_keys('standard_user')
time.sleep(1)
driver.find_element('class name', 'input_error.form_input').send_keys('secret_sauce')

## Both username and password will be filled in the username section only
## Whenever we are having multiple occurances, class name will always consider the first occurance



























































