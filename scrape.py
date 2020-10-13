import time
import os


import smtplib
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
driver = webdriver.Chrome(executable_path='C:\webdrivers\chromedriver.exe')


#functions
#this function is used to remove all the non ascii characters so they dont cause problem while parsing
def remove_non_ascii(text):
    return ''.join([i if ord(i) < 128 else '' for i in text])


#this function will check whether the product is in stock or not
def court_system(body):
    span=body.find("span",{'class':'FirstColumnPrompt'})[0]
    data=span.text
    return data
def case_number(body):
    span=body.find("span",{'class':'FirstColumnPrompt'})[1]
    case_num=span.text
    return case_num
def case_status(body):
    span=body.find("span",{'class':'Prompt'})[0]
    case_status=span.text
    return case_status
def status_date(body):
    span=body.find("span",{'class':'FirstColumnPrompt'})[2]
    case_date=span.text
    return case_date
def tracking_number(body):
    span=body.find("span",{'class':'FirstColumnPrompt'})[3]
    track_=span.text
    return track_
def complaint_number(body):
    span=body.find("span",{'class':'FirstColumnPrompt'})[4]
    comp_num=span.text
    return comp_num
def dist_case_number(body):
    span=body.find("span",{'class':'FirstColumnPrompt'})[5]
    dist_case_num=span.text
    return dist_case_num
def filling_date(body):
    span=body.find("span",{'class':'FirstColumnPrompt'})[6]
    filling_date=span.text
    return filling_date
def incident_date(body):
    span=body.find("span",{'class':'Prompt'})[1]
    incident_date=span.text
    return incident_date

#taking url as input
url=input("Enter the url of the product page:\n")


driver=webdriver.Chrome('C:\webdrivers\chromedriver.exe')
driver.get(url)
time.sleep(5)
page=driver.page_source
driver.close()
soup=BeautifulSoup(page,'html.parser')
var=soup.find_all('span')
soup.find_element_by_name('disclaimer').click()
soup.find_element_by_xpath("//input[@value='Continue']").click()
print(var)
if not case_number:
    print('Case not available')
    
    
print('Case is available')

time.sleep(20)


type(var)
