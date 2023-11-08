import tkinter as tk

# pack(), place() and grid() used to place item in screen
window = tk.Tk()
window.title("First GUI")
window.minsize(width=500, height=600)


# Label
my_label = tk.Label(text="This is new text")
# my_label.pack() #default to side = "top"
my_label.grid(column= 0, row= 0)

# input - text box
input = tk.Entry()
input.grid(column=4, row=2)

# button
def button_click():
    my_label['text'] = input.get()

btn1 = tk.Button(text="click me", command=button_click)
# we need to use this pack() show this on screen.
btn1.grid(column=1, row=1)




window.mainloop()