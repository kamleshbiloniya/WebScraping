from selenium import webdriver 
import requests
import csv

##################### store all celebrities names in celebs list ##########
celebs = []
with open('data.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile)
    count =0
    for row in spamreader:
        celeb = row[0].replace(' ', '-').lower()
        if count==0:
            count +=1
            continue
        celebs.append(celeb)


################################### store all actors and actresses anem in data list #######
fp = open("bollywood_actress_and_actors.txt","r")
data = fp.read().strip().split("\n")
for i,name in enumerate(data):
    data[i] = name.replace(' ','-').lower()


################## only_celebs list stores name of all bollywood celebrities ######
only_celebs = []
for celeb in celebs:
    if celeb in data:
        only_celebs.append(celeb)



######################followong code download one image for each bollywood celebrity ####
browser = webdriver.Chrome('chromedriver') 
with open("valid_url.txt","r") as fp:
    urls = fp.read().strip().split('\n')
    for url in urls:
        if url.split('/')[-4] in only_celebs:
            print(url)
            browser.get(url) 
            time.sleep(5)
            celebrity_name = browser.find_element_by_css_selector('h3.native-name.show-for-medium-up').text.replace(' ','_')
            image = browser.find_element_by_xpath("//img[@class='native avatar']").get_attribute("src")
            response = requests.get(image)
            imgformat = image.split('.')[-1]
            file = open("dataset/"+str(celebrity_name)+"." + imgformat, "wb")
            file.write(response.content)
            file.close()