# Let's merge the relevant data from all CSV files into a single consolidated CSV
# that includes symptoms, severity, description, and precautions for easier integration.

# Load all necessary datasets again for merging
dataset_df = pd.read_csv("/Users/suyeoncho/Downloads/oracle_AI/dataset.csv")
severity_df = pd.read_csv("/Users/suyeoncho/Downloads/oracle_AI/Symptom-severity.csv")
precaution_df = pd.read_csv("/Users/suyeoncho/Downloads/oracle_AI/symptom_precaution.csv")
description_df = pd.read_csv("/Users/suyeoncho/Downloads/oracle_AI/symptom_Description.csv")


# Flatten the symptoms in dataset_df and add severity for each symptom based on severity_df
# Fill NaN in dataset for uniformity
dataset_df = dataset_df.fillna("None")

# Merge dataset_df with severity for each symptom
for symptom_col in dataset_df.columns[1:]:  # skip 'Disease' column
    dataset_df = dataset_df.merge(severity_df, left_on=symptom_col, right_on='Symptom', how='left')
    dataset_df = dataset_df.drop(columns=['Symptom'])  # remove 'Symptom' column from merge
    dataset_df = dataset_df.rename(columns={'weight': f'{symptom_col}_severity'})  # rename weight to specific symptom severity

# Merge description and precautions
consolidated_df = dataset_df.merge(description_df, on='Disease', how='left')
consolidated_df = consolidated_df.merge(precaution_df, on='Disease', how='left')

# Saving the consolidated CSV for use in model training and chatbot
consolidated_df.to_csv("/mnt/data/consolidated_data.csv", index=False)

# Display the first few rows of the consolidated DataFrame
consolidated_df.head()
