from tkinter import *

def calculateBMI(weight, height):

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

    return f"Twoje BMI to: {bmi}. To {message}"


root = Tk()
root.title("Kalkulator BMI")

weight_label = Label(text="Podaj wagę w KG: ")
height_label = Label(text="Podaje wzrost w CM: ")

weight_label.grid(column=0, row=0)
height_label.grid(column=0, row=1)

user_weight = Entry()
user_height = Entry()

user_weight.grid(column=1, row=0)
user_height.grid(column=1, row=1)

calculate_button = Button(text="Oblicz BMI")

calculate_button.grid(column=0, row=3, columnspan=2, command="")

output_label = Label()

output_label.grid(column=0, row=4, columnspan=2)
# weight = input("Podaj swoją wagę: ")
# height = input("Podaj swój wzrost w centrymetrach: ")
#
# bmi = round(int(weight)/(int(height)/100)**2, 2)
#
# message = ""
# if bmi < 16:
#     message = "wygłodzenie"
# elif bmi < 17:
#     message = "wychudzenie"
# elif bmi < 18.5:
#     message = "niedowaga"
# elif bmi < 25:
#     message = "wartość prawidłową"
# elif bmi < 30:
#     message = "nadwaga"
# else :
#     message = "otyłość"
#
# print(f"Twoje BMI to: {bmi}. To {message}")

root.mainloop()




# poniżej 16,0 – wygłodzenie
# 16,0–17,0 – wychudzenie (spowodowane często przez ciężką chorobę)
# 17–18,5 – niedowagę
# 18,5–25,0 – wartość prawidłową
# 25,0–30,0 – nadwagę
# 30,0–35,0 – I stopień otyłości
# 35,0–40,0 – II stopień otyłości
# powyżej 40,0 – III stopień otyłości (otyłość skrajna)