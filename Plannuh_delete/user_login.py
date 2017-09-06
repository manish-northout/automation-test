import  time
from plannuh.Plannuh_delete.Launch import Launch


class Login(Launch):

    def __init__(self):
        launch1 = Launch()
        self.driver = launch1.driverlaunch()

    def testLogin(self, driver):
        print("Enter email")
        loginId = driver.find_element_by_xpath("//form[@id='form-signUp']/div/div[1]/input")
        loginId.send_keys("sourabh.charwande@northout.com")
        time.sleep(1)

        print("Enter password")
        loginPassword = driver.find_element_by_xpath("//*[@id='form-signUp']/div/div[2]/input")
        loginPassword.send_keys("123456")
        time.sleep(1)

        print("Click on login button")
        loginBtn = driver.find_element_by_xpath("//form[@id='form-signUp']/div/div[4]/button")
        loginBtn.click()


        print("Login success")

# Creating a main method and here we are calling
    def main(self):
        self.testLogin(self.driver)

# We have to call this main method and here we are accessing it's own class methods
if __name__ =='__main__':
    login1 = Login()
    login1.main()

