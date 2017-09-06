from selenium.webdriver.support.select import Select
import time
from plannuh_edition.Login import Login

class EditExpenses():

    def __init__(self):
        login1 = Login()
        self.driver = login1.driver
        login1.main()

    def testExpenses(self, driver):
        time.sleep(10)

        select_goal = driver.find_element_by_link_text("Goal1").click()
        time.sleep(3)
        print("Select Goal")

        select_expense = driver.find_element_by_xpath("//*[@id='tab-dashboardTable-1']/table/tbody/tr/td/div/table/tbody/tr[2]/td[3]").click()
        time.sleep(3)
        print("Select Expense")

        edit_expense = driver.find_element_by_css_selector("button.btn.btn-skyBlue").click()
        time.sleep(5)
        print("Click edit expenses")

        continue1 = driver.find_element_by_xpath("//*[@id='editExpensesHead2']")
        continue1.click()
        time.sleep(3)

        # q1 = driver.find_element_by_xpath("//*[@id='editExpensesColl2']/div/div/div/div[1]/div[1]/label/input").click()
        # time.sleep(2)

        # q2 = driver.find_element_by_xpath("//*[@id='editExpensesColl2']/div/div/div/div[1]/div[2]/label/input").click()
        # time.sleep(3)

        # q3 = driver.find_element_by_xpath("//*[@id='editExpensesColl2']/div/div/div/div[1]/div[3]/label/input")
        # q3.click()
        # time.sleep(1)
        #
        # q4 = driver.find_element_by_xpath("//*[@id='editExpensesColl2']/div/div/div/div[1]/div[4]/label/input")
        # q4.click()
        # time.sleep(1)

        # Choose Goal
        assign_goal = driver.find_element_by_xpath("//*[@id='tab-addExpenses-1']/div/div[2]/label/input").click()
        time.sleep(4)
        print("Select abcde as new goal")

        # Choose Campaign


        campaign_link = driver.find_element_by_link_text("Campaigns").click()
        time.sleep(1)

        clear_selected_campaign = driver.find_element_by_xpath("//*[@id='tab-addExpenses-2']/button").click()
        time.sleep(1)

        campaign = driver.find_element_by_xpath("//*[@id='tab-addExpenses-2']/div[1]/div/label/input").click()
        time.sleep(1)
        print("Select campaign for the selected timeframe and goal")

        # Choose Program

        program_link = driver.find_element_by_link_text("Program").click()
        time.sleep(2)

        clear_selected_program = driver.find_element_by_xpath("//*[@id='tab-addExpenses-3']/button").click()
        time.sleep(2)

        program = driver.find_element_by_xpath("//*[@id='tab-addExpenses-3']/div[1]/div[2]/label/input").click()
        time.sleep(2)
        print("Select program for the selected timeframe, goal and campaign")

        finishBtn = driver.find_element_by_xpath("//*[@id='form-editExpenseDetail']/div[3]/button[1]").click()
        time.sleep(5)


        # Reset all

        select_goal = driver.find_element_by_link_text("Goal1").click()
        time.sleep(3)
        print("Select Goal")

        select_expense = driver.find_element_by_xpath(
            "//*[@id='tab-dashboardTable-1']/table/tbody/tr/td/div/table/tbody/tr").click()
        time.sleep(3)
        print("Select Expense")

        edit_expense = driver.find_element_by_xpath(
            "/html/body/modal-overlay/bs-modal-container/div/div/modal-content/div/div/div/div[2]/div[2]/button").click()
        time.sleep(5)
        print("Click edit expenses")

        continue1 = driver.find_element_by_xpath("//*[@id='editExpensesHead2']")
        continue1.click()
        time.sleep(10)

        # q1 = driver.find_element_by_xpath("//*[@id='editExpensesColl2']/div/div/div/div[1]/div[1]/label/input").click()
        # time.sleep(2)

        # q2 = driver.find_element_by_xpath("//*[@id='editExpensesColl2']/div/div/div/div[1]/div[2]/label/input").click()
        # time.sleep(3)

        # q3 = driver.find_element_by_xpath("//*[@id='editExpensesColl2']/div/div/div/div[1]/div[3]/label/input")
        # q3.click()
        # time.sleep(1)
        #
        # q4 = driver.find_element_by_xpath("//*[@id='editExpensesColl2']/div/div/div/div[1]/div[4]/label/input")
        # q4.click()
        # time.sleep(1)

        # Choose Goal
        assign_goal = driver.find_element_by_xpath("// *[ @ id = 'tab-addExpenses-1'] / div / div[1] / label / input").click()

        time.sleep(4)
        print("Select abcde as new goal")

        # Choose Campaign


        campaign_link = driver.find_element_by_link_text("Campaigns").click()
        time.sleep(2)

        clear_selected_campaign = driver.find_element_by_xpath("//*[@id='tab-addExpenses-2']/button").click()
        time.sleep(2)

        campaign = driver.find_element_by_xpath("//*[@id='tab-addExpenses-2']/div[1]/div/label/input").click()
        time.sleep(2)
        print("Select campaign for the selected timeframe and goal")

        # Choose Program

        program_link = driver.find_element_by_link_text("Program").click()
        time.sleep(2)

        clear_selected_program = driver.find_element_by_xpath("//*[@id='tab-addExpenses-3']/button").click()
        time.sleep(2)

        program = driver.find_element_by_xpath("//*[@id='tab-addExpenses-3']/div[1]/div[3]/label/input").click()
        time.sleep(2)
        print("Select program for the selected timeframe, goal and campaign")

        finishBtn = driver.find_element_by_xpath("//*[@id='form-editExpenseDetail']/div[3]/button[1]").click()
        time.sleep(5)

    def main(self):
        self.testExpenses(self.driver)

# We have to call this main method and here we are accessing it's own class methods
if __name__ == '__main__':
    expenses = EditExpenses()
    expenses.main()