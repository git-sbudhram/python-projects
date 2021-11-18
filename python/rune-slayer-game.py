name = input("What is your name\n ")

print('''
*******************************************************************************
                      ,-,-      
                     / / |      
   ,-'             _/ / /       
  (-_          _,-' `Z_/        
   "#:      ,-'_,-.    \  _     
    #'    _(_-'_()\     \ |    
  ,--_,--'                 |    
 / ""                      L-'\ 
 \,--^---v--v-._        /   \ | 
   \_________________,-'      | 
                    \           
                     \          
                      \         
*******************************************************************************
''')
print(f"Welcome to Runeslayer {name}")
print("Your mission is to find the rune sword needed to slay the dragon.") 

print("\nMy name is Grandor and I will help you on your journey")

print("\nYou are all packed and good to go on your journey!")

question1 = input("\nYou approach the first crossroad, will you go left or right?\n ")
if question1.lower() == "left":
  boar = input("\nYou decide to go left and encounter a wild boar, will you attack or run?\n ")
  if boar.lower() == "attack":
    print("\nYou attack the boar and kill it swiftly. You continue your journey\n")
  else:
    print("\nYou run and escape from the boar. You find an apple tree, you pick an apple and continue your journey.\n")
  
  print("As you get closer to the cave you hear a deep roar, it's the dragon! It's not far now\n")
  print("You're in front of the rune cave entrance now, as you place your hand on the door you hear it open\n")
  doors = input("As you enter the cave you see 2 doors; blue and yellow. Which will you enter?\n ")
  if doors.lower() == "blue":
    print("\nYou enter the blue door and find the rune sword!")
  else:
    print("\nYou enter the yellow door but there's nothing behind it so you open the blue door and find the rune sword!\n")
  print("\nYou walk through the narrow pathway and find the rune dragon!\n")
  dragon_choice = input("What will you do, attack the dragon or run?\n ")
  if dragon_choice.lower() == "attack":
    print("\nYou have a long and tiresome fight with the dragon but come out as winner!")
    print(f"\nYou loot the dragons den and head back to the village which you saved, well done {name}!")
    print("\nThe villagers welcome you back warmly and thank you with a big party that lasted for 2 days!")
    print("\nEnd of game <3")
  else:
    print("\nYou run back and fall into trap killing you instantly...\n")
    print("GAME OVER!!..")
else:
  print("\nYou go right, walk over the unsteady bridge and fall into the abyss ...\n")
  print("GAME OVER!!.....")
