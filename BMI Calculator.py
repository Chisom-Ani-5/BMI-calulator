Name = input('Enter your name: ')

Height = float(input('Enter your height measurement in meters: '))

Weight = int(input(' Enter your weight in Kilograms: '))

BMI = Weight / (Height **2)
print(BMI)


if BMI <= 18.5 :
    print('You are underweight, fatten up!')

elif 24.9 > BMI > 18.6 :
    print('Your BMI is normal, keep it up')

elif 29.9 > BMI > 25 :
    print('You are overweight. Trim your size.')

else :
    print('You are obese. Speak to a Dietician urgently.')

users = {'Name': {
    'height' : Height, 'weight' : Weight, 'bmi' : BMI
    }
    }