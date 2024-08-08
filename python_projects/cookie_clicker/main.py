from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")


cookie = driver.find_element(By.XPATH, value='//*[@id="cookie"]')

timeout = time.time() + 5
checker = time.time() + 60*5


while True:
    cookie.click()
    if time.time() > timeout:
        timeout = time.time() + 5
        for n in range(8):
            money = int((driver.find_element(By.XPATH, value='//*[@id="money"]').text).replace(",", ""))
            try:
             prices = [driver.find_element(By.XPATH, value=f'/html/body/div[3]/div[5]/div/div[{i + 1}]/b').text for i in
                        range(8)]
            except:
                break
            price_list = [int((price.split("-")[1]).replace(",", "")) for price in prices]
            if money < min(price_list):
                break
            elif money > price_list[len(price_list)-n-1]:
                while money > price_list[len(price_list)-n-1]:
                    money = int((driver.find_element(By.XPATH, value='//*[@id="money"]').text).replace(",", ""))
                    buttons = [driver.find_element(By.XPATH, value=f'/html/body/div[3]/div[5]/div/div[{n + 1}]') for n in
                               range(8)]
                    try:
                        buttons[len(price_list)-n-1].click()
                    except:
                        break

    if time.time() > checker:
        print((driver.find_element(By.XPATH, value='/html/body/div[3]/div[4]/div[1]')).text)
        checker = time.time() + 60*5


