# Customer demographics analysis
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Gender distribution
gender_counts = df['Gender'].value_counts()
axes[0, 0].pie(gender_counts.values, labels=gender_counts.index, autopct='%1.1f%%', startangle=90)
axes[0, 0].set_title('Customer Gender Distribution', fontweight='bold')

# Age distribution
axes[0, 1].hist(df['Age'], bins=20, edgecolor='black', alpha=0.7)
axes[0, 1].set_xlabel('Age')
axes[0, 1].set_ylabel('Frequency')
axes[0, 1].set_title('Customer Age Distribution', fontweight='bold')

# Age group distribution
age_group_counts = df['Age Group'].value_counts()
axes[1, 0].bar(age_group_counts.index.astype(str), age_group_counts.values)
axes[1, 0].set_xlabel('Age Group')
axes[1, 0].set_ylabel('Count')
axes[1, 0].set_title('Customer Age Group Distribution', fontweight='bold')
axes[1, 0].tick_params(axis='x', rotation=45)

# Product category distribution
category_counts = df['Product Category'].value_counts()
axes[1, 1].bar(category_counts.index, category_counts.values)
axes[1, 1].set_xlabel('Product Category')
axes[1, 1].set_ylabel('Count')
axes[1, 1].set_title('Product Category Distribution', fontweight='bold')
axes[1, 1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig('customer_demographics.png', dpi=300, bbox_inches='tight')
plt.show()

# Analyze purchasing behavior by demographic
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Average purchase amount by gender
gender_avg = df.groupby('Gender')['Total Amount'].mean()
axes[0, 0].bar(gender_avg.index, gender_avg.values)
axes[0, 0].set_title('Average Purchase Amount by Gender', fontweight='bold')
axes[0, 0].set_ylabel('Average Amount ($)')

# Average purchase amount by age group
age_group_avg = df.groupby('Age Group')['Total Amount'].mean()
axes[0, 1].bar(age_group_avg.index.astype(str), age_group_avg.values)
axes[0, 1].set_title('Average Purchase Amount by Age Group', fontweight='bold')
axes[0, 1].set_ylabel('Average Amount ($)')
axes[0, 1].tick_params(axis='x', rotation=45)

# Popular products by gender
gender_category = pd.crosstab(df['Gender'], df['Product Category'])
gender_category.plot(kind='bar', ax=axes[1, 0])
axes[1, 0].set_title('Product Category Preference by Gender', fontweight='bold')
axes[1, 0].set_ylabel('Count')
axes[1, 0].tick_params(axis='x', rotation=0)

# Popular products by age group
age_category = pd.crosstab(df['Age Group'], df['Product Category'])
age_category.plot(kind='bar', ax=axes[1, 1])
axes[1, 1].set_title('Product Category Preference by Age Group', fontweight='bold')
axes[1, 1].set_ylabel('Count')
axes[1, 1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig('purchasing_behavior.png', dpi=300, bbox_inches='tight')
plt.show()

# Top customers by total spending
top_customers = df.groupby('Customer ID')['Total Amount'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(12, 6))
top_customers.plot(kind='bar')
plt.title('Top 10 Customers by Total Spending', fontweight='bold')
plt.ylabel('Total Amount ($)')
plt.xlabel('Customer ID')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('top_customers.png', dpi=300, bbox_inches='tight')
plt.show()