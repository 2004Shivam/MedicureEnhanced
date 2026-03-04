from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

driver.get("http://127.0.0.1:8000")

assert "MediCure" in driver.title

time.sleep(3)
driver.quit()

print("Test Passed Successfully")