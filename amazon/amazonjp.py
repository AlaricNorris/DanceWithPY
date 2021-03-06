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

  




def recordFailure(cardposition,index):
	print ("failed" + cardlist[int(cardposition)]  + "|" + str(index)) 

# 初始化Options
driverOptions = webdriver.ChromeOptions()
driverOptions.add_argument(r"user-data-dir=C:\Users\AlaricNorris\AppData\Local\Google\Chrome\User Data")
#driverOptions.add_experimental_option('mobileEmulation', mobileEmulation)
# 初始化WebDriver
driver = webdriver.Chrome("chromedriver",0,driverOptions)
driver.maximize_window()    # 最大化浏览器窗口  
driver.implicitly_wait(1)   # 设置隐式时间等待  
def R(cardposition,index):
	driver.get("https://www.amazon.co.jp/") 
	time.sleep(0.5)

	# 账户及列表
	panel = driver.find_element_by_id("nav-link-accountList")
	panel.click() 

	try:  
		time.sleep(0.5)
		# 礼品卡
	    giftcard = driver.find_element_by_xpath("//*/a[contains(@href,'https://www.amazon.co.jp/gp/css/gc/balance?ref_=ya_d_c_gc')]")
	    giftcard.click() 
	except Exception as e:  
	    recordFailure(cardposition,index)
	    print ("Exception found", format(e))  
	    return

	try:  
		time.sleep(1)
		# 充值礼品卡
	    chzh = driver.find_element_by_xpath("//*/a[contains(@href,'/gp/gc/create/ref=gc-ya-view')]")
	    chzh.click() 
	except Exception as e:  
	    
	    recordFailure(cardposition,index)
	    print ("Exception found", format(e)) 
	    return
 

	try:   
		# 金额
		summary = driver.find_element_by_id("gc-asv-manual-reload-amount")
		summary.click() 
		summary.send_keys("15")
		summary.click() 
	except Exception as e:  
	    recordFailure(cardposition,index)
	    print ("Exception found", format(e)) 
	    return

	try:  
		time.sleep(1)
		# 继续
		submit = driver.find_element_by_id("form-submit-button")
		submit.click()
	except Exception as e:  
	    recordFailure(cardposition,index)
	    print ("Exception found", format(e))  
	    return

	try:  
		time.sleep(1)
		# 卡 //*[@id="existing-credit-cards-box"]/div[3]
		#//*[@id="pm_0"]
		#card = driver.find_element_by_id("pm_" + str(cardposition))
		#card = driver.find_element_by_xpath("//*[@id='existing-credit-cards-box']/div[" + str(cardposition+3) + "]")
		card = driver.find_element_by_xpath("//*[@id='pm_" + str(cardposition) + "']")
		card.click() 
	except Exception as e:  
	    recordFailure(cardposition,index)
	    print ("Exception found", format(e))  
	    return

	try:  
		# 继续
		contimuetop = driver.find_element_by_id("continue-top")
		contimuetop.click()
		time.sleep(0.5)
	except Exception as e:  
	    recordFailure(cardposition,index)
	    print ("Exception found", format(e))  
	    return

	try:
                # 校验金额是否正确
                #//*[@id="subtotals-marketplace-table"]/table/tbody/tr[4]/td[2]/strong
                totalSummary = driver.find_element_by_xpath("//*[@id='subtotals-marketplace-table']/table/tbody/tr[4]/td[2]/strong")
                if totalSummary.text == "￥ 15":
                        # 校验是否选择对了
                        validate = driver.find_element_by_xpath("//*[@id='payment-information']/ul/li/span/span[2]")
                        if validate.text == cardlist[int(cardposition)] :
                                # 提交订单
                                placeYourOrder = driver.find_element_by_name("placeYourOrder1")
                                print(str(placeYourOrder))
                                placeYourOrder.click()
                                time.sleep(0.5)
                print ("finish" + cardlist[int(cardposition)]  + "|" + str(index))                      	    
	except Exception as e:  
	    recordFailure(cardposition,index)
	    print ("Exception found", format(e)) 
	    return

	time.sleep(0.5)


for cardposition in range(4):
        for repeattime in range (int(repeattimes[cardposition])):
                R(cardposition,repeattime)


print ("Mission Accomplished" )    
#driver.quit()

