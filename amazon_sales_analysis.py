"""
Amazon Sales 2025 - Python Analysis
Covers: data cleaning, EDA, KPI computation, visualizations, and insights export.
Libraries: pandas, numpy, matplotlib, seaborn
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set_style('whitegrid')
plt.rcParams['figure.dpi'] = 110

DATA_PATH = '/home/claude/amazon_sales_project/data/amazon_sales_2025.csv'
OUT_DIR = '/home/claude/amazon_sales_project/python/charts'
os.makedirs(OUT_DIR, exist_ok=True)

# ----------------------------------------------------------
# 1. LOAD & CLEAN
# ----------------------------------------------------------
df = pd.read_csv(DATA_PATH, parse_dates=['Order_Date'])
df['Month'] = df['Order_Date'].dt.month
df['Month_Name'] = df['Order_Date'].dt.strftime('%b')
df['Weekday'] = df['Order_Date'].dt.day_name()

print("Shape:", df.shape)
print("\nMissing values:\n", df.isnull().sum())
print("\nDuplicate Order_IDs:", df['Order_ID'].duplicated().sum())

# Valid (non-cancelled) orders for revenue analysis
valid = df[df['Order_Status'] != 'Cancelled'].copy()

# ----------------------------------------------------------
# 2. KPI SUMMARY
# ----------------------------------------------------------
total_revenue = valid['Net_Amount'].sum()
total_orders = len(valid)
aov = valid['Net_Amount'].mean()
return_rate = (df['Order_Status'] == 'Returned').mean() * 100
cancel_rate = (df['Order_Status'] == 'Cancelled').mean() * 100

print(f"\n--- KPI SUMMARY ---")
print(f"Total Net Revenue: ₹{total_revenue:,.0f}")
print(f"Total Valid Orders: {total_orders:,}")
print(f"Average Order Value (AOV): ₹{aov:,.2f}")
print(f"Return Rate: {return_rate:.2f}%")
print(f"Cancellation Rate: {cancel_rate:.2f}%")

# ----------------------------------------------------------
# 3. MONTHLY REVENUE TREND
# ----------------------------------------------------------
monthly = valid.groupby(valid['Order_Date'].dt.to_period('M'))['Net_Amount'].sum().reset_index()
monthly['Order_Date'] = monthly['Order_Date'].astype(str)

plt.figure(figsize=(10,5))
plt.plot(monthly['Order_Date'], monthly['Net_Amount'], marker='o', color='#FF9900', linewidth=2)
plt.title('Monthly Net Revenue - 2025', fontsize=13, fontweight='bold')
plt.ylabel('Net Revenue (₹)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f'{OUT_DIR}/01_monthly_revenue_trend.png')
plt.close()

# ----------------------------------------------------------
# 4. REVENUE BY CATEGORY
# ----------------------------------------------------------
cat_rev = valid.groupby('Category')['Net_Amount'].sum().sort_values(ascending=False)

plt.figure(figsize=(10,5))
sns.barplot(x=cat_rev.values, y=cat_rev.index, palette='viridis')
plt.title('Revenue by Category - 2025', fontsize=13, fontweight='bold')
plt.xlabel('Net Revenue (₹)')
plt.tight_layout()
plt.savefig(f'{OUT_DIR}/02_revenue_by_category.png')
plt.close()

# ----------------------------------------------------------
# 5. TOP 10 PRODUCTS
# ----------------------------------------------------------
top_products = valid.groupby('Product')['Net_Amount'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,5))
sns.barplot(x=top_products.values, y=top_products.index, palette='mako')
plt.title('Top 10 Products by Revenue', fontsize=13, fontweight='bold')
plt.xlabel('Net Revenue (₹)')
plt.tight_layout()
plt.savefig(f'{OUT_DIR}/03_top10_products.png')
plt.close()

# ----------------------------------------------------------
# 6. ORDER STATUS DISTRIBUTION
# ----------------------------------------------------------
status_counts = df['Order_Status'].value_counts()

plt.figure(figsize=(7,7))
plt.pie(status_counts.values, labels=status_counts.index, autopct='%1.1f%%',
        colors=sns.color_palette('Set2'), startangle=140)
plt.title('Order Status Distribution', fontsize=13, fontweight='bold')
plt.tight_layout()
plt.savefig(f'{OUT_DIR}/04_order_status_pie.png')
plt.close()

# ----------------------------------------------------------
# 7. TOP CITIES BY REVENUE
# ----------------------------------------------------------
city_rev = valid.groupby('City')['Net_Amount'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,5))
sns.barplot(x=city_rev.values, y=city_rev.index, palette='rocket')
plt.title('Top 10 Cities by Revenue', fontsize=13, fontweight='bold')
plt.xlabel('Net Revenue (₹)')
plt.tight_layout()
plt.savefig(f'{OUT_DIR}/05_top_cities.png')
plt.close()

# ----------------------------------------------------------
# 8. DISCOUNT vs REVENUE / AOV
# ----------------------------------------------------------
bins = [-1,0,10,20,30,50,100]
labels = ['0%','1-10%','11-20%','21-30%','31-50%','50%+']
valid['Discount_Band'] = pd.cut(valid['Discount_Pct'], bins=bins, labels=labels)
disc_summary = valid.groupby('Discount_Band').agg(orders=('Order_ID','count'), revenue=('Net_Amount','sum'), aov=('Net_Amount','mean')).reset_index()

fig, ax1 = plt.subplots(figsize=(10,5))
sns.barplot(data=disc_summary, x='Discount_Band', y='revenue', color='#FF9900', ax=ax1)
ax1.set_ylabel('Net Revenue (₹)')
ax2 = ax1.twinx()
sns.lineplot(data=disc_summary, x='Discount_Band', y='aov', marker='o', color='navy', ax=ax2)
ax2.set_ylabel('AOV (₹)')
plt.title('Discount Band vs Revenue & AOV', fontsize=13, fontweight='bold')
plt.tight_layout()
plt.savefig(f'{OUT_DIR}/06_discount_impact.png')
plt.close()

# ----------------------------------------------------------
# 9. CUSTOMER SEGMENT (PRIME vs NON-PRIME)
# ----------------------------------------------------------
seg_summary = valid.groupby('Customer_Segment').agg(
    orders=('Order_ID','count'), revenue=('Net_Amount','sum'), aov=('Net_Amount','mean')).reset_index()
print("\nCustomer Segment Summary:\n", seg_summary)

# ----------------------------------------------------------
# 10. RETURN RATE BY CATEGORY
# ----------------------------------------------------------
return_rate_cat = df.groupby('Category').apply(
    lambda x: (x['Order_Status']=='Returned').mean()*100).sort_values(ascending=False)

plt.figure(figsize=(10,5))
sns.barplot(x=return_rate_cat.values, y=return_rate_cat.index, palette='flare')
plt.title('Return Rate (%) by Category', fontsize=13, fontweight='bold')
plt.xlabel('Return Rate (%)')
plt.tight_layout()
plt.savefig(f'{OUT_DIR}/07_return_rate_by_category.png')
plt.close()

# ----------------------------------------------------------
# 11. CORRELATION HEATMAP (numeric features)
# ----------------------------------------------------------
num_cols = ['Quantity','Unit_Price','Discount_Pct','Net_Amount','Rating','Delivery_Days']
plt.figure(figsize=(8,6))
sns.heatmap(valid[num_cols].corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap', fontsize=13, fontweight='bold')
plt.tight_layout()
plt.savefig(f'{OUT_DIR}/08_correlation_heatmap.png')
plt.close()

# ----------------------------------------------------------
# 12. EXPORT CLEANED/SUMMARY DATA FOR EXCEL / POWER BI
# ----------------------------------------------------------
monthly.to_csv('/home/claude/amazon_sales_project/python/monthly_revenue_summary.csv', index=False)
cat_rev.to_csv('/home/claude/amazon_sales_project/python/category_revenue_summary.csv')
df.to_csv('/home/claude/amazon_sales_project/python/amazon_sales_2025_cleaned.csv', index=False)

print("\nAll charts saved to:", OUT_DIR)
print("Cleaned data + summaries exported.")
