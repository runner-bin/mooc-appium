import time

from appium import webdriver

global driver

def setDriver():
    capabilities={
    "platformName": "Android",
    "deviceName": "c23505107d12",
    "appPackage": "com.android.deskclock",
    "appActivity":".DeskClock"}
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",capabilities)
    return driver

driver=setDriver()

def getWindowSize():
    size = driver.get_window_size()
    width = size['width']
    height = size['height']
    return width,height

def swipe(dire):
    x1= getWindowSize()[0]/10*9
    y1=getWindowSize()[1]/7
    x= getWindowSize()[0]/10
    y=getWindowSize()[1]/2

    if dire=="left":  
        driver.swipe(x1,y1,x,y1)
    elif dire=="right":
        driver.swipe(x,y1,x1,y1)
    elif dire=="up":
        driver.swipe(x1,y,x1,y1) 
    elif dire=="down":
        driver.swipe(x1,y1,x1,y)  
    else:
        print "dire setting is incalid!"

# class Operation():
#     def __init__(self,way,mode,ID):
#         self.way=way
#         self.mode=mode
#         self.ID=ID
def OOP(mode,parse):
    if mode=="Id":
        return driver.find_element_by_id(parse)
    elif mode=="ClassName":
        return driver.find_element_by_class_name(parse)
    else:
        print "mode error->" + mode
try:
    swipe("right")
    time.sleep(1)
    OOP("Id","com.android.deskclock:id/arrow").click()
    time.sleep(1)
    OOP("Id","com.android.deskclock:id/edit_label").click()
    OOP("ClassName","android.widget.EditText").send_keys("HelloWorld!")

    
 
    # swipe("left")
    # swipe("left")
    # swipe("up")
    # swipe("down")
    print "success!Bye"
except:
    print "see consoloe"
