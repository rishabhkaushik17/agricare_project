from selenium import webdriver
from selenium.webdriver.common.by import By

op = webdriver.ChromeOptions()
op.add_argument('headless')

browser = webdriver.Chrome(options=op)
browser.maximize_window()
browser.get("http://127.0.0.1:8000/agricare/home/")

browser.find_element(By.XPATH, "/html/body/div/div[1]/div[3]/a/input").click()

browser.find_element(By.NAME, "n").send_keys("20")
browser.find_element(By.NAME, "p").send_keys("30")
browser.find_element(By.NAME, "k").send_keys("10")
browser.find_element(By.NAME, "temp").send_keys("25")
browser.find_element(By.NAME, "hum").send_keys("100")
browser.find_element(By.NAME, "ph").send_keys("6")
browser.find_element(By.NAME, "rain").send_keys("200")

browser.find_element(By.CLASS_NAME, "button").click()
