# Use the same Python version as the GitHub workflow
FROM python:3.12-slim

# Create the application folder inside the container
WORKDIR /app

# Copy and install the required Python modules
COPY pipeline/requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python code and source data
COPY testing testing
COPY data data

# Run the data-cleaning application
CMD ["python", "-m", "testing.cleaning_module"]