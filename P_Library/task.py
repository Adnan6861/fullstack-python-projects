class TaskManger:
    def __init__(self,user):
        self.user=user
        self.task_file=f"{self.user}_task.txt"
    def add_task(self,task):
        with open(self.task_file,'a') as f:
            f.write(task + "\n")
    def view_task(self):
        try:
          with open(self.task_file,'r') as f:
            tasks=f.readlines()
            return tasks if tasks else ["No Task Found"]
        except FileNotFoundError:
           print("Not Any File Exist")
    def delete_task(self):
       with open(self.task_file,'w').close():
        return "All Task Deleted"
        

        