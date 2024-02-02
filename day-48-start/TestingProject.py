from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
""" Add the Path for Webdriver """
chrome_driver_path = "C:/Users/teodo/Desktop/pythonProject/day-48-start/chromedriver.exe"
chrome_options = Options()

""" Keep the browser open after execution """
chrome_options.add_experimental_option("detach", True)

""" Handle Chrome alert with allow """
chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 1})
driver = webdriver.Chrome(options=chrome_options)

""" Open website """
driver.get("https://www.ebay.de/")

# """ Enter User and password and click login """
# driver.find_element(By.NAME, value="email").send_keys("")
# driver.find_element(By.NAME, value="pass").send_keys("#")
# driver.find_element(By.NAME, value="login").click()

""" maximize window """
driver.maximize_window()

""" Wait 5 seconds """
time.sleep(5)
# """ If pop up Cookies appears """
# """ Click on 'Weiter ohne zu akzeptieren' if it appears"""
# if driver.find_element(By.ID, value="gdpr-banner-decline").text == "Alle ablehnen":
#     driver.find_element(By.ID, value="gdpr-banner-decline").click()
# # """Click on accept if no other options are there"""
# elif driver.find_element(By.ID, value="gdpr-banner-accept").text == "Alle akzeptieren":
#     driver.find_element(By.ID, value="gdpr-banner-accept").click()
# print(groupName.text)

# """ If the group doesn't appear then scroll down and look again """
# groupName = driver.find_element(By.XPATH, value="")
# # group_name_text = True
# while driver.find_element(By.XPATH, value=""):
#     """ Search for a group with a specific name """
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     groupName = driver.find_element(By.XPATH, value="")
#     time.sleep(3)
#     if "TLS contact appointments" in groupName:
#
#         break
#     else:
#         continue

""" Login """
driver.find_element(By.XPATH, value='//*[@id="gh-ug"]/a').click()
driver.find_element(By.ID, value='userid').send_keys("teodorv55@gmail.com")
driver.find_element(By.ID, value='signin-continue-btn').click()
time.sleep(2)
driver.find_element(By.ID, value='pass').send_keys("123456Tt$")
driver.find_element(By.ID, value='sgnBt').click()

"""Search for Iphone 15 and click enter"""
search_bar = driver.find_element(By.ID, value="gh-ac")
search_bar.send_keys("iphone 15")
search_bar.send_keys(Keys.ENTER)

""" Fetch articles which contains Iphone 15 in an array"""
articles = driver.find_elements(By.XPATH, value="//span[contains(text(),'iphone 15')]")
print(articles[0])
""" Fetch seller type in an array"""
sellers = driver.find_elements(By.XPATH, value="//span[contains(text(),'Gewerblich')]")
print(sellers[0].text)

""" Add the article to the shopping cart """
articles[0].click()
# #get current window handle
# p = driver.current_window_handle
#
# #get first child window
# chwd = driver.window_handles
#
# for w in chwd:
# #switch focus to child window
#     if(w!=p):
#     driver.switch_to.window(w)