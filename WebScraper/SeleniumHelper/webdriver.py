from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType
from Logger.logger import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

def getFirefoxDriver(host,port):
	try:
		path='C:\\webdrivers\\geckodriver.exe'
		fullproxy = host+":"+port
		#https://stackoverflow.com/questions/17082425/running-selenium-webdriver-with-a-proxy-in-python
		firefox_capabilities = DesiredCapabilities.FIREFOX
		firefox_capabilities['marionette'] = True
		webdriver.DesiredCapabilities.FIREFOX['proxy']={
			"httpProxy":fullproxy,
			"ftpProxy":fullproxy,
			"sslProxy":fullproxy,
			"noProxy":None,
			"proxyType":"MANUAL",
			"autodetect":False
		}		
		prox = Proxy()
		prox.proxy_type = ProxyType.MANUAL
		prox.http_proxy = fullproxy
		prox.socks_proxy = fullproxy
		prox.ssl_proxy =fullproxy	
		#prox.add_to_capabilities(firefox_capabilities)
		fp = webdriver.FirefoxProfile()
		fp.set_preference("network.proxy.type", 1)
		fp.set_preference("network.proxy.http",host)
		fp.set_preference("network.proxy.http_port",int(port))
		fp.set_preference("network.proxy.https",host)
		fp.set_preference("network.proxy.https_port",int(port))
		fp.set_preference("network.proxy.ssl",host)
		fp.set_preference("network.proxy.ssl_port",int(port))  
		fp.set_preference("network.proxy.ftp",host)
		fp.set_preference("network.proxy.ftp_port",int(port))   
		fp.set_preference("network.proxy.socks",host)
		fp.set_preference("network.proxy.socks_port",int(port))   
		#fp.set_preference("general.useragent.override","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A")
		fp.update_preferences()
		driver = webdriver.Firefox(executable_path=path)


		return driver
	except Exception:
		LogError(''.join(traceback.format_exc()),"host = "+host+" and port = "+port)
	return getGoogleChromeDriver(host+":"+port)
	
def waitForWebdriver(browser,css_selector):
	delay = 55 # seconds
	try:
		print("begin wait for "+css_selector)
		wait = WebDriverWait(browser, delay)
		print("before test")
		wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))
		print("end wait")
	except Exception:
		LogError(''.join(traceback.format_exc()),"css_selector = "+css_selector)
	return			
	
def getGoogleChromeDriver(fullproxy):
	try:
		option = webdriver.ChromeOptions()
		option.add_argument("--incognito")
		prox = Proxy()
		prox.proxy_type = ProxyType.MANUAL
		prox.http_proxy = fullproxy
		prox.socks_proxy = fullproxy
		prox.ssl_proxy =fullproxy

		capabilities = webdriver.DesiredCapabilities.CHROME
		prox.add_to_capabilities(capabilities)
		browser = webdriver.Chrome(executable_path="C:\\webdrivers\\chromedriver.exe", chrome_options=option,desired_capabilities=capabilities)
		return browser
	except Exception:
		LogError(''.join(traceback.format_exc()),"fullproxy = "+fullproxy)
	return null		