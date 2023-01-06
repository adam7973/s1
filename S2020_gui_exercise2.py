"""
Exercise "GUI step 2":

As always, read the whole exercise description carefully before you begin to solve the exercise.

Copy this file into your own solution directory. Write your solution into the copy.
use what you've learned in the GUI example files and build the GUI depicted in images/gui_2020.png

Reuse your code from "GUI step 1".

The GUI structure should be this:
    main window
        labelframe
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

import tkinter as tk


def clear_entry_boxes():
    entry_weight.delete(0, tk.END)
    entry_dest.delete(0, tk.END)
    entry_id.delete(0, tk.END)
    entry_weather(0, tk.END)


main_window = tk.Tk()
main_window.title("my first GUI")
main_window.geometry("500x150")

padx = 8
pady = 4

label_frame_1 = tk.LabelFrame(main_window, text="Container")
label_frame_1.grid(row=0, column=0, padx=padx, pady=pady, sticky=tk.N)

frame_1 = tk.Frame(label_frame_1)
frame_1.grid(row=0, column=0, padx=padx, pady=pady, sticky=tk.N)

frame_2 = tk.Frame(label_frame_1)
frame_2.grid(row=1, column=0, padx=padx, pady=pady, sticky=tk.N)

label_id = tk.Label(frame_1, text="Id")
label_id.grid(row=0, column=0, padx=padx, pady=pady)
entry_id = tk.Entry(frame_1, width=4)
entry_id.grid(row=1, column=0, padx=padx, pady=padx)

label_weight = tk.Label(frame_1, text="Weight")
label_weight.grid(row=0, column=1, padx=padx, pady=pady)
entry_weight = tk.Entry(frame_1, width=8)
entry_weight.grid(row=1, column=1, padx=padx, pady=padx)

label_dest = tk.Label(frame_1, text="Destination")
label_dest.grid(row=0, column=2, padx=padx, pady=pady)
entry_dest = tk.Entry(frame_1, width=15)
entry_dest.grid(row=1, column=2, padx=padx, pady=padx)

label_weather = tk.Label(frame_1, text="Weather")
label_weather.grid(row=0, column=3, padx=padx, pady=pady)
entry_weather = tk.Entry(frame_1, width=12)
entry_weather.grid(row=1, column=3, padx=padx, pady=padx)

button_create = tk.Button(frame_2, text="Create")
button_create.grid(row=0, column=0, padx=padx, pady=pady)

button_update = tk.Button(frame_2, text="Update")
button_update.grid(row=0, column=1, padx=padx, pady=pady)

button_del = tk.Button(frame_2, text="Delete")
button_del.grid(row=0, column=2, padx=padx, pady=pady)

button_clear = tk.Button(frame_2, text="Clear Entry Boxes", command=clear_entry_boxes)
button_clear.grid(row=0, column=3, padx=padx, pady=pady)

if __name__ == "__main__":
    main_window.mainloop()
