# Library Data Quality Automation

This project automates the cleaning and presentation of library loan data.

The original process required records to be checked manually, which took time and could produce inconsistent results. Python and Pandas are used to clean the data automatically before presenting it in a simple web dashboard.

## Live dashboard

[Open the Library Data Quality Dashboard](https://library-data-quality-automation.streamlit.app/)

The dashboard displays:

- The number of valid loans.
- The number of customers.
- Books checked out by each customer.
- The longest and shortest loan periods.
- A table of the cleaned library records.

## How the application works

1. Library loan and customer data is read from CSV files.
2. Python and Pandas clean and validate the records.
3. Pytest and unittest check that the cleaning functions work correctly.
4. Cleaned results are saved as new CSV files.
5. Streamlit presents the cleaned data in a web dashboard.
6. GitHub Actions automatically tests the project when code is changed.
7. Docker packages the application and its dependencies into an image.

## Data cleaning

The cleaning code is stored in:

```text
testing/cleaning_module.py
```

It performs the following checks:

- Removes records containing required empty values.
- Converts checkout and return dates into date format.
- Removes invalid dates.
- Removes records where a book was returned before it was checked out.
- Removes duplicate loans using the columns that define a loan.
- Checks that customer IDs exist in the customer file.
- Applies the 14-day borrowing rule.
- Corrects an incorrectly entered book title.
- Removes trailing spaces from book titles.
- Converts ID columns into whole numbers.

The cleaned files are saved as:

```text
data/cleaned_library.csv
data/cleaned_library_customers.csv
```

## Automated testing

The project includes tests written using pytest and unittest.

The tests check:

- Empty-cell handling.
- Date conversion.
- Incorrect data.
- Duplicate removal.
- Customer IDs.
- Loan periods.
- Book titles.

Run the pytest tests:

```powershell
python -m pytest testing/testing_module.py -v
```

Run the unittest tests:

```powershell
python -m testing.unittest_module -v
```

## Continuous integration

Two GitHub Actions workflows are included:

- `library_ci.yml` installs Python and runs the automated tests.
- `docker_ci.yml` tests the application, builds a Docker image, runs a container and stores the image as an artifact.

Both workflows run automatically when code is pushed to the `main` branch or when a pull request targets `main`.

The Docker workflow only builds the image after the Python tests pass.

## Docker

The Dockerfile packages Python, the required modules, application code and source data into one image.

Build the image:

```powershell
docker build --file docker/Dockerfile --tag library-quality-analysis:1.0 .
```

Run a container:

```powershell
docker run --name library-cleaner library-quality-analysis:1.0
```

When the container starts, pytest runs first. The cleaning application only runs if all the tests pass.

## Streamlit dashboard

Install the dashboard requirements:

```powershell
python -m pip install -r presentation/requirements.txt
```

Run the dashboard locally:

```powershell
python -m streamlit run presentation/app.py
```

The local dashboard will normally open at:

```text
http://localhost:8501
```

The published dashboard is hosted using Streamlit Community Cloud and is connected to this GitHub repository.

## Security

- `.gitignore` prevents unnecessary or sensitive local files from being committed.
- Credentials should be stored using GitHub Secrets.
- Secrets are not written directly into the Python code, workflow files or Dockerfile.
- `.dockerignore` prevents unnecessary files from being included in the Docker build context.

## Documentation

Further project documentation is available here:

- [Architecture design](documentation/architecture.md)
- [User stories and Kanban board](documentation/user-stories.md)
- [Test plan](documentation/test-plan.md)

## Repository structure

```text
python-training/
├── .github/workflows/    GitHub Actions workflows
├── data/                 Source and cleaned CSV files
├── docker/               Dockerfile and Docker commands
├── documentation/        Architecture, user stories and test plan
├── pipeline/             Python requirements
├── presentation/         Streamlit dashboard
├── testing/              Cleaning code and automated tests
├── .dockerignore
├── .gitignore
└── README.md
```

## Technology choices

- **Python:** Automates the data-cleaning process.
- **Pandas:** Reads, cleans, validates and saves the library data.
- **Pytest and unittest:** Check that the cleaning code works correctly.
- **GitHub Actions:** Automatically tests changes pushed to the repository.
- **Docker:** Packages the application so it can run consistently.
- **Streamlit:** Provides a free and simple web dashboard.
- **Azure Synapse and ADLS:** Included in the proposed architecture because my company uses Microsoft Azure and I am familiar with these tools.

## Outcome

The project reduces manual checking, improves data consistency and produces repeatable library data-quality results. The cleaned information is ready for presentation through the Streamlit dashboard.