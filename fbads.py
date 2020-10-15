from selenium import webdriver
#from selenium.webdriver.firefox import options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options, DesiredCapabilities
import time
import os
import zipfile
import requests
namestr = 'Testings'#input('Введите название страницы: ')
#mla_profile_id = '7c0abfab-e230-465d-a9ab-18c5b343e902'
ask = requests.get('http://rev.click/api/task/server/vasya').json()
print(ask)
task_id = ask['task']
mla_profile_id = ask['uuid']
card = ask['card']
mla_url = 'http://127.0.0.1:45000/api/v1/profile/start?automation=true&profileId='+mla_profile_id

def send_log(task_id, message):
    url = 'http://rev.click/api/task/' + str(task_id) + '/progress'
    #print(url)
    data = {
        'message': message
    }
    requests.post(url=url, data=data)
"""
Send GET request to start the browser profile by profileId. Returns response in the following format: '{"status":"OK","value":"http://127.0.0.1:XXXXX"}', where XXXXX is the localhost port on which browser profile is launched. Please make sure that you have Multilogin listening port set to 35000. Otherwise please change the port value in the url string
"""
resp = requests.get(mla_url)
status = False
json = resp.json()
if str(json['status']) == 'ERROR':
    print('OK')
    send_log(task_id=task_id, message='ERROR VALUE')
print(json)

#Define DesiredCapabilities
#opts = options.DesiredCapabilities()
#_browser_profile = webdriver.FirefoxProfile()
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.set_capability("dom.push.enabled", False)
#_browser_profile.set_preference("dom.webnotifications.enabled", False) #dom.webnotifications.enabled
capabilities = {
    "chromeOptions": {
        'args': ['--disable-notifications', '--lang=ru', '--window-size=1920,1080', '--window-position=0,0']}
}
"""options = webdriver.FirefoxOptions()
options.set_preference("dom.push.enabled", False)
options1 = webdriver.FirefoxOptions()
options1.add_argument('--disable-notifications')"""

#Instantiate the Remote Web Driver to connect to the browser profile launched by previous GET request
browser = webdriver.Remote(command_executor=json['value'],desired_capabilities=capabilities, options=chrome_options) #desired_capabilities={} browser_profile=_browser_profile
browser.get('https://www.fb.com/') #'http://127.0.0.1:33623'
time.sleep(4) #
try:
    WebDriverWait(browser, 30).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[1]/div[3]/div[1]/div[1]/form/div/div[1]/div/div/div[2]/p[1]')))
    send_log(task_id=task_id, message='Checkpoint')
except:
    print('All normal')
browser.get('https://www.facebook.com/pages')

try:
    WebDriverWait(browser, 30).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[1]/div[3]/div[1]/div[1]/form/div/div[1]/div/div/div[2]/p[1]')))
    send_log(task_id=task_id, message='Checkpoint')
except:
    print('All normal')
try:
    WebDriverWait(browser, 30).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div[1]/button')))
    but10 = browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[2]/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div[1]/button')
    but10.click()
except:
    print('All normal')
try:
    WebDriverWait(browser, 50).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[3]/div[2]/form/div[1]')))
    send_log(task_id=task_id, message='Without login')
except:
    print('All normal')
time.sleep(5)
send_log(task_id=task_id, message='Trying to create funpage')
try:
    WebDriverWait(browser, 30).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[1]/div[3]/div[1]/div[1]/form/div/div[1]/div/div/div[2]/p[1]')))
    send_log(task_id=task_id, message='Checkpoint')
    status = False
except:
    print('All normal')
try:
    WebDriverWait(browser, 30).until(EC.presence_of_element_located(
    (By.XPATH, '/html/body/div[1]/div[3]/div[1]/div/div[1]/div/div[1]/div/div/div/div[2]/ul/li/a/div/button')))
    beginbut = browser.find_element_by_xpath(
    '/html/body/div[1]/div[3]/div[1]/div/div[1]/div/div[1]/div/div/div/div[2]/ul/li/a/div/button')
    beginbut.click()
