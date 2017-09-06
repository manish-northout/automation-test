from Plannuh_delete.user_login import Login
import time


class DeleteProgram():
    def __init__(self):
        login = Login()
        self.driver = login.driver
        login.main()

    def deleteprogram(self, driver):

            try:
                time.sleep(5)

                print("Click on program under campaign")
                p = driver.find_element_by_xpath("//div[@id='tab-goal-1']/div[1]/ul/li/div/div[3]/ul[1]/li[1]/a")
                p.click()
                time.sleep(5)

                print("Click on edit program")
                p2 = driver.find_element_by_xpath(
                    "/html/body/modal-overlay/bs-modal-container/div/div/modal-content/div/div/div/div[2]/div[2]/button")
                p2.click()
                time.sleep(5)

                print("Click on delete button")
                p3 = driver.find_element_by_xpath("//*[@id='form-addGoalDetail']/div[3]/button[2]")
                p3.click()
                time.sleep(5)

                print("Click on alert box")
                alert = driver.switch_to_alert()
                alert.dismiss()

                print("No program found")
            except:
                print("No program found")




    def main(self):
        self.deleteprogram(self.driver)

if __name__ =='__main__':
    program = DeleteProgram()
    program.main()