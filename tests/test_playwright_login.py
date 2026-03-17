import pytest
from playwright.sync_api import sync_playwright
from pages.pw_login_page import PlaywrightLoginPage

@pytest.fixture
def page():
    """Setup browser and teardown after test!"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()

def test_login(page):
    """Verify valid user can login successfully!"""
    page.goto(
    "https://opensource-demo.orangehrmlive.com/")
    login = PlaywrightLoginPage(page)
    login.login("Admin", "admin123")
    page.wait_for_url("**/dashboard**")
    assert "dashboard" in page.url

def test_invalid_login(page):
    """Verify invalid credentials stay on login page!"""
    page.goto(
    "https://opensource-demo.orangehrmlive.com/")
    login = PlaywrightLoginPage(page)
    login.login("wronguser", "wrongpass")
    assert "dashboard" not in page.url

@pytest.mark.parametrize(
    "username,password,expected",[
    ("Admin", "admin123", True),
    ("wronguser", "wrongpass", False),
])
def test_login_parametrize(page,
                username, password, expected):
    """Verify login with multiple data sets!"""
    page.goto(
    "https://opensource-demo.orangehrmlive.com/")
    login = PlaywrightLoginPage(page)
    login.login(username, password)
    if expected:
        page.wait_for_url("**/dashboard**")
        assert "dashboard" in page.url
    else:
        assert "dashboard" not in page.url