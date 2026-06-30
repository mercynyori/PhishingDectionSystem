import sqlite3
print(f"sqlite is ready!")


def database_table():
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
    conn.close()

