from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get('https://www.messenger.com/')

driver.find_element_by_id('email').send_keys('melvinchia623600@gmail.com')
driver.find_element_by_id('pass').send_keys('idontwanttotellyoulol')
driver.find_element_by_id('loginbutton').click()
lol = driver.find_element_by_tag_name('ul').find_elements_by_tag_name('li')
for i in lol:
    print(i.find_element_by_tag_name('a').get_attribute('data-href'))


driver.find_element_by_xpath("//*[contains(text(), 'Jeddy')]").click()
for i in range(500):
    try:
        driver.find_element_by_css_selector("[aria-label='Type a message...']").send_keys(r"Happy New Month")
    except:
        driver.find_element_by_css_selector("[aria-label='Type a message, @name...']").send_keys(r"Happy New Month")
    driver.find_element_by_css_selector("[aria-label='Type a message...']").send_keys(Keys.ENTER)
