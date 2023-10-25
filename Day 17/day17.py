class User:

    # class Constructor
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.username = user_name
        self.followers = 0
        self.following = 0

    # class methods
    def followings(self, user_name):
        user_name.following += 1
        self.followers += 1


# create 2 object of class
user_1 = User("01", "Unknown")
user_2 = User("02", "Secound")

# call class method using objects
user_1.followings(user_2)

# print class attributes
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)