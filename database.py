import sqlite3
print(f"sqlite is ready!")

#creates a database where i can store the reusults after training and testing
conn = sqlite3.connect("results.db")
cursor = conn.cursor()

#create the table the,cursor sends SQL commands to the database 
cursor.execute (""" 
CREATE TABlE IF NOT EXISTS results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email_text TEXT,
                prediction INTEGER
);
""" )
conn.commit()#Save the table creation

cursor.execute(#add new row of data in the database
    "INSERT INTO results (email_text, prediction) VALUES (?,?)", (email, int(prediction[0])) 
)
conn.commit()
