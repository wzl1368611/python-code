import time 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random

driver=webdriver.Chrome()
#请求网页
driver.get("https://www.huya.com/688")
#查找id
loginBtn=driver.find_element_by_id('nav-login')
loginBtn.click()
#写个死循环发送弹幕
time.sleep(40)





while 1:
	#输入发送弹幕内容
	input_text=driver.find_element_by_id('pub_msg_input')
	test_arr=['???',"哈哈哈哈","666","强啊"]
	random_index=random.randint(0,len(test_arr)-1)
	input_text.send_keys(test_arr[random_index])
	time.sleep(3)
	send_btn=driver.find_element_by_id('msg_send_bt')


	send_btn.click()
	time.sleep(7)



