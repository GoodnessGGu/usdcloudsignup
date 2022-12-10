from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
import time
import random
import emails
import tests
import pyautogui as pg
import sqlite3

# web = webdriver.Chrome("/home/gushex/Documents/chromedriver")
# web.get('https://uscloudminer.com/')
# web.maximize_window()
# web.implicitly_wait(5)
# start = web.find_element(By.CLASS_NAME,'sign-up-btn btn open-modal')
# start.click()


driver = webdriver.Chrome("/home/gushex/Documents/usd signup auto/chromedriver")
# driver.get("https://www.python.org/")
# driver.maximize_window()

# element = driver.find_element(By.NAME, value='q')

# element.clear()
# element.send_keys("pycon")
# # element.send_keys(Keys.RETURN)
# submit = driver.find_element(By., 'search-button')
# submit.click()


# _________=_________________-----________________________________

gen_suffix = ["ex", "xr", "ax", "ox", "ie", "io", "ui", "ux", "op", "go", "on", "Og"]

# ++++++++++++++++++++++++++++++emails++++++++++++++++++++++++++++
email = random.choice(emails.mail)
premail = random.choice(gen_suffix)
email_ex = premail + email
# with open("usernames.txt") as names:
#     names.read()
#     for 

# +++++++++++++++++++++++phone number+++++++++++++++++++++++++++++++
suffix = ["090", "091", "070", "080", "081"]
pick = random.choice(suffix)

for i in range(8):
    phone = random.randint(0, 9)

phone_number = pick + str(phone)*2

phone_number = tests.phone_number

# +++++++++++++++++++++++++NAMES+++++++++++++++++++++++++++
names = random.choice(tests.name)
name_suffix = random.choice(gen_suffix)
name_ex = names + name_suffix
# ____________________________-----________________________________

#-------------------the database for storing my used passwords and usernames------------------------------- 

# con = sqlite3.connect("data.db")
# cur = con.cursor()

# cur.execute("CREATE TABLE logins(usernames, emails, phonenumbers)")

# ---------------------------++++++++++++++----------------------------------------------------------------
def usdminer():
    url1 = 'https://uscloudminer.com/7291836363284843'
    url2 = 'https://uscloudminer.com/#'

    driver.get(url1)
    driver.maximize_window()
    # username = driver.find_element(By.NAME, "username")
    # username.send_keys("Greatgush")

    # clicking on the signup button
    # time.sleep(2)
    # pg.moveTo(504, 718, 2)
    # pg.click()
    # time.sleep(2)

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "about"))
        )
    except:
        driver.quit()
    # signup = driver.find_element(By.CLASS_NAME, 'sign-up-btn btn open-modal')
    # signup.click()

    pg.moveTo(504, 718, 1)
    pg.click()
    pg.sleep(1)

    # Actions by html elements
    def clicks():
        alert = driver.switch_to.alert
        alert.find_element(By.NAME, "username")
        alert.send_keys(names)

    # ACtions by mouse positions
    def clicks1():
        # click on the username
        pg.moveTo(621, 209)
        pg.click()
        pg.write(name_ex)
        time.sleep(0)

        # clicking on the phonenumber
        pg.moveTo(632,314)
        pg.click()
        pg.write(phone_number)
        time.sleep(0)

        # clicking on the email
        pg.moveTo(578, 410)
        pg.click()
        pg.write(email_ex)
        time.sleep(0)

        # clicking on the password
        pg.moveTo(590, 512)
        pg.click()
        pg.write("gushxtreme")
        time.sleep(0)

        # clicking on the confirm_password
        pg.moveTo(590, 612)
        pg.click()
        pg.write("gushxtreme")
        time.sleep(0)

        # clicking the agree checkbox
        pg.moveTo(465, 706)
        pg.click()
        time.sleep(0)

        # submit button
        pg.moveTo(631, 747)
        pg.click()
        time.sleep(0)

        time.sleep(2)
        driver.quit()

    clicks1()

for x in range(5):
    usdminer()



