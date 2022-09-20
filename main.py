weight = input("Podaj swoją wagę: ")
height = input("Podaj swój wzrost w centrymetrach: ")

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

print(f"Twoje BMI to: {bmi}. To {message}")






# poniżej 16,0 – wygłodzenie
# 16,0–17,0 – wychudzenie (spowodowane często przez ciężką chorobę)
# 17–18,5 – niedowagę
# 18,5–25,0 – wartość prawidłową
# 25,0–30,0 – nadwagę
# 30,0–35,0 – I stopień otyłości
# 35,0–40,0 – II stopień otyłości
# powyżej 40,0 – III stopień otyłości (otyłość skrajna)