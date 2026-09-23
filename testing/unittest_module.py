import unittest
import pandas as pd


from testing.cleaning_module import clean_books
from testing.cleaning_module import clean_customers

class TestLibraryCleaning(unittest.TestCase):

    ## Runs before each test
    def setUp(self):

        self.books = pd.read_csv("data/library.csv")
        self.customers = pd.read_csv(
            "data/library_customers.csv"
        )

        self.cleaned_customers = clean_customers(
            self.customers
        )

        self.cleaned_books = clean_books(
            self.books,
            self.cleaned_customers
        )

    # Test that empty cells have been removed
    def test_empty_cells(self):

        missing_books = (
            self.cleaned_books.isnull().sum().sum()
        )

        missing_customers = (
            self.cleaned_customers.isnull().sum().sum()
        )

        self.assertEqual(missing_books, 0)
        self.assertEqual(missing_customers, 0)

    # Test that the date columns are dates
    def test_date_format(self):

        checkout_is_date = (
            pd.api.types.is_datetime64_any_dtype(
                self.cleaned_books["Book checkout"]
            )
        )

        returned_is_date = (
            pd.api.types.is_datetime64_any_dtype(
                self.cleaned_books["Book Returned"]
            )
        )

        self.assertTrue(checkout_is_date)
        self.assertTrue(returned_is_date)

    # Test that incorrect loan data has been removed
    def test_wrong_data(self):

        valid_customers = (
            self.cleaned_books["Customer ID"].isin(
                self.cleaned_customers["Customer ID"]
            ).all()
        )

        correct_dates = (
            self.cleaned_books["Days borrowed"] >= 0
        ).all()

        within_limit = (
            self.cleaned_books["Days borrowed"] <= 14
        ).all()

        self.assertTrue(valid_customers)
        self.assertTrue(correct_dates)
        self.assertTrue(within_limit)

    # Test that duplicate loans have been removed
    def test_duplicates(self):

        duplicate_columns = [
            "Books",
            "Book checkout",
            "Book Returned",
            "Customer ID"
        ]

        duplicates = self.cleaned_books.duplicated(
            subset=duplicate_columns
        ).sum()

        self.assertEqual(duplicates, 0)

    # Runs after each test
    def tearDown(self):

        del self.books
        del self.customers
        del self.cleaned_books
        del self.cleaned_customers


if __name__ == "__main__":
    unittest.main()