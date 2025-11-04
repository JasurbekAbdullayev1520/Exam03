class AgeError(Exception):
    pass

age = int(input("Yoshingizni kiriting: "))

if age <= 0:
    raise AgeError("Yosh noto‘g‘ri!")

print(f"Siz {age} yoshdasiz.")