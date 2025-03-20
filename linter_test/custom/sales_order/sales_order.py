import frappe

def this_is_test_method(self):
    # This method is called when the test method is run
    # Here, we're fetching a record from the database and printing its data
    customer = frappe.get_doc('Customer', 'Customer-1')
    print(f'Customer Name: {customer.customer_name}')
    print(f'Customer Email: {customer.email}')
    
def test_create(self):
  # This test method creates a new customer record
  print(f'Customer Name Name    ' + self.customer)                   