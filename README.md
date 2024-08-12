# **Churn Rates and Root Causes**

##**Background**

Churn analysis is a process used by businesses to understand and manage customer attrition, or "churn".  Churn analysis helps to identify pain points throughout the customer journey.  It involves examining why customers stop using a product or service and identifying patterns or factors that contribute to their decision to leave.  Understanding those pain points then opens avenues to improve products, services and communication.

This project aims to analyze customer churn rates and identify the underlying causes.


##**Data Description**


For this project, I used a Kaggle telecom churn dataset. The dataset is formatted as a .csv file that contains 7043 rows and 21 columns.  The data includes:
 - The dataset contains 7043 rows and 21 columns.
 - Customer who left within a month, a year, and two years.
 - The services each customer signed up for:  phone, multiple lines, internet, online seurity, online backup, device protection, tech support, and streaming TV and movies. 
 - Customer account information:  how long a person was a customer, contract payment method, paperless billing, monthly charges, and total charges. 
 - Demographic info about customers:  gender, age range, and if they have partners and dependents.


The data files are located in the 'data/' directory.


##**Describing Data**

The dataset used in this project includes:

1. customerID:  A unique identifier of each customer.
2. gender:  The gender of the customer (e.g., Male, Female).
3. age:  The age of the customer, broken into a category.
4. tenure:  The length of time (in months) the customer has been with the company.
5. Contracts:  The type of contract the customer has (.e.g., Month-to-Month, One-Year, Two-Years).
6. MonthlyCharges:  The amount the customer is billed each month.
7. TotalCharges:  The total amount billed to the customer over their entire tenure.
8. PaymentMethod:  The method by which the customer pays their bill (e.g., Electronic Check, Credit Card)
9. InternetService:  The type of internet service teh customer has (e.g., DSL, Fiber Optic, No).
10. Online Security:  Whether the customer has an online security service (e.g., Yes, No).
11. OnlineBackup:  Whether the customer has an online backup service (e.g., Yes, No).
12. DeviceProtection:  Whether the customer has device protection (e.g., Yes, No).
13. TechSupport:  Whether the customer has tech support (e.g., Yes, No).
14. StreamingTV:  Whether the customer has a streaming TV service (e.g., Yes, No).
15. StreamingMovies:  Whether the customer has a streaming movies service (e.g., Yes, No).
16. Churn:  The target variable indicating whether the customer has churned (e.g., Yes, No).
17. Partner:  Indicates if the customer has a partner (e.g., Yes, No).
18. Dependents: Indicates if the customer has dependents (e.g., Yes, No).
19. PhoneService:  Whether the customer has phone service (e.g., Yes, No).
20. MultipleLines:  Whether the customer has multiple lines (e.g., Yes, No, No phone service).
21. Senior Citizens:  Indicates if the customer is a senior citizen (e.g., 1 for Yes, 0 for No).

 

##**Data Visualization**

Figure 1 shows bar graph of distribution by customer contracts.

<p align="center">
    <img src="img/distribution_by_customers_contracts.png"/>
</p>

<p align="center">
    Figure 1.  Bar graph of customer contracts

</p>

Figure 2 shows bar graph of distibution by tenure - churn, contracts-churn, and charges-churn.

<p align="center">
    <img src="img/distribution_by_tenure_contracts_charges_churn.png"/>
</p>

<p align="center">
    Figure 2.  Bar graph of tenure - churn, contracts-churn, and charges-churn

</p>

Figure 3 shows correlation heatmap.

<p align="center">
    <img src="img/correlation_heatmap.png"/>
</p>

<p align="center">
    Figure 2.  Correlation Heatmap

</p>

##**Methodology**

1. Data Collection:  Collect and preprocess data.
2. Churn Rate Calculation:  Compute churn rates using historical data.
3. Root Cause Analysis:  Apply statistical and machine learning techniques to identify factors contributing to churn.
4. Predictive Modeling:  Develop a model to predict customer churn.

For detailed information on each method, reference the notebooks in the 'notebooks/' directory.

##**Results**

The results section includes:

- Churn Rate Analysis:  Summary of churn rates and trends.
- Root Cause Insights:  Key factors contributing to churn.
- Segmentation Outcomes:  Customer segments at high risk of churn.
- Predictive Model Performance:  Metrics and evaluation of churn prediction model

##**Future Directions**

Improve regression model.  Train and test with more data.

##**References**

Telecom Dataset Website:
https://www.kaggle.com/datasets/blastchar/telco-customer-churn?select=WA_Fn-UseC_-Telco-Customer-Churn.csv

Github Location:  https://github.com/jeffreymenchion/churn_rates_and_root_causes
