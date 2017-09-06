from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import os

from selenium.webdriver.support.select import Select
from plannuh_edition.Driver_Launch import launch
from plannuh_edition.Login import Login
from plannuh_edition.edit_campaign import EditCampaign
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class EditCampaignAddProgram():

    def __init__(self):
        campaign = EditCampaign()
        self.driver = campaign.driver
        campaign.main()


    def testCampaign(self, driver):

        time.sleep(10)

        select_goal = driver.find_element_by_link_text("Goal1").click()
        time.sleep(3)

        view_campaign = driver.find_element_by_link_text("Campaign4").click()
        time.sleep(3)

        add_program = driver.find_element_by_xpath("//*[@id='tab-viewCampaign-1']/button")
        add_program.click()
        time.sleep(3)

        program_name = driver.find_element_by_name("name").send_keys("Program6")
        time.sleep(2)

        current_status = driver.find_element_by_name("mode")
        select = Select(current_status)
        time.sleep(2)

        select.select_by_visible_text("Planned")
        print("Select planned as current status")
        time.sleep(1)

        # select.select_by_visible_text("Open")
        # print("Select Open as current status")
        # time.sleep(1)
        #
        # select.select_by_visible_text("Completed")
        # print("Select Completed as current status")
        # time.sleep(1)

        budget = driver.find_element_by_name("amount").send_keys("2000")
        time.sleep(1)

        continueBtn1 = driver.find_element_by_css_selector("#addProgramColl1 > div > div > div.col-xs-12.col-sm-12.col-md-12 > div > div > div > a").click()
        time.sleep(5)

        # Choose Timeframe
        # q1 = driver.find_element_by_xpath("//*[@id='addProgramColl2']/div/div/div[1]/div[1]/div[1]/label/input")
        # q1.click()
        # time.sleep(1)

        q2 = driver.find_element_by_xpath("//*[@id='addProgramColl2']/div/div/div[1]/div[1]/div[2]/label/input")
        q2.click()
        time.sleep(2)

        q3 = driver.find_element_by_xpath("//*[@id='addProgramColl2']/div/div/div[1]/div[1]/div[3]/label/input")
        q3.click()
        time.sleep(2)

        q4 = driver.find_element_by_xpath("//*[@id='addProgramColl2']/div/div/div[1]/div[1]/div[4]/label/input")
        q4.click()
        time.sleep(3)

        # Choose Goal

        goal = driver.find_element_by_css_selector("#tab-addProgram-1 > div > div:nth-child(1) > label > input").click()
        print("Select goal for selected timeframe")
        time.sleep(3)

        campaign_link = driver.find_element_by_xpath("//*[@id='addProgramColl2']/div/div/div[1]/div[2]/nav/ul/li[2]/a").click()
        time.sleep(3)

        campaign = driver.find_element_by_xpath("//*[@id='tab-addProgram-2']/div[1]/div/label/input").click()
        time.sleep(3)

        continueBtn2 = driver.find_element_by_xpath("//*[@id='addProgramColl2']/div/div/div[2]/div/div/a").click()
        time.sleep(5)

        choose_metric1 = driver.find_element_by_xpath("//*[@id='addProgramColl3']/div/div/div/div/div[1]/select")
        select1 = Select(choose_metric1)

        # select1.select_by_value("Other")
        # print("Select Other by value")
        # time.sleep(1)

        select1.select_by_value("New customers")
        print("Select New customers by value")
        time.sleep(1)

        # select1.select_by_value("Registrations")
        # print("Select Registrations by value")
        # time.sleep(1)
        #
        # select1.select_by_value("Website visits")
        # print("Select Website visits by value")
        # time.sleep(1)
        #
        # select1.select_by_value("Bookings")
        # print("Select Bookings by value")
        # time.sleep(1)
        #
        # select1.select_by_value("Pipeline")
        # print("Select Pipeline by value")
        # time.sleep(1)
        #
        # select1.select_by_value("Revenue")
        # print("Select Revenue by value")
        # time.sleep(1)
        #
        # select1.select_by_value("Opportunities")
        # print("Select Opportunities by value")
        # time.sleep(1)
        #
        # select1.select_by_value("Leads")
        # print("Select Leads by value")
        # time.sleep(1)

        projecting_1 = driver.find_element_by_xpath("//*[@id='addProgramColl3']/div/div/div/div/div[2]/input")
        projecting_1.send_keys("1000")
        time.sleep(1)

        finishBtn = driver.find_element_by_xpath("//*[@id='form-addGoalDetail']/div[3]/button[1]")
        finishBtn.click()
        time.sleep(5)

    def main(self):
        self.testCampaign(self.driver)

# We have to call this main method and here we are accessing it's own class methods
if __name__ == '__main__':
    editCampaignAddProgram = EditCampaignAddProgram()
    editCampaignAddProgram.main()







