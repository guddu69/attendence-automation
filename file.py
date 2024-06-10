import sys
import threading
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# event = to pause all threads at a specific point until the code is entered and then continue execution

def toc(driver, event):
    # Wait for the event to be set before continuing
    event.wait()
    
    # find submit attendanc button and click
    submit_attendance_btn = driver.find_element("xpath", "//*[contains(text(), 'Submit')]")
    att_link = submit_attendance_btn.get_attribute("href")
    driver.get(att_link)
    
    status_btn = driver.find_element("xpath", "//input[@type='radio']")
    status_btn.click()
    # enter code and click
    code_ip = driver.find_element("name", "studentpassword")
    code_ip.send_keys(moodle_code)
    
    driver.find_element("id", "id_submitbutton").click()

def perform(moodle_mail, moodle_pass, sub_id, event):
    
    driver = webdriver.Chrome()
    # PASTE YOUR LOGIN LINK HERE
    driver.get("https://lms.thapar.edu/moodle/login/")
    
    # LOGIN
    username_ip = driver.find_element("name", "username")
    username_ip.send_keys(moodle_mail)
    
    pass_ip = driver.find_element("name", "password")
    pass_ip.send_keys(moodle_pass)
    
    login_btn = driver.find_element("xpath", '//*[@id="loginbtn"]')
    login_btn.click()
    
    # Define attendence page link
    url = "https://lms.thapar.edu/moodle/mod/attendance/view.php?id=" + sub_id
    driver.get(url)

    if sub_id == "126734":
        # if it contains a button to go to another page
        toc(driver, event)
    else:
        # Now all threads wait till code is entered
        event.wait()
        # enter pass and click
        code_ip = driver.find_element("name", "qrpass")
        code_ip.send_keys(moodle_code)
        sub_btn = driver.find_element("xpath", "//input[@type='submit' and @class='btn btn-secondary']")
        sub_btn.click()

    driver.quit()

def subjects(moodle_mail, moodle_pass, event):
    # you can modify this section
    # These are subjects and their codes for attedence page
    sub = {
        "CG": "126662",
        "QC": "126275",
        "TOC": "126734",
        "PA": "122704",
        "PAL": "126144", 
        "ADS": "126669" 
    }
    sub_id = sub[sub_name]
    perform(moodle_mail, moodle_pass, sub_id, event)

# ADD USERS HERE
users = [
    {"moodle_mail" : "", "moodle_pass" : ""}, # user 1
    {"moodle_mail" : "", "moodle_pass" : ""} # user 2
]

# Initialize the event
event = threading.Event()

# Input from user
sub_name = sys.argv[1]

# Create threads
threads = []
for user in users:
    thread = threading.Thread(target=subjects, args=(user["moodle_mail"], user["moodle_pass"], event))
    threads.append(thread)
    thread.start()

# Wait for user to enter the attendance code
moodle_code = input("Enter the attendance code: ")
event.set()  # Allow all threads to continue

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("All attendance marked.")
