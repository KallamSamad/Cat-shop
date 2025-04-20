import pandas as pd
import numpy as np
import random
import time
import os
import matplotlib.pyplot as plt
import seaborn as sns
catfile = pd.read_csv(os.path.join(os.path.dirname(__file__), 'cats_dataset.csv'))
count=0
budget=1500
basket={}

catlist= {
    "breed": [
        "russian Blue", "norwegian forest", "chartreux", "persian", "ragdoll", "ocicat", "abyssinian",
        "oriental", "egyptian mau", "american shorthair", "bengal", "cornish rex", "british shorthair",
        "burmese", "singapura", "maine coon", "turkish angora", "himalayan", "sphynx", "manx", "siberian",
        "birman", "balinese", "devon rex", "exotic shorthair", "scottish fold", "savannah", "munchkin",
        "siamese", "tonkinese"
    ],
    "price": [
        "130", "700", "200", "570", "400", "700", "200", "100", "300", "100", "300", "320",
        "300", "150", "500", "300", "150", "100", "300", "320", "300", "150", "500", "320",
        "300", "150", "500", "200", "100", "300", "100"
    ]
}






catcolours=('Tortoiseshell', 'Brown', 'Sable', 'Tabby', 'Blue', 'Calico', 'White', 'Black', 'Pointed', 'Red', 'Tricolor', 'Cream', 'Orange', 'Gray', 'Bicolor')
time.sleep(1)
print("Hello and welcome to the SHU Cat shop!")
time.sleep(1)
print("We hope you find find a purrfect match in finding a feline friend!")
time.sleep(2)
print(f"You have £{budget}")
time.sleep(1)
print("Here is a cat-alogue of the cats we have right meow")
time.sleep(3)
print("Just tell me what you're interested in :")
time.sleep(2) 
num=1
for x in range(len(catlist["breed"])):
  time.sleep(0.5)
  print( f"\n. {catlist['breed'][x]} cats arew £{catlist['price'][x]}")

print("The available colours are (not all may apply to every breed): ")
for colour in catcolours:
    print(f". {colour}")
    num=num+1
class catclass:# use for numpy stuff and stats
  def  __init__(self,Breed,Age,Weight,Color,Gender):
    self.Breed=Breed
    self.Age=Age
    self.Weight=Weight
    self.Color=Color
    self.Gender=Gender
    
def intro():
  choose=input("Now before we start, would you like more information on our cats? (y/n)").lower()
  if choose=="yes" or choose=="y" or choose=="yup":
    print("to add")
  elif choose=="no" or choose=="n" or choose=="nah":
    return userinput()
  else:
    print("I'm sorry, I didn't get that.....")
    time.sleep(1)
    return intro()

    
def userinput():
    while True:
        Breed = input("Enter Breed: ").lower()
        
      
        if Breed not in [breed.lower() for breed in catlist['breed']]:
            print("Error: Please enter a valid breed from the catalogue.")
        else:
            break  

    while True:
            Color = input("Enter fur colour: ").lower()
            if Color not in [color.lower() for color in catcolours]:   
                print("Error: Please enter a valid colour from the catalogue.")
            else:
                break   
    while True:
        Gender = input("Male or Female? ").lower()
        if Gender == "male" or Gender =="female":
            break
        else:
            print("Invalid input! Please enter 'male' or 'female'.")

    while True:
        try:
            Age = int(input("Enter Cat Age: "))
            if Age < 0:
                print("Age must be a positive number. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input! Age must be a number. Please try again.")


    while True:
        try:
            Weight = int(input("Enter Weight(kg): "))
            if Weight <= 0:
                print("Weight must be a positive number. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input! Weight must be a number. Please try again.")

    time.sleep(1)
    print(f"\nYou want a cat that is a {Breed} and is {Age} years old. It weighs {Weight} kilograms, has {Color} fur, and is a {Gender}. ")
    time.sleep(3)
    print("\nPlease wait. I am Pawcessing this information.")
    time.sleep(5)
    return Breed, Age, Weight, Color, Gender

