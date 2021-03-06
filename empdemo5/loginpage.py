
import unittest


from selenium import webdriver
import time

from selenium.webdriver.support.select import Select

from empdemo5 import commons
from empdemo5.basetest import BaseTest
from selenium.webdriver.common.action_chains import ActionChains


class MyTest(BaseTest):  # Create a class which is a childclass of unittest.testcase

    def setUp(self):
        BaseTest.setUp(self)
        self.driver.get(commons.app_url)
        time.sleep(5)
        self.assertEqual("Welcome to Employee Application", self.driver.title, "invalid title for login.html")

    # 1.test with valid username and password
    def testLogintoAppbyvalidCreds(self):
        # enter login name
        self.login("admin", "admin")
        time.sleep(3)
        self.assertEqual("Employee Profile", self.driver.title, "invalid title for home page")
        self.checkHeaderlinks()
        time.sleep(5)

    # 2.test with valid username and invalid password
    def testLogintoAppbyInvalidCreds(self):
        self.login("admin", "admin1")
        time.sleep(3)
        self.assertEqual("Employee Application", self.driver.title, "invalid title for login.html")

        errorObj = self.findbyxpath("//font[@color='Red']")
        self.assertTrue(errorObj.is_enabled())
        self.assertTrue(errorObj.is_displayed())
        self.assertEqual("Invalid Login.", errorObj.text, "invalid error msg")

        time.sleep(5)


    #below methods are not tested

    def testLoginWithEmptyUserName(self): #negative test case
        self.findbyname("loginName")
        self.findbyname("password").send_keys("admin")
        self.findbyxpath("//input[@value='Login']").click()
        alertObj = self.driver.switch_to.alert  # to get the alert obj
        msg = alertObj.text  # to get the alert msg
        self.assertEqual("Please provide loginName!", msg, "invalid msg for alert1")
        time.sleep(5)
        alertObj.accept()
        time.sleep(5)

    def testLoginWithEmptyPassword(self):
        self.findbyname("loginName").send_keys("admin")
        self.findbyname("password")
        self.findbyxpath("//input[@value='Login']").click()
        alertObj = self.driver.switch_to.alert  # to get the alert obj
        msg = alertObj.text  # to get the alert msg
        self.assertEqual("Please provide Password!", msg, "invalid msg for alert1")
        time.sleep(5)
        alertObj.accept()
        time.sleep(5)
    def testLoginWithEmptyUnameAndPassword(self):
        self.findbyname("loginName")
        self.findbyname("password")
        self.findbyxpath("//input[@value='Login']").click()
        alertObj = self.driver.switch_to.alert  # to get the alert obj
        msg = alertObj.text  # to get the alert msg
        self.assertEqual("Please provide loginName!", msg, "invalid msg for alert1")
        time.sleep(5)
        alertObj.accept()
        time.sleep(5)
    def testValiUsernameAndWrongpassword(self):
        self.findbyname("loginName").send_keys("admin")
        self.findbyname("password").send_keys("mahetha")
        self.findbyxpath("//input[@value='Login']").click()
        time.sleep(5)
    def testInvalidUser(self):
        self.findbyname("loginName").send_keys("user1")
        self.findbyname("password").send_keys("user2")
        self.findbyxpath("//input[@value='Login']").click()
        time.sleep(5)

    def testLoginAdmin(self):
        self.findbyname("loginName").send_keys("admin")

        self.findbyname("password").send_keys("admin")
        self.findbyxpath("//input[@value='Login']").click()
        self.assertEqual("Employee Profile", self.driver.title, "invalid title for login.html")  # validate title
        time.sleep(5)
        self.driver.find_element_by_link_text("My Profile")
        empobj = self.findbyid("EmployeeLbl")
        action = ActionChains(self.driver)
        action.move_to_element(empobj).perform()
        self.driver.find_element_by_link_text("Add New Employee")
        self.driver.find_element_by_link_text("Change Password")
        self.driver.find_element_by_link_text("Advance Search")
        self.driver.find_element_by_link_text("Show All Employees")
        self.driver.find_element_by_link_text("My Subordinates")
        DepartmentLblobj = self.findbyid("DepartmentLbl")
        action = ActionChains(self.driver)
        action.move_to_element(DepartmentLblobj).perform()
        self.driver.find_element_by_link_text("Add New Department")
        self.driver.find_element_by_link_text("Search Department")
        self.driver.find_element_by_link_text("Show All Departments")
        self.driver.find_element_by_link_text("Logout")
        time.sleep(5)

















