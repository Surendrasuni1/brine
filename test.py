import unittest

from task import compute_customer_revenue, compute_monthly_revenue, compute_product_revenue, top_10_customers

class TestOrderAnalysis(unittest.TestCase):
    def setUp(self):
        self.orders = [
            {'order_id': '1', 'customer_id': '101', 'order_date': '2023-01-01',
             'product_id': '1', 'product_name': 'Product A', 'product_price': '10', 'quantity': '2'},
            {'order_id': '2', 'customer_id': '102', 'order_date': '2023-01-15',
             'product_id': '2', 'product_name': 'Product B', 'product_price': '15', 'quantity': '1'},
            {'order_id': '3', 'customer_id': '101', 'order_date': '2023-02-01',
             'product_id': '1', 'product_name': 'Product A', 'product_price': '10', 'quantity': '3'}
        ]

    def test_compute_monthly_revenue(self):
        monthly_revenue = compute_monthly_revenue(self.orders)
        self.assertEqual(monthly_revenue['2023-01'], 35)
        self.assertEqual(monthly_revenue['2023-02'], 30)

    def test_compute_product_revenue(self):
        product_revenue = compute_product_revenue(self.orders)
        self.assertEqual(product_revenue['Product A'], 50)
        self.assertEqual(product_revenue['Product B'], 15)

    def test_compute_customer_revenue(self):
        customer_revenue = compute_customer_revenue(self.orders)
        self.assertEqual(customer_revenue['101'], 50)
        self.assertEqual(customer_revenue['102'], 15)

    def test_top_10_customers(self):
        customer_revenue = compute_customer_revenue(self.orders)
        top_customers = top_10_customers(customer_revenue)
        self.assertEqual(len(top_customers), 2)
        self.assertEqual(top_customers[0][0], '101')
        self.assertEqual(top_customers[0][1], 50)

if __name__ == "__main__":
    unittest.main()