except:
    WebDriverWait(browser, 30).until(EC.presence_of_element_located(
    (By.XPATH, '/html/body/div[1]/div[3]/div[1]/div/div[1]/div/div[1]/div/div/div/div[2]/ul/li/a')))
    beginbut = browser.find_element_by_xpath(
    '/html/body/div[1]/div[3]/div[1]/div/div[1]/div/div[1]/div/div/div/div[2]/ul/li/a')
    browser.get(beginbut.get_attribute('href'))
try:
    WebDriverWait(browser, 60).until(EC.presence_of_element_located(
    (By.XPATH, '/html/body/div[1]/div[3]/div[1]/div/div[2]/div/div[2]/table/tbody/tr/td[1]/div/div[1]/div[2]/button')))
    beginbut2 = browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div/div[2]/table/tbody/tr/td[1]/div/div[1]/div[2]/button')
    beginbut2.click()
except:
    WebDriverWait(browser, 60).until(EC.presence_of_element_located(
    (By.XPATH, '/html/body/div[1]/div[3]/div[1]/div/div[2]/div/div[2]/table/tbody/tr/td[1]/div/div[1]/div[2]/button')))
    beginbut2 = browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div/div[2]/table/tbody/tr/td[1]/div/div[1]/div[2]/button')
    beginbut2.click()
try:
    WebDriverWait(browser, 30).until(EC.presence_of_element_located(
        (By.ID,
         'BUSINESS_SUPERCATEGORYPageNameInput"]')))
    pole1 = browser.find_element_by_id('BUSINESS_SUPERCATEGORYPageNameInput')
    pole1.send_keys(namestr)
    time.sleep(3)
except:
    WebDriverWait(browser, 30).until(EC.presence_of_element_located(
        (By.XPATH,
         '//*[@id="BUSINESS_SUPERCATEGORYPageNameInput"]')))
    pole1 = browser.find_element_by_xpath('//*[@id="BUSINESS_SUPERCATEGORYPageNameInput"]')
    pole1.send_keys(namestr)#
    time.sleep(3)
try:
    pole2 = browser.find_element_by_xpath('//*[@id="js_a"]/input')
    pole2.send_keys('Не компанія')
except:
    pole2 = browser.find_element_by_xpath(
        '/html/body/div[1]/div[3]/div[1]/div/div[2]/div/div[2]/table/tbody/tr/td[1]/div/div[2]/div[3]/table/tbody/tr[2]/td/div/div[1]/div/span/span/label/input')  # //*[@id="js_b"]/input
    pole2.send_keys('Не компанія')
time.sleep(3)
ActionChains(browser).send_keys(Keys.ENTER).perform()
time.sleep(3)
adres1 = browser.find_element_by_xpath('//*[@id="pageAddress"]')
adres1.send_keys('Хрещатик,3')
time.sleep(4)
try:
    city1 = browser.find_element_by_xpath('//*[@id="js_g"]/input')
    city1.send_keys('Киев')
    time.sleep(3)
    ActionChains(browser).send_keys(Keys.ENTER).perform()
except:
    city1 = browser.find_element_by_xpath(
        '/html/body/div[1]/div[3]/div[1]/div/div[2]/div/div[2]/table/tbody/tr/td[1]/div/div[2]/div[2]/table[2]/tbody/tr[2]/td/table/tbody/tr/td[1]/div/span/span/label/input')
    city1.send_keys('Киев')
    time.sleep(3)
    ActionChains(browser).send_keys(Keys.ENTER).perform()
index = browser.find_element_by_xpath('//*[@id="pageZipCode"]')
index.send_keys('54003')
time.sleep(3)
check1 = browser.find_element_by_xpath(
    '//*[@id="content"]/div/div[2]/div/div[2]/table/tbody/tr/td[1]/div/div[2]/div[2]/div/label/button')
check1.click()
time.sleep(3)
but2 = browser.find_element_by_xpath(
    '//*[@id="content"]/div/div[2]/div/div[2]/table/tbody/tr/td[1]/div/div[2]/div[4]/button/div/div')
