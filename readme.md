# Attendence Automation

This project is designed to automate the process of marking attendance on Moodle for multiple users. By using Selenium, a powerful tool for controlling web browsers through programs, this script efficiently logs into Moodle and marks attendance by entering a provided code simultaneously using Threading. This is a ideal solution for students who wish to mark multiple user attendence at once on Moodel (LMS).

## Features

1. **Automatic login**: It login into Moodel automatically.
2. **Multi-user Support**: Capable of handling multiple accounts.
3. **Concurrent Attendance Marking**: Utilizes threading to handle multiple Moodle accounts at once.

## Prerequisites

1. **python3**
2. **Selenium WebDriver**: `pip install selenium` in the attendence-automation repository
3. **ChromeDriver**: Download from [here](https://googlechromelabs.github.io/chrome-for-testing/) according to you system, now extract and place the chromedriver.exe file in the root (attendence-automation) folder.

## Configuration

1. **Credentials**: Provide Moodle usernames and passwords for all users.

```
users = [
    {"moodle_mail" : "", "moodle_pass" : ""}, # user 1
    {"moodle_mail" : "", "moodle_pass" : ""} # user 2
]
```

2. **Page Link** : Provide moodel links if **outside thapar**.

   Example:

   1. Login page `driver.get("https://lms.thapar.edu/moodle/login/")`
   2. Attendence page `url = "https://lms.thapar.edu/moodle/mod/attendance/view.php?id=" + sub_id` you can also omit sub_id.

3. **Attendance Code**: Provide the attendance code in the script as needed.

## Files:

1. single_user.py
2. multiuser.py
3. file.py

## Execution

`python3 file.py "CG"`
Provide moodel code in terminal now
