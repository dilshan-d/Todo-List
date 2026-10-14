import customtkinter as ctk
import tkinter as tk
import os

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Task Manager")
root.geometry("1000x750")
root.resizable(False, False)

task_list = []

def add_Task(event=None):
    task = taskEntry.get().strip()

    if task:
        listBox.insert(tk.END, task)
        task_list.append(task)

        with open("Tasklist.txt", "a") as file:
            file.write(task + "\n")

        taskEntry.delete(0, tk.END)
        update_count()


def delete_Task():
    selected = listBox.curselection()

    if not selected:
        return

    task = listBox.get(selected[0])

    listBox.delete(selected[0])
    task_list.remove(task)

    with open("Tasklist.txt", "w") as file:
        for item in task_list:
            file.write(item + "\n")

    update_count()


def get_Data():

    if not os.path.exists("Tasklist.txt"):
        open("Tasklist.txt", "w").close()
        return

    with open("Tasklist.txt", "r") as file:
        tasks = file.readlines()

        for task in tasks:
            task = task.strip()

            if task:
                listBox.insert(tk.END, task)
                task_list.append(task)

    update_count()


def update_count():
    countLabel.configure(text=f"{len(task_list)}")


header = ctk.CTkFrame(
    root,
    fg_color="transparent"
)
header.pack(fill="x", padx=40, pady=(30, 10))

title = ctk.CTkLabel(
    header,
    text="TASK MANAGER",
    font=("Segoe UI", 36, "bold")
)
title.pack(anchor="w")

subtitle = ctk.CTkLabel(
    header,
    text="Stay organized. Get things done.",
    font=("Segoe UI", 18),
    text_color="#9CA3AF"
)
subtitle.pack(anchor="w")

input_frame = ctk.CTkFrame(
    root,
    fg_color="transparent"
)
input_frame.pack(fill="x", padx=40, pady=20)

taskEntry = ctk.CTkEntry(
    input_frame,
    height=55,
    font=("Segoe UI", 16),
    placeholder_text="What do you need to do?"
)
taskEntry.pack(side="left", fill="x", expand=True)

taskEntry.bind("<Return>", add_Task)

addButton = ctk.CTkButton(
    input_frame,
    text="+  Add Task",
    width=180,
    height=55,
    font=("Segoe UI", 16, "bold"),
    command=add_Task
)
addButton.pack(side="left", padx=(20, 0))

taskCard = ctk.CTkFrame(
    root,
    corner_radius=20
)
taskCard.pack(
    fill="both",
    expand=True,
    padx=40,
    pady=10
)

taskHeader = ctk.CTkLabel(
    taskCard,
    text="All Tasks",
    font=("Segoe UI", 20, "bold")
)
taskHeader.pack(anchor="w", padx=20, pady=(20, 10))

listFrame = ctk.CTkFrame(
    taskCard,
    fg_color="#0F172A"
)
listFrame.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=(0, 20)
)

scrollbar = tk.Scrollbar(listFrame)
scrollbar.pack(side="right", fill="y")

listBox = tk.Listbox(
    listFrame,
    font=("Segoe UI", 14),
    bg="#0F172A",
    fg="white",
    selectbackground="#2563EB",
    selectforeground="white",
    borderwidth=0,
    highlightthickness=0,
    activestyle="none",
    yscrollcommand=scrollbar.set
)

listBox.pack(fill="both", expand=True)

scrollbar.config(command=listBox.yview)

footer = ctk.CTkFrame(
    root,
    corner_radius=20,
    height=90
)
footer.pack(
    fill="x",
    padx=40,
    pady=(0, 30)
)

leftSide = ctk.CTkFrame(
    footer,
    fg_color="transparent"
)
leftSide.pack(side="left", padx=25)

ctk.CTkLabel(
    leftSide,
    text="Total Tasks",
    font=("Segoe UI", 14),
    text_color="#9CA3AF"
).pack(anchor="w")

countLabel = ctk.CTkLabel(
    leftSide,
    text="0",
    font=("Segoe UI", 28, "bold")
)
countLabel.pack(anchor="w")

deleteButton = ctk.CTkButton(
    footer,
    text="🗑 Delete Selected Task",
    width=220,
    height=50,
    fg_color="#DC2626",
    hover_color="#B91C1C",
    font=("Segoe UI", 14, "bold"),
    command=delete_Task
)

deleteButton.pack(
    side="right",
    padx=20,
    pady=20
)

get_Data()

root.mainloop()