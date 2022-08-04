
import time

from selenium.webdriver import Chrome

driver = Chrome()
driver.implicitly_wait(5) # 隐式等待

driver.get("http://www.baidu.com")

driver.maximize_window()

# 元素定位
driver.find_element(by="id", value="kw").send_keys("baidu")

driver.find_element(by="id", value="su").click()

driver.find_element(by="xpath", value='//*[@id="1"]/div/h3/a[1]').click()




# driver.quit()




