from selenium import webdriver
from selenium.webdriver.common.by import By


def fn_get_image(keyword):
    url = 'https://www.google.com/search?q='
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome('../day4/chromedriver')

    driver.implicitly_wait(1)
    driver.get(url + keyword)
    driver.implicitly_wait(2)

    driver.find_element(By.XPATH, '//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click()
    body = driver.find_element(By.TAG_NAME, 'body')

    img = body.find_elements(By.TAG_NAME, 'img')
    for v in img:
        try:
            result = v.get_attribute('src')
            if result != None:
                if 'usqp=CAU' in result:
                    print(result)
                    break
        except Exception as e:
            print(str(e))
    driver.close()


keywords = ['저전동 상가골목축제']

for keyword in keywords:
    fn_get_image(keyword)
