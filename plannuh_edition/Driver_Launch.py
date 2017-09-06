from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


class launch() :
    def driverLaunch(self):

        baseUrl = "http://plannuh-stage-front.us-east-1.elasticbeanstalk.com/login"
        # driverLocation = "C:\\Python_learn\\chromedriver.exe"
        driverLocation = "C:\\Users\\Toshiba\\PycharmProjects\\libs\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.get(baseUrl)
       # Returning Driver as we again want to use it in another class
        return driver
