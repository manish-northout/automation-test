from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from selenium.webdriver.support.select import Select

class AddProgramWithoutGoalCampaign():
    def testProgram(self, driver):
        time.sleep(10)

        add = driver.find_element_by_class_name("btn-addgoals")
        add.click()
        print("CLick Add button")
        time.sleep(5)

        add_program = driver.find_element_by_class_name("btn-program")
        add_program.click()
        time.sleep(5)

        program_name = driver.find_element_by_xpath("//*[@id='addProgramColl1']/div/div/div[1]/div[1]/input")
        program_name.send_keys("prog")
        time.sleep(1)

        current_status = driver.find_element_by_xpath("//*[@id='addProgramColl1']/div/div/div[1]/div[2]/div/select")
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

        budget = driver.find_element_by_xpath("//*[@id='addProgramColl1']/div/div/div[1]/div[3]/input")
        budget.send_keys("1234")
        time.sleep(1)

        # add_notes = driver.find_element_by_xpath("//*[@id='addProgramColl1']/div/div/div[1]/div[4]/textarea")
        # add_notes.send_keys("Add notes here")
        # time.sleep(1)

        continueBtn1 = driver.find_element_by_xpath("//*[@id='addProgramColl1']/div/div/div[3]/div/div/div")
        continueBtn1.click()
        time.sleep(3)


        q2 = driver.find_element_by_xpath("//*[@id='addProgramColl2']/div/div/div[1]/div[1]/div[2]/label/input")
        q2.click()
        time.sleep(3)

        q3 = driver.find_element_by_xpath("//*[@id='addProgramColl2']/div/div/div[1]/div[1]/div[3]/label/input")
        q3.click()
        time.sleep(3)

        q4 = driver.find_element_by_xpath("//*[@id='addProgramColl2']/div/div/div[1]/div[1]/div[4]/label/input")
        q4.click()
        time.sleep(3)

        continueBtn2 = driver.find_element_by_xpath("//*[@id='addProgramColl2']/div/div/div[2]/div/div/a")
        continueBtn2.click()
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







