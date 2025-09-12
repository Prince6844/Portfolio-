import random
item_list = ["Stone", "Paper", "Sissor"]
user_choice =  input("Enter your choice : Stone, Paper, Sissor ")
comp_choice = random.choice(item_list)

print(f"User choice = {user_choice}, Computer choice = {comp_choice} ")
if user_choice == comp_choice:
 print("Both choses the same = Match Tie")
elif user_choice == "Stone":
  if comp_choice == "Paper":
    print("Paper cover Stone = computer win")
  else:
    print("Stone Smahes Sissor = User Win")
elif user_choice == "Paper":
 if comp_choice == "Stone":
    print("Paper cover Stone = User Win")
 else:
    print("Sissor cut the paper = Computer win")
elif user_choice == "Sissor":
  if comp_choice == "Stone":
    print("Stone Smahes Sissor = Computer Win")
  else:
    print("Sisssor cut the paper = User win")
  


  
## Project 3 ...  Stone, Paper and sissors game
# Input From User (Stone, Paper and Sissor
# computer choice 
# result
# Case A - Stone
# Stone - Stone = Tie
# Stone - Sissor = Stone win
# Stone - Paper = Paper win

# Case B - Sissor
# Sissor - Sissor = Tie
# Sissor - Stone = Stone win
# Sissor - Paper = Sissor win

# Case c - Paper
# Paper - Paper = Tie
# Paper - Stone = Paper win
# Paper - Sissor = Sissor win
 



  
