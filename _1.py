class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        with open(self.__file_name, 'r') as file:
            return file.read()
            file.close()

    def add(self, *products):
        for product in products:
            with open(self.__file_name, 'r') as check_file:
                if product.name in check_file.read():
                    print(f'Product {product.name} Продукт уже есть в магазине')
                else:
                    with open(self.__file_name, 'a') as file:
                        file.write(str(product) + '\n')
                        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)

print(s1.get_products())
