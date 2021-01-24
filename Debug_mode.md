https://selenium-python.readthedocs.io/locating-elements.html
**Locating Elements:**
Selenium provides the following methods to locate elements in a page:
find_element_by_id
find_element_by_name
find_element_by_xpath
find_element_by_link_text
find_element_by_partial_link_text
find_element_by_tag_name
find_element_by_class_name
find_element_by_css_selector

To find multiple elements (these methods will return a list):
find_elements_by_name
find_elements_by_xpath
find_elements_by_link_text
find_elements_by_partial_link_text
find_elements_by_tag_name
find_elements_by_class_name
find_elements_by_css_selector

-------------------------------------------------------------
# Type in console
from selenium import webdriver
page = webbrowser.Chrome()
page.get('https://tst-05.test.intelliflo.com/nio/authentication/login')
page.find_element_by_css_selector('a[title="Login"]').click()
page.find_element_by_name('Username').send_keys('novdima')
page.find_element_by_name('Password').send_keys('testpass0')
page.find_element_by_css_selector('button[title="Login"]').click()
page.find_element_by_css_selector('a[title="Skip for now"]').click()
page.find_element_by_link_text('Ray Blow').click()

page.find_element_by_xpath('//a[contains(text(), "Fact Find")]').click()
page.find_element_by_xpath('//a[contains(text(), "Assets & Liabilities")]').click()
page.find_element_by_name('ff-grid-btn-add').click()
page.find_element_by_id('733_AssetCategoryId_0').click()
page.find_element_by_xpath('//option[contains(text(), "Boat")]').click()
page.find_element_by_xpath('//option[contains(text(), "Cash")]').click()
page.find_element_by_id('AssetDescription_Description_0').send_keys('Description')
page.find_element_by_id('128_Amount_0').send_keys('100')
page.find_element_by_css_selector('#ff-form-save').click()
assert page.find_element_by_css_selector('td.txtr.Amount').text == '100.00' 
page.find_element_by_name('ff-grid-btn-delete').click()
page.find_element_by_id('btnid_0').click()

page.quit()