from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import os

from selenium.webdriver.support.select import Select
from plannuh_edition.Driver_Launch import launch
from plannuh_edition.Login import Login
from plannuh_edition.edit_campaign import EditCampaign
from plannuh_edition.edit_campaign_add_program import EditCampaignAddProgram
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class EditCampaignAddExpenses():

    # def __init__(self):
    #     editCampaignAddProgram = EditCampaignAddProgram()
    #     self.driver = editCampaignAddProgram.driver
    #     editCampaignAddProgram.main()

    def __init__(self):
        login1 = Login()
        self.driver = login1.driver
        login1.main()

    def testCampaign(self, driver):

        time.sleep(10)

        select_goal = driver.find_element_by_link_text("Goal3").click()
        time.sleep(3)
        print("Select Goal")

        view_campaign = driver.find_element_by_link_text("Campaign1").click()
        time.sleep(5)
        print("Select Campaign")

        select_expenses = driver.find_element_by_xpath("/html/body/modal-overlay/bs-modal-container/div/div/modal-content/div/div/div/div[2]/div[1]/nav/ul/li[2]/a")
        select_expenses.click()
        time.sleep(3)
        print("Select expenses link")

        add_expenses = driver.find_element_by_xpath("//*[@id='tab-viewCampaign-2']/button").click()
        time.sleep(3)
        print("Add new expenses")

        expenses_name = driver.find_element_by_xpath("//*[@id='addExpensesColl1']/div/div/div[1]/div[1]/input")
        expenses_name.send_keys("Expenses6")
        time.sleep(1)
        print("Type expenses name")

        current_status = driver.find_element_by_xpath("//*[@id='addExpensesColl1']/div/div/div[1]/div[2]/div/select")
        select = Select(current_status)
        time.sleep(1)
        print("Select current status")

        select.select_by_value("Planned")
        print("Select Planned as current status")
        time.sleep(1)

        # select.select_by_value("Committed")
        # print("Select Committed as current status")
        # time.sleep(1)
        #
        # select.select_by_value("Vendor Selected")
        # print("Select Vendor Selected as current status")
        # time.sleep(1)

        # select.select_by_value("Delivered")
        # print("Select Delivered as current status")
        # time.sleep(1)
        #
        # select.select_by_value("Billed")
        # print("Select Billed as current status")
        # time.sleep(1)

        status_amount = driver.find_element_by_xpath("//*[@id='addExpensesColl1']/div/div/div[1]/div[3]/input")
        status_amount.send_keys("1000")
        time.sleep(1)
        print("Type status amount")

        expenses_type = driver.find_element_by_xpath("//*[@id='addExpensesColl1']/div/div/div[1]/div[4]/div/select")
        select = Select(expenses_type)
        print("Select expenses type")

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

        vendor_name = driver.find_element_by_xpath(
            "//*[@id='addExpensesColl1']/div/div/div[1]/div[5]/ng2-completer/div/input")
        vendor_name.send_keys("v1")
        time.sleep(1)
        print("Type vendor name")

        po_number = driver.find_element_by_xpath("//*[@id='addExpensesColl1']/div/div/div[1]/div[6]/input")
        po_number.send_keys("123456")
        time.sleep(1)
        print("Type po number")

        add_notes = driver.find_element_by_xpath("//*[@id='addExpensesColl1']/div/div/div[2]/div[2]/textarea")
        add_notes.send_keys("Add Notes here")
        time.sleep(3)
        print("Add notes")

        deliveryDate_link = driver.find_element_by_css_selector("button.btnpicker.btnpickerenabled").click()
        delivery_date = driver.find_element_by_css_selector("div.datevalue.currmonth > span").click()
        time.sleep(1)
        print("Select delivery date")

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

        # Choose Goal

        goal = driver.find_element_by_xpath("//input[@type='radio']").click()
        print("Select goal for selected timeframe")
        time.sleep(3)

        # Choose Campaign

        campaign_link = driver.find_element_by_link_text("Campaigns").click()
        time.sleep(3)
        print("Select campaign link")

        campaign = driver.find_element_by_xpath("//*[@id='tab-addExpenses-2']/div[1]/div/label/input").click()
        time.sleep(3)
        print("Select campaign for the selected timeframe and goal")

        # Choose Program

        program_link = driver.find_element_by_link_text("Program").click()
        time.sleep(3)
        print("Select program link")

        program = driver.find_element_by_xpath("//*[@id='tab-addExpenses-3']/div[1]/div[1]/label/input").click()
        time.sleep(3)
        print("Select program for the selected timeframe, goal and campaign")

        finishBtn = driver.find_element_by_xpath("//*[@id='form-addExpenseDetail']/div[3]/button[1]")
        finishBtn.click()
        time.sleep(5)

        alert1 = driver.switch_to_alert()
        alert1.accept()
        time.sleep(5)

    def main(self):
        self.testCampaign(self.driver)

# We have to call this main method and here we are accessing it's own class methods
if __name__ == '__main__':
    editCampaignAddExpenses = EditCampaignAddExpenses()
    editCampaignAddExpenses.main()





