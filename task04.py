import json

name = input("Ismingiz: ")
age = input("Yoshingiz: ")

try:
    
    with open("data.json", "r") as f:
        users = json.load(f)
except:
    print("Fayl hali  bo'sh")
      
    users = []


users=({
    "name": name,
    "age": age
})


with open("data.json", "w") as f:
    json.dump(users, f, indent=4)