but2.click()
time.sleep(5)
try:
    WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type=file]')))
    send_log(task_id=task_id, message='Funpage created')
    status = True
    dali1 = browser.find_element_by_css_selector('input[type=file]')
    dali1.send_keys(r"D:\programs\facebookbm\new\112233.jpg")  # r"D:\programs\facebookbm\112233.jpg"
    time.sleep(10)
except:
    print('Первое фото не загрузилось')
    send_log(task_id=task_id, message='Cannot load first pic to funpage')
    status = False
try:
    WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type=file]')))
    dali2 = browser.find_element_by_css_selector('input[type=file]')
    dali2.send_keys(r"D:\programs\facebookbm\new\2211.jpg")  # r"D:\programs\facebookbm\2211.jpg"
    time.sleep(10)
except:
    print('Второе фото не загрузилось')
    send_log(task_id=task_id, message='Cannot load second pic to funpage')
    status = False
try:
    WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/div[1]/div/div[3]/div[2]/a')))
    dali3 = browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[3]/div[2]/a')
    dali3.click()
    time.sleep(5)
    WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="userNavigationLabel"]')))
    but3 = browser.find_element_by_xpath('//*[@id="userNavigationLabel"]')
    but3.click()
    time.sleep(5)
    el1 = browser.find_elements_by_class_name('_54nh')
    print(len(el1))
    for ss in el1:
        try:
            if ss.text == 'Реклама на Facebook':
                print(ss.text)
                ss.click()
                break
        except:
            continue
except:
    print('no')
time.sleep(10)

time.sleep(10)
browser.get(
    'https://www.facebook.com/micro_site/url/?click_from_context_menu=true&country=UA&destination=https%3A%2F%2Fwww.facebook.com%2Fads%2Fmanager%2Faccount_settings%2Faccount_billing&event_type=click&last_nav_impression_id=0M90XBWjzEGeXVkd3&max_percent_page_viewed=46&max_viewport_height_px=657&max_viewport_width_px=1366&orig_http_referrer=https%3A%2F%2Fwww.google.com%2F&orig_request_uri=https%3A%2F%2Fwww.facebook.com%2Fbusiness%2Fhelp%2F132073386867900&primary_cmsid=132073386867900&primary_content_locale=ru_RU&region=emea&scrolled=true&session_id=2P6zpQht8TgSaz0Ye&site=fb4b&extra_data[view_type]=v3_initial_view&extra_data[site_section]=help&extra_data[placement]=%2Fbusiness%2Fhelp%2F13207338686790')
time.sleep(180)
try:
    WebDriverWait(browser, 30).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[1]/div[3]/div[1]/div[1]/form/div/div[1]/div/div/div[2]/p[1]')))
    send_log(task_id=task_id, message='Checkpoint')
except:
    print('All normal')
send_log(task_id=task_id, message='Trying to load card')
try:
    WebDriverWait(browser, 60).until(
        EC.presence_of_element_located((By.XPATH,
                                        '/html/body/div[7]/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div[1]/div/span/div/div/div')))
    ss1 = browser.find_element_by_xpath(
        '/html/body/div[7]/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div[1]/div/span/div/div/div')
    ss1.click()
except:
    print(
        'нет рекламы')  # /html/body/div[8]/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div/div[1]/div[4]/div/div/div/div[1]/div[1]/div[1]/div/span/span
try:
    WebDriverWait(browser, 60).until(
        EC.presence_of_element_located((By.XPATH,
                                        '/html/body/div[1]/div/div/div/div[1]/div/div/div[2]/div/div[3]/div/div[3]/div/div/div[1]/div/div/button')))
    ss1 = browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/div[1]/div/div/div[2]/div/div[3]/div/div[3]/div/div/div[1]/div/div/button')
    ss1.click()
except:
    print('no button')

