from selenium import webdriver
import pyscreenshot as screenshothelper
from Globals import GlobalConstants as Const


def check_login_webpage_functionality(_driver, _functionality="login"):
    if _driver is not None:
        username_ele = _driver.find_element_by_id('txtUserName')
        pwd = _driver.find_element_by_id('txtPassword')

        if username_ele:
            username_ele.clear()

        if pwd:
            pwd.clear()

        if _functionality == "login":
            username_ele.send_keys("system")
            pwd.send_keys('sagar')
        elif _functionality == "UsernameValidation":
            pwd.send_keys('sagar')
        elif _functionality == "PasswordValidation":
            username_ele.send_keys("system")
        else:
            return Const.NOT_SUPPORTED

        login_btn = _driver.find_element_by_id('btnLogin')
        if login_btn:
            login_btn.click()

        if _driver.current_url == "http://localhost/PigmyPlus/Welcome.aspx":
            return Const.PASS
        elif (_driver.find_element_by_id('ValidationSummary1')) is not None and _driver.current_url == "http://localhost/PigmyPlus/Login.aspx":
            error_msg = _driver.find_element_by_tag_name("div[id='ValidationSummary1'] ul li").text
            if error_msg == "Enter Password" and _functionality == "PasswordValidation":
                return Const.PASS
            elif error_msg == "Enter Your Username" and _functionality == "UsernameValidation":
                return Const.PASS
            else:
                print(f"Unexpected Error found on {_driver.current_url}")
                image = screenshothelper.grab()
                image.save("Unexpected Error")
                return Const.FAIL
        else:
            return Const.FAIL
    else:
        print("Selenium Web Driver not instantiated")
        return Const.UNKNOWN_ERROR


def print_step_result(step, result):
    if result == Const.PASS:
        print(f"Step: '{step}' successfully completed, Result: PASS")
    elif result == Const.FAIL:
        print(f"Step: '{step}' FAILED, kindly check logs for more details, Result: FAIL")
    else:
        print(f"Unexpected Error found at Step: '{step}', check logs for more details, Result: FAIL")


if __name__ == '__main__':
    chromedriver = webdriver.Chrome()
    chromedriver.get("http://localhost/PigmyPlus/Login.aspx")

    result_info = check_login_webpage_functionality(chromedriver, 'UsernameValidation')
    print_step_result("Username Validation", result_info)

    result_info = check_login_webpage_functionality(chromedriver, 'PasswordValidation')
    print_step_result("Password Validation", result_info)

    result_info = check_login_webpage_functionality(chromedriver)
    print_step_result("Successfull Login", result_info)

    chromedriver.quit()
