import tkinter as tk

window = tk.Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_result.config(text=f"{km}")

miles_input = tk.Entry(width=7)
miles_input.grid(row=0, column=1)

miles_label = tk.Label(text="Miles")
miles_label.grid(row=0, column=2)

is_equal_label = tk.Label(text="is equal to")
is_equal_label.grid(row=1, column=0)

kilometer_result = tk.Label(text="0")
kilometer_result.grid(row=1, column=1)

kilometer_label = tk.Label(text="K.M")
kilometer_label.grid(row=1, column=2)

calculate_btn = tk.Button(text="Calculate", command=miles_to_km)
calculate_btn.grid(row=2,column=1)


window.mainloop()