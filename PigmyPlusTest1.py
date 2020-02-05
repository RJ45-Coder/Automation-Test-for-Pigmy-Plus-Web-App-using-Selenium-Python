from selenium import webdriver

chromedriver = webdriver.Chrome()
chromedriver.get("http://localhost/PigmyPlus/Login.aspx")

username_ele = chromedriver.find_element_by_id('txtUserName')
if username_ele:
    username_ele.clear()
    username_ele.send_keys("system")

pwd = chromedriver.find_element_by_id('txtPassword')
if pwd:
    pwd.clear()
    pwd.send_keys('sagar')

login_btn = chromedriver.find_element_by_id('btnLogin')
if login_btn:
    login_btn.click()

if chromedriver.current_url == "http://localhost/PigmyPlus/Welcome.aspx":
    print("Test case PASS")
else:
    print("Test case FAILED")

chromedriver.quit()
