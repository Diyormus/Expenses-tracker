number_of_products = int(input("Enter the number of products: "))

product_list = []
total_price = 0

for i in range(number_of_products):
    products_name = str(input("Enter the name of your product: "))
    products_price = float(input("Enter the price of your product: "))
    product_list.append(products_name)  # Add product name to the list
    total_price += products_price  # Add product price to the total

print("\n".join(product_list))  # Print each product name on a new line
print(f"Total Price: {total_price}")  # Print the total price
