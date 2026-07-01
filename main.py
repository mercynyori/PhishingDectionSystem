

import pandas as pd
import sqlite3

#loading the dataset for python to read it
df = pd.read_csv("Phishing_Email.csv", encoding="latin-1")
print(df.head())
print(df.columns) 

# the columns that i need
df = df[["Email Text", "Email Type"]]

# removing rows with no values
df = df.dropna()

#see the number of rows and columns the dataset has
print(df.shape)

#randomly choosing 300 rows and maintaining consistently
df_smaller = df.sample(n=300, random_state=42)

#saving the new clean dataset
df_smaller.to_csv("clean_emails_300.csv", index=False)

#results
print(df_smaller.head())
print("Saved rows:", len(df_smaller))

# checking the Email type values
print(df["Email Type"].unique())

#Converting the Email type values to 1 and 0
df["Email Type"] = df["Email Type"].map({
    "Safe Email" : 0,
    "Phishing Email" : 1
})

#confirmation 
print(df["Email Type"].unique())

#how many 0 and 1 values i have 
print(df["Email Type"].value_counts())

#defining the x,y
x = df["Email Text"]
y = df["Email Type"]

#import the TfidVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer


#object of the TF-IDF
vectorizer = TfidfVectorizer()
x = vectorizer.fit_transform(x)

#dividing training and testing emails
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 42)

#Logistic Regression
from sklearn.linear_model import LogisticRegression 


#creating model
model = LogisticRegression()

#Learning the pattern between x and y
model.fit(x_train, y_train)

#Predicting unseen emails
y_pred = model.predict(x_test)

#accuracy
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, y_pred)

print("accuracy", accuracy)

from database import  database_table,  saving_results 
import joblib

#start the loop to get the email u `need thid is the CLI part`
while True:
    email = input(" Input the email: ")

    if email.lower() == "exit":
        break
   #s convert to numbers
email_vector = vectorizer.transform([email])

    # predict the email 
prediction = model.predict(email_vector)[0]

    # show result from the database part
print("This is a phisshing enauk" if prediction == 1 else "This is a afe email")

    # saving it SQLite
saving_results(email, prediction)




