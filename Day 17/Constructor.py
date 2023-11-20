class User:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.name = user_name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following +=1

def printing(user_id):
    print(f"Id: {user_id.id}  Name: {user_id.name} Followers: {user_id.followers} Followings: {user_id.following}")



user_1 = User("001", "Farhan")
user_2 = User("002", "Rehan")

user_1.follow(user_2)

printing(user_1)
printing(user_2)
