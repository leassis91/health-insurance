<div align="center">

# 🏥🚗 HEALTH INSURANCE CROSS-SELL 🚗🏥

<img src="https://user-images.githubusercontent.com/67332395/192871886-1a546e1d-1330-40a0-a661-e1b71b8e0671.png" width=70% height=50% title="Health-Insurance-Ranking" alt="project_cover_image"/>

</div>

## 📖 Background

*The following context is completely fictional.*

Insurance All is a company that provides health insurance to its customers and the product team is analyzing the possibility of offering policyholders a new product: vehicle insurance. New customers of this product will pay an amount annually to Insurance All to obtain an amount insured by the company, intended at the costs of an eventual accident or damage to the vehicle.

Insurance All conducted a survey for over 380,000 customers about their interest in joining a new vehicle insurance product last year. The responses results were saved in a database along with other customer attributes.

<br>


## 📌 Problem Statement

*Ranking customers interested in purchasing vehicle insurance.*

The survey obtained feedback from 304,000 customers about their interest in purchasing vehicle insurance. The new insurance was developed and is being offered to the interested parties. However, there are more than 76,000 customers who did not respond to the survey. The already busy call center has the capacity to contact only 20,000 of these potential customers. Therefore, we need a list ordered by interest of these 76k customers, in order to optimize the company's conversion and revenue.


<br>

## 💾 Data Understanding

 ### - Tools Used:

