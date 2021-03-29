def bmi_grade_calculator(weight: float, height: float) -> str:
    bmi = weight / (height / 100) ** 2

    print('Your BMI is {:.2f}'.format(bmi))

    weight_range = 'It could not calculate your BMI grade'

    if bmi < 16:
        weight_range = 'Low weight grade III'
    elif bmi < 17:
        weight_range = 'Low weight grade II'
    elif bmi < 18.5:
        weight_range = 'Low weight grade I'
    elif bmi < 25:
        weight_range = 'Ideal weight'
    elif bmi < 30:
        weight_range = 'Overweight'
    elif bmi < 35:
        weight_range = 'Obesity grade I'
    elif bmi < 40:
        weight_range = 'Obesity grade II'
    else:
        weight_range = 'Obesity grade III'

    return weight_range

weight = float(input('Type your weight (kg): '))
height = float(input('Type your height (cm): '))
bmi_grade = bmi_grade_calculator(weight, height)

print('You are classified in the following BMI grade: {}'.format(bmi_grade))
