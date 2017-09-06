
from Plannuh_delete.user_login import Login
import time


class DeleteGoal():

    def __init__(self):
       login= Login()
       self.driver= login.driver
       login.main()

    def deletegoal(self, driver):
        time.sleep(15)
        print("click on view goal")
        view = driver.find_element_by_xpath("//div[@id='tab-goal-1']/button")
        view.click()
        time.sleep(5)

        print("Click on edit goal")
        editgoal = driver.find_element_by_xpath("html/body/modal-overlay/bs-modal-container//div/modal-content//div/div[2]/div[3]/button")
        editgoal.click()
        time.sleep(3)

        print("Click on delete button")
        delete = driver.find_element_by_css_selector("#form-addGoalDetail > div.modal-footer > button.btn.btn-danger")
        delete.click()
        time.sleep(5)

        print("Click on alert box")
        alert = driver.switch_to.alert
        time.sleep(5)
        alert.dismiss()





    def main(self):
        self.deletegoal(self.driver)

# We have to call this main method and here we are accessing it's own class methods
if __name__ =='__main__':
    goal = DeleteGoal()
    goal.main()













