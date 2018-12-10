# Topic: Instagram Account Type Prediction
 -- Galvanize Data Science Immersive Capstone Project (Dec 2018)



### Business Problem: 
![Slide_BusinessApplication](https://github.com/liyingli0818/instagram_account_type_predictor/blob/master/image/Slide_BusinessApplication.png)

Being one of the most popular social networking platform, instagram has attracted a lot of business corporations to advertise their product and make social impact. Sometimes for those businesses, for example E-Commerce companies, they want to have information on user’s marketing potentials when looking for Instagram influencers, however, they do not want to ignore those accounts that appear to be personal accounts but actually have noticeable marketing potentials. To help them gaining insights, I have developed a solution using machine learning models to predict Instagram Account Type (Business/Personal) based on user information and various types of account features.

### Data Preparation:
By assuming randomness, I scraped users information of followers under Instagram's official account (200 users to train Baseline model and increased to 2000 users for training my final model).
Created instagram.yaml file to store login informations on local machine (not in the project directory) and created automated login process. Therefore, next time if I am interested in followers information of another account (e.g. a particular e-commerce platform, celebrities/stars), there is no need to log in manually every time.

### Data Exploration:
![Slide_DataExploration](https://github.com/liyingli0818/instagram_account_type_predictor/blob/master/image/Slide_DataExploration.png)


### Data Preparation:
![Slide_DataPreparation](https://github.com/liyingli0818/instagram_account_type_predictor/blob/master/image/Slide_DataPreparation.png)
Web-scraping or api-scraping (api key)
Created a followers collection (fc) and stored json file (dict format) from "follower_urls" in Mongo DB
Get information on username, fullname, number of posts, number of followers, number of followings, is private or not, is business or not, is joined recently or not, etc. 
Manipulate data using python numpy, pandas. Clean out nan values and invalid values.



### Modeling:
Features: Number of posts, number of followers, number of followings, likes on last post, is_private, is_joined_recently, avg_likes_five_recent_posts (measures the average number of likes on users five most recent posts). 
All the number of likes features does not include video posts. 

Linear Regression
Random Forest
Best Random Forest (best parameters using grid search)



Check Beta values to see the correlation and perform statistical tests on it (e.g. calculate p-value to check if a feature significantly correlated with the predicted probability of business account). 


### Evaluation:
Use cross validation, k-fold to train model and get the results of log loss and roc.
Some afterwork treatment will be: give insights on those features, maybe suggest a company to look into which feature if it is strongly correlated to the engagement rate.
![roc.png](https://github.com/liyingli0818/instagram_account_type_predictor/blob/master/image/roc_after_add_avg5.png)



### Next Steps:
Business applications: Use the model to develop in product advertising and online marketing to find influencers that have high potential business marketing power. Actually looking into the account and demonstrate that the account has high potential marketing power (e.g. large number of followers, lots of Likes in each posts).
