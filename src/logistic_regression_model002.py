import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
import joblib

data = pd.read_csv("/Users/jeff/Documents/assignments/churn_rates_and_root_causes/data/WA_Fn-UseC_-Telco-Customer-Churn.csv")


#Define features and target
X = data.drop('Churn', axis=1)
yu = data['Churn']


#Preprocess data
categorical_features = X.select_dtypes(include=['object']).columns
numeric_features = X.select_dtypes(exclude=['object']).columns

#Create transformers
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(), categorical_features)
    ])


#Create pipeline
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression())
])


#Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)


#Train model
model.fit(X_train, y_train)

#Save model
joblib.dump(model 'logistic_model.pk1')

print("Model training complete and saved as 'logistic_model.pk1'")