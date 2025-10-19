questions= (("What is the latest version of Nvidia's Graphic card")
           ,("Which is the largest country in Asia")
           ,("Who is the president of USA")
           ,("What year did India won the cricket World cup"))

options= (("A.RTX 30 SERIES","B.RTX 40 SERIES","C.RTX 50 SERIES","D.RTX 20 SERIES")
         ,("A.Russia","B.India","C.China","D.Pakistan")
         ,("A.Trump","B.Joe Biden","C.Barack Obama","D.Hitler")
         ,("A.1940","B.2011","C.2001","D.2007"))

answer =("C","A","A","B")
guesses=[]
score = 0
question_num = 0

for question in questions:
    print("......................................")
    print(question)
    for option in options[question_num]:
        print(option)
    
    guess = input("Enter your Answer(A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answer[question_num]:
        score += 1
        print("CORRECT")
    else:
        print("INCORRECT")
        print(f"{answer[question_num]} is the correct answer")

    question_num += 1

print("............................")
print("          RESULT            ")
print("............................")

print("guesses: ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()


score = int(score/len(questions) * 100)
print(f"Your score is: {score}%")