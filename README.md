## Data cleaning

The Python script reads the library books and customer CSV files using Pandas.

The script cleans the data by:

- Removing rows containing empty cells.
- Removing duplicate records.
- Converting the checkout and returned columns into date format.
- Identifying and removing invalid dates.
- Correcting an incorrectly entered book title.
- Removing records where the return date is before the checkout date.
- Converting ID columns into whole numbers.

The cleaned results are saved as:

- `data/cleaned_library.csv`
- `data/cleaned_library_customers.csv`

The main Python file is:

- `cleaning_module.py`



## Unit testing

Pytest is used to test the data-cleaning functions.

The tests check:

- Empty cells are removed.
- Date columns use the correct data type.
- Incorrect customer, date and borrowing data is removed.
- Duplicate loans are removed.
- Book titles do not contain trailing spaces.

Run the tests using:

`python -m pytest testing_module.py -v`

### Additional testing

A second test file uses Python's built-in `unittest` module.

#test