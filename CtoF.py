#Change Celcius to Fahrenheit or vice versa

#get the degree and unit of degree from user
def user_input():
    CorF = input("Enter starting unit of temperature C or F? ").lower()
    degree = int(input("Enter starting unit of temperature. "))
    return CorF, degree

#Get the degree and unit from user_input() to do conversion
def conversion(CorF, degree):
    if CorF == 'c':
        #result = the final degree
        result = round(32 + 9/5 * degree, 2)
        print(f"{degree}C is {result}F")

    else:
        result = round(5/9 * (degree -32), 2)
        print(f"{degree}F is {result}C")

#define a tuple from user_input function
    #x = Corf= whatever the unit to convert with
    #y = degree
(x, y) = user_input()

#use a tuple previously defined tuple as an argument for conversion()
conversion(x, y)
