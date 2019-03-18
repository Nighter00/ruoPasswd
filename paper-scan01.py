import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def login(login_strLoginName, login_strPassword):
    # firefox = "C:\Program Files (x86)/firefox/firefox.exe"
    login_url = 'url'
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument('--headless')
    # browser = webdriver.firefox(executable_path=firefox, firefox_options=firefox_options)

    browser = webdriver.Firefox(firefox_options=firefox_options)
    browser.get(login_url)
    # name_input = browser.find_element_by_tag_name('login_strLoginName')
    name_input = browser.find_element_by_xpath("//input[@name='login_strLoginName']")
    # pass_input = browser.find_element_by_tag_name('login_strPassword')
    pass_input = browser.find_element_by_xpath("//input[@name='login_strPassword']")
    login_button = browser.find_element_by_xpath("//table[@id='login']/tbody[1]/tr[4]/td/input")

    name_input.clear()
    name_input.send_keys(login_strLoginName)
    time.sleep(0.5)
    pass_input.clear()
    pass_input.send_keys(login_strPassword)
    time.sleep(0.5)
    login_button.click()

    # time.sleep(0.5)
    # print(browser.get_cookies())

    time.sleep(0.5)
    # print(browser.page_source)
    l_p = len(browser.page_source)
    if (l_p < 2000):
        print(login_strLoginName)
    browser.quit()


login_strPassword = ''

stu_num = []
for i in range(0, 100):
    stu_num.append('num' + i)

for i in range(0, 100):
    login(stu_num[i], login_strPassword)
