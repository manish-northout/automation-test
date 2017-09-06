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

class Update_Program_ViaGoalAndCampaign():
    def __init__(self):
        # Now creating object of Login class login1 and accessing variable driver of Login class by login1 object and storing it in self.driver
        login1 = Login()
        self.driver = login1.driver
        login1.main()

    def testGoals(self, driver):

        time.sleep(10)

        element = driver.find_element(By.XPATH, "/html/body/app-root/app-root/article/div[1]/div[1]/ul[1]/li[2]/a")
        itemToClickLocator = driver.find_element_by_xpath("/html/body/app-root/app-root/article/div[1]/div[1]/ul[1]/li[2]/ul/li[4]/a")
        try:
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()
            print("Mouse Hovered on Timeframe")
            time.sleep(2)
            # topLink = driver.find_element(By.XPATH, itemToClickLocator)
            actions.move_to_element(itemToClickLocator).click().perform()
            print("Click on Particular Timeframe")
            time.sleep(5)
        except:
            print("Mouse Hover failed on element")


        Goal = driver.find_element_by_link_text("GoalToAddCampaign")
        Goal.click()
        print("CLick on particular Goal")
        time.sleep(5)

        Program = driver.find_element_by_link_text("Program1")
        Program.click()
        print("CLick on particular Program")
        time.sleep(5)

        Edit_Program = driver.find_element_by_xpath("/html/body/modal-overlay/bs-modal-container/div/div/modal-content/div/div/div/div[2]/div[3]/button")
        Edit_Program.click()
        time.sleep(2)
        print("CLick on Edit Program")


        continueBtn1 = driver.find_element_by_xpath("//*[@id='editProgramColl1']/div/div/div[3]/div/div/div/a")
        continueBtn1.click()
        time.sleep(5)
        print("Click on Continue button")

        # q1 = driver.find_element_by_xpath("//*[@id='editProgramColl2']//input[@value='33']")
        # q1.click()
        # time.sleep(1)
        #
        # # q2 = driver.find_element_by_xpath("//*[@id='editProgramColl2']//input[@value='34']")
        # # q2.click()
        # # time.sleep(1)
        #
        # q3 = driver.find_element_by_xpath("//*[@id='editProgramColl2']//input[@value='35']")
        # q3.click()
        # time.sleep(1)
        #
        # q4 = driver.find_element_by_xpath("//*[@id='editProgramColl2']//input[@value='36']")
        # q4.click()
        # time.sleep(1)

        clear_btn = driver.find_element_by_xpath("//*[@id='tab-editProgram-1']/button")
        clear_btn.click()
        time.sleep(4)
        print("Click on Clear button")


        Goal1 = driver.find_element_by_xpath("//*[@id='tab-editProgram-1']/div/div[1]/label/input")
        Goal1.click()
        time.sleep(4)

        Goal2 = driver.find_element_by_xpath("//*[@id='tab-editProgram-1']/div/div[2]/label/input")
        Goal2.click()
        time.sleep(4)

        Campaign = driver.find_element_by_xpath("//*[@id='editProgramColl2']/div/div/div[1]/div[2]/nav/ul/li[2]/a")
        Campaign.click()
        time.sleep(4)

        # clear_btn = driver.find_element_by_xpath("//*[@id='tab-editProgram-2']/button")
        # clear_btn.click()
        # time.sleep(1)

        c1 = driver.find_element_by_xpath("//*[@id='tab-editProgram-2']/div[1]/div[1]/label/input")
        c1.click()
        time.sleep(1)


        continueBtn2 = driver.find_element_by_xpath("//*[@id='editProgramColl2']/div/div/div[2]/div/a")
        continueBtn2.click()
        time.sleep(3)

        Finish = driver.find_element_by_xpath("//*[@id='form-addGoalDetail']/div[3]/button[1]")
        Finish.click()
        time.sleep(6)

        ViewProgramInGoal = driver.find_element_by_link_text("G2")
        ViewProgramInGoal.click()
        time.sleep(3)
        print("View particular Program in new assigned Goal")

        AccessProgram = driver.find_element_by_link_text("Program1")
        AccessProgram.click()
        time.sleep(3)
        print("Again click on same program to reset values")

        Edit_Program = driver.find_element_by_xpath(
            "/html/body/modal-overlay/bs-modal-container/div/div/modal-content/div/div/div/div[2]/div[3]/button")
        Edit_Program.click()
        time.sleep(2)
        print("CLick on Edit Program")

        continueBtn1 = driver.find_element_by_xpath("//*[@id='editProgramColl1']/div/div/div[3]/div/div/div/a")
        continueBtn1.click()
        time.sleep(5)
        print("Click on Continue button")

        Goal1 = driver.find_element_by_xpath("//*[@id='tab-editProgram-1']/div/div[1]/label/input")
        Goal1.click()
        time.sleep(4)

        Campaign = driver.find_element_by_xpath("//*[@id='editProgramColl2']/div/div/div[1]/div[2]/nav/ul/li[2]/a")
        Campaign.click()
        time.sleep(4)

        c1 = driver.find_element_by_xpath("//*[@id='tab-editProgram-2']/div[1]/div[1]/label/input")
        c1.click()
        time.sleep(1)

        continueBtn2 = driver.find_element_by_xpath("//*[@id='editProgramColl2']/div/div/div[2]/div/a")
        continueBtn2.click()
        time.sleep(3)

        Finish = driver.find_element_by_xpath("//*[@id='form-addGoalDetail']/div[3]/button[1]")
        Finish.click()
        time.sleep(3)
        print("Successfully reset Program and assigned it to same Goal and Campaign so that Test Case can run again")


        # element = driver.find_element(By.XPATH, "/html/body/app-root/app-root/article/div[1]/div[1]/ul[1]/li[2]/a")
        # itemToClickLocator = driver.find_element_by_xpath("/html/body/app-root/app-root/article/div[1]/div[1]/ul[1]/li[2]/ul/li[1]/a")
        # try:
        #     actions = ActionChains(driver)
        #     actions.move_to_element(element).perform()
        #     print("Mouse Hovered on element")
        #     time.sleep(2)
        #     # topLink = driver.find_element(By.XPATH, itemToClickLocator)
        #     actions.move_to_element(itemToClickLocator).click().perform()
        #     print("Item Clicked")
        # except:
        #     print("Mouse Hover failed on element")
        #
        #     element = driver.find_element(By.CLASS_NAME, "btn-viewGoal")
        #     try:
        #         actions = ActionChains(driver)
        #         actions.move_to_element(element).perform()
        #         print("Mouse Hovered on element")
        #         time.sleep(2)
        #         # topLink = driver.find_element(By.XPATH, itemToClickLocator)
        #         # actions.move_to_element(itemToClickLocator).click().perform()
        #         # print("Item Clicked")
        #     except:
        #         print("Mouse Hover failed on element")







        # Creating a main method and here we are calling
    def main(self):
        self.testGoals(self.driver)

# We have to call this main method and here we are accessing it's own class methods
if __name__ =='__main__':
    goal = Update_Program_ViaGoalAndCampaign()
    goal.main()

