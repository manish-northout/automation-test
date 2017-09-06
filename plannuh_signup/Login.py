
import time


class Login():
    def testLogin(self, driver):
        baseUrl = "http://plannuh-stage-front.us-east-1.elasticbeanstalk.com/login"
        driver.get(baseUrl)
        time.sleep(5)

        loginId = driver.find_element_by_xpath("//form[@id='form-signUp']/div/div[1]/input")
        loginId.send_keys("testnorthout0@gmail.com")
        time.sleep(3)

        loginPassword = driver.find_element_by_xpath("//*[@id='form-signUp']/div/div[2]/input")
        loginPassword.send_keys("northout1234")
        time.sleep(3)

        loginBtn = driver.find_element_by_xpath("//form[@id='form-signUp']/div/div[4]/button")
        loginBtn.click()

        print("Valid email id and password")

