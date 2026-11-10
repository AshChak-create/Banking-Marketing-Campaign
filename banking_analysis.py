import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the dataset
#file_path = r"C:\Users\ASHMITA\PycharmProjects\Banking-marketing-campaign-analysis\banking_data"

df = pd.read_csv("banking_data.csv")

# Step 2: View the first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Step 3: Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Step 4: Basic info about the dataset
print("\nInfo about the dataset:")
print(df.info())
# Age Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df['age'], bins=20, kde=True)
plt.title('Age Distribution of Clients')
plt.xlabel('Age')
plt.ylabel('Number of Clients')
plt.tight_layout()
plt.show()
# Job Type Count
plt.figure(figsize=(10, 5))
sns.countplot(data=df, x='job', order=df['job'].value_counts().index)
plt.title('Distribution of Job Types')
plt.xlabel('Job')
plt.ylabel('Number of Clients')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# Marital Status Distribution
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='marital', order=df['marital'].value_counts().index)
plt.title('Marital Status Distribution')
plt.xlabel('Marital Status')
plt.ylabel('Number of Clients')
plt.tight_layout()
plt.show()

# Education Level Distribution
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='education', order=df['education'].value_counts().index)
plt.title('Education Level of Clients')
plt.xlabel('Education')
plt.ylabel('Number of Clients')
plt.tight_layout()
plt.show()
# Count of default values (yes/no)
default_counts = df['default'].value_counts()
print("Credit Default Counts:")
print(default_counts)

# Proportion (percentage)
default_percent = df['default'].value_counts(normalize=True) * 100
print("\nCredit Default Proportion (%):")
print(default_percent)

# Plot the proportions


plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='default', order=default_counts.index)
plt.title('Proportion of Clients with Credit in Default')
plt.xlabel('Credit in Default')
plt.ylabel('Number of Clients')
plt.tight_layout()
plt.show()

# Plot the balance distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['balance'], bins=50, kde=True)
plt.title('Distribution of Average Yearly Balance')
plt.xlabel('Balance (in Euros)')
plt.ylabel('Number of Clients')
plt.xlim(-2000, 40000)  # Optional: limit the range to focus on most data
plt.tight_layout()
plt.show()

# You can also print summary stats:
print("Summary statistics for balance:")
print(df['balance'].describe())
# Count of housing loan status
housing_counts = df['housing'].value_counts()
print("Housing Loan Status Counts:")
print(housing_counts)

# Percentage
housing_percent = df['housing'].value_counts(normalize=True) * 100
print("\nHousing Loan Status Proportion (%):")
print(housing_percent)

# Visualization


plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='housing', order=housing_counts.index)
plt.title('Number of Clients with Housing Loans')
plt.xlabel('Has Housing Loan')
plt.ylabel('Number of Clients')
plt.tight_layout()
plt.show()

# Count of personal loan status
loan_counts = df['loan'].value_counts()
print("Personal Loan Status Counts:")
print(loan_counts)

# Percentage
loan_percent = df['loan'].value_counts(normalize=True) * 100
print("\nPersonal Loan Status Proportion (%):")
print(loan_percent)

# Visualization


plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='loan', order=loan_counts.index)
plt.title('Number of Clients with Personal Loans')
plt.xlabel('Has Personal Loan')
plt.ylabel('Number of Clients')
plt.tight_layout()
plt.show()
# Count the contact types
contact_counts = df['contact'].value_counts()
print("Contact Types:")
print(contact_counts)

