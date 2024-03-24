weight = int(input())
height = float(input())

bmi = float(weight/(height**2))

if bmi<18:
    print(0)
elif 18<=bmi<25:
    print(1)
elif 25<=bmi<30:
    print(2)
elif 30<=bmi<40:
    print(3)
elif bmi>=40:
    print(4)