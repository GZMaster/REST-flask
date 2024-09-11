my_variable = "Hello World"

for char in my_variable:
  print(char)
  
  my_list = [1, 2, 3, 4, 5]
  
  for number in my_list:
    print(number * 2)
    
    
user_wants_number = True

while user_wants_number == True:
    print(10)
    
    user_input = input("Should we print again? (y/n)")
    if user_input == "n":
        user_wants_number = False
        
        