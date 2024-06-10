# Import webdriver module from selenium
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Create new driver object (change the file name based on your OS)
service = Service(executable_path='./chromedriver.exe')
driver = webdriver.Chrome()

# PASTE YOUR LOGIN LINK HERE
driver.get("https://lms.thapar.edu/moodle/login/")

# Define Moodle email and password
moodle_mail = ""
moodle_pass = ""
moodle_code = sys.argv[1]

# Login:
# Find the field element and send the input keys to the element
username_ip = driver.find_element("name", "username")
username_ip.send_keys(moodle_mail)
pass_ip = driver.find_element("name","password")
pass_ip.send_keys(moodle_pass)
# Find the login button using XPATH and click it
login_btn = driver.find_element("xpath",'//*[@id="loginbtn"]')
login_btn.click()

# ATTENDENCE PAGE URL
url = "https://lms.thapar.edu/moodle/mod/attendance/view.php?id=126275"
driver.get(url)

# time.sleep(6) # for testing

# Mark attendence
code_ip = driver.find_element("name","Enter")
code_ip.send_keys(moodle_code)
# find and click on submit button
sub_btn = driver.find_element("xpath", "//*[contains(text(), 'Submit')]")
sub_btn.click()

driver.quit() # close the drivers to release allocated resources