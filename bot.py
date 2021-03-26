from selenium import webdriver
import time, requests

# setting chromedriver as web driver
driver = webdriver.Chrome('/Users/lbrooks/downloads/chromedriver')
time.sleep(2)

#navigate to linkedin
driver.get('https://www.linkedin.com/home')
time.sleep(2)

#clicking signin button
driver.find_element_by_xpath('/html/body/nav/div/a[2]').click()
time.sleep(2)

#takes username and password from user running python app
username = input('enter your email or phone number')
password = input('enter your password')

#inputs user provided data to page and signs in
driver.find_element_by_xpath('//*[@id="username"]').send_keys(username)
driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button').click()
time.sleep(2)

#opens up notifications tab
driver.find_element_by_xpath('//*[@id="ember28"]').click()
time.sleep(10)

#opens up jobs tab
driver.find_element_by_xpath('//*[@id="ember24"]').click()
time.sleep(2)

#inputs software engineer and clicks search
driver.find_element_by_xpath('//*[@id="jobs-search-box-keyword-id-ember545"]').send_keys('Software Engineer')
driver.find_element_by_xpath('//*[@id="ember544"]/div/div[2]/button').click()
time.sleep(2)

#shows only jobs posted within last week
driver.find_element_by_xpath('//*[@id="ember1025"]').click()
driver.find_element_by_xpath('//*[@id="artdeco-hoverable-artdeco-gen-43"]/div[1]/div/form/fieldset/div[1]/ul/li[2]/label/p/span').click()
driver.find_element_by_xpath('//*[@id="ember1029"]').click()

