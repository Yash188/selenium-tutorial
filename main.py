from selenium import webdriver

# creating driver objects if we want to use chrome use Chrome()
# for firefox use Firefox()
driver = webdriver.Chrome('F:\Installations\Chromium driver\chromedriver_win32\chromedriver.exe')

# get method is used to navigate to a url
driver.get("https://www.instagram.com/lucid.programmer/")

# the xpath copied from the browser
x_path = '//*[@id="react-root"]/section/main/div/header/section/div[1]/div/div/div/a'
follow_button = driver.find_element_by_xpath(x_path)

# it'll click on the follow_button after page loading
# is completed
follow_button.click()
