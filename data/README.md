# Data Folder

This folder contains datasets used in the Docker Data Science project.

## Contents

- `iris.csv`: The famous Iris flower dataset for classification tasks. It contains measurements of sepal length, sepal width, petal length, petal width, and species classification for 150 iris flowers across three species (setosa, versicolor, and virginica).

## Usage

Datasets in this folder can be accessed from within Docker containers as they are mounted as volumes. This allows you to:

1. Perform exploratory data analysis
2. Train machine learning models
3. Test data processing pipelines

## Best Practices

- Keep raw data separate from processed data
- Consider adding larger datasets to `.gitignore` and `.dockerignore`
- Document the source and structure of each dataset
- Use version control for datasets when appropriate 