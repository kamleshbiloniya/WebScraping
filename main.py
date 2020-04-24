from selenium import webdriver
import datetime
import time
import csv
import os



def getTraitDetails(url):
    global driver,traits_dict,actors

    driver.get(url)
    time.sleep(5)

    celebrity_name = driver.find_element_by_css_selector('h3.native-name.show-for-medium-up').text
    actors.append(celebrity_name)
    traits = driver.find_elements_by_css_selector('label.ng-binding')

    for trait in traits:
        print(trait.text)
        
        traittext = trait.text.replace('*','').replace(' ','')
        if traittext not in traits_dict:
            traits_dict.update({traittext:[]})
        checkbox = trait.find_element_by_tag_name('input')

        if checkbox.get_property('checked') :
            traits_dict[traittext].append(celebrity_name)



if __name__ == '__main__':
    traits_dict={}
    actors = []
    driver = webdriver.Chrome()

    ############################
    with open("valid_url.txt","r") as fp:
        data = fp.read().strip().split('\n')
        for url in data:
            getTraitDetails(url)


    ##########################
    
    with open('data.csv','w', newline='') as datafile:
        csvdata = csv.writer(datafile)
        header = ['Celebrity'] + list(traits_dict.keys())
        csvdata.writerow(header)

        trait_keys = list(traits_dict.keys())
        
        for actor in actors:
            actor_list=[actor]
            for key in trait_keys:
                if actor in traits_dict[key]:
                    actor_list.append(1)
                else:
                    actor_list.append(0)
            csvdata.writerow(actor_list)

        datafile.close()
