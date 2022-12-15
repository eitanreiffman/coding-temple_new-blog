class Blog:
    def __init__(self):
        self.users = set()
        self.posts = []
        self.current_user = None # attribute used to determine if there's a logged in user

    # Method to add new user to the blog
    def create_new_user(self):
        # Get user info from input
        username = input("Please enter a username: ")
        # Check if there is a user that already has that username
        if username in {u.username for u in self.users}:
            print(f"User with username {username} already exists.")
        else:
            # Get password
            password = input("Please enter a password: ")
            # Create a new user instance with info from inputs
            new_user = User(username, password)
            # Add new user instance to the blog user set
            self.users.add(new_user)
            print(f"{new_user} has been created!")

    # Method to log user in
    def log_user_in(self):
        # Get user credentials
        username = input("What is your username? ")
        password = input("What is your password? ")
        # Loop through each user in the blog
        for user in self.users:
            # Check if a user has the same username and then check the password
            if user.username == username and user.check_password(password):
                # If user has correct credentials, set the blog's current user to that user instance
                self.current_user = user
                print(f"{user} has been logged in.")
                break
        # If no users in our blog user set have that username/password, alert invalid credentials
        else:
            print("Username and/or password is incorrect.")

    # Method to log user out
    def log_user_out(self):
        # Change current user attribute on this instance to None
        self.current_user = None
        print("You have succesfully logged out.")

class User:
    id_counter = 1 # Class attribute keeping track of user IDs

    def __init__(self, username, password):
        self.username = username
        self.password = password[::-2]
        self.id = User.id_counter
        User.id_counter += 1

    def __str__(self):
        return self.username

    def __repr__(self):
        return f"<User {self.id}|{self.username}>"

    def check_password(self, password_guess):
        return self.password == password_guess[::-2]

class Post:
    pass

# Define a function to run the blog
def run_blog():
    # Create an instance of the Blog Class
    my_blog = Blog()
    # Keep looping while the blog is "running"
    while True:
        # if there is no current user logged in
        if my_blog.current_user is None:
            # Print the menu options
            print("1. Sign Up\n2. Log In\n5. Quit")
            # Ask the user which option they would like to do
            to_do = input("Which option would you like to do? ")
            # Keep asking if user chooses an invalid option
            while to_do not in {'1', '5', '2'}:
                to_do = input("Invalid option. Please choose 1, 2, or 5: ")
            if to_do == '5':
                print("Thanks for checking out the blog.")
                break
            elif to_do == '1':
                # method to create a new user
                my_blog.create_new_user()
            elif to_do == '2':
                # method to log user in
                my_blog.log_user_in()
        # If the current user is not "None", AKA a current is already logged in
        else:
            # Print menu options for logged in user
            print("1. Log Out")
            to_do = input("Which option would you like to choose? ")
            while to_do not in {'1'}:
                to_do = input("Invalid option. Please choose 1. ")
            if to_do == "1":
                my_blog.log_user_out()

# Execute the function to run the blog
run_blog()