import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.youtube.com/watch?v=T4KLIF0BTdI&ab_channel=CUOMUSIC%ED%81%90%EC%98%A4%EB%AE%A4%EC%A7%81"

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")

i = 1
while True:
    # browser = webdriver.Chrome()
    browser = webdriver.Chrome(options=options)
    browser.get(url)

    interval = 3

    time.sleep(interval)

    agree = browser.find_element_by_xpath("//*[@id='content']/div[2]/div[5]/div[2]/ytd-button-renderer[2]/a")
    agree.click()

    mute = browser.find_element_by_xpath("//*[@id='movie_player']/div[28]/div[2]/div[1]/span/button")
    mute.click()

    time.sleep(180)

    browser.quit()
    print("{}회 재생".format(i))
    i += 1