* Python Version : 3.10
* Packages : Jupyter, Pandas, Numpy, Matplotlib, Seaborn, Scikit-Learn among others (please, check full list [here](https://github.com/leassis91/health-insurance/blob/master/requirements.txt))
* Coggle Mindmaps
* [SweetViz](https://pypi.org/project/sweetviz/)
* [Optuna](https://optuna.org/) - A hyperparameter optimization framework
* Frontend API: [Google Sheets Script](https://docs.google.com/spreadsheets/d/10Jjy_Iil6XGr7A3X0B3_fJEuFlBTCxRktnQhQkJh9Kg/edit#gid=862044370)
* Backend: Heroku

<br>

 ### - Importing Dataset:

* Kaggle: https://www.kaggle.com/datasets/anmolkumar/health-insurance-cross-sell-prediction or
* AWS PostgresSQL

<br>

 ### - Data Dictionary

| Variable                       | Descriptions                                                      |
| -------------------------------- | ------------------------------------------------------------ |
| Id                               | Unique customer identifier. |
| Gender                           | Customer's gender.                                   |
| Age                              | Customer's age.                             |
| Driving License                  | An indicator for whether a customer has a driving license.                      |
| Region Code                      | Customer's region code. |
| Previously Insured               | An indicator if a customer already had an auto insurance. |
| Vehicle Age                      | Customer's vehicle age. |
| Vehicle Damage                   | An indicator for whether a customer had previous damage in vehicle.  |
| Annual Premium                   | Total annual amount a customer pays for current health insurance. |
| Policy Sales Channel             | Anonymous code for a customer contact channel.          |
| Vintage                          | Number of days a customer was associated with the company through the purchase of health insurance. |
| Response                         | An indicator for auto insurance purchase.        |
 


<br>

 ### - Business Assumptions
 
Data Science team have to answer the following questions:

- What percentage of customers interested in purchasing auto insurance will the sales team be able to contact by making 20,000 calls?
- If the sales team capacity increases to 40,000 calls, what percentage of customers interested in purchasing auto insurance will the sales team be able to contact?
- How many calls does the sales team need to make to contact 80% of customers interested in purchasing auto insurance?


We have the following assumptions:

- policy sales channels used were SMS, e-mail and phone calls.
- all customers were above minimum drive age.


 
 <br>
 
## 🧾 Evaluation Metric

Here, we are mostly using the AUC-ROC curve to evaluate our models. ROC is a probability curve and AUC represents the degree or measure of separability.
The ROC curve is plotted with TPR (True Positive Rate) against the FPR (False Positive Rate) where TPR is on the y-axis and FPR is on the x-axis. 

<div align="center">

![auc](/image/AUC-ROC.jpg)

![tpr](/image/TPR.jpg)

![fpr](/image/FPR.jpg)

</div>

<br>

## 🔬 Solution Approach

The approach used to solve this task was done by applying CRISP-DM¹ methodology, which was divided in the following parts:

1. **Data Description:** understanding of the status of the database and dealing with missing values properly. Basic statistics metrics furnish an overview of the data.  
2. **Feature Engineering:** derivation of new attributes based on the original variables aiming to better describe the phenomenon that will be modeled, and to supply interesting attributes for the Exploratory Data Analysis.
3. **Feature Filtering:** filtering of records and selection of attributes that do not contain information for modeling or that do not match the scope of the business problem.
4. **Exploratory Data Analysis (EDA):** exploration of the data searching for insights and seeking to understand the impact of each variable on the upcoming machine learning modeling.
5. **Data Preparation:** preprocessing stage required prior to the machine learning modeling step.
6. **Feature Selection:** selection of the most significant attributes for training the model.
7. **Machine Learning Modeling:** implementation of a few algorithms appropriate to the task at hand. In this case, models befitting the *regression* assignment - *i.e.*, forecasting a continuous value, namely sales.
8. **Hyperparameter Fine Tuning:** search for the best values for each of the parameters of the best performing model(s) selected from the previous step.
9. **Statistical Error Analysis:** conversion of the performance metrics of the Machine Learning model to a more tangible business result.
10. **Production Deployment:** deployment of the model in a cloud environment (Heroku), using Flask connected to our model in a pickle file.
11. **Google Sheets Script** show our business results with some customers example in a Google Sheets. Check out at "Deployment" section.

<br>

## 🕵🏽‍♂️ Exploratory Data Analysis & Main Insights

### Hypothesis Creation Map

<img src="https://user-images.githubusercontent.com/67332395/193338010-3cb13048-a011-4940-a8e8-f20886786e1c.png" width=65% height=60%/>


### - Numerical Attributes Correlation

<img src="https://user-images.githubusercontent.com/67332395/193337884-7b66c5b9-e569-48c6-ba83-c4ade9b95585.png" width=55% height=55%/>


### - Categorical Attributes Correlation

<img src="https://user-images.githubusercontent.com/67332395/193337934-2974b53f-f9f9-4f8c-a968-da3557cf9adf.png" width=60% height=60%/>


### - Main Insights

Insights are information that are new or that break beliefs previously established of the business team. They are also actionable, enabling action to drive future results.

- **Hypothesis 1:** *Higher interest in FEMALE customers.*

A: False. We could observe a significant higher interest in male customers.

<img src='https://user-images.githubusercontent.com/67332395/193344924-c9aa476c-c194-4093-b6f8-d548b5be0d98.png' width=80% height=80%/>


- **Hypothesis 2:** *Higher interest in customers who had VEHICLE PREVIOUSLY DAMAGED.*

A: True. Almost no one who didn't have your vehicle damaged having any interest in a insurance.

<img src='https://user-images.githubusercontent.com/67332395/193345025-13958da5-296c-4eb4-a275-65b2aae3e790.png' width=80% height=80%/>

   
- **Hypothesis 3:** *Higher interest in LONGER CUSTOMERS.*

A: False. Interets didn't show any correlation between old clients.

<img src="https://user-images.githubusercontent.com/67332395/193345395-5e29d52d-a624-450e-ab15-7ecff7eb9300.png" width=80% height=80%/>

<br>

## 💻 Machine Learning Modeling & Evaluation

For measuring the performance of the models we will use the cross-validation method which prevents the model from overfitting when the model receives some data that he has never seen before. The @K for the metrics of Ranking-To-Learn approach is 20.000 and will better explained in the business results in the next section.

|Model Name				|Accuracy Balanced  |Precision @K Mean	|Recall @K Mean |	ROC AUC Score	|Top K Score|
|	:---:					|			:--:		|			:--:		|			:--:	|		:--:			|		:--:	|
|**LGBM Classifier**		|	0.501066	|0.307935	|	**0.828112**	| **0.853336**	|0.877706|
|**Cat Boost Classifier**		|	0.507893	| 0.305995	|	**0.822895**	| **0.850966**	|0.876744|
|**XGB Classifier**			|	0.511982		|	0.305255		|	**0.820905**	|	**0.849166**		|0.876341	|
|**Random Forest Classifier**	|	0.542660		|	0.289416		|	**0.778310**	|	0.829445		|0.865662	|
| GaussianNB 			|	0.783939		|	0.288646		|	0.776239	|	0.825829		| 0.637886	|
| Logistic Regression		|	0.500000		|	0.274926		|	0.739344	|	0.817501		| 0.878030	|
| K-Nearest Neighbors Classifier	|	0.557291		|	0.268607	    |	0.722349	|	0.752549	| 0.856038 |

In all scenarios, LGBM, CatBoost and XGBoost Classifiers had the best performance, so we chose the model with best size-speed ratio: LGBM model. Then, we proceeded to the Hyperparameter Fine-Tuning step, using Optuna Framework. 

|Model Name|Recall @K Mean |ROC AUC	|Top @K Acc|
|--: |--:| --:|
|LGBM Classifier Tuned | 0.827252	| 0.852081 |	0.877505 |

*Note that for this optimization we used "Recall" as metric to better find positive interested customers.*

<br>

## 📉 Business Performance

<br>

## 💡 Conclusions

in progress

<br>

## 👣 Next steps

in progress

<br>

## 🚀 Deployment

[<img alt="Google Sheets" src="https://img.shields.io/badge/Google%20Sheets-34A853?style=for-the-badge&logo=google-sheets&logoColor=white"/>](https://docs.google.com/spreadsheets/d/10Jjy_Iil6XGr7A3X0B3_fJEuFlBTCxRktnQhQkJh9Kg/edit#gid=862044370)

![scorevideo](https://github.com/leassis91/health-insurance/blob/main/image/score-sheets.gif)


*If you can't see properly, right-click on gif and "Open in a new tab" and try to zoom in and have a better visualization.*

<br>

## 🔗 References

1. Data Science Process Alliance - [What is CRISP-DM](https://www.datascience-pm.com/crisp-dm-2/)
2. in progress


<br>

If you have any other suggestion or question, feel free to contact me via [LinkedIn](https://linkedin.com/in/leandrodestefani).

<br>

## ✍🏽 Author

- [Leandro Destefani](https://github.com/leassis91)

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/leandrodestefani) [![gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:leassis.destefani@gmail.com) [![kaggle](https://img.shields.io/badge/Kaggle-3776AB?style=for-the-badge&logo=Kaggle&logoColor=white)](https://kaggle.com/leandrodestefani)

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)

***

## 💪 How to contribute

1. Fork the project.
2. Create a new branch with your changes: `git checkout -b my-feature`
3. Save your changes and create a commit message telling you what you did: `git commit -m" feature: My new feature "`
4. Submit your changes: `git push origin my-feature`



***
