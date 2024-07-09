# 1st input: Get height in meters e.g: 1.65
height = input("Enter your height in metres : ")
# 2nd input: enter weight in kilograms e.g: 72
weight = input("Enter your weight in kilograms : ")
float_weight = float(weight)
float_height = float(height)
numerator = float_weight
denominator = float_height * float_height
BMI = int(numerator/denominator)
print(f"Your BMI is {BMI}.")
