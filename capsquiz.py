import warnings
import pandas as pd
import random as rd
warnings.simplefilter(action='ignore', category=FutureWarning)

df = pd.read_csv('countrycapital2.csv')
# https://geographyfieldwork.com/WorldCapitalCities.htm

def typemode(lives = 3):
  score = 0
  geoquiz = df
  i = 0
  print("This is capital game. You have 3 lives! Type the capital of the given country.")
  while lives > 0:
    randactual = rd.choice(geoquiz.index)
    actual = geoquiz.loc[randactual]
    guess = input(f"What is the capital of {actual[0]}: ")
    if guess.lower() == actual[1].lower():
      print("Good Job!")
      score+=1
    else:
      print("Incorrect")
      lives -=1
      print(f"The correct answer is {actual[1]}")
    geoquiz = geoquiz.drop(randactual)
    i += 1
    print(f" Score = {score}\n Lives = {lives}")

  if lives == 0 and i-3 < 10:
    print(f"You ran out of lives. You named {i-3} capitals. Keep studying!")
  else:
    print(f"Great Job! You named {i-3} capitals, that's more than 95% of the population!")

def multichoice(lives = 3):
  score = 0
  geoquiz = df
  i = 0
  print("This is capital game. You have 3 lives! Type the number that corresponds to the capital of the given country.")
  while lives > 0:
    randactual = rd.choice(geoquiz.index)
    actual = geoquiz.loc[randactual]
    choice = rd.randint(0, 3)
    quadcaps = f""
    for j in range(4):
      randcountrygen = rd.choice(geoquiz.index)
      randcountry = geoquiz.loc[randcountrygen]
      if choice == j:
        quadcaps += f"{j+1}: {actual[1]}  "
      else:
        quadcaps += f"{j+1}: {randcountry[1]}  "
    print(quadcaps)
    guess = eval(input(f"Which is the capital of {actual[0]}? "))
    if guess == choice+1:
      print("Good Job!")
      score+=1
    else:
      print("Incorrect")
      lives -=1
      print(f"The correct answer is {actual[1]}")
    geoquiz = geoquiz.drop(randcountrygen)
    i += 1
    print(f" Score = {score}\n Lives = {lives}")

  if lives == 0 and i-3 < 10:
    print(f"You ran out of lives. You named {i-3} capitals. Keep studying!")
  else:
    print(f"Great Job! You named {i-3} capitals. ;)")

def main():
  print("Welcome to Max's capital quiz!")
  user = input("Would you like to play on easy or hard mode?: ")
  if user.upper() == "easy".upper() or user.upper() == "easy mode".upper():
    multichoice()
  elif user.upper() == "hard".upper() or user.upper() == "hard mode".upper():
    typemode()
main()