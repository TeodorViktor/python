from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.com/Instant-pot-plus-60-programmable/dp/B01NBKTPTS/?th=1")
# price_whole = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
# price_fraction = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text
# print(f"{price_whole},{price_fraction}")

# driver.get("https://www.facebook.com/")
# driver.find_element(By.ID, value="email").send_keys("zfbdsfgfbdsgfbdgf")
# driver.find_element(By.ID, value="pass").send_keys("zfbdsfgfbdsgfbdgf")
# driver.find_element(By.CLASS_NAME, value="selected").click()


driver.get("https://www.python.org")

events = {}
def fetch_events(dict):
    elements = [driver.find_elements(By.CSS_SELECTOR, value='.event-widget li time'),
                driver.find_elements(By.CSS_SELECTOR, value='.event-widget li a')]

    names = 1
    times = 0
    for i in range(len(elements[0])):
        dict[i] = {
            'time': elements[times][i].text,
            'name': elements[names][i].text
        }
    print(dict)

fetch_events(events)



driver.quit()