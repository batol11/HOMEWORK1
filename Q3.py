#Question3
import csv
# Load the quiz questions from the CSV file
def load_questions(filename):
    questions = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            question = {
                'question': row[0],
                'answer': row[1]
            }
            questions.append(question)
    return questions
# Display the quiz questions and get user responses
def conduct_quiz(questions):
    score = 0
    for i, question in enumerate(questions, 1):
        print(f"Question {i}: {question['question']}")
        user_answer = input("Your answer: ")
        if user_answer.lower() == question['answer'].lower():
            score += 1
    return score
# Get user name
user_name = input("Enter your name: ")
# Load questions from the CSV file
questions = load_questions('quiz_questions.csv')
# Conduct the quiz
user_score = conduct_quiz(questions)
# Print the user's score
print(f"Dear {user_name}, your score is: {user_score}")
# Store user name and score in a CSV file
with open('user_results.csv', 'a', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow([user_name, user_score])


