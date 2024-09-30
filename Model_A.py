# After Code Review Changes
# order_processor.py

import time

def process_order(order):
	print(f"Processing order: {order['id']}")

	# Check for out-of-stock items (NFR improvement)
	if order['item_quantity'] <= 0:
		print(f"Order {order['id']} failed: Item is out of stock.")
		return

	# Simulate delay for real-time processing
	time.sleep(2)
	print(f"Order {order['id']} processed successfully.")

if __name__ == "__main__":
	order = {'id': 1, 'item_quantity': 1}
	process_order(order)