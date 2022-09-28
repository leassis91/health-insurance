<div align="center">

# 🏥🚗 HEALTH INSURANCE CROSS-SELL 🚗🏥

<img src="https://user-images.githubusercontent.com/67332395/192871886-1a546e1d-1330-40a0-a661-e1b71b8e0671.png" width=70% height=50% title="Health-Insurance-Ranking" alt="project_cover_image"/>

</div>

## 📖 Background

*The following context is completely fictional.*

Insurance All is a company that provides health insurance to its customers and the product team is analyzing the possibility of offering policyholders a new product: auto insurance.

As with health insurance, customers of this new auto insurance plan need to pay an amount annually to Insurance All to obtain an amount insured by the company, aimed at the costs of an eventual accident or damage to the vehicle.

Insurance All conducted a survey of about 380,000 customers about their interest in joining a new auto insurance product last year. All customers expressed interest or not in purchasing auto insurance and these responses were saved in a database along with other customer attributes.

The product team selected 127 thousand new customers who did not respond to the survey to participate in a campaign, in which they will receive the offer of the new auto insurance product. The offer will be made by the sales team through telephone calls.

However, the sales team has the capacity to make 20 thousand calls within the campaign period.

<br>


## 📌 Problem Statement

*Predicting whether or not the customer would be interested in auto insurance.*

<br>

## 💾 Data Understanding

 ### - Code Used:

* Python Version : 3.10
* Packages : Jupyter, Pandas, Numpy, Matplotlib, Seaborn, Scikit-Learn among others (please, check full list [here](https://github.com/leassis91/health-insurance/blob/master/requirements.txt))
* Frontend API: Google Sheets Script
* Backend: Heroku

<br>

 ### - Importing Dataset:

* Kaggle: https://www.kaggle.com/competitions/rossmann-store-sales/data

<br>

 ### - Data Dictionary

| Variable                       | Descriptions                                                      |
| -------------------------------- | ------------------------------------------------------------ |
| Id                               | An id that represents a (store, date) duple within the test set|
| Store                            | A unique id for each store                                   |
| Sales                            | The turnover for any given day                          |
| Customers                        | The number of customers on a given day                       |
| Open                             | An indicator for whether the store was open: 0 = closed, 1 = open |
| Stateholiday                     | Indicates a state holiday. Normally all stores, with few exceptions, are closed on state holidays. Note that all schools are closed on public holidays and weekends. A = public holiday, b = easter holiday, c = christmas, 0 = none |
| Schoolholiday                    | Indicates if the (store, date) was affected by the closure of public schools |
| Storetype                        | Differentiates between 4 different store models: a, b, c, d  |
| Assortment                       | Describes an assortment level: a = basic, b = extra, c = extended |
| Competitiondistance              |Distance in meters to the nearest competitor store           |
| Competitionopensince[month/year] | Gives the approximate year and month of the time the nearest competitor was opened |
| Promo                            | Indicates whether a store is running a promo on that day        |
| Promo2                           | Promo2 is a continuing and consecutive promotion for some stores: 0 = store is not participating, 1 = store is participating |
| Promo2since[year/week]           | Describes the year and calendar week when the store started participating in promo2 |
| Promointerval                    | Describes the consecutive intervals promo2 is started, naming the months the promotion is started anew. E.G. "Feb,may,aug,nov" means each round starts in february, may, august, november of any given year for that store |
 


<br>

 ### - Business Assumptions

 
 <br>
 
## 🧾 Evaluation Metric


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
11. **Telegram Bot:** deployment of Telegram Bot API, here used as our user receiver. Check out at "Deployment" section.

<br>

## 🕵🏽‍♂️Exploratory Data Analysis & Main Insights

### - Numerical Attributes Correlation

![image](https://user-images.githubusercontent.com/67332395/175460617-43a48c17-d3e0-4d05-9c86-b7d7be891572.png)

### - Categorical Attributes Correlation

![image](https://user-images.githubusercontent.com/67332395/175460670-83e08358-dd8f-432a-ad87-51037abe5fad.png)

### - Main Hypothesis Chosen


- **Hypothesis 1:**

- **Hypothesis 2:** 
   
   
- **Hypothesis 3:** 

<br>

## 💻 Machine Learning Modeling & Evaluation


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


## Project designed to rank customers interested in purchasing a vehicle insurance.

#### This project was made by Leandro Destefani.

# 1. Business Problem.

A Insurance All é uma empresa tradicional de seguros de saúde. Ela pretende lançar agora um novo produto ems eu portfólio, seguro de automóveis. Para isso, realizaram uma pesquisa entre seus milhares de clientes para coletar informações relevantes. 

A empresa quer que façamos um estudo sobre os dados repassados para que possamos criar um modelo eficiente e assertivo em relação ao número de clientes que aceitariam a contratação do novo produto, já que não seria viável (custo com ligação, tempo de contato, etc.) realizar uma pesquisa individual com todos os clientes. 

Devemos então otimizar uma lista para a empresa com as pessoas com maior probabilidade de realizar a compra.



# 2. Business Assumptions.

# 3. Solution Strategy

My strategy to solve this challenge was:

**Step 01. Data Description:**

**Step 02. Feature Engineering:**

**Step 03. Data Filtering:**

**Step 04. Exploratory Data Analysis:**

**Step 05. Data Preparation:**

**Step 06. Feature Selection:**

**Step 07. Machine Learning Modelling:**

**Step 08. Hyperparameter Fine Tunning:**

**Step 09. Convert Model Performance to Business Values:**

**Step 10. Deploy Modelo to Production:**

# 4. Top 3 Data Insights

**Hypothesis 01:**

**True/False.**

**Hypothesis 02:**

**True/False.**

**Hypothesis 03:**

**True/False.**

# 5. Machine Learning Model Applied

# 6. Machine Learning Modelo Performance

# 7. Business Results

# 8. Conclusions

# 9. Lessons Learned

# 10. Next Steps to Improve

