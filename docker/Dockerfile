# Start with a small image containing Python 3.14
FROM python:3.14-slim

# Set the working folder inside the image
WORKDIR /app

# Copy the requirements file
COPY pipeline/requirements.txt requirements.txt

# Install Pandas, Pytest and the other requirements
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python code and data into the image
COPY testing testing
COPY data data

# Run the tests first, then run the application if they pass
CMD ["sh", "-c", "python -m pytest testing/testing_module.py -v && python -m testing.cleaning_module"]