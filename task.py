####------------------------Brine-python-task--------------------####
#                                                                   #
#                                                                   #
#                                                                   #
#                        AUTHOR:Surendra Salapu                     #
#                        DATE:18-02-2024                            #
#                                                                   #
#                                                                   #   
#                                                                   #
##################################################################### 



## importing necessary modules ##
import csv
from collections import defaultdict
from datetime import datetime

##function to read CSV file ##
def read_orders(filename):
    orders = []
    with open(filename, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            orders.append(row)
    return orders


## function to calculate monthly revenue ##
def compute_monthly_revenue(orders):
    monthly_revenue = defaultdict(float)
    for order in orders:
        order_date = datetime.strptime(order['order_date'], '%Y-%m-%d')
        month_key = order_date.strftime('%Y-%m')
        monthly_revenue[month_key] += float(order['product_price']) * int(order['quantity'])
    return monthly_revenue

## function to calculate product revenue ##
def compute_product_revenue(orders):
    product_revenue = defaultdict(float)
    for order in orders:
        product_revenue[order['product_name']] += float(order['product_price']) * int(order['quantity'])
    return product_revenue


## function to calculate customer revenue ##
def compute_customer_revenue(orders):
    customer_revenue = defaultdict(float)
    for order in orders:
        customer_revenue[order['customer_id']] += float(order['product_price']) * int(order['quantity'])
    return customer_revenue


## function to calculate top 10 customers revenue ##
def top_10_customers(customer_revenue):
    sorted_customers = sorted(customer_revenue.items(), key=lambda x: x[1], reverse=True)
    return sorted_customers[:10]


### main function where the execution starts ###
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
    print("\ntop_10_customers revenue:")
    top_customers = top_10_customers(customer_revenue)
    for customer_id, revenue in top_customers:
        print(f"Customer ID: {customer_id}, Revenue: ${revenue:.2f}")
