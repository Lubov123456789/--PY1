import random
import string
def get_random_password() -> str:
    S = string.ascii_lowercase + string.ascii_uppercase + string.digits
    i = random.sample(S,8)
    password = str(i)
    return password
print(get_random_password())







