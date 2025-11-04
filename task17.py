import json

class User:
    def __init__(self, name, email, is_active):
        self.name = name
        self.email = email
        self.is_active = is_active

    def save(self):
        with open("data.json", "r") as f:
            users = json.load(f)

        users.append({
            "name": self.name,
            "email": self.email,
            "is_active": self.is_active
        })
        with open("data.json", "w") as f:
            content = json.dumps(users, indent=4)
            f.write(content)

        return users

    def deactivate(self):
        with open("data.json", "r") as f:
            users = json.load(f)

        for user in users:
            if user["email"] == self.email:
                user["is_active"] = False
                self.is_active = False

        with open("data.json", "w") as f:
            user = json.dump(users, f, indent=4)

user = User("Ali", "ali@gamil.com", True)
user.save()

user2 = User("Vali", "vali@gamail.com", False)
user2.save()

