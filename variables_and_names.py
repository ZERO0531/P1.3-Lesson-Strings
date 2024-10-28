# variables_and_names.py

enemey = 100
player = 50 

#show the data
print(f"Enemey health: {enemey}")
print(f"Player health: {player}")
print(" ")

#player chooses an action 
action = input("---Attack or Heal?---")
print(" ")

#attack the enemey
if action == "attack": 
    print("Attacking: -10")
    enemey -= 10
    print(f"Enemey health: {enemey}")

#heal yourself
elif action == "heal": 
    print("Healing: +10")
    player += 10
    print(f"Player health: {player}")

#other option
else: 
    print("Don't have this option")
