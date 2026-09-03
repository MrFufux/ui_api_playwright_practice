from pages.base_page import BasePage

class CheckBox(BasePage):
    
    # constructor
    def __init__(self, page):
        super().__init__(page)
        
        
        # Locators
        self.check_box_option = self.page.get_by_role('main').get_by_role('link', name='Check Box')
        # Finds the label "Home", then looks at any earlier sibling <span> (same parent) 
        # and grabs the <input> nested inside it, no matter how deep
        self.home_option = self.page.locator("//label[text()='Home']/preceding-sibling::span//input")
        self.toggle_button = self.page.locator("div.flex.items-center.gap-2.py-1")

    
    # Methods 
    def click_check_box_option(self):
        self.click_element(self.check_box_option)
        
    def click_home_option(self):
        self.click_element(self.home_option)
        
    # Scopes to the row matching `label` (e.g. "Home", "Desktop") since every row shares
    # the same "Toggle" button name/role, then clicks that row's Toggle chevron.
    def  click_chevron_toggle(self, label: str):
        chevron_row = self.toggle_button.filter(has_text=label)
        chevron_row.get_by_role('button', label).click()
        
        
    