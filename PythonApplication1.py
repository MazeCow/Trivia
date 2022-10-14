from ast import IsNot
from operator import is_not
from random import * 
import requests
from pprint import *
from termcolor import *
import json
import html

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
    print(colored("Category: ", "cyan"), "\n".upper(), "".ljust(1), colored(html.unescape(question['results'][0]['category']), "cyan"), "\n")
    if (html.unescape(question['results'][0]['difficulty'])) == "easy":
        difficultyRating = "green"
    if (html.unescape(question['results'][0]['difficulty'])) == "medium":
        difficultyRating = "yellow"
    if (html.unescape(question['results'][0]['difficulty'])) == "hard":
        difficultyRating = "red"
    print(colored("Difficulty: ", "cyan"), "\n".upper(), "".ljust(1), colored(html.unescape(question['results'][0]['difficulty']).upper(), difficultyRating), "\n")
    print(colored("Question: ", "cyan"), "\n".upper(), "".ljust(1), colored(html.unescape(question['results'][0]['question']), "cyan"), "\n")
    answers = []
    answers.append(html.unescape(question['results'][0]['correct_answer']).upper())
    for answer in question['results'][0]['incorrect_answers']:
        answers.append(html.unescape(answer).upper())
    

    shuffle(answers)
    answerNumbers = []
    x = list.index(answers, str(question['results'][0]['correct_answer']).upper())
    
    for answerNum in range(1, len(answers) + 1):
        answerNumbers.append(answerNum)
    count = 1
    for answer in answers:
        print("\t" + colored(f"({count}.)", "cyan") + colored(f"{answer}", "white"))
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
        input(colored("\tPress any key to continue . . .", "cyan"))
    else:
        print(colored("\n\tIncorrect!\n", "red"))
        print(colored(f"\tYou answered: {answers[answer]}", "red"))
        print(colored(f"\tThe correct answer was: {answers[x]}!\n", "red"))
        input(colored("\tPress any key to continue . . .", "cyan"))

print(colored("\nThanks for playing!", "green"))

