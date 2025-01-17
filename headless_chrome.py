import os 
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.chrome.options import Options

chrome_options = Options()  
chrome_options.add_argument("--headless")
fp = os.path.join(os.path.dirname(__file__), 'drivers/chromedriver')  
driver = webdriver.Chrome(fp,chrome_options=chrome_options)  
driver.get("http://www.duo.com")

magnifying_glass = driver.find_element_by_id("js-open-icon")  
if magnifying_glass.is_displayed():  
  magnifying_glass.click()  
else:  
  menu_button = driver.find_element_by_css_selector(".menu-trigger.local")  
  menu_button.click()  

search_field = driver.find_element_by_id("site-search")  
search_field.clear()  
search_field.send_keys("Olabode")  
search_field.send_keys(Keys.RETURN)  
assert "Looking Back at Android Security in 2016" in driver.page_source   

driver.get_screenshot_as_file('snapshot.png')

driver.close() 
