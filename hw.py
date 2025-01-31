import random
import string

def generate_password(length=12):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits


    password = random.choice(lower) + random.choice(upper) + random.choice(digits)

    
    all_chars = lower + upper + digits
    password += ''.join(random.choices(all_chars, k=length-3))

    
    password = ''.join(random.sample(password, len(password)))

    return password

print(generate_password(12))
