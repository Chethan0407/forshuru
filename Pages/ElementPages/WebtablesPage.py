import time
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Utilities.TestData.ElementsTestData.FomTestData import WebtableData


class WebtablesPage(BasePage):
    WebTables_cta = (By.XPATH, "//span[normalize-space() = 'Web Tables'] ")
    Add_button = (By.XPATH, "//button[@id = 'addNewRecordButton']")
    First_name_field = (By.XPATH, "//input[@id = 'firstName']")
    Last_name_field = (By.XPATH, "//input[@id = 'lastName']")
    Email_field = (By.XPATH, "//input[@id = 'userEmail']")
    Age_field = (By.XPATH, "//input[@id = 'age']")
    Salary_field = (By.XPATH, "//input[@id = 'salary']")
    Department_field = (By.XPATH, "//input[@id = 'department']")
    Submit_button_field = (By.XPATH, "//button[@id = 'submit']")
    Edit_Record = (By.XPATH, "//span[@id='edit-record-1']//*[name()='svg']")
    Delete_record = (By.XPATH, "//span[@id='delete-record-1']//*[name()='svg']")

    def web_table_page(self):
        self.scroll_to_and_click(self.WebTables_cta)
        self.scroll_to_and_click(self.Add_button)
        self.send_keys(self.First_name_field, WebtableData.First_name)
        self.send_keys(self.Last_name_field, WebtableData.Second_name)
        self.send_keys(self.Email_field, WebtableData.Email)
        self.send_keys(self.Age_field, WebtableData.Age)
        self.send_keys(self.Salary_field, WebtableData.Salary)
        self.send_keys(self.Department_field, WebtableData.Department)
        self.scroll_to_and_click(self.Submit_button_field)

    def web_table_edit(self):
        self.scroll_to_and_click(self.WebTables_cta)
        self.scroll_to_and_click(self.Edit_Record)
        self.clear(self.First_name_field)
        self.send_keys(self.First_name_field, WebtableData.First_name)
        self.clear(self.Last_name_field)
        self.send_keys(self.Last_name_field, WebtableData.Second_name)
        self.clear(self.Email_field)
        self.send_keys(self.Email_field, WebtableData.Email)
        self.clear(self.Age_field)
        self.send_keys(self.Age_field, WebtableData.Age)
        self.clear(self.Salary_field)
        self.send_keys(self.Salary_field, WebtableData.Salary)
        self.clear(self.Department_field)
        self.send_keys(self.Department_field, WebtableData.Department)
        self.scroll_to_and_click(self.Submit_button_field)


    def delete_record(self):
        self.click(self.Delete_record)







