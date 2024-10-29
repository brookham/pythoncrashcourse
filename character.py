class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def greet(self):
        print(f"My name is {self.name}")

    def instigate(self, opponent_name):
        print(f"A fow detected!!!")
        print(f"{self.name} attacks {opponent_name}!!")


character_1 = Character("Bronk", 100)
character_2 = Character("Hank", 125)


print(character_1.name, character_1.health)

print(character_2.name, character_2.health)

character_1.greet()

character_2.greet()

character_1.instigate(character_2.name)