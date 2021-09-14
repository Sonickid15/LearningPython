#python calculator

#define variables
userIn = ''
numOne = 0
numTwo = 0
numAnswer = 0

#Body

print("Hello Welcome to my first python program, Please tell me wether you want to do "
        "addition, subtraction, multiplacation or division")
    
userIn = input()

#code for addition
if userIn == 'addition':
    print("Please put in two numbers")
    numOne = input()
    numTwo = input()
    print("Here are your two numbers added")
    numAnswer = float(numOne) + float(numTwo)
    print(numAnswer)

#code for subtracting
elif userIn == 'subtraction':
    print("Please put in two numbers in order (so num 1 - num 2)")
    numOne = input()
    numTwo = input()
    print("Here are your two numbers subtracted")
    numAnswer = float(numOne) - float(numTwo)
    print(numAnswer)

#code for multiplying
elif userIn == 'multiplication':
    print("Please put in two numbers")
    numOne = input()
    numTwo = input()
    print("Here are your two numbers multiplied")
    numAnswer = float(numOne) * float(numTwo)
    print(numAnswer)

#code for division
elif userIn == 'division':
    print("Please put in two numbers in order (so num 1/num 2)")
    numOne = input()
    numTwo = input()
    print("Here are your two numbers divided")
    numAnswer = float(numOne) / float(numTwo)
    print(numAnswer)