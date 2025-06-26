# Base image with Python 3.11
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the necessary files
COPY linear_regression.py .
COPY Salary_Data.csv .

# Set the entry point to run the linear regression script
ENTRYPOINT ["python3", "linear_regression.py"] 