# Parent my class
# OOP principles: Inheritance, Abstraction, Encapsulation, Polymorphism
from playwright.sync_api import Page, Locator

# Parent Class for all Page objects
# encapsulation
class BasePage:
    
    # The constructor
    # Automatically runs whenever a new page object is created
    def __init__(self, page: Page):
        # Page object into the constructor
        # Saved as an instance variable (self.page = page)
        # Every method inside this class now has control of the browser tab
        self.page = page
        
        
    # Reusable custom click method
    # Accepts raw locatores(css, xpath) or playwright locators
    def click_element(self, locator: str | Locator, action_timeout: int = 5000):
        # Ternary operator: one line if else
        # Polymorphism => Method overloading
        # isintance: it's a type checking
        
        # if instance(locator, str) -> verifies if locator is a str
        # if True -> assumes that is a locator(css,xpath as text) and transform it
        # into a playwright locator  with self.page.locator(locator)
        # if False -> Assumes locator is an Locator object from playwright and leaves it.
        element = self.page.locator(locator) if isinstance(locator, str) else locator
        
        # click action applying the defined custom timeout
        element.click(timeout=action_timeout)
        
        
    # Reusable custom wait method
    # waits for a specific UI state without performing any action
    # useful for cases where Playwright's auto-wait doesn't apply (e.g. screenshots, assertions)
    def wait_for_element_visible(self, locator: str | Locator, action_timeout: int = 10000):
        # Ternary operator: one line if else
        # if isintance(locator, str) -> verifies is a str
        # if True -> assumes that is a locator(css, xpath as text) and transform it 
        # into a playwright locator with the self.page.locator(locator)
        # if False -> assumes locator is an Locator object from playwrigth and leaves it 
        element = self.page.locator(locator) if isinstance(locator, str) else locator
        
        # wait_for() 
        element.wait_for(state='visible', timeout=action_timeout)
        
    # Reusable custom fill text method
    def fill_text(self, locator: str | Locator, text: str, action_timeout: int = 5000):
        
        element = self.page.locator(locator) if isinstance(locator, str) else locator
        
        # .fill() automatically waits for the element to be visible, enabled and editable
        element.fill(text, timeout=action_timeout)
        
    # Custom navigation method
    # Navigates to a specific path using the base_url in conftest.py
    # path = '' : the path is optional, if not path => empty string
    def navigate(self, path = ''):
        self.page.goto(path)
        
        
            