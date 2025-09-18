# Calculate basic statistics
print("DESCRIPTIVE STATISTICS")
print("=" * 50)

# Overall statistics
print("Overall Sales Statistics:")
print(f"Total Sales: ${df['Total Amount'].sum():,.2f}")
print(f"Average Transaction Value: ${df['Total Amount'].mean():.2f}")
print(f"Median Transaction Value: ${df['Total Amount'].median():.2f}")
print(f"Standard Deviation: ${df['Total Amount'].std():.2f}")
print(f"Minimum Transaction: ${df['Total Amount'].min():.2f}")
print(f"Maximum Transaction: ${df['Total Amount'].max():.2f}")

# Statistics by gender
print("\nSales Statistics by Gender:")
gender_stats = df.groupby('Gender')['Total Amount'].agg(['sum', 'mean', 'count'])
print(gender_stats)

# Statistics by product category
print("\nSales Statistics by Product Category:")
category_stats = df.groupby('Product Category')['Total Amount'].agg(['sum', 'mean', 'count'])
print(category_stats)

# Statistics by age group
print("\nSales Statistics by Age Group:")
age_stats = df.groupby('Age Group')['Total Amount'].agg(['sum', 'mean', 'count'])
print(age_stats)