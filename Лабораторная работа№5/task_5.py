import random
import string


def get_random_password(n=8) -> str:
    S = string.ascii_lowercase + string.ascii_uppercase + string.digits
    password = random.sample(S,n)
    return password
    
print(get_random_password())







