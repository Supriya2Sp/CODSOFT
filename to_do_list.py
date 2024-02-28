import tkinter
import tkinter.messagebox
import pickle

window = tkinter.Tk()
window.title("To Do List")

def task_adding():
    todo = task_add.get()
    if todo!="":
        todo_box.insert(tkinter.END,todo)
        task_add.delete(0,tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Attention!!!",message="To add a task,please enter some task!")

def task_removing():
    try:
        index_todo = todo_box.curselection()[0]
        todo_box.delete(index_todo)
    except IndexError:
        tkinter.messagebox.showwarning(title="Attention!!", message="To delete a task, you must select a task!!")

def task_loading():
    try:
        todo_list = pickle.load(open("tasks.dat","rb"))
        list_frame.delete(0,tkinter.END)
        for todo in todo_list:
            list_frame.insert(tkinter.END,todo)
    except:
        tkinter.messagebox.showwarning(title="Attention!!",message="Cannot find task.data ")
  
def task_save():
    todo_list = todo_box.get(0, tkinter.END)
    pickle.dump(todo_list, open("tasks.dat", "wb"))


list_frame = tkinter.Frame(window) #frame where the added list will be kept
list_frame.pack()  #pack is used to apply all things written 

todo_box = tkinter.Listbox(list_frame,height=20,width=50)
todo_box.pack(side=tkinter.LEFT) #at which place we need box

#in case of long list we need the scroller

scroller = tkinter.Scrollbar()
scroller.pack(side=tkinter.RIGHT,fill=tkinter.Y)

#box for adding list
todo_box.config(yscrollcommand=scroller.set)
#scroller.config(command=list_frame.yview)

task_add = tkinter.Entry(window,width=70)   #box where we write what we want to add in list
task_add.pack()

#add button for add,delete task

add_task_button =tkinter.Button(window,text="CLICK TO ADD TASK",font=("arial",20,"bold"),background="blue",width=30,command=task_adding)
add_task_button.pack()

remove_task_button =tkinter.Button(window,text="CLICK TO DELETE TASK",font=("arial",20,"bold"),background="red",width=30,command=task_removing)
remove_task_button.pack()

load_task_button =tkinter.Button(window,text="CLICK TO LOAD TASK",font=("arial",20,"bold"),background="brown",width=30,command=task_loading)
load_task_button.pack()

save_task_button =tkinter.Button(window,text="CLICK TO SAVE TASK",font=("arial",20,"bold"),background="green",width=30,command=task_save)
save_task_button.pack()

window.mainloop()