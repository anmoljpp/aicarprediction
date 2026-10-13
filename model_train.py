import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

dataset = pd.read_csv('used_cars_clean.csv')

features = dataset.drop('Price_Class', axis=1)
target = dataset['Price_Class']

Xtrain, Xtest, Ytrain, Ytest = train_test_split(features, target, train_size=0.8, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
print("model training started...")
model.fit(Xtrain, Ytrain)
print("model training completed...")
joblib.dump(model, 'trainedmodel.joblib')
print("model saved to disk...")


print(model.predict([[3,2016,11554,1,0,1,19.67,1582.0,126.2,5.0,14.25,10,164,10,0]]))
