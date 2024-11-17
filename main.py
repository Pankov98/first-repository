class Warrior():
    def __init__(self, name, power, endurance, hair_color):
        self.name = name
        self.power = power
        self.endurance = endurance
        self.hair_color = hair_color

    def sleep(self):
        print(f"{self.name} лег спать")
        self.endurance += 2

    def eat(self):
        print(f"{self.name} сел кушать ")
        self.power += 1

    def hit(self):
        print(f"{self.name} ударил")
        self.endurance -= 6


    def walk(self):
        print(f"{self.name} пошел гулять")

    def info(self):
        print(f"Имя: {self.name}")
        print(f"сила: {self.power}")
        print(f"выносливость: {self. endurance}")
        print(f"цвет волос: {self.hair_color}")
