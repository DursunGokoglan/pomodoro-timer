from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
CHECKMARK = "✔"
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
BLUE = "#5fbdff"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
work_sec = WORK_MIN * 60
short_break_sec = SHORT_BREAK_MIN * 60
long_break_sec = LONG_BREAK_MIN * 60
reps = 0
timer = ""
remaining_count = 0
# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    info_label.config(text="TIMER", font=(FONT_NAME, 35, "bold"), bg=YELLOW, highlightthickness=0, fg=GREEN)
    global reps
    reps = 0

    stop_button.grid_forget()
    continue_button.grid_forget()
    start_button.grid(column=0, row=2)
    checkmark_label.config(text=CHECKMARK * (reps // 2), font=(FONT_NAME, 10, "bold"), bg=YELLOW, highlightthickness=0, fg=GREEN)


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer(*args):
    global reps
    reps += 1

    if args:
        reps -= 1
        count_down(args[0])
    else:
        if reps % 2 == 1:
            count_down(work_sec)
            info_label.config(text="WORK", font=(FONT_NAME, 35, "bold"), bg=YELLOW, highlightthickness=0, fg=GREEN)
        elif reps % 2 == 0 and reps % 8 != 0:
            count_down(short_break_sec)
            info_label.config(text="BREAK", font=(FONT_NAME, 35, "bold"), bg=YELLOW, highlightthickness=0, fg=GREEN)
        else:
            count_down(long_break_sec)
            info_label.config(text="BREAK", font=(FONT_NAME, 35, "bold"), bg=YELLOW, highlightthickness=0, fg=BLUE)

    checkmark_label.config(text=CHECKMARK * (reps // 2), font=(FONT_NAME, 10, "bold"), bg=YELLOW, highlightthickness=0, fg=GREEN)
    start_button.grid_forget()
    stop_button.grid(column=0, row=2)


def stop_timer():
    window.after_cancel(timer)
    stop_button.grid_forget()
    continue_button.grid(column=0, row=2)


def continue_timer():
    window.after(1000, start_timer, remaining_count)
    continue_button.grid_forget()
    stop_button.grid(column=0, row=2)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    global remaining_count
    remaining_count = count

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    count -= 1

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count)
    else:
        window.after(1000, start_timer)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

info_label = Label(text="TIMER", font=(FONT_NAME, 35, "bold"), bg=YELLOW, highlightthickness=0, fg=GREEN)
info_label.grid(column=1, row=0)

start_button = Button(text="Start", font=(FONT_NAME, 9, "bold"), bg=YELLOW, command=start_timer)
start_button.grid(column=0, row=2)

stop_button = Button(text="Stop", font=(FONT_NAME, 9, "bold"), bg=YELLOW, command=stop_timer)

continue_button = Button(text="Continue", font=(FONT_NAME, 9, "bold"), bg=YELLOW, command=continue_timer)

reset_button = Button(text="Reset", font=(FONT_NAME, 9, "bold"), bg=YELLOW, command=reset_timer)
reset_button.grid(column=2, row=2)

checkmark_label = Label(font=(FONT_NAME, 10, "bold"), bg=YELLOW, highlightthickness=0, fg=GREEN)
checkmark_label.grid(column=1, row=3)

window.mainloop()