# Percentage
contact_percent = df['contact'].value_counts(normalize=True) * 100
print("\nContact Type Proportions (%):")
print(contact_percent)

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='contact', order=contact_counts.index)
plt.title('Types of Communication Used During the Campaign')
plt.xlabel('Contact Type')
plt.ylabel('Number of Clients Contacted')
plt.tight_layout()
plt.show()
# Plot distribution of contact day
plt.figure(figsize=(10, 5))
sns.histplot(df['day'], bins=31, kde=False)
plt.title('Distribution of Last Contact Day of the Month')
plt.xlabel('Day of the Month')
plt.ylabel('Number of Clients Contacted')
plt.xticks(range(1, 32))  # days from 1 to 31
plt.tight_layout()
plt.show()
# Define month order manually for proper display
month_order = ['jan', 'feb', 'mar', 'apr', 'may', 'jun',
               'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

# Plot the contact month distribution
plt.figure(figsize=(10, 5))
sns.countplot(data=df, x='month', order=month_order)
plt.title('Client Contact Counts by Month')
plt.xlabel('Month')
plt.ylabel('Number of Clients Contacted')
plt.tight_layout()
plt.show()
# Optionally limit to reasonable range to avoid outliers messing up the plot
plt.figure(figsize=(10, 5))
sns.histplot(df['duration'], bins=50, kde=True)
plt.title('Distribution of Duration of Last Contact')
plt.xlabel('Duration (seconds)')
plt.ylabel('Number of Clients')
plt.xlim(0, 1000)  # Focus on normal range; most calls are under 1000s
plt.tight_layout()
plt.show()

# Summary statistics
print("Summary statistics for duration:")
print(df['duration'].describe())

# Plot the campaign contact distribution
plt.figure(figsize=(10, 5))
sns.histplot(df['campaign'], bins=range(1, 40), kde=False)
plt.title('Number of Contacts per Client During the Campaign')
plt.xlabel('Number of Contacts')
plt.ylabel('Number of Clients')
plt.xlim(0, 35)  # Most clients were contacted less than 35 times
plt.tight_layout()
plt.show()

# Summary stats
print("Summary statistics for campaign contacts:")
print(df['campaign'].describe())

# Count how many have never been contacted before
never_contacted = df[df['pdays'] == -1].shape[0]
print(f"Clients never contacted before: {never_contacted}")

# Plot only those who were contacted before (pdays ≠ -1)
plt.figure(figsize=(10, 5))
sns.histplot(df[df['pdays'] != -1]['pdays'], bins=30, kde=True)
plt.title('Days Since Last Contact (Previous Campaign)')
plt.xlabel('Days')
plt.ylabel('Number of Clients')
plt.tight_layout()
plt.show()

# Plot distribution of 'previous' contacts
plt.figure(figsize=(10, 5))
sns.histplot(df['previous'], bins=30, kde=False)
plt.title('Number of Contacts Before the Current Campaign')
plt.xlabel('Previous Contacts')
plt.ylabel('Number of Clients')
plt.tight_layout()
plt.show()

# Optional: Summary statistics
print("Summary statistics for 'previous' contacts:")
print(df['previous'].describe())

# Count the previous outcomes
poutcome_counts = df['poutcome'].value_counts()
print("Previous Campaign Outcomes:")
print(poutcome_counts)

# Plot the outcomes
plt.figure(figsize=(7, 5))
sns.countplot(data=df, x='poutcome', order=poutcome_counts.index)
plt.title('Outcomes of Previous Marketing Campaigns')
plt.xlabel('Previous Campaign Outcome')
plt.ylabel('Number of Clients')
plt.tight_layout()
plt.show()

# Count the subscription values
subscription_counts = df['y'].value_counts()
print("Term Deposit Subscription Counts:")
print(subscription_counts)

# Calculate percentage
subscription_percent = df['y'].value_counts(normalize=True) * 100
print("\nSubscription Proportions (%):")
print(subscription_percent)

# Plot the result
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='y', order=subscription_counts.index)
plt.title('Subscription to Term Deposit')
plt.xlabel('Subscribed to Term Deposit')
plt.ylabel('Number of Clients')
plt.tight_layout()
plt.show()

# Convert target column to numeric: 'yes' = 1, 'no' = 0
df['y_numeric'] = df['y'].map({'yes': 1, 'no': 0})

# Select numeric columns for correlation
numeric_cols = ['age', 'balance', 'duration', 'campaign', 'pdays', 'previous', 'y_numeric']
correlation = df[numeric_cols].corr()

# Heatmap of correlations
plt.figure(figsize=(10, 6))
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Correlation Between Numeric Features and Term Deposit Subscription')
plt.tight_layout()
plt.show()
# Subscription rate by job
job_subscription = df.groupby('job')['y_numeric'].mean().sort_values(ascending=False)
print("Subscription rate by job:")
print(job_subscription)

# Plot
plt.figure(figsize=(10, 5))
sns.barplot(x=job_subscription.index, y=job_subscription.values)
plt.xticks(rotation=45)
plt.ylabel("Subscription Rate")
plt.title("Term Deposit Subscription Rate by Job")
plt.tight_layout()
plt.show()