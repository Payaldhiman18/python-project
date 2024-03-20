import tkinter
from tkinter import *
from datetime import datetime

root=Tk()
root.title("To Do List")
root.geometry("420x680+400+100")
root.resizable(False,False)
task_list=[]
def addtask():
 task = task_entry.get()
 task_entry.delete(0, END)
 if task:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        current_date = now.strftime("%Y-%m-%d")
        task_with_datetime = f"{task} ,      {current_date} {current_time}, Completed: No"
        
        with open("tasklist.txt", 'a') as taskfile:
            taskfile.write(f"{task_with_datetime}\n")
        
        task_list.append(task_with_datetime)
        formatted_task = f"{task} ({current_date} {current_time}), Completed: No"
        listbox.insert(END, formatted_task)

def deletetask():
    global task_list
    delete_task = listbox.curselection()
    if delete_task:
        for index in sorted(delete_task, reverse=True):
            task = listbox.get(index)
            if task in task_list:
                task_list.remove(task)
            listbox.delete(index)
        with open("tasklist.txt", 'w') as taskfile:
            taskfile.write("\n".join(task_list))
            
def toggle_completion(event):
    selected_index = listbox.curselection()[0]
    task_info = task_list[selected_index].split(", ")
    completion_status = task_info[2].split(": ")[1]
    new_completion_status = "Yes" if completion_status == "No" else "No"
    updated_task_item = f"{task_info[0]}, {task_info[1]}, Completed: {new_completion_status}"
    task_list[selected_index] = updated_task_item
    update_task_display()

def update_task_display():
    listbox.delete(0, END)
    for task_item in task_list:
        listbox.insert(END, task_item)

def opentaskfile():
    
    try:
        global task_list
        with open ("tasklist.txt","r") as taskfile:
                 tasks=taskfile.readlines()
        for task in tasks:
            if task  != "\n":
                task_list.append(task)
            listbox.insert(END,task)
    except:
        file=open('tasklist.txt','w')
        file.close()
#icon
Image_logo=PhotoImage(file="images/logo.png")
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
task=StringVar()
task_entry=Entry(frame,width=18,font=("Comic Sans MS", 20),bd=0)
task_entry.place(x=10,y=5)
task_entry.focus()
button=Button(frame,text="Add",font=("Comic Sans MS", 16, "bold"),width=6,bg="#4caf50",fg="#fff",bd=0,command=addtask) 
button.place(x=300,y=4)

#list
frame1=Frame(root,bd=3,width=500,height=280,bg="#2b2b2b")
frame1.pack(pady=(200,0))
listbox=Listbox(frame1,font=('Comic Sans MS', 16),width=40,height=16,bg="#2b2b2b",fg="#ffffff",cursor="hand2",selectbackground="#4caf50")
listbox.pack(side=LEFT,fill=BOTH,padx=2)
scrollbar=Scrollbar(frame1)
scrollbar.pack(side=RIGHT,fill=BOTH)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

opentaskfile()
#for deleting the task
# Bind double-click event to toggle completion
listbox.bind("<Double-Button-1>", toggle_completion)
delete_task=PhotoImage(file="images/delete.png")
Button(root,image=delete_task,bd=0,command=deletetask,bg="#f44336").place(x=180, y=610)
root.mainloop()
