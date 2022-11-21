import random
def get_random_password() -> str:
    S = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789bcdefghijklmnopqrstuvwxyz'
    i = random.sample(S,8)
    password = str(i)
    return password
print(get_random_password())







