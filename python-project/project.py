import tkinter
#import all names defined  in the module
from tkinter import *
from datetime import datetime
#creates the main window
root=Tk()
root.title("To Do List")
#width x height + x_offset + y_offset. 
root.geometry("420x680+400+100")
root.resizable(False,False)
#empty list to store the tasks 
task_list=[]
def addtask():
 #this will retrieve the text entered by user in input entry widget and store in task
 task = task_entry.get()
 #deletes characters from 0 index to end
 task_entry.delete(0, END)
 #if user enter some  text
 if task:
        now = datetime.now()
        #specified format
        current_time = now.strftime("%H:%M:%S")
        current_date = now.strftime("%Y-%m-%d")
        # f here is formatted string   literal by wrapping them in curly brackets
        task_with_datetime = f"{task} ,      ({current_date} {current_time}), Completed: No"
 #f the file does not exist, it will be created. If the file does exist, new data will be appended to the end of it
        # with is used so that it properly closed after code inside executed       
        with open("tasklist.txt", 'a') as taskfile:
# adds the new task with its associated date and time to the end of the file.       
            taskfile.write(f"{task_with_datetime}\n")
       # stores all the tasks along with their associated date and time.
        task_list.append(task_with_datetime)
#This string is used for displaying the task in the GUI.
        formatted_task = f"{task} ({current_date} {current_time}), Completed: No"
    # thetask should be inserted at the end of the list displayed in the GUI.
        listbox.insert(END, formatted_task)

def deletetask():
    global task_list
    #retrieves the index of the currently selected item
    delete_task = listbox.curselection()
    if delete_task:
        #reverse =true means from start to end deletion
        for index in sorted(delete_task, reverse=True):
            task = listbox.get(index)
            #task you want to remove
            if task in task_list:
                task_list.remove(task)
            listbox.delete(index)
        with open("tasklist.txt", 'w') as taskfile:
# This ensures that the contents of the file are updated to reflect the changes 
            taskfile.write("\n".join(task_list))
            
def toggle_completion(event):
    #only one item canbe selected
    selected_index = listbox.curselection()[0]
    #splits into components
    task_info = task_list[selected_index].split(", ")
    #extracts completion status from task info
    completion_status = task_info[2].split(": ")[1]
    # toggles the completion status.
    new_completion_status = "Yes" if completion_status == "No" else "No"
    # new completion status.
    updated_task_item = f"{task_info[0]}, {task_info[1]}, Completed: {new_completion_status}"
    # updates the task item
    task_list[selected_index] = updated_task_item
    #update after deleting and inserting
    update_task_display()
#update the changes
def update_task_display():
    listbox.delete(0, END)
    
    for task_item in task_list:
        listbox.insert(END, task_item)

def opentaskfile():
    
    try:
        global task_list
#ensures that the file is properly closed after reading, even if an error occurs.
        with open ("tasklist.txt","r") as taskfile:
#This line reads all lines from the file 
                 tasks=taskfile.readlines()
#ensures text are added
        for task in tasks:
            if task  != "\n":
                #For each non-empty task, this code appends the task
                task_list.append(task)
            listbox.insert(END,task)
            #If an error occurs in the try block, execution will jump to this except block
    except:
        file=open('tasklist.txt','w')
        file.close()
#icon
Image_logo=PhotoImage(file="images/logo.png") 
#not temporary image
root.iconphoto(False,Image_logo)

#top bar
Topimage= PhotoImage(file="images/topbar.png")
Label(root,image=Topimage).pack()
dotsimage=PhotoImage(file="images/menu.png")
Label(root,image=dotsimage,bg="#32405b").place(x=30,y=25)

noteimage=PhotoImage(file="images/logo.png")
Label(root,image=noteimage,bg="#32405b").place(x=25,y=80)
heading=Label(root,text="Add your tasks",font=("Comic Sans MS", 20, "bold"),fg="white",bg="#32405b")
heading.place(x=130,y=20)
#main 
frame=Frame(root,width=400,height=50,bg="#fff")
frame.place(x=30,y=120)
#holds string value
task=StringVar()
 #input  bd=border
task_entry=Entry(frame,width=18,font=("Comic Sans MS", 20),bd=0)
task_entry.place(x=10,y=5)
# meaning the cursor will automatically appear in the entry 
#widget when the application starts.
task_entry.focus()
button=Button(frame,text="Add",font=("Comic Sans MS", 16, "bold"),width=6,bg="#4caf50",fg="#fff",bd=0,command=addtask) 
button.place(x=300,y=4)

#list
frame1=Frame(root,bd=3,width=500,height=280,bg="#2b2b2b")
#. Padding is the space outside the widget, between the widget and its surrounding elements.
frame1.pack(pady=(200,0))
#selectbackground   background color of the selected item 
listbox=Listbox(frame1,font=('Comic Sans MS', 16),width=40,height=16,bg="#2b2b2b",fg="#ffffff",cursor="hand2",selectbackground="#4caf50")
#pack -visible within parent widget  side=left left of parent widget
#fill the available space both horizontally and vertically within its parent widget (the frame).
#This adds horizontal padding of 2 pixels on both sides
listbox.pack(side=LEFT,fill=BOTH,padx=2)
#fill=BOTH parameter ensures that the scrollbar expands both horizontally and vertically to fill its container.
scrollbar=Scrollbar(frame1)
scrollbar.pack(side=RIGHT,fill=BOTH)
#vertical scroll   scroll.set called whenever scroll vertically
listbox.config(yscrollcommand=scrollbar.set)
#This ensures that scrolling the scrollbar will update the view of the listbox
scrollbar.config(command=listbox.yview)

opentaskfile()
#for deleting the task
# Bind double-click event to toggle completion status
listbox.bind("<Double-Button-1>", toggle_completion)
delete_task=PhotoImage(file="images/delete.png")
#creates delete button
Button(root,image=delete_task,bd=0,command=deletetask,bg="#f44336").place(x=180, y=610)
# The application continues running and responding to user input until the main window is closed.
root.mainloop()
