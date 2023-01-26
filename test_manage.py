# import time
# time.sleep(120)

from selenium import webdriver
from selenium.webdriver.common.by import By
import random
from selenium.webdriver.common.keys import Keys

op = webdriver.ChromeOptions()
op.add_argument('headless')

browser = webdriver.Chrome(options=op)
browser.maximize_window()
browser.get("http://127.0.0.1:8000/agricare/home/")

def test_sell():
    browser.get("http://127.0.0.1:8000/agricare/home/")
    browser.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/a/input").click()
    print("Selling Functionality Testing Successful\n")

def test_list_now():
    browser.get("http://127.0.0.1:8000/agricare/home/")
    browser.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/a/input").click()
    browser.find_element(By.ID, "name").send_keys("test " + str(random.randint(1,100)))
    browser.find_element(By.ID, "phone").send_keys(random.randint(1111111111, 9999999999))
    browser.find_element(By.ID, "city").send_keys("testcity")
    browser.find_element(By.ID, "state").send_keys("teststate")
    browser.find_element(By.ID, "crop").send_keys("testcrop")
    browser.find_element(By.ID, "quantity").send_keys(random.randint(100,200))
    browser.find_element(By.NAME, "price").send_keys(random.randint(1000,3000))
    browser.find_element(By.CLASS_NAME, "button").click()

    print("List Now Functionality Testing Successful\n")


def test_crop_prediction():
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

    print("Crop Prediction Testing Successful\n")

def test_fertilizer_prediction():
    browser.get("http://127.0.0.1:8000/agricare/home/")
    browser.find_element(By.XPATH, "/html/body/div/div[1]/div[4]/a/input").click()
    browser.find_element(By.NAME, "ca").send_keys("20")
    browser.find_element(By.NAME, "mg").send_keys("30")
    browser.find_element(By.NAME, "k").send_keys("10")
    browser.find_element(By.NAME, "s").send_keys("25")
    browser.find_element(By.NAME, "n").send_keys("100")
    browser.find_element(By.NAME, "lime").send_keys("6")
    browser.find_element(By.NAME, "c").send_keys("200")
    browser.find_element(By.NAME, "p").send_keys("200")
    browser.find_element(By.NAME, "moisture").send_keys("200")
    element = browser.find_element(By.CLASS_NAME, "button")
    browser.execute_script("arguments[0].click();", element)

    print("Fertilizer Prediction Testing Successful\n")

def test_live_mandi():
    browser.get("http://127.0.0.1:8000/agricare/home/")
    browser.find_element(By.XPATH, "/html/body/header/a/input").click()
    print("Live Mandi Prices Functionality Testing Successful\n")

    
def test_come_back_to_home_page():
    browser.find_element(By.TAG_NAME, "img").click()
    print("Coming back to Home Page Testing Successful\n")

test_sell()
test_come_back_to_home_page()
test_list_now()
test_crop_prediction()
test_fertilizer_prediction()
test_live_mandi()

