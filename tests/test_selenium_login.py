import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage


@pytest.fixture
def driver():
    """
    Setup: Initializes the Chrome browser with WebDriver Manager.
    Teardown: Safely closes the browser after the test ends.
    """
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


def test_user_authentication_flow(driver):
    """Verify valid user can login and
        reach dashboard successfully."""
    driver.get("https://opensource-demo.orangehrmlive.com/")

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.NAME, "username")))

    login_page = LoginPage(driver)
    login_page.execute_login("Admin", "admin123")

    WebDriverWait(driver, 20).until(
        EC.url_contains("dashboard"))

    assert "dashboard" in driver.current_url
    print("Login passed!")


def test_invalid_login(driver):
    """Verify invalid credentials keep
        user on login page."""
    driver.get("https://opensource-demo.orangehrmlive.com/")

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.NAME, "username")))

    login_page = LoginPage(driver)
    login_page.execute_login("wronguser", "wrongpass")

    assert "dashboard" not in driver.current_url
    print("Invalid login test passed!")


@pytest.mark.parametrize("username, password, expected", [
    ("Admin", "admin123", True),
    ("wronguser", "wrongpass", False),
])
def test_login_parametrize(driver, username, password, expected):
    """Verify login with multiple data sets —
        valid and invalid credentials."""
    driver.get("https://opensource-demo.orangehrmlive.com/")
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.NAME, "username")))

    login_page = LoginPage(driver)
    login_page.execute_login(username, password)

    if expected:
        assert "dashboard" in driver.current_url
    else:
        assert "dashboard" not in driver.current_url
    print(f"Test passed for {username}!")


def test_locators(driver):
    """Demonstrate all locator types —
        NAME, XPATH, CSS_SELECTOR."""
    driver.get(
        "https://opensource-demo.orangehrmlive.com/")
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.NAME, "username")))

    driver.find_element(
        By.NAME, "username").send_keys("Admin")

    driver.find_element(
        By.XPATH,
        "//input[@name='password']").send_keys("admin123")

    driver.find_element(
        By.CSS_SELECTOR,
        "button[type='submit']").click()

    assert "dashboard" in driver.current_url
    print("Locators test passed!")