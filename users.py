"""A class related to users."""

class User():
    """Describe some users."""
    def __init__(self, first_name, last_name, age, sex, race, username):
        """initialize user attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.race = race
        self.username = username
        self.login_attempts = 0
        
    def describe_user(self):
        """describe the user"""
        print('\nName: ' + self.first_name.title() + ' ' + self.last_name.title())
        print('Age: ' + str(self.age))
        print('Sex: ' + self.sex)
        print('Race: ' + self.race)
        print('Username: ' + self.username)
        print("Number of login attempts: " + str(self.login_attempts))
        
    def increment_login_attempts(self):
        """increase number of login attempts"""
        self.login_attempts += 1
        
    def greet_user(self):
        """greet the user"""
        print('Hello ' + self.first_name.title() + ' ' + self.last_name.title() + '!')
        
    def reset_login_attempts(self):
        """reset the number of login attempts"""
        self.login_attempts = 0
              
