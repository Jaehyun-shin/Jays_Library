import math
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from openpyxl import Workbook

wb = Workbook()
ws = wb.active

ws.append(["Fach", "Note", "CP", "Versuche"])

# options = webdriver.ChromeOptions()
# options.headless = True
# options.add_argument("window-size=1920x1080")



url = "https://qis.server.uni-frankfurt.de/qisserver/rds?state=user&type=8&topitem=functions&breadCrumbSource=portal"

# browser = webdriver.Chrome(options=options)
browser = webdriver.Chrome()
browser.get(url)
browser.maximize_window()

browser.find_element_by_xpath("//*[@id='wrapper']/div[3]/a").click()

input = browser.find_element_by_id("asdf").send_keys("s6010479")
password = browser.find_element_by_id("fdsa").send_keys("Wogusrne1!")

OK_button = browser.find_element_by_xpath("//*[@id='loginForm:login']")
OK_button.click()

Pruefungsverwaltung = browser.find_element_by_xpath("//*[@id='makronavigation']/ul/li[3]/a")
Pruefungsverwaltung.click()

Notenspiegel = browser.find_element_by_xpath("//*[@id='wrapper']/div[6]/div[2]/div/form/div/ul/li[3]/a")
Notenspiegel.click()

PO_2019 = browser.find_element_by_xpath("//*[@id='wrapper']/div[6]/div[2]/form/ul/li/a[1]")
PO_2019.click()

Ausrufzeichen = browser.find_element_by_xpath("//*[@id='wrapper']/div[6]/div[2]/form/ul/li/ul/li[2]/a[1]")
Ausrufzeichen.click()                                               # PO_2019 사이트까지 들어가기

list = ["Fach", "Note", "Status", "CP", "Versuche"]

# Fach 1, Note 3, Status 6, CP 7, Versuch 9 필요함

# 스크롤 내리기
# interval = 5

# prev_height = browser.execute_script("return document.body.scrollHeight")

scores = []
while True:
    # browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    for i in range(10, len(browser.find_elements_by_class_name("qis_records"))):
        a = i % 9
        if a == 1:
            scores.append(browser.find_elements_by_class_name("qis_records")[i].text)
        elif a == 3:
            scores.append(browser.find_elements_by_class_name("qis_records")[i].text)
        elif a == 6:
            scores.append(browser.find_elements_by_class_name("qis_records")[i].text)
        elif a == 7:
            scores.append(browser.find_elements_by_class_name("qis_records")[i].text)
        elif a == 0:
            scores.append(browser.find_elements_by_class_name("qis_records")[i].text)
    
    # time.sleep(interval)

    # curr_height = browser.execute_script("return document.body.scrollHeight")

    # if curr_height == prev_height:
    #     break

    # prev_height = curr_height

for i in range(0, math.ceil(len(browser.find_elements_by_class_name("qis_records"))/4)):
    a = i % 5
    if a == 0:
        # print(score_list[i:i+4])
        Note = str(scores[i+1])
        if Note != "":
            Note = float(Note.replace(",","."))
            if Note >= 5:
                continue
            else: print("Fach : {} | Note = {} | CP = {} | Versuche = {}".format(scores[i],scores[i+1],scores[i+2],scores[i+3],scores[i+4]))
            

# browser.quit()

wb.save("Notenspiegel.xlsx")