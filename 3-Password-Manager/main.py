from cryptography.fernet import Fernet
import os


# Get the current directory where the script is running
current_dir = os.path.dirname(os.path.abspath(__file__))
password_file = os.path.join(current_dir, "passwords.txt")
raw_key_file = os.path.join(current_dir, "key.key")

'''
def write_key():
    key = Fernet.generate_key()
    with open(real_key_file, "wb") as key_file:
        key_file.write(key)
write_key()
'''

def load_key():
    file = open(raw_key_file, 'rb')
    key = file.read()
    file.close()
    return key


master_pwd = input("Enter the Master Password: ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)

def view():
    with open(password_file, 'r') as f:
        for line in f.readlines():
            data = line.strip()
            user,passw = data.split("|")
            print("User: " + user + ", Pass: ",fer.decrypt(passw.encode()).decode())

def add():
    name = input("Name: ")
    pwd = input("Password: ")

    with open(password_file, "a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")




while True:
    mode = input("Would you like to add a password or View a password or quit ?")
    if mode.lower() == "q":
        quit()
    elif mode.lower().strip() == "v":
        view()
    elif mode.lower().strip() == "a":
        add()
