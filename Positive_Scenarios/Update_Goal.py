from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import os

from selenium.webdriver.support.select import Select
from Positive_Scenarios.Driver_Launch import launch
from Positive_Scenarios.Login import Login
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class UpdateGoals():
    def __init__(self):
        # Now creating object of Login class login1 and accessing variable driver of Login class by login1 object and storing it in self.driver
        login1 = Login()
        self.driver = login1.driver
        login1.main()

    def testGoals(self, driver):

        time.sleep(10)

        View = driver.find_element_by_class_name("btn-viewGoal")
        View.click()
        print("CLick View button")
        time.sleep(5)

        Edit_goals = driver.find_element_by_xpath("/html/body/modal-overlay/bs-modal-container/div/div/modal-content/div/div/div/div[2]/div[2]/button")
        Edit_goals.click()
        print("CLick on Edit goals")
        time.sleep(5)

        # goal_name = driver.find_element_by_xpath("//*[@id='form-addGoalDetail']/div[1]/div[1]/input")
        # goal_name.send_keys("G1")
        # time.sleep(1)

        current_status = driver.find_element_by_xpath("//div[@id='form-addGoalDetail']/div[1]/div[2]/div/select")
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

        add_note = driver.find_element_by_xpath("//div[@id='form-addGoalDetail']/div[1]/div[3]/textarea")
        add_note.clear()
        add_note.send_keys("Add notes here")
        time.sleep(1)

        continueBtn1 = driver.find_element_by_xpath("//*[@id='form-addGoalDetail']/div[3]/div/div/div")
        continueBtn1.click()
        time.sleep(5)
        print("Choose time frame")

        # time_frame = driver.find_elements(By.XPATH, "//input[contains(@type, 'checkbox')]")
        # select = Select(time_frame)
        # time.sleep(1)
        #
        # select.select_by_index(0)
        # print("Select planned as current status")
        # time.sleep(1)
        #
        #

        q1 = driver.find_element_by_xpath("//*[@id='form-addGoalTimeFrame']/div/div[1]/div[1]/label/input")
        q1.click()
        time.sleep(1)

        q2 = driver.find_element_by_xpath("//*[@id='form-addGoalTimeFrame']/div/div[1]/div[2]/label/input")
        q2.click()
        time.sleep(1)

        q3 = driver.find_element_by_xpath("//*[@id='form-addGoalTimeFrame']/div/div[1]/div[3]/label/input")
        q3.click()
        time.sleep(1)

        q4 = driver.find_element_by_xpath("//*[@id='form-addGoalTimeFrame']/div/div[1]/div[4]/label/input")
        q4.click()
        time.sleep(1)

        q1 = driver.find_element_by_xpath("//*[@id='form-addGoalTimeFrame']/div/div[1]/div[1]/label/input")
        q1.click()
        time.sleep(1)

        q2 = driver.find_element_by_xpath("//*[@id='form-addGoalTimeFrame']/div/div[1]/div[2]/label/input")
        q2.click()
        time.sleep(1)

        continueBtn2 = driver.find_element_by_xpath("//*[@id='form-addGoalTimeFrame']/div/div[2]/a")
        continueBtn2.click()
        time.sleep(3)

        choose_metric1 = driver.find_element_by_xpath("//*[@id='form-addGoalTrack']/div/div/div[1]/div/select")
        select1 = Select(choose_metric1)

        select1.select_by_value("Other")
        print("Select Other by value")
        time.sleep(1)

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
        #
        # # sel.select_by_index("2")
        # # print("Select Honda by index")
        # # time.sleep(1)
        # #
        # # sel.select_by_visible_text("BMW")
        # # print("Select BMW by visible text")
        # # time.sleep(1)
        # #
        # # sel.select_by_index(2)
        # # print("Select Honda by index")

        projecting_1 = driver.find_element_by_xpath("//*[@id='form-addGoalTrack']/div/div/div[2]/input")
        projecting_1.clear()
        projecting_1.send_keys("1000")
        time.sleep(1)

        add_metric = driver.find_element_by_xpath("//*[@id='form-addGoalTrack']/div/button")
        add_metric.click()
        time.sleep(1)

        choose_metric2 = driver.find_element_by_xpath("//*[@id='form-addGoalTrack']/div/div[2]/div[1]/div/select")
        select2 = Select(choose_metric2)
        time.sleep(1)

        # select2.select_by_value("Other")
        # print("Select Other by value")
        # time.sleep(1)

        select2.select_by_value("New customers")
        print("Select New customers by value")
        time.sleep(1)
        #
        # select2.select_by_value("Registrations")
        # print("Select Registrations by value")
        # time.sleep(1)
        #
        # select2.select_by_value("Website visits")
        # print("Select Website visits by value")
        # time.sleep(1)
        #
        # select2.select_by_value("Bookings")
        # print("Select Bookings by value")
        # time.sleep(1)
        #
        # select2.select_by_value("Pipeline")
        # print("Select Pipeline by value")
        # time.sleep(1)
        #
        # select2.select_by_value("Revenue")
        # print("Select Revenue by value")
        # time.sleep(1)
        #
        # select2.select_by_value("Opportunities")
        # print("Select Opportunities by value")
        # time.sleep(1)
        #
        # select2.select_by_value("Leads")
        # print("Select Leads by value")
        # time.sleep(1)

        projecting_2 = driver.find_element_by_xpath("//*[@id='form-addGoalTrack']/div/div[2]/div[2]/input")
        projecting_2.clear()
        projecting_2.send_keys("1000")
        time.sleep(1)

        finishBtn = driver.find_element_by_xpath("//*[@id='form-addGoalDetail']/div[3]/button[1]")
        finishBtn.click()
        time.sleep(5)

        # closeBtn = driver.find_element_by_xpath("//*[@id='form-addGoalDetail']/div[3]/button[2]")
        # closeBtn.click()
        # time.sleep(5)

        # select2.select_by_value("Other")
        # print("Select Other by value")
        # time.sleep(1)


        element = driver.find_element(By.XPATH, "/html/body/app-root/app-root/article/div[1]/div[1]/ul[1]/li[2]/a")
        itemToClickLocator = driver.find_element_by_xpath("/html/body/app-root/app-root/article/div[1]/div[1]/ul[1]/li[2]/ul/li[1]/a")
        try:
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()
            print("Mouse Hovered on element")
            time.sleep(2)
            # topLink = driver.find_element(By.XPATH, itemToClickLocator)
            actions.move_to_element(itemToClickLocator).click().perform()
            print("Item Clicked")
        except:
            print("Mouse Hover failed on element")

            element = driver.find_element(By.CLASS_NAME, "btn-viewGoal")
            try:
                actions = ActionChains(driver)
                actions.move_to_element(element).perform()
                print("Mouse Hovered on element")
                time.sleep(2)
                # topLink = driver.find_element(By.XPATH, itemToClickLocator)
                # actions.move_to_element(itemToClickLocator).click().perform()
                # print("Item Clicked")
            except:
                print("Mouse Hover failed on element")


                element = driver.find_element(By.XPATH,"/html/body/app-root/app-root/article/div[1]/div[1]/ul[1]/li[2]/a")
                itemToClickLocator = driver.find_element_by_xpath("/html/body/app-root/app-root/article/div[1]/div[1]/ul[1]/li[2]/ul/li[2]/a")
                try:
                    actions = ActionChains(driver)
                    actions.move_to_element(element).perform()
                    print("Mouse Hovered on element")
                    time.sleep(2)
                    # topLink = driver.find_element(By.XPATH, itemToClickLocator)
                    actions.move_to_element(itemToClickLocator).click().perform()
                    print("Item Clicked")
                except:
                    print("Mouse Hover failed on element")




        # Creating a main method and here we are calling
    def main(self):
        self.testGoals(self.driver)

# We have to call this main method and here we are accessing it's own class methods
if __name__ =='__main__':
    goal = UpdateGoals()
    goal.main()