try:
    try:
        WebDriverWait(browser, 60).until(
            EC.presence_of_element_located((By.XPATH,'/html/body/div[8]/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div/div[1]/div[4]/div/div/div/div[1]/div[1]/div[1]/div/span/span')))
        but11 = browser.find_element_by_xpath('/html/body/div[8]/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div/div[1]/div[4]/div/div/div/div[1]/div[1]/div[1]/div/span/span')
        but11.click()
        print('1')
        WebDriverWait(browser, 60).until(
            EC.presence_of_element_located((By.XPATH,'/html/body/div[8]/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div/div[1]/div[3]/div/div[1]/div[2]/div[2]/div/div/div/div/div/label/div/div[2]/input')))
        cardNumber = browser.find_element_by_xpath('/html/body/div[8]/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div/div[1]/div[3]/div/div[1]/div[2]/div[2]/div/div/div/div/div/label/div/div[2]/input')
        cardNumber.send_keys('4441 1144 2323 9886')
        cardMonthYear = browser.find_element_by_xpath('/html/body/div[8]/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div/div[1]/div[3]/div/div[1]/div[2]/div[3]/div/div/div/div/div/label/div/div[1]/input')
        cardMonthYear.send_keys('0624')
        cardCvv = browser.find_element_by_xpath(
            '/html/body/div[8]/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div/div[1]/div[3]/div/div[1]/div[2]/div[4]/div/div/div/div/div/label/div/div[1]/input')
        cardCvv.send_keys('886')
        cardBut = browser.find_element_by_xpath(
            '/html/body/div[8]/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div/div[1]/div[4]/div/div/div/div[1]/div[1]/div[1]/div/span/span')
        cardBut.click()
    except:
        print('2')
        WebDriverWait(browser, 60).until(
            EC.presence_of_element_located((By.XPATH,
                                            # /html/body/div[8]/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div/div[1]/div[4]/div/div/div/div[1]/div[1]/div[1]/div/span/span
                                            '/html/body/div[1]/div/div/div/div[1]/div/div/div[2]/div/div[3]/div/div[3]/div/div/div[1]/div/div/button')))  # /html/body/div[8]/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div/div[1]/div[4]/div/div/div/div[1]/div[1]/div[1]/div/span/span
        but11 = browser.find_element_by_xpath(
            '/html/body/div[1]/div/div/div/div[1]/div/div/div[2]/div/div[3]/div/div[3]/div/div/div[1]/div/div/button')  # //*[@id="facebook"]/body/div[8]/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div/div[1]/div[4]/div/div/div/div[1]/div[1]/div[1]/div/span/span
        but11.click()
        print('33')
        WebDriverWait(browser, 60).until(
            EC.presence_of_element_located((By.XPATH,
                                            '/html/body/div[8]/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div/div[1]/div[3]/div/div/div[2]/div[2]/div/div/div/div/div/label/div/div[2]/input')))
        cardNumber = browser.find_element_by_xpath(#/html/body/div[8]/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div/div[1]/div[3]/div/div/div[2]/div[2]/div/div/div/div/div/label/div/div[2]/input
            '/html/body/div[8]/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div/div[1]/div[3]/div/div/div[2]/div[2]/div/div/div/div/div/label/div/div[2]/input')
        cardNumber.send_keys('4441 1144 2323 9886')
        cardMonthYear = browser.find_element_by_xpath(
            '/html/body/div[8]/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div/div[1]/div[3]/div/div/div[2]/div[3]/div/div/div/div/div/label/div/div[1]/input')
        cardMonthYear.send_keys('0624')
        cardCvv = browser.find_element_by_xpath(
            '/html/body/div[8]/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div/div[1]/div[3]/div/div/div[2]/div[4]/div/div/div/div/div/label/div/div[1]/input')
        cardCvv.send_keys('886')
        cardBut = browser.find_element_by_xpath(
            '/html/body/div[8]/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div/div[1]/div[4]/div/div/div/div[1]/div[1]/div[1]/div/span')
        cardBut.click()

