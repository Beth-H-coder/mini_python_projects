print("Welcome to my Quiz!")

playing = input("Do you want to play? (y/n) ")

if playing.lower() != "y":
    quit()

print("Let's play :)")
score = 0

answer = input("What is the name of the Bootcamp Course by Makers ")
if answer.lower() == "oracle":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is the name of Deloitte's centre focused on software development? ")
if answer.lower() == "capability centre":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("After training, how many months will the placement last? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Who is the best candidate? ")
if answer.lower() == "beth hughes":
    print('You bet she is!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("That's " + str(int((score / 4) * 100)) + "%.")