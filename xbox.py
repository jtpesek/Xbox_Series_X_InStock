from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
import time
from multiprocessing import Process
import smtplib
from selenium.webdriver.chrome.options import Options

options = Options()
# uncomment to to run headless mode
#options.add_argument('--headless')

# Email Variables
# your Gmail email that will be sending the email
gmail_email = ''
# Must set up a password for a scipt to login ( google somewhere)
gmail_password = ''
# Email Address you want to get the alerts - Recommend iCloud email so you can get instant push notifications
to_email =''


# Chrome variables
#Chromedriver path
cpath = r''
driver = webdriver.Chrome(cpath,options=options)

def send_email(site,url):

   with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
       smtp.ehlo()
       smtp.starttls()
       smtp.ehlo()

       smtp.login(gmail_email,gmail_password)
       subject = 'Xbox In Stock'
       body = 'Xbox is in stock at ....' + str(site) + '\nURL = ' + url

       msg = f'Subject: {subject}\n\n{body}'
       smtp.sendmail(gmail_email, to_email, msg)


def BestBuy():
    url = r'https://www.bestbuy.com/site/microsoft-xbox-series-x-1tb-console-black/6428324.p?skuId=6428324'
    driver.get(url)
    while True:
        try:
           time.sleep(5)
           driver.find_element(By.XPATH, "//div[@class='v-m-top-m v-p-top-m v-border v-border-top'][contains(.,'Coming Soon')]")
           print('Xbox Out of Stock at BestBuy')
           driver.refresh()
        except NoSuchElementException:
            print('Xbox Series X in Stock @ BestBuy!')
            print('Getting the web address')
            web_address = driver.current_url
            send_email('BestBuy', web_address)
            print('Email Sent')
            break



def Amazon():
    url = r'https://www.amazon.com/Xbox-X/dp/B08H75RTZ8/ref=sr_1_1?dchild=1&keywords=xbox+series+x&qid=1601774210&sr=8-1'
    driver.get(url)
    while True:
        try:
           time.sleep(5)
           driver.find_element(By.XPATH, "//div[@id='availability']/span[@class='a-size-medium a-color-price'][contains(.,'Currently unavailable')]")
           print('Xbox Out of Stock at Amazon')
           driver.refresh()
        except NoSuchElementException:
            print('Xbox Series X in Stock @ Amazon!')
            print('Getting the web address')
            web_address = driver.current_url
            send_email('Amazon', web_address)
            print('Email Sent')
            break

def Target():
    url = r'https://www.target.com/p/xbox-series-x-console/-/A-80790841'
    driver.get(url)
    while True:
        try:
           time.sleep(5)
           driver.find_element(By.XPATH, "//div[@class='h-text-md h-text-grayDark'][contains(.,'Preorders have sold out. Check back on release date')]")
           print('Xbox Out of Stock at Target')
           driver.refresh()
        except NoSuchElementException:
            print('Xbox Series X in Stock @ Target!')
            print('Getting the web address')
            web_address = driver.current_url
            send_email('Target', web_address)
            print('Email Sent')
            break

def GameStop():
    url = r'https://www.gamestop.com/video-games/xbox-series-x/consoles/products/xbox-series-x/11108371.html' \
          r'?condition=New&utm_expid=.cxvp7jeuRNKc9QoJTI6kMQ.0&utm_referrer=https%3A%2F%2Fwww.gamestop.com%2' \
          r'Fsearch%2F%3Fq%3Dxbox%2Bseries%2Bx%2B%26lang%3Ddefault'
    driver.get(url)
    while True:
        try:
           time.sleep(5)
           driver.find_element(By.XPATH, "//button[contains(.,'Not Available')]")
           print('Xbox Out of Stock at GameStop')
           driver.refresh()
        except NoSuchElementException:
            print('Xbox Series X in Stock @ GameStop!')
            print('Getting the web address')
            web_address = driver.current_url
            send_email('GameStop', web_address)
            print('Email Sent')
            break



if __name__ == '__main__':
    p1 = Process(target=BestBuy)
    p1.start()
    p2 = Process(target=Amazon)
    p2.start()
    p3 = Process(target=Target)
    p3.start()
    # Having an issue with GameStop. Getting false positives due to poor site loading
    p4 = Process(target=GameStop)
