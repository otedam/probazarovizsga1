from datetime import datetime
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def find_element(driver, search_type, value):
    element = WebDriverWait(
        driver, 10).until(
        EC.visibility_of_element_located((search_type, value))
    )
    return element


browser = webdriver.Chrome("C://chromedriver.exe")
browser.get('https://witty-hill-0acfceb03.azurestaticapps.net/landtransfertax.html')

## TC01: üres kitöltés helyessége
# * ha nincs kitoltve az "Estimate of property you wish you to purchase:" mező de mégis csak megnyomjuk a "Go" feliratú gombot
# * ellenőrizzük, hogy a "Land Transfer Fee" feliratú mező pontosan üres marad-e
# * ellenőrizzük, hogy megjelenik-e a következő felirat: "Enter the property value before clicking Go button."
#
btn_go = find_element(browser, By.CLASS_NAME, 'btn-go')
btn_go.click()
attention = find_element(browser, By.CSS_SELECTOR, 'p[id="disclaimer"] strong')
print(attention.text)
assert attention.text == 'Enter the property value before clicking Go button.'
browser.close()

## TC02: helyes kitöltés helyes kitöltése
# * töltsük ki a következő adatokkal a formot:
#     * 33333
# * nyomjuk meg a "Go" feliratú gombot
# * ellenőrizzük, hogy a "Land Transfer Fee" feliratú mező pontosan: 16.665 értéket mutatja-e

browser = webdriver.Chrome("C://chromedriver.exe")
browser.get('https://witty-hill-0acfceb03.azurestaticapps.net/landtransfertax.html')

price = find_element(browser, By.ID, 'price')
price.send_keys('33333')
btn_go = find_element(browser, By.CLASS_NAME, 'btn-go')
btn_go.click()
tax = find_element(browser, By.ID, 'tax')
tax_value = tax.get_attribute('value')
assert tax_value == '166.665'
browser.close()