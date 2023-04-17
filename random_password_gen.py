import random
import string

print("""
    This is a Random Password Generator!
    Type 'go' and I will give you a perfect password!
""")


def password_gen():
    password = []
    special_xters = ["!", "@", "#", "%", "&", "$", "?", "_", "-", "="]
    pwd_length = random.randrange(8, 12)
    pwd_xter = 0
    while pwd_xter <= pwd_length:
        num = random.randrange(0, 9) #string.digits
        password.append(str(num))
        spx = random.choice(special_xters) #string.punctuation
        password.append(spx)
        upp_alpha = random.choice(string.ascii_uppercase)
        password.append(upp_alpha)
        low_alpha = random.choice(string.ascii_lowercase)
        password.append(low_alpha)
        pwd_xter += 4
    
    random.shuffle(password)
    final_password = "".join(password)
    print(final_password)


while True:
    print("Type 'go' to generate a password!")
    response = input("> ")
    if response != "go":
        print("Sorry I don't understand that")
    else:
        password_gen()
        break