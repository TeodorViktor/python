from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

import time

chrome_driver_path = "C:/Users/teodo/Desktop/pythonProject/day-48-start/chromedriver.exe"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 1})
driver = webdriver.Chrome(options=chrome_options)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
#
# statistic = driver.find_element(By.CSS_SELECTOR, value="#articlecount > :first-child")
# all_portal = driver.find_element(By.)
# print(statistic.text)

# driver.get("http://secure-retreat-92358.herokuapp.com/")
# driver.find_element(By.NAME, value="fName").send_keys("Thomas")
# driver.find_element(By.NAME, value="lName").send_keys("Jens")
# driver.find_element(By.NAME, value="email").send_keys("Jens@gmail.com")
# driver.find_element(By.CLASS_NAME, value="btn-lg").click()

# driver.get("https://orteil.dashnet.org/cookieclicker/")
# time.sleep(5)
# driver.find_element(By.ID, value="langSelect-EN").click()
# time.sleep(5)
# for _ in range(501):
#     driver.find_element(By.ID, value="bigCookie").click()


driver.get("https://www.facebook.com")
driver.maximize_window()
driver.find_element(By.NAME, value="email").send_keys("01285985621")
driver.find_element(By.NAME, value="pass").send_keys("#")
driver.find_element(By.NAME, value="login").click()
time.sleep(5)

desired_cap = chrome_options.to_capabilities()
driver.find_element(By.CSS_SELECTOR, value='div[aria-label="Menu"]').click()
driver.find_element(By.CSS_SELECTOR, value='a[href="https://www.facebook.com/groups/?ref=bookmarks"]').click()
last_active = driver.find_elements(By.CSS_SELECTOR, value='div.xb57i2i span.xo1l8bm')
print(last_active[3].text)


driver.quit()