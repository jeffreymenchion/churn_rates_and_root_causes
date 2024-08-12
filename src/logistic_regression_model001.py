#!/usr/bin/env python
# coding: utf-8

# In[35]:


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics import classification_report, accuracy_score


# In[36]:


#telecom_churn = pd.DataFrame()
df = pd.read_csv("/Users/jeff/Documents/assignments/churn_rates_and_root_causes/data/WA_Fn-UseC_-Telco-Customer-Churn.csv")
df


# In[37]:


#Define features and target
X = df.drop('Churn', axis=1)  #Drop the target variable to get features
y = df['Churn']  #Target variable

#Encode categorical variable if necessary
X = pd.get_dummies(X, drop_first=True)  #Convert categorial features to dummy variables

#Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


# In[38]:


#Initialize the StandardScaler
scaler = StandardScaler()

#Initalize and train the logistic regression model
model = LogisticRegression()


#Create a pipeline that scales the features then fits the model
pipeline = make_pipeline(scaler, model)

#Fit the mode to the training data
pipeline.fit(X_train, y_train)

#Make predictions
y_pred = pipeline.predict(X_test)


# In[39]:


#Evaluate the model

#Accuracy Score
print("Accuracy Score:", accuracy_score(y_test, y_pred))

#Classification Report
print("Classification Report:\n", classification_report(y_test, y_pred))

