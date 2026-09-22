import pandas as pd


# Function to clean the customer data
def clean_customers(customers):

    # Remove empty rows
    customers = customers.dropna()

    # Remove duplicate customers using Customer ID
    customers = customers.drop_duplicates(
        subset=["Customer ID"]
    )

    # Change Customer ID into a whole number
    customers["Customer ID"] = customers["Customer ID"].astype(int)

    return customers


# Function to clean the library data
def clean_books(books, customers):

    # Remove rows containing empty cells
    books = books.dropna()

    # Remove speech marks from the checkout dates
    books["Book checkout"] = books["Book checkout"].str.replace('"', '')

    # Change the columns into date format
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

    # Remove invalid dates, such as 32/05/2023
    books = books.dropna()

    # Remove extra spaces from book names
    books["Books"] = books["Books"].str.strip()

    # Correct the spelling mistake
    books["Books"] = books["Books"].replace(
        "Lord of the rings the return of the kind",
        "Lord of the rings the return of the king"
    )

    # Change the ID columns into whole numbers
    books["Id"] = books["Id"].astype(int)
    books["Customer ID"] = books["Customer ID"].astype(int)

    # Remove duplicate loans
    # Id is not included because duplicate loans can have different IDs
    books = books.drop_duplicates(
        subset=[
            "Books",
            "Book checkout",
            "Book Returned",
            "Customer ID"
        ]
    )

    # Keep loans only when the customer exists
    books = books[
        books["Customer ID"].isin(customers["Customer ID"])
    ]

    # Change "2 weeks" into 14 days
    books["Days allowed"] = (
        books["Days allowed to borrow"]
        .str.replace(" weeks", "")
        .astype(int) * 7
    )

    # Work out the number of days each book was borrowed
    books["Days borrowed"] = (
        books["Book Returned"] - books["Book checkout"]
    ).dt.days

    # Show loans with incorrect dates
    wrong_dates = books[
        books["Days borrowed"] < 0
    ]

    print("Loans with incorrect dates:")
    print(wrong_dates)

    # Show loans that went over the allowed time
    overdue_books = books[
        books["Days borrowed"] > books["Days allowed"]
    ]

    print("Loans over the 14 day limit:")
    print(overdue_books)

    # Keep only loans between 0 and 14 days
    books = books[
        (books["Days borrowed"] >= 0) &
        (books["Days borrowed"] <= books["Days allowed"])
    ]

    return books


# Only runs when cleaning_module.py is opened directly
if __name__ == "__main__":

    # Read the CSV files
    books = pd.read_csv("data/library.csv")
    customers = pd.read_csv("data/library_customers.csv")

    # Show the original number of rows
    print("Original book rows:", len(books))
    print("Original customer rows:", len(customers))

    # Run the cleaning functions
    customers = clean_customers(customers)
    books = clean_books(books, customers)

    # Show the cleaned data
    print(books)
    print(customers)

    # Save the cleaned files
    books.to_csv("data/cleaned_library.csv", index=False)

    customers.to_csv(
        "data/cleaned_library_customers.csv",
        index=False
    )

    print("Data cleaning completed")