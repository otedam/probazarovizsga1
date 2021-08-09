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
browser.get('https://witty-hill-0acfceb03.azurestaticapps.net/lottery.html')

# elem lekérdezések



## TC01: lotto huzas elott nem ismertek a szamok
#* nem szabad, hogy akár csak egy szám is megjelenjen mielőt az első alkalommal a "Generate" feliratú gombra kattintunk

try:
    balls_list = WebDriverWait(browser, 5).until(
        # EC.visibility_of_all_elements_located((By.XPATH, '//div[@balls]')))
        EC.visibility_of_all_elements_located((By.CLASS_NAME, 'balls')))
except:
    print("Még nincs húzott szám!")

## TC02: lottohuzás működik
#* Nyomjuk meg hatszor a "Generate" feliratú gombot
#* Ellenőrizzük, hogy pontosan 6db szám jelenik meg a képernyőn
#* Olvassuk ki a számokat és ellnőrizzük, hogy mind 1 és 59 között vannak

ism = 6
for i in range(ism):
    generate = find_element(browser, By.ID, 'draw-number')
    generate.click()
time.sleep(1)
balls_list = WebDriverWait(browser, 10).until(
    # EC.visibility_of_all_elements_located((By.XPATH, '//div[@balls]')))
    EC.visibility_of_all_elements_located((By.CLASS_NAME, 'balls')))
time.sleep(5)
hossz = len(balls_list)
print(hossz)
if hossz == 6:
    print("Teszt átment")
assert hossz == 6

for i, value in enumerate(balls_list):
    print(i+1, value.text)
    if value.text < '1' or value.text > '59':
        print('Az ' + i+1 + '. szám out of range!')

browser.close()