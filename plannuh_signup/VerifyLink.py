from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

class VerifyLink(object):
    def testverificationLink(self, driver):
        baseUrl = "https://accounts.google.com/signin/v2/sl/pwd?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin"

        driver.get(baseUrl)
        time.sleep(2)

        email_id = driver.find_element_by_xpath("//input[@id='identifierId']")
        email_id.send_keys("testnorthout0@gmail.com")
        time.sleep(2)

        clickNext1 = driver.find_element_by_xpath("//div[@id='identifierNext']/content/span")
        clickNext1.click()
        time.sleep(2)

        password = driver.find_element_by_xpath("//div[@id='password']/div[1]/div/div[1]/input")
        password.send_keys("northout1234")
        time.sleep(2)

        clickNext2 = driver.find_element_by_xpath("//div[@id='passwordNext']/content/span")
        clickNext2.click()
        time.sleep(4)
        print("Success")

        clickMail = driver.find_element_by_xpath("//*[@id=':37']")
        clickMail.click()
        time.sleep(4)
        print("click mail")

        clickVerificationLink = driver.find_element_by_xpath(
            "//a[contains(@href, 'http://plannuh-stage-front.us-east-1.elasticbeanstalk.com/verify_user')]")
        clickVerificationLink.click()
        time.sleep(2)
        print("click verification link")


