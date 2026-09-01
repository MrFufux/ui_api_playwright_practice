from playwright.sync_api import Page
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    
    # Constructor
    # Rewrites the basepage constructor
    # Let the locators and methods works
    def __init__(self, page):
        super().__init__(page)
        
        # Locators (instance variables)
    
        # Text Box option
        self.text_box_option = self.page.get_by_role('link', name='Text Box')
        self.submit_button = self.page.get_by_role('button', name='Submit')
        self.full_name = self.page.get_by_role('textbox', name='Full Name')
        
        
        
    # Actions (Methods)
    
    def click_text_box_option(self):
        self.click_element(self.text_box_option)
        
    def fill_full_name(self):
        self.fill_text()
        
    def fill_email(self):
        self.fill_text()
        
    def fill_current_address(self):
        self.fill_text()
        
    def fill_permanent_address(self):
        self.fill_text()
        
    def click_submit_button(self):
        self.click_element(self.submit_button)