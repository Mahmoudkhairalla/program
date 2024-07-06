class Product:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}"

class ProductManager:
    def __init__(self):
        self.products = []
        self.next_id = 1

    def list_products(self):
        if not self.products:
            print("No products found.")
        else:
            for product in self.products:
                print(product)

    def add_product(self, name):
        product = Product(self.next_id, name)
        self.products.append(product)
        print(f"Product '{name}' added with ID: {self.next_id}")
        self.next_id += 1

    def delete_product(self, name):
        found = False
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                found = True
                print(f"Product '{name}' deleted.")
                break
        if not found:
            print(f"Product '{name}' not found.")

    def delete_by_id(self, id):
        found = False
        for product in self.products:
            if product.id == id:
                self.products.remove(product)
                found = True
                print(f"Product with ID {id} deleted.")
                break
        if not found:
            print(f"Product with ID {id} not found.")

    def run(self):
        while True:
            print("\nMenu:")
            print("1. List products")
            print("2. Add product")
            print("3. Delete product by name")
            print("4. Delete product by ID")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                print("\nList of Products:")
                self.list_products()
            elif choice == '2':
                name = input("Enter product name to add: ")
                self.add_product(name)
            elif choice == '3':
                name = input("Enter product name to delete: ")
                self.delete_product(name)
            elif choice == '4':
                id = int(input("Enter product ID to delete: "))
                self.delete_by_id(id)
            elif choice == '5':
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    manager = ProductManager()
    manager.run()
