from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title('Mile to Km Converter')
window.config(padx=20, pady=20)



# Labels
label_ml = Label(text='Miles')
label_ml.grid(column=2, row=0)

label_km = Label(text='Km')
label_km.grid(column=2, row=1)

label_equal = Label(text='is equal to')
label_equal.grid(column=0, row=1)

label_res = Label(text='0')
label_res.grid(column=1, row=1)


# Buttons
def ml_to_km():
    miles = float(entry.get())
    km = round(miles * 1.609344)
    label_res.config(text=f"{km}")


# calls action() when pressed
button = Button(text="Calculate", command=ml_to_km)
button.grid(column=1, row=3)


# Entries
entry = Entry(width=10)
# Add some text to begin with
entry.insert(END, string="")

entry.grid(column=1, row=0)


window.mainloop()
