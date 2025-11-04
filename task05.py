import json

try:
    with open("data1.json", "r") as f:
        read_json = json.load(f)
    
    for user in read_json:
        print(f"Name: {user['name']}, Age: {user['age']}") 
except FileNotFoundError:
    print('Fayl topilmadi!')
except json.decoder.JSONDecodeError:
    print('Fayl ichi bosh!')