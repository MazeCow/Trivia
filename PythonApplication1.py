from ast import IsNot
from operator import is_not
from random import * 
import requests
from pprint import *
from termcolor import colored
import json

data_valid = False
while data_valid == False:
    qAmount = input(colored("How many trivia questions do you want?: ", "cyan"))
    try:
        qAmount = int(qAmount)
        if qAmount <= 0:
            print(colored("Invalid input!", "red"))
            continue
        data_valid = True
    except:
        print(colored("Invalid input!", "red"))
        continue

for i in range(qAmount):
    request = requests.get("https://opentdb.com/api.php?amount=1")
    question = json.loads(request.text)
    print(colored("Category: ", "cyan"), "\n".upper(), "".ljust(1), colored((question['results'][0]['category'].upper()), "white"), "\n")
    print(colored("Difficulty: ", "cyan"), "\n".upper(), "".ljust(1), colored((question['results'][0]['difficulty'].upper()), "white"), "\n")
    print(colored("Question: ", "cyan"), "\n".upper(), "".ljust(1), colored((question['results'][0]['question'].upper()), "white"))
    answers = []
    answers.append(question['results'][0]['correct_answer'].upper())
    for answer in question['results'][0]['incorrect_answers']:
        answers.append(answer.upper())
    

    shuffle(answers)
    answerNumbers = []
    x = list.index(answers, str(question['results'][0]['correct_answer']).upper())
    
    for answerNum in range(1, len(answers) + 1):
        answerNumbers.append(answerNum)
    count = 1
    for answer in answers:
        print("\t" + colored(f"({count}.)", "cyan") + colored(f" {answer}", "white"))
        count += 1

    data_valid = False
    while data_valid == False:
        answer = input(colored("\nWhat is your answer? (type #):", "cyan"))
        try:
            answer = int(answer)
        except:
            print(colored("Please select an available answer!", "red"))
            continue
        if answer in answerNumbers:
            pass
        else:
            print(colored("Please select an available answer!", "red"))
            continue
        data_valid = True

    answer -= 1
    if answers[x] == answers[answer]:
        print(colored("\n\tCorrect!\n", "green"))
    else:
        print(colored("\n\tIncorrect!\n", "red"))
        print(answers[x])
        print(answers[answer])
        print(colored(f"\tThe correct answer was {answers[x]}!\n", "red"))
        input("")

