try:
    with open("data.txt ", "r") as f:
     lines = f.readlines()


    for line in lines:
        print(line.strip())

except:
    print("fayl topilmadi")

