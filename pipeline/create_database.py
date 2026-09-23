import pandas as pd
import sqlite3
import os

# Read the cleaned CSV files
books = pd.read_csv("data/cleaned_library.csv")
customers = pd.read_csv("data/cleaned_library_customers.csv")

# Create the output folder
os.makedirs("output", exist_ok=True)

# Connect to the SQLite database
connection = sqlite3.connect("output/library.db")

# Add the cleaned data to database tables
books.to_sql(
    "books",
    connection,
    if_exists="replace",
    index=False
)

customers.to_sql(
    "customers",
    connection,
    if_exists="replace",
    index=False
)

# Close the database connection
connection.close()

print("Library database created")