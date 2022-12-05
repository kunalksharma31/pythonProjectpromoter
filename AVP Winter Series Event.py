import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(executable_path="D:\\Seleinum Project\\AVP Promoter\\chromedriver.exe")

print(type(driver))
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://promoter.applination.in/")

myPageTitle = driver.title
print(myPageTitle)

# Login user id
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[4]/div[1]/input").send_keys("kaushiki@applination.in")
# Password
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[4]/div[2]/input").send_keys("123456")
# Login Button click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[4]/div[3]").click()
time.sleep(2)
driver.execute_script("window.scrollBy(0,2000)","")

# Ongoing Event
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[4]/div/div[1]/div[2]/a").click()
# time.sleep(100)

# Back to dashboard click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div[2]/button[1]").click()

# Upcoming Match
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[4]/div/div[2]/div[2]/a").click()
# time.sleep(10)
# Recently created
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[4]/div/div[3]/div[2]/a").click()
# time.sleep(20)

# New Tournament click
# driver.execute_script("window.scrollTo({},{});".format(0, 1000))
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[5]/div[2]/div[1]/div[2]").click()
time.sleep(2)
# New Event
driver.execute_script("window.scrollTo({},{});".format(0, 200))
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[1]/div/div/div[2]/div[1]/div[2]/div/div[1]/input").send_keys("AVP Winter Series")
## Event AVP Tour series ####
time.sleep(1)

# Add Photo
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/label").click()
time.sleep(1)
# Event Subtitle
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[1]/div/div/div[3]/div[2]/div/div/textarea").send_keys("AVP Live Event")
time.sleep(1)
# Address
# Hamburger Button click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[1]/div/div/div[4]/div[1]/div/div[3]/a/div/img").click()
time.sleep(2)
# click address and enter zip code
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[1]/div/div/div[4]/div[1]/div/div[3]/a/div/span/div[1]/div[2]/input").send_keys("90002")
time.sleep(2)
# click to choose zip code
driver.execute_script("window.scrollTo({},{});".format(0, 200))
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[1]/div/div/div[4]/div[1]/div/div[3]/a/div/span/div[2]/div[2]").click()
time.sleep(2)
# click on save to List address
# time.sleep(5)
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[1]/div/div/div[4]/div[3]/div[2]/label/span[2]").click()

# Date
# click on Start Date icon
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[5]/div[2]/div/div[3]/div/div").click()
time.sleep(1)
# Start date calender icon click
# driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[5]/div[2]/div/div[3]/div/div/span").click()
# time.sleep(1)
# start date 22 nov click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[1]/div[2]/table/tbody/tr[4]/td[3]/div").click()
time.sleep(1)

# End date icon click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[1]/div/div/div[5]/div[3]/div/div[3]/div/div").click()
time.sleep(1)

# End date  24 calender click
driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div[1]/div[2]/table/tbody/tr[4]/td[5]/div").click()
time.sleep(2)
# closed on  icon click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[1]/div/div/div[5]/div[4]/div/div[3]/div/div").click()
time.sleep(1)

# closed on  15 calender click
driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div/div/div[1]/div[2]/table/tbody/tr[3]/td[3]/div").click()
## driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[5]/div[5]/div/div[3]/div/div").click()

time.sleep(2)
# Early bid icon click
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[5]/div[5]/div/div[3]/div/div").click()
time.sleep(1)

# Early bid  13 calender click
driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/div/div[1]/div[2]/table/tbody/tr[3]/td[1]/div").click()
time.sleep(1)
# Time Start icon click
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[6]/div[2]/div/div[3]/div/div").click()
time.sleep(2)
# Time Hrours click
driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div/div[1]/div/ul[1]/li[4]/div").click()
driver.execute_script("window.scrollTo({},{});".format(0, 200))
time.sleep(2)
# Time Second click
driver.execute_script("window.scrollTo({},{});".format(0, 200))
driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div/div[1]/div/ul[2]/li[6]/div").click()
time.sleep(1)
# Time AM/PM
driver.execute_script("window.scrollTo({},{});".format(0, 200))
driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div/div[1]/div/ul[3]/li[2]/div").click()
time.sleep(1)
# ok Button
driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div/div[2]/ul/li[2]/button").click()
time.sleep(1)
# Now Time click
# driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div/div[2]/ul/li[1]/a").click()
# time.sleep(200)


