myTasks = []

def showMenu():
    print("My To Do List")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as completed")
    print("4. Exit")

def addTask():
    task = input("Enter the task.")
    myTasks.append(task)
    print("Your task has been added succefully.")

def viewTasks():
  print("My Tasks")
  if len(myTasks) == 0:
    print("No tasks found.")
  else:
    for i, task in enumerate(myTasks, 1):
       print(f"{i}. {task}")

def markCompleted():
  viewTasks()
  if len(myTasks) == 0:
    return

  taskNumber = int(input("Enter task number to mark completed")) - 1
  if 0 <= taskNumber <= len(myTasks):
    myTasks.pop(taskNumber)
    print("Task marked as completed.")
  else:
    print("Invalid task number.")

def main():
  while True:
    showMenu()
    choice = input("Enter your choice (1-4)")
    if choice == "1":
      addTask()
    elif choice == "2":
      viewTasks()
    elif choice == "3":
      markCompleted()
    elif choice == "4":
      print("Thank you for using My To Do List App.")
      break
    else:
      print("Invalid choice.")
  
if __name__ == "__main__":
  main()
        