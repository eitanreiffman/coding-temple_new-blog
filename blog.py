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
        return self.password == password_guess[::2]

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
            print("1. Sign Up\n5. Quit")
            # Ask the user which option they would like to do
            to_do = input("Which option would you like to do? ")
            # Keep asking if user chooses an invalid option
            while to_do not in {'1', '5'}:
                to_do = input("Invalid option. Please choose 1 or 5: ")
            if to_do == '5':
                print("Thanks for checking out the blog.")
                break
            elif to_do == '1':
                # method to create a new user
                my_blog.create_new_user()

# Execute the function to run the blog
run_blog()