# Division + Button click
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[7]/div[1]/img").click()
time.sleep(1)
# Click Template icon Button
driver.find_element(By.XPATH, "/html/body/div[7]/div/div[2]/div/div/div/div/div/form/div[1]/div/a/div/img").click()
time.sleep(2)

driver.execute_script("window.scrollTo({},{});".format(0, 1000))
# Division Name 18TeamsOpen Open A
driver.find_element(By.XPATH, "/html/body/div[7]/div/div[2]/div/div/div/div/div/form/div[1]/div/a/div/span/ul/li[21]").click()
time.sleep(1)
# Division name done click
driver.find_element(By.XPATH, "/html/body/div[7]/div/div[2]/div/div/div/div/div/form/div[2]/div/div/button").click()
time.sleep(1)

'''# Template New button click
driver.find_element(By.XPATH, "/html/body/div[7]/div/div[2]/div/div/div/div/div/form/div[2]/button[2]/span").click()
time.sleep(2)
# Division Template choose and click
driver.execute_script("window.scrollTo({},{});".format(0, 200))
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/a/div/span/ul/li[3]").click()
time.sleep(2)
## Division Template choose  and Next Button click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[2]/button[2]/span").click()
time.sleep(1)
# Choose Age of Bracket  icon click
driver.find_element(By.XPATH, "/html/body/div[7]/div/div[2]/div/div/div/div/div/form/div[1]/div/div/a/div/img").click()
time.sleep(3)
# Choose age of bracket -> Adult click
driver.find_element(By.XPATH, "/html/body/div[7]/div/div[2]/div/div/div/div/div/form/div[1]/div/div/a/div/span/ul/li[1]").click()
time.sleep(3)
# Choose age of bracket -> Adult -> Next Button click
driver.find_element(By.XPATH, "/html/body/div[7]/div/div[2]/div/div/div/div/div/form/div[2]/button[2]/span").click()
time.sleep(3)
# Gender group(s) are needed for this Division? Male click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div/form/div[1]/div/label[1]/input").click()
time.sleep(3)
# Gender group(s) are needed for this Division? Male -> Next button click
driver.find_element(By.XPATH, "/html/body/div[7]/div/div[2]/div/div/div/div/div/form/div[2]/button[2]/span").click()
time.sleep(1)
# What is the age range needed for this Division? 35+
# driver.find_element(By.XPATH, "/html/body/div[7]/div/div[2]/div/div/div/div/div/form/div[1]/div/div[3]/label[1]/input").click()
time.sleep(1)'''
'''# What is the age range needed for this Division? 35+ ->Next Button click
driver.find_element(By.XPATH, "/html/body/div[7]/div/div[2]/div/div/div/div/div/form/div[2]/button[2]/span").click()
time.sleep(1)
#### 2 Skills taken
# skill level needed for this Division? Open
driver.find_element(By.XPATH, "/html/body/div[7]/div/div[2]/div/div/div/div/div/form/div[1]/div/div[1]/label[2]/input").click()
time.sleep(1)
# skill level needed for this Division? A
driver.find_element(By.XPATH, "/html/body/div[7]/div/div[2]/div/div/div/div/div/form/div[1]/div/div[2]/label[1]/input").click()
time.sleep(1)
# skill level needed for this Division? Open and A -> Next button click
# driver.find_element(By.XPATH, "/html/body/div[7]/div/div[2]/div/div/div/div/div/form/div[2]/button[2]/span").click()
# time.sleep(1)
# Total no. of teams in this division icon click
# driver.find_element(By.XPATH, "/html/body/div[7]/div/div[2]/div/div/div/div/div/form/div[1]/div/div/a/div/img").click()
# time.sleep(1)
# driver.execute_script("window.scrollTo({},{});".format(0, 2000))
# Total no. of teams in this division 21 Teams   click
# driver.find_element(By.XPATH, "/html/body/div[7]/div/div[2]/div/div/div/div/div/form/div[1]/div/div/a/div/span/ul/li[18]").click()
# time.sleep(1)
# Total no. of teams in this division 21 Teams -> Next Button  click
# driver.find_element(By.XPATH, "/html/body/div[7]/div/div[2]/div/div/div/div/div/form/div[2]/button[2]/span").click()
# time.sleep(1)
# Players per team click icon
# driver.find_element(By.XPATH, "/html/body/div[7]/div/div[2]/div/div/div/div/div/form/div[1]/div/div/a/div/img").click()
# time.sleep(1)
# Players per team click 2v2
# driver.find_element(By.XPATH, "/html/body/div[7]/div/div[2]/div/div/div/div/div/form/div[1]/div/div/a/div/span/ul/li[1]").click()
# time.sleep(1)
# Players per team click 2v2 -> Next Button click
# driver.find_element(By.XPATH, "/html/body/div[7]/div/div[2]/div/div/div/div/div/form/div[2]/button[2]/span").click()
# time.sleep(1)
# Discount Section Next button click
# driver.find_element(By.XPATH, "/html/body/div[7]/div/div[2]/div/div/div/div/div/form/div[3]/button[2]/span").click()
# time.sleep(1)
# Will these Divisions need an Early Bird entry? No click
# driver.find_element(By.XPATH, "/html/body/div[7]/div/div[2]/div/div/div/div/div/form/div[1]/div/label[2]/input").click()
# time.sleep(1)
# Will these Divisions need an Early Bird entry? No -> Next Button click
# driver.find_element(By.XPATH, "/html/body/div[7]/div/div[2]/div/div/div/div/div/form/div[2]/button[2]/span").click()
# time.sleep(1)
# Normal Entry Send keys $700
# driver.find_element(By.XPATH, "/html/body/div[7]/div/div[2]/div/div/div/div/div/form/div[1]/div/div[1]/input").send_keys("$700")
# time.sleep(3)
# Normal Entry Send keys Click Next Button
# driver.find_element(By.XPATH, "/html/body/div[7]/div/div[2]/div/div/div/div/div/form/div[2]/button[2]/span").click()
# time.sleep(2)
# Late Entry $900 send keys
# driver.find_element(By.XPATH, "/html/body/div[7]/div/div[2]/div/div/div/div/div/form/div[1]/div/div[1]/input").send_keys("$900")
# time.sleep(3)
# Late Entry $900 Next Button click
# driver.find_element(By.XPATH, "/html/body/div[7]/div/div[2]/div/div/div/div/div/form/div[2]/button[2]/span").click()
# time.sleep(1)
# Division Template Name click 21Teams 35+ Open A
# driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div/form/div[1]/label/input").click()
# time.sleep(1)
# Division Template Name  21Teams 35+ Open A  send key
# driver.find_element(By.XPATH, "/html/body/div[7]/div/div[2]/div/div/div/div/div/form/div[1]/label[1]/input").send_keys("21Teams 35+ Open A ")
# #ime.sleep(3)
# # Division Template Name  21Teams 35+ Open A -> save button click
# driver.find_element(By.XPATH, "/html/body/div[7]/div/div[2]/div/div/div/div/div/form/div[1]/div/button").click()
time.sleep(200)'''

