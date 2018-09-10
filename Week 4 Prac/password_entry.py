"""Thomas"""
def main():
    password = get_password()
    print('*' *len(password))

def get_password():
    password = input("Please enter a password more than 2 characters long")
    while len(password) < 2:
        password = input("INVALID! Please enter a password above 2 characters")
    return password

main()
