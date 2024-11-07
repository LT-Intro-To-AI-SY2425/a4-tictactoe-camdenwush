# object oriented programming

# (define-struct dog [fur_color name age favorite_food])

class Dog:
    species = "canis not typing that"
    
    def __init__(self, n = "no name", a = 0):
        self.name = n
        self.age = a
        self.fetch_count = 0

    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
    def play_fetch(self, num_fetch):
        self.fetch_count += num_fetch

    def fetch_reset(self):
        self.fetch_count = 0

logan = Dog("logan", 8)
becker = Dog("becker", 4)
kepa = Dog("kepa", 4)

print(logan.fetch_count)

logan.play_fetch(5)

print(logan.fetch_count)

logan.play_fetch(3)

print(logan.fetch_count)

logan.fetch_reset()

print(logan.fetch_count)