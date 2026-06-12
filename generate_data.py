import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

categories = {
    'Electronics': ['Wireless Earbuds', 'Smartphone Case', 'Bluetooth Speaker', 'Power Bank', 'USB-C Cable', 'Smartwatch', 'Laptop Stand', 'Webcam'],
    'Home & Kitchen': ['Air Fryer', 'Coffee Maker', 'Knife Set', 'Storage Containers', 'Blender', 'Cutting Board', 'Dish Rack', 'Vacuum Cleaner'],
    'Clothing': ['Men T-Shirt', 'Women Kurti', 'Denim Jeans', 'Running Shoes', 'Hoodie', 'Formal Shirt', 'Yoga Pants', 'Jacket'],
    'Beauty & Personal Care': ['Face Serum', 'Shampoo', 'Sunscreen', 'Lipstick', 'Hair Dryer', 'Electric Trimmer', 'Body Lotion', 'Perfume'],
    'Books': ['Fiction Novel', 'Self-Help Book', 'Children Storybook', 'Cookbook', 'Biography', 'Comic Book'],
    'Sports & Fitness': ['Yoga Mat', 'Dumbbell Set', 'Resistance Bands', 'Cycling Helmet', 'Skipping Rope', 'Gym Bag'],
    'Toys & Games': ['Building Blocks', 'Remote Control Car', 'Puzzle Set', 'Board Game', 'Action Figure', 'Soft Toy'],
    'Office Products': ['Notebook Set', 'Office Chair', 'Desk Organizer', 'Printer Ink', 'Whiteboard', 'Backpack']
}

price_ranges = {
    'Electronics': (499, 8999), 'Home & Kitchen': (299, 6999), 'Clothing': (299, 2999),
    'Beauty & Personal Care': (149, 2499), 'Books': (99, 999), 'Sports & Fitness': (199, 4999),
    'Toys & Games': (149, 1999), 'Office Products': (99, 12999)
}

cities = ['Bengaluru', 'Mumbai', 'Delhi', 'Hyderabad', 'Chennai', 'Pune', 'Kolkata', 'Ahmedabad', 'Jaipur', 'Lucknow', 'Surat', 'Kochi']
states_map = {
    'Bengaluru': 'Karnataka', 'Mumbai': 'Maharashtra', 'Delhi': 'Delhi', 'Hyderabad': 'Telangana',
    'Chennai': 'Tamil Nadu', 'Pune': 'Maharashtra', 'Kolkata': 'West Bengal', 'Ahmedabad': 'Gujarat',
    'Jaipur': 'Rajasthan', 'Lucknow': 'Uttar Pradesh', 'Surat': 'Gujarat', 'Kochi': 'Kerala'
}
channels = ['Amazon App', 'Amazon Web', 'Alexa Voice Order']
payment_modes = ['Prepaid - Card', 'Prepaid - UPI', 'Prepaid - Wallet', 'Cash on Delivery', 'Prepaid - Net Banking']
order_status = ['Delivered', 'Cancelled', 'Returned', 'Shipped - In Transit']
status_weights = [0.82, 0.06, 0.07, 0.05]
customer_segments = ['Prime', 'Non-Prime']

n_orders = 12000
start_date = datetime(2025, 1, 1)
end_date = datetime(2025, 12, 31)
date_range_days = (end_date - start_date).days

# seasonality weights by month (festive boosts: Jan sale, Aug-Oct festive, Nov Black Friday/Diwali, Dec year end)
month_weight = {1: 1.3, 2: 0.9, 3: 0.95, 4: 0.9, 5: 0.95, 6: 1.0, 7: 1.0, 8: 1.1, 9: 1.2, 10: 1.5, 11: 1.6, 12: 1.3}

rows = []
order_id_start = 100000

for i in range(n_orders):
    # weighted date sampling by month
    month = np.random.choice(list(month_weight.keys()), p=np.array(list(month_weight.values()))/sum(month_weight.values()))
    day = np.random.randint(1, 29)
    order_date = datetime(2025, month, day) + timedelta(hours=np.random.randint(0,24), minutes=np.random.randint(0,60))

    category = np.random.choice(list(categories.keys()), p=[0.22,0.16,0.18,0.13,0.06,0.10,0.08,0.07])
    product = np.random.choice(categories[category])
    low, high = price_ranges[category]
    price = round(np.random.uniform(low, high), -1) if high > 1000 else round(np.random.uniform(low, high))
    
    qty = np.random.choice([1,1,1,1,2,2,3], p=[0.45,0.2,0.1,0.05,0.1,0.07,0.03])
    discount_pct = np.random.choice([0,5,10,15,20,25,30,40,50], p=[0.15,0.1,0.15,0.15,0.15,0.1,0.1,0.05,0.05])
    
    # festive months get higher discounts
    if month in [10,11]:
        discount_pct = min(discount_pct + np.random.choice([0,5,10]), 60)

    gross_amount = price * qty
    discount_amount = round(gross_amount * discount_pct/100, 2)
    net_amount = round(gross_amount - discount_amount, 2)
    
    city = np.random.choice(cities)
    state = states_map[city]
    channel = np.random.choice(channels, p=[0.6,0.32,0.08])
    payment = np.random.choice(payment_modes, p=[0.28,0.35,0.07,0.20,0.10])
    segment = np.random.choice(customer_segments, p=[0.55,0.45])
    status = np.random.choice(order_status, p=status_weights)
    
    rating = np.nan
    if status == 'Delivered':
        rating = np.random.choice([5,4,3,2,1, np.nan], p=[0.40,0.28,0.12,0.05,0.05,0.10])
    
    delivery_days = np.random.choice([1,2,3,4,5,6,7], p=[0.10,0.25,0.25,0.18,0.12,0.06,0.04]) if status in ['Delivered','Shipped - In Transit'] else np.nan
    
    customer_id = f"CUST{np.random.randint(1,4500):05d}"
    
    rows.append([
        order_id_start+i, order_date.strftime('%Y-%m-%d'), order_date.strftime('%H:%M:%S'),
        customer_id, segment, category, product, qty, price, gross_amount,
        discount_pct, discount_amount, net_amount, city, state, channel, payment,
        status, rating, delivery_days
    ])

df = pd.DataFrame(rows, columns=[
    'Order_ID','Order_Date','Order_Time','Customer_ID','Customer_Segment','Category','Product',
    'Quantity','Unit_Price','Gross_Amount','Discount_Pct','Discount_Amount','Net_Amount',
    'City','State','Sales_Channel','Payment_Method','Order_Status','Rating','Delivery_Days'
])

df = df.sort_values('Order_ID').reset_index(drop=True)
df.to_csv('/home/claude/amazon_sales_project/data/amazon_sales_2025.csv', index=False)
print(df.shape)
print(df.head())
print(df['Order_Status'].value_counts())
print(f"Total Net Revenue: {df['Net_Amount'].sum():,.0f}")
