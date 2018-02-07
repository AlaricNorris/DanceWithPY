import time  
import sys

from selenium import webdriver

cardlist = [ '7292', '4767', '6709', '3405']
args = sys.argv[1]
repeattimes = args.split(',')

# WIDTH = 320
#  = 640
# PIXEL_RATIO = 3.0
# UA = 'Mozilla/5.0 (Linux; Android 4.1.1; GT-N7100 Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/6.3'
# mobileEmulation = {"deviceMetrics": {"width": WIDTH, "height": HEIGHT, "pixelRatio": PIXEL_RATIO}, "userAgent": UA}
# options = webdriver.ChromeOptions()

  

# 初始化Options
driverOptions = webdriver.ChromeOptions()
driverOptions.add_argument(r"user-data-dir=C:\Users\AlaricNorris\AppData\Local\Google\Chrome\User Data")
#driverOptions.add_experimental_option('mobileEmulation', mobileEmulation)
# 初始化WebDriver
driver = webdriver.Chrome("chromedriver",0,driverOptions)
#driver.maximize_window()    # 最大化浏览器窗口  
driver.implicitly_wait(2)   # 设置隐式时间等待  
def R(cardposition,index):
	driver.get("https://www.amazon.co.jp/") 

	panel = driver.find_element_by_id("nav-link-accountList")
	panel.click()

	try:  
	    giftcard = driver.find_element_by_xpath("//*/a[contains(@href,'https://www.amazon.co.jp/gp/css/gc/balance?ref_=ya_d_c_gc')]")
	    giftcard.click()
	except Exception as e:  
	    print ("Exception found", format(e))  

	try:  
	    chzh = driver.find_element_by_xpath("//*/a[contains(@href,'/gp/gc/create/ref=gc-ya-view')]")
	    chzh.click()
	except Exception as e:  
	    print ("Exception found", format(e))  

	time.sleep(1)

	# 金额
	summary = driver.find_element_by_id("gc-asv-manual-reload-amount")
	summary.click()
	summary.send_keys("15")
	time.sleep(1)

	# 继续
	submit = driver.find_element_by_id("form-submit-button")
	submit.click()
	time.sleep(1)

	# 卡
	submit = driver.find_element_by_id("pm_" + str(cardposition))
	submit.click()
	time.sleep(1)

	# 继续
	submit = driver.find_element_by_id("continue-top")
	time.sleep(1)
	submit.click()

	try:
                # 校验金额是否正确
                totalSummary = driver.find_element_by_xpath("//*[@id='subtotals-marketplace-table']/table/tbody/tr[4]/td[2]/strong")
                if totalSummary.text == "￥ 15":
                        # 校验是否选择对了
                        validate = driver.find_element_by_xpath("//*[@id='payment-information']/ul/li/span/span[2]")
                        if validate.text == cardlist[int(cardposition)] :
                                # 提交订单
                                submit = driver.find_element_by_name("placeYourOrder1")
                                time.sleep(1)
                                submit.click()
    
                print ("finish" + cardlist[int(cardposition)]  + "|" + str(index))                      	    
	except Exception as e:  
	    print ("Exception found", format(e)) 

	time.sleep(1) 


for cardposition in range(4):
        for repeattime in range (int(repeattimes[cardposition])):
                R(cardposition,repeattime)


#driver.quit()
