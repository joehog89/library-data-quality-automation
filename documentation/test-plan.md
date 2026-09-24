# Test Plan

The following tests check the main data-cleaning requirements.

| Test ID | Test scenario | Expected result | Acceptance criteria | Date implemented |
|---|---|---|---|---|
| T01 | Check for empty cells | Records containing required empty values are removed | No required fields contain null values | 24/09/2026 |
| T02 | Check date formats | Checkout and return dates are converted into date format | Both date columns use a datetime data type | 24/09/2026 |
| T03 | Check invalid dates | Invalid dates such as 32/05/2023 are removed | No invalid dates remain | 24/09/2026 |
| T04 | Check returned-before-checkout dates | Incorrect loan dates are removed | Return date is not earlier than checkout date | 24/09/2026 |
| T05 | Check duplicate loans | Duplicate loan records are removed | No duplicates exist across the selected loan columns | 24/09/2026 |
| T06 | Check customer IDs | Loans without a matching customer are removed | Every loan customer ID exists in the customer file | 24/09/2026 |
| T07 | Check the 14-day rule | Loans exceeding their allowed period are removed | Days borrowed does not exceed days allowed | 24/09/2026 |
| T08 | Check book titles | Incorrect spelling and trailing spaces are corrected | Titles contain no known spelling errors or trailing spaces | 24/09/2026 |

## Automated testing

The tests are automated using pytest and unittest. GitHub Actions runs the tests whenever code is pushed to the main branch.