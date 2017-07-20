#Jaye Sosa
#07-20-17

#Create a program that asks the user
#how many Fibonacci numbers to generate and then generates them

# 1 , 1 , 2 , 3 , 5 , 8 , 13 , 21

def fibonacci():

    #prompt user input for how many fibonacci numbers 
    number = int(input("How many fibonacci numbers would you like to generate? "))

    #set a counter to 1
    counter = 1

    #hard code cases where number = 0, 1, 2
    if number == 0:

        fib_num = []

    elif number == 1:

        fib_num = [1]

    elif number == 2:

        fib_num = [1,1]

    #if the number is larger than 2, hard code the first 2 numbers in the sequence
    #so the counter can sum the current index an the index previous to get the
    #value of the number after until the the counter reaches one before the user selected
    #fibonacci number       
    elif number > 2:

        fib_num = [1,1]

        while counter < (number-1):

            fib_num.append(fib_num[counter] + fib_num[counter - 1])

            counter += 1

    #return the list
    return fib_num

#print list
print(fibonacci())


            

            

    
