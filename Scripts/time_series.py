# Set Date as index for time series analysis
df_time = df.set_index('Date')

# Resample by month to see monthly trends
monthly_sales = df_time['Total Amount'].resample('M').sum()
monthly_transactions = df_time['Transaction ID'].resample('M').count()

# Create subplots for time series analysis
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))

# Monthly sales trend
ax1.plot(monthly_sales.index, monthly_sales.values, marker='o', linewidth=2)
ax1.set_title('Monthly Sales Trend', fontsize=16, fontweight='bold')
ax1.set_ylabel('Sales Amount ($)')
ax1.grid(True)

# Monthly transactions trend
ax2.plot(monthly_transactions.index, monthly_transactions.values, marker='o', color='green', linewidth=2)
ax2.set_title('Monthly Transactions Trend', fontsize=16, fontweight='bold')
ax2.set_ylabel('Number of Transactions')
ax2.grid(True)

plt.tight_layout()
plt.savefig('time_series_analysis.png', dpi=300, bbox_inches='tight')
plt.show()

# Analyze seasonal patterns
monthly_avg_sales = df_time['Total Amount'].resample('M').mean()
quarterly_sales = df_time['Total Amount'].resample('Q').sum()

# Create a heatmap of sales by month and year
pivot_table = pd.pivot_table(df, values='Total Amount', index=df['Date'].dt.year, 
                            columns=df['Date'].dt.month, aggfunc='sum')

plt.figure(figsize=(12, 6))
sns.heatmap(pivot_table, cmap='YlGnBu', annot=True, fmt=".0f", linewidths=.5)
plt.title('Sales Heatmap by Year and Month', fontsize=16, fontweight='bold')
plt.xlabel('Month')
plt.ylabel('Year')
plt.tight_layout()
plt.savefig('sales_heatmap.png', dpi=300, bbox_inches='tight')
plt.show()