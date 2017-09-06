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
from plannuh_creation.add_program import AddProgram
from plannuh_creation.add_expenses import AddExpenses
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class AddGoalsWithMultipleTimeframe():

    def __init__(self):
        expenses = AddExpenses()
        self.driver = expenses.driver
        expenses.main()

    def testGoals(self, driver):
        time.sleep(10)

        add = driver.find_element_by_xpath("//button[@class='btn-addgoals']")
        add.click()
        print("CLick Add button")
        time.sleep(5)

        add_goals = driver.find_element_by_xpath("//button[@class='btn-goal']")
        add_goals.click()
        print("CLick goals")
        time.sleep(10)

        goal_name = driver.find_element_by_xpath("//div[@id='form-addGoalDetail']//input[@name='name']")
        goal_name.send_keys("Goal3")
        time.sleep(1)

        current_status = driver.find_element_by_xpath(
            "//form[@id = 'form-addGoalDetail']//select[starts-with(@class, 'input-animation ng-untouched ng-pristine ng-invalid')]")

        select = Select(current_status)
        time.sleep(1)

        select.select_by_value("Planned")
        print("Select planned as current status")
        time.sleep(1)

        # select.select_by_value("Approved")
        # print("Select approved as current status")
        #
        # select.select_by_value("Closed")
        # print("Select closed as current status")

        add_note = driver.find_element_by_xpath("//form[@id='form-addGoalDetail']//textarea[@name='note']")
        add_note.send_keys("Add notes here")
        time.sleep(1)

        continueBtn1 = driver.find_element_by_xpath("//div[@id='form-addGoalDetail']//a[@href='#collapse2']")
        continueBtn1.click()
        time.sleep(10)
        print("Choose time frame")

        # q1 = driver.find_element_by_xpath("//*[@id='form-addGoalTimeFrame']/div/div[1]/div[1]/label/input")
        # q1.click()
        # time.sleep(1)

        # q2 = driver.find_element_by_xpath("//*[@id='form-addGoalTimeFrame']/div/div[1]/div[2]/label/input")
        # q2.click()
        # time.sleep(1)

        # q3 = driver.find_element_by_xpath("//*[@id='form-addGoalTimeFrame']/div/div[1]/div[3]/label/input")
        # q3.click()
        # time.sleep(1)
        #
        # q4 = driver.find_element_by_xpath("//*[@id='form-addGoalTimeFrame']/div/div[1]/div[4]/label/input")
        # q4.click()
        # time.sleep(1)

        continueBtn2 = driver.find_element_by_xpath("//*[@id='form-addGoalTimeFrame']//a[@href='#collapse3']")
        continueBtn2.click()
        time.sleep(3)

        choose_metric1 = driver.find_element_by_xpath("//div[@id='form-addGoalTrack']//select")
        select1 = Select(choose_metric1)

        # select1.select_by_value("Other")
        # print("Select Other by value")
        # time.sleep(1)

        # select1.select_by_value("New customers")
        # print("Select New customers by value")
        # time.sleep(1)
        #
        # select1.select_by_value("Registrations")
        # print("Select Registrations by value")
        # time.sleep(1)
        #
        # select1.select_by_value("Website visits")
        # print("Select Website visits by value")
        # time.sleep(1)
        #
        select1.select_by_value("Bookings")
        print("Select Bookings by value")
        time.sleep(1)
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
        #

        projecting_1 = driver.find_element_by_xpath("//div[@id='form-addGoalTrack']//input")
        projecting_1.send_keys("2000")
        time.sleep(1)

        finishBtn = driver.find_element_by_xpath("//form[@id='form-addGoalDetail']//button[contains(text(), 'Finish')]")
        finishBtn.click()
        time.sleep(5)

    def main(self):
        self.testGoals(self.driver)

# We have to call this main method and here we are accessing it's own class methods
if __name__ == '__main__':
    goalMultipleTimeframe = AddGoalsWithMultipleTimeframe()
    goalMultipleTimeframe.main()

