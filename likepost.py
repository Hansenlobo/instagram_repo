from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
PATH = "C:\Program Files (x86)\chromedriver.exe"
print("Instagram Post Liker Based on Username ")
username = input("Enter Your Username: ")
password = input("Enter Your Password: ")

usern = input("Enter the persons username whose post you want to like:")
tot=input("Enter the total No of Posts that user has uploaded")

driver = webdriver.Chrome(PATH)
driver.get("https://www.instagram.com/accounts/login")
time.sleep(3)


email = driver.find_element_by_name('username').send_keys(username)
password = driver.find_element_by_name(
    'password').send_keys(password + Keys.RETURN)
time.sleep(3)
# otp=input("enter otp")

# driver.find_element_by_name('verificationCode').send_keys(otp + Keys.RETURN)

# time.sleep(10)



driver.get("https://www.instagram.com/"+usern)
driver.find_element_by_class_name('_9AhH0').click()
time.sleep(3)
n = 0
while n <=int(tot):
    driver.find_element_by_class_name('fr66n').click()
    driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
    time.sleep(1)
    n += 1
driver.quit()