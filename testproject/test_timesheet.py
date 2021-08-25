import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def find_element(driver, search_type, value):
    element = WebDriverWait(
        driver, 10).until(
        EC.visibility_of_element_located((search_type, value))
    )
    return element

def test_timesheet1():
    browser_options = Options()
    browser_options.headless = True
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
    # browser.get(URL_main)

    # browser = webdriver.Chrome("C://chromedriver.exe")
    browser.get('https://witty-hill-0acfceb03.azurestaticapps.net/timesheet.html')

    browser.maximize_window()

    # elem lekérdezések

    # ## TC01: üres kitöltés helyessége
    # * ha nincs kitoltve az e-mail mező nem lehet megnyomni a "next" feliratú gombot
    # * ha helytelen (formailag helytelen) e-mailcimmel probáljuk kitölteni a formot nem lehet megnyomni a "next" feliratú gombot

    email = find_element(browser, By.CSS_SELECTOR, 'input[placeholder="artist@moviemakr.com"]')
    email_value = email.get_attribute('value')
    print(email_value)
    if len(email_value) == 0:
        try:
            next_btn = find_element(browser, By.XPATH, '//input[@value="Next"]')
            next_btn_property = next_btn.get_property('disabled')
            if next_btn_property == True:
                print("Teszt átment")
            else:
                print("Elbukott")

        except:
            print("Sg wrong")

    email.send_keys("gktest&gmail")
    try:
        next_btn = find_element(browser, By.XPATH, '//input[@value="Next"]')
        next_btn_property = next_btn.get_property('disabled')
        if next_btn_property == True:
            print("Teszt átment")
        else:
            print("Elbukott")
    except:
        print("sg wrong")
    browser.close()

# ## TC02: helyes kitöltés helyes köszönet képernyő
# * töltsük ki a következő adatokkal a formot:
#     * test@bela.hu
#     * 2 hours and 0 minutes
#     * working hard
#     * types of work: Time working on visual effects for movie
# * nyomjuk meg a "next" feliratú gombot
# * ellenőrizzük a megjelenő tartalomban az órák és percek helyességét

def test_timesheet2():
    browser_options = Options()
    browser_options.headless = True
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
    # browser.get(URL_main)

    # browser = webdriver.Chrome("C://chromedriver.exe")
    browser.get('https://witty-hill-0acfceb03.azurestaticapps.net/timesheet.html')

    browser.maximize_window()

    # browser = webdriver.Chrome("C://chromedriver.exe")
    # browser.get('https://witty-hill-0acfceb03.azurestaticapps.net/timesheet.html')
    email = find_element(browser, By.CSS_SELECTOR, 'input[placeholder="artist@moviemakr.com"]')
    email.send_keys("test@bela.hu")
    hours = find_element(browser, By.CSS_SELECTOR, 'input[placeholder="hours"]')
    hours.send_keys('2')
    minutes = find_element(browser, By.CSS_SELECTOR, 'input[placeholder="minutes"]')
    minutes.send_keys('0' + Keys.TAB)
    time.sleep(2)
    # messagem = find_element(browser, By.CSS_SELECTOR, '.ng-pristine.ng-valid.ng-touched')
    # messagem = find_element(browser, By.XPATH, '//textarea[@class="ng-pristine ng-valid ng-touched"]')
    # messagem.send_keys("working hard")
    # add_new_btn.click()
    # find_element(browser, By.ID, 'dropDown')
    dropdown = Select(browser.find_element_by_id('dropDown'))
    dropdown.select_by_value('Time working on visual effects for movie')
    next_btn = find_element(browser, By.XPATH, '//input[@value="Next"]')
    next_btn.click()

    time.sleep(4)
    span_list = WebDriverWait(browser, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, '//span[@class]')))
    # print(len(span_list))
    # span_list = browser.find_elements_by_class_name('green ng-binding')
    # for i, value in enumerate(span_list):
    #     print(i, value.text)
    check_hours = span_list[1].text
    # # # check_mins = span_list[2].get_attribute('value')
    check_mins = span_list[2].text
    # print(check_hours)
    # print(check_mins)
    assert check_hours == '2' and check_mins == '0'
    browser.close()
