from creational.fluent_builder.pizza import Pizza


class PizzaBuilder:
    def __init__(self):
        self.garlic = False
        self.extra_cheese = False

    def add_garlic(self):
        self.garlic = True
        return self

    def add_extra_cheese(self):
        self.extra_cheese = True
        return self

    def build(self):
        pizza = Pizza()
        pizza.garlic = self.garlic
        pizza.extra_cheese = self.extra_cheese
        return pizza


if __name__ == "__main__":
    garlic_cheese_pizza = PizzaBuilder().add_garlic().add_extra_cheese().build()
    print(garlic_cheese_pizza)

