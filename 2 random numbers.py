#Program 2: Addition Trainer
#Create a program that automatically generate two random numbers to add (0 to 99)
#Let the user answer and evaluate if the user has the correct answer
#The program will ask the user 10 addition operation
#Display the result summary of the 10 operations (ex 9/10)


import random

score = 0

for x in range(10):
    first_number = random. randint(0,99)
    second_number = random. randint (0,99)
    print (f"Add these 2 number: {first_number} + {second_number}")
    User_answer = int(input("    Enter the answer here: "))
    answer = first_number + second_number

    if User_answer == answer:
        print ("Correct!")
        score = score + 1
    else:
        print (f"Incorrect, The right answer is {answer}")

print (f"Your score is {score}/10")