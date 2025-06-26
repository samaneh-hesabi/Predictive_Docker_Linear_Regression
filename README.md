<div style="font-size:2.5em; font-weight:bold; text-align:center; margin-top:20px;">Salary Prediction with Docker</div>

This is a simple project that uses Docker to run a salary prediction model based on years of experience.

## Project Structure

```
.
├── Dockerfile            # Instructions for building the Docker image
├── docker-compose.yml    # Configuration for Docker Compose
├── linear_regression.py  # Python script for the salary prediction model
├── requirements.txt      # Python package dependencies
├── Salary_Data.csv       # Dataset with salary information
└── README.md             # This file
```

## How to Use

### 1. Build and Run with Docker

```bash
# Build the Docker image
docker-compose build

# Run the container
docker-compose up
```

### 2. What the Model Does

The model:
1. Loads salary data
2. Trains a linear regression model
3. Evaluates the model performance
4. Makes predictions for 5, 10, and 15 years of experience
5. Saves the trained model

## Dataset

The `Salary_Data.csv` file contains two columns:
- `YearsExperience`: Years of work experience
- `Salary`: Annual salary in dollars
cat > README.md << 'EOL'
<div style="font-size:2.5em; font-weight:bold; text-align:center; margin-top:20px;">Salary Prediction with Docker</div>

This is a simple project that uses Docker to run a salary prediction model based on years of experience.

## Project Structure

```
.
├── Dockerfile            # Instructions for building the Docker image
├── docker-compose.yml    # Configuration for Docker Compose
├── linear_regression.py  # Python script for the salary prediction model
├── requirements.txt      # Python package dependencies
├── Salary_Data.csv       # Dataset with salary information
└── README.md             # This file
```

## How to Use

### 1. Build and Run with Docker

```bash
# Build the Docker image
docker-compose build

# Run the container
docker-compose up
```

### 2. What the Model Does

The model:
1. Loads salary data
2. Trains a linear regression model
3. Evaluates the model performance
4. Makes predictions for 5, 10, and 15 years of experience
5. Saves the trained model

## Dataset

The `Salary_Data.csv` file contains two columns:
- `YearsExperience`: Years of work experience
- `Salary`: Annual salary in dollars
EOL