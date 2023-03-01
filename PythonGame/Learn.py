"""def add(a, b):
 print(f'First sign is: {a}', f'Second sign is: {b}')
 total = a + b
 print(f'Score is: {total}')


def print_range(a, b):
 for i in range(a, b, +1):
 print(i)


def print_star(num):
 stars = ""
 for i in range(num):
 stars += "*"
 print(stars)


def print_square(size):
 for i in range(size):
 print_star(size)


def print_triangle(size):
 for i in range(size):
 print_star(i+1)


add(2, 5)
print_range(2, 10)
print_star(5)
print_square(6)
print_triangle(3)



def days_to_millisecond(days):
# 24000 - bo 1 milisek to 1000 sek, a 24 to ilość godzin w dniu
# 3600 - bo 60 min ma godzina, a min ma 60 sek
 return days * 24000 * 3600


def square_triangle_area(a, b):
 return a * b / 2


def biggest(a, b, c):
 if a >= b and a >= c:
 return a
 elif b >= c:
 return b
 else:
 return c


def sum_range(a, b):
 res = 0
 for i in range(a, b):
 res += i
 return res


print(days_to_millisecond(3))
print(square_triangle_area(1, 1))
print(biggest(2, 3, 1))
print(sum_range(2, 5))

class Player:
 pass


player = Player()
player.points = 0
print(player.points)
player.points = 1
print(player.points)
class BankAccount:
 def __init__(self):
 self.balance = 0

 def deposit(self, amount):
 self.balance += amount

 def withdraw(self, amount):
 if amount <= self.balance:
 self.balance -= amount
 return True
 else:
 return False


account = BankAccount()
account1 = BankAccount()
account2 = BankAccount()
print(account.balance)
account.deposit(1000)
print(account.balance)
account.deposit(2000)
print(account.balance)
res = account.withdraw(1500)
print(res)
print(account.balance)
res = account.withdraw(2000)
print(res)
print(account.balance)
account1.deposit(1000)
print(account1.balance)
print(account2.balance)

age = input('Please write here your age: ')
print(f"You're age is: {age}")

letters = ["A", "B", "C", "D", "E", "F"]
print(len(letters))
print(letters[4])

numbers = [5, 6, 7, 8, 9, 10, 11, 12]
print(len(numbers))
print(numbers[3])

l1 = ["A", "B"]
l2 = ["D", "E"]
letters = l1 + l2
l1Copy = l1[:]
print(letters)

l1.append("C")
print(l1)
print(letters)
print(l1Copy)

names = ["Jola", "Marcin", "Kamil", "Maja", "Stefan"]
m_names = [name for name in names if name[0] == 'M']
print(m_names)

m_names = []
for name in names:
 if name[0] == 'M':
 m_names.append(name)
print(m_names)

names = ["michał", "nela", "ola", "przemek"]
first_big_names = [name.capitalize() for name in names]
print(first_big_names)

woman_names = tuple(name.capitalize()for name in names if name[-1] == 'a')
print(woman_names)

len_names = 0
for name in names:
 len_names += len(name)
print(len_names)

"""