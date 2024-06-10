import sys
import threading
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By # driver.find_element(By.name, "NAME")

# for cources which has additional present and absent fields
def toc(driver, moodle_code):

    submit_attendance_btn = driver.find_element("xpath","//*[contains(text(), 'Submit')]")

    # visit the link (HTML "href" attribute) specified by the button
    att_link = submit_attendance_btn.get_attribute("href")
    driver.get(att_link) # opens the page contaning present and absent buttons
    
    # Find the fist attendance status radio button, ie, the one corresponding to "Present" (left most)
    status_btn = driver.find_element("xpath","//input[@type='radio']")
    status_btn.click() # click present button

    # fill out the code in "enter password" column
    code_ip = driver.find_element("name","studentpassword")
    code_ip.send_keys(moodle_code)
    
    # click the save changes button to mark attendance
    driver.find_element("id","id_submitbutton").click()


def perform(moodle_mail, moodle_pass, sub_id):

    driver = webdriver.Chrome() # load new driver for each user

    # LOG IN 
    driver.get("https://lms.thapar.edu/moodle/login/") # website
    # Enter username
    username_ip = driver.find_element("name", "username")
    username_ip.send_keys(moodle_mail)
    # Enter password
    pass_ip = driver.find_element("name","password")
    pass_ip.send_keys(moodle_pass)
    # click login button
    login_btn = driver.find_element("xpath",'//*[@id="loginbtn"]')
    login_btn.click()

    # specify attandance urls
    url = "https://lms.thapar.edu/moodle/mod/attendance/view.php?id=" + sub_id
    driver.get(url)

    # MARK ATTENDANCE
    if(sub_id == "126734"):
        toc(driver, moodle_code)
    else:
        # enter code
        code_ip = driver.find_element("name","qrpass")
        code_ip.send_keys(moodle_code)
        # click the submit button
        sub_btn = driver.find_element("xpath","//input[@type='submit' and @class='btn btn-secondary']")
        sub_btn.click()

    # time.sleep(3) # rough wait (to check if attendance is marked) you can delete this wait
    driver.quit() # Close the drivers to release allocated resources

def subjects(moodle_mail, moodle_pass):
    sub = {
        "CG" : "126662",
        "QC" : "126275",
        "TOC" : "126734",
        "PA" : "122704",
        "PAL" : "126144",
        "ADS" : "126669"
    }
    sub_id = sub.get(sub_name)
    perform(moodle_mail, moodle_pass, sub_id)


# for uploading path of chrome driver (in this case it is in same Repo as this file)
service = Service(executable_path = './chromedriver.exe')

# Input from user
sub_name = sys.argv[1] # subject code
moodle_code = sys.argv[2] # the code for attendance (input from user)

# Specify the USERS and their PASSWORDS
users = [
    {"moodle_mail" : "", "moodle_pass" : ""}, # user 1
    {"moodle_mail" : "", "moodle_pass" : ""} # user 2
]

# Threading for Parallel processing 
threads = []
for user in users:
    thread = threading.Thread(target = subjects, args = (user["moodle_mail"], user["moodle_pass"]))
    threads.append(thread)
    thread.start() # start the execution of threads

# Wait for all threads to finish untill then blocks main program
for thread in threads:
    thread.join()