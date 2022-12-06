def bmi_calculator(height, weight):
    bmi = round(weight/(height**2),2)
    if bmi < 18.5:
        bmi_means = '過輕'
    elif bmi >= 18.5 and bmi < 24:
        bmi_means = '健康體位'
    elif bmi >= 24 and bmi < 27:
        bmi_means = '過重'
    elif bmi >= 27 and bmi < 30:
        bmi_means = '輕度肥胖'
    elif bmi >= 30 and bmi < 35:
        bmi_means = '中度肥胖'
    else:
        bmi_means = '重度肥胖'
    return bmi, bmi_means