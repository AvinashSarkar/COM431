class Cat:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def eat(self):
        self.weight += 1
        print(f"{self.name} ate some food now weighs {self.weight} kg")

    def walk(self):
        if self.weight > 1:
            self.weight -= 1
            print(f"{self.name} went for a walk and now weighs {self.weight} kg")
        else:
            print(f"{self.name} is too weak to walk")

    def print_details(self):
        print(f"Cat: {self.name}, Weight: {self.weight} kg")



