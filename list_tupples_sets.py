my_variable = "Hello World"

grade_one = 90
grade_two = 80
grade_three = 70

grades = [90, 80, 70]

print(grades[0])

grades.append(60)

tuple_grades = (90, 80, 70)

set_grades = {90, 80, 70, 60, 50, 40, 30, 20, 10}

print(set_grades)

set_grades.add(55)

print(set_grades)


## set operations

your_lottery_numbers = {1, 2, 3, 4, 5}
winning_numbers = {1, 3, 5, 7, 9, 11}

print(your_lottery_numbers.intersection(winning_numbers))
print(your_lottery_numbers.union(winning_numbers))
print({1, 2, 3, 4}.difference({1, 2}))

