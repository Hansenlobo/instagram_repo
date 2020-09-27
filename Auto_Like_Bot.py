from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


PATH = "C:\Program Files (x86)\chromedriver.exe"
print("Instagram Auto Liker")
username = input("Enter Your Username: ")
password = input("Enter Your Password: ")
tag = input("Enter a Tag:")
num = input("No of posts you want to like: ")


driver = webdriver.Chrome(PATH)
driver.get("https://www.instagram.com/accounts/login")
time.sleep(3)


email = driver.find_element_by_name('username').send_keys(username)
password = driver.find_element_by_name(
    'password').send_keys(password + Keys.RETURN)
time.sleep(3)

driver.get("https://www.instagram.com/explore/tags/"+tag)
time.sleep(3)

driver.find_element_by_class_name('_9AhH0').click()
time.sleep(3)
n = 0
while n <= int(num):
    driver.find_element_by_class_name('fr66n').click()
    driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
    time.sleep(1)
    n += 1
# wpO6b
driver.close()
