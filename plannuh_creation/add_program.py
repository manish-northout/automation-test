from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import os

from selenium.webdriver.support.select import Select
from plannuh_creation.Driver_Launch import launch
from plannuh_creation.Login import Login
from plannuh_creation.add_goals import AddGoals
from plannuh_creation.add_campaign import AddCampaign
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class AddProgram():

    def __init__(self):
        campaign = AddCampaign()
        self.driver = campaign.driver
        campaign.main()

    def testProgram(self, driver):
        time.sleep(10)

        add = driver.find_element_by_xpath("//button[@class='btn-addgoals']")
        add.click()
        print("CLick Add button")
        time.sleep(3)

        add_program = driver.find_element_by_xpath("//button[@class='btn-program']")
        add_program.click()
        print("Click Add Program button")
        time.sleep(5)

        program_name = driver.find_element_by_xpath("//div[@id='addProgramColl1']//input[@name='name']")
        program_name.send_keys("Program2")
        time.sleep(1)

        current_status = driver.find_element_by_xpath("//div[@id='addProgramColl1']//select[@name='mode']")
        select = Select(current_status)
        time.sleep(1)

        select.select_by_value("Planned")
        print("Select planned as current status")
        time.sleep(1)

        # select.select_by_value("Approved")
        # print("Select approved as current status")
        # time.sleep(1)
        #
        # select.select_by_value("Closed")
        # print("Select closed as current status")
        # time.sleep(1)

        budget = driver.find_element_by_xpath("//div[@id='addProgramColl1']//input[@name='amount']")
        budget.send_keys("1234")
        time.sleep(1)

        continueBtn1 = driver.find_element_by_xpath("//*[@id='addProgramColl1']/div/div/div[3]/div/div/div/a")
        continueBtn1.click()
        time.sleep(3)

        # Choose time frame
        q1 = driver.find_element_by_xpath("//*[@id='addProgramColl2']/div/div/div[1]/div[1]/div[1]/label/input")
        q1.click()
        time.sleep(1)

        # q2 = driver.find_element_by_xpath("//*[@id='addProgramColl2']/div/div/div[1]/div[1]/div[2]/label/input")
        # q2.click()
        # time.sleep(3)

        q3 = driver.find_element_by_xpath("//*[@id='addProgramColl2']/div/div/div[1]/div[1]/div[3]/label/input")
        q3.click()
        time.sleep(3)

        q4 = driver.find_element_by_xpath("//*[@id='addProgramColl2']/div/div/div[1]/div[1]/div[4]/label/input")
        q4.click()
        time.sleep(3)

        goal = driver.find_element_by_xpath("//*[@id='tab-addProgram-1']/div/div/label/input").click()
        print("Select Goal for selected timeframe")
        time.sleep(3)


        campaign_link = driver.find_element_by_link_text("Campaign").click()
        time.sleep(3)

        campaign = driver.find_element_by_name("campaign").click()
        print("Select campaign for selected timeframe and goal")
        time.sleep(3)

        continueBtn2 = driver.find_element_by_xpath("//*[@id='addProgramColl2']/div/div/div[2]/div/div/a")
        continueBtn2.click()
        time.sleep(3)

        finishBtn = driver.find_element_by_xpath("//form[@id='form-addGoalDetail']//button[contains(text(), 'Finish')]")
        finishBtn.click()
        time.sleep(5)

    def main(self):
        self.testProgram(self.driver)

# We have to call this main method and here we are accessing it's own class methods
if __name__ == '__main__':
    program = AddProgram()
    program.main()





