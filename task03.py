try:
    with open("data.txt ", "r") as f:
     lines = len(f.readlines())
     print(f"data.txt da {lines} ta foydalanuvchi bor")

except:
    print("fayl topilmadi")