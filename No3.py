class BMI_Calculator:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height
    
    def BMI_Value(self):
        return self.weight / (self.height ** 2)

weight = float(input("Enter weight in kilograms: "))
height = float(input("Enter height in meters: "))

bmi_calculator = BMI_Calculator(weight, height)
bmi = bmi_calculator.BMI_Value()
print("BMI:", bmi)