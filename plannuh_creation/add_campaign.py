from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import os

from selenium.webdriver.support.select import Select
from plannuh_creation.Driver_Launch import launch
from plannuh_creation.Login import Login
from plannuh_creation.add_goals import AddGoals
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class AddCampaign():

    def __init__(self):
        goals = AddGoals()
        self.driver = goals.driver
        goals.main()

    def testCampaign(self, driver):

        time.sleep(10)

        add = driver.find_element_by_xpath("//button[@class='btn-addgoals']")
        add.click()
        print("CLick Add button")
        time.sleep(5)

        add_campaign = driver.find_element_by_xpath("//button[@class='btn-campaign']")
        add_campaign.click()
        print("Click Add campaign button")
        time.sleep(5)

        campaign_name = driver.find_element_by_xpath("//div[@id='addCampaignColl1']//input[@name='name']")
        campaign_name.send_keys("Campaign2")
        time.sleep(1)

        current_status = driver.find_element_by_xpath("//div[@id='addCampaignColl1']//select[@name='mode']")
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

        budget = driver.find_element_by_xpath("//div[@id='addCampaignColl1']//input[@name='amount']")
        budget.send_keys("12345")
        time.sleep(1)

        continueBtn1 = driver.find_element_by_xpath("//div[@id='addCampaignColl1']//a[contains(text(), 'Continue')]")
        continueBtn1.click()
        time.sleep(1)


        q1 = driver.find_element_by_xpath("//*[@id='form-addGoalTimeFrame']/div/div[1]/div[1]/label/input")
        q1.click()
        time.sleep(1)

        # q2 = driver.find_element_by_xpath("//*[@id='form-addGoalTimeFrame']/div/div[1]/div[2]/label/input")
        # q2.click()
        # time.sleep(1)

        q3 = driver.find_element_by_xpath("//*[@id='form-addGoalTimeFrame']/div/div[1]/div[3]/label/input")
        q3.click()
        time.sleep(1)

        q4 = driver.find_element_by_xpath("//*[@id='form-addGoalTimeFrame']/div/div[1]/div[4]/label/input")
        q4.click()
        time.sleep(3)

        # Choose Goal

        goal = driver.find_element_by_name("selectedGoal").click()
        print("Select goal for selected timeframe")
        time.sleep(3)

        continueBtn2 = driver.find_element_by_xpath("//*[@id='form-addGoalTimeFrame']/div/div[2]/a")
        continueBtn2.click()
        time.sleep(1)

        finishBtn = driver.find_element_by_xpath("//form[@id='form-addGoalDetail']//button[contains(text(), 'Finish')]")
        finishBtn.click()
        time.sleep(5)

    def main(self):
        self.testCampaign(self.driver)

# We have to call this main method and here we are accessing it's own class methods
if __name__ == '__main__':
    campaign = AddCampaign()
    campaign.main()
