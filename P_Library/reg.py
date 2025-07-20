import os 
class User:
    def __init__(self,username,email,password):
        self.username=username
        self.email=email
        self.password=password
        self.filename=f"{self.username}_task.txt"
    def save_data(self):
        with  open("reg_data.txt",'a') as f:
            f.write(f"{self.username},{self.email},{self.password}")
    @staticmethod
    def login(username,password):
        if not os.path.exists("reg_data.txt"):
            return None
        else:
            with open("reg_data.txt",'r') as f:
                for line in f:
                    u,e,p=line.strip().split(",")
                    if u == username and p==password:
                        return u,p,e
                    else:
                        return None
                    
