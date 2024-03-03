from user import User


class SocialNetwork:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, stringname):
        if not hasattr(self, 'initialized'):
            self.stringname = stringname
            self.users = []
            print(f"The social network {self.stringname} was created!")
            self.initialized = True

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        self.users.remove(user)

    def connect_users(self, user1, user2):
        user1.follow(user2)

    def sign_up(self, username, password):
        # Create a new User object
        new_user = User(username, password)
        # Add the user to the list of users in the social network
        self.add_user(new_user)
        # Return the created user
        return new_user

    def log_out(self, username):
        user_to_log_out = self.find_user_by_username(username)
        if user_to_log_out:
            user_to_log_out.disconnect()
        else:
            print(f"User {username} not found.")

    def log_in(self, username, password):
        user_to_log_in = self.find_user_by_username(username)
        if user_to_log_in and user_to_log_in.password == password:
            user_to_log_in.connect()
        else:
            print(f"Login failed for user {username}.")

    def __str__(self):
        result = self.stringname + " social network:\n"
        for i, user in enumerate(self.users):
            result += f"{user}\n"
            if i == len(self.users) - 1:
                result = result.rstrip('\n')
        return result

    def find_user_by_username(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None
