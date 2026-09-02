import pytest
from playwright.sync_api import Page, expect
from pages.text_box_page import TextBoxPage


@pytest.mark.ui
def test_text_box_creation(ui_page: Page):
    # Using the AAA approach Arrange - Act - Assert
    
    # 1. Arrange: Setup the page object
    home_page = TextBoxPage(ui_page)
    
    # 2. Act: Perform the actions
    home_page.click_text_box_option()
    home_page.fill_full_name('Hollywood')
    home_page.fill_email('xxdd@test.com')
    home_page.fill_current_address('av 40 # 67-19')
    home_page.fill_permanent_address('av 43 # 56-77')
    home_page.click_submit_button()
    
    # 3. Assert: Verifies the expected outcomes
    expect(home_page.output).to_contain_text('Name: Hollywood')
    expect(home_page.output).to_contain_text('Email: xxdd@test.com')
    expect(home_page.output).to_contain_text('Current Address : av 40 # 67-19')
    expect(home_page.output).to_contain_text('Permanent Address : av 43 # 56-77')