import time
class Student:
    def __init__(self, name, hometown, age, height, favorite_icecream, birthday_year, birthday_month, birthday_day):
        self.name = name
        self.hometown = hometown
        self.age = age
        self.height = str(height)
        self.favorite_icecream = favorite_icecream
        self.birthday_year = birthday_year
        self.birthday_month = birthday_month
        self.birthday_day = birthday_day

    def print_summary(self):
        print("This is ", self.name, ", ", self.name, " is ", self.age, " years old, and is ", self.height, " meeters tall and lives in ", self.hometown, ". ")
        print(self.name, "'s favorite ice cream flavor is ", self.favorite_icecream ,".")

    def get_giraffe_gap(self):
        average_giraffe = 500
        gap = average_giraffe - int(self.height)
        return gap
        print(gap)


    def get_days_to_birthday(self):
        epoch_to_birthday = time.mktime((int(self.birthday_year),int(self.birthday_month),int(self.birthday_day),0,0,0,0,0,0))
        age_in_seconds = time.time()- epoch_to_birthday
        age_in_years = age_in_seconds/(3600*24*365.25)
##        #print(age_in_years)
##        return age_in_years
        next_birthday_year = int(self.birthday_year) + int(age_in_years) +1
        seconds_till_birthday = time.mktime((next_birthday_year, int(self.birthday_month), int(self.birthday_day),0,0,0,0,0,0)) - time.time()
        days_till_birthday = seconds_till_birthday/(60*60*24)
        print(days_till_birthday)
        return days_till_birthday
