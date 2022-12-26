import os
import subprocess


class Store:
    email = ''


class gitAutomate:
    def __init__(self):
        pass

    def SetupQuestion(self):
        email = input("Enter your github email ")
        email2 = input("Confirm your github email ")
        if email == email2:
            Store.email = email
            self.Key(email)
        else:
            print("Email does not match")
            self.SetupQuestion()

    # Adding your SSH key to the ssh-agent

    def Key(self, email):
        process = subprocess.Popen(["ssh-keygen", "-t", "ed25519", "-C",
                                    f"{email}"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        file_name = input("Enter the file name for the key: ")
        file_name = file_name.encode()
        output, err = process.communicate(file_name)
        output, err = process.communicate(file_name)

        subprocess.run(["eval", "$(ssh-agent -s)"])
        subprocess.run(["ssh-add", "~/.ssh/id_ed25519"])
        self.LocateKey()
        # print(output.decode())

    def LocateKey(self):
        # subprocess.run(["cat", "~/.ssh/id_ed25519.pub"])
        AvNet = os.popen("cat ~/.ssh/id_ed25519.pub").read()
        print(AvNet)


# LocateKey()
gitAutomate().SetupQuestion()
