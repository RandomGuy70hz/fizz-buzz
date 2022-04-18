# Fizz Buzz Program
import re # import regex package

def fizz_buzz(input):       # our fizz buzz function takes an input
	if input % 3 == 0:      # if input is evenly divided
		result = "Fizz"     # result is equal to Fizz
	else:                   # if input is not evenly divided
		result = "Buzz"     # result is equal to Buzz
	return result           # return the result  variable


def greet():                # main function called at start
    freshstart = True       # loop control variable
    print('Input a number') # print to console

    while(freshstart):      # while control is true
        number = input()    # store input as variable called number

        if re.match("[^\d]", number):       # if regex  matches input of non-integer
            print('Try Again')              # print 'Try Again'
        else:                               # if regex detects an integer
            print(fizz_buzz(int(number)))   # execute FizzBuzz function
            freshstart = False              # ends loop and stops program

# Main function call
greet() 
