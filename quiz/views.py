from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Quiz


def quiz_page(request):
    quizes = Quiz.objects.all()
   
    return render(request, "quiz.html", {'quizes': quizes})


def quiz_answer(request, pk):
    answer = get_object_or_404(Quiz, pk=pk)
    if request.method == 'POST':
        messages.success(request, "Answer: ") 

    return render(request, "answer.html", {'answer': answer})