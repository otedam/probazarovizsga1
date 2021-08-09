from datetime import datetime
import time

from selenium import webdriver
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
browser.get('https://witty-hill-0acfceb03.azurestaticapps.net/salestax.html')
time.sleep(2)

# elem lekérdezések

## TC01: üres kitöltés helyessége
# nem kell ellenőrizni, hogy üresek-e a mezők, csak azt, hogy alapból a "Subtotal" feliratú gomb megnyomásakor a `salestax` azonosítójú mező 0.00 értéket kell mutasson.
# illetve a "Calculate Order" gomb megyomására a `gtotal` mező 4.95 értéket kell mutasson

subtotalBtn = find_element(browser, By.ID, 'subtotalBtn')
subtotalBtn.click()
subtotal = find_element(browser, By.ID, 'subtotal')
subtotal_text = subtotal.get_attribute('value')
print(subtotal_text)
assert subtotal_text == "0.00"

gtotalBtn = find_element(browser, By.ID, 'gtotalBtn')
gtotalBtn.click()
gtotal_text = browser.find_element_by_id('gtotal').get_attribute('value')
print(gtotal_text)
assert gtotal_text == "4.95"
browser.close()
## TC02: 6" x 6" Volkanik Ice kitöltés helyessége
# válasszuk ki a Product Item feliratú mezőből a `6" x 6" Volkanik Ice` értéket
# a quantity feliratú mezőbe írjunk 1-et
# ellenőrizzük, hogy a "Subtotal" feliratú gomb megnyomásakor a `salestax` azonosítójú mező 4.95 értéket kell mutasson.
# illetve a "Calculate Order" gomb megyomására a `gtotal` mező 9.90 értéket kell mutasson

browser = webdriver.Chrome("C://chromedriver.exe")
browser.get('https://witty-hill-0acfceb03.azurestaticapps.net/salestax.html')
proditem = Select(browser.find_element_by_id('Proditem'))
proditem.select_by_index(1)
 #   ('6" x 6" Volkanik Ice')
quantity = find_element(browser, By.ID, 'quantity')
quantity.send_keys('1')
subtotalBtn = find_element(browser, By.ID, 'subtotalBtn')
subtotalBtn.click()
subtotal = find_element(browser, By.ID, 'subtotal')
subtotal_text = subtotal.get_attribute('value')
print(subtotal_text)
assert subtotal_text == "4.95"

gtotalBtn = find_element(browser, By.ID, 'gtotalBtn')
gtotalBtn.click()
time.sleep(2)
gtotal_text = browser.find_element_by_id('gtotal').get_attribute('value')
print(gtotal_text)
assert gtotal_text == "9.90"

browser.close()
