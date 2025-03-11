import random
import time
import mysql.connector
 
# Sample data

db = mysql.connector.connect(
    host="localhost",  # Change to your MySQL server
    user="root",
    password="Momo@7002",
    database="django_DB"
)
cursor = db.cursor()

names = ["Company A", "Company B", "Company C", "Company D", "Company E"]
countries = ["USA", "Canada", "Germany", "India", "Australia"]
 
def generate_data():
    data = []
    for i in range(5):
        name = names[i]
        revenue = round(random.uniform(1000, 10000), 2)  # Random revenue between 1000 and 10000
        profit = round(random.uniform(100, 5000), 2)  # Random profit between 100 and 5000
        employees = round(random.uniform(10, 500), 2)  # Random number of employees between 10 and 500
        country = random.choice(countries)
        data.append((name, revenue, profit, employees, country))
    return data

while True:
    # Generate and print data
    data = generate_data()
    for row in data:
        cursor.execute("INSERT INTO statapp_business (name, revenue, profit, employees, country) VALUES (%s, %s, %s, %s, %s)", row)
        db.commit()
        print(f"Inserted: {row}")
        print(row)
        time.sleep(4)
 