# driver.execute_script("window.scrollTo({},{});".format(0, 200))

# Tournament Format
# Select Tournament Format icon click
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[8]/div[2]/div/div/div[4]/a/div").click()
time.sleep(1)
# Select Tournament Format Regular click
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[8]/div[2]/div/div/div[4]/a/div/span/ul/li[1]").click()
time.sleep(1)
# driver.execute_script("window.scrollTo({},{});".format(0, 200))
# Registration Cap * icon click
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[9]/div[2]/div/div/div[3]/div[2]/a/div/img").click()
time.sleep(1)
# Registration Cap *  Yes choose and click
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[9]/div[2]/div/div/div[3]/div[2]/a/div/span/ul/li[1]").click()
time.sleep(1)
# Ends At * click icon
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[9]/div[3]/div/div[3]/div/div").click()
time.sleep(1)
# Ends At * click 4 Hr
driver.find_element(By.XPATH, "/html/body/div[7]/div/div/div/div/div[1]/div/ul[1]/li[5]/div").click()
time.sleep(1)
# Ends At * click 01 Minutes
driver.find_element(By.XPATH, "/html/body/div[7]/div/div/div/div/div[1]/div/ul[2]/li[2]/div").click()
time.sleep(1)
# Ends At * click PM
driver.execute_script("window.scrollTo({},{});".format(0, 200))
driver.find_element(By.XPATH, "/html/body/div[7]/div/div/div/div/div[1]/div/ul[3]/li[2]/div").click()
time.sleep(1)
# Ends ok button click
driver.find_element(By.XPATH, "/html/body/div[7]/div/div/div/div/div[2]/ul/li[2]/button/span").click()
time.sleep(1)
# Number of sets * click icon
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[9]/div[4]/div/div/div[3]/div[2]/a/div/img").click()
time.sleep(1)
# Number of sets * 3 click
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[9]/div[4]/div/div/div[3]/div[2]/a/div/span/ul/li[3]").click()
time.sleep(1)
# Match Time * click icon
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[9]/div[5]/div/div/div[3]/div[2]/a/div/img").click()
time.sleep(1)
# Match Time * click 60 min
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[9]/div[5]/div/div/div[3]/div[2]/a/div/span/ul/li[2]").click()
time.sleep(1)
# Max points per set 21 By default send key
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[9]/div[6]/div/div[3]/input").send_keys("21")
time.sleep(1)
# Number of playoffs * click icon
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[9]/div[7]/div/div/div[3]/div[2]/a/div/img").click()
time.sleep(1)
# Number of playoffs * click choose 1
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[9]/div[7]/div/div/div[3]/div[2]/a/div/span/ul/li[1]").click()
time.sleep(1)
# Show Registration * click icon
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[9]/div[8]/div/div/div/div[3]/div[2]/a/div/img").click()
time.sleep(1)
# Show Registration * click
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[9]/div[8]/div/div/div/div[3]/div[2]/a/div/span/ul/li[1]").click()
time.sleep(1)

