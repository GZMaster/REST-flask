def methodception(another):
    return another()

def add_two_numbers():
    return 35 + 77

# print(methodception(add_two_numbers))

# print(methodception(lambda: 35 + 77))

my_list = [13, 45, 67, 89, 11, 34, 56, 78, 90]

print(list(filter(lambda x: x != 13, my_list)))

(lambda x: x * 3)(5)

def f(x):
    return x * 3

print(f(5))