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
from plannuh_creation.goal_multiple_timeframe import AddGoalsWithMultipleTimeframe
from plannuh_creation.campaign_without_goal import AddCampaignWthoutGoal
from plannuh_creation.program_with_goal import AddProgramWithGoal
from plannuh_creation.program_with_campaign import AddProgramWithCampaign
from plannuh_creation.expenses_with_goal import AddExpensesWithGoal
from plannuh_creation.expenses_with_campaign import AddExpensesWithCampaign
from plannuh_creation.expenses_with_goal_campaign_program import AddExpensesWithGoalCampaignProgram
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class AddExpensesWithoutGoalCampaignProgram():

    def __init__(self):
        expensesWithGoalCampaignProgram = AddExpensesWithGoalCampaignProgram()
        self.driver = expensesWithGoalCampaignProgram.driver
        expensesWithGoalCampaignProgram.main()

    def testExpenses(self, driver):
        time.sleep(10)

        add = driver.find_element_by_class_name("btn-addgoals")
        add.click()
        print("CLick Add button")
        time.sleep(5)

        add_expenses = driver.find_element_by_class_name("btn-expenses")
        add_expenses.click()
        time.sleep(5)

        expenses_name = driver.find_element_by_xpath("//*[@id='addExpensesColl1']/div/div/div[1]/div[1]/input")
        expenses_name.send_keys("expense1")
        time.sleep(1)

        current_status = driver.find_element_by_xpath("//*[@id='addExpensesColl1']/div/div/div[1]/div[2]/div/select")
        select = Select(current_status)
        time.sleep(1)

        # select.select_by_value("Planned")
        # print("Select Planned as current status")
        # time.sleep(1)

        select.select_by_value("Committed")
        print("Select Committed as current status")
        time.sleep(1)

        # select.select_by_value("Vendor Selected")
        # print("Select Vendor Selected as current status")
        # time.sleep(1)

        # select.select_by_value("Delivered")
        # print("Select Delivered as current status")
        # time.sleep(1)

        # select.select_by_value("Billed")
        # print("Select Billed as current status")
        # time.sleep(1)

        status_amount = driver.find_element_by_xpath("//*[@id='addExpensesColl1']/div/div/div[1]/div[3]/input")
        status_amount.send_keys("1000")
        time.sleep(1)

        expenses_type = driver.find_element_by_xpath("//*[@id='addExpensesColl1']/div/div/div[1]/div[4]/div/select")
        select = Select(expenses_type)

        # select.select_by_visible_text("Other")
        # print("Select Other as expenses type")
        # time.sleep(1)
        #
        select.select_by_visible_text("Postage")
        print("Select Postage as expenses type")
        time.sleep(1)
        #
        # select.select_by_visible_text("Advisory Services")
        # print("Select Advisory Services as expenses type")
        # time.sleep(1)
        #
        # select.select_by_visible_text("Tchotchkes")
        # print("Select Tchotchkes as expenses type")
        # time.sleep(1)
        #
        # select.select_by_visible_text("Outside services")
        # print("Select Outside services as expenses type")
        # time.sleep(1)
        #
        # select.select_by_visible_text("Consultants")
        # print("Select Consultants as expenses type")
        # time.sleep(1)
        #
        # select.select_by_visible_text("Technology")
        # print("Select Technology as expenses type")
        # time.sleep(1)
        #
        # select.select_by_visible_text("Data")
        # print("Select Data as expenses type")
        # time.sleep(1)
        #
        # select.select_by_visible_text("Analyst Relations")
        # print("Select Analyst Relations as expenses type")
        # time.sleep(1)
        #
        # select.select_by_visible_text("Design Services")
        # print("Select Design Services as expenses type")
        # time.sleep(1)
        #
        # select.select_by_visible_text("Sponsorships")
        # print("Select Sponsorships as expenses type")
        # time.sleep(1)
        #
        # select.select_by_visible_text("Hospitality")
        # print("Select Hospitality as expenses type")
        # time.sleep(1)
        #
        # select.select_by_visible_text("Customer Programs")
        # print("Select Customer Programs as expenses type")
        # time.sleep(1)
        #
        # select.select_by_visible_text("Radio Advertising")
        # print("Select Radio Advertising as expenses type")
        # time.sleep(1)
        #
        # select.select_by_visible_text("Television")
        # print("Select Television as expenses type")
        # time.sleep(1)
        #
        # select.select_by_visible_text("Search Engine Marketing/Optimization")
        # print("Select Search Engine Marketing/Optimization as expenses type")
        # time.sleep(1)
        #
        # select.select_by_visible_text("Public Relations")
        # print("Select Public Relations as expenses type")
        # time.sleep(1)
        #
        # select.select_by_visible_text("Out of Home Media")
        # print("Select Out of Home Media as expenses type")
        # time.sleep(1)
        #
        # select.select_by_visible_text("Content Creation and Management")
        # print("Select Content Creation and Management as expenses type")
        # time.sleep(1)
        #
        # select.select_by_visible_text("Channel Marketing")
        # print("Select Channel Marketing as expenses type")
        # time.sleep(1)
        #
        # select.select_by_visible_text("Email Marketing")
        # print("Select Email Marketing as expenses type")
        # time.sleep(1)
        #
        # select.select_by_visible_text("Event Marketing")
        # print("Select Event Marketing as expenses type")
        # time.sleep(1)
        #
        # select.select_by_visible_text("Print Advertising")
        # print("Select Print Advertising as expenses type")
        # time.sleep(1)
        #
        # select.select_by_visible_text("Research")
        # print("Select Research as expenses type")
        # time.sleep(1)
        #
        # select.select_by_visible_text("Web")
        # print("Select Web as expenses type")
        # time.sleep(1)
        #
        # select.select_by_visible_text("Mobile Marketing")
        # print("Select Mobile Marketing as expenses type")
        # time.sleep(1)
        #
        # select.select_by_visible_text("Social Media Marketing")
        # print("Select Social Media Marketing as expenses type")
        # time.sleep(1)
        #
        # select.select_by_visible_text("Marketing Analytics")
        # print("Select Marketing Analytics as expenses type")
        # time.sleep(1)
        #
        # select.select_by_visible_text("Digital Advertising")
        # print("Select Digital Advertising as expenses type")
        # time.sleep(1)
        #
        # select.select_by_visible_text("Digital Commerce")
        # print("Select Digital Commerce as expenses type")
        # time.sleep(1)

        vendor_name = driver.find_element_by_xpath("//*[@id='addExpensesColl1']/div/div/div[1]/div[5]/ng2-completer/div/input")
        vendor_name.send_keys("v1")
        time.sleep(1)

        po_number = driver.find_element_by_xpath("//*[@id='addExpensesColl1']/div/div/div[1]/div[6]/input")
        po_number.send_keys("123456")
        time.sleep(1)


        add_notes = driver.find_element_by_xpath("//*[@id='addExpensesColl1']/div/div/div[2]/div[2]/textarea")
        add_notes.send_keys("Add Notes here")
        time.sleep(3)

        deliveryDate_link = driver.find_element_by_css_selector("button.btnpicker.btnpickerenabled").click()
        delivery_date = driver.find_element_by_css_selector("div.datevalue.currmonth > span").click()
        time.sleep(1)

        continueBtn1 = driver.find_element_by_xpath("//*[@id='addExpensesColl1']/div/div/div[3]/div/div/div")
        continueBtn1.click()
        time.sleep(3)

        # Choose timeframe

        # q1 = driver.find_element_by_xpath("//*[@id='addExpensesColl2']/div/div/div/div[1]/div[1]/label/input")
        # q1.click()
        # time.sleep(1)

        q2 = driver.find_element_by_xpath("//*[@id='addExpensesColl2']/div/div/div/div[1]/div[2]/label/input")
        q2.click()
        time.sleep(1)

        q3 = driver.find_element_by_xpath("//*[@id='addExpensesColl2']/div/div/div/div[1]/div[3]/label/input")
        q3.click()
        time.sleep(1)

        q4 = driver.find_element_by_xpath("//*[@id='addExpensesColl2']/div/div/div/div[1]/div[4]/label/input")
        q4.click()
        time.sleep(1)

        finishBtn = driver.find_element_by_xpath("//*[@id='form-addExpenseDetail']/div[3]/button[1]")
        finishBtn.click()
        time.sleep(5)

    def main(self):
        self.testExpenses(self.driver)

# We have to call this main method and here we are accessing it's own class methods
if __name__ == '__main__':
    expensesWithoutGoalCampaignProgram = AddExpensesWithoutGoalCampaignProgram()
    expensesWithoutGoalCampaignProgram.main()

