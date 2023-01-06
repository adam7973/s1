"""
Exercise "GUI step 3":

As always, read the whole exercise description carefully before you begin to solve the exercise.

Copy this file into your own solution directory. Write your solution into the copy.
use what you've learned in the GUI example files and build the GUI depicted in images/gui_2030.png

Reuse your code from "GUI step 2".

The GUI structure should be this:
    main window
        labelframe
            frame
                treeview and scrollbar
            frame
                labels and entries
            frame
                buttons

Functionality:
    clicking on the button "clear entry boxes" deletes the text in all entry boxes

When your program is complete, push it to your github repository.
Then send this Teams message to your teacher: <filename> done
Thereafter go on with the next file.
"""

import os
import tkinter as tk
from tkinter import ttk


def empty_entry():
    entry_weight.delete(0, tk.END)
    entry_id.delete(0, tk.END)
    entry_weather.delete(0, tk.END)
    entry_dest.delete(0, tk.END)


padx = 8
pady = 4
rowheight = 24
treeview_background = "#eeeeee"
treeview_foreground = "black"
treeview_selected = "#773333"

main_window = tk.Tk()
main_window.title("my first GUI")
main_window.geometry("600x500")

# main_window.tk.call("lappend", "auto_path", os.path.join(os.getcwd(), "tkBreeze"))
# main_window.tk.call("package", "require", "breeze-dark")
main_window.tk.call(
    "source", os.path.join(os.getcwd(), "tkBreeze", "breeze", "breeze.tcl")
)

style = ttk.Style()
style.theme_use("breeze")
style.configure(
    "Treeview",
    background=treeview_background,
    foreground=treeview_foreground,
    rowheight=rowheight,
    fieldbackgound=treeview_background,
)
style.map("Treeview", background=[("selected", treeview_selected)])

label_frame_1 = ttk.LabelFrame(main_window, text="Container")
label_frame_1.grid(row=0, column=0, padx=padx, pady=pady, sticky=tk.N)

frame_1 = ttk.Frame(label_frame_1)
frame_1.grid(row=0, column=0, padx=padx, pady=pady, sticky=tk.N)

frame_2 = ttk.Frame(label_frame_1)
frame_2.grid(row=1, column=0, padx=padx, pady=pady, sticky=tk.N)

frame_3 = ttk.Frame(label_frame_1)
frame_3.grid(row=2, column=0, padx=padx, pady=pady, sticky=tk.N)

tree_1_scrollbar = ttk.Scrollbar(frame_1)
tree_1_scrollbar.grid(row=0, column=1, padx=padx, pady=pady, sticky="ns")
tree_1 = ttk.Treeview(frame_1, yscrollcommand=tree_1_scrollbar.set, selectmode="browse")
tree_1.grid(row=0, column=0, padx=padx, pady=pady)
tree_1_scrollbar.config(command=tree_1.yview)

tree_1["columns"] = ("col1", "col2", "col3")
tree_1.column("#0", width=0, stretch=tk.NO)
tree_1.column("col1", anchor=tk.E, width=90)
tree_1.column("col2", anchor=tk.W, width=130)
tree_1.column("col3", anchor=tk.W, width=180)

tree_1.heading("#0", text="", anchor=tk.W)
tree_1.heading("col1", text="Id", anchor=tk.CENTER)
tree_1.heading("col2", text="Weight", anchor=tk.CENTER)
tree_1.heading("col3", text="Destination", anchor=tk.CENTER)

label_id = ttk.Label(frame_2, text="Id")
label_id.grid(row=0, column=0, padx=padx, pady=pady)
entry_id = ttk.Entry(frame_2, width=4)
entry_id.grid(row=1, column=0, padx=padx, pady=pady)

label_weight = ttk.Label(frame_2, text="Weight")
label_weight.grid(row=0, column=1, padx=padx, pady=pady)
entry_weight = ttk.Entry(frame_2, width=8)
entry_weight.grid(row=1, column=1, padx=padx, pady=pady)

label_dest = ttk.Label(frame_2, text="Destination")
label_dest.grid(row=0, column=2, padx=padx, pady=pady)
entry_dest = ttk.Entry(frame_2, width=15)
entry_dest.grid(row=1, column=2, padx=padx, pady=pady)

label_weather = ttk.Label(frame_2, text="Weather")
label_weather.grid(row=0, column=3, padx=padx, pady=pady)
entry_weather = ttk.Entry(frame_2, width=12)
entry_weather.grid(row=1, column=3, padx=padx, pady=pady)

button_create = ttk.Button(frame_3, text="Create")
button_create.grid(row=0, column=0, padx=padx, pady=pady)

button_update = ttk.Button(frame_3, text="Update")
button_update.grid(row=0, column=1, padx=padx, pady=pady)

button_del = ttk.Button(frame_3, text="Delete")
button_del.grid(row=0, column=2, padx=padx, pady=pady)

button_clear = ttk.Button(frame_3, text="Clear Entry Boxes", command=empty_entry)
button_clear.grid(row=0, column=3, padx=padx, pady=pady)

if __name__ == "__main__":
    main_window.mainloop()
