def signup():
    username=input("Creat username").strip().lower()
    password=input("Creat password").strip()
    with open("user.txt", "a")as f:
        f.write(f"{username},{password}\n")
    print("SIGNUP SUCCESSFULL")
def login():
    username=input("Enter username").strip().lower()
    password=input("Enter password").strip()
    try:
        with open("user.txt", "r")as f:
            data=f.readlines()
    except FileNotFoundError:
        print("user not found ! please first signup")
        return False
    login_success=False
    for line in data:
        savad_user,savad_pass=line.strip().split(",")
        if username == savad_user and password == savad_pass:
            login_success=True
            break
    if login_success:
        print("LOGIN SUCCESSFULL")
    else:
        print("WRONG USERNAME AND PASSWORD")
def change_password():
    user=input("Enter username").strip().lower()
    old_pass=input("Enter your old password").strip()
    try:
        with open("user.txt", "r")as f:
            data=f.readlines()
    except FileNotFoundError:
        print("user not found ! please first signup")
        return False
    updated=False
    new_lines=[]
    for line in data:
        savad_user,savad_pass=line.strip().split(",")
        if savad_user == user and savad_pass == old_pass:
            new_pass=input("Enter your new password").strip()
            new_lines.append(f"{savad_pass},{new_pass}")
            updated=True
        else:
            new_lines.append(line)
    if updated:
        with open("user.txt", "w")as f:
            f.writelines(new_lines)
        print("password changed successfully")
    else:
        print("username and password incorrect")
#------MANU-------#
while True:
    print("A= login")
    print("B= signup")
    print("C= change password")
    print("D= Exit")
    choice=input("choose the options").strip().upper()
    if choice == "A":
        login()
    elif choice == "B":
        signup()
    elif choice == "C":
        change_password()
    elif choice == "D":
        print("EXITING")
        break
    else:
        print("invalid options ! try again")
    