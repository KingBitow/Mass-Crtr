import random
import string
from modules.getIdentity import getIdentity

def random_string(length):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def generate_account_info(email_domain, country):
    identity = getIdentity(country)
    first = identity["first_name"].lower()
    last = identity["last_name"].lower()
    
    username = f"{first}{last}{random_string(4)}{random.randint(10,99)}"
    password = random_string(10) + str(random.randint(100,999))
    email = f"{username}@{email_domain}"
    
    return {
        "username": username,
        "password": password,
        "email": email,
        "identity": identity
    }
