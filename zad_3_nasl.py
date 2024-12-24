class Product:
    def __init__(self, name, price, weight):
        self.__name = name
        self.__price = price
        self.__weight = weight

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight


class Buy(Product):
    def __init__(self, name, price, weight, quantity):
        super().__init__(name, price, weight)
        self.__quantity = quantity
        self.__total_price = self.__calculate_total_price()
        self.__total_weight = self.__calculate_total_weight()

    def __calculate_total_price(self):
        return self.price * self.__quantity

    def __calculate_total_weight(self):
        return self.weight * self.__quantity

    @property
    def total_price(self):
        return self.__total_price

    @property
    def total_weight(self):
        return self.__total_weight

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        self.__quantity = quantity
        self.__total_price = self.__calculate_total_price()  # Пересчитываем общую стоимость
        self.__total_weight = self.__calculate_total_weight()  # Пересчитываем общий вес


class Check(Buy):
    def __init__(self, name, price, weight, quantity):
        super().__init__(name, price, weight, quantity)

    def __str__(self):
        return (
            f"Товар: {self.name}\n"
            f"Цена за единицу: {self.price} руб.\n"
            f"Вес единицы товара: {self.weight} кг.\n"
            f"Количество: {self.quantity} шт.\n"
            f"Общая стоимость: {self.total_price} руб.\n"
            f"Общий вес: {self.total_weight} кг."
        )


purchase = Check("Яблоки", 50, 0.2, 10)

print(purchase)

print("\nИзменяем количество:")
purchase.quantity = 15
print(purchase)
