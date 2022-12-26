import os
import subprocess


class Store:
    email = ''


def SetupQuestion():
    email = input("Enter your github email ")
    email2 = input("Confirm your github email ")
    if email == email2:
        Store.email = email
    else:
        print("Email does not match")
        SetupQuestion()


# SetupQuestion()
# Adding your SSH key to the ssh-agent


def Key():
    os.popen(f"ssh-keygen -t ed25519 -C {Store.email}").read()


def LocateKey():
    # subprocess.run(["cat", "~/.ssh/id_ed25519.pub"])
    AvNet = os.popen("cat ~/.ssh/id_ed25519.pub").read()
    print(AvNet)


LocateKey()