def retry():
    again = input("Would you like to search again? (y/n): ").lower()
    if again =="y" or again=="yes":
        catsearch()
    else:
        print("Thank you for visiting the SHU Cat Shop!")


def reciept(basket, budget):
    with open("receipt.txt", "w") as file:
        file.write("Receipt for SHU Cat Shop:\n")
        for item in basket.values():
            file.write(f"{item['breed']} - £{item['price']}\n")
        file.write(f"Remaining Budget: £{budget}")
        if os.path.exists("receipt.txt"):
            print("Receipt successfully created! You can find it as 'receipt.txt'.")
            
        else:
            print("Error: Receipt file was not created.")

def checkout():
  global budget
  check=input("Have you done shopping?").lower()
  print(f"Your budget is £{budget}")
  if check=="y" or check=="yes":
    for m in basket:
      breed=basket[m]['breed']
      price=int(basket[m]['price'])
      print(f"You have bought a {breed} in your basket which costs £{price}")
      budget=(budget-price)
      end=input("Would you like a recieet?").lower()
      if end=="y" or end=="yes":
        reciept(basket, budget)
      else:
        print("Thank you for visiting the SHU catshop")
    print(f"Your new budget is £{budget}")     
  else:
    retry()
   

  
  
def shop():
    buy = input("Would you like to purchase a cat?").lower()
    if buy == "yes" or buy == "y":
        while True:
            try:
                ID = int(input("Give the ID of the cat"))
                if ID in catfile.index:
                    print("Cat found!")
                    purchase = catfile.loc[ID]
                    catlink = purchase["breed"]
                    breedex = catlist["breed"].index(catlink)
                    price = catlist["price"][breedex]
                    print(f"{catlist['breed'][breedex]} cats cost £{price}")
                    basket[catlink] = {"breed": catlink, "price": price} 
                    print("Added to the basket")
                    checkout()
                    break  
                else:
                    print("No cat found with that ID")
            except ValueError:
                print("Enter a numeric ID")
                shop()
    else:
      print("Thank you for your enquirey!")
      retry()



def catsearch():
    
    catfile.columns = catfile.columns.str.lower().str.strip()
    userdata = intro()
    if userdata:
        Breed, Age, Weight, Color, Gender = userdata
        x = catclass(Breed, Age, Weight, Color, Gender)
        catfile['breed'] = catfile['breed'].str.lower()
        catfile['color'] = catfile['color'].str.lower()
        catfile['gender'] = catfile['gender'].str.lower()
        breedfilter = catfile[catfile['breed'].apply(lambda x: x == Breed)]
        if not breedfilter.empty:
            print("\nPossible cats after filtering by breed:")
            print(breedfilter)
        else:
            print("\nNo cats found with the specified breed.")
            shop()
            retry()
            return

        colorfilter = breedfilter[breedfilter['color'].apply(lambda x: x == Color)]
        if not colorfilter.empty:
            print("\nPossible cats after filtering by color:")
            print(colorfilter)
        else:
            print("\nNo cats found with the specified color.")
            shop()
            retry()
            return

        genderfilter = colorfilter[colorfilter['gender'].apply(lambda x: x == Gender)]
        if not genderfilter.empty:
            print("\nPossible cats after filtering by gender:")
            print(genderfilter)
            
        else:
            print("\nNo cats found with the specified gender.")
            shop()
            retry()
            return

        agefilter = genderfilter[genderfilter['age (years)'].apply(lambda x: x == Age)]
        if not agefilter.empty:
            print("\nPossible cats after filtering by age:")
            print(agefilter)
        else:
            print("\nNo cats found with the specified age.")
            shop()
            retry()
            return

        weightfilter = agefilter[agefilter['weight (kg)'].apply(lambda x: x == Weight)]
        if not weightfilter.empty:
            print("\nPossible cats after filtering by weight:")
            print(weightfilter)
        else:
            print("\nNo cats found with the specified weight.")
            shop()
        shop()
  

catsearch()