except:
    try:
        print('3')
        WebDriverWait(browser, 60).until(
            EC.presence_of_element_located((By.XPATH, #/html/body/div[8]/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div/div[1]/div[4]/div/div/div/div[1]/div[1]/div[1]/div/span/span
                                                '/html/body/div[8]/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div/div[1]/div[4]/div/div/div/div[1]/div[1]/div[1]/div/span/span')))  #/html/body/div[8]/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div/div[1]/div[4]/div/div/div/div[1]/div[1]/div[1]/div/span/span
        but11 = browser.find_element_by_xpath('/html/body/div[8]/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div/div[1]/div[4]/div/div/div/div[1]/div[1]/div[1]/div/span/span') #//*[@id="facebook"]/body/div[8]/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div/div[1]/div[4]/div/div/div/div[1]/div[1]/div[1]/div/span/span
        but11.click()
        print('44')

        cardNumber = browser.find_element_by_xpath(
                '/html/body/div[8]/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div/div[1]/div[3]/div/div/div[2]/div[2]/div/div/div/div/div/label/div/div[2]/input')
        cardNumber.send_keys('4441 1144 2323 9886')
        cardMonthYear = browser.find_element_by_xpath(
                '/html/body/div[8]/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div/div[1]/div[3]/div/div/div[2]/div[3]/div/div/div/div/div/label/div/div[1]/input')
        cardMonth = browser.find_element_by_xpath(
            '/html/body/div[7]/div[2]/div/div/div/div[2]/form[1]/div/div[1]/div/div/div/div[4]/div[2]/label/input')
        cardMonth.send_keys('0624')
        cardCvv = browser.find_element_by_xpath(
                '/html/body/div[8]/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div/div[1]/div[3]/div/div/div[2]/div[4]/div/div/div/div/div/label/div/div[1]/input')
        cardCvv.send_keys('886')
        cardBut = browser.find_element_by_xpath(
                '/html/body/div[8]/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div/div[1]/div[4]/div/div/div/div[1]/div[1]/div[1]/div/span/span')
        cardBut.click()
    except:
        print('Не заполняем карту 1')
    try:
        print('5')
        WebDriverWait(browser, 60).until(
            EC.presence_of_element_located((By.XPATH,
                                                '/html/body/div[7]/div[2]/div/div/div/div[2]/form[1]/div/div[1]/div/div/div/div[2]/div/label/input')))  #
        cardName = browser.find_element_by_xpath(
                '/html/body/div[7]/div[2]/div/div/div/div[2]/form[1]/div/div[1]/div/div/div/div[2]/div/label/input')
            #cardName.send_keys()
        cardNumber = browser.find_element_by_xpath(
                '/html/body/div[7]/div[2]/div/div/div/div[2]/form[1]/div/div[1]/div/div/div/div[4]/div[1]/label/input')
        cardNumber.send_keys('4441 1144 2323 9886')
        cardMonth = browser.find_element_by_xpath(
                '/html/body/div[7]/div[2]/div/div/div/div[2]/form[1]/div/div[1]/div/div/div/div[4]/div[2]/label/input')
        cardMonth.send_keys('06')
        cardYear = browser.find_element_by_xpath(
                '/html/body/div[7]/div[2]/div/div/div/div[2]/form[1]/div/div[1]/div/div/div/div[4]/div[3]/label/input')
        cardYear.send_keys('24')
        cardCvv = browser.find_element_by_xpath(
                '/html/body/div[7]/div[2]/div/div/div/div[2]/form[1]/div/div[1]/div/div/div/div[6]/div[1]/label/input')
        cardCvv.send_keys('886')
        cardBut = browser.find_element_by_xpath(
                '/html/body/div[7]/div[2]/div/div/div/div[3]/table/tbody/tr/td[1]/div/div[2]/button')
        cardBut.click() #5355 1719 8480 3642, 04/22, 238
    except:
        print('Не заполняем карту 2')
time.sleep(60)
statuscard = True
try:
    try:#/html/body/div[7]/div[2]/div/div/div/div[2]/form[1]/div/div[1]/div/div/div/div[1]/div/span/div
        WebDriverWait(browser, 60).until(
            EC.presence_of_element_located((By.XPATH,
                                            '/html/body/div[8]/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div/div[1]/div[3]/div/div/div/div[2]/div/div/span')))
        statuscard = False
    except:
        WebDriverWait(browser, 60).until(
            EC.presence_of_element_located((By.XPATH,
                                            '/html/body/div[8]/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div/div[1]/div[3]/div/div/div/div[2]/div/div/span')))
        statuscard = False
except:
    print('All normal with card')
if statuscard == False:
    send_log(task_id=task_id, message='Cannot load card')
