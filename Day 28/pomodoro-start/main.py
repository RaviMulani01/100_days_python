from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    reps = 0

    # enable start btn to start again
    start_btn.config(state=NORMAL)

    window.after_cancel(timer)
    # timer_text =  00:00
    canvas.itemconfig(timer_text, text="00:00")
    # timer_label = Timer
    timer_label.config(text="Timer")
    # reset checkmarks
    checkmark_label.config(text="")
   
 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():

    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_breke_sec = SHORT_BREAK_MIN * 60
    long_breke_sec = LONG_BREAK_MIN * 60

    # diable start btn to start again once timer start
    start_btn.config(state=DISABLED)

    # it it's the 8th rep:
    if reps % 8 == 0:
        timer_label.config(text="Brake", fg=RED)
        count_down(long_breke_sec)
    
    if reps%2 == 0:
        timer_label.config(text="Brake", fg=PINK)
        count_down(short_breke_sec)

    else:
        timer_label.config(text="Work", fg=GREEN)
          # if it's the 1st/3rd/5th/7th rep:
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):

    count_min = math.floor(count / 60)
    count_second = count % 60

    if count_second < 10:
        count_second = f"0{count_second}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_second}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)

    else:
        start_timer()
        mark = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            mark += "✔"
        checkmark_label.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #

# create window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# label
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 50))
timer_label.grid(row=0, column=1)

# canvas widget
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# btn
start_btn = Button(text="Start", highlightthickness=0, bg="white", command=start_timer)
start_btn.grid(row=2, column=0)

reset_btn = Button(text="Reset", highlightthickness=0, bg="white", command=reset_timer)
reset_btn.grid(row=2, column=2)

# label
checkmark_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
checkmark_label.grid(row=3, column=1)


window.mainloop()