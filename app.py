import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

CHROMEDRIVER_PATH = '/workspace/x/chromedriver'
URL = 'http://example.com'


def main():
    opts = Options()
    opts.add_argument('--headless')
    opts.add_argument('--no-sandbox')

    driver = webdriver.Chrome(CHROMEDRIVER_PATH, options=opts)
    driver.get(URL)
    time.sleep(1)
    print(driver.page_source)

    driver.close()


if __name__ == '__main__':
    main()
