from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import os
from plannuh_edition.Driver_Launch import launch
from plannuh_edition.Login import Login

class EditProgramRemoveCampaign():

    def __init__(self):
        login1 = Login()
        self.driver = login1.driver
        login1.main()

    def testRemoveCampaign(self, driver):

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

        campaign_link = driver.find_element_by_xpath("//*[@id='editProgramColl2']/div/div/div[1]/div[2]/nav/ul/li[2]/a").click()
        time.sleep(1)
        print("Click on campaign link")

        clear_selected_campaign = driver.find_element_by_xpath("//*[@id='tab-editProgram-2']/button").click()
        time.sleep(1)
        print("Remove selected Campaign")

        finishBtn = driver.find_element_by_xpath("//form[@id='form-addGoalDetail']//button[contains(text(), 'Finish')]")
        finishBtn.click()
        print("Finish the process")
        time.sleep(5)

    def main(self):
        self.testRemoveCampaign(self.driver)

# We have to call this main method and here we are accessing it's own class methods
if __name__ == '__main__':
    edit_program_remove_campaign = EditProgramRemoveCampaign()
    edit_program_remove_campaign.main()