# Details
# Pools * click icon
driver.execute_script("window.scrollTo({},{});".format(0, 1400))
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[10]/div[2]/div/div/div[4]/a/div/img").click()
time.sleep(1)
# Pools *  7Teams3Pool3 Courts click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[1]/div/div/div[10]/div[2]/div/div/div[4]/a/div/span/ul/li[22]").click()
time.sleep(1)
# Season * icon click
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[10]/div[3]/div/div/div[4]/a/div/img").click()
time.sleep(1)
# Season *  choose Tournament Season click
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[10]/div[3]/div/div/div[4]/a/div/span/ul/li[1]").click()
time.sleep(1)
# Placement Points * icon click
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[10]/div[4]/div/div/div[4]/a/div/img").click()
time.sleep(1)
# Placement Points * AVPNext Gold choose  click
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[10]/div[4]/div/div/div[4]/a/div/span/ul/li[2]").click()
time.sleep(1)
# Seeding Method * icon click
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[10]/div[5]/div/div/div[4]").click()
time.sleep(1)
# Seeding Method * Tournament Seeding click
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[10]/div[5]/div/div/div[4]/a/div/span/ul/li[1]").click()
time.sleep(1)
# Surface Type * icon click
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[10]/div[6]/div/div/div[4]").click()
time.sleep(1)
# Surface Type * optional to choose Sand click
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[10]/div[6]/div/div/div[4]/a/div/span/ul/li[1]").click()
time.sleep(1)
# Host Clinic * icon click
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[10]/div[7]/div/div[4]").click()
time.sleep(1)
# Host Clinic * yes click
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[10]/div[7]/div/div[4]/a/div/span/ul/li[1]").click()
time.sleep(1)
# Show Entries * icon click
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[10]/div[8]/div/div[4]/a/div/img").click()
time.sleep(1)
# Show Entries * Yes click
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[10]/div[8]/div/div[4]/a/div/span/ul/li[1]").click()
time.sleep(1)
# Team Listing icon click
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[10]/div[9]/div/div/div[4]/a/div/img").click()
time.sleep(1)
# Team Listing * By Ranking Points click
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[10]/div[9]/div/div/div[4]/a/div/span/ul/li[1]").click()
time.sleep(1)
driver.execute_script("window.scrollTo({},{});".format(0, 1600))

# Contact:
# Director * icon click
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[11]/div[2]/div/div[4]/a/div/img").click()
time.sleep(1)
# Director * Kunal Kumar  click
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[11]/div[2]/div/div[4]/a/div/span/div[11]/div[2]").click()
time.sleep(1)
# Main Contact * click icon
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[11]/div[3]/div/div[4]/a/div/img").click()
time.sleep(1)
# Main Contact * Kaushiki Applination click
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[11]/div[3]/div/div[4]/a/div/span/div[2]/div[2]").click()
time.sleep(1)

