
from database import  create_table,  saving_results 
import joblib

create_table() #this create the table ones the pragram starts not everztime coz every time will waste time

#this is always  return a trained brain
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

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
print("This is a phishing email" if prediction == 1 else "This is a safe email")

    # saving it SQLite
saving_results(email, prediction)


