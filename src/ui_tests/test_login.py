import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Initialize the WebDriver
driver = webdriver.Chrome()  # Ensure you have ChromeDriver installed and in your PATH

# URL of the login page
url = "http://localhost:5173/learning-github-action/"

# Test data
valid_username = "webdriver"
valid_password = "webdriver123"
invalid_username = "invalid_user"
invalid_password = "invalid_password"

def login(username, password):
    driver.get(url)
    
    # Find the username, password input fields, and login button
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "submit-button")
    
    # Enter username and password
    username_field.send_keys(username)
    password_field.send_keys(password)
    
    # Click the login button
    login_button.click()
    
    # Wait for the alert to appear
    time.sleep(2)  # Adjust sleep time if necessary, or use WebDriverWait

def test_valid_login():
    login(valid_username, valid_password)
    
    # Handle alert for valid login
    try:
        alert_message = driver.find_element(By.ID, "alert-dialog-description").text
        alert_button = driver.find_element(By.ID, "alert-close-button")
        assert "PASSED" in alert_message
        alert_button.click()
        print("Valid login test passed")
    except Exception as e:
        print("Valid login test failed:", e)

def test_invalid_login():
    login(invalid_username, invalid_password)
    
    # Handle alert for invalid login
    try:
        alert_message = driver.find_element(By.ID, "alert-dialog-description").text
        alert_button = driver.find_element(By.ID, "alert-close-button")
        assert "FAILED" in alert_message
        alert_button.click()
        print("Invalid login test passed")
    except Exception as e:
        print("Invalid login test failed:", e)

# Run tests
test_valid_login()
test_invalid_login()

# Close the WebDriver
driver.quit()