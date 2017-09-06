
import time
from plannuh_creation.Driver_Launch import launch

class Login():

    def __init__(self):
        launch1 = launch()
        self.driver = launch1.driverLaunch()

    def testLogin(self, driver):

        time.sleep(3)

        loginId = driver.find_element_by_xpath("//input[@name='email']")
        loginId.send_keys("testnorthout0@gmail.com")
        print("Please type valid Login ID")
        time.sleep(1)

        loginPassword = driver.find_element_by_xpath("//input[@name='password']")
        loginPassword.send_keys("northout1234")
        print("Please type valid Password")
        time.sleep(5)

        loginBtn = driver.find_element_by_xpath("//form[@id='form-signUp']//button")
        loginBtn.click()
        print("Valid email id and password")
        time.sleep(5)

    def main(self):
        self.testLogin(self.driver)

if __name__ =='__main__':
    login1 = Login()
    login1.main()

