from tkinter import *

def calculateBMI(weight, height):

    try:
        bmi = round(int(weight)/(int(height)/100)**2, 2)

        message = ""
        if bmi < 16:
             message = "wygłodzenie"
        elif bmi < 17:
             message = "wychudzenie"
        elif bmi < 18.5:
             message = "niedowaga"
        elif bmi < 25:
             message = "wartość prawidłową"
        elif bmi < 30:
             message = "nadwaga"
        else :
             message = "otyłość"

        output_label["text"]=f"Twoje BMI to: {bmi}. To {message}"
    except:
        output_label["text"]="Podaj poprawną wartóść!"


root = Tk()
root.title("Kalkulator BMI")

Grid.rowconfigure(root, 0, weight=1)
Grid.rowconfigure(root, 1, weight=1)
Grid.rowconfigure(root, 2, weight=1)
Grid.columnconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 1, weight=1)

window_width = 300
window_height = 200

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int((screen_width - window_width)/2)
center_y = int((screen_height - window_height)/2)

root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

weight_label = Label(text="Podaj wagę w KG: ")
height_label = Label(text="Podaje wzrost w CM: ")

weight_label.grid(column=0, row=0)
height_label.grid(column=0, row=1)

user_weight = Entry()
user_height = Entry()

user_weight.grid(column=1, row=0)
user_height.grid(column=1, row=1)

calculate_button = Button(text="Oblicz BMI", pady=5, command=lambda: calculateBMI(user_weight.get(), user_height.get()))

calculate_button.grid(column=0, row=3, columnspan=2)

output_label = Label()

output_label.grid(column=0, row=4, columnspan=2)



root.mainloop()
