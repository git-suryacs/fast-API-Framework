days_remaining = int(input("Enter the number of days until your next birthday - "))
weeks_remaining = days_remaining //7
print(f"the number of weeks remaining for your next birthday is {weeks_remaining}")

zoo = ['tiger','lion','snake','crow','cheetah']
zoo.pop(3)
zoo.append('elephant')
zoo.remove('cheetah')
print(zoo)
print(zoo[0:3])