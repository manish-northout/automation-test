from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import os
from plannuh_edition.Driver_Launch import launch
from plannuh_edition.Login import Login
from plannuh_edition.edit_program_remove_campaign import EditProgramRemoveCampaign

class EditProgramRemoveGoal():

    def __init__(self):
        edit_program_remove_campaign = EditProgramRemoveCampaign()
        self.driver = edit_program_remove_campaign.driver
        edit_program_remove_campaign.main()

    def testRemoveGoal(self, driver):

        time.sleep(5)

        select_goal = driver.find_element_by_link_text("Goal1").click()
        time.sleep(3)
        print("Select Goal")

        view_program = driver.find_element_by_link_text("p1").click()
        time.sleep(5)
        print("Select Program")

        edit_program = driver.find_element_by_xpath("/html/body/modal-overlay/bs-modal-container/div/div/modal-content/div/div/div/div[2]/div[2]/button")
        edit_program.click()
        print("Click edit program")
        time.sleep(5)

        continueBtn = driver.find_element_by_xpath("//*[@id='editProgramColl1']/div/div/div[3]/div/div/div/a").click()
        print("Click continue button")
        time.sleep(3)

        clear_selected_goal = driver.find_element_by_xpath("//*[@id='tab-editProgram-1']/button").click()
        time.sleep(1)
        print("Remove selected Goal")

        finishBtn = driver.find_element_by_xpath("//*[@id='form-addGoalDetail']/div[3]/button[1]")
        finishBtn.click()
        print("Finish the process")
        time.sleep(10)


    def main(self):
        self.testRemoveGoal(self.driver)

# We have to call this main method and here we are accessing it's own class methods
if __name__ == '__main__':
    edit_program_remove_goal = EditProgramRemoveGoal()
    edit_program_remove_goal.main()






