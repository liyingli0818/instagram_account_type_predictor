# Instagram Fake Followers Detector
Galvanize Data Science Immersive Capstone Project (Dec 2018)

## Topic: Instagram Fake Followers Detector 

### Business Understanding: 
Being one of the most popular social networking platform, instagram has always been troubled with fraud/robot account and private commercial account, which has a significant negative effect on their users experience as well. Sometimes, when E-Commerce companies are looking for bloggers for the purpose of advertising, they should be aware that there are ways to buy followers. They really want to identify "bloggers" that have fake followers among all the bloggers that they are interested in partnering with. To resolve this types of problem, I developed a solution to use machine learning models in detecting those account with fake followers or notify their users about the suspicious of an abnormal account. 

### Data Availability:
Scraping followers informations from Instagram's official account.
Created instagram.yaml file to store login informations on local machine (not in the project directory), so that nexttime if I am interested in informations from another account (e.g. a particular e-commerce platform), there is no need to log in manually everytime.


### Data Preparation:
Web-scraping or api-scraping (api key)
Leave private accounts aside
Future: Natural language processing on the biography feature.
Manipulate data using python numpy, pandas. Clean out nan values and invalid values.
Generated y-value ('target') based on the engagement rates that I got from another website: 'https://hypeauditor.com/'.


### Modeling:
feature: generated a new feature called 'following_num_follower_ratio' which is basically the ratio of number of followings and number of followers, which turns out to have strong power in my prediction.

Knn

Logistic Regression

Random Forest

Build models on the users information. 

The features can be number of posts of a particular account, its number of followers, and the average number of account it follows on a daily basis.


### Evaluation:
Probability of: has fake (1) or does not have fake (0)
Make prediction on probabilities based on couple of features and get the results of if an account has fake followers or not. 

Use cross validation, k-fold and evaluated the models using log loss.

Some afterwork treatment will be: give warning to businesses that would like to partner with those account, or just give warning to those users directly. 

At the end, I plan to have a website that user can input a instagram username, and if that user has few posts but a lot of followers, or the follower increment is not consistent overtime, it is likely that the user has fake followers or has bought followers in the past.


### Deployment and Next Steps:
Show examples in presentation.
Website that user can input an instagram username and check if that instagram user has fake followers or not.

Minimal viable product will be a presentation slides that includes the methods and model evaluation and the prediction results.
