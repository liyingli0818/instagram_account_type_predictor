# capstone_project
Galvanize Data Science Immersive Capstone Project

## Topic: Instagram Fake Followers Detector 

### Business Understanding: 
Being one of the most popular social networking platform, instagram has always been troubled with fraud/robot account and private commercial account, which has a significant negative effect on their users experience as well. This issue also points us to develop a solution to detect those account or notify their users about the suspicious of an abnormal account.

### Data Availability:
Scraping from instagram api.



### Data Preparation:
Web-scraping or api-scraping (api key)
Leave private accounts aside
Natural language processing
Manipulate data using python numpy, pandas. Clean out nan values and invalid values.

### Modeling:
feature:ratio/followers
Knn
Random forest
Build models on the users information. The features can be number of posts of a particular account, its number of followers, and the average number of account it follows on a daily basis.

### Evaluation:
Probability of: fake (1) or not_fake (0)
Use cross validation, k-fold to train model and make prediction based on couple of features and get the results of if an account is fake or not. 
Some afterwork treatment will be: give warning on those account, or just forced close the accounts for a certain amount of time.
At the end, I plan to have a website that user can input a instagram username, and if that user has few posts but a lot of followers, it is likely a robot account.


### Deployment:
Show examples in presentation.
Website that user can input a instagram username and test it out.
Minimal viable product will be a presentation slides that includes the methods and model evaluation and the prediction results.
