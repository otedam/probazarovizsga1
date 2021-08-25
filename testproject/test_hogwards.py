from datetime import datetime
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def find_element(driver, search_type, value):
    element = WebDriverWait(
        driver, 10).until(
        EC.visibility_of_element_located((search_type, value))
    )
    return element


def timeConversion(s):
    # suffix = s[-2:]
    h_str = s[0:2]
    if int(h_str) > 12:
        hh = int(h_str) - 12
    return s.replace(h_str, str(hh).zfill(2), 1)

def test_hogwarts():
    now = datetime.now()
    print(now)
    year = now.strftime("%Y")
    print("year:", year)

    month = now.strftime("%m")
    print("month:", month)

    day = now.strftime("%d")
    print("day:", day)
    date_m = now.strftime("%Y%m%d")
    date = year + '-' + month + '-' + day
    print(date)

    browser_options = Options()
    browser_options.headless = True
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
    # browser.get(URL_main)

    # browser = webdriver.Chrome("C://chromedriver.exe")

    browser.get('https://witty-hill-0acfceb03.azurestaticapps.net/hogwards.html')
    browser.maximize_window()

    time.sleep(2)

    # elem lekérdezések
    passenger = find_element(browser, By.ID, 'passenger')
    departure_date = find_element(browser, By.ID, 'departure-date')
    departure_time = find_element(browser, By.ID, 'departure-time')
    btn_issue_ticket = find_element(browser, By.ID, 'issue-ticket')

    passenger.send_keys("Harry")
    departure_date.send_keys(year)
    departure_date.send_keys(Keys.TAB)
    departure_date.send_keys(month)
    departure_date.send_keys(day)
    time_m = now.strftime("%H:%M")
    print("time_m: ", time_m)
    departure_time.send_keys(time_m)
    btn_issue_ticket.click()

    passenger_name = find_element(browser, By.ID, 'passenger-name').text
    departure_date_text = find_element(browser, By.ID, 'departure-date-text').text
    departure_time_text = find_element(browser, By.ID, 'departure-time-text').text
    departure_time_text = departure_time_text[:-2]
    print(passenger_name)
    print(departure_date_text)
    conv_time = timeConversion(time_m)
    print("conv_time_m: ", conv_time)
    print(departure_time_text)

    assert passenger_name == "HARRY"
    assert departure_date_text == date
    assert departure_time_text == conv_time
    browser.close()
