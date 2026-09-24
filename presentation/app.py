import streamlit as st
import pandas as pd

# Read the cleaned files
books = pd.read_csv("data/cleaned_library.csv")
customers = pd.read_csv("data/cleaned_library_customers.csv")

# Add the customer names to the book data
library_data = books.merge(customers, on="Customer ID")

# Change the dates back into date format
library_data["Book checkout"] = pd.to_datetime(
    library_data["Book checkout"]
)

library_data["Book Returned"] = pd.to_datetime(
    library_data["Book Returned"]
)

# Work out how long each book was borrowed
library_data["Days borrowed"] = (
    library_data["Book Returned"] -
    library_data["Book checkout"]
).dt.days

# Dashboard title
st.title("Library Data Quality Dashboard")

st.write(
    "This dashboard displays the cleaned library loan data."
)

# Display some totals
column1, column2 = st.columns(2)

column1.metric(
    "Number of loans",
    len(library_data)
)

column2.metric(
    "Number of customers",
    library_data["Customer ID"].nunique()
)

# Count the loans for each customer
books_by_customer = (
    library_data.groupby("Customer Name")
    .size()
    .reset_index(name="Books checked out")
)

st.subheader("Books checked out by customer")

st.bar_chart(
    books_by_customer.set_index("Customer Name")
)

# Find the longest and shortest loans
longest_loan = library_data.loc[
    library_data["Days borrowed"].idxmax()
]

shortest_loan = library_data.loc[
    library_data["Days borrowed"].idxmin()
]

st.subheader("Loan periods")

st.write(
    "Longest loan:",
    longest_loan["Books"],
    "-",
    longest_loan["Days borrowed"],
    "days"
)

st.write(
    "Shortest loan:",
    shortest_loan["Books"],
    "-",
    shortest_loan["Days borrowed"],
    "days"
)

# Display the cleaned records
st.subheader("Cleaned library records")

st.dataframe(
    library_data[
        [
            "Books",
            "Customer Name",
            "Book checkout",
            "Book Returned",
            "Days borrowed"
        ]
    ],
    hide_index=True
)