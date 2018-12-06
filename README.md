# Topic: Instagram Account Type Prediction
Galvanize Data Science Immersive Capstone Project (Dec 2018)


### Business Understanding: 
Being one of the most popular social networking platform, instagram has attracted a lot of business corporations to advertise their product and make social impact. Sometimes for those businesses, for example E-Commerce companies, they want to have information on user’s account status when they are looking for instagram influencers, however, they do not want to ignore those accounts that appear to be personal accounts but actually has potential business power. To help them gaining insights, I have developed a solution using machine learning models to predict Instagram Account Type (Business/Personal) based on user information and various types of account features.

### Data Availability:
By assuming randomness, I scraped users information of followers under Instagram's official account (200 users to train Baseline model and increased to 2000 users for training my final model).
Created instagram.yaml file to store login informations on local machine (not in the project directory) and created automated login process. Therefore, next time if I am interested in followers information of another account (e.g. a particular e-commerce platform, celebrities/stars), there is no need to log in manually every time.


### Data Preparation:
Web-scraping or api-scraping (api key)
Created a followers collection (fc) and stored json file (dict format) from "follower_urls" in Mongo DB
Get information on username, fullname, number of posts, number of followers, number of followings, is private or not, is business or not, is joined recently or not, etc. 
Manipulate data using python numpy, pandas. Clean out nan values and invalid values.



### Modeling:
Generated Features:ratio of number of followings to number of followers

Linear Regression
Random Forest
Best Random Forest (best parameters using grid search)

Build models on the users information. The features can be the number of posts of a particular account, its number of followers, and the average number of account it follows on a daily basis.


Check Beta values to see the correlation and perform statistical tests on it (e.g. calculate p-value to check if a feature significantly correlated with the predicted probability of business account). 


### Evaluation:
Use cross validation, k-fold to train model based on couple of features and get the results of beta’s and log loss.
Some afterwork treatment will be: give insights on those features, maybe suggest a company to look into which feature if it is strongly correlated to the engagement rate.


At the end, I plan to have a website that user can input a instagram username and get insights on their account analysis.



### Deployment and Next Steps:
Show examples in presentation.
Find a particular account that get a high prediction in being business account from my model, however, it is actually not a business account.
Business applications: Use the model to develop in product advertising and online marketing to find influencers that have high potential business power.


Minimal viable product will be a presentation slides that includes the methods and model evaluation and the regression results and the analysis of features. Actually looking into the account and demonstrate that the account has high potential marketing power (e.g. large number of followers, lots of Likes in each posts).
