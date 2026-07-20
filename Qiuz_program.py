# A Program for quiz

questions=["1.Who is the G.O.A.T?",
           "2.Where is the Mt.Everest loacated?",
           "3.Fastest Memory: "]     # questions in list

options=(("A. Ronaldo","B.Messi","C.Bale"),
         ("A. India","B.China","C.Nepal"),
         ("A. Register","B.Cache","C.RAM"),) # using tuple (easy)

Answers=(("A"),("C"),("A"))
guess=[] 
score=0
ques_no=0
total = len(questions)  # Automatically count total questions

for question in questions:
    print(question)
    for option in options[ques_no]:
        print(option)
    user_guess=input("Enter (A,B,C):").upper()
    guess.append(user_guess)
   
    if user_guess ==Answers[ques_no]:
        score+=1
        print("Correct!")
    else:
        print("Wrong!!")    
    ques_no+=1
    print()

print("Thanks for playing quiz..")
print(f"You got: {score}/{total}")    
   