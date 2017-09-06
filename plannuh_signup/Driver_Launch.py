from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from plannuh_signup.SignUp import SignUp
from plannuh_signup.VerifyLink import VerifyLink
from plannuh_signup.Login import Login

baseUrl = "http://plannuh-stage-front.us-east-1.elasticbeanstalk.com/login"
driverLocation = "C:\\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = driverLocation
driver = webdriver.Chrome(driverLocation)
driver.get(baseUrl)


time.sleep(1)

signup= SignUp()
signup.testSignup(driver)
time.sleep(1)

verify= VerifyLink()
verify.testverificationLink(driver)

login = Login()
login.testLogin(driver)
