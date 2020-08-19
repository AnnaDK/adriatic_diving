from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Quiz

from django.contrib import messages



def quiz_page(request):
    quizes = Quiz.objects.all()
   
    return render(request, "quiz.html", {'quizes': quizes})


def quiz_answer(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    if request.method == 'POST':
        messages.success(request, "Answer: ") 

    return render(request, "answer.html", {'quiz': quiz})







