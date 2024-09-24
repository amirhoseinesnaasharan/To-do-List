from tkinter import *
from tkinter import messagebox

# Global list to store tasks
tasks_list = []
counter = 1

# Function to check for input errors (empty task input)
def inputError():
    if enterTaskField.get() == "":
        messagebox.showerror("Input Error", "Task field cannot be empty")
        return 0
    return 1

# Function to clear task input field
def clear_taskField():
    enterTaskField.delete(0, END)

# Function to insert tasks into the list and TextArea
def insertTask():
    global counter
    value = inputError()
    if value == 0:
        return
    task_content = enterTaskField.get() + "\n"
    tasks_list.append(task_content)
    TextArea.insert(END, f"[ {counter} ] {task_content}")
    counter += 1
    clear_taskField()

# Function to delete a specific task by task number
def deleteTask():
    global counter
    if len(tasks_list) == 0:
        messagebox.showerror("Error", "No tasks to delete")
        return
    try:
        task_no = int(taskNumberField.get())
        if task_no > counter or task_no <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Invalid task number")
        return
    
    tasks_list.pop(task_no - 1)
    counter -= 1
    TextArea.delete(1.0, END)

    # Re-write the tasks in the text area after deletion
    for idx, task in enumerate(tasks_list):
        TextArea.insert(END, f"[ {idx + 1} ] {task}")
    clear_taskField()
    taskNumberField.delete(0, END)

# Function to mark tasks as completed
def markCompleted():
    task_no = taskNumberField.get()
    try:
        task_no = int(task_no)
        if task_no <= 0 or task_no > len(tasks_list):
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Invalid task number")
        return

    # Update task to show as completed
    tasks_list[task_no - 1] = tasks_list[task_no - 1].strip() + " [Completed]\n"
    TextArea.delete(1.0, END)
    for idx, task in enumerate(tasks_list):
        TextArea.insert(END, f"[ {idx + 1} ] {task}")
    taskNumberField.delete(0, END)

# Function to mark tasks as failed
def markFailed():
    task_no = taskNumberField.get()
    try:
        task_no = int(task_no)
        if task_no <= 0 or task_no > len(tasks_list):
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Invalid task number")
        return

    # Update task to show as failed
    tasks_list[task_no - 1] = tasks_list[task_no - 1].strip() + " [Failed]\n"
    TextArea.delete(1.0, END)
    for idx, task in enumerate(tasks_list):
        TextArea.insert(END, f"[ {idx + 1} ] {task}")
    taskNumberField.delete(0, END)

# Driver code
if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="light green")
    gui.title("To-Do List")
    gui.geometry("491x506")  # Set the window size to 491x506

    # Add the welcome label
    welcome_label = Label(gui, text="Welcome to To-Do App!", bg="light green", font=("Arial", 16), fg="white")
    welcome_label.grid(row=0, column=1, columnspan=2)

    # Task entry label and entry box
    enterTask = Label(gui, text="Enter Your Task", bg="light green")
    enterTask.grid(row=1, column=1)

    enterTaskField = Entry(gui)
    enterTaskField.grid(row=2, column=1, ipadx=50)

    # Submit button to add the task
    Submit = Button(gui, text="Submit", fg="Black", bg="Red", command=insertTask)
    Submit.grid(row=3, column=1)

    # Text area to display tasks
    TextArea = Text(gui, height=8, width=30, font="lucida 13")
    TextArea.grid(row=4, column=1, padx=10, pady=10)

    # Delete task label and input field
    taskNumber = Label(gui, text="Enter Task No. to Delete or Complete", bg="light green")
    taskNumber.grid(row=5, column=1)

    taskNumberField = Entry(gui)
    taskNumberField.grid(row=6, column=1)

    # Delete task button
    deleteButton = Button(gui, text="Delete Task", fg="Black", bg="Red", command=deleteTask)
    deleteButton.grid(row=7, column=0, pady=10)

    # Mark task as completed button
    completeButton = Button(gui, text="Mark Completed", fg="Black", bg="Blue", command=markCompleted)
    completeButton.grid(row=7, column=1, pady=10)

    # Mark task as failed button
    failButton = Button(gui, text="Mark Failed", fg="Black", bg="Orange", command=markFailed)
    failButton.grid(row=7, column=2, pady=10)

    # Exit button
    Exit = Button(gui, text="Exit", fg="Black", bg="Red", command=gui.destroy)
    Exit.grid(row=8, column=1, pady=20)

    gui.mainloop()
