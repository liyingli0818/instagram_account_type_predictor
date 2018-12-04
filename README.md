# Topic: Instagram User Engagement Analysis
Galvanize Data Science Immersive Capstone Project (Dec 2018)


### Business Understanding: 
Being one of the most popular social networking platform, instagram has attracted a lot of business corporations to advertise their product and make social impact. Sometimes for those businesses, for example E-Commerce companies, want to gather insights on which features are correlated to a user’s account status when they are looking for instagram influencers. To resolve this type of problem, I developed a solution using machine learning models to provide insights on which features are correlated with low engagement rate. 

### Data Availability:
Scraping users informations from Instagram's official account followers.
Created instagram.yaml file to store login informations on local machine (not in the project directory) and created automated login process. Therefore, next time if I am interested in informations from another account (e.g. a particular e-commerce platform), there is no need to log in manually everytime.


### Data Preparation:
Web-scraping or api-scraping (api key)
Get information on username, fullname, number of posts, number of followers, number of followings, is private or not, is business or not, is joined recently or not. 
Manipulate data using python numpy, pandas. Clean out nan values and invalid values.
Obtained y-value ('target'), the engagement rates, from external website: 'https://hypeauditor.com/'.


### Modeling:
Feature:ratio on number of followings and number of followers


Linear Regression


Random forest


Build models on the users information. The features can be the number of posts of a particular account, its number of followers, and the average number of account it follows on a daily basis.


Check Beta values to see the correlation and perform statistical tests on it (e.g. calculate p-value to check if a feature significantly correlated with the engagement rate) . 


### Evaluation:
Use cross validation, k-fold to train model based on couple of features and get the results of beta’s and log loss.
Some afterwork treatment will be: give insights on those features, maybe suggest a company to look into which feature if it is strongly correlated to the engagement rate.


At the end, I plan to have a website that user can input a instagram username and get insights on their account analysis.



### Deployment and Next Steps:
Show examples in presentation.
Website that user can input a instagram username

Minimal viable product will be a presentation slides that includes the methods and model evaluation and the regression results and the analysis of features.
