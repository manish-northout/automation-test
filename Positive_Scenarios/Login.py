import time
from Positive_Scenarios.Driver_Launch import launch
import unittest

# Calling Login via unittest feature
class LoginTests(unittest.TestCase):

    # We have to create this init method to create object of another class launch and call it's methods
    # We are using self.driver here because we called it below in main method
    # def __init__(self,driver):
    #     launch1 = launch()
    #     self.driver = launch1.driverLaunch()

    # def __init__(self):
    #     self.driverLaunch()

    def test_Login(self):
        try :
            try:
                launch1 = launch()
                self.driver = launch1.driverLaunch()
            except  Exception as es:
                print(es)
            print('Enter email')

            loginId = self.driver.find_element_by_xpath("//form[@id='form-signUp']/div/div[1]/input")
            print('checking..')
            print(loginId)
            loginId.send_keys("t.estnorthout0@gmail.com")
            time.sleep(3)



            print('Enter password')

            loginPassword = self.driver.find_element_by_xpath("//*[@id='form-signUp']/div/div[2]/input")
            loginPassword.send_keys("northout1234")
            time.sleep(3)

            loginBtn = self.driver.find_element_by_xpath("//*[@id='form-signUp']/div/div[3]/button")
            loginBtn.click()

            print("Valid email id and password")
        except Exception as e:
            print(e)


            # baseUrl = "http://plannuh-stage-front.us-east-1.elasticbeanstalk.com/login"
        # driver.get(baseUrl)




# # Creating a main method and here we are calling
#     def main(self):
#         self.test_Login()(self.driver)

# We have to call this main method and here we are accessing it's own class methods
if __name__ =='__main__':
    # login1 = Login()
    # login1.main()
    unittest.main(verbosity=2)


