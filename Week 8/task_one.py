import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1: Load and Explore the Dataset with Error Handling
try:
    # Load the dataset (replace with the actual path to your downloaded CSV file)
    df = pd.read_csv('/Users/jeanguya/Desktop/Software Engineering/Python Navigation/Python Assignments/Week 8/Upper Secondary.csv', encoding='ISO-8859-1')
    print("Dataset loaded successfully")
except FileNotFoundError:
    print("Error: The file was not found. Please check the file path.")
    exit()  # Stop the program if file is not found
except pd.errors.ParserError:
    print("Error: There was a problem parsing the CSV file.")
    exit()
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    exit()

# Display the first few rows to inspect the data
print(df.head())

# Check for missing values and data types
print(df.info())

# Check for summary statistics of the numerical columns
print(df.describe())

# Data cleaning: Drop rows with missing values
df_cleaned = df.dropna()  # Drops rows with any missing value
print("Cleaned dataset:")
print(df_cleaned.info())

# Task 2: Basic Data Analysis with Error Handling
try:
    # Statistical summary of numerical columns
    print(df_cleaned[['Total', 'Female', 'Male', 'Rural_Residence', 'Urban_Residence']].describe())
except KeyError as e:
    print(f"Error: One or more columns are missing - {e}")

# Group by Region and calculate the average of out-of-school rates
try:
    region_avg = df_cleaned.groupby('Region')[['Total', 'Female', 'Male', 'Rural_Residence', 'Urban_Residence']].mean()
    print(region_avg)
except KeyError as e:
    print(f"Error: The column 'Region' or other required columns are missing - {e}")

# Check correlation between numeric columns
try:
    print(df_cleaned[['Total', 'Female', 'Male', 'Rural_Residence', 'Urban_Residence']].corr())
except KeyError as e:
    print(f"Error: One or more numeric columns are missing - {e}")

# Task 3: Data Visualization with Error Handling

try:
    # Aggregate the data by year (Time period) and calculate the mean of 'Total'
    df_cleaned['Time period'] = pd.to_numeric(df_cleaned['Time period'], errors='coerce')  # Ensure 'Time period' is numeric
    yearly_avg = df_cleaned.groupby('Time period')['Total'].mean()

     # Heatmap for correlation between numerical columns
    plt.figure(figsize=(10, 6))
    sns.heatmap(df_cleaned[['Total', 'Female', 'Male', 'Rural_Residence', 'Urban_Residence']].corr(), annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Heatmap of Out-of-School Rates')
    plt.show()

    # Bar chart comparing out-of-school rates by Region
    region_avg['Total'].plot(kind='bar', figsize=(12, 8))
    plt.title('Average Out of School Rate by Region')
    plt.xlabel('Region')
    plt.ylabel('Average Out of School Rate')
    plt.xticks(rotation=90)
    plt.show()

    # Pie chart showing distribution of out-of-school rates by Sub-region
    sub_region_avg = df_cleaned.groupby('Sub-region')['Total'].mean()
    sub_region_avg.plot(kind='pie', figsize=(8, 8), autopct='%1.1f%%', startangle=90)
    plt.title('Distribution of Out-of-School Rates by Sub-region')
    plt.ylabel('')
    plt.show()

    # Histogram for out-of-school rates
    plt.figure(figsize=(10, 6))
    plt.hist(df_cleaned['Total'], bins=20, edgecolor='black')
    plt.title('Distribution of Out-of-School Rates')
    plt.xlabel('Out-of-School Rate (%)')
    plt.ylabel('Frequency')
    plt.show()

except Exception as e:
    print(f"An error occurred during visualization: {e}")





# Step 4: Findings and Observations

# Observations based on the analysis and visualizations
print("\nFindings and Observations:")
print("- 1. Sub-Saharan Africa exhibits the highest average out-of-school rate, while Eastern and Central Asia shows the lowest.")
print("- 2. Strong positive correlations are found between overall out-of-school rates and female, male, rural, and urban residence rates.")
print("- 3. The distribution of out-of-school rates is multimodal and positively skewed, indicating several common clusters of rates.")
print("- 4. West and Central Africa contributes the largest share of the total out-of-school rates, while Eastern Europe and Central Asia has the smallest.")

