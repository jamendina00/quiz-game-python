print("Welcome To My Computer Quiz Game!")

playing = input("Do You Want To Play? ")


if playing.lower() != "yes":
    quit()

print("Okay Let's Play! :) ")
score = 0

#1
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect! ")
    print("The correct answer is 'central processing unit'.")

#2
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect! ")
    print("The correct answer is 'graphics processing unit'.")

#3
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect! ")
    print("The correct answer is 'random access memory'.")

#4
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect! ")
    print("The correct answer is 'power supply unit'.")

print("You Got " + str(score) + " Questions Correct!")
print("You Got " + str((score / 4) * 100) + "% Questions Correct!")