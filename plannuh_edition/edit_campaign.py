from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import os

from selenium.webdriver.support.select import Select
from plannuh_edition.Driver_Launch import launch
from plannuh_edition.Login import Login
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class EditCampaign():

    def __init__(self):
        login1 = Login()
        self.driver = login1.driver
        login1.main()

    def testEditCampaign(self, driver):

        time.sleep(15)

        select_goal = driver.find_element_by_link_text("Goal1").click()
        time.sleep(3)
        print("Select Goal")

        view_campaign = driver.find_element_by_link_text("Campaign1").click()
        time.sleep(5)
        print("Select Campaign")

        edit_campaign = driver.find_element_by_css_selector("button.btn.btn-skyBlue")
        edit_campaign.click()
        time.sleep(3)

        click_continue = driver.find_element_by_xpath("//*[@id='editCampaignColl1']/div/div/div[3]/div/div/div/a").click()
        time.sleep(5)

        # q1 = driver.find_element_by_xpath("//*[@id='form-addGoalTimeFrame']/div/div[1]/div[1]/label/input")
        # q1.click()
        # time.sleep(1)
        #
        # q2 = driver.find_element_by_xpath("//*[@id='form-addGoalTimeFrame']/div/div[1]/div[2]/label/input")
        # q2.click()
        # time.sleep(1)

        # q3 = driver.find_element_by_xpath("//*[@id='form-addGoalTimeFrame']/div/div[1]/div[3]/label/input")
        # q3.click()
        # time.sleep(1)
        #
        # q4 = driver.find_element_by_xpath("//*[@id='form-addGoalTimeFrame']/div/div[1]/div[4]/label/input")
        # q4.click()
        # time.sleep(3)

        # Choose Goal

        clear_selected_goal = driver.find_element_by_css_selector("button.btn-clear.btn-cleared").click()
        time.sleep(3)

        goal = driver.find_element_by_xpath("(//input[@name='selectedGoal'])[2]").click()
        print("Select goal for selected timeframe")
        time.sleep(5)

        finishBtn = driver.find_element_by_xpath("//*[@id='form-editCampaign']/div/div/div/div[3]/button[1]")
        finishBtn.click()
        time.sleep(5)

        # Reset all

        select_goal = driver.find_element_by_link_text("Goal3").click()
        time.sleep(3)
        print("Select Goal")

        view_campaign = driver.find_element_by_link_text("Campaign1").click()
        time.sleep(5)
        print("Select Campaign")

        edit_campaign = driver.find_element_by_css_selector("button.btn.btn-skyBlue")
        edit_campaign.click()
        time.sleep(3)

        click_continue = driver.find_element_by_xpath(
            "//*[@id='editCampaignColl1']/div/div/div[3]/div/div/div/a").click()
        time.sleep(5)

        # q1 = driver.find_element_by_xpath("//*[@id='form-addGoalTimeFrame']/div/div[1]/div[1]/label/input")
        # q1.click()
        # time.sleep(1)
        #
        # q2 = driver.find_element_by_xpath("//*[@id='form-addGoalTimeFrame']/div/div[1]/div[2]/label/input")
        # q2.click()
        # time.sleep(1)

        # q3 = driver.find_element_by_xpath("//*[@id='form-addGoalTimeFrame']/div/div[1]/div[3]/label/input")
        # q3.click()
        # time.sleep(1)
        #
        # q4 = driver.find_element_by_xpath("//*[@id='form-addGoalTimeFrame']/div/div[1]/div[4]/label/input")
        # q4.click()
        # time.sleep(3)

        # Choose Goal

        clear_selected_goal = driver.find_element_by_css_selector("button.btn-clear.btn-cleared").click()
        time.sleep(3)

        goal = driver.find_element_by_xpath("//*[@id='tab-addCampaign-1']/div/div[1]/label/input").click()
        print("Select goal for selected timeframe")
        time.sleep(5)

        finishBtn = driver.find_element_by_xpath("//*[@id='form-editCampaign']/div/div/div/div[3]/button[1]")
        finishBtn.click()
        time.sleep(5)

    def main(self):
        self.testEditCampaign(self.driver)

# We have to call this main method and here we are accessing it's own class methods
if __name__ == '__main__':
    campaign = EditCampaign()
    campaign.main()




