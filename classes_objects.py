lottery_player_dict = {
  "name": "Rolf",
  "numbers": (5, 9, 12, 3, 1, 21) 
}

class LotteryPlayer:
  def __init__(self, name):
    self.name = name
    self.numbers = (5, 9, 12, 3, 1, 21)
    
  def total(self):
    return sum(self.numbers)
    
player = LotteryPlayer("John")

# print(player.name)
# print(player.numbers)
# print(player.total())

player_one = LotteryPlayer("John")
player_two = LotteryPlayer("Jane")

# print(player_one == player_two)


##

class Student:
  def __init__(self, name, school):
    self.name = name
    self.school = school
    self.marks = []
    
  def average(self):
    return sum(self.marks) / len(self.marks)
    


rolf = Student("Rolf", "MIT")

rolf.marks.append(56)
rolf.marks.append(71)

print(rolf.average())
