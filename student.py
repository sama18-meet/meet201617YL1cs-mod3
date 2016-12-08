class Student:
    def __init__(self, name, hometown, age, height, favorite_icecream):
        self.name = name
        self.hometown = hometown
        self.age = age
        self.height = str(height)
        self.favorite_icecream = favorite_icecream

    def print_summary(self):
        print("This is ", self.name, ", ", self.name, " is ", self.age, " years old, and is ", self.height, " meeters tall and lives in ", self.hometown, ". ")
        print(self.name, "'s favorite ice cream flavor is ", self.favorite_icecream ,".")

    def get_giraffe_gap(self):
        average_giraffe = 500
        gap = average_giraffe - int(self.height)
        return gap
        print(gap)
