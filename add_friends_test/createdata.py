from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument('blink-settings=imagesEnabled=false')
chrome_options.add_argument('--headless')
driver = webdriver.Chrome("/Users/tuishoutest/Downloads/chromedriver", options=chrome_options)

print("---------")
driver.quit()
