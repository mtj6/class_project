from users import User
from admin import Priveledges, Admin

user1 = Admin('rebecca', 'appl', '45', 'female', 'white', 'beccaskye')
user1.describe_user()
user1.priveledges.show_priveledges()