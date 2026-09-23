import pandas as pd
import pytest

## Import cleaning functions
from testing.cleaning_module import clean_books
from testing.cleaning_module import clean_customers


# Read test data
books = pd.read_csv("data/library.csv")
customers = pd.read_csv("data/library_customers.csv")

# Run cleaning functions
cleaned_customers = clean_customers(customers)
cleaned_books = clean_books(books, cleaned_customers)


# Test empty cells have been removed
def test_empty_cells():

    assert cleaned_books.isnull().sum().sum() == 0
    assert cleaned_customers.isnull().sum().sum() == 0

    # Check that every loan has a customer ID
    assert cleaned_books["Customer ID"].isnull().sum() == 0


# Test  dates are in the correct format
def test_date_format():

    assert str(cleaned_books["Book checkout"].dtype) == "datetime64[ns]"
    assert str(cleaned_books["Book Returned"].dtype) == "datetime64[ns]"


# Test that wrong data has been removed
def test_wrong_data():

    # Check that all customers exist in the customer file
    assert cleaned_books["Customer ID"].isin(
        cleaned_customers["Customer ID"]
    ).all()

    # Check that no return date is before the checkout date
    assert (cleaned_books["Days borrowed"] >= 0).all()

    # Check that no book was borrowed for more than 14 days
    assert (cleaned_books["Days borrowed"] <= 14).all()

    # Check that the spelling mistake was removed
    assert (
        "Lord of the rings the return of the kind"
        not in cleaned_books["Books"].values
    )

    # Check that book titles do not have trailing spaces
    assert cleaned_books["Books"].str.endswith(" ").sum() == 0


# Test that duplicate loans have been removed
def test_duplicates():

    duplicate_columns = [
        "Books",
        "Book checkout",
        "Book Returned",
        "Customer ID"
    ]

    duplicates = cleaned_books.duplicated(
        subset=duplicate_columns
    ).sum()

    assert duplicates == 0