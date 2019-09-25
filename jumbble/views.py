from django.shortcuts import render, redirect
from random import *

words = [
    'python', 'java', 'javascript', 'nishant', 'akshay', 'shubham', 'sourabh', 'mongodb', 'sqlite'
]

message = ""


def randomwords():
    global jumbble_word, word
    word = choice(words)
    jumbble_word = "".join(sample(word, len(word)))


def index(request):
    randomwords()
    global jumbble_word, message
    return render(request, 'index.html', {'jumbble_word': jumbble_word, 'message': message})


def answer(request):
    answer = request.POST['answer']
    global word, jumbble_word, message
    if word == answer:
        message = "Correct"
        return redirect('index')
    else:
        message = "Try Again"
        return render(request, 'index.html', {'jumbble_word': jumbble_word, 'message': message})
