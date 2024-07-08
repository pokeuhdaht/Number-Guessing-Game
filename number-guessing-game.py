
import random
import time

#Function to fet game difficulty
def diff_select():

      i="k"
      while i != "e" and i !="E" and i != "m" and i !="M" and i != "h" and i !="H":
            print(f"Please Select a difficulty")
            print(f"e = Easy  m = Medium  h = Hard")
            i = input("Selection: ")
      else:
            if i=="e" or i=="E":
                  print("Easy Difficulty Selected")
                  return 1
            elif i=="m" or i=="M":
                  print("Medium Difficulty Selected")
                  return 2
            else:
                  print("Hard Difficulty Selected")
                  return 3
 


#Function that gets the random number and keeps track of attempts
def numbergame(diff, j, k):

      print(diff)
      print(j)
      print(k)


#Game Start
print(f"{'Number Guessing Game' : >30}")


#Gets Game Difficulty
#1= easy, 2= medium, 3= hard
diff = diff_select()


#defines the rangeselected
print("Please select two numbers to define your range.")

testj = False                 #This chunk of code allows user to select STARTING number
while testj == False:
      try:
            j= int(input("Select Starting Range: "))
      except ValueError:
            print("Please enter a solid number.")
      else:
            print("good")
            testj = True;


testk = False                 #This chunk of code allows user to select ENDING number
while testk == False:
      try:
            k= int(input("Select End Range: "))
      except ValueError:
            print("Please enter a solid number.")
      else:
            if k<=j:
                  print("not good")
            else:
                  print("good")
                  testk = True


numbergame(diff, j, k)