else:
    send_log(task_id=task_id, message='Card is loaded')
browser.get('https://www.facebook.com/adsmanager')
time.sleep(3)
try:
    WebDriverWait(browser, 30).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[1]/div[3]/div[1]/div[1]/form/div/div[1]/div/div/div[2]/p[1]')))
    send_log(task_id=task_id, message='Checkpoint')
except:
    print('All normal')
browser.get('https://www.facebook.com/adsmanager')
time.sleep(120)
try:
    WebDriverWait(browser, 30).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[5]/div[2]/div/div/div/div/div/div/div[2]/span[2]/div/div/button/div/div')))
    bb = browser.find_element_by_xpath(
        '/html/body/div[5]/div[2]/div/div/div/div/div/div/div[2]/span[2]/div/div/button/div/div')
    bb.click()
except:
    print('all right')
try:
    WebDriverWait(browser, 30).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[6]/div[2]/div/div/div/div/div/div/div[2]/span[2]/div/div/button/div/div')))
    bb = browser.find_element_by_xpath(
        '/html/body/div[6]/div[2]/div/div/div/div/div/div/div[2]/span[2]/div/div/button/div/div')
    bb.click()
except:
    print('all right')

try:
    WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="APP_INSTALLS"]/div/div[1]/div/input')))
    click1 = browser.find_element_by_xpath('//*[@id="APP_INSTALLS"]/div/div[1]/div/input')
    click1.click()
except:
    print('dali')
try:
    click2 = browser.find_element_by_xpath(
        '/html/body/div[6]/div[2]/div/div/div/div/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[1]/div/input')
    click2.click()
    but4 = browser.find_element_by_xpath(
        '//*[@id="facebook"]/body/div[6]/div[2]/div/div/div/div/div/div/div[3]/span[2]/div/div[2]/button/div/div')
    but4.click()
except:
    print('dali')
try:
    WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((By.XPATH,
                                        '/html/body/div[1]/div/div/div/div/div/div[1]/div/div[2]/div/div[2]/div[3]/div[4]/div/div[3]/div/div/div/div/div[1]/div/div/div/div[1]/div/div[5]/span/div/div/div[1]')))  #
    g1 = browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/div/div/div[1]/div/div[2]/div/div[2]/div[3]/div[4]/div/div[3]/div/div/div/div/div[1]/div/div/div/div[1]/div/div[5]/span/div/div/div[1]')
    g1.click()
except:
    WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((By.XPATH,
                                        '/html/body/div[1]/div/div/div/div/div/div[1]/div/div[2]/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div/div/div[1]/div/div/div/div[1]/div/div[5]')))  # /html/body/div[1]/div/div/div/div/div/div[1]/div/div[2]/div/div[2]/div[3]/div[4]/div/div[3]/div/div/div/div/div[1]/div/div/div/div[1]/div/div[5]/span/div/div/div[1]
    g1 = browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/div/div/div[1]/div/div[2]/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div/div/div[1]/div/div/div/div[1]/div/div[5]]')
    g1.click()
ActionChains(browser).send_keys(Keys.DOWN).perform()
ActionChains(browser).send_keys(Keys.DOWN).perform()
ActionChains(browser).send_keys(Keys.ENTER).perform()
time.sleep(2)
WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type=file]')))
try:
    try:
        excelimage = browser.find_element_by_xpath(
            '/html/body/div[6]/div[2]/div/div/div/div/div/div/div[2]/div/div[1]/div/ul/li[2]/a')
        excelimage.click() #/html/body/div[7]/div[2]/div/div/div/div/div/div/div[2]/div/div[1]/div/ul/li[2]/a
        WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type=file]')))
        excel = browser.find_element_by_css_selector('input[type=file]')
        excel.send_keys(r"D:\programs\facebookbm\rek1.jpg")
        send_log(task_id=task_id, message='Photo for ads loaded')
    except:
        excelimage = browser.find_element_by_xpath(
            '/html/body/div[7]/div[2]/div/div/div/div/div/div/div[2]/div/div[1]/div/ul/li[2]/a')
        excelimage.click() #/html/body/div[7]/div[2]/div/div/div/div/div/div/div[2]/div/div[1]/div/ul/li[2]/a
        WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type=file]')))
        excel = browser.find_element_by_css_selector('input[type=file]')
        excel.send_keys(r"D:\programs\facebookbm\rek1.jpg")
        send_log(task_id=task_id, message='Photo for ads loaded')
