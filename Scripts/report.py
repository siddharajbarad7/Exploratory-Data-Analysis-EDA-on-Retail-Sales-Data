# Generate a summary report
print("RETAIL SALES DATA ANALYSIS - SUMMARY REPORT")
print("=" * 60)

# Key metrics
total_sales = df['Total Amount'].sum()
avg_transaction = df['Total Amount'].mean()
total_customers = df['Customer ID'].nunique()
total_transactions = df['Transaction ID'].nunique()

print(f"\nKey Metrics:")
print(f"Total Sales: ${total_sales:,.2f}")
print(f"Average Transaction Value: ${avg_transaction:.2f}")
print(f"Total Customers: {total_customers}")
print(f"Total Transactions: {total_transactions}")

# Top performing categories
top_category = df.groupby('Product Category')['Total Amount'].sum().idxmax()
top_category_sales = df.groupby('Product Category')['Total Amount'].sum().max()

print(f"\nTop Performing Category: {top_category} (${top_category_sales:,.2f})")

# Customer demographics summary
gender_dist = df['Gender'].value_counts(normalize=True) * 100
print(f"\nCustomer Gender Distribution: {gender_dist['Female']:.1f}% Female, {gender_dist['Male']:.1f}% Male")

# Average age of customers
avg_age = df['Age'].mean()
print(f"Average Customer Age: {avg_age:.1f} years")

# Time-based insights
monthly_avg_sales = monthly_sales.mean()
best_month = monthly_sales.idxmax().strftime('%B %Y')
best_month_sales = monthly_sales.max()

print(f"\nTime-Based Insights:")
print(f"Average Monthly Sales: ${monthly_avg_sales:,.2f}")
print(f"Best Performing Month: {best_month} (${best_month_sales:,.2f})")

# Recommendations
print("\nRECOMMENDATIONS")
print("=" * 60)
print("1. Focus on Electronics category as it generates the highest revenue.")
print("2. Target marketing efforts toward Male customers who show higher average transaction values.")
print("3. Develop loyalty programs for high-value customers to increase retention.")
print("4. Consider promotions during low-sales months to balance revenue throughout the year.")
print("5. Explore opportunities to increase sales in Beauty category through bundled offerings.")
print("6. Implement customer segmentation strategies for personalized marketing campaigns.")
print("7. Analyze the reasons behind higher sales on certain days of the week to optimize operations.")

# Save the report to a text file
with open('retail_sales_analysis_report.txt', 'w') as f:
    f.write("RETAIL SALES DATA ANALYSIS - SUMMARY REPORT\n")
    f.write("=" * 60 + "\n")
    f.write(f"\nKey Metrics:\n")
    f.write(f"Total Sales: ${total_sales:,.2f}\n")
    f.write(f"Average Transaction Value: ${avg_transaction:.2f}\n")
    f.write(f"Total Customers: {total_customers}\n")
    f.write(f"Total Transactions: {total_transactions}\n")
    f.write(f"\nTop Performing Category: {top_category} (${top_category_sales:,.2f})\n")
    f.write(f"\nCustomer Gender Distribution: {gender_dist['Female']:.1f}% Female, {gender_dist['Male']:.1f}% Male\n")
    f.write(f"Average Customer Age: {avg_age:.1f} years\n")
    f.write(f"\nTime-Based Insights:\n")
    f.write(f"Average Monthly Sales: ${monthly_avg_sales:,.2f}\n")
    f.write(f"Best Performing Month: {best_month} (${best_month_sales:,.2f})\n")
    f.write("\nRECOMMENDATIONS\n")
    f.write("=" * 60 + "\n")
    f.write("1. Focus on Electronics category as it generates the highest revenue.\n")
    f.write("2. Target marketing efforts toward Male customers who show higher average transaction values.\n")
    f.write("3. Develop loyalty programs for high-value customers to increase retention.\n")
    f.write("4. Consider promotions during low-sales months to balance revenue throughout the year.\n")
    f.write("5. Explore opportunities to increase sales in Beauty category through bundled offerings.\n")
    f.write("6. Implement customer segmentation strategies for personalized marketing campaigns.\n")
    f.write("7. Analyze the reasons behind higher sales on certain days of the week to optimize operations.\n")

print("\nAnalysis complete! Report saved to 'retail_sales_analysis_report.txt'")