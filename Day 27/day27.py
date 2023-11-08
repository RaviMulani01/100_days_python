import tkinter as tk

window = tk.Tk()
window.title("First GUI")
window.minsize(width=500, height=600)


# Label
my_label = tk.Label(text="This is new text")
my_label.pack() #default to side = "top"

# button

def button_click():
    my_label['text'] = input.get()

btn1 = tk.Button(text="click me", command=button_click)
# we need to use this pack() show this on screen.
btn1.pack()


# input - text box
input = tk.Entry()
input.pack()

# input - big text
text = tk.Text(height=5, width=30)
# create curser to blink
text.focus()
text.pack()

# Spinbox
def spinbox_used():
    print(spinbox.get())

spinbox = tk.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

# scale
def scale_used(value):
    print(value)

scale = tk.Scale(from_=0, to=100, command=scale_used)
scale.pack()

# check-box button
def checkbutton_used():
    print(checked_state.get())

# store value
checked_state = tk.IntVar()
checkbox = tk.Checkbutton(text="Is on?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbox.pack()

# radio button
def radio_used():
    print(radio_state.get())

# store value
radio_state = tk.IntVar() 
radio_btn1 = tk.Radiobutton(text="option1", value=1, variable=radio_state,command=radio_used)
radio_btn2 = tk.Radiobutton(text="option2", value=2, variable=radio_state,command=radio_used)
radio_btn1.pack()
radio_btn2.pack()

# list box
window.mainloop()