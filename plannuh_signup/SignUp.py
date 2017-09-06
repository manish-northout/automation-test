
import time
class SignUp(object):
    def testSignup(self, driver):

        driver.implicitly_wait(3)

        createAccount = driver.find_element_by_class_name("link-createAcc")
        createAccount.click()
        time.sleep(1)

        fullName = driver.find_element_by_name("full_name")
        fullName.send_keys("Aparna")
        print("Valid name")

        companyName = driver.find_element_by_name("company_name")
        companyName.send_keys("Northout Solutions pvt. ltd.")
        time.sleep(3)
        print("Valid company name")

        workEmail = driver.find_element_by_name("email")
        workEmail.send_keys("testnorthout0@gmail.com")
        print("Valid email")

        password = driver.find_element_by_name("password")
        password.send_keys("northout1234")
        print("Valid Password")
        time.sleep(3)

        confirmPassword = driver.find_element_by_name("confirmPassword")
        confirmPassword.send_keys("northout1234")
        time.sleep(3)
        print("password and confirm password field matched")

        acceptTearmsAndConditions = driver.find_element_by_name("acceptTerms")
        acceptTearmsAndConditions.click()
        time.sleep(3)

        readyToStart = driver.find_element_by_xpath("//form[@id='form-signUp']/div/div[7]/button")
        readyToStart.click()
        time.sleep(3)

