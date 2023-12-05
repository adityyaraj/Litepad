import tkinter as tk
from tkinter import filedialog as fd
tkt=tk.Tk()
icon_path="icon.ico"
tkt.iconbitmap(icon_path)
def new_file():
    en1.delete("1.0",tk.END)
    tkt.title("Litepad - New")
def open_file():
    file_path = fd.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            en1.delete("1.0", tk.END)
            en1.insert(tk.END, content)
        tkt.title(f"Litepad- {file_path}")

def save_file(event=None):
    global current_file_path
    if current_file_path:
        with open(current_file_path, 'w') as file:
            content = en1.get("1.0", tk.END)
            file.write(content)
        tkt.title(f"Litepad - {current_file_path}")
    else:
        save_as()


def save_as():
    global current_file_path
    file_path = fd.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        with open(file_path, 'w') as file:
            content = en1.get("1.0", tk.END)
            file.write(content)
        tkt.title(f"Litepad- {file_path}")
        set_current_file_path(file_path)

def set_current_file_path(file_path):
    global current_file_path
    current_file_path = file_path


def exitapp():
    tkt.destroy()
 
tkt.title("Litepad")
menu=tk.Menu(tkt)
tkt.config(bg="white",menu=menu)
tkt.geometry("800x600")
fm=tk.Menu(menu,tearoff=0)
menu.add_cascade(label="File",menu=fm)
fm.add_command(label="New",command=new_file)
fm.add_command(label="Open",command=open_file)
fm.add_command(label="Save",command=save_file)
fm.add_command(label="Save As",command=save_as)
fm.add_command(label="Exit",command=exitapp)
tkt.bind("<F5>",save_file)
en1=tk.Text(tkt)
en1.pack(expand=True,fill=tk.BOTH)
tkt.mainloop()