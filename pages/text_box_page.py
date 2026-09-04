from pages.base_page import BasePage


class TextBoxPage(BasePage):
    
    # Constructor
    # Rewrites the basepage constructor
    # Let the locators and methods works
    def __init__(self, page):
        super().__init__(page)
        
        # Locators (instance variables)
    
        # Text Box option
        self.text_box_option = self.page.get_by_role('main').get_by_role('link', name='Text Box')
        self.submit_button = self.page.get_by_role('button', name='Submit')
        self.full_name = self.page.get_by_role('textbox', name='Full Name')
        self.email = self.page.get_by_role('textbox', name='Email')
        self.current_address = self.page.get_by_role('textbox', name='Current Address')
        self.permanent_address = self.page.get_by_role('textbox', name='Permanent Address')
        self.output = self.page.locator('#output')


    # Actions (Methods)

    def click_text_box_option(self):
        self.click_element(self.text_box_option)

    def fill_full_name(self, text):
        self.fill_text(self.full_name, text)

    def fill_email(self, text):
        self.fill_text(self.email, text)

    def fill_current_address(self, text):
        self.fill_text(self.current_address, text)

    def fill_permanent_address(self, text):
        self.fill_text(self.permanent_address, text)

    def click_submit_button(self):
        self.click_element(self.submit_button)