# Check for missing values
print("Missing values in each column:")
print(df.isnull().sum())

# Check for duplicates
print(f"\nNumber of duplicate rows: {df.duplicated().sum()}")

# Convert Date column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Extract additional time features
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
df['DayOfWeek'] = df['Date'].dt.dayofweek
df['Quarter'] = df['Date'].dt.quarter

# Create age groups
bins = [0, 18, 30, 45, 60, 100]
labels = ['Teen', 'Young Adult', 'Adult', 'Middle Aged', 'Senior']
df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=labels)

# Check for any inconsistent data
print("\nUnique values in categorical columns:")
print("Gender:", df['Gender'].unique())
print("Product Category:", df['Product Category'].unique())

# Check for outliers in numerical columns
numerical_cols = ['Age', 'Quantity', 'Price per Unit', 'Total Amount']
print("\nStatistical summary of numerical columns:")
print(df[numerical_cols].describe())