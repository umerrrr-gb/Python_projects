tasks = []

def addTask():
  task = input("Enter a new task:")
  tasks.append(task)
  print(f"Task '{task}' has been added")

def listTask():
  if not tasks:
    print("There are currently no tasks")
  else:
    print("Current tasks")
    for index, task in enumerate(tasks):
      print(f"Task # {index}. {tasks}")

def deleteTask():
  listTask()
  try:
    tasktodelete = int(input("Enter the # to delete"))
    if tasktodelete >=0 and tasktodelete < len(tasks):
      tasks.pop(tasktodelete)
      print(f"{tasktodelete} has been removed")
    else:
      print(f"Task # {tasktodelete} was not found")
  except:
    print("Invalid input")


if __name__ == "__main__":
#Create a loop to run the app:
 print("Welcome to the to-do list app")
while True:
  print("Select one of the choices below!")
  print("--------------------------------")
  print("1. Add a new task")
  print("2. delete a task")
  print("3. List all the task")
  print("4. -Quit")

  choice = input("Enter your choice: ")

  if choice == "1":
    addTask()
  elif choice == "2":
    deleteTask()
  elif choice == "3":
    listTask()
  elif choice == "4":
    break
  else:
    print("Invalid option, Please try again!")

print("Goodbye")
    
  

