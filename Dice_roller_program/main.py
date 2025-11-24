import random

'''print("\u25CF") #●
print("\u250C") #┌
print("\u2500") #─
print("\u2510") #┐
print("\u2502") #│
print("\u2514") #└
print("\u2518") #┘'''

"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"

dice_art ={
    1 : ("┌─────────┐", 
         "│         │", 
         "│    ●    │", 
         "│         │", 
         "└─────────┘"),

    2 : ("┌─────────┐", 
         "│ ●       │", 
         "│         │", 
         "│       ● │", 
         "└─────────┘"),

    3 : ("┌─────────┐", 
         "│ ●       │", 
         "│    ●    │", 
         "│       ● │", 
         "└─────────┘"), 
    
    4 : ("┌─────────┐", 
         "│ ●     ● │", 
         "│         │", 
         "│ ●     ● │", 
         "└─────────┘"),   

    5 : ("┌─────────┐", 
         "│  ●   ●  │", 
         "│    ●    │", 
         "│  ●   ●  │", 
         "└─────────┘"),

    6 : ("┌─────────┐", 
         "│  ●   ●  │", 
         "│  ●   ●  │", 
         "│  ●   ●  │", 
         "└─────────┘"),     
}

dice = []
total = 0
num_dice = int(input("How many dice?: "))

for die in range(num_dice):
   dice.append(random.randint(1, 6))

for line in range(5):
   for die in dice:
      print(dice_art.get(die)[line], end= "")
   print()

for die in dice:
   total += die
print(f"Total: {total}")