# WebScraping
1) Aim of this project was to create a database of Indian movie celebrities with their images and personality traits.
2) Use https://astrolinked.com/ to get personality trait. This website has data about many celebrities including film starts, political leaders, cricketers etc.
3) extracted list personality traits.\\
['Celebrity', 'Adventurous', 'Ambitious', 'Analytical', 'Arrogant', 'Balanced', 'Broad-minded', 'Business-oriented', 'Careless', 'Cautious', 'Charming', 'Clever', 'Compassionate', 'Confident', 'Pronetoaddictions', 'Conservative', 'Courageous', 'Creative', 'Dependable', 'Pronetodepression', 'Detached', 'Diplomatic', 'Disciplined', 'Dominating', 'Downtoearth', 'Dreamer', 'Egoistic', 'Emotional', 'Enthusiastic', 'Erratic', 'Faithful', 'Focussed', 'Friendly', 'Frugal', 'Generous', 'Hard-working', 'Idealistic', 'Impatient', 'Impulsive', 'Independent', 'Innovative', 'Intelligent', 'Intuitive', 'Lazy', 'Leader', 'Lively', 'LovingandCaring', 'Manipulative', 'Materialistic', 'Meticulous', 'Moody', 'Nervous', 'Optimistic', 'Passionate', 'Patient', 'Perfectionist', 'Pessimistic', 'Philanthropic', 'Philosophical', 'Possessive', 'Practical', 'Reserved', 'Romantic', 'Secretive', 'Self-centred', 'Selfless', 'Shy', 'Soft-Spoken', 'Stubborn', 'Tactful', 'Tactless', 'Understanding', 'Versatile']
4) first column is the name of celebrity and other columns are 0 or 1. where 0 indicates that tarit absent and 1 means that trait is present.
## System requirements
1) python 3.6.9
2) selenium (https://pypi.org/project/selenium/)
3) webdriver (https://yizeng.me/2014/04/20/install-chromedriver-and-phantomjs-on-linux-mint/)
## Personality traits extraction
1) First, extracte valied urls using fetchurl.py files( it contain all type of celebrities)
2) Extract personality traits of all celebrities using main.py (saved in data.csv)
3) bollywood_actress_and_actors.txt file contain name of all bollywood actresses and actors (got from wiki). 
4) Using above file seperate bollywood celebrities from all celebrities (save in celebs_traits.csv)

## Download images of bollywood celebrities
1) Use download_images.py to download one image for each celebrities and save at dataset/celebritiesNAME.png
