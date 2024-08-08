from selenium.webdriver import Keys

password = "Facebook_password"
email = "facebook_email"
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://tinder.com/")


time.sleep(3)
driver.find_element(By.XPATH, value='//*[@id="u-1419960890"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a').click()
time.sleep(3)
driver.find_element(By.XPATH, value='//*[@id="u1146625330"]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div[2]/div/div').click()
time.sleep(3)
base_window = driver.window_handles[0]
try:
    fb_window = driver.window_handles[1]
    driver.switch_to.window(fb_window)

    driver.find_element(By.ID, value="email").send_keys(email)
    driver.find_element(By.ID, value="pass").send_keys(password)
    driver.find_element(By.NAME, value="login").click()
except NoSuchElementException:
    pass


driver.switch_to.window(base_window)


time.sleep(7)
driver.find_element(By.XPATH, value='//*[@id="u1146625330"]/div/div[2]/div/div/div[1]/div[1]/button').click()
time.sleep(3)
driver.find_element(By.XPATH, value='//*[@id="u1146625330"]/div/div/div/div/div[3]/button[1]').click()
time.sleep(3)
driver.find_element(By.XPATH, value='//*[@id="u1146625330"]/div/div/div/div/div[3]/button[2]').click()
time.sleep(4)

for i in range(20):
    try:
         hearth = driver.find_element(By.XPATH, value='//*[@id="u-1419960890"]/div/div[1]/div/div/main/div/div/div[1]/div/div[3]/div/div[4]/button')
         hearth.click()
    except NoSuchElementException:
        time.sleep(3)
        pass

