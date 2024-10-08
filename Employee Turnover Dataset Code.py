import pandas as pd

# General Overview
# Load Dataset
df = pd.read_excel(r"C:\Users\merie\OneDrive\Bureau\WGU\D599\Employee Turnover Dataset.xlsx")

# Get Number of Rows and Columns
num_rows, num_columns = df.shape

# Display number of rows and columns
print(f"Number of rows: {num_rows}")
print(f"Number of columns: {num_columns}")

# Print all column names
print(df.columns)  

# Check for duplcates
duplicate_rows = df[df.duplicated()]
# Display number of duplicates
print("Number of duplicate rows:" , duplicate_rows.shape[0])

# Check for missing values and add up the number of missing values in each column
missing_values_rows = df.isnull().sum()
# Print missing values
print("Missing values per column:\n" , missing_values_rows)

# Check for inconsistent entries in the Gender columns
gender_unique = df['Gender'].unique()
print("unique gender in the gender columns:" , gender_unique)

# check for inconsistent entries for all columns
for column in df.columns:
    print(f"unique values in {column}:\n{df[column].unique()}\n")

# Check for formatting errors
print(df.dtypes)

# Outlier for JobSatisfaction (count employees with satisfaction score 1)
low_satisfaction_count = df[df['JobSatisfaction'] == 1].shape[0]
# Display
print("Number of employees with satisfaction score 1:", low_satisfaction_count)

# Data cleaning

# Remove duplicates
df.drop_duplicates(inplace=True)
# Check number of duplicates after removal 
print("Number of duplicates after removal:", df.duplicated().sum())


# Filling the missing entries
df.fillna(method='ffill', inplace=True)
# Fill missing values with the mean
df['TrainingTimesLastYear'] = df['TrainingTimesLastYear'].fillna(df['TrainingTimesLastYear'].mean())

# Check the number of missing values after filling
missing_values_after_fill = df.isnull().sum()
# Display the number of missing values per column
print("Missing values per column after filling:\n", missing_values_after_fill)

# Correct inconsistent entries
# Create dictionary to correct inconsistent entries in multiple columns
replacements = {
    'Age': {148: None, 96: None, 12: None, 15: None},  # Unlikely ages
    'BusinessTravel': {'00': 'Non-Travel', 1: 'Travel_Rarely', -1: 'Non-Travel', ' ': 'Non-Travel'},  
    'DistanceFromHome': {3737: None, 3535: None, 978: None},  # Unlikely distances
    'EmployeeCount': {-1: 1, 3: 1},  # only 1 employee count
    'EducationField': {' ': 'Other'},  # Blank entry replaced with 'Other'
    'JobRole': {' ': 'Unknown'},  # Blank entry replaced with 'Unknown'
    'TotalWorkingYears': {-1: 1, 222: 1},  # Negative and high value replaced by 1
    'YearsWithCurrManager': {'na': None, -1000: None},  # Replace 'na' and negative values

}
# Apply replacements to dataframe
df.replace(replacements, inplace=True)
# Check for any remaining inconsistent entries
for column in replacements.keys():
    print(f"Unique values in {column} column after correction:\n{df[column].unique()}\n")

# Correct formatting errors

# Print the columns to check their names
print("Columns in DataFrame:", df.columns.tolist())

# Strip whitespace from all column names
df.columns = df.columns.str.strip()

# Define a function to safely convert columns
def safe_convert(column, dtype, fill_value=None):
    if fill_value is not None:
        column = column.fillna(fill_value)  # Fill NaN values
    return column.astype(dtype)

# Convert to appropriate data types 
df['Age'] = safe_convert(df['Age'], int, fill_value=0)  # Integer
df['HourlyRate'] = safe_convert(df['HourlyRate'], float)  # Float
df['MonthlyIncome'] = safe_convert(df['MonthlyIncome'], float)  # Float
df['PercentSalaryHike'] = safe_convert(df['PercentSalaryHike'], float)  # Float
df['PerformanceRating'] = safe_convert(df['PerformanceRating'], float)  # Float
df['WorkLifeBalance'] = safe_convert(df['WorkLifeBalance'], float)  # Float
df['TrainingTimesLastYear'] = safe_convert(df['TrainingTimesLastYear'], float)  # Float
df['EmployeeCount'] = safe_convert(df['EmployeeCount'], int, fill_value=0)  # Integer
df['EmployeeNumber'] = safe_convert(df['EmployeeNumber'], int, fill_value=0)  # Integer
df['EnvironmentSatisfaction'] = safe_convert(df['EnvironmentSatisfaction'], int, fill_value=0)  # Integer
df['JobInvolvement'] = safe_convert(df['JobInvolvement'], int, fill_value=0)  # Integer
df['JobLevel'] = safe_convert(df['JobLevel'], int, fill_value=0)  # Integer
df['NumCompaniesWorked'] = safe_convert(df['NumCompaniesWorked'], int, fill_value=0)  # Integer
df['StandardHours'] = safe_convert(df['StandardHours'], int, fill_value=0)  # Integer
df['StockOptionLevel'] = safe_convert(df['StockOptionLevel'], int, fill_value=0)  # Integer
df['TotalWorkingYears'] = safe_convert(df['TotalWorkingYears'], int, fill_value=0)  # Integer
df['YearsAtCompany'] = safe_convert(df['YearsAtCompany'], int, fill_value=0)  # Integer
df['YearsInCurrentRole'] = safe_convert(df['YearsInCurrentRole'], int, fill_value=0)  # Integer
df['YearsSinceLastPromotion'] = safe_convert(df['YearsSinceLastPromotion'], int, fill_value=0)  # Integer
df['YearsWithCurrManager'] = safe_convert(df['YearsWithCurrManager'], int, fill_value=0)  # Integer

# Categorical columns (convert to category dtype)
categorical_columns = ['Turnover', 'BusinessTravel', 'Department', 'Education', 
                       'EducationField', 'Gender', 'JobRole', 'MaritalStatus', 
                       'Over18', 'OverTime']

df[categorical_columns] = df[categorical_columns].astype('category')

# Check the data types after conversion
print(df.dtypes)

# Save the cleaned DataFrame to a CSV file
cleaned_file_path = r"C:\Users\merie\OneDrive\Bureau\WGU\D599\cleaned_employee_turnover_dataset.csv"
df.to_csv(cleaned_file_path, index=False)  

print(f"Cleaned dataset saved to {cleaned_file_path}")