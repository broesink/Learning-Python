weight = float(input("What is your weight in kg? "))

height = float(input("What is your height in cm? "))

height_in_meter = height / 100

bmi = weight / (height_in_meter ** 2)

if bmi >= 30:
    category = "obesitas"
elif bmi >= 25:
    category = "overweight"
elif bmi >= 18.5:
    category = "normal"
else:
    category = "underweight"

print(f"BMI: {bmi:.2f}. You have a {category} BMI.")

