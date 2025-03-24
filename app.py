from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from dotenv import load_dotenv
import time
import os

# Load environment variables from .env file (make sure to have EMAIL and PASSWORD stored in it)
load_dotenv()

# Initialize the Firefox browser instance
browser = webdriver.Firefox()

# Step 1: Open LinkedIn login page
browser.get('https://www.linkedin.com/login')
time.sleep(2)  # Wait for the page to load completely

# Step 2: Locate email and password input fields and log in
email_field = browser.find_element(By.ID, 'username')
password_field = browser.find_element(By.ID, 'password')
email_field.send_keys(os.getenv('EMAIL'))  # Input email from environment variable
password_field.send_keys(os.getenv('PASSWORD'))  # Input password from environment variable
password_field.send_keys(Keys.RETURN)  # Simulate pressing Enter to log in

# Wait for login process to complete and dashboard to load
time.sleep(5)

# Step 3: Navigate to the LinkedIn Connections page
browser.get('https://www.linkedin.com/mynetwork/invite-connect/connections/')
time.sleep(5)  # Wait for connections page to load

# Initialize counter to track the number of connections removed
COUNTER = 0

# Start loop to remove connections one by one
while True:
    try:
        # Step 4: Locate and click the "More" button on each connection card to open options
        more_button = browser.find_element(By.XPATH, "//button[@data-view-name='connections-remove-connection-dropdown']")
        more_button.click()
        time.sleep(1)  # Small delay to allow dropdown to appear
        
        # Step 5: Select "Remove Connection" option from the dropdown
        remove_button = browser.find_element(By.XPATH, "//p[text()='Remove connection']")
        remove_button.click()
        time.sleep(2)  # Small delay for the confirmation dialog to appear
        
        # Step 6: Confirm the removal of the connection
        confirm_button = browser.find_element(By.XPATH, "//button[@data-view-name='connections-remove']")
        confirm_button.click()
        
        # Update the counter and print the count of removed connections
        COUNTER += 1
        print("Removed connection count: " + str(COUNTER))
        time.sleep(3)  # Delay to mimic human interaction speed and avoid detection

    except NoSuchElementException:
        # Exit the loop if no more connections are found or elements are missing
        print("No more connections found or unable to locate elements.")
        break

# Close the browser session
browser.quit()
print("All connections removed.")
