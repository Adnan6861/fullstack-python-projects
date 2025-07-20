from reg import User
from task import TaskManger
def main():
    print(f"Welcome to Task Manger:")
    while True:
     print("1- Registration")
     print("2- Login")

    
     opation=int(input("Enter Number Choose Opation: "))
     if opation == 1:
         username=input("Enter Your Name:").lower()
         email=input("Enter your Email:")
         password=int(input("Enter the Password:"))
         u1=User(username,email,password)
         print(f"Sucessfull Registration:{u1.save_data()}")
        
        
    
     elif opation == 2:
        name=input("Enter you Name TO Login:")
        password1=int("Enter the Password:")
        u1.login(name,password1)
        if User:
           print(f"Welcome Back {username}")
           print("3- add Task")
           print("4- View Task")
           print("5- delete Task")
           t1=TaskManger(username)
           while True:
              
              opation1=int(input("Enter the choice"))
              if opation1 == 3:
                task1=input("Enter the Task To add:")
                print(f"SucessFully Add Task:{t1.add_task(task1)}")
              elif opation1 == 4:
                print(f"See Below:{t1.view_task()}")
              elif opation == 5 :
               print(f"Delete All Task :{t1.delete_task()}")
              else:
                 print("invalid")
     else:
        print("invalid Choice")
if __name__ =="__main__":
 main()
