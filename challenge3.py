"""Dado dos diccionarios 1 de productos y el 2 de categoría, conocer un 3 que permita tener el nombre del producto y el nombre de su categoría ejemplo.
"""
# Dictionary for categories
categories = {
    101: {
        "id": 101,
        "name": "Utiles escolares"
    },
    102: {
        "id": 102,
        "name": "Aseo"
    }
}

# Dictionary for products
products = {
    1: {
        "id": 1,
        "name": "Libreta",
        "price": 12.500,
        "id_cat": 101
    },
    2: {
        "id": 2,
        "name": "Jabón",
        "price": 10.500,
        "id_cat": 102
    }
}


# Function to get the name of a product and its category
def get_product_and_category(product_id):
    try:
        # Convert input to integer
        product_id = int(product_id)
        
        # Check if the product exists
        if product_id not in products:
            return "Product not found"
        
        # Get the product
        product = products[product_id]
        
        # Get the category
        category = categories[product["id_cat"]]
        
        # Return the product and category names using f-strings
        return f"Product: {product['name']}\nCategory: {category['name']}"
    
    except ValueError:
        return "Invalid input. Please enter a valid product ID."


product_id = input("Enter the product ID: ")
print(get_product_and_category(product_id))











