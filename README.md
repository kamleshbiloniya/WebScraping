# WebScraping
1) Aim of this project was to create a database of Indian movie celebrities with their images and personality traits.
2) Use https://astrolinked.com/ to get personality trait. This website has data about many celebrities including film starts, political leaders, cricketers etc. 
## system requirements
1) python 3.6.9
2) selenium (https://pypi.org/project/selenium/)
3) webdriver (https://yizeng.me/2014/04/20/install-chromedriver-and-phantomjs-on-linux-mint/)
## personality traits extraction
1) First, extracte valied urls using fetchurl.py files( it contain all type of celebrities)
2) Extract personality traits of all celebrities using main.py (saved in data.csv)
3) bollywood_actress_and_actors.txt file contain name of all bollywood actresses and actors (got from wiki). 
4) Using above file seperate bollywood celebrities from all celebrities (save in celebs_traits.csv)

## Download images of bollywood celebrities
1) Use download_images.py to download one image for each celebrities and save at dataset/celebritiesNAME.png
