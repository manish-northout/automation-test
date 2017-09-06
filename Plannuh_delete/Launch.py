from selenium import webdriver
import  os
import time



class Launch():
    # def __init__(self):
    #     self.driverlaunch()

    def driverlaunch(self):
        baseUrl = "http://plannuh-stage-front.us-east-1.elasticbeanstalk.com/login"
        driverLocation = "D:\\Automation\\Pycharm_workspace\\Plannuh1\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.get(baseUrl)
        time.sleep(1)
        # self.driver = driverObj
        return driver



