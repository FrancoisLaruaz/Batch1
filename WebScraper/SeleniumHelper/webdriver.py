from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options

def getFirefoxDriver(proxy,port):

    binary_argument = FirefoxBinary("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
    binary_argument = FirefoxBinary("C:\\webdrivers\\FirefoxPortable\\FirefoxPortable.exe")
    capabilities_argument = DesiredCapabilities().FIREFOX
    capabilities_argument["marionette"] = False
    profile = webdriver.FirefoxProfile()
    profile.set_preference("network.proxy.type", 1);
    profile.set_preference("network.proxy.http", proxy);
    profile.set_preference("network.proxy.http_port", port);
    profile.set_preference("network.proxy.ssl", proxy);
    profile.set_preference("network.proxy.ssl_port", port);
    #driver = webdriver.Firefox(firefox_binary=binary_argument, capabilities=capabilities_argument);
    driver = webdriver.Firefox(executable_path="C:\\webdrivers\\geckodriver.exe")
    driver.get("http://icanhazip.com")
    return driver
	
def getGoogleChromeDriver():
    option = webdriver.ChromeOptions()
    option.add_argument("--incognito")
    browser = webdriver.Chrome(executable_path="C:\\webdrivers\\chromedriver.exe", chrome_options=option)
    return browser	