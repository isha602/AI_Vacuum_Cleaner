# -*- coding: utf-8 -*-
"""Vacuum_Cleaner.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dp6G-cA9JPQXfLJdOxjY_7V-GomUE1es
"""

# 0 --> CLEAN 
# 1--> NOT CLEAN
#THERE ARE TWO ROOMS A AND B 

#defining a function and introducing a goal state. 

def vacuum_cleaner():
  goal = {"A":"0","B":"0"}
  cost = 0

  location = input("enter the location of the vacuum  ")
  status = input(("enter the status of  " + location))
  status_complement = input("enter the status of the other room  ")
  print("Initial Location Condition " + str(goal))

  if location=="A":
    print("the vaccum is in room A")
    if status == "1":
      print("location A is dirty")
      goal["A"] = "0"
      cost = cost + 1 
      print("Room A has been cleaned and the cost for cleaning A room is " + str(cost))

        
      if status_complement == "1":
        print("location B is dirty")
        print("moving right to location B")
        goal["B"] = "0"
        cost = cost + 1 
        print("Room B has been cleaned and the cost for cleaning B room is " + str(cost))

      else: 
        print("NO ACTION NEEDED AS ROOM B IS ALREADY CLEANED. THE COST IS " + str(cost))

      
        if status == "0":
          print("location A is already Clean")
        
          if status_complement == "1":
            print("location B is dirty")
            print("moving right to location B")
            goal["B"] = "0"
            cost = cost + 1 
            print("Room B has been cleaned and the cost for cleaning B room is " + str(cost))

          else: 
            print("NO ACTION NEEDED AS ROOM B IS ALREADY CLEANED. THE COST IS " + str(cost))

  else: 
    print("Vacuum is in Room B")
    if status == "1":
      print("location B is dirty")
      goal["B"] = "0"
      cost = cost + 1 
      print("Room B has been cleaned and the cost for cleaning B room is " + str(cost))

        
      if status_complement == "1":
        print("location A is dirty")
        print("moving left to location A")
        goal["A"] = "0"
        cost = cost + 1 
        print("Room A has been cleaned and the cost for cleaning A room is " + str(cost))

      else: 
        print("NO ACTION NEEDED AS ROOM B IS ALREADY CLEANED. THE COST IS " + str(cost))

      
      if status == "0":
        print("location B is already Clean")
        
        if status_complement == "1":
          print("location A is dirty")
          print("moving left to location A")
          goal["A"] = "0"
          cost = cost + 1 
          print("Room A has been cleaned and the cost for cleaning A room is " + str(cost))

        else: 
          print("NO ACTION NEEDED AS ROOM B IS ALREADY CLEANED. THE COST IS " + str(cost))

  print()
  print("goal state is " + str(goal))
  print("perfomance measurement is  " + str(cost))
        
vacuum_cleaner()