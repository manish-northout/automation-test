from Plannuh_delete.user_login import Login
import time

class DeleteExpenses():

    def __init__(self):
        login= Login()
        self.driver=login.driver
        login.main()

    def deleteexpnses(self, driver):

        time.sleep(12)
        print("Click on view expenses")
        e1=driver.find_element_by_xpath("//div[@id='tab-dashboardTable-1']//table//td[2]//div/label/input")
        e1.click()
        time.sleep(5)

        print("Click on edit expenses")
        e2= driver.find_element_by_css_selector("button.btn.btn-skyBlue")
        e2.click()
        time.sleep(5)

        print("click on delete button")
        e3= driver.find_element_by_css_selector("button.btn.btn-danger")
        e3.click()
        time.sleep(5)

        print("Click on alert box")
        alert= driver.switch_to_alert()
        alert.dismiss()


    def main(self):
        self.deleteexpnses(self.driver)


if __name__ =='__main__':
    exp= DeleteExpenses()
    exp.main()
