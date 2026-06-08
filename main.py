

import pandas as pd

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

