import pandas as pd

# Read the CSV files
books = pd.read_csv("data/library.csv")
customers = pd.read_csv("data/library_customers.csv")

# Show the original data
print(books)
print(customers)

# Check for empty cells
print(books.isnull().sum())
print(customers.isnull().sum())

# Remove rows with empty cells
books = books.dropna()
customers = customers.dropna()

# Check for duplicates
print(books.duplicated())
print(customers.duplicated())

# Remove duplicates
books = books.drop_duplicates()
customers = customers.drop_duplicates()

# Remove speech marks from the checkout date
books["Book checkout"] = books["Book checkout"].str.replace('"', '')

# Change the columns into date format
# Invalid dates will be changed into empty values
books["Book checkout"] = pd.to_datetime(
    books["Book checkout"],
    dayfirst=True,
    errors="coerce"
)

books["Book Returned"] = pd.to_datetime(
    books["Book Returned"],
    dayfirst=True,
    errors="coerce"
)

# Remove rows containing invalid dates
books = books.dropna()

# Check the different book names
print(books["Books"].value_counts())

# Correct a spelling mistake
books["Books"] = books["Books"].replace(
    "Lord of the rings the return of the kind",
    "Lord of the rings the return of the king"
)

# Find dates where the book was returned before it was checked out
wrong_dates = books[
    books["Book Returned"] < books["Book checkout"]
]

print(wrong_dates)

# Remove the rows containing incorrect dates
books = books[
    books["Book Returned"] >= books["Book checkout"]
]

# Change the ID columns into whole numbers
books["Id"] = books["Id"].astype(int)
books["Customer ID"] = books["Customer ID"].astype(int)
customers["Customer ID"] = customers["Customer ID"].astype(int)

# Show the cleaned data
print(books)
print(customers)

# Save the cleaned data
books.to_csv("data/cleaned_library.csv", index=False)
customers.to_csv("data/cleaned_library_customers.csv", index=False)