from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import platform
# from plannuh.SignUp import SignUp
# from plannuh.VerifyLink import VerifyLink
# from plannuh.Login import Login

class launch() :
    def driverLaunch(self):

        baseUrl = "http://plannuh-stage-front.us-east-1.elasticbeanstalk.com/login"
        driverLocation = "C:\\chromedriver.exe"
        driverLocation_linux = "/usr/lib/chromium-browser/chromedriver"

        print(os.getcwd(),"---------------------")
        #os.chdir()
        # driverLocation = "..\\Chrome_Driver\\chromedriver.exe"

        current_paltform = platform.system()
        driver = {}
        if current_paltform != 'Linux':
            os.environ["webdriver.chrome.driver"] = driverLocation
            driver = webdriver.Chrome(driverLocation)
        else :
            print("--in condition--")
            try:
                os.environ["webdriver.chrome.driver"] = driverLocation_linux
                driver = webdriver.Chrome(driverLocation_linux)
                #driver.maximize_window()
                #driver.implicitly_wait(30)
            except Exception as e:
                print(e)

        driver.get(baseUrl)
       # Returning Driver as we again want to use it in another class
        return driver

        time.sleep(1)

# signup= SignUp()
# signup.testSignup(driver)
# time.sleep(1)

# verify= VerifyLink()
# verify.testverificationLink(driver)

# login = Login()
# login.testLogin(driver)