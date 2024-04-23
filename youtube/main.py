from selenium import webdriver

if __name__ == '__main__':
    # options = webdriver.ChromeOptions()

    # options.add_argument('--ignore-certificate-errors')
    # options.add_argument('log-level=INT')
    # driver = webdriver.Firefox()
    # options = Options()
    # options.set_preference("network.proxy.type", 1)
    # options.set_preference("network.proxy.http", "xx.xxx.xxx.xxxx")
    # options.set_preference("network.proxy.http_port", 8000)
    # options.set_preference("network.proxy.ssl", "xx.xxx.xxx.xxx")
    # options.set_preference("network.proxy.ssl_port", 8000)

    driver = webdriver.Firefox()

    res = driver.get(u'https://www.youtube.com/@BroCodez/video')
    print(driver.page_source)

    driver.close()