except:
    send_log(task_id=task_id, message='Cannot load pic to Ads')
try:
    try:
        excelvideo = browser.find_element_by_xpath(
            '/html/body/div[6]/div[2]/div/div/div/div/div/div/div[2]/div/div[1]/div/ul/li[3]/a')
        excelvideo.click()
        WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type=file]')))
        excel = browser.find_element_by_css_selector('input[type=file]')
        excel.send_keys(r"D:\programs\facebookbm\ru2.mp4")
        send_log(task_id=task_id, message='Video for ads loaded')
    except:
        excelvideo = browser.find_element_by_xpath(
            '/html/body/div[7]/div[2]/div/div/div/div/div/div/div[2]/div/div[1]/div/ul/li[3]/a')
        excelvideo.click()
        WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type=file]')))
        excel = browser.find_element_by_css_selector('input[type=file]')
        excel.send_keys(r"D:\programs\facebookbm\ru2.mp4")
        send_log(task_id=task_id, message='Video for ads loaded')
except:
    send_log(task_id=task_id, message='Cannot load video to Ads')
try:
    try:
        exceltable = browser.find_element_by_xpath(
            '/html/body/div[6]/div[2]/div/div/div/div/div/div/div[2]/div/div[1]/div/ul/li[1]/a')
        exceltable.click()
        WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type=file]')))
        excel = browser.find_element_by_css_selector('input[type=file]')
        excel.send_keys(r"D:\programs\facebookbm\ads.xlsx")
    except:
        exceltable = browser.find_element_by_xpath(
            '/html/body/div[7]/div[2]/div/div/div/div/div/div/div[2]/div/div[1]/div/ul/li[1]/a')
        exceltable.click()
        WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type=file]')))
        excel = browser.find_element_by_css_selector('input[type=file]')
        excel.send_keys(r"D:\programs\facebookbm\ads.xlsx")
except:
    send_log(task_id=task_id, message='Cannot load excel to Ads')
time.sleep(5)  # /html/body/div[5]/div[2]/div/div/div/div/div/div/div[3]/span[2]/div/div[2]/button/div/div
try:
    try:
        WebDriverWait(browser, 30).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[6]/div[2]/div/div/div/div/div/div/div[3]/span[2]/div/div[2]/button')))
        excelbut = browser.find_element_by_xpath(
            '/html/body/div[6]/div[2]/div/div/div/div/div/div/div[3]/span[2]/div/div[2]/button')
        excelbut.click()
        status = True#/html/body/div[7]/div[2]/div/div/div/div/div/div/div[3]/span[2]/div/div[2]/button
    except:
        WebDriverWait(browser, 30).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[7]/div[2]/div/div/div/div/div/div/div[3]/span[2]/div/div[2]/button')))
        excelbut = browser.find_element_by_xpath(
            '/html/body/div[7]/div[2]/div/div/div/div/div/div/div[3]/span[2]/div/div[2]/button')
        excelbut.click()
        status = True#
except:
    send_log(task_id=task_id, message='Cannot create Ads')

try:
    WebDriverWait(browser, 30).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[1]/div[3]/div[1]/div[1]/form/div/div[1]/div/div/div[2]/p[1]')))
    send_log(task_id=task_id, message='Checkpoint')
    status = False
except:
    print('All normal')
try:
    WebDriverWait(browser, 30).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[1]/div[1]/div[2]/h1/span')))
    send_log(task_id=task_id, message='Connection lost')
    status = False
except:
    print('all nornal')
try:
    WebDriverWait(browser, 30).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[1]/div[3]/div[1]/div[1]/form/div/div[1]/div/div/div[2]/p[1]')))
    send_log(task_id=task_id, message='Checkpoint')
    status = False
except:
    print('all normal')
if status == True:
    print('OK)')
    send_log(task_id=task_id, message='All ads created')
