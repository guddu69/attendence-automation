# Attendence Automation

This project is designed to automate the process of marking attendance on Moodle for multiple users. By using Selenium, a powerful tool for controlling web browsers through programs, this script efficiently logs into Moodle and marks attendance by entering a provided code simultaneously using Threading. This is a ideal solution for students who wish to mark multiple user attendence at once on Moodel (LMS).

There are three files, run any one according to the need.

## Features

1. **Automatic login**: It logs in into Moodel automatically.
2. **Multi-user Support**: Capable of handling multiple accounts.
3. **Concurrent Attendance Marking**: Utilizes threading to handle multiple Moodle accounts at once.

## Prerequisites

1. **python3**
2. **Selenium WebDriver**: `pip install selenium` in the attendence-automation repository (Try using pip3 is pip command does not work).
3. **ChromeDriver**: Download from [here](https://googlechromelabs.github.io/chrome-for-testing/) according to your system, now extract and place the chromedriver.exe file in the root (attendence-automation) folder.

## Configuration

1. **Credentials**: Provide Moodle usernames and passwords for all users.

```
users = [
    {"moodle_mail" : "", "moodle_pass" : ""}, # user 1
    {"moodle_mail" : "", "moodle_pass" : ""} # user 2
]
```

2.  **Page Link** : Provide moodel links if **outside thapar**.

    Example:

    1. Login page: `driver.get("https://lms.thapar.edu/moodle/login/")`
    2. Attendence page:

       1. In file.py or multi_user.py: `url = "https://lms.thapar.edu/moodle/mod/attendance/view.php?id=" + sub_id` you can also omit sub_id.

       2. In single_user.py: `url = "https://lms.thapar.edu/moodle/mod/attendance/view.php?id=126275"`

3.  **Attendance Code**: Provide the attendance code in the script as needed.

    Example if code is `1234` then:

    1. **file.py**: Enter code in terminal after running the script as `python3 file.py "CG"`

    2. **single_user**: `python3 single_user.py "1234"`
    3. **multi_user.py**: `python3 multi_user.py "CG" "1234"`
