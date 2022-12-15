class Blog:
    def __init__(self):
        self.users = set()
        self.posts = []
        self.current_user = None # attribute used to determine if there's a logged in user

    # Private method for getting a post instance from the blog based on its ID
    # Returns None if post with ID does not exist
    def _get_post_from_id(self, post_id):
        for post in self.posts:
            if post.id == int(post_id):
                return post

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

    # Method to create new post if user is logged in
    def create_post(self):
        # Check to make sure user is logged in before creating post
        if self.current_user is not None:
           # Get the title and body from user input
           title = input("Enter the title of your post: ")
           body = input("Enter the body of your post: ")
           # Create a new Post instance with the input
           new_post = Post(title, body, self.current_user)
           # Add the new post instance to our blog's list of posts
           self.posts.append(new_post)
           print(f"{new_post.title} has been created!")
        else:
            print("You must be logged in to perform this action.")

    # Method to view ALL posts
    def view_posts(self):
        if self.posts:
            # Loop through all of the posts
            for post in self.posts:
                # Display the post
                print(post)
        # If no posts:
        else:
            print("There are currently no posts for this blog")

    # Method to view single post by ID
    def view_post(self, post_id):
        post = self._get_post_from_id(post_id)
        if post:
            print(post)
        else:
            print(f"Post with ID {post_id} does not exist.")

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
    id_counter = 1

    def __init__(self, title, body, author):
        """
        title: str
        body: str
        author: User
        """
        self.title = title
        self.body = body
        self.author = author
        self.id = Post.id_counter
        Post.id_counter += 1

    def __str__(self):
        formatted_post = f"""
        {self.id}. {self.title.title()}
        By: {self.author}
        {self.body}
        """
        return formatted_post

    def __repr__(self):
        return f"<Post {self.id}|{self.title}>"


# Define a function to run the blog
def run_blog():
    # Create an instance of the Blog Class
    my_blog = Blog()

    # Add preloaded data for the Blog
    initial_user = User('eitanr','abc123')
    my_blog.users.add(initial_user)
    initial_post = (Post('Pre-Loaded', 'This post was preloaded', initial_user))
    my_blog.posts.append(initial_post)

    # Keep looping while the blog is "running"
    while True:
        # if there is no current user logged in
        if my_blog.current_user is None:
            # Print the menu options
            print("1. Sign Up\n2. Log In\n3. View All Posts\n4. View Single Post\n5. Quit")
            # Ask the user which option they would like to do
            to_do = input("Which option would you like to do? ")
            # Keep asking if user chooses an invalid option
            while to_do not in {'1', '5', '2', '3', '4'}:
                to_do = input("Invalid option. Please choose 1, 2, 3, 4, or 5: ")
            if to_do == '5':
                print("Thanks for checking out the blog.")
                break
            elif to_do == '1':
                # method to create a new user
                my_blog.create_new_user()
            elif to_do == '2':
                # method to log user in
                my_blog.log_user_in()
            elif to_do == '3':
                # method to view all posts
                my_blog.view_posts()
            elif to_do == '4':
                # Get ID of post
                post_id = input("What is the ID of the post you would like to view? ")
                # Call the view single post method with post_id as an argument
                my_blog.view_post(post_id)
        # If the current user is not "None", AKA a current is already logged in
        else:
            # Print menu options for logged in user
            print("1. Log Out\n2. Create New Post\n3. View All Posts\n4. View Single Post")
            to_do = input("Which option would you like to choose? ")
            while to_do not in {'1', '2', '3', '4'}:
                to_do = input("Invalid option. Please choose 1, 2, 3, or 4. ")
            if to_do == '1':
                my_blog.log_user_out()
            elif to_do == '2':
                my_blog.create_post()
            elif to_do == '3':
                my_blog.view_posts()
            elif to_do == '4':
                # Get ID of post
                post_id = input("What is the ID of the post you would like to view? ")
                # Call the view single post method with post_id as an argument
                my_blog.view_post(post_id)


# Execute the function to run the blog
run_blog()