driver.execute_script("window.scrollTo({},{});".format(0, 1900))
# Finance
# Online Pay * icon click
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[12]/div[2]/div/div[3]/div[2]/a/div/img").click()
time.sleep(2)
# Online Pay * Yes click
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[12]/div[2]/div/div[3]/div[2]/a/div/span/ul/li[1]").click()
time.sleep(1)
# Purse Amount * icon click
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[12]/div[3]/div/div/div[4]/a/div/img").click()
time.sleep(1)
# Purse Amount * 499k-400k click
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[12]/div[3]/div/div/div[4]/a/div/span/ul/li[2]").click()
time.sleep(1)
# Purse Amount 20% Percent send key
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[12]/div[4]/div/div[3]/input").send_keys("20%")
time.sleep(1)
# Donation text for Flood send keys
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[12]/div[5]/div/div[3]/input").send_keys("Flood")
time.sleep(1)
# 1 Donation amount 1 10 Text $10
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[12]/div[6]/div/div[3]/input").send_keys("$10")
time.sleep(1)
# 1 Donation Amount 2 $5 send key
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[12]/div[7]/div/div[3]/input").send_keys("$5")
time.sleep(1)
# 3 Donation Amount 3 send key $4
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[12]/div[8]/div/div[3]/input").send_keys("$4")
time.sleep(1)
# Minimum Membership Requirement * icon click
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[12]/div[9]/div/div/div[4]/a/div/img").click()
time.sleep(1)
# Minimum Membership Requirement * Silver  click
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[12]/div[9]/div/div/div[4]/a/div/span/ul/li[2]").click()
time.sleep(1)

# Documents
# Signature Agreement * icon click
driver.execute_script("window.scrollTo({},{});".format(0, 2000))
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[13]/div[2]/div/div[4]/a/div/img").click()
time.sleep(1)
# Signature Agreement * Yes click
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[13]/div[2]/div/div[4]/a/div/span/ul/li[1]").click()
time.sleep(1)
# ScoreSheet * icon click
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[13]/div[3]/div/div/div[4]/a/div/img").click()
time.sleep(1)
# ScoreSheets  * Tournament Scoresheet click
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[13]/div[3]/div/div/div[4]/a/div/span/ul/li[1]").click()
time.sleep(1)
# PDF Instructions icon click
# driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[13]/div[4]/div/div[4]/label/img").click()
# time.sleep(3)
# Description * send keys
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[14]/div[3]/div/div/div").send_keys("AVP Event")
time.sleep(3)
driver.execute_script("window.scrollTo({},{});".format(0, 2400))
# Color Palette
# Choose Color click and choose colour icon
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[15]/div[2]/div/div[3]/div/div[2]/input").click()
time.sleep(2)
# Save of event click
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/button/span").click()
time.sleep(1)

# Go Live
# Hamberbage icon click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div/div[2]/a/div/img").click()
time.sleep(1)
# Go live option click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div/div[2]/a/div/span/ul/li[4]").click()
time.sleep(1)
# After go live -> registration open click on tool tip icon
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[1]/nav/div/div/ul[1]/li[2]").click()
time.sleep(1)
# After clicked on tool tip icon forward to add Team Page and Mens Open 35+ click on icon menu
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div/div/div/div[3]/div[1]/div/div/span/img").click()
time.sleep(1)

# driver.execute_script("window.scrollBy(0,200)","")
# Mens Open 35+ , Team 1-0  (+) icon click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div/div/div/div[3]/div[1]/div[2]/div/div[1]/div[1]/div[2]/img").click()
time.sleep(1)
# Mens open 35+ -> Open after team 1-0 icon click next page -> details Mens 35_ open -> division  -> click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div[1]/div/div/span/img").click()
time.sleep(1)

 ###Add Team ####
# 1 Team 1 player + icon click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div/img").click()
time.sleep(1)
# 1Team 1 Player search option click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div/span/div[1]/div[2]/input").click()
time.sleep(1)
# 1Team 1 Player search "a" option -> send key
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div/span/div[1]/div[2]/input").send_keys("a")
time.sleep(1)
# 1Team 1 Player search "a" option -> Richard Abiador, Bothell, WA -> click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div/span/div[2]/div[2]").click()
time.sleep(1)
# Donation
# Flood 40 click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[3]/div[3]/label/input").click()
time.sleep(1)
# Flood 40 -> Next button click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[5]/div/button[2]/span").click()
time.sleep(200)











































