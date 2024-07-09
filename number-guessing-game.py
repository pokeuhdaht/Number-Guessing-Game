
import random
import time

easyWin=0
mediumWin=0
hardWin=0

#Game Start
print(f"{'Number Guessing Game' : >30}")

play_again= "y"

while play_again=="y" or play_again=="Y":
      #Function to fet game difficulty
      def diff_select():

            i="k"
            while i != "e" and i !="E" and i != "m" and i !="M" and i != "h" and i !="H":
                  print("\nPlease Select a difficulty")
                  print("e = Easy  m = Medium  h = Hard")
                  i = input("Selection: ")
            else:
                  if i=="e" or i=="E":
                        print("\nEasy Difficulty Selected")
                        return 1
                  elif i=="m" or i=="M":
                        print("\nMedium Difficulty Selected")
                        return 2
                  else:
                        print("\nHard Difficulty Selected")
                        return 3
       


      #Function that gets the random number and keeps track of attempts
      def numbergame(diff, j, k):

            rand = int(random.randrange(j,k+1))
            print("\nA Number Has Been Chosen.")

            #Difficulty = number of given attempts
            if diff==1:
                  b=25
            elif diff==2:
                  b=10
            else:
                  b=3
            
            a=1                           #attempt number
            win=False                     #win condition
            guess = True                  #intiate while loop/end while loop
            while guess==True:
                  print("This is attempt number: "+ str(a))

                  #gets answer input from player
                  ans= None
                  while ans == None or ans<j or ans>k:
                        ans=int(input("What is your Guess? "))
                        if ans<j or ans>k:
                              print("Please enter a number within the designated range.")
                              
                  #determines whether player wins or not
                  if ans==rand:
                        print("\nThat is the correct number!")
                        win=True
                        guess=False
                  else:
                        print("\nThat is not the correct number.")
                        if a==b:
                              win=False
                              guess=False
                        else:
                              a+=1

            if win==True:
                  print("You got the number right in: "+ str(a)+ " attempts")
                  return 1
            else:
                  print("You could not get the number right in: "+ str(a)+ " attempts")
                  return 0


      #Gets Game Difficulty
      #1= easy, 2= medium, 3= hard
      diff = diff_select()


      #defines the range selected
      print("Please select two numbers to define your range.")

      testj = False                 #This chunk of code allows user to select STARTING number
      while testj == False:
            try:
                  j= int(input("Select Starting Range: "))
            except ValueError:
                  print("Please enter a solid number.")
            else:
                  testj = True;


      testk = False                 #This chunk of code allows user to select ENDING number
      while testk == False:
            try:
                  k= int(input("Select End Range: "))
            except ValueError:
                  print("Please enter a solid number.")
            else:
                  if k<=j:
                        print("Please enter a higher number.")
                  else:
                        testk = True


      #adds score to number of times won
      game=numbergame(diff, j, k)
      
      if diff==1:
            easyWin+=game
      elif diff==2:
            mediumWin+=game
      elif diff==3:
            hardWin+=game


      print("\nYou currently have "+str(easyWin)+" win(s) on Easy, "+str(mediumWin)+" win(s) on Medium, "+str(hardWin)+" win(s) on Hard.\n")
            


      #Play Again Loop
      playTrue=False

      while playTrue==False:
            play_again=input("Would you like to play again? (y/n) ")
            if play_again != "n" and play_again != "N" and play_again != "y" and play_again != "Y":
                  print("Please select (y/n)")
            else:
                  playTrue=True

else:
      print("Thank you for playing!")

   
exit()
