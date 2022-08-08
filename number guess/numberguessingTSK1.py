
import random

#initial_range=input("Enter initial range: ")
print("________________\n")
final_range = input("Enter End Range: ")

if final_range.isdigit():
    final_range = int(final_range) #checking if the input is int or not


l=6   #chances
n=random.randint(0,final_range) 
c=0   #chances taken to win

print("_____________\n Let's Try Your Luck")
print("You have",l*'*','chances')
print('Guess a number between 0-',final_range)
while(True):
  l=l-1
  c=c+1
  num=int(input())
  if num<n:
    print(num)
    print("Guess Greater than it   ",l,'chances left\n')
    #print('Guess again')
  elif num>n:
     print(num)
     print("Guess lesser than it   ",l,'chances left\n')
     #print('Guess again')
  elif num==n:
      print(num)
      print("You Won \n")
      print("You took",c,'chances to win\n')
      break
  if l<1:
     print('better luck next time \n Try Again\n')
     print('---Game over----')
     break
  if l>1:
     print('Guess again')
print('Thank You for playing this ')