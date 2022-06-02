# math_tutor_v2
#Owner- Jonel Azul
#Collaborator- Czarina Pielago

import random


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def dividiby(x, y):
    return x / y

while True:
    score = 0
    choice = input("Choose Operation (1- add, 2- sub, 3 -mult, 4 - divi): ")
    if choice in ('1', '2', '3', '4'):
        
        if choice == '1':
            question = int(input("How many problems?: "))
            total = question
            for i in range(question):
                num1 = float(random.randint(0, 9))
                num2 = float(random.randrange(2, 10, 2))
                num3 = add(num1, num2)
                print ("\nWhat is the sum of " + str(num1) + " and " + str(num2))
                answer = float(input ("Enter your answer: "))
                if num3 == answer:
                    score = score + 1
                    print("Correct")
                else:
                    print("Wrong, the answer is" , num3)
                question += 1
            print("\nScore: " + str(score) + "/" + str(total))
            

        elif choice == '2':
            question = int(input("How many problems?: "))
            total = question
            for i in range(question):
                num1 = float(random.randint(0, 9))
                num2 = float(random.randrange(2, 10, 2))
                num3 = subtract(num1, num2)
                print("\nWhat is the difference of " + str(num1) + " and " + str(num2))
                answer = float(input ("Enter your answer: "))
                if num3 == answer:
                    score = score + 1
                    print("Correct")
                else:
                    print("Wrong, the answer is" ,num3)
                question += 1
            print("\nScore: " + str(score) + "/" + str(total))    

        elif choice == '3':
            question = int(input("How many problems?: "))
            total = question
            for i in range(question):
                num1 = float(random.randint(0, 9))
                num2 = float(random.randrange(2, 10, 2))
                num3 = multiply(num1, num2)
                print("\nWhat is the product of " + str(num1) + " and " + str(num2))
                answer = float(input("Enter your answer: "))
                if num3 == answer:
                    score = score + 1
                    print("Correct")
                else:
                    print("Wrong, the answer is", num3)
                question += 1
            print("\nScore: " + str(score) + "/" + str(total))     
        
        elif choice == '4':
            question = int(input("How many problems?: "))
            total = question
            for i in range(question):
                num1 = round(float(random.randint(0, 9)), 2)
                num2 = round(float(random.randrange(2, 10, 2)),2)
                num3 = dividiby(num1, num2)
                print("\nWhat is the quotient of " + str(num1) + " and " + str(num2))
                answer = float(input("Enter your answer: "))
                if num3 == answer:
                    score = score + 1
                    print("Correct")
                else:
                    print("Wrong, the answer is", num3)
                question += 1
            print("\nScore: " + str(score) + "/" + str(total))
            
    try_again = input("Want to try again? (yes/no): ")
    if try_again == "no":
        break
else:
    print("Invalid Input")      