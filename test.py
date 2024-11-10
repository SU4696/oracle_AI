import pandas as pd

# Load the CSV files to inspect their contents and ensure column compatibility
dataset_df = pd.read_csv("/Users/suyeoncho/Downloads/oracle_AI/dataset.csv")
severity_df = pd.read_csv("/Users/suyeoncho/Downloads/oracle_AI/Symptom-severity.csv")
precaution_df = pd.read_csv("/Users/suyeoncho/Downloads/oracle_AI/symptom_precaution.csv")
description_df = pd.read_csv("/Users/suyeoncho/Downloads/oracle_AI/symptom_Description.csv")

# Display the first few rows and column names of each file to ensure compatibility with the code
{
    "dataset_columns": dataset_df.columns.tolist(),
    "severity_columns": severity_df.columns.tolist(),
    "precaution_columns": precaution_df.columns.tolist(),
    "description_columns": description_df.columns.tolist(),
    "dataset_sample": dataset_df.head(),
    "severity_sample": severity_df.head(),
    "precaution_sample": precaution_df.head(),
    "description_sample": description_df.head()
}
