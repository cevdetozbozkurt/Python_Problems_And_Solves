
weight = int(input("Please enter your Weight : "))
height = float(input("Please enter your Height (decimal) : "))


result_BMI = weight / (height ** 2)

if result_BMI < 18.5:
    print("Underweight")
elif result_BMI >= 18.5 and result_BMI < 25:
    print("Normal")
elif result_BMI >= 25 and result_BMI < 30:
    print("Overweight")
elif result_BMI >= 30:
    print("Obesity")