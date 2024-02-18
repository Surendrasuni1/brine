import csv
from collections import defaultdict
from datetime import datetime

def read_orders(filename):
    orders = []
    with open(filename, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            orders.append(row)
    return orders

def compute_monthly_revenue(orders):
    monthly_revenue = defaultdict(float)
    for order in orders:
        order_date = datetime.strptime(order['order_date'], '%Y-%m-%d')
        month_key = order_date.strftime('%Y-%m')
        monthly_revenue[month_key] += float(order['product_price']) * int(order['quantity'])
    return monthly_revenue

def compute_product_revenue(orders):
    product_revenue = defaultdict(float)
    for order in orders:
        product_revenue[order['product_name']] += float(order['product_price']) * int(order['quantity'])
    return product_revenue

def compute_customer_revenue(orders):
    customer_revenue = defaultdict(float)
    for order in orders:
        customer_revenue[order['customer_id']] += float(order['product_price']) * int(order['quantity'])
    return customer_revenue

def top_10_customers(customer_revenue):
    sorted_customers = sorted(customer_revenue.items(), key=lambda x: x[1], reverse=True)
    return sorted_customers[:10]

if __name__ == "__main__":
    orders = read_orders('orders.csv')
    
    monthly_revenue = compute_monthly_revenue(orders)
    print("Monthly revenue:")
    for month, revenue in monthly_revenue.items():
        print(f"{month}: ${revenue:.2f}")
    
    product_revenue = compute_product_revenue(orders)
    print("\nProduct revenue:")
    for product, revenue in product_revenue.items():
        print(f"{product}: ${revenue:.2f}")
    
    
    customer_revenue = compute_customer_revenue(orders)
    print("\nCustomer revenue:")    
    for customer_id, revenue in customer_revenue.items():
        print(f"Customer ID: {customer_id}, Revenue: ${revenue:.2f}")
    
    customer_revenue = compute_customer_revenue(orders)
    print("\nCustomer revenue:")
    top_customers = top_10_customers(customer_revenue)
    for customer_id, revenue in top_customers:
        print(f"Customer ID: {customer_id}, Revenue: ${revenue:.2f}")
