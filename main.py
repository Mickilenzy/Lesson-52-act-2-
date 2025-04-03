import random

def math_quiz() :
    score = 0 
    for _ in range(5): # A sk 5 questions
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operation = random.choice(["+", "-"])

        question = f"{num1} {operation} {num2}"
        answer = eval(question) # Calculate the correct answer 

        user_answer = input(f"Solve: {question} = ")

        if user_answer.isdigit() and int(user_answer) == answer:
              print(" ✅ Correct!\n")
              score += 1
        else:
            print(f"❌ Oops! The right  answer is {answer}\n")
            print(f" You scored {score}/5. well done!")

math_quiz()





       

