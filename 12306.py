from  selenium  import webdriver#导入浏览器模块
import time
from selenium.webdriver.support.select import Select#下拉框模块
from winsound import Beep#提示声音模块
path = r"C:\Users\admin\Downloads\chromedriver.exe"#谷歌控住器路径
url = "https://kyfw.12306.cn/otn/leftTicket/init?"#12306网址
browser = webdriver.Chrome(path)#用谷歌打开浏览器
time.sleep(5)#睡5秒
browser.get(url)#用谷歌请求12306网址
start_city = browser.find_element_by_id("fromStationText")#用谷歌请求开始位置的id
start_city.click()#筛选
start_city.clear()#清
start_city.send_keys("北京\n")#输入自己现在的地方
start_city = browser.find_element_by_id("toStationText")#用谷歌输入目的地的id
start_city.click()#筛选
start_city.clear()#清除
start_city.send_keys("上海\n")#输入自己目的地

choice_time = Select(browser.find_element_by_id("cc_start_time"))#这个是获取下拉框当前时间
choice_time.select_by_visible_text("00:00--24:00")#这是输入时间
data = browser.find_element_by_css_selector("#date_range li:nth-child(5)")#时间
data.click()#筛选

time.sleep(3)

favorite = ["G9","G129","G137","G145","G11","G153"]#车的种类


xpath ='//tbody[@id="queryLeftTable"]//td[4][@class]/../td[1]//a'#有票的车信息
train_list = browser.find_elements_by_xpath(xpath)#提取车票信息

for train in train_list:
    train_num = train.text
    if train_num in favorite:
     print("亲 有票了哦！！！")
    target = train.find_elements_by_xpath('../../../../../td[13]/a')[0]
    target.click()
    input("请手动登录 登录成功后按回车键")
    time.sleep(3)
    browser.find_element_by_id("normalPassenger_0").click()
    browser.find_element_by_id("submitOrder_id").click()
    time.sleep(1)
    browser.find_element_by_id("qr_submit_id").click()
    print("亲 恭喜您抢票成功！！！")
    Beep(3000,3000)
    break
else:
        print("亲 暂时还没有票  请耐心等待...")
browser.quit()
