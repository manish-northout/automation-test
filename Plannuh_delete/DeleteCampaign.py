from Plannuh_delete.user_login import Login
import time


class DeleteCampaign():
    def __init__(self):
       login= Login()
       self.driver= login.driver
       login.main()


    def deletecam(self, driver):
        # try:
            time.sleep(8)
            print("Click on campaign")
            camp= driver.find_element_by_xpath("//div[@id='tab-goal-1']//div[1]/a")
            camp.click()
            time.sleep(5)

            print("Click on edit campaign button")
            edit= driver.find_element_by_xpath("html/body/modal-overlay/bs-modal-container//div/div[2]/div[3]/button")
            edit.click()
            time.sleep(5)

            print("Click on delete button")
            delcam= driver.find_element_by_xpath("//*[@id='form-editCampaign']//div/div[3]/button[2]")
            delcam.click()
            time.sleep(5)

            print("click on alert box")
            alert= driver.switch_to_alert()
            alert.dismiss()
        # except:
        #     print("No campaign found")




    def main(self):
        self.deletecam(self.driver)



if __name__ =='__main__':
    cam = DeleteCampaign()
    cam.main()
