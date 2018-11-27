"""More classes to represent users."""

from users import User

class Priveledges():
    """Display user priveledges."""
    
    def __init__(self, priveledges=['can add post', 'can approve new member', 'can delete post']):
        self.priveledges = priveledges
        
    def show_priveledges(self):
        """List priveledges specific to admin users."""
        print("\nAdmin users have the following special priveledges:")
        for priveledge in self.priveledges:
            print('-' + priveledge)

class Admin(User):
    """Represent a special kind of user, an admin."""
    
    def __init__(self, first_name, last_name, age, sex, race, username):
        """
        Initialize attributes of parent class.
        Then initialize attributes specific to admin.
        """
        super().__init__(first_name, last_name, age, sex, race, username)
        self.priveledges = Priveledges()