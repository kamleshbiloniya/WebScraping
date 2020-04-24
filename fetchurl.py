from selenium import webdriver
import time
import csv
import os



def getURL(url):
    global driver,valid_url

    driver.get(url)
    time.sleep(5)
    
    traits = driver.find_elements_by_css_selector('h6.caption.sub.ng-binding')
    celeb_name = driver.find_element_by_css_selector('h3.native-name.show-for-medium-up').text
    
    if len(traits) == 0:
        print(celeb_name,' Unable to Fetch')
    else:
        valid_url.append(driver.current_url)
        print(celeb_name,driver.current_url,sep=' ')
    
    
if __name__ == '__main__':
    valid_url =[]
    BASE_URL = 'https://astrolinked.com/native/'
    
    driver = webdriver.Chrome()
    actor_count = int(input('Enter the Range:'))
    for i in range(1,actor_count+1):
        try:
            getURL('{}/{}'.format(BASE_URL,i))
        except:
            print('Unexpected Error')

    with open('valid_url.txt','w') as file:
        file.writelines('\n'.join(valid_url